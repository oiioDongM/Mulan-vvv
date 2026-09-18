# GitHub 新手操作：用木兰项目学会第一次存档

## 四个概念

| 名称 | 对你的用途 |
|---|---|
| GitHub | 在线存放、查找、协作和追踪项目版本的平台 |
| Repository / Repo，仓库 | 你命名的 **Mulan vvv** 项目库：[oiioDongM/Mulan-vvv](https://github.com/oiioDongM/Mulan-vvv) |
| Commit，提交 | 一次带说明的存档，例如“锁定木兰主脸和红衣造型” |
| Skill | 给 AI 反复执行的制作规程；由 SKILL.md、参考和可选脚本组成 |

“蒸馏 Skill”在这里指把有效经验提炼成可复用步骤、输入、判断标准和工具调用，不是训练 Seedance 的模型权重。GitHub 本身也不提供 Seedance 的生成算力。

## 在已有仓库里开始

项目仓库为 [oiioDongM/Mulan-vvv](https://github.com/oiioDongM/Mulan-vvv)，主分支为 `main`。创作者已明确选择保持公开，并授权上传这份制作包。

教学方式：用户亲自操作，助手负责材料准备、检查状态和图文指导。当前远程仓库已创建并可访问，仍为空仓库，首次上传尚待用户完成。

## 第一次上传：先到文件预览这一步

1. 在“陆东西”的 Chrome 打开仓库首页。
2. 空仓库页面在 Quick setup（快速设置）区域寻找 **uploading an existing file（上传现有文件）**；如果已有文件，则使用 **Add file → Upload files**。
3. 解压本地制作包，打开里面的 `mulan-visual-lab` 文件夹，选中 README.md、.gitignore、docs、skills、templates 共 5 项，拖到上传区。它们合计包含 10 个文件，目录层级应保留。
4. 在提交前核对列表：README.md 位于仓库根目录，docs 下 4 篇文档，skills 下 3 个文件，templates 下 1 个 JSON，再加 .gitignore。提交的是这些文件，不是 ZIP 压缩包本身。
5. 将文件列表截图交给助手核对。本次练习先理解预览页，再学习填写提交说明和保存版本。

当前仓库为公开状态。选择文件时只包含已经准备公开的制作包文档与脚本，原始音视频、登录凭据和私人文件单独保管。

1. 打开仓库首页，向下滚动阅读 README，即项目入口说明。
2. 点击 `docs` 文件夹，查看素材诊断、24 秒分镜、提示词和来源记录。
3. 点击 `skills/mulan-hiphop-video/SKILL.md`，查看供 AI 使用的制作规程。
4. 点击 `templates/shot-log.json`，查看镜头队列；每次实测后补充结果、费用和问题。
5. 首页通过 **Code → Download ZIP** 下载当前版本；需要回看改动时查看文件的 **History**。

## 以后如何添加文件

在已有仓库选择 **Add file → Upload files**，拖入要新增或更新的文档，保持目录结构，填写清楚的提交说明，再保存。无需重新建仓库。网页上传不等于在本机安装 Skill。

如果仓库访问失效，从当前使用的 GitHub 插件设置进入管理仓库，核对 Mulan-vvv 是否在授权范围；不要仅根据应用名称选择第三方同名产品。[OpenAI 连接说明](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt)

教程依据：[GitHub 入门](https://docs.github.com/en/get-started/using-github/hello-world)、[网页上传文件](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)。网页上传单文件上限 25 MiB；本起步包只有文字、JSON 和脚本。

本项目建议 GitHub 保存：人物规则、分镜、提示词、生成日志、辅助脚本。MP4、WAV、大尺寸原图先保存在本机或你惯用的素材盘，仓库中记录素材编号和位置。`.gitignore` 对本机 Git 生效；网页拖拽上传仍需自己确认文件。不要把登录凭据写进项目。

## 第二次使用：改一个文件

打开 `docs/02-24秒分镜与即梦提示词.md`，点编辑，将一次实测有效的提示词更新进去；提交说明写清楚“把系发带改为松手，减少手指穿模”。提交历史会告诉你何时、为什么改过。Skill 应从这些证据中改进。

Branch（分支）可以理解为另开一个试验版本；Pull Request 是把试验版本与正式版本对照审阅；Merge 是把已接受的修改合并。第一天会“创建、上传、编辑、提交、查看历史”就够了，不需要先学编程或命令行。

## Skill 如何安装

GitHub 上保存不等于 Codex 已启用。项目 `skills/mulan-hiphop-video` 可以复制为本地项目下 `.agents/skills/mulan-hiphop-video`，然后在 Codex 中打开该项目使用。也可以让 Codex 帮你安装到它当前环境的个人 Skill 目录。只选一个范围，避免个人与项目重复安装同名 Skill。

本次另外按当前环境的 Skill 创建规范，把同一版本放入了个人 Skill 目录；项目中的副本用于公开分享和版本管理。若列表没有刷新，可重新打开 Codex 后选择，或直接让 AI 读取本包的 SKILL.md。[官方 Skill 文档](https://developers.openai.com/codex/skills/)

## 本次查过哪些开源项目

| 项目 | 实际作用 | 你现在要不要安装 |
|---|---|---|
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | 探测媒体信息、抽帧、转码、检测黑场；本机已使用 | 暂不需要另装 |
| [PySceneDetect](https://github.com/Breakthrough/PySceneDetect) | 自动找镜头切点，便于处理较长参考片 | 等有完整参考片和更多镜头时再用 |

两者是媒体工具，不是风格模型。我们已通过 GitHub 读取官方 README，没有安装来源不明的“一键 MV 神器”。可先看 README 是否有实际输入输出、安装条件、许可证和最近维护记录，再决定是否引入。
