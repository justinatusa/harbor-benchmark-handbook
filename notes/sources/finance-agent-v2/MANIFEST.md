# finance-agent-v2

- slug：`finance-agent-v2`
- 抓取日：2026-09-24 Asia/Shanghai
- 入口 URL：https://vals.ai/benchmarks/fabv2
- 官方仓 URL 与 commit SHA：https://github.com/vals-ai/finance-agent-v2 ，`git ls-remote` HEAD `502aab6fdaa3fb9294905c7453f89882baa8d39b`（2026-09-21，`Merge pull request #14 from vals-ai/ss/native-helper-capture`）。默认分支 `main`。许可 MIT。页面 “accessed here” 的公开 harness 链接就是这个仓。没有 Hugging Face dataset id。
- 论文 / blog / HF id：页面让引用 https://arxiv.org/abs/2508.00828 ，bib 题名是 Finance Agent Benchmark: Benchmarking LLMs on Real-world Financial Research Tasks（Bigeard 等，2025-05）。这是 v1 论文条目，页面没有另给 v2 的 arXiv id。榜单页即 https://vals.ai/benchmarks/fabv2 ，页面标注 Updated 9/23/2026。
- 一句话测什么：测 agent 能否做入门级金融分析师的工作，依据公开公司文件回答需要多步、精确数字和行业惯例的问题。出处：https://vals.ai/benchmarks/fabv2 的 Background。
- 环境线索：
  - 容器：unknown。该 commit 的 tree 有 21 个文件，没有 Dockerfile 或 compose。
  - 出网：要。工具打到 Tavily、SEC EDGAR（sec-api）和 Tiingo 价格接口。README 要求 `TAVILY_API_KEY`、`SEC_EDGAR_API_KEY`、`PRICING_DATA_API_KEY`，以及所选模型的 API key。
  - GPU：unknown。`pyproject.toml` 依赖里没有 GPU 包。
  - K8s：unknown。
  - 多容器：unknown。
- 评分：要另外的 judge 模型。页面写三模型 jury：GPT-5.4、Gemini-3.1-Pro、Claude Sonnet 4.6。主分 Partial Credit 是 dealbreaker 闸门后的加权 check 均分，任一 dealbreaker 失败则该题为 0；All-Pass 要每个 check 都过。公开仓没有这套 jury 的代码。`data/public.csv` 带 `Rubric` 列，那是公开题的检查项文本，不是打分程序。
- agent / runtime 线索：Python 包 `finance-agent`，入口 `finance_agent.run_agent:main_sync`，依赖 `model-library==0.1.33`。`finance_agent/get_agent.py` 把单次运行上限写成 `MAX_TIME_SECONDS = 2 * 60 * 60`，与页面的两小时一致。`VALID_TOOLS` 是 `web_search`、`retrieve_information`、`parse_html_page`、`edgar_search`、`calculator`、`price_history`。系统提示把“当前日期”写成 2026-03-01，并用 `submit_final_result` 交卷。`retrieve_information` 会再调一个 LLM 去读已经存下的 HTML，这是做题工具，不是上面的 jury。Private Validation / Test 的运行要 Vals platform 的 Test Suite ID，README 写该平台需审批。
- 体积与是否入 git：
  - GitHub API `size` 467 KB。该 commit 递归 blob 合计 530,341 字节。其中 `uv.lock` 385,578 字节，`data/public.csv` 61,330 字节，`data/public.txt` 14,035 字节、27 行，与页面的 27 道公开样本一致。
  - 公开仓体积上可以进 git。本次只把清单和 `excerpt-grading.txt` 放在本目录，不把上游仓拷进本仓库。Test 450 题和 Private Validation 450 题不在公开仓里。
- 未抓取项与原因：
  - Test 与 Private Validation 的题目、dealbreaker 标注和 jury 提示词：页面写 Test 保持私有，Validation 要向 contact@vals.ai 授权。未下载。
  - 平台 `suites.json` 里的 Test Suite ID：README 说通过邮件或平台侧栏获取，仓里没有这个文件。
  - 没有把 `data/public.csv` 拷进本目录。题面和 rubric 在上游该路径，61 KB。
  - README 工具列表漏了 `calculator`，已用 `tools.py` 核对，不以 README 那五行作为完整工具表。

同目录摘录：`excerpt-grading.txt`。

MANIFEST-END
