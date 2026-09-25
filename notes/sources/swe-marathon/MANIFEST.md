# MANIFEST

- slug: `swe-marathon`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://www.swe-marathon.org/
- 官方仓: https://github.com/abundant-ai/swe-marathon
- commit: `5c468fae8656ef9f7bca36cc8c6ee6e7478aa0f6`（`main`；`git ls-remote HEAD` 与 GitHub `commits/main` 一致；作者日期 2026-09-22T19:11:36Z，说明 “Update README.md (#291)”）
- 标签: `v1.1-official` → `7bce7b29e1f2413633eb5ed6eb10dc2efb036712`，与上面的 `main` 不是同一提交。`v1.0-official` 的提交是 `9a7083e30059b04b73108708834a8cee4b21b15a`。本摘录对着 `main` 的 SHA，不把标签 SHA 当成当前树。
- 论文: arXiv:2606.07682（https://arxiv.org/abs/2606.07682）
- blog: 没有单独 blog。站点即入口。
- HF: `rdesai2/swe-marathon`，dataset sha `8129e0634100dbb6fe0cdc32d703bf2aa03f6cbb`，`lastModified` 2026-06-05T04:12:24Z。钉死的 README 链接里没有这个 HF id。

## 测什么

测 agent 能否在各自可执行环境里自主做完超长程软件工作。出处：论文摘要 “We introduce SWE-Marathon, a benchmark of 20 long-horizon tasks spanning software engineering and adjacent technical domains.”（https://arxiv.org/abs/2606.07682）。仓内 `tasks/` 有 20 个任务目录，与这句话的题数一致。

## 环境

- 容器: 20 个任务各有 `environment/Dockerfile`。递归树里没有 `docker-compose` 文件（唯一含 compose 字样的路径是 `tasks/mastodon-clone/solution/templates/_composer.html`）。
- 出网: 不一致，按任务写在 `task.toml`。16 题 `[agent].network_mode = "allowlist"`，其中 `ruby-rust-port` 与 `rust-java-lsp` 的 agent 和 verifier 都写了 crates.io / github.com / static.rust-lang.org。多数 verifier 是 `no-network`。`excel-clone`、`mastodon-clone`、`s3-clone`、`slack-clone` 的 `[agent]` 没有 `network_mode`；`CHANGELOG.md` 写这 4 个 CUA clone 题是开放出网，其余是关闭或 registry allowlist。`scripts/run-benchmark.sh` 对限制出网的题加 `--allow-agent-host`，并关掉 Claude Code 的 `WebSearch` / `WebFetch`。
- GPU: 5 题 `gpus = 1`：`embedding-eval`、`parameter-golf`、`post-train-ifeval-gpu`、`trimul-cuda` 为 `H100`，`jax-pytorch-rewrite` 为 `A100`。14 题 `gpus = 0`。`wasm-simd` 的 `[environment]` 没有 `gpus` 键。
- K8s: 评测编排里没看到 Kubernetes。`kubernetes-rust-rewrite` 是一道用 Rust 重写控制器的题，树里的 kubernetes 路径都在这道题的源码和测试下。
- 多容器: 没看到多 service compose。`slack-clone` 的 `task.toml` 写三个 HTTP 节点加 IRC gateway 跑在一个容器里。
- 运行沙箱: `scripts/run-benchmark.sh` 每条命令都带 `-e modal`。镜像构建阶段 `[environment].network_mode = "public"`。

## 评分

混合。16 题的 `verification_explanation` 写的是测试、阈值或差分比较，`ruby-rust-port` 明文写 “All scoring is deterministic. No language model judge anywhere.”。4 道 CUA 题（`excel-clone`、`mastodon-clone`、`s3-clone`、`slack-clone`）的 reward 是 `0.5 * correctness + 0.5 * ux`，UX 由 Claude Opus 4.7 走 rubric，`task.toml` 把它称为 LLM judge，verifier 需要 `ANTHROPIC_API_KEY`。这 4 题要另外的 judge 模型。judge 基础设施失败时不写 reward，trial 报错。

## agent / runtime

官方运行说明用 Harbor CLI。钉死 README 写安装 `harbor[modal]==0.20.0`。`CHANGELOG.md` 写 v1.1 改走上游 Harbor 0.20.0，不再用 `RishiDesai/harbor` fork。示例 agent 是 `claude-code`；`scripts/run-benchmark.sh` 注释里还有 `codex`。`.github/harbor-run-defaults.yml` 还列出 `claude-code`、`codex`、`gemini-cli`。agent 回路在 Harbor 进程里，任务在 Modal 沙箱。`harbor analyze` 另用一个 `analyze_model: sonnet`，那是轨迹分析，不是这 4 道 CUA 题的 verifier judge。

## 体积与是否入 git

GitHub API `size` = 1240601 KB。该提交递归树 4223 项、3396 个 blob，blob 尺寸合计 193454647 字节，最大单文件 31732624 字节。没有把克隆放进 `/workspace`。本目录只留本文件和 `excerpts.md`。二者都小于 200KB，可以进 git。S3 轨迹 README 写大约 800GB，未下载。

## 未抓取

- 站点正文。`https://www.swe-marathon.org/` 返回的 HTML 约 4538 字节，标题是 “SWE-Marathon - Long-Horizon Software Engineering Benchmark”，正文由客户端渲染，榜和任务卡没拿到。
- 全量任务树和最大的数据文件。仓体积超过 5MB，按约定不留在 `/workspace`。
- S3 轨迹。README 写需要向维护者要 S3 凭据，未申请、未下载。
- HF 数据集的 3275 个文件。该 snapshot 的 `lastModified` 是 2026-06-05，早于当前 `main`，未当作当前树。

MANIFEST-END
