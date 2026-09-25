# SWE-Atlas

三轨分开看。Codebase Q&A（代码库问答）和 Test Writing 有 `dataset.toml`，Refactoring 没有。三轨的 rubric 都要另调模型。

1. 一句话测什么。测编程代理在代码库问答、写测试和重构里的表现，题量是 124、90、70。出处是 https://arxiv.org/abs/2605.08366 摘要。钉死树上 `data/qa`、`data/tw`、`data/rf` 的题数与摘要一致。

2. 官方源。仓库 https://github.com/scaleapi/SWE-Atlas ，commit `49e4af3b6c803dd54a1cd60ead703aac25de4e21`（2026-08-20，说明 “Merge pull request #20 … TW: provision uv and Python 3.11 in the simple-login task images”）。论文 https://arxiv.org/abs/2605.08366 。博客 https://scale.com/blog/swe-atlas-complete 。榜 https://labs.scale.com/leaderboard/sweatlas-qna 、https://labs.scale.com/leaderboard/sweatlas-tw 、https://labs.scale.com/leaderboard/sweatlas-refactoring 。没有 Hugging Face dataset id。没有 git tag。

3. 形态。`task`、`dataset`、`environment`、`verifier`、`agent`。示例直接调用 `harbor run`。清单没写单独的 `adapter`。

4. 与 Harbor 距离。重改造。任务文件的 Harbor 版本是 v0.18.0，不是 0.23.0。没有 git tag。`data/qa/dataset.toml` 的名字是 `scale-ai/swe-atlas-qna`，`data/tw/dataset.toml` 存在，各题有 `task.toml`。`data/rf` 有 70 个目录，没有 `dataset.toml`。README 写用 Claude Opus 4.5 做 rubric 评判，`task.toml` 里默认 `EVAL_MODEL` 是 `anthropic/claude-opus-4-5-20251101`。要另调模型，所以是重改造。

5. 环境。三轨都有 Dockerfile。浅克隆后 compose 文件数是 0，也没看到 Kubernetes。Codebase Q&A 的 124 题和 Test Writing 的 90 题写 `gpus = 0`。Refactoring 的 70 个 `task.toml` 没有 `gpus` 键。Test Writing 和 Refactoring 的 `[agent].network_mode` 是 `allowlist`。Codebase Q&A 的 `task.toml` 没有 `network_mode`，示例脚本 `run_config/qa/opus-4p6_claude-code.sh` 也没有 `--allow-agent-host`。README 写 QnA（即 Codebase Q&A）在 `agent.run()` 期间限制出网，和这两处文件不完全同一套。三份示例脚本都是 `harbor run -e modal`。Refactoring 另有 `--ek modal_vm_runtime=true`。没看到一道题多个容器。

6. 评分。三轨都要另调模型。Codebase Q&A 的 rubric 全部是必须项，全过才算过。Test Writing 分三段：manifest 由模型看是否如实列出新增测试，mutation 用程序检查（原代码上测试要过，相关代码换成空操作（no-op）后测试要失败），rubric 再由模型打。Refactoring 的回归测试用程序检查，rubric 由模型打。必须项不过，最后就不算过。

7. agent/runtime。README 要求安装 Harbor `v0.18.0`，沙箱用 Modal。示例脚本用 `-a claude-code -m anthropic/claude-opus-4-6`，同目录还有 `opus-4p6_miniswe.sh`。论文第 3 节写实验用 Harbor，一线是 Codex CLI、Claude Code、Gemini CLI，并用 mini-SWE-agent 做对照。代理回路在 Harbor 进程里，任务环境是 Modal 沙箱。本手册的 Harbor 是 0.23.0。v0.18.0 的字段能否原样用，清单没核对。

8. 迁入代价。中。任务目录已经有 `task.toml`，示例就是 `harbor run`。还要准备评判模型用的密钥。Refactoring 没有 `dataset.toml`。README 钉的是 Harbor v0.18.0，和 0.23.0 是否相容，清单没核实。

9. 对抽象的压力。`verifier` 要同时接程序检查和必须通过的模型 rubric。`dataset` 在前两轨有 `dataset.toml`，Refactoring 没有。`environment` 是单份 Dockerfile，沙箱类型是 Modal，Refactoring 还打开 `modal_vm_runtime`。`agent` 的回路在 Harbor 进程里。

10. MANIFEST 路径。`notes/sources/swe-atlas/MANIFEST.md`
