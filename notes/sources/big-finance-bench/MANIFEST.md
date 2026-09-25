# big-finance-bench

- slug: `big-finance-bench`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://github.com/Rogo-Technologies/big-finance-benchmark

## 官方仓

有。https://github.com/Rogo-Technologies/big-finance-benchmark ，默认分支 `main`，抓取时 HEAD `d794a65fe583edc6852b44c817b0a2aef33ca831`（2026-08-06T20:39:05Z，`Add grades and human workbooks`）。Apache-2.0。论文脚注与 README 都把这个 URL 写成 grading harness。

## 论文 / blog / HF

- 论文: arXiv:2606.03829（https://arxiv.org/abs/2606.03829）。抓取的是 arXiv HTML。
- 榜: https://bigfinancebench.com/ 。2026-09-24 打开返回 200，页面纯文本写 “Models 29 / Questions 928 / Updated Sep 17, 2026”，并写分数是 Gemini 3.1 Pro 与 Claude Opus 4.7 的两评委均值。HTML 未存盘。
- HF: `RogoAI/big-finance-benchmark`。数据集仓 sha `139d5a18fe3ae3203332e1ffd173dfd525e96e31`。`gated: false`。card license `cc-by-4.0`。datasets-server 的 `public_release` split 是 50 行。

## 一句话测什么

测金融研究答案能不能按分析师的推导步骤被审计：928 道专家开放题，每题配参考答案和分值 rubric，分数打在可见轨迹上的检索、口径和计算，而不只打最终数字。（arXiv:2606.03829 摘要与第 4.1 节）

公开能直接跑的是分层抽出的 50 题。论文附录 A 写全集在投稿时 withhold。榜页面仍写 Questions 928。

## 环境线索

- 容器: 仓内未见 Dockerfile。README 写 `python_exec` 是 5 秒超时的 subprocess，不是安全沙箱，并建议调用方自己用 `--network=none --read-only` 的容器包一层。论文第 4.1 节把 `python_exec` 写成 sandbox。两处用词不一致，以 README 的实现说明为准：官方 harness 没有交付隔离容器。
- 出网: 要。工具是 `web_search`（SerpAPI 或 Tavily）、`edgar_search`（SEC EDGAR）、`fetch_url`，再加上模型 API。
- GPU: 论文第 4.1 节写 “All model inference uses commercial hosted APIs … No on-site compute workers”。未见本地 GPU 要求。
- K8s: 未见。unknown。
- 多容器: 未见。unknown。

## 评分

要另外的 judge 模型。论文第 4.1 节：每条轨迹由 Gemini 3.1 Pro Preview 与 Claude Opus 4.7 独立评分，主指标是两点均值后的 rubric score（得到的分 / 总分，再对题宏平均）。另报 final-answer accuracy。README 写发布的 grades 里还有 GPT-5.5 作稳健性评委。不是程序对答案做确定性比对。

## agent / runtime

有公开 runtime。README：ReAct 循环，LiteLLM 统一消息，默认 50 turn，每题 3 次试验。工具四个加终止符 `final_answer`。论文写同一套公开来源工具，明确排除 FactSet、CapIQ、Bloomberg。agent 循环跑在执行 harness 的机器上；`python_exec` 是该机器上的子进程。

## 体积与是否入 git

- 代码仓: GitHub `size` 字段 2356（KB）。`git/trees` 递归 blob 合计 21,548,183 bytes（约 20.55 MiB），81 个文件。其中 `data/big_finance_subset.jsonl` 111,875 bytes。大于 5MB，未克隆进 `/workspace`。
- HF 文件树合计 264,977,716 bytes（约 252.70 MiB），大头是 `traces/*.jsonl`。datasets-server 只统计 `public_release` parquet：50 行、87,530 bytes，不含 traces。
- 入 git: 本目录只留本文件和 `excerpt.md`。仓、子集 JSONL、grades、traces 都不放进工作区。

## 未抓取项与原因

- 928 题全文：论文写投稿时不公开；仓与 HF split 都是 50 题。
- HF traces（最大单文件约 47.92 MiB）：超过本任务的留存上限，未下载。
- bigfinancebench.com 只核了页面文本开头，未存 HTML。
- 未安装、未跑 harness。论文与 README 对 `python_exec` 是否叫 sandbox 的用词冲突已记在环境节，未再读 `big_finance_harness/` 源码逐行对实现。

MANIFEST-END
