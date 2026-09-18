"""Inspect a local video without changing it. Requires FFmpeg, ffprobe and Pillow.

Example: python audit_video.py input.mp4 --output audit-output --samples 16
The contact sheet supports visual review; it does not validate audio or lip sync.
"""
import argparse
import json
import math
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def run(command):
    result = subprocess.run(command, capture_output=True, encoding="utf-8", errors="replace")
    if result.returncode:
        raise RuntimeError(result.stderr[-2500:] or "Command failed")
    return result


def audit(source, output, samples):
    source = source.resolve(strict=True)
    if not source.is_file():
        raise ValueError("Input must be a local file")
    ffmpeg, ffprobe = shutil.which("ffmpeg"), shutil.which("ffprobe")
    if not ffmpeg or not ffprobe:
        raise RuntimeError("FFmpeg and ffprobe must be installed and on PATH")
    output.mkdir(parents=True, exist_ok=True)
    if any((output / name).exists() for name in ("metadata.json", "contact-sheet.jpg", "review-notes.md")):
        raise FileExistsError("Choose a fresh output directory to preserve an earlier audit")
    metadata = json.loads(run([
        ffprobe, "-v", "error", "-show_entries",
        "format=duration,size,bit_rate:stream=index,codec_name,codec_type,width,height,r_frame_rate,sample_rate,channels",
        "-of", "json", str(source)
    ]).stdout)
    if not any(s.get("codec_type") == "video" for s in metadata.get("streams", [])):
        raise ValueError("No video stream found")
    duration = float(metadata["format"]["duration"])
    if not math.isfinite(duration) or duration <= 0:
        raise ValueError("Video duration is unavailable or invalid")
    analysis = run([
        ffmpeg, "-hide_banner", "-nostdin", "-i", str(source),
        "-map", "0:v:0", "-an", "-vf", "blackdetect=d=0.15:pix_th=0.10",
        "-f", "null", "-"
    ])
    matches = re.findall(r"black_start:([\d.]+) black_end:([\d.]+) black_duration:([\d.]+)", analysis.stderr)
    black = [dict(zip(("start", "end", "duration"), map(float, m))) for m in matches]
    metadata["source_filename"] = source.name
    metadata["black_intervals"] = black
    metadata["blackdetect_settings"] = {"minimum_seconds": 0.15, "pixel_threshold": 0.10}
    last_sample = max(0, duration - min(0.10, duration / 2))
    timestamps = [i * last_sample / (samples - 1) for i in range(samples)]
    metadata["sample_times_seconds"] = timestamps
    cols, width, tile_h = 4, 400, 258
    sheet = Image.new("RGB", (cols * width, math.ceil(samples / cols) * tile_h), "#161a20")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default(size=19)
    with tempfile.TemporaryDirectory(prefix="video-audit-", dir=output) as scratch:
        for index, timestamp in enumerate(timestamps):
            frame = Path(scratch) / f"{index:03d}.jpg"
            run([ffmpeg, "-hide_banner", "-loglevel", "error", "-nostdin", "-y", "-ss", f"{timestamp:.6f}",
                 "-i", str(source), "-frames:v", "1", "-vf", "scale=640:-2", str(frame)])
            with Image.open(frame) as image:
                image.thumbnail((width - 8, 220))
                x, y = (index % cols) * width, (index // cols) * tile_h
                sheet.paste(image, (x + (width - image.width) // 2, y + 30 + (220 - image.height) // 2))
                draw.text((x + 10, y + 5), f"{timestamp:06.2f} s", font=font, fill="white")
    sheet.save(output / "contact-sheet.jpg", quality=92)
    (output / "metadata.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    intervals = "\n".join(f"- {v['start']:.3f}–{v['end']:.3f} s ({v['duration']:.3f} s)" for v in black) or "- None detected."
    notes = f"""# Video audit

Source: {source.name}
Duration: {duration:.3f} seconds

## Detected dark intervals

{intervals}

Dark intervals can be intentional. Inspect actual frames before editing.
The contact sheet is evenly sampled, not a shot-boundary detector.
Audio, lyrics, lip synchronization, temporal artifacts and artistic quality require separate review.
The source file was not modified.
"""
    (output / "review-notes.md").write_text(notes, encoding="utf-8")
    return {"duration_seconds": duration, "samples": samples, "black_intervals": black, "output": str(output.resolve())}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--samples", type=int, default=16)
    args = parser.parse_args()
    if not 2 <= args.samples <= 64:
        parser.error("--samples must be between 2 and 64")
    print(json.dumps(audit(args.input, args.output, args.samples), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
