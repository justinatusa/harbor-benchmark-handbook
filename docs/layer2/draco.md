# DRACO

题和 rubric 在 Hugging Face。论文脚注里的打分库不是这套题的任务仓。被测的是各家深度研究产品，产品内部循环没有随数据发布。

1. 一句话测什么。测深度研究系统答 100 道开放研究题时，事实、分析、表述和引用是否过关。题来自脱敏后的 Perplexity Deep Research 请求，覆盖 10 个领域。出处是 https://huggingface.co/datasets/perplexity-ai/draco 数据集卡首段，以及 arXiv 2602.11685 摘要。

2. 官方源。没有 GitHub 题面仓。数据集 https://huggingface.co/datasets/perplexity-ai/draco ，修订 `ce076749809027649ebd331bcb70f42bf720d387`（`lastModified` 2026-02-20，`gated` false，MIT）。论文 https://arxiv.org/abs/2602.11685 。文章 https://research.perplexity.ai/articles/evaluating-deep-research-performance-in-the-wild-with-the-draco-benchmark 。论文脚注把打分协议指到 https://github.com/The-LLM-Data-Company/rubric ，2026-09-24 该地址 301 到 https://github.com/paper-instruments/rubric ，main HEAD `eb0755a1c4682cd20c490550bd6260ccea8bafe0`（2026-02-03，说明 “fix: rename criterion_number to criterion_idx (#44)”）。那是打分库，不是题面仓。

3. 形态。`dataset`、`verifier`。HF 树上是 `LICENSE`、`README.md`、`test.jsonl`，没有 `environment` 定义，也没有 `agent` 循环。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。每条 rubric 要另调 judge 模型。清单没有给出 `task.toml` 或 `dataset.toml`。

5. 环境。论文和数据集卡都没写统一容器。被测系统要检索外部资料。论文第 5 节写 Perplexity、OpenAI、Gemini 的 deep research 接口，以及 Claude API 的 `web_search_20250305` 和 `code_execution_20250825`。judge 看的是已生成文本，不要求 judge 再上网核对。GPU、Kubernetes、多容器都没看到，记 unknown。

6. 评分。要另调模型。每条 rubric 由 judge 给 MET 或 UNMET。正权重做对了加分，负权重表示错误出现了就扣分。`raw_score` 是判定乘权重之和，归一化分是 raw_score 除以正权重之和，再夹到 0–100%。公式在数据集卡。论文写主 judge 是 Gemini-3-Pro；附录 D 用 GPT-5.2 和 Sonnet-4.5 复评，名次稳定、绝对分会变。每题 5 次评判。数据集卡写换 judge 时绝对分会变，比较必须固定 judge 配置。评分提示词见论文附录 F.5，HF 仓里没有单独的 prompt 文件。

7. agent/runtime。没有统一开源 agent。论文把被测对象当黑盒：Perplexity Deep Research（Opus 4.5 或 4.6）、Gemini `deep-research-pro-preview-12-2025`、OpenAI `o3-deep-research-2025-06-26` 与 `o4-mini-deep-research-2025-06-26`，以及带网页搜索和代码执行的 Claude Opus。这些产品的内部循环没有随数据集发布，记 unknown。

8. 迁入代价。高。`test.jsonl` 公开（HTTP Content-Length 909,190 字节），但没有任务目录。检索回路要自备。评分要固定一套 judge。

9. 对抽象的压力。`verifier` 的 reward 来自另一个模型的 MET 或 UNMET，正负权重还要分开。`agent` 的检索回路不在这个数据集仓里。`dataset` 是 `test.jsonl`，没有容器可接成 `environment`。

10. 本地摘录。[`notes/sources/draco/MANIFEST.md`](../../notes/sources/draco/MANIFEST.md)。
