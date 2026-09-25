# APEX–Agents

运行框架在 Archipelago。world、任务和 rubric 在 gated 的 Hugging Face 数据集。论文写 Environment、Agents、Grading 三个 Docker 容器；仓里的 compose 只声明 `environment` 一个服务。

1. 一句话测什么。测 agent 能否在带文件和工具的仿真工作环境里，完成投行分析师、管理顾问和公司律师编写的长程跨应用任务。出处是 https://huggingface.co/datasets/mercor/apex-agents 卡片，以及 arXiv 2601.14242 摘要。卡片写 480 个任务、33 个 world。

2. 官方源。数据集 https://huggingface.co/datasets/mercor/apex-agents ，Hub API `sha` `92c86856cf1b11f9833a8a076b3a45a63afa3929`（`lastModified` 2026-06-11，`gated` 为 `auto`，CC-BY-4.0）。运行与评分代码 https://github.com/Mercor-Intelligence/archipelago ，`main` HEAD `942d4bc6ba8ca788aac75a4a96a3c06e590b342a`（2026-09-24，说明从 `Mercor-io/studio@2356f19710efc058a1fb156c2c3880b609d102c6` 同步），Apache-2.0。论文 https://arxiv.org/abs/2601.14242 。`Mercor-io/studio` 不是本次核对到的公开仓。

3. 形态。`task`、`environment`、`verifier`、`agent`。公开示例才碰到 `dataset`，而且 gated。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。暂不宜接。题目 gated。评分要另调 judge。论文写三个容器。清单没有给出 `task.toml` 或 `dataset.toml`。

5. 环境。论文写三个组件都是 Docker 容器，并举 Kubernetes 和 Modal 当编排例子。该 commit 的 compose 文件没有 Kubernetes 清单。`environment/Dockerfile` 基镜像是 `debian:trixie-slim`。`environment/docker-compose.yml` 只启动一个名为 `environment` 的服务，端口 8080。`agents/`、`environment/`、`grading/` 各有 `.dockerignore`。基准内部关闭 web search，world 里要自带完成任务所需的文件。跑公开示例仍要从 Hugging Face 下任务，并调用模型 API。Environment 还能对 S3 做 populate / snapshot。已读的 Dockerfile 没有 nvidia 或 GPU 基镜像。GPU 记 unknown。

6. 评分。要另调模型。卡片写 judge model 对每条二元 criterion 独立打分，依据 prompt、agent 输出和相关产物。平均每题 4.06 条，范围 1–10。`grading/README.md` 的配置字段是 `llm_judge_model`，verifier 类型包含 `output_llm`。框架文字也允许静态 verifier；本基准公开说明使用的是 judge。

7. agent/runtime。论文写本基准的 agent harness 是 ReAct toolbelt，agent 通过统一 MCP gateway 使用 world 里的应用。Archipelago README 的默认实现名是 `react_toolbelt_agent`，同仓还有 loop、responses 等别的注册项。`examples/hugging_face_task/README.md` 写示例会下载 `mercor/apex-agents`、起 environment 容器、灌 world 快照、配 MCP、跑 agent、存快照、再 grading。该示例列出的 MCP 服务有 calendar、chat、code execution、spreadsheets、filesystem、mail、pdfs、presentations、documents。卡片另写部分 world 有额外金融数据应用；仓里有 `mcp_servers/edgar_sec` 和 `mcp_servers/fmp`。

8. 迁入代价。高。计分用的 world zip、`tasks_and_rubrics.json` 和 gold files 要先过 HF 门禁。Hub API `usedStorage` 20,093,539,877 字节，页面另写 Total file size 9.04 GB，两个数字没有文件级 size 可折成一个数。Archipelago 该 commit 的 blob 合计约 43 MB。评分还要 judge 模型。

9. 对抽象的压力。`dataset` 接不上可再分发的任务目录，题和 world 不公开下载。`verifier` 是按条二元的模型裁决。`environment` 在论文里是三个容器，仓内 compose 只声明一个服务。`agent` 是 `react_toolbelt_agent` 经 MCP 调用 world 里的应用。

10. 本地摘录。[`notes/sources/apex-agents/MANIFEST.md`](../../notes/sources/apex-agents/MANIFEST.md)。
