# AA-LCR v1.1

v1.1 改了 16 个答案键，并给等价判断加了 system prompt。题目和文档集没变。README 写 v1.0.0 的分数不能和 v1.1 直接比。没有公开的批量运行仓。

1. 一句话测什么。用 100 道开放题测模型能否从约 1 万到 10 万 token 的长文档里抽取、连接并推理。文档集平均约 10 万 token（cl100k_base）。答案不能从单处直接抄出。出处是 https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning 页首，以及该 commit 的 HF README。

2. 官方源。GitHub 上没有核实到的官方代码仓。数据集 https://huggingface.co/datasets/ArtificialAnalysis/AA-LCR ，`main` HEAD `9a77ef56b717057ade24ceab4d273712a0b4f19e`（2026-09-04，说明 “v1.1: correct 16 answer keys and document the judge system prompt (#12)”），`gated` false。题集许可 apache-2.0。README 写文档文本是公开材料的文本表示，作者不对其主张版权。v1.0.0 仍在 revision `bdae010bbce259820c0e34c1d7cce210d966fb75`（2025-12-08）。本 slug 对的是 v1.1 的 `main`。没有找到 AA-LCR 自己的 arXiv id。公告 https://artificialanalysis.ai/articles/announcing-aa-lcr 描述的是最初发布，不是这 16 处答案更正。该 SHA 的 `AA-LCR_Dataset.csv` 是 145,408 字节、101 行含表头。`extracted_text/AA-LCR_extracted-text.zip` 是 4,023,468 字节。

3. 形态。`dataset`、`verifier`。公开材料是单次长上下文提示，没有 `agent`，也没有 `environment` 容器。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。等价判断要另调模型。清单没有给出 `task.toml` 或 `dataset.toml`。

5. 环境。未见容器。公开流程是把抽出的文档文本和问题放进同一次提示。文档 URL 列在 CSV 里，但 README 让评测读 zip 里的已抽出文本。等价判断要另调模型，因此评分侧要能访问该模型。GPU、Kubernetes、多容器都没看到，记 unknown。token 计数用 tiktoken 的 cl100k_base。

6. 评分。要另调模型。v1.1 的等价判断器是 GPT-5.6 Luna (medium)，带 system prompt，要求 JSON，verdict 为 CORRECT 或 INCORRECT。榜单页写 pass/fail，由另一个 LLM 判断与官方答案等价，分数是通过率平均。v1.0.0 没有 system prompt，只要求回复 CORRECT 或 INCORRECT。这不是本地字符串全等。

7. agent/runtime。公开材料没有 agent 或容器 runtime。评测是按 `data_source_filenames` 的顺序拼文档，再用 README 里的 prompt 模板做单次提示。造题时学生用过非前沿模型检查难度，那不是被测运行时。Artificial Analysis 的批量运行代码没有公开仓。被测运行时记 unknown。

8. 迁入代价。高。100 题和抽出的文档 zip 公开，但没有任务目录，也没有批量运行代码。评分要 GPT-5.6 Luna (medium) 这一套 prompt。用 v1.0.0 的答案键或无 system prompt 的判断，分数不能和 v1.1 直接比。

9. 对抽象的压力。`verifier` 的通过与否来自另一个模型的 CORRECT 或 INCORRECT，v1.1 还绑了 system prompt。`dataset` 的文档正文在 zip 里，CSV 含官方答案，v1.0.0 的 16 个键已经过时。现有说明是单次长上下文提示，没有代理循环可以接到 `agent`，也没有容器可接成 `environment`。

10. 本地摘录。[`notes/sources/aa-lcr-v1-1/MANIFEST.md`](../../notes/sources/aa-lcr-v1-1/MANIFEST.md)。
