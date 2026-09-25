# deepswe-v1-1

- slug: `deepswe-v1-1`
- 抓取日: 2026-09-24 Asia/Shanghai

## 入口与官方仓

- 入口: https://github.com/datacurve-ai/deep-swe
- 官方仓: 同上。default branch `main`。抓取时 HEAD = `0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea`（2026-08-26 +0000，“Update task timeout settings to 10800s”）。
- tag: 只有 `v1.0.0`。annotated tag 对象 `79a508a908998690c6ceb773ae2dbcc23f55e434`，剥开后的 commit 是 `c33fa70e68d11d85f9e58abcd5d78643705e916e`。没有名为 `v1.1` 的 tag。
- 本清单读的是 `main` @ `0b9fabbb` 上的 README 和 113 个 `task.toml`。没有做 `v1.0.0` 与 `main` 的 diff，所以不能把该 commit 说成 “v1.1 标签对象”。v1.1 的文字定义在 blog 和这份 README 的 “Since v1.1” 段。

## 论文 / blog / HF

- 论文: https://arxiv.org/abs/2607.07946 （Huang, Lee, Tng, Ge, Datacurve, May 2026）。HTML: https://arxiv.org/html/2607.07946
- v1.1 blog: https://deepswe.datacurve.ai/blog/deepswe-v1-1 （Wenqi Huang, Peter Jiang, June 14, 2026）。站点首页 https://deepswe.datacurve.ai/
- HF: `datacurve/deep-swe` 。数据集卡写明这是 held-out 评测数据，gated。https://huggingface.co/datasets/datacurve/deep-swe 。卡上的任务数与 README 一致，为 113。行数据未下载。
- blog 自引 bibtex 的 url 是 GitHub 仓，不是 arXiv。

## 测什么

README @ `0b9fabbb`：衡量前沿 coding agent 在活跃开源仓库上的原创、长程软件工程任务；113 题，语言为 TypeScript、Go、Python、JavaScript、Rust，带隔离环境和程序 verifier。论文摘要同口径：113 个原创长程任务，题面从零写成，不回上游，由手写 verifier 按所要求的功能给分、接受任何实现。

## 环境线索

- 容器: 有。113/113 `task.toml` 有 `docker_image`（抽到的例子是 `public.ecr.aws/d3j8x8q7/swe-bench-202605:<id>-v1.1`）、`os = "linux"`、`[verifier] environment_mode = "separate"`，以及 `[[verifier.collect]]` 把相对 base commit 的 `git diff` 收到 `/logs/artifacts/model.patch`。README：agent 在隔离环境里提交，patch 在干净容器里评分。树清单里 113 个 `tasks/*/environment/Dockerfile`，另有 113 个 `tasks/*/tests/Dockerfile`（verifier 镜像）。
- 出网: 113/113 的 `[agent]` 与 `[verifier]` 都是 `network_mode = "no-network"`。`task.toml` 没有 `allow_internet` 键。README 对 Pier 的说明：Harbor 在 `allow_internet = false` 时会挡住全部出站（含依赖安装和 LLM API）；Pier 给 agent 单独的网络白名单。榜分是用 Pier 跑的，因此榜上的 agent 出网不等于 `task.toml` 里的 `no-network` 原样执行。
- GPU: 113/113 `gpus = 0`。没有 `gpu_types`。
- K8s: unknown。已检出的 md/toml/yaml/py/sh 中没有 `kubernetes` 或 `k8s`。
- 多容器: 未见。113 个任务没有 compose 文件（同日完整克隆扫描 `compose` 计数为 0）。verifier 是另一个容器（`environment_mode = "separate"`），不是 compose 多服务。
- 超时: 抽到的 `[agent] timeout_sec = 10800.0`，与 HEAD 提交说明一致。`[verifier] timeout_sec = 1800.0`（该样本）。

## 评分

解题分是程序 verifier，不是 judge 模型。`tests/grader.py` 头注释写明：`reward` 为 binary 0/1，当 fail-to-pass 非空且全部通过、并且 pass-to-pass 规则满足时为 1；结果写入 `/logs/verifier/reward.json`。`tests/test.sh` 跑语言测试并生成 CTRF，再交给 grader。论文 §3.4 原文：“We treat this judge as an auditor of the verifier, not as the grader of record; the executable verifier remains authoritative for the leaderboard.” 该 judge 是 GPT-5.5（xhigh，Codex CLI agent），用来抽查 verifier 与“补丁是否实现了要求”是否一致，不是榜上的 pass@1。论文 Figure 1：pass@1 是各题通过率的等权平均。

## agent / runtime

README：用 Pier（https://github.com/datacurve-ai/pier ，PyPI `datacurve-pier`，要求新于 0.3.0）跑 Harbor 任务格式。示例 `pier run -p deep-swe/tasks --agent mini-swe-agent`。又写 Pier 也能直接驱动 `claude-code`、`codex`、`gemini-cli`、`opencode`；`--env modal` 做并行沙箱。原文：“All leaderboard scores were produced with Pier running `mini-swe-agent` on Modal.” 论文 §5 附近写 Harbor 提供了 DeepSWE 采用的 task/trajectory 格式，跨模型比较用 mini-swe-agent。

## 体积与是否入 git

- GitHub API `size`（2026-09-24，KB）: 3489。
- 同日 `--depth 1` 完整克隆工作树约 37MB（`/tmp`，未放入 `/workspace`）。
- 本目录只留这份 `MANIFEST.md`。官方仓与 HF 行数据都不入本仓库 git。

## 未能抓取

- 没有 `v1.1` git tag，因此没有一个名叫 v1.1 的 commit SHA。当前公开 tip 是 `0b9fabbb`；`v1.0.0` 是更早的 `c33fa70e`。未做二者 diff。
- HF `datacurve/deep-swe` 是 gated，行数据未下。
- blog 页上的 rollout 浏览器和 “Run DeepSWE” 交互页没有逐条抓取。
- 预构建镜像 `public.ecr.aws/...` 没有 pull。

MANIFEST-END
