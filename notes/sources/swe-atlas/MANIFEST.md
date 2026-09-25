# MANIFEST

- slug: `swe-atlas`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://github.com/scaleapi/SWE-Atlas
- 官方仓: https://github.com/scaleapi/SWE-Atlas
- commit: `49e4af3b6c803dd54a1cd60ead703aac25de4e21`（`main`；`git ls-remote HEAD` 与 GitHub `commits/main` 一致；2026-08-20T19:09:41Z，说明 “Merge pull request #20 … TW: provision uv and Python 3.11 in the simple-login task images”）
- 标签: `git ls-remote --tags` 没有标签。
- 论文: arXiv:2605.08366（https://arxiv.org/abs/2605.08366）
- blog: https://scale.com/blog/swe-atlas-complete
- 榜: https://labs.scale.com/leaderboard/sweatlas-qna 、https://labs.scale.com/leaderboard/sweatlas-tw 、https://labs.scale.com/leaderboard/sweatlas-refactoring
- HF: 没有。钉死 README 没给 dataset id。

同一产品，三轨分开记。钉死树上 `data/qa` 124 题、`data/tw` 90 题、`data/rf` 70 题，与论文摘要的 124 / 90 / 70 一致。`data/qa/dataset.toml` 名是 `scale-ai/swe-atlas-qna`，`data/tw/dataset.toml` 存在。`data/rf` 70 个目录，没有 `dataset.toml`。

## 测什么

测 coding agent 在专业软件工程流程里的表现，范围是 Codebase Q&A、Test Writing、Refactoring，而不只是修 issue。出处：论文摘要 “We introduce SWE Atlas, a benchmark suite for coding agents spanning three professional software engineering workflows: Codebase Q&A (124 tasks), Test Writing (90 tasks), and Refactoring (70 tasks).”（https://arxiv.org/abs/2605.08366）。

### Codebase QnA

在真实仓库里回答开发者上手、架构、运行时异常或安全审查类问题，题面要求探索代码并跑起来再答。出处：论文 2.1.1。124 题全部 `gpus = 0`，`allow_internet = true`，`task.toml` 没有 `network_mode`，都有 `docker_image`（示例 `ghcr.io/scaleapi/swe-atlas:swe_atlas_QnA_Automattic_wp-calypso_1.0`）和一份很短的 `Dockerfile`。评分是 rubric，全部 must-have，全过才算过。出处：论文 2.1.1 Evaluation。抽查 `data/qa/task-6905333b74f22949d97ba998/tests/test.sh` 调用 `evaluate_answer.py`。`[verifier.env]` 默认 `EVAL_MODEL` 为 `anthropic/claude-opus-4-5-20251101`，走 `OPENAI_API_KEY` / `OPENAI_API_BASE`。要另外的 judge 模型。

### Test Writing

给一个高层行为描述，agent 自己找测试位置、按仓库习惯写测试，并交 manifest。出处：论文 2.1.2，以及 README 对 `data/tw` 的指向。90 题全部 `gpus = 0`、`allow_internet = true`，且 `[agent].network_mode = "allowlist"`，主机是 PyPI、Debian/Ubuntu、Alpine、Go、npm/yarn、nodejs.org 这一组。评分三截：manifest 由 LLM judge 看是否如实列出新增测试；mutation 是程序化的（原代码上测试要过，相关代码换成 no-op 后测试要失败）；rubric 再由 judge LLM 打。必须项是 manifest、mutation、以及 Test Comprehensiveness。出处：论文 2.1.2 Evaluation。要另外的 judge 模型，同时有确定性的 mutation 检查。

### Refactoring

在不改变可观察行为的前提下重组代码。出处：论文 2.1.3。70 题全部 `allow_internet = true` 且 agent allowlist 与 Test Writing 同一组主机。这 70 个 `task.toml` 都没有 `gpus` 键。25 个含 `docker_image` 字段，70 个都有 `environment/Dockerfile`。评分两截：回归测试是程序化的（相关旧测试不能从过变挂，隐藏新测试不能挂，agent 不能改测试文件）；rubric 由 judge LLM 打，Code Maintainability、Artifact Cleanup、Negative Rubrics 是必须项。出处：论文 2.1.3 Evaluation。抽查 `data/rf/task-69391d8d1ce51c407be1e531/tests/test.sh` 先跑 master validator，再跑 `evaluate_rubrics.py`。要另外的 judge 模型。

## 环境

- 容器: 三轨都有 Dockerfile。抽查三题的 `environment/` 只有 Dockerfile，没有 compose。浅克隆后三轨合计 compose 文件数是 0，文件名里也没有 k8s。
- 出网: README 写 Test Writing 和 Refactoring 禁用任意出网，只留构建和跑测试需要的 registry allowlist，并在 harness 层禁 `WebSearch,WebFetch`。钉死的 `run_config/tw/opus-4p6_claude-code.sh` 和 `run_config/rf/opus-4p6_claude-code.sh` 传了 `--allow-agent-host` 和 `disallowed_tools=WebSearch,WebFetch`。README 也写 QnA 在 `agent.run()` 期间限制出网，但钉死的 `run_config/qa/opus-4p6_claude-code.sh` 没有 `--allow-agent-host`，124 个 QnA `task.toml` 也没有 `network_mode`。QnA 的实际出网以这两处文件为准，和 README 那句不完全同一套。
- GPU: QnA 124/124 与 Test Writing 90/90 为 `gpus = 0`。Refactoring 70/70 未写 `gpus`。
- K8s: 没看到。
- 多容器: 没看到 compose 或多 service。
- 沙箱: 三份示例脚本都是 `harbor run -e modal`。Refactoring 脚本另有 `--ek modal_vm_runtime=true`。

## 评分

三轨都要另外的 judge 模型。README 写 “We use Claude Opus 4.5 as the Judge model for rubric grading”，`task.toml` 的默认 `EVAL_MODEL` 是 `anthropic/claude-opus-4-5-20251101`。Test Writing 的 mutation 和 Refactoring 的回归测试是程序算的，最后是否通过还要看必须的 rubric。

## agent / runtime

README 要求安装 Harbor `v0.18.0`，沙箱用 Modal。示例脚本用 `-a claude-code -m anthropic/claude-opus-4-6`。同目录还有 `opus-4p6_miniswe.sh`。论文第 3 节写实验用 Harbor，一线 harness 是 Codex CLI、Claude Code、Gemini CLI，并用 mini-SWE-agent 做同一脚手架对照。agent 回路在 Harbor 进程，任务环境是 Modal 沙箱。

## 体积与是否入 git

GitHub API `size` = 2611 KB。2026-09-24 在 `/tmp/srcfetch/SWE-Atlas` 做的 `git clone --depth 1` 工作树是 42M，没有放进 `/workspace`。本目录只留本文件和 `excerpts.md`，可以进 git。

## 未抓取

- 三轨预构建镜像（`ghcr.io/scaleapi/swe-atlas:*`）没拉。
- 榜页只记了 URL，没有把分数表抄下来。
- Refactoring 没有 `dataset.toml`，所以没有 dataset digest 清单。
- 浅克隆留在 `/tmp`，不在本仓。

MANIFEST-END
