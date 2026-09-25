# BigFinanceBench

论文全集是 928 道专家开放题。公开能直接跑的是分层抽出的 50 题。README 写 `python_exec` 不是沙箱；论文第 4.1 节把同一工具写成 sandbox。以 README 的实现说明为准：官方 harness 没有交付隔离容器。

1. 一句话测什么。测金融研究答案能不能按分析师的推导步骤被审计：每题配参考答案和分值 rubric，分数打在可见轨迹上的检索、口径和计算，而不只打最终数字。出处是 arXiv 2606.03829 摘要与第 4.1 节。摘要写 928 题。论文附录 A 写全集在投稿时 withhold，公开的是 50 题子集。榜页 https://bigfinancebench.com/ 在 2026-09-24 仍写 Questions 928。

2. 官方源。harness https://github.com/Rogo-Technologies/big-finance-benchmark ，`main` HEAD `d794a65fe583edc6852b44c817b0a2aef33ca831`（2026-08-06，说明 “Add grades and human workbooks”），Apache-2.0。论文 https://arxiv.org/abs/2606.03829 。榜 https://bigfinancebench.com/ 。数据集 https://huggingface.co/datasets/RogoAI/big-finance-benchmark ，sha `139d5a18fe3ae3203332e1ffd173dfd525e96e31`，`gated` false，cc-by-4.0。datasets-server 的 `public_release` split 是 50 行。仓内公开子集是 `data/big_finance_subset.jsonl`。

3. 形态。`agent`、`dataset`、`verifier`。公开能跑的是 50 题，不是 928。官方 harness 没有交付 `environment` 容器。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。评分要另调两个 judge。清单没有给出 `task.toml` 或 `dataset.toml`。做题要出网检索。

5. 环境。仓内未见 Dockerfile。README 写 `python_exec` 是 5 秒超时的 subprocess，不是安全沙箱，并建议调用方自己用 `--network=none --read-only` 的容器包一层。要出网。工具是 `web_search`（SerpAPI 或 Tavily）、`edgar_search`（SEC EDGAR）、`fetch_url`，再加上模型 API。论文第 4.1 节写 “All model inference uses commercial hosted APIs … No on-site compute workers”。未见本地 GPU 要求。Kubernetes、多容器未见，记 unknown。

6. 评分。要另调模型。论文第 4.1 节：每条轨迹由 Gemini 3.1 Pro Preview 与 Claude Opus 4.7 独立评分，主指标是两点均值后的 rubric score（得到的分 / 总分，再对题宏平均）。另报 final-answer accuracy。README 写发布的 grades 里还有 GPT-5.5 作稳健性评委。榜页纯文本写分数是 Gemini 3.1 Pro 与 Claude Opus 4.7 的两评委均值。不是程序对答案做确定性比对。

7. agent/runtime。有公开 runtime。README：ReAct 循环，LiteLLM 统一消息，默认 50 turn，每题 3 次试验。工具四个加终止符 `final_answer`。论文写同一套公开来源工具，明确排除 FactSet、CapIQ、Bloomberg。agent 循环跑在执行 harness 的机器上；`python_exec` 是该机器上的子进程。

8. 迁入代价。高。50 题和 harness 公开，928 题全文不在这个 commit。评分要两套 judge。官方没有交付隔离容器。没有 Harbor task 目录。

9. 对抽象的压力。`verifier` 是两个模型的 rubric 均值，不是最终数字的字符串比对。`dataset` 公开能跑的是 50 题，榜上仍写 928。`agent` 的检索在跑 harness 的机器上，`python_exec` 没有官方隔离容器，接不成现成的 `environment`。

10. 本地摘录。[`notes/sources/big-finance-bench/MANIFEST.md`](../../notes/sources/big-finance-bench/MANIFEST.md)。
