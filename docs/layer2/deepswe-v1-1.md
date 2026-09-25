# DeepSWE v1.1

没有名为 `v1.1` 的 git tag。v1.1 的文字定义在 blog 和 README 的 “Since v1.1” 段。下面的 commit 是抓取日的 `main`，不能说成 v1.1 标签对象。

1. 一句话测什么。衡量前沿 coding agent 在活跃开源仓库上的原创、长程软件工程任务。113 题，语言为 TypeScript、Go、Python、JavaScript、Rust，带隔离环境和程序 verifier。出处是 README @ `0b9fabbb`。论文摘要同口径：题面从零写成，不回上游，由手写 verifier 按所要求的功能给分、接受任何实现。

2. 官方源。入口与仓库 https://github.com/datacurve-ai/deep-swe ，`main` HEAD = `0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea`（2026-08-26 +0000，说明 “Update task timeout settings to 10800s”）。tag 只有 `v1.0.0`，剥开后的 commit 是 `c33fa70e68d11d85f9e58abcd5d78643705e916e`。论文 https://arxiv.org/abs/2607.07946 ，HTML https://arxiv.org/html/2607.07946 。blog https://deepswe.datacurve.ai/blog/deepswe-v1-1 （Wenqi Huang, Peter Jiang, June 14, 2026）。站点 https://deepswe.datacurve.ai/ 。HF `datacurve/deep-swe` ，https://huggingface.co/datasets/datacurve/deep-swe ，卡上写明 held-out、gated，任务数 113。行数据未下载。blog 自引 bibtex 的 url 是 GitHub 仓。

3. 形态。`task`、`dataset`、`environment`、`verifier`、`agent`。README 写 DeepSWE 任务使用 Harbor task 格式。清单读了 113 个 `task.toml`，并写出 `tasks/*/environment/Dockerfile` 与 `tasks/*/tests/Dockerfile`。运行示例是 `pier run -p deep-swe/tasks`。清单没有写出 `dataset.toml` 的路径，也没有写 `adapter`。

4. 与 Harbor 距离。轻适配。没有 v1.1 tag，main 上的 task.toml 不能当成 v1.1。官方仓能指出这 113 个 Harbor `task.toml`。README 写任务目录就是 Harbor task 格式。

5. 环境。113/113 的 `task.toml` 有 `docker_image`（抽到的例子是 `public.ecr.aws/d3j8x8q7/swe-bench-202605:<id>-v1.1`）、`os = "linux"`、`[verifier] environment_mode = "separate"`，以及 `[[verifier.collect]]` 把相对 base commit 的 `git diff` 收到 `/logs/artifacts/model.patch`。113 个 `tasks/*/environment/Dockerfile`，另有 113 个 `tasks/*/tests/Dockerfile`。113/113 的 `[agent]` 与 `[verifier]` 都是 `network_mode = "no-network"`。`task.toml` 没有 `allow_internet` 键。README 写 Harbor 在 `allow_internet = false` 时会挡住全部出站，包括依赖安装和 LLM API；Pier 给 agent 单独的网络白名单。榜分用 Pier 跑，因此榜上的 agent 出网和 `task.toml` 里的 `no-network` 不是同一条执行路径。113/113 `gpus = 0`，没有 `gpu_types`。K8s 是 unknown。完整克隆里 compose 计数为 0。separate verifier 是另一个容器，清单把它和 compose 多服务分开记。抽到的 `[agent] timeout_sec = 10800.0`，`[verifier] timeout_sec = 1800.0`。

6. 评分。解题分由程序 verifier 给出。`tests/grader.py` 头注释写 `reward` 为 binary 0/1：fail-to-pass 非空且全部通过，并且 pass-to-pass 规则满足时为 1，结果写入 `/logs/verifier/reward.json`。`tests/test.sh` 跑语言测试并生成 CTRF，再交给 grader。论文 §3.4 写 GPT-5.5（xhigh，Codex CLI agent）是 verifier 的审计，executable verifier 仍是榜上的 grader。论文 Figure 1 的 pass@1 是各题通过率的等权平均。

7. agent/runtime。README 用 Pier（https://github.com/datacurve-ai/pier ，PyPI `datacurve-pier`，要求新于 0.3.0）跑 Harbor 任务格式。示例 `pier run -p deep-swe/tasks --agent mini-swe-agent`。Pier 也能直接驱动 `claude-code`、`codex`、`gemini-cli`、`opencode`；`--env modal` 做并行沙箱。原文写榜上分数由 Pier 跑 `mini-swe-agent`，沙箱是 Modal。论文写 Harbor 提供了 DeepSWE 采用的 task/trajectory 格式，跨模型比较用 mini-swe-agent。

8. 迁入代价。中。113 个任务目录已是 Harbor task 格式。文档化的榜分运行器是 Pier，不是清单里的一条 `harbor run`。README 写这样做是因为 Harbor 在关闭出网时会挡住 LLM API，Pier 再加 agent 网络白名单。预构建镜像没有 pull。HF 行数据是 gated，未下载。

9. 对抽象的压力。`environment` 的网络分成两层：`task.toml` 写 `no-network`，榜上的 agent 出网走 Pier 白名单。`verifier` 用 `environment_mode = "separate"`，并用 `[[verifier.collect]]` 收 `model.patch`，再在干净容器里评分。`agent` 的榜上回路在 Pier 里，示例 agent 是 `mini-swe-agent`。`dataset` 的运行入口是目录 `deep-swe/tasks`；清单没有写出 `dataset.toml` 路径。

10. 本地摘录。私有摘录未随公开手册发布。
