来源：https://github.com/databricks/officeqa/blob/7b9a3c154ef9fb40215bb67934afc43e6799de16/README.md

OfficeQA Pro：133 题，语料是 U.S. Treasury Bulletins，1939–2025。OfficeQA Full 是它的超集（246 题）。题目 CSV、PDF、解析文本在 Hugging Face `databricks/officeqa`，不在这个 GitHub 仓里。两个数据集都是 gated。

代码仓里的 `reward.py` 对 Pro、Full、Pro V2 共用。`score_answer(ground_truth, predicted, tolerance)` 返回 1.0 或 0.0。README 列出的容差是相对误差 0.0%、0.1%、1.0%、5.0%。

论文 https://arxiv.org/abs/2603.08655 摘要：133 道题，要求在财政部公报上做精确解析、检索，以及跨非结构化文本和表格的分析推理。同文写明，除非另有说明，OfficeQA Pro 用 0.0% allowable absolute relative error。评分实现是文中指向的 reward，对标点、符号、缩写做规范化，数值和文本做模糊匹配。

论文第 3 节把 agent baseline 定义成能自主调用工具、多步推理的编排。第 4 节的工具包括 Web Search API、限制扫目录的 Python REPL，以及自定义 fs_search / fs_read。README 另记录了 Claude Agent SDK、Codex SDK、Gemini / Antigravity CLI 上的 harness 结果。
