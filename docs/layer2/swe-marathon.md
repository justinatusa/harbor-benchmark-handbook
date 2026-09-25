# SWE-Marathon

20 个目录已经是 Harbor task。`scripts/run-benchmark.sh` 对每题写 `harbor run`。README 安装的是 `harbor[modal]==0.20.0`，不是本手册的 0.23.0。4 道界面题的体验分要另调 Claude Opus 4.7。

1. 一句话测什么。测 agent 能否在各自可执行环境里自主做完超长程软件工作。20 题。出处是 arXiv 2606.07682 摘要：“a benchmark of 20 long-horizon tasks spanning software engineering and adjacent technical domains.” 仓内 `tasks/` 有 20 个任务目录，与这句话的题数一致。

2. 官方源。仓库 https://github.com/abundant-ai/swe-marathon ，`main` HEAD `5c468fae8656ef9f7bca36cc8c6ee6e7478aa0f6`（2026-09-22，说明 “Update README.md (#291)”）。标签 `v1.1-official` 指向 `7bce7b29e1f2413633eb5ed6eb10dc2efb036712`，与这个 `main` 不是同一提交。`v1.0-official` 是 `9a7083e30059b04b73108708834a8cee4b21b15a`。下面对着 `main` 的 SHA，不把标签 SHA 当成当前树。论文 https://arxiv.org/abs/2606.07682 。站点 https://www.swe-marathon.org/ 。没有单独 blog。HF `rdesai2/swe-marathon` 的 `lastModified` 是 2026-06-05，钉死的 README 没有这个 id，未当作当前树。

3. 形态。`task`、`environment`、`verifier`、`agent`。20 个目录各有 `task.toml` 和 `environment/Dockerfile`。示例直接调用 `harbor run`。清单没有写出 `dataset.toml`。公开材料没有单独的 Harbor adapter。

4. 与 Harbor 距离。轻适配。这个 commit 有 Harbor task 目录，`scripts/run-benchmark.sh` 对每题写 `harbor run`。README 钉的是 `harbor[modal]==0.20.0`，不是 0.23.0，所以不是原生可接。4 道 UX 题要另调模型。部分题要 GPU。

5. 环境。20 题各有一个 Dockerfile。递归树里没有 docker-compose 文件。`scripts/run-benchmark.sh` 每条命令都带 `-e modal`。镜像构建阶段 `[environment].network_mode = "public"`。16 题 `[agent].network_mode = "allowlist"`，其中 `ruby-rust-port` 与 `rust-java-lsp` 的 agent 和 verifier 都写了 crates.io、github.com、static.rust-lang.org。多数 verifier 是 `no-network`。`excel-clone`、`mastodon-clone`、`s3-clone`、`slack-clone` 的 `[agent]` 没有 `network_mode`。`CHANGELOG.md` 写这 4 个 CUA clone 题是开放出网，其余是关闭或 registry allowlist。脚本对限制出网的题加 `--allow-agent-host`，并关掉 Claude Code 的 `WebSearch` / `WebFetch`。5 题 `gpus = 1`：`embedding-eval`、`parameter-golf`、`post-train-ifeval-gpu`、`trimul-cuda` 为 H100，`jax-pytorch-rewrite` 为 A100。14 题 `gpus = 0`。`wasm-simd` 的 `[environment]` 没有 `gpus` 键。评测编排里没看到 Kubernetes。`slack-clone` 的 `task.toml` 写三个 HTTP 节点加 IRC gateway 跑在一个容器里。没看到一道题多个容器。

6. 评分。混合。16 题的 `verification_explanation` 写的是测试、阈值或差分比较。`ruby-rust-port` 明文写 “All scoring is deterministic. No language model judge anywhere.”。4 道 CUA 题（`excel-clone`、`mastodon-clone`、`s3-clone`、`slack-clone`）的 reward 是 `0.5 * correctness + 0.5 * ux`。UX 由 Claude Opus 4.7 走 rubric，`task.toml` 把它称为 LLM judge，verifier 需要 `ANTHROPIC_API_KEY`。judge 基础设施失败时不写 reward，trial 报错。`slack-clone` 写 Playwright 驱动 Chromium，按 `tests/rubric.json` 打分。

7. agent/runtime。官方运行说明用 Harbor CLI。钉死 README 写安装 `uv tool install 'harbor[modal]==0.20.0'`。`CHANGELOG.md` 写 v1.1 改走上游 Harbor 0.20.0，不再用 `RishiDesai/harbor` fork。示例 agent 是 `claude-code`。脚本注释里还有 `codex`。`.github/harbor-run-defaults.yml` 还列出 `claude-code`、`codex`、`gemini-cli`。代理回路在 Harbor 进程里，任务环境是 Modal 沙箱。本手册的 Harbor 是 0.23.0。0.20.0 的字段能否原样用，清单没核对。`harbor analyze` 另用一个 `analyze_model: sonnet`，那是轨迹分析，不是这 4 道题的 verifier judge。

8. 迁入代价。高。20 个任务目录已经有 `task.toml`，示例就是 `harbor run`。README 钉的是 Harbor 0.20.0，不是 0.23.0。5 题要 GPU。4 道 UX 题要 Anthropic 密钥。仓体积远超一次浅读，S3 轨迹 README 写大约 800 GB，凭据要另问维护者。

9. 对抽象的压力。`verifier` 在 16 题上是程序测试，在 4 道界面题上还要必须能调到的模型 rubric。`environment` 是单份 Dockerfile，沙箱类型是 Modal，GPU 按题填写，有一道题没写 `gpus`。`agent` 的回路在 Harbor 进程里，版本钉在 0.20.0。清单没有写出 `dataset.toml`。

10. 本地摘录。[`notes/sources/swe-marathon/MANIFEST.md`](../../notes/sources/swe-marathon/MANIFEST.md)。
