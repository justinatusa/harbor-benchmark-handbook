# MLS-Bench-Lite

Lite 是全量 140 题里的 30 题子集。清单写这些 Harbor 目录在 0.6.6 和 0.22.0 上跑过，没有写成 0.23.0。

1. 一句话测什么。测系统能否做出可迁移的机器学习方法改进。Lite 是全量里的 30 题子集，覆盖全部 12 个领域。出处是仓库 README 的 “MLS-Bench-Lite” 节，以及 https://arxiv.org/abs/2605.08678 摘要。论文写 Lite 约 99.2 H100-hours。

2. 官方源。仓库 https://github.com/Imbernoulli/MLS-Bench ，commit `80cf5c5cc8f70fb1b09f185e59ebf5eca04f610c`（2026-09-18，说明 “Merge pull request #102 … Editable-scope fixes”）。`git ls-remote --tags` 没有标签。论文 https://arxiv.org/abs/2605.08678 。站 https://mls-bench.com ，榜 https://mls-bench.com/leaderboard 。HF `Bohan22/MLS-Bench-Tasks`，dataset sha `b50fe197b609b1225ba296dbacd0dd1a45fb4cf4`，`lastModified` 2026-05-11，早于当前 `main`。

3. 形态。`task`、`environment`、`verifier`、`agent`、`dataset`。Lite 的 30 个 docker 变体是 `harbor/tasks-docker/mls-bench__<id>/task.toml`。三份名单是 `harbor/tasks-docker/dataset.toml`、`harbor/tasks-modal/dataset.toml`、`harbor/tasks-daytona/dataset.toml`，各 140 条，没有单独的 Lite `dataset.toml`。Lite 的点名在 `harbor/run-modal-lite.yaml` 与 `harbor/run-daytona-lite.yaml` 的 `task_names`。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。轻适配。清单写了这 30 个 `task.toml` 路径。Harbor README 写 bundles 在 Harbor 0.6.6 和 0.22.0 上跑过，Modal 路径要求 Harbor ≥ 0.22。没有写成 Harbor 0.23.0。没有 git tag。

5. 环境。README 写 runtime 可以是 Docker、Apptainer 或 local Conda。Harbor 变体是 Docker、Daytona、Modal。已读的 30 个 docker `task.toml` 全部是 `allow_internet = true`。26 题 `gpu_types = ["h100"]`，`gpus` 从 1 到 8。4 题 `gpus = 0`：`optimization-multi-objective`、`ml-clustering-algorithm`、`ml-dimensionality-reduction`、`causal-discovery-discrete`。`tasks-docker` 的 `environment/docker-compose.yaml` 只有一个 service `main`。Kubernetes 没看到。

6. 评分。程序算出的分数，不靠另一套 rubric judge。每题用原生 `score_spec.py` 算出 `combined_score`，写入 `/logs/verifier/reward.txt`。越出可编辑范围则 reward 为 0。全量里有两题 evaluator 会调用外部模型接口，它们不在这 30 个 Lite id 里。

7. agent/runtime。原生路径是仓内 agent loop。Harbor 路径用 `harbor run`，示例 agent 包括 `oracle`、`claude-code`、`codex`。每题 `[agent] timeout_sec = 18000`（5 小时）。agent 回路在 Harbor 进程或原生 `mlsbench` 进程，任务在 Docker、Daytona、Modal 或 Conda 环境里。

8. 迁入代价。低。30 个 docker 变体已有 `task.toml`。跑过的 Harbor 版本不是 0.23.0。多数题要显卡，并且 `task.toml` 允许出网。

9. 对抽象的压力。`environment` 要显卡，并且 `task.toml` 允许出网。`verifier` 把程序算出的分数写入 reward 文件。`dataset` 没有单独的 Lite 名单，Lite 用 `harbor/run-modal-lite.yaml` 与 `harbor/run-daytona-lite.yaml` 的 `task_names`。`agent` 可以走仓内循环，也可以走 Harbor 的 agent。

10. 本地摘录。[`notes/sources/mls-bench-lite/MANIFEST.md`](../../notes/sources/mls-bench-lite/MANIFEST.md)。
