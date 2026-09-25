# terminal-bench-2-1

- slug: `terminal-bench-2-1`
- 抓取日: 2026-09-24 Asia/Shanghai

## 入口与官方仓

- 入口: https://github.com/harbor-framework/terminal-bench-2-1
- 官方仓: 同上。`git ls-remote HEAD` = `7131e4375048a0e408a8fb404b5f499d726b695b`。`git log -1` 为 2026-08-11 -0700，“Add notice that community submissions are currently closed (#202)”。default branch `main`。
- 同日 `git ls-remote --tags` 没有任何 tag。没有单独的 2.1 release tag；以当天 `main` 这个 commit 为准。
- 数据集页（README 链接，页面正文未抓）: https://hub.harborframework.com/datasets/terminal-bench/terminal-bench-2-1/latest
- 榜: https://www.tbench.ai/leaderboard/terminal-bench/2.1

## 论文 / blog / HF

- 论文: https://arxiv.org/abs/2601.11868 。摘要写的是 Terminal-Bench 2.0：89 个终端环境任务，每题有独立环境、人工解法和测试。README 的 bibtex 指向同一篇。
- blog: 没有单独的 2.1 公告页。项目站是 https://www.tbench.ai 。
- HF: README 没有把某个 dataset id 写成 2.1 本体。它说许多修改来自 https://huggingface.co/datasets/zai-org/terminal-bench-2-verified 。2.1 发布位置写的是 Harbor Hub，不是这个 HF 库。

## 测什么

README 写：Terminal-Bench 衡量 agent 在容器环境里完成有价值且复杂的任务的能力，例子包括组装待合成蛋白、调试 async 代码、处理安全漏洞；2.1 是 2.0 的更经核对的一版，改了 26 个任务（修 bug、改超时或资源、或降低 reward hacking）。（README @ `7131e437`）仓内 `tasks/*/task.toml` 有 89 个，与论文里 Terminal-Bench 2.0 的 89 题数量相同；README 没有写 2.1 增删了题数。

## 环境线索

- 容器: 有。89 个任务目录都有 `environment/Dockerfile`（树清单）。论文 §2.1：每题包含一个 Docker image，agent 在容器里做任务，测试被拷进容器执行。
- 出网: 89 个任务 `task.toml` 都是 `allow_internet = true`。另有 1 份排行榜 CI 模板 `leaderboard/src/leaderboard/ci/analysis-task-template/task.toml` 也是 `allow_internet = true`，它不在 `tasks/` 下。
- GPU: 89 个任务 `task.toml` 都写 `gpus = 0`。上述 CI 模板没有 `gpus` 键。没有看到 `gpu_types`。
- K8s: unknown。已检出的 md/toml/yaml/py/sh 中没有 `kubernetes` 或 `k8s`。
- 多容器: `mcmc-sampling-stan` 与 `rstan-to-pystan` 的 `task.toml` 有 `custom_docker_compose = true`，同时有 `moved_workdir_from_compose_to_dockerfile = true`。这两题当前树里没有 `docker-compose.yaml`，只有 `environment/Dockerfile`。全树里唯一的 `docker-compose.yaml` 在 CI 模板目录，不在 89 题里。89 题是否在运行时再拼多服务，未见 compose 文件，记 unknown。

## 评分

89/89 的 `tasks/*/tests/test.sh` 含 reward 字样。抽到的 `path-tracing-reverse/tests/test.sh` 跑 `pytest`，成功写 `/logs/verifier/reward.txt` 为 1，否则为 0。论文 §2.1：测试验证 instruction 描述的最终容器状态，不看 agent 命令或控制台输出。

另有一份 LLM judge，但是轨迹审查，不是这 89 题的解题分：`leaderboard/src/leaderboard/ci/analysis-task-template/task.toml` 的 description 为 “Judge whether trajectory {trial_id} exhibits harness-level cheating, task-level reward hacking, or refusal.”，keywords 含 `llm-judge`。

## agent / runtime

README 要求安装 Harbor，示例 `uv tool install "harbor[daytona]"`，提交命令是 `harbor run -d terminal-bench/terminal-bench-2-1 -a <agent> -m <provider/model> -e <sandbox> -k 5`。`-a` / `-e` 是占位符，README 没有指定唯一 agent。论文 §2.1 说 Harbor 支持 Claude Code、Codex CLI、OpenHands、Mini-SWE-Agent 和 Terminus 2；该句写的是框架，不是 2.1 榜单的唯一运行时。README 写明社区提交目前关闭，只有维护者跑的结果进榜。

## 体积与是否入 git

- GitHub API `size`（2026-09-24，KB）: 47186。
- 同日 `--depth 1` 完整克隆工作树约 108MB（`/tmp`，未放入 `/workspace`）。
- 本目录只留这份 `MANIFEST.md`。官方仓不入本仓库 git。

## 未能抓取

- Harbor Hub 数据集页和 tbench.ai 2.1 榜的正文没有抓取。
- 没有 tag，无法再钉一个不同于 `7131e437` 的发布 commit。
- `zai-org/terminal-bench-2-verified` 只按 README 记录为改动来源，没有下载该 HF 数据集。
- 两题的 `custom_docker_compose = true` 在当前树中没有对应 compose 文件，多容器运行形态 unknown。

MANIFEST-END
