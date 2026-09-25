# Terminal-Bench 2.1

没有 git tag。下面的 commit 是抓取日的 `main`。论文摘要写的是 Terminal-Bench 2.0 的 89 题。

1. 一句话测什么。衡量 agent 在容器环境里完成有价值且复杂的任务的能力，例子包括组装待合成蛋白、调试 async 代码、处理安全漏洞。2.1 是 2.0 更经核对的一版，改了 26 个任务（修 bug、改超时或资源、或降低 reward hacking）。出处是 README @ `7131e437`。仓内 `tasks/*/task.toml` 有 89 个，与论文里 2.0 的题数相同。README 没有写 2.1 增删了题数。

2. 官方源。入口与仓库 https://github.com/harbor-framework/terminal-bench-2-1 ，`main` = `7131e4375048a0e408a8fb404b5f499d726b695b`（2026-08-11 -0700，说明 “Add notice that community submissions are currently closed (#202)”）。`git ls-remote --tags` 没有 tag。数据集页 https://hub.harborframework.com/datasets/terminal-bench/terminal-bench-2-1/latest （页面正文未抓）。榜 https://www.tbench.ai/leaderboard/terminal-bench/2.1 （正文未抓）。论文 https://arxiv.org/abs/2601.11868 。没有单独的 2.1 公告页。项目站 https://www.tbench.ai 。README 把许多修改的来源写成 https://huggingface.co/datasets/zai-org/terminal-bench-2-verified ，没有把某个 HF id 写成 2.1 本体。该 HF 数据集没有下载。

3. 形态。`task`、`dataset`、`environment`、`verifier`、`agent`。89 个 `tasks/*/task.toml`。README 的提交命令是 `harbor run -d terminal-bench/terminal-bench-2-1`。清单没有写出 `dataset.toml` 的路径，也没有写 `adapter`。

4. 与 Harbor 距离。原生可接。官方仓能指出 `tasks/*/task.toml`（89 个）。README 用 `harbor run -d terminal-bench/terminal-bench-2-1` 跑这个数据集。

5. 环境。89 个任务目录都有 `environment/Dockerfile`。论文 §2.1 写每题一个 Docker image，agent 在容器里做任务，测试被拷进容器执行。89 个 `task.toml` 都是 `allow_internet = true`，`gpus = 0`，没有 `gpu_types`。排行榜 CI 模板 `leaderboard/src/leaderboard/ci/analysis-task-template/task.toml` 也是 `allow_internet = true`，没有 `gpus` 键，它不在 `tasks/` 下。K8s 是 unknown。`mcmc-sampling-stan` 与 `rstan-to-pystan` 写了 `custom_docker_compose = true`，同时有 `moved_workdir_from_compose_to_dockerfile = true`；这两题当前树里没有 `docker-compose.yaml`。全树唯一的 `docker-compose.yaml` 在 CI 模板目录。89 题的多容器运行形态是 unknown。

6. 评分。89/89 的 `tasks/*/tests/test.sh` 含 reward 字样。抽到的 `path-tracing-reverse/tests/test.sh` 跑 pytest，成功写 `/logs/verifier/reward.txt` 为 1，否则为 0。论文 §2.1 写测试验证 instruction 描述的最终容器状态。另有一份轨迹审查：`leaderboard/src/leaderboard/ci/analysis-task-template/task.toml` 的 description 是判断轨迹是否有 harness-level cheating、task-level reward hacking 或 refusal，keywords 含 `llm-judge`。这份 judge 不给这 89 题打解题分。

7. agent/runtime。README 要求安装 Harbor，示例 `uv tool install "harbor[daytona]"`。提交命令是 `harbor run -d terminal-bench/terminal-bench-2-1 -a <agent> -m <provider/model> -e <sandbox> -k 5`。`-a` 和 `-e` 是占位符。论文 §2.1 写 Harbor 支持 Claude Code、Codex CLI、OpenHands、Mini-SWE-Agent 和 Terminus 2；该句写的是框架。README 写明社区提交目前关闭，只有维护者跑的结果进榜。

8. 迁入代价。低。89 个任务已有 Harbor `task.toml`，README 直接 `harbor run`。`gpus = 0`。清单没有写图形桌面。两题的 `custom_docker_compose = true` 在当前树里没有 compose 文件，多容器形态仍是 unknown。

9. 对抽象的压力。`environment` 是单份 Dockerfile，`allow_internet = true`，`gpus = 0`。两题的 compose 标志没有对应文件。`verifier` 把 0/1 写入 `reward.txt`。`agent` 由 `harbor run -a` 传入，README 没有指定唯一实现。`dataset` 用 Hub 名 `terminal-bench/terminal-bench-2-1`。轨迹审查的 `llm-judge` 在 leaderboard CI 模板里，和 89 题的解题分分开。

10. MANIFEST 路径。`notes/sources/terminal-bench-2-1/MANIFEST.md`
