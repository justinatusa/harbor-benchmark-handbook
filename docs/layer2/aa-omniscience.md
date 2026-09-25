# AA-Omniscience

公开集是全量 6,000 题的 10%，600 题。指数公式是程序，四档标签来自另一个模型。评测当时不是 agent。批量评测代码没有公开仓。

1. 一句话测什么。用权威来源抽出的事实题测模型的跨域回忆和弃答校准。全量 6,000 题、6 个域、42 个题目，公开集 600 题。出处是 arXiv 2511.13029 摘要，以及 https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public 的 README。公开集用来看总体指数，不适合当域或题目级结论。

2. 官方源。GitHub 上没有核实到的官方代码仓。`ArtificialAnalysis` 组织的公开仓里没有 Omniscience。数据集 https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public ，`main` HEAD `e4883edbb9f5ccf2b2a8fdc6fb65e01a58e99849`（2026-08-24，说明 “add_subtopic (#7)”），`gated` false，apache-2.0。论文 https://arxiv.org/abs/2511.13029 。榜单页 https://artificialanalysis.ai/evaluations/omniscience 。该 SHA 的 `AA-Omniscience_dataset_public.csv` 是 154,615 字节，点数 601 行含表头。

3. 形态。`dataset`、`verifier`。评测是无工具的单次作答，没有 `agent`，也没有 `environment` 容器。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。四档标签要另调 judge。清单没有给出 `task.toml` 或 `dataset.toml`。

5. 环境。未见容器。评测材料写模型作答时无上下文、无工具。评分模型要另一次模型调用，因此评分侧要能访问该模型。被测模型怎么托管，公开材料没写。GPU、Kubernetes、多容器都没看到，记 unknown。

6. 评分。要另调模型。回答先被分成 correct、partially correct、incorrect、not answered。论文第 2.3 节和 HF README 都写评分模型是 Google Gemini 2.5 Flash Preview (09-2025) with reasoning。指数本身是确定性公式：OI = 100 × (c − i) / (c + p + i + a)，范围 −100 到 100。c 正确，p 部分正确，i 错误，a 弃答。0 表示答对与答错一样多。标签不是字符串全等。榜单页另定义 hallucination rate 为 incorrect / (incorrect + partial answers + not attempted)。

7. agent/runtime。评测当时不是 agent。论文写答案不依赖上下文或工具，提示要求不确定就弃答。题目生成阶段用了 question generation agent，那是造数据，不是被测运行时。Artificial Analysis 自己的批量评测代码没有公开仓。被测运行时记 unknown。

8. 迁入代价。高。600 题的公开 CSV 可以读，全量 6,000 不在这个仓。没有任务目录，也没有批量运行代码。评分要固定 Gemini 2.5 Flash Preview 这一档，换模型标签会变，指数公式本身不会把标签变回字符串匹配。

9. 对抽象的压力。`verifier` 的标签来自另一个模型，指数只是把四档计数代进公式。`dataset` 公开的是 10% 子集，列里带答案。现有说明是单次无工具作答，没有代理循环可以接到 `agent`，也没有容器可接成 `environment`。

10. 本地摘录。[`notes/sources/aa-omniscience/MANIFEST.md`](../../notes/sources/aa-omniscience/MANIFEST.md)。
