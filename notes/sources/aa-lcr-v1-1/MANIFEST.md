# aa-lcr-v1-1

- slug: `aa-lcr-v1-1`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning

## 官方仓

- GitHub 上没有核实到的官方代码仓。`ArtificialAnalysis` 组织的公开仓里没有 AA-LCR。
- 数据集仓是 Hugging Face [ArtificialAnalysis/AA-LCR](https://huggingface.co/datasets/ArtificialAnalysis/AA-LCR)。
- `main` HEAD: `9a77ef56b717057ade24ceab4d273712a0b4f19e`
- 核实: datasets API 的 `sha` 与 commits API 第一条一致。日期 2026-09-04T08:41:58.000Z，message 为 “v1.1: correct 16 answer keys and document the judge system prompt (#12)”。`private` false，`gated` false。许可证：题集 apache-2.0；README 写文档文本是公开材料的文本表示，作者不对其主张版权。
- v1.0.0 仍在 revision `bdae010bbce259820c0e34c1d7cce210d966fb75`（2025-12-08，message “add document ordering snippets (#10)”）。本 slug 对的是 v1.1 的 `main` HEAD。

## 论文 / blog / HF

- 没有找到 AA-LCR 自己的 arXiv id。HF 引用是 dataset citation，作者 Artificial Analysis Team，年份 2025。
- 公告: https://artificialanalysis.ai/articles/announcing-aa-lcr 。页面返回 200。公告描述的是最初发布，不是 v1.1 的 16 处答案更正。
- HF id: `ArtificialAnalysis/AA-LCR`。
- 该 SHA 的文件: README.md 16,803 字节；`AA-LCR_Dataset.csv` 145,408 字节（本次点数为 101 行，含表头）；`extracted_text/AA-LCR_extracted-text.zip` 4,023,468 字节。

## 测什么

用 100 道开放题测模型能否从约 1 万到 10 万 token 的长文档里抽取、连接并推理，文档集平均约 10 万 token（cl100k_base）。出处: 入口页首段，以及该 commit 的 HF README。

## 环境线索

- 容器: 未见。记 unknown。
- 出网: 公开流程是把抽出的文档文本和问题放进同一次提示。文档 URL 列在 CSV 里，但 README 让评测读 zip 里的已抽出文本。等价判断要另调模型，因此评分侧要能访问该模型。
- GPU: 未见。记 unknown。
- K8s: 未见。记 unknown。
- 多容器: 未见。记 unknown。

## 评分

要另外的 judge 模型。v1.1 的等价判断器是 GPT-5.6 Luna (medium)，带 system prompt，要求 JSON，verdict 为 CORRECT 或 INCORRECT。榜单页写 pass/fail，由另一个 LLM 判断与官方答案等价，分数是通过率平均。v1.0.0 没有 system prompt，只要求回复 CORRECT 或 INCORRECT。README 写两个版本的分数不能直接比。这不是本地字符串全等。

## agent / runtime

公开材料没有 agent 或容器 runtime。评测是单次长上下文提示：按 `data_source_filenames` 的顺序拼文档，再用 README 里的 prompt 模板。造题时学生用过非前沿模型检查难度，那不是被测运行时。Artificial Analysis 的批量运行代码没有公开仓。被测运行时记 unknown。

## 体积与是否入 git

- CSV 145,408 字节，含答案，没有放进本目录。
- 文档 zip 4,023,468 字节，没有下载到 `/workspace`。
- 本目录只留本文件和 `excerpt-scoring.txt`。这两份可以进 git。没有 GitHub 全仓可入。

## 未抓取项与原因

- 没有 GitHub 代码仓。
- 未保存 CSV 和 extracted-text zip。zip 是文档正文，CSV 含官方答案。
- 未逐篇打开公告文的发布日期；v1.1 的日期以 HF commit 2026-09-04 为准。
- 未跑等价判断，也没有 GPT-5.6 Luna 的调用。

MANIFEST-END
