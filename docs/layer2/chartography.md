# Chartography

题目是图，judge 不看图。分数仍要另调一个模型。

## 测什么

测模型能否只看职业场景里的专业图表和领域知识，回答从业者写的题。公开说明是 100 题，图种包括 Kaplan-Meier、K 线、等高线、Sankey、Bode。

## 官方源

仓 https://github.com/surge-ai/chartography ，commit `3f1bf837232d3918c2cc35c6e2418c9e70d2a57b`（2026-08-14）。论文 https://arxiv.org/abs/2608.10677 。博客 https://surgehq.ai/blog/chartography 。榜 https://surgehq.ai/benchmarks/chartography 。Hugging Face（HF）https://huggingface.co/datasets/surgeai/chartography ，修订 `a0156216330b52452b1da68b58ffcc0a53be3984`，gated 为 false。仓内没有许可证文件。HF 卡片写 cc-by-4.0。

## 形态

task、dataset、verifier。代码在 `src/chartography/`，运行时是 Inspect AI。`task_packs/sample_charts/` 有 2 道样例。没有 `task.toml`、`dataset.toml`、Dockerfile 或 adapter。没有单独的 agent 回路。

## 与 Harbor 距离

重改造。评分要另调 judge 模型。

## 环境

这个 commit 没有 Dockerfile 或 compose。全量 100 题要从 HF 拉取。被测模型和 judge 走供应商接口。`tests/test_offline.py` 的说明是不联网、不用密钥。图形处理器（GPU）、Kubernetes、多容器、图形桌面都没有写。图表是题目图片。

## 评分

`src/chartography/task.py` 的 solver 是 Inspect 的 `generate()`，scorer 是 `golden_answer_scorer`。默认 `judge_model` 为 `google/gemini-3.5-flash`。`scorer.py` 要求 judge 只回 0 或 1，全部分项都对才给 1。README 写 judge 只看题目、标准答案和回答，不看图。论文表 1 写全部分项都由模型判 0 或 1。论文摘要写每个配置每题 20 次计分。同一 README 的榜单配置写 `--epochs 10`。两个次数都保留。

## agent / runtime

看到的是单轮生成。README 写图表内嵌，没有工具。运行时是 Inspect AI（`inspect-ai>=0.3.244`）。没有单独的 agent 程序。

## 迁入代价

中。题目和评分入口公开。仓里的样例是 2 道假题。正式 100 张图在 HF，约 31.7 MB，本次没下。接进 Harbor 时 verifier 仍要调用 judge 模型。

## 对抽象的压力

压在 verifier。分数依赖另一个模型，而且该模型不看图。Inspect 的 task 也还不是带 `task.toml` 的 Harbor task 目录。

## 本地摘录

见 [`notes/sources/chartography/MANIFEST.md`](../../notes/sources/chartography/MANIFEST.md)。
