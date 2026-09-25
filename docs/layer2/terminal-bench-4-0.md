# Terminal-Bench 4.0

4.0 以 tag `v4.0.0` 为准。同日 `main` 是更晚的 `4def1f367467b34b18e0dbdc086400ba71c3e037`。论文摘要写的是 Terminal-Bench 2.0 的 89 题。

1. 一句话测什么。衡量 agent 在会随时间演进的多样化困难任务上能做到哪。4.0 在这套数据集上校准时间、CPU 和内存，修任务，并删掉饱和任务。出处是 tag `v4.0.0` 的 README，以及 https://www.tbench.ai/news/terminal-bench-4-0 。该 tag 的 `tasks/*/task.toml` 有 66 个，与 HF 卡上的 66 tasks 一致。

2. 官方源。入口 https://www.tbench.ai/news/terminal-bench-4-0 。仓库 https://github.com/harbor-framework/terminal-bench ，tag `v4.0.0` = commit `452bf305c6daa62fc59061d22133a7cbc7c1572e`（作者日期 2026-08-25 -0700，说明 “Add prebuilt image publishing for releases (#1811)”）。发布页 https://github.com/harbor-framework/terminal-bench/releases/tag/v4.0.0 （`published_at` 2026-08-26T04:48:12Z）。Harbor Hub https://hub.harborframework.com/datasets/terminal-bench/terminal-bench/4 。运行说明 https://www.tbench.ai/run 。论文 https://arxiv.org/abs/2601.11868 。HF `harborframework/terminal-bench`，Hub tag `v4.0.0`，Released 2026-08-26。

3. 形态。`task`、`dataset`、`environment`、`verifier`、`agent`。66 个 `tasks/*/task.toml`。发布说明的命令是 `harbor run -d terminal-bench/terminal-bench@4.0.0`。清单没有写出该 tag 上的 `dataset.toml` 路径，也没有写 `adapter`。

4. 与 Harbor 距离。原生可接。官方仓 tag `v4.0.0` 能指出 `tasks/*/task.toml`（66 个）。发布说明直接调用 `harbor run -d terminal-bench/terminal-bench@4.0.0`。

5. 环境。66/66 写 `environment_mode = "separate"`。模板 `docs/task-template.toml` 的注释写 verifier 在自己的容器里。66/66 有 `environment/Dockerfile`。66/66 的 `task.toml` 没有 `network_mode`。模板里有 `network_mode = "public"`，注释是 “Terminal-Bench is open internet”；这是模板，不是每题已写入的值。`batched-eval-parity` 和 `lake-temp-glm` 写了 `allow_internet = false`。其余 64 题没有写 `allow_internet`。`fp8-rmsnorm-gemm`、`jax-speedrun-gpu`、`math-eval-grader` 是 `gpus = 1` 且 `gpu_types = ["H100"]`；`jax-speedrun-gpu` 的 `[verifier.environment]` 同样是 1×H100。55 题 `gpus = 0`。8 题没有 `gpus` 键：`bun-sourcemap-leak`、`ctr-optimization`、`interleaved-vigenere`、`payments-pipeline-fix`、`production-planning`、`session-window-debug`、`shadow-relay`、`wal-recovery-ordering`。运行页写有任务需要 GPU，示例沙箱是 Modal。K8s 是 unknown。11 题有 `environment/docker-compose.yaml`，并且都有 `main` 以外的服务。公告把 agent timeout 写成 8 小时；抽到的 `[agent] timeout_sec = 28800.0`。

6. 评分。解题分由程序 verifier 写入 reward。论文 §2.1 写测试检查最终容器状态是否达到 instruction 里的结果。tag 上 63/66 的 `tests/test.sh` 含 `/logs/verifier/reward` 或 `reward.txt` / `reward.json`，其中 53 个脚本出现 `pytest`。`heat-pump-warranty` 与 `legacy-utility-triage` 调用 `tests/test_scoring.py`；`vba-userform-port` 用 pytest 跑 `test_scoring.py`。抽读的 `test_scoring.py` 把 0/1 写入 `reward.json`。`heat-pump-warranty`、`legacy-utility-triage`、`medical-claims-processing` 的 `verification_explanation` 写 deterministic、no LLM judge；`freight-dispatch-shift` 写 verifier 按固定步骤跑。未逐行审完 66 题全部测试文件。

7. agent/runtime。README 用 Harbor：`uv tool install 'harbor[modal]'`，示例 `--agent oracle`、`--agent claude-code`，`--env modal`。运行页示例是 `harbor run -d terminal-bench/terminal-bench@4.0.0 -e modal -a claude-code`。论文 §2.1 列举 Harbor 可接 Claude Code、Codex CLI、OpenHands、Mini-SWE-Agent 和 Terminus 2；该段写的是框架，不是 4.0 榜单的唯一 agent。

8. 迁入代价。低。tag 上已有 66 个 Harbor `task.toml`，发布命令就是 `harbor run`。跑全集时，3 题要 H100，11 题的 compose 还有额外服务；这是任务环境资源。清单没有要求再写一套 task 格式。

9. 对抽象的压力。`environment` 要同时接 separate verifier 容器、11 题的 compose 多服务，以及 3 题的 H100。8 题缺 `gpus`，64 题缺 `allow_internet`，清单写明不能从缺键推出运行时默认值。`verifier` 固定 `environment_mode = "separate"`。`agent` 超时是 8 小时，示例跑在 Modal。`dataset` 用 Hub 上的 `terminal-bench/terminal-bench@4.0.0`。清单没有给出该 tag 的 `dataset.toml` 路径。

10. 本地摘录。私有摘录未随公开手册发布。
