# MANIFEST

- slug: `mls-bench-lite`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://github.com/Imbernoulli/MLS-Bench
- 官方仓: https://github.com/Imbernoulli/MLS-Bench
- commit: `80cf5c5cc8f70fb1b09f185e59ebf5eca04f610c`（`refs/heads/main`；`git ls-remote HEAD` 与 GitHub `commits/main` 一致；2026-09-18T17:09:07Z，说明 “Merge pull request #102 … Editable-scope fixes”）
- 标签: `git ls-remote --tags` 没有标签。`main` 以外还有多条 `agent/`、`fix/`、`mls-*` 分支，本文件只核实 `main`。
- 论文: arXiv:2605.08678（https://arxiv.org/abs/2605.08678）
- 站 / 榜: https://mls-bench.com ，Lite 榜 https://mls-bench.com/leaderboard
- HF: `Bohan22/MLS-Bench-Tasks`，dataset sha `b50fe197b609b1225ba296dbacd0dd1a45fb4cf4`，`lastModified` 2026-05-11T16:21:09.000Z。README 徽章指向这篇论文和 Docker Hub `bohanlyu2022`，HF 卡片指向同一 GitHub。该 HF snapshot 早于当前 `main`。
- 许可证: GitHub API 的 `license` 字段为空。

Lite 是全量 140 题里的 30 题子集，不是另一个仓。`harbor/run-modal-lite.yaml` 与 `harbor/run-daytona-lite.yaml` 用 `task_names` 点名这 30 题，README 写没有单独的 Lite 数据集目录。

## 测什么

测 AI 系统能否做出可迁移、可放大的 ML 方法改进，而不是只把一个固定实例调上去。出处：README 首段 “can an AI agent propose a new component, loss, optimizer, or training procedure whose gain transfers across settings, seeds, datasets, and scales?”，以及论文摘要 “MLS-Bench contains 140 tasks across 12 domains, each requiring an agent to improve one targeted component of an ML system or algorithm and demonstrate that the improvement generalizes across controlled settings and scales.”（https://arxiv.org/abs/2605.08678）。Lite 的定义在 README “MLS-Bench-Lite” 节：全量的 30 题子集，覆盖全部 12 个领域，用来更快比较模型。论文写全量约 704.7 H100-hours，Lite 约 99.2 H100-hours。

30 题 id 以 `harbor/run-modal-lite.yaml` 为准，与 README 表一致：`llm-dllm-demask-strategy`、`llm-pretrain-optimizer`、`llm-rl-importance-sampling`、`jepa-planning`、`robo-diffusion-guidance`、`robo-diffusion-policy`、`robo-humanoid-sim2real-algo`、`robomimic-bc-loss`、`rl-value-discrete`、`cv-3dgs-densification`、`cv-dbm-sampler`、`cv-vae-loss`、`llm-ptq-algorithm`、`llm-qat-algorithm`、`mlsys-sparse-attention-inference`、`ai4bio-mutation-effect-prediction`、`ai4sci-inverse-diffusion-algo`、`ai4sci-pla-binding-affinity`、`optimization-multi-objective`、`optimization-variance-reduction`、`ml-clustering-algorithm`、`ml-dimensionality-reduction`、`cv-pooling-aggregation`、`dl-activation-function`、`quant-concept-drift`、`ts-exogenous-forecast`、`ts-imputation`、`causal-discovery-discrete`、`graph-generation`、`security-membership-inference-defense`。Harbor 任务目录名是 `mls-bench__` 加这些 id。

## 环境

- 容器: README 写 runtime 可以是 Docker、Apptainer 或 local Conda（`container_runtime`）。Harbor 变体三份：`harbor/tasks-docker/`、`harbor/tasks-daytona/`、`harbor/tasks-modal/`。Dockerfile 形如 `FROM bohanlyu2022/mlsbench-harbor-<pkg>:latest`。
- 出网: 已读的 30 个 `harbor/tasks-docker/mls-bench__<id>/task.toml` 全部是 `allow_internet = true`。没有看到 agent allowlist 或 verifier 断网字段。
- GPU: 这 30 个 docker 变体 `task.toml` 里 26 题 `gpu_types = ["h100"]`，`gpus` 从 1 到 8（`cv-vae-loss` 为 8）。4 题 `gpus = 0`：`optimization-multi-objective`、`ml-clustering-algorithm`、`ml-dimensionality-reduction`、`causal-discovery-discrete`。`harbor/README.md` 写 GPU 题需要 NVIDIA Container Toolkit；Daytona/Modal 配置默认 `gpu_type: H100`。
- K8s: 没看到。调度器是 SLURM（配置里有 `slurm:` 时）或自带单机 GPU scheduler。`pyproject.toml` 提供 `mlsbench-sbatch` / `squeue` / `sacct` / `scancel`。
- 多容器: `tasks-docker` 的 `environment/docker-compose.yaml` 只有一个 service `main`。GPU 题在该 service 上加 nvidia device reservation 和 `shm_size: 16gb`；抽查的 CPU 题只有 `shm_size`。抽查 `tasks-modal/.../docker-compose.yaml` 返回 404，与 Harbor README “Daytona/Modal 变体没有 compose” 一致。

## 评分

确定性分数，不靠另一套 rubric judge。`harbor/README.md` 写每题用原生 `score_spec.py` 算出 `combined_score ∈ [0, 1]`，写入 `/logs/verifier/reward.txt`，原始指标在 `metrics.json`。越出可编辑范围则 reward 为 0。论文写 agent 工具是 `edit` / `test` / `submit` / `undo`，`test` 返回训练和可见测试指标。全量说明里有两题 evaluator 会调用 DeepSeek / DashScope（`agent-tool-reasoning`、`mas-topology`），它们不在上面的 30 个 Lite id 里，Harbor 全量配置写的是 138 道 non-API 题。

## agent / runtime

两条公开路径。原生路径是仓内 agent loop，`pip install -e ".[agent]"`，可选依赖含 `anthropic`、`openai`，另有 `openevolve` 和 `discover`。Harbor 路径用 `harbor run -c harbor/run-daytona-lite.yaml` 或 `run-modal-lite.yaml`。README 示例 agent 包括 `oracle`、`claude-code`、`codex`，并列出 `aider`、`swe-agent`、`opencode`、`openhands`、`gemini-cli`、`goose`。Harbor README 写 bundles 在 Harbor 0.6.6 和 0.22.0 上跑过，Modal 路径要求 Harbor ≥ 0.22。每题 `[agent] timeout_sec = 18000`（5 小时），Lite 榜按这个预算。agent 回路在 Harbor 进程或原生 `mlsbench` 进程，任务在 Docker / Daytona / Modal / Conda 环境里。

## 体积与是否入 git

GitHub API `size` = 30280 KB。没有整库克隆进 `/workspace`。本目录只留本文件和 `excerpts.md`，可以进 git。HF 上的 `sif/*.sif` 是预构建 Apptainer 镜像，未下载。

## 未抓取

- 整库与 Docker/Apptainer 镜像。仓的 GitHub size 已超过 5MB，镜像更大。
- HF `Bohan22/MLS-Bench-Tasks` 的 2201 个文件。`lastModified` 是 2026-05-11，早于当前 `main`，且含 `sif/`。
- `main` 以外分支的差异。
- 站点榜的分数表。只核实了榜 URL 写在 README 里。

MANIFEST-END
