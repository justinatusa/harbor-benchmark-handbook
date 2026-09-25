# apex-agents

- slug：`apex-agents`
- 抓取日：2026-09-24 Asia/Shanghai
- 入口 URL：https://huggingface.co/datasets/mercor/apex-agents
- 官方仓 URL 与 commit SHA：
  - 数据集：https://huggingface.co/datasets/mercor/apex-agents 。Hub API `sha` 为 `92c86856cf1b11f9833a8a076b3a45a63afa3929`，`lastModified` 2026-06-11，`gated` 为 `auto`，许可 CC-BY-4.0。未登录 `git ls-remote` 被要求账号，没有用 git 再对一次。
  - 运行与评分代码：https://github.com/Mercor-Intelligence/archipelago ，`git ls-remote` HEAD `942d4bc6ba8ca788aac75a4a96a3c06e590b342a`（2026-09-24T08:32:12Z，提交说明写从 `Mercor-io/studio@2356f19710efc058a1fb156c2c3880b609d102c6` 同步）。默认分支 `main`。许可 Apache-2.0。论文脚注给出的就是这个 GitHub 地址。`Mercor-io/studio` 不是本次核对到的公开仓。
- 论文 / blog / HF id：
  - 论文：arXiv `2601.14242`，https://arxiv.org/abs/2601.14242 （读的是 v3 摘要页）。
  - HF：`mercor/apex-agents`。
  - Blog：Archipelago README 指向 http://mercor.com/blog/introducing-apex-agents 。本次没有逐段抓这篇博客。
- 一句话测什么：测 agent 能否在带文件和工具的仿真工作环境里，完成投行分析师、管理顾问和公司律师编写的长程跨应用任务。出处：HF 卡片与 arXiv `2601.14242` 摘要。
- 环境线索：
  - 容器：有。论文写 Environment、Agents、Grading 三个组件都是 Docker 容器。`environment/Dockerfile` 基镜像是 `debian:trixie-slim`。`environment/docker-compose.yml` 只启动一个名为 `environment` 的服务，端口 8080。
  - 出网：基准内部关闭 web search，论文和卡片都写这是为了可复现，world 里要自带完成任务所需的文件。跑公开示例仍要从 Hugging Face 下任务，并调用模型 API。Environment 还能对 S3 做 populate / snapshot。世界内的 web search 与 harness 访问 HF、模型和对象存储不是同一件事。
  - GPU：unknown。已读的 `environment/Dockerfile` 没有 nvidia 或 GPU 基镜像。
  - K8s：论文把 Kubernetes 和 Modal 写成这三份容器可以用的编排例子。该 commit 的 compose 文件没有 Kubernetes 清单。
  - 多容器：论文写三个 Docker 容器。仓里 `agents/`、`environment/`、`grading/` 各有 `.dockerignore`。compose 文件本身只声明 environment 一个服务。
- 评分：要另外的 judge 模型。卡片写 judge model 对每条二元 criterion 独立打分，依据 prompt、agent 输出和相关产物。平均每题 4.06 条，范围 1–10。Archipelago `grading/README.md` 的配置字段是 `llm_judge_model`，verifier 类型包含 `output_llm`。框架文字也允许静态 verifier；本基准公开说明使用的是 judge。
- agent / runtime 线索：论文写本基准的 agent harness 是 ReAct toolbelt，agent 通过统一 MCP gateway 使用 world 里的应用。Archipelago README 的默认实现名是 `react_toolbelt_agent`，同仓还有 loop、responses 等别的注册项。`examples/hugging_face_task/README.md` 写示例会下载 `mercor/apex-agents`、起 environment 容器、灌 world 快照、配 MCP、跑 agent、存快照、再 grading。该示例列出的 MCP 服务有 calendar、chat、code execution、spreadsheets、filesystem、mail、pdfs、presentations、documents。卡片另写部分 world 有额外金融数据应用；仓里有 `mcp_servers/edgar_sec` 和 `mcp_servers/fmp`。
- 体积与是否入 git：
  - 数据集：Hub API `usedStorage` 20,093,539,877 字节，319 个文件（含 `world_files_zipped` 33 个、`task_files` 222 个、`gold_files` 58 个，以及 `tasks_and_rubrics.json`、`world_descriptions.json`、`metadata.json`、`eval.yaml`）。HF 页面另写 Total file size 9.04 GB。两个数字都来自公开页或 API，本次没有文件级 size，不能把它们折成一个数。
  - Archipelago：GitHub API `size` 5540 KB；该 commit 递归 tree 的 blob size 合计 43,063,290 字节，4045 项。检出大于 5MB，没有克隆到 `/workspace`。
  - 数据集和 Archipelago 检出都不进本仓库 git。本目录只留 `MANIFEST.md` 与 `excerpt-runtime.txt`。
- 未抓取项与原因：
  - `tasks_and_rubrics.json`、world zip、gold files：gated，且数据集大于 5MB。
  - Archipelago 全树：blob 合计约 43MB，只抽了 README、compose、grading README、environment Dockerfile 首行和 HF 示例 README。
  - `Mercor-io/studio` 上的同步源提交：提交说明里出现，没有作为公开入口打开。
  - 博客正文：只记录了 README 上的 URL，没有另存全文。

同目录摘录：`excerpt-runtime.txt`。

MANIFEST-END
