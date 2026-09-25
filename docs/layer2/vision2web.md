# Vision2Web

沙箱把数据库、浏览器和 coding agent 装在同一个镜像里。功能分和视觉分都要另调模型。代码仓 README 写 CC-BY-NC-SA-4.0，HF 卡片写 apache-2.0，两处没有收成一个许可证结论。

1. 一句话测什么。测多模态编程智能体能否按 UI 原型和文字需求做出静态网页、交互式多页前端和全栈网站。193 题、16 类、918 张原型图、1,255 个测试用例。出处是 arXiv 2603.26648 摘要。该 commit 的 README 统计与摘要一致：webpage 100、frontend 66、website 27。

2. 官方源。仓库 https://github.com/zai-org/Vision2Web ，`main` HEAD `577f9397b3db8fc6d828adde254a830caa65d515`（2026-08-05，说明 “fix call_vlm async”）。GitHub `license` 字段为空。论文 https://arxiv.org/abs/2603.26648 。项目页 https://vision2web-bench.github.io/ 。README 新闻写 2026.04.30 被 ICML 2026 接收为 Spotlight。数据集 https://huggingface.co/datasets/zai-org/Vision2Web ，sha `8f03299d92b9bd852e93852d0c21e8a4848ab661`（2026-03-30，`gated` false）。该修订的 tree 是三个 `archives/*.tar.gz`，合计约 4.1 GB。卡片 YAML 还列了三个 `test.parquet`，这次拉到的 27 文件树里没有这些 parquet 路径。题目数据不在 git 里。

3. 形态。`dataset`、`environment`、`verifier`、`agent`。被测对象是 coding agent，跑在 sandbox 容器里。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。功能分和视觉分都要另调模型。清单没有给出 `task.toml` 或 `dataset.toml`。

5. 环境。`docker/build.sh` 构建 `vision2web-sandbox:latest`。`docker/Dockerfile.sandbox` 基于 `ubuntu:22.04`，在同一镜像里安装 PostgreSQL、Redis、nginx、SQLite、Node 20、Playwright/Chrome，以及 Claude Code、Codex、OpenHands。没有 docker-compose。每个 workspace 一个容器（`docker create … sleep infinity`）。`vision2web/core/sandbox.py` 的 `docker create` 没有 `--network none`，也没有 `--gpus`，并会把 proxy 环境变量传进容器。`scripts/run_evaluation.sh` 默认 `MAX_WORKERS=1`，参数可以加大，从而同时开多个同镜像容器。Postgres、Redis、nginx 装在这个镜像里面，不是旁路容器。构建镜像要出网。评测要打功能测试模型和视觉 judge 的 API。该 SHA 的文件名里没有 kubernetes、helm 或 k8s，记 unknown。沙箱本身未见 GPU。

6. 评分。要另调模型。README Step 4：功能分由 Claude Code 会话用 `playwright-cli` 按 `workflow.json` 跑，记录 Pass/Fail/Blocked；视觉分由 VLM judge 比较原型图和运行中截图。官方榜由维护者用当时的 VLM Judge 和 GUI Agent 重评，提交方只交推理产物。论文的利益声明写评测里的 GUI agent verifier 用的是 GLM-4.6V。该 SHA 的 README 新闻（2026.06.15）写功能测试改为 Claude Code + `playwright-cli`。两处说法都保留，没有合并成一个实现。

7. agent/runtime。`scripts/run_inference.sh` 的 `--framework` 取 `claude_code`、`codex` 或 `openhands`，跑在上面的 sandbox 里。功能测试本身也是一轮 Claude Code。单题默认超时 7200 秒。适配代码在 `vision2web/inference/adapters/`。

8. 迁入代价。高。沙箱 Dockerfile 公开，但没有 Harbor task 目录。HF 三个压缩包约 4.1 GB。功能和视觉两段评分都要模型密钥。论文里的 GLM-4.6V verifier 与当前 README 的 Claude Code verifier 不是同一句。

9. 对抽象的压力。`verifier` 的功能分和视觉分都来自另一个模型。`environment` 是单镜像里的多个进程，不是 compose 多服务。`agent` 在 sandbox 容器里，可选三套 CLI。`dataset` 的题面在 HF 压缩包，卡片 YAML 里的 parquet 路径这次 tree 没有出现。

10. 本地摘录。[`notes/sources/vision2web/MANIFEST.md`](../../notes/sources/vision2web/MANIFEST.md)。
