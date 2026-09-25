# MANIFEST

- slug: draco
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://huggingface.co/datasets/perplexity-ai/draco

## 官方仓

- 没有 GitHub 任务仓。HF 数据集页、论文和 Perplexity 文章都把数据放在这个 HF 仓库，没有另外的代码仓库链接。
- 数据集 git: https://huggingface.co/datasets/perplexity-ai/draco
- HF 修订: `ce076749809027649ebd331bcb70f42bf720d387`
- HF `lastModified`: 2026-02-20T23:02:24.000Z
- `gated`: false
- 文件 4 个: `.gitattributes`、`LICENSE`、`README.md`、`test.jsonl`
- `LICENSE` 是 MIT，版权 Perplexity AI, Inc. 2026
- 论文脚注把打分协议指到 https://github.com/The-LLM-Data-Company/rubric 。2026-09-24 该 URL 301 到 https://github.com/paper-instruments/rubric
- 跳转后仓库 main HEAD: `eb0755a1c4682cd20c490550bd6260ccea8bafe0`
- committer 日期: 2026-02-03T18:57:44Z
- 说明: fix: rename criterion_number to criterion_idx (#44)
- GitHub API `size`: 238 KB
- 这是论文引用的打分库，不是 DRACO 题面仓。没有把它当成 DRACO 官方任务仓。

## 论文 / blog / HF

- 论文: https://arxiv.org/abs/2602.11685
- PDF: https://arxiv.org/pdf/2602.11685
- 文章: https://research.perplexity.ai/articles/evaluating-deep-research-performance-in-the-wild-with-the-draco-benchmark
- HF id: `perplexity-ai/draco`
- 文章写会放出全部 rubric 和 judge prompt。HF 仓里没有单独的 prompt 文件；数据集卡写评分提示词见论文。论文附录 F.5 是 grading prompt。本次没有把附录全文摘下来。

## 测什么

测深度研究系统回答 100 道开放研究题时，事实是否对、分析是否够、表述是否清楚、引用是否到位。题来自脱敏后的 Perplexity Deep Research 请求，覆盖 10 个领域。出处：HF 数据集卡首段，以及 arXiv:2602.11685 摘要。

## 环境线索

- 容器: 论文和数据集卡都没写统一容器。unknown。
- 出网: 被测系统要检索外部资料。论文第 5 节写 Perplexity、OpenAI、Gemini 的 deep research 接口，以及 Claude API 的 `web_search_20250305` 和 `code_execution_20250825`。judge 本身看的是已生成的文本，不要求 judge 再上网核对。
- GPU: 没看到。unknown。
- K8s: 没看到。unknown。
- 多容器: 没看到。unknown。

## 评分

要另外的 judge 模型，不是确定性对答案。

每条 rubric 由 judge 给 MET 或 UNMET。正权重表示做对了加分，负权重表示错误出现了就扣分。归一化分是 raw_score 除以正权重之和，再夹到 0–100%。公式见 `excerpt-scoring.txt`。论文写主 judge 是 Gemini-3-Pro；附录 D 用 GPT-5.2 和 Sonnet-4.5 复评，名次稳定、绝对分会变。每题 5 次评判。数据集卡写换 judge 时绝对分会变，比较必须固定 judge 配置。

## agent / runtime

没有统一的开源 agent runtime。论文把被测对象当黑盒产品：Perplexity Deep Research（Opus 4.5 或 4.6）、Gemini `deep-research-pro-preview-12-2025`、OpenAI `o3-deep-research-2025-06-26` 与 `o4-mini-deep-research-2025-06-26`，以及带网页搜索和代码执行工具的 Claude Opus。复现这些产品内部循环的代码没有随数据集发布。unknown。

## 体积与是否入 git

`test.jsonl` 的 HTTP Content-Length 是 909,190 字节。HF API `usedStorage` 是 403,911 字节。两个数都在，未下载正文，所以没有逐字节核对压缩差。100 行 JSONL，单行 rubric 在数据集预览里大约 2.6–12.8 KB。

打分库约 238 KB。没有克隆进本仓。

本目录只有本文件和 `excerpt-scoring.txt`。本次没有 git commit。题面可以放进 git，但本次不复制 `test.jsonl`（超过单文件 200KB 摘录上限）。

## 未抓取项与原因

- `test.jsonl` 全文：909,190 字节，超过摘录上限。结构以数据集卡为准：`id`、`domain`、`problem`、`answer`（JSON rubric）。
- 论文附录 F.5 的 judge prompt 全文：没有单独文件，本次没有整篇保存。
- `paper-instruments/rubric` 只核实了 HEAD，没有通读是否与 DRACO 的字段一一对应。
- 各家 deep research 产品的容器、GPU 和内部代理循环：论文按黑盒评测，没有写。

MANIFEST-END
