# SEC-bench Pro

公开材料能看出任务形态和评分方式。评分要另调模型，Linux 题还要特权容器。

## 测什么

测模型在 V8、SpiderMonkey 和 Linux 内核上的长程漏洞寻找。当前集合是 344 个已核实例。

## 官方源

仓 https://github.com/SEC-bench/SEC-bench-Pro ，commit `da80928ee20dc417ca6a068a1213e1d9d279df20`（2026-09-21），许可证 MIT。论文 https://arxiv.org/abs/2605.26548 。榜站 https://sec-bench.github.io/ ，本次没有整站抓取。没有 Hugging Face 数据集，也没有单独的博客。

## 形态

task、environment、verifier、agent。每题一个容器。没有看到 `task.toml`、`dataset.toml` 或 adapter。

## 与 Harbor 距离

重改造。评分要另调 judge 模型。同一题的评分还会分别起多个镜像。

## 环境

每题用 Docker 镜像。Linux 要特权容器，容器内要能读写 `/dev/kvm`。agent 侧的示例配置把出网收紧。judge 调用仍要模型供应商凭据。镜像可以按参数补拉，本次没有拉取。图形处理器（GPU）和 Kubernetes 没有写，记 unknown。agent 评测是每题一个容器。评分对同一题的有缺陷版本、修复版本和最新版本镜像分别起容器。Linux 的虚拟机在该特权容器内。没有看到 compose。

## 评分

要另外的 judge 模型。退出码和重试在评分程序里。结果是否对上目标，交给模型判断。默认 judge 是 `claude-sonnet-4-6`。OpenAI 回退默认 `gpt-5.4`。V8 和 SpiderMonkey 在修复版镜像上不能直接否定时，还有带终端输出的源码复查。论文摘要也写了由模型担任 judge。

## agent / runtime

`harness/eval_codex.py`、`eval_claude.py`、`eval_opencode.py` 在每题容器里跑 Codex、Claude Code 或 OpenCode。示例超时 5400 秒，与论文写的 90 分钟一致。Linux 上的虚拟机留在特权容器里，agent 不直接改内核镜像。Python 依赖在 `pyproject.toml`，要求 Python 3.11 及以上。

## 迁入代价

高。verifier 要另调 judge 模型，还要准备多套镜像。Linux 题要特权容器和 `/dev/kvm`。

## 对抽象的压力

压在 verifier 和 environment。对错要交给另一个模型，本地退出码不够用。environment 在评分时要按题起多个镜像，Linux 还要特权容器。

## 本地摘录

私有摘录未随公开手册发布。
