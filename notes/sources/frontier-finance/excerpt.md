# frontier-finance 摘录

抓取日 2026-09-24 Asia/Shanghai。只保留短句，不收录数据集。

入口页 https://research.samaya.ai/benchmarks/frontier-finance ：

> FrontierFinance is an open benchmark measuring how well AI systems support the full investment workflow — from screening and discovery to earnings analysis and portfolio monitoring. Queries are open-ended financial research tasks scored against expert-written rubric items using a rubric-based evaluation methodology.
>
> Dataset: 220 public queries … The dataset is available on Hugging Face and the evaluation code is open-source on GitHub.

论文 https://arxiv.org/abs/2608.11683 摘要：

> We introduce FrontierFinance, a fully open benchmark of 220 expert-crafted queries and 11,543 source-attributed rubrics spanning six crucial use cases across the full investor workflow. … We make the dataset and grading code publicly available.

论文第 5 节（arXiv HTML）：

> We score each rubric by majority vote across three independent LLM judges: GPT 5.4, Gemini 3.1 Pro, and Claude Sonnet 4.6.

评分仓 README，钉在 `cd51ad2b14dab298cf11151fb8d28a54613d7074`：

> Rubrics-based LLM grader … an LLM judge panel decides whether each rubric is satisfied
>
> judge_models: claude-sonnet-4-6 / gemini-3.1-pro-preview / gpt-5.4
>
> The dataset is public — no login or token needed.

HF API 2026-09-24：`samaya-ai/FrontierFinance`，`gated: auto`，sha `36afd6dc1cbb2c4512536daf917dc28b1225a720`。匿名 resolve JSONL 返回 401。
