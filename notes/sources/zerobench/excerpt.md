# excerpt: zerobench

来源 commit `0debbe43deddfe54f9965a6fdfd4f70a20d8ab62` 的 `README.md`，以及抓取日的 https://zerobench.github.io/ 。

`README.md`: “ZeroBench is a challenging visual reasoning benchmark for Large Multimodal Models (LMMs). It consists of a main set of 100 high-quality, manually curated questions covering numerous domains, reasoning types and image type.” 子问题 split 的示例 `num_rows: 334`。

同一 README 的 pass@1 片段：从最后一对花括号取出答案，与 ground truth 做 strip + lower 后的等长相等比较。没有 judge 模型参数。

同一 README 的指标定义: pass@1、pass@5、pass^5，均相对每题 5 次采样。该 commit 写的官方最高分为 GPT-5.6 Sol (max) pass@5 30.0、pass^5 13.0。

项目页（2026-09-24 抓取）写 2026-08 评测协议 red team 后改正了 0.71% 的 grading。页内官方表另有更高的 pass@5（例如 GPT-6 Astra (max) 52.0）。外部表 Notes 中出现 “graded by an LLM judge” 与 “Containerized coding+GUI tools”。这些句子不在该 git commit 的代码里。

数据集 id: `jonathan-roberts1/zerobench`。HF API `gated` 为 `auto`。本摘录不收录 README 中的 canary 字符串。
