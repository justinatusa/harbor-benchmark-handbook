# sec-bench-pro

- slug: `sec-bench-pro`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://github.com/SEC-bench/SEC-bench-Pro

## 官方仓

- 有。https://github.com/SEC-bench/SEC-bench-Pro
- 默认分支 `main` HEAD: `da80928ee20dc417ca6a068a1213e1d9d279df20`
- 核实: `git ls-remote` HEAD 与 commits API 一致。commit 日期 2026-09-21T17:31:42Z，message 为 “Merge pull request #10 from smlijun/fix/linux-latest-validation-hotfixes”。
- 许可证: MIT。GitHub `size` 字段 16,926 KB。该 SHA 的 git tree 未截断，blob 合计 134,865,817 字节；其中 `projects/` 133.77 MB、4,274 个文件。
- 论文摘要给出的 artifact 地址就是这个仓。榜单站是 https://sec-bench.github.io/ ，本次没有整站抓取。

## 论文 / blog / HF

- 论文: arXiv [2605.26548](https://arxiv.org/abs/2605.26548)。abs 页写提交 2026-05-26（v1），最后修订 2026-07-20（当前 v2）。没有单独的 blog id。没有 HF dataset id。
- 镜像名出现在 harness README：`hwiwonlee/v8.x86_64`、`hwiwonlee/v8.x86_64.fixed`、`hwiwonlee/sm.x86_64`、`hwiwonlee/sm.x86_64.fixed`、`hwiwonlee/linux.x86_64`、`hwiwonlee/linux.x86_64.fixed`、`hwiwonlee/linux.x86_64.latest`。镜像本身没有拉取。

## 测什么

用已披露报告复现可工作的 PoC 输入，测模型在 V8、SpiderMonkey 和 Linux kernel 上的长程漏洞寻找；当前集合是 344 个已核实例。出处: arXiv 2605.26548 摘要，以及该 commit 的 README。

## 环境线索

- 容器: 有。每题用 Docker 镜像；Linux 要特权容器，并且容器内能读写 `/dev/kvm`。文档写不用 QEMU TCG 代替 KVM。
- 出网: agent 侧按示例配置收紧。Codex 关 `network_access` 和 `web_search`；Claude 拒绝域名 `*`；OpenCode 的 Bash 进无外网的网络命名空间，模型客户端仍可访问 provider。judge 调用要 Bedrock、Anthropic 或 OpenAI 凭据。镜像可用 `--pull-missing` 拉取。
- GPU: 未见。记 unknown。
- K8s: 未见。记 unknown。
- 多容器: 评分对同一题的 vulnerable、fixed、latest 镜像分别起容器。agent 评测是每题一个容器。Linux 的 QEMU 在该特权容器内，MCP server 在 agent 命令沙箱外。未见 compose 或多容器编排文件。

## 评分

要另外的 judge 模型。退出码和重试在 harness 里；崩溃是否对上目标漏洞交给模型。默认 judge 是 `claude-sonnet-4-6`（Bedrock 名为 `us.anthropic.claude-sonnet-4-6`），OpenAI 回退默认 `gpt-5.4`。V8/SpiderMonkey 在 fixed 镜像不能干净否定时还有带终端的 source review。出处: `harness/README.md` 与 `harness/GRADING.md`，以及论文摘要里的 LLM-based judge。

## agent / runtime

有证据。`harness/eval_codex.py`、`eval_claude.py`、`eval_opencode.py` 在每题容器里跑 Codex、Claude Code 或 OpenCode。示例 timeout 5400 秒，与论文写的 90 分钟一致。Linux agent 通过 `secb-linux-vm-mcp` 的 `secb_build`、`secb_repro`、`secb_validate` 接触 QEMU，不直接碰内核镜像。Python 依赖在 `pyproject.toml`：`jinja2`、`litellm`、`rich`、`boto3`，要求 Python ≥ 3.11。

## 体积与是否入 git

- 全树约 135 MB，超过 5 MB，没有克隆进 `/workspace`，不入 git。
- 本目录只留本文件和 `excerpt-scoring.txt`。这两份可以进 git。
- Docker 镜像体积未计。

## 未抓取项与原因

- 未克隆全仓，也未下载 `projects/` 里的实例、PoC 或验证日志。树太大，而且含可运行的复现材料。
- 未拉取 `hwiwonlee/*` 镜像，未跑 eval 或 grade。
- 未抓 https://sec-bench.github.io/ 的榜单全文。
- 未抄 `prompts/` 里的任务或 judge 模板。

MANIFEST-END
