# mls-bench-lite 摘录

抓取日 2026-09-24 Asia/Shanghai。树：`80cf5c5cc8f70fb1b09f185e59ebf5eca04f610c`。

## Lite 定义

来源：同提交 `README.md` “MLS-Bench-Lite” 节。

“MLS-Bench-Lite is a 30-task subset of the full 140-task suite, spanning all 12 research domains.”

同页写没有单独 Lite 目录，`run-daytona-lite.yaml` 用 `task_names` 点名 30 题。

## 运行时

来源：同提交 `README.md` Installation。

“Runtime backends: Docker, Apptainer, or local Conda”。“Job schedulers: SLURM … or the built-in single-node GPU scheduler.”

## Harbor 评分

来源：同提交 `harbor/README.md` Scoring。

“Each task uses MLS-Bench's native `score_spec.py` declaration to compute a single `combined_score ∈ [0, 1]` written to `/logs/verifier/reward.txt`.”

## Lite 30 题 docker 变体资源

来源：同提交 `harbor/tasks-docker/mls-bench__<id>/task.toml`，30 个都拉过。全部 `allow_internet = true`。

`gpus = 0`：`optimization-multi-objective`、`ml-clustering-algorithm`、`ml-dimensionality-reduction`、`causal-discovery-discrete`。

其余 26 题 `gpu_types = ["h100"]`。`gpus` 最高是 `cv-vae-loss` 的 8。

`cv-vae-loss` 的 `environment/docker-compose.yaml` 只有 service `main`，nvidia count 8，`shm_size: 16gb`。`ml-clustering-algorithm` 的 compose 只有 `main` 和 `shm_size`。
