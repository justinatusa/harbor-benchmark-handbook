# aa-omniscience

- slug: `aa-omniscience`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://artificialanalysis.ai/evaluations/omniscience

## 官方仓

- GitHub 上没有核实到的官方代码仓。`ArtificialAnalysis` 组织的公开仓是 Stirrup、StirrupJS、optima、aiperf，没有 Omniscience 仓。
- 数据集仓是 Hugging Face [ArtificialAnalysis/AA-Omniscience-Public](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public)。
- `main` HEAD: `e4883edbb9f5ccf2b2a8fdc6fb65e01a58e99849`
- 核实: datasets API 的 `sha` 与 commits API 第一条一致。日期 2026-08-24T06:39:56.000Z，message 为 “add_subtopic (#7)”。`private` false，`gated` false。许可证 apache-2.0。

## 论文 / blog / HF

- 论文: arXiv [2511.13029](https://arxiv.org/abs/2511.13029)。abs 页只有 v1，提交 2025-11-17。标题 *AA-Omniscience: Evaluating Cross-Domain Knowledge Reliability in Large Language Models*。
- HF id: `ArtificialAnalysis/AA-Omniscience-Public`。公开集是全量 6,000 题的 10%，600 题。
- 榜单页就是入口 URL。HF README 也指向该页。没有另找的独立 blog id。
- 该 SHA 的文件: README.md 11,444 字节；`AA-Omniscience_dataset_public.csv` 154,615 字节（本次点数为 601 行，含表头）；论文 PDF 3,847,115 字节；题目分布图 167,741 字节。

## 测什么

用权威来源抽出的事实题测模型的跨域回忆和弃答校准，全量 6,000 题、6 个域、42 个题目，公开集 600 题。出处: arXiv 2511.13029 摘要，以及 HF README 对公开子集的说明。

## 环境线索

- 容器: 未见。记 unknown。
- 出网: 评测材料写模型作答时无上下文、无工具。评分模型要另一次模型调用，因此评分侧要能访问该模型。被测模型怎么托管，公开材料没写。
- GPU: 未见。记 unknown。
- K8s: 未见。记 unknown。
- 多容器: 未见。记 unknown。

## 评分

要另外的 judge 模型。回答先被分成 correct、partially correct、incorrect、not answered。论文第 2.3 节和 HF README 都写评分模型是 Google Gemini 2.5 Flash Preview (09-2025) with reasoning。指数本身是确定性公式：OI = 100 * (c - i) / (c + p + i + a)，范围 -100 到 100。标签不是字符串全等。榜单页另定义 hallucination rate 为 incorrect / (incorrect + partial answers + not attempted)。

## agent / runtime

评测当时不是 agent。论文写答案不依赖上下文或工具，提示要求不确定就弃答。题目生成阶段用了 question generation agent，那是造数据，不是被测运行时。Artificial Analysis 自己的批量评测代码没有公开仓。被测运行时记 unknown。

## 体积与是否入 git

- 公开 CSV 154,615 字节，含答案，没有放进本目录，不入 git。
- PDF 3.8 MB，没有下载到 `/workspace`。
- 本目录只留本文件和 `excerpt-scoring.txt`。这两份可以进 git。

## 未抓取项与原因

- 没有 GitHub 代码仓可克隆。
- 未保存 CSV、PDF 和分布图。CSV 是题库加答案，PDF 超过本目录摘录要用的篇幅。
- 未跑评分，也没有 Gemini 凭据。
- 全量 6,000 题不在这个公开仓里。

MANIFEST-END
