# FrontierFinance

公开仓只跑 grader，输入是别人交来的 `system_summaries.json`。评分仓 README 写数据集 “public — no login”。Hugging Face 的 `gated` 却是 `auto`，匿名下载 JSONL 返回 401。

1. 一句话测什么。测公开数据上的投资研究全流程：220 条专家开放题、11,543 条带来源标注的二元 rubric，覆盖筛选发现到持仓监控。出处是 https://research.samaya.ai/benchmarks/frontier-finance 的 “220 public queries…”，以及 arXiv 2608.11683 摘要与第 1 节。

2. 官方源。评分代码 https://github.com/samaya-ai/frontier-finance ，`main` HEAD `cd51ad2b14dab298cf11151fb8d28a54613d7074`（2026-09-22，说明 “Merge pull request #4 from samaya-ai/dependabot/uv/anyio-4.14.2”），Apache-2.0。这个仓不含被测 agent。论文 https://arxiv.org/abs/2608.11683 。blog https://samaya.ai/blog/frontier-finance 。数据集 `samaya-ai/FrontierFinance` ，https://huggingface.co/datasets/samaya-ai/FrontierFinance ，sha `36afd6dc1cbb2c4512536daf917dc28b1225a720`，卡片许可 cc-by-4.0，`gated: auto`。JSONL `frontier_finance_public.jsonl` 在 tree API 上是 4,855,986 字节，正文未下载。

3. 形态。`dataset`、`verifier`。公开仓没有被测 `agent` 循环，也没有 `environment` 定义。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。每条 rubric 要另调 judge，再多数票。清单没有给出 `task.toml` 或 `dataset.toml`。匿名拿不到 JSONL。

5. 环境。评分仓文件树 25 个 blob，未见 Dockerfile。grader 调 judge API。论文第 6 节的被测设置还要公开网页检索、SEC、行情；附录 D 写 Azure OpenAI、Vertex、Fireworks。论文写被测模型走托管 API。本地 GPU、Kubernetes、多容器都没写成评测条件，记 unknown。

6. 评分。要另调模型。每条 rubric 由多名 LLM 独立打二元分，再多数票。README 与 `eval.example.yaml` 的默认三模型是 `claude-sonnet-4-6`、`gemini-3.1-pro-preview`、`gpt-5.4`。论文第 5 节写同一组：GPT 5.4、Gemini 3.1 Pro、Claude Sonnet 4.6。指标是 Rubric Qualification Rate。

7. agent/runtime。公开仓只跑 grader。论文第 6 节写了三种被测 harness，都限制在公开数据：厂商自带 web search；改编自 https://github.com/vals-ai/finance-agent-v2 的 LangChain 版（工具上限 200 次或 300 秒）；Samaya 内部生产 harness。内部 harness 源码不在这个公开仓，记 unknown。

8. 迁入代价。高。grader 公开，题面文件匿名下不来。被测检索回路要自备。评分要三模型多数票。没有任务目录。

9. 对抽象的压力。`verifier` 是三模型二元票，不是字符串比对。`dataset` 的 JSONL 在 gated 的 HF 仓，和 README 的 “no login” 不一致。`agent` 有三套被测设置，内部那套没有源码。没有容器可接成 `environment`。

10. 本地摘录。[`notes/sources/frontier-finance/MANIFEST.md`](../../notes/sources/frontier-finance/MANIFEST.md)。
