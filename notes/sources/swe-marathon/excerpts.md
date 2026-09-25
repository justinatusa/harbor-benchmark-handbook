# swe-marathon 摘录

抓取日 2026-09-24 Asia/Shanghai。树：`5c468fae8656ef9f7bca36cc8c6ee6e7478aa0f6`。

## README 运行说明

来源：https://raw.githubusercontent.com/abundant-ai/swe-marathon/5c468fae8656ef9f7bca36cc8c6ee6e7478aa0f6/README.md

Install Harbor：`uv tool install 'harbor[modal]==0.20.0'`。还需要 Anthropic API key 和 Modal 账号。试跑命令见 `scripts/run-benchmark.sh`。轨迹在公开 S3，README 写大约 800GB，下载脚本是 `scripts/read-swe-marathon-logs.py`，凭据要另问维护者。论文链接 `https://arxiv.org/abs/2606.07682`。

## CHANGELOG 出网与 Harbor 版本

来源：同提交 `CHANGELOG.md`。

“SWE-Marathon runs on upstream Harbor 0.20.0 instead of the RishiDesai/Harbor fork.”

“Tasks now run with closed (or registry-allowlisted) agent network access. The only tasks that are open internet are the 4 CUA-verified clone tasks (`excel-clone`, `mastodon-clone`, `s3-clone`, `slack-clone`).”

## 20 题 `task.toml` 字段

来源：同提交 `tasks/<name>/task.toml`，20 个文件都拉过。

| 任务 | gpus | agent 出网 | verifier 出网 | 评分 |
| --- | --- | --- | --- | --- |
| biofabric-rust-rewrite | 0 | allowlist | no-network | 测试 |
| embedding-eval | 1 H100 | allowlist | no-network | 测试 |
| excel-clone | 0 | 未写 network_mode | 未写 | 测试 + Opus 4.7 LLM judge |
| find-network-alignments | 0 | allowlist | no-network | 测试 |
| jax-pytorch-rewrite | 1 A100 | allowlist | no-network | 测试 |
| kubernetes-rust-rewrite | 0 | allowlist | no-network | 测试 |
| mastodon-clone | 0 | 未写 network_mode | 未写 | 测试 + Opus 4.7 LLM judge |
| nextjs-vite-rewrite | 0 | allowlist | no-network | 测试 |
| parameter-golf | 1 H100 | allowlist | no-network | 测试 |
| post-train-ifeval-gpu | 1 H100 | allowlist | no-network | 测试，verification 写 All gates are deterministic |
| ruby-rust-port | 0 | allowlist（crates.io / github.com / static.rust-lang.org） | 同左 | 明文 deterministic，No language model judge |
| rust-c-compiler | 0 | allowlist | no-network | 测试比例 |
| rust-java-lsp | 0 | allowlist（crates.io / github.com / static.rust-lang.org） | 同左 | 测试 |
| s3-clone | 0 | 未写 network_mode | 未写 | 测试 + Opus 4.7 LLM judge |
| slack-clone | 0 | 未写 network_mode | 未写 | 0.5 正确性 + 0.5 CUA rubric |
| stripe-clone | 0 | allowlist | no-network | 测试 |
| trimul-cuda | 1 H100 | allowlist | no-network | 正确性与延迟阈值 |
| vliw-kernel-optimization | 0 | allowlist | no-network | 测试 |
| wasm-simd | 键缺失 | allowlist | no-network | 测试 |
| zstd-decoder | 0 | allowlist | no-network | 测试 |

`slack-clone` 的 `verification_explanation` 写：Playwright 驱动 Chromium，Claude Opus 4.7 按 `tests/rubric.json` 打分，reward = `0.5 * correctness + 0.5 * ux`。
