# MANIFEST

- slug: chartography
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://github.com/surge-ai/chartography

## 官方仓

- 核实到的官方仓: https://github.com/surge-ai/chartography
- 默认分支: main
- commit SHA: 3f1bf837232d3918c2cc35c6e2418c9e70d2a57b
- 核实: `git ls-remote` HEAD 与 commits API 一致。message 为 “Add Chartography benchmark”，committer 日期 2026-08-14T18:45:03Z。
- GitHub API `size`: 446 KB。该 SHA 的递归 git tree 未截断，16 个 blob，合计 981,963 字节。
- 仓内没有 `LICENSE` 文件。GitHub `license` 字段为空。
- 文件: `src/chartography/`（Inspect AI task）、`task_packs/sample_charts/`（2 道假题）、`tests/test_offline.py`、`uv.lock`。没有 Dockerfile。

## 论文 / blog / HF

- 论文: arXiv [2608.10677](https://arxiv.org/abs/2608.10677)，“Chartography: A Benchmark for Professional Chart Understanding”。
- blog: https://surgehq.ai/blog/chartography
- 榜: https://surgehq.ai/benchmarks/chartography
- HF id: `surgeai/chartography`。API `sha` `a0156216330b52452b1da68b58ffcc0a53be3984`，`lastModified` 2026-08-03T17:50:10.000Z，卡片许可证 cc-by-4.0，`gated` false。
- 该 HF 修订的 tree 有 104 个文件，合计 31,705,853 字节。

## 测什么

测模型能否只看职业场景里的专业图表（Kaplan–Meier、K 线、等高线、Sankey、Bode 等）和领域知识，回答从业者写的题。出处: 该 SHA 的 README「What it tests」，以及 arXiv:2608.10677 摘要（100 题，作者为从业者，另有三名专家独立复核）。

## 环境线索

- 容器: 该 SHA 的文件名里没有 Dockerfile 或 compose。unknown。
- 出网: 全量 100 题要拉 HF（`task.py` 的 `hf_repo`，README 写 `-T hf_repo=surgeai/chartography`）。被测模型和 judge 走供应商 API（`.env.example` 只列空的 key 名）。`tests/test_offline.py` 的说明是不联网、不用 key。
- GPU: README 和 `pyproject.toml` 没有写本地 GPU。unknown。
- K8s: 没看到。unknown。
- 多容器: 没看到。unknown。

## 评分

要另外的 judge 模型，不是确定性规则分。`src/chartography/task.py` 的 solver 是 Inspect `generate()`，scorer 是 `golden_answer_scorer`。默认 `judge_model` 为 `google/gemini-3.5-flash`。`scorer.py` 要求 judge 只回 0 或 1，全部分项都对才给 1；README 写 judge 只看题目、标准答案和回答，不看图。论文表 1 也写 “All-parts binary LLM judge”。论文摘要写每个配置每题 20 次 scored trials；同一 README 的 Leaderboard Configuration 写 `--epochs 10`。两个次数都保留。

## agent / runtime

有证据的是单轮生成，不是多步工具循环。README Quick start 写 “chart attached inline, no tools”。运行时是 Inspect AI（`pyproject.toml` 依赖 `inspect-ai>=0.3.244`）。没有单独的 agent harness。

## 体积与是否入 git

- 上游代码仓 checkout 约 0.98 MB，其中 `uv.lock` 701,194 字节，两张样例图合计约 251 KB。没有把这个克隆放进 `/workspace`。
- HF 图表集约 31.7 MB，没有下载。
- 本目录只有 MANIFEST 和短摘录，摘录来自上述 SHA 的公开文本。本次没有 git commit。

## 未抓取项与原因

- HF 上 100 张正式图表和标注：合计超过 5 MB。
- 论文 PDF 全文和榜页全文：摘要与 README 已够用，没有存 PDF。
- 论文 “20 trials” 与 README “epochs 10” 没有对上，没有改任何一方的原文。
- 代码仓没有许可证文件；数据集许可证只记了 HF 卡片上的 cc-by-4.0。

MANIFEST-END
