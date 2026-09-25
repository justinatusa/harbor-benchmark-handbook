# MANIFEST

- slug: agents-last-exam
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://agents-last-exam.org/

## 官方仓

- 核实到的官方仓: https://github.com/rdi-berkeley/agents-last-exam
- 默认分支: main
- commit SHA: `d10fb61a14f9719774c3520c5763068b28ef5546`
- commit 说明: Merge pull request #21 from rdi-berkeley/feat/antigravity-cli
- committer 日期: 2026-09-04T03:02:10Z
- 仓库 `pushed_at`: 2026-09-20T10:50:16Z（默认分支 HEAD 仍是上面的 SHA）
- 许可证: 软件 Apache-2.0（`LICENSE`）；数据 CC-BY-4.0（`LICENSE-DATA`，覆盖 `tasks/`、`selected_tasks/`）
- GitHub API `size`: 24314 KB
- 该提交的递归树: 1547 个条目，`truncated=false`；blob 合计 28,998,885 字节
- 父提交里的 submodule gitlink（只记存在，没有再打开各 upstream 的说明）:
  - `ale_run/agents/codex/upstream`
  - `ale_run/agents/gemini_cli/upstream`
  - `ale_run/agents/grok_cli/upstream`
  - `ale_run/agents/hermes/upstream`
  - `ale_run/agents/openclaw_cli/upstream`
- `.gitmodules` 把这些指到 `cua-verse` 组织下的 fork，分支名 `agenthle`（grok_cli 那条没有写 branch）

## 论文 / blog / HF

- 论文: https://arxiv.org/abs/2606.05405 （v2，2026-06-11；HTML: https://arxiv.org/html/2606.05405v2）
- 网站: https://agents-last-exam.org/
- 排行榜（README 徽章）: https://agenthle.org/leaderboard
- 博客一篇，未当作任务定义: https://agents-last-exam.org/blogs/harness-matters
- 任务卡数据集: https://huggingface.co/datasets/agents-last-exam/agents-last-exam
- HF 修订: `ea617358e3c2e244d6f4d473c6a6a85d394bf90d`
- HF `lastModified`: 2026-09-19T17:46:08.000Z
- 文件: `README.md`、`release-v1.1.json`（175 字节）、`task_cards.parquet`（218,515 字节）
- 本地 Docker 用的任务包是另一个 gated 数据集: https://huggingface.co/datasets/agents-last-exam/agents-last-exam-data-archive
- 该数据集修订: `dedf6556c88f7dfd4fce891f9fa213e66584c71e`
- `gated`: manual
- 文件名: `ale-tasks-data.tar.gz`

## 测什么

测通用计算机使用代理能否完成长程、经济上有价值、结果可核验的专业工作。公开仓 README 写：55 个子领域、13 个行业簇，开放框架约 150 道公开任务。出处：该 README，以及 arXiv:2606.05405 摘要（论文写 1K+ 任务、最难档平均满分率低于 1%）。网站首页写已收集 1,500+ 题、目标 5,000。三处数字不是同一口径。

## 环境线索

- 容器: 有，而且不是唯一路径。README 的提供者表：Google Cloud VM（推荐）、AWS EC2、阿里云 ECS、QEMU/KVM、本地 Docker（较轻的 Ubuntu 子集）、已有的 CUA 沙箱。Docker 配置见 `excerpt-docker.yaml`：镜像 `agentslastexam/ale-ubuntu22-docker:latest`，无 GPU、无许可证的 Linux 子集。
- 出网: 编排器要访问云 API、Hugging Face 和模型 API。沙箱内部是否默认放行出站，`docker.yaml` 和 README 没有写成禁网或放行。论文写代理动作包括浏览器、shell、键鼠和 API。unknown。
- GPU: 论文附录写默认是 GCP `c4-standard-4`（4 vCPU、16 GB）。需要 GPU 的任务（例如 3D 渲染、仿真）用 `g2-standard-8` 加 NVIDIA L4。本地 Docker 这份配置写明 no-GPU。
- K8s: 评测编排不是 Kubernetes。仓里有 `env/packages-linux/helm-3.14.0`，以及任务 `tasks/computing_math/k8s_migration_1`、`k8s_payment_api_root_cause_analysis`。这是题目要装的软件和要做的事，不是评测平台本身。
- 多容器: 默认是每题一台 VM 或一个容器。`docker.yaml` 写四道题要在沙箱里再跑 Docker，两道要 Apptainer/Singularity，这两类应改走 QEMU，不在支持的 `docker_support.txt` 里。没有看到用 compose 把一道题拆成多个服务容器。

## 评分

主路径是确定性程序分，少数题要另外的 judge 模型。

README 写 hidden reference 加 deterministic graders，`evaluate()` 分数在 [0, 1]，参考答案在代理结束之后才放进环境。论文附录 C.3 写比较方式包括精确值、带容差的表、几何距离、行为状态、视觉和自由文本。同一附录的表 4 统计开源任务树：93.2% 是 code-based，6.8% 是 LLM-as-judge，后者主要是画面、截图、短视频上的是/否探针，由代码把答案合成分数。`docs/quickstart.md` 写 judge 类任务可以在 `secret/eval_time/` 放单独的 evaluator key；hello-world 不需要。本次没有打开各题 `main.py` 去点名 judge 模型。

## agent / runtime

有。框架包名 `agent-last-exam`，入口是 `ale_run`。`pyproject.toml` 依赖 `openenv-core==0.3.0`、`cua-bench==0.2.7`。README 写被测对象是自带循环的 harness（Claude Code、Codex、Openclaw 等），再用统一 CUA MCP 补上桌面动作。该提交下 `ale_run/agents/` 有这些适配目录：`ale_claw`、`antigravity_cli`、`codex`、`cursor_cli`、`droid`、`forgecode`、`gemini_cli`、`grok_build`、`grok_cli`、`hermes`、`octavus_cli`、`openclaw_cli`、`openhands_cli`、`terminus_2`。in-sandbox 的 CLI 注入虚拟机；out-of-sandbox 的 harness 在 ALE 进程里通过 MCP 遥控。论文写单次运行上限 5 小时。

## 体积与是否入 git

框架仓 blob 合计约 29.0MB，其中 `assets/teaser.pdf` 14,539,619 字节、`assets/teaser.png` 4,624,162 字节。大于 5MB，没有克隆进 `/workspace`。

任务卡 HF 仓 `usedStorage` 3,610,565 字节，未下载 parquet。

gated 数据包 HF API `usedStorage` 217,212,747,241 字节（约 202 GiB）。未申请、未下载。

本目录只有本文件和 `excerpt-docker.yaml`。本次没有 git commit。

## 未抓取项与原因

- `ale-tasks-data.tar.gz`：gated，且约 202 GiB。`scripts/fetch_task_data.sh` 写明要先申请 https://huggingface.co/datasets/agents-last-exam/agents-last-exam-data-archive 。
- 五个 upstream submodule 的源码：父提交有 gitlink，没有再克隆。
- 每题 `evaluate()` 和 LLM judge 的具体模型名：开源树有 1000+ 文件，本次只核实了框架说明、论文附录的 93.2% / 6.8% 比例和 Docker 配置。
- 云镜像 `agenthle-488519` 上的 `ale-ubuntu22` / `ale-win10`，以及 Docker Hub 镜像的 digest：没有拉取。
- 网站写 1,500+ 已收集题、论文写约 1,490 instances、README 写约 150 道公开题。未公开的那部分没有 URL。

MANIFEST-END
