# Finance Agent Benchmark v2

榜上计分用的 Test 450 题不在公开仓。公开仓有 27 道样本、工具循环和两小时上限。三模型 jury 的代码不在这个 commit。

1. 一句话测什么。测 agent 能否做入门级金融分析师的工作，依据公开公司文件回答需要多步、精确数字和行业惯例的问题。出处是 https://vals.ai/benchmarks/fabv2 的 Background。页面标注 Updated 9/23/2026。

2. 官方源。页面 “accessed here” 指向 https://github.com/vals-ai/finance-agent-v2 ，`main` HEAD `502aab6fdaa3fb9294905c7453f89882baa8d39b`（2026-09-21，说明 “Merge pull request #14 from vals-ai/ss/native-helper-capture”），MIT。没有 Hugging Face dataset id。页面让引用 https://arxiv.org/abs/2508.00828 ，bib 题名是 Finance Agent Benchmark（Bigeard 等，2025）。这是 v1 论文条目，页面没有另给 v2 的 arXiv id。

3. 形态。`agent`、`dataset`、`verifier`。公开 `data/public.csv` 有 27 道题和 `Rubric` 列。该 commit 的树有 21 个文件，没有 `environment` 定义。jury 代码不在公开仓。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。公开样本和 rubric 文本在仓里，没有 Harbor task 目录。正式 Test Suite 要平台 ID，不在这个 commit。评分要另调三模型 jury。清单没有给出 `task.toml` 或 `dataset.toml`。

5. 环境。该 commit 没有 Dockerfile 或 compose。要出网。工具打到 Tavily、SEC EDGAR（sec-api）和 Tiingo。README 要求 `TAVILY_API_KEY`、`SEC_EDGAR_API_KEY`、`PRICING_DATA_API_KEY`，以及所选模型的 API key。`pyproject.toml` 依赖里没有 GPU 包。GPU、Kubernetes、多容器都没看到，记 unknown。

6. 评分。要另调模型。页面写三模型 jury：GPT-5.4、Gemini-3.1-Pro、Claude Sonnet 4.6。主分 Partial Credit 是 dealbreaker 闸门后的加权 check 均分，任一 dealbreaker 失败则该题为 0。All-Pass 要每个 check 都过。页面上的结果只用 Test。公开仓没有这套 jury 的代码。`data/public.csv` 的 `Rubric` 列是检查项文本，不是打分程序。

7. agent/runtime。Python 包 `finance-agent`，入口 `finance_agent.run_agent:main_sync`，依赖 `model-library==0.1.33`。`finance_agent/get_agent.py` 把单次运行上限写成 `MAX_TIME_SECONDS = 2 * 60 * 60`，与页面的两小时一致。`finance_agent/tools.py` 的 `VALID_TOOLS` 是 `web_search`、`retrieve_information`、`parse_html_page`、`edgar_search`、`calculator`、`price_history`。README 的工具列表漏了 `calculator`，以代码和页面为准。系统提示把“当前日期”写成 2026-03-01，并用 `submit_final_result` 交卷。`retrieve_information` 会再调一个 LLM 去读已经存下的 HTML，这是做题工具，不是 jury。Private Validation / Test 要 Vals platform 的 Test Suite ID，README 写该平台需审批。仓里没有 `suites.json`。

8. 迁入代价。高。27 道公开题可以读，Test 450 与 Private Validation 450 不在这个 commit。jury 提示词和 dealbreaker 标注要向平台要。没有任务目录。

9. 对抽象的压力。`dataset` 的计分题不在公开 commit，公开 CSV 只有 27 行。`verifier` 的 jury 代码不在仓里，dealbreaker 失败整题为 0。`agent` 是本机两小时工具循环，要三把数据接口密钥。没有容器可接成 `environment`。

10. 本地摘录。[`notes/sources/finance-agent-v2/MANIFEST.md`](../../notes/sources/finance-agent-v2/MANIFEST.md)。
