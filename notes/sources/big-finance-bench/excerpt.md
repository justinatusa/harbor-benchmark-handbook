# big-finance-bench 摘录

抓取日 2026-09-24 Asia/Shanghai。

论文 https://arxiv.org/abs/2606.03829 摘要：

> We introduce BigFinanceBench, a 928-item expert-authored benchmark of open-ended financial-research tasks in which each item pairs a ground-truth reference answer with a point-weighted rubric that decomposes the derivation into independently checkable steps.

论文第 4.1 节：

> two independent judges (Gemini 3.1 Pro Preview and Claude Opus 4.7) … The primary metric is rubric score … web_search … edgar_search … fetch_url … python_exec … All model inference uses commercial hosted APIs … No on-site compute workers are used.

论文附录 A：

> We release a stratified 50-question subset … https://huggingface.co/datasets/RogoAI/big-finance-benchmark … https://github.com/Rogo-Technologies/big-finance-benchmark … https://bigfinancebench.com/ … The full benchmark is withheld at submission time.

README 钉在 `d794a65fe583edc6852b44c817b0a2aef33ca831`：

> Reference scaffold … 928 workflow-grounded financial-research questions
>
> The publicly-released 50-item subset is bundled in data/big_finance_subset.jsonl
>
> python_exec is not a sandbox. It's a subprocess with a 5-second timeout and no filesystem, network, or syscall isolation.

榜页 https://bigfinancebench.com/ 2026-09-24 纯文本开头：

> Models 29 Questions 928 Updated Sep 17, 2026 … Scores are a two-judge mean (Gemini 3.1 Pro and Claude Opus 4.7)
