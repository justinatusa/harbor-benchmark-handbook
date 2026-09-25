# OfficeQA Pro V2

90 道题和 1,435 份联邦收支 PDF 在 Hugging Face，下载前要同意门禁。评分脚本不在数据集仓，在 `databricks/officeqa` 的 `reward.py`，与 Pro 共用，不另调模型。

1. 一句话测什么。测 agent 能否在 1793–2024 年美国联邦收支账的 1,435 份 PDF 上做跨文档数值推理。卡片写这是 OfficeQA Pro（财政部公报）之外的一份新语料。出处是 https://huggingface.co/datasets/databricks/officeqa-pro-v2 卡片，以及 https://www.databricks.com/blog/introducing-officeqa-pro-v2-new-benchmark-enterprise-grounded-reasoning 。博客把同一基准写成约 1,400 份 PDF、约 120,000 页。

2. 官方源。数据集 https://huggingface.co/datasets/databricks/officeqa-pro-v2 ，Hub API `sha` `65a2b315780417bc50d7bfe6e5bdb904e63fda65`（`lastModified` 2026-08-06，`gated` 为 `auto`，CC-BY-SA-4.0）。题文件 `officeqa_pro_v2.csv`，90 题。没有单独的 Pro v2 代码仓。评分脚本在 https://github.com/databricks/officeqa ，HEAD `7b9a3c154ef9fb40215bb67934afc43e6799de16`（说明 “Merge pull request #53 from databricks/readme-officeqa-suite-pro-v2”）。卡片引用的技术报告仍是 Pro 的 https://arxiv.org/abs/2603.08655 。没有单独的 Pro v2 arXiv id。

3. 形态。`dataset`、`verifier`。`reward.py` 在公开 GitHub 仓。已发表 harness 的循环不在该 commit，也不在已读到的 HF 文件列表里。这个 commit 的树里没有 `environment` 定义。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。暂不宜接。题目与语料 gated。评分是公开脚本，脚本不调用 judge 模型。清单没有给出 `task.toml` 或 `dataset.toml`。

5. 环境。GitHub 代码树没有 Dockerfile。数据集卡片没有容器说明。README @ `7b9a3c15` 写 Pro v2 的已发表 agent harness 与 Pro 相同，包含 web search、文件搜索和代码执行。只读本地解析 JSON 时，卡片没有把出网写成必选项。Hub API `usedStorage` 14,131,884,104 字节。卡片写总大小 14.1 GB，PDF 约 13.3 GB，解析 JSON 约 794 MB，API 文件数 2879（含 1,435 个 PDF 与 1,435 个解析 JSON）。卡片写 90 题只引用其中 249 份文档。GPU、Kubernetes、多容器都没写，记 unknown。

6. 评分。确定性程序，不另调 judge。与 Pro 共用 `reward.py` 的 `score_answer`。卡片写它会规范化货币符号、千分位、会计负号、单位和百分号，标签类答案再退到文本重叠。返回 1.0 或 0.0，`tolerance` 可调。

7. agent/runtime。README 写已发表的 v2 结果使用 Claude Agent SDK、Codex SDK、Gemini / Antigravity CLI，并打开 file search、web search、code execution。这套循环的代码不在 GitHub 该 commit 里。本仓提供的是评分脚本。

8. 迁入代价。高。评分函数已经在公开仓，但没有 Harbor 的 task 目录。题面、PDF 和解析 JSON 都要先在 HF 上同意门禁。未登录不能下这些文件。

9. 对抽象的压力。`dataset` 接不上可再分发的任务目录，语料 gated，体积约 14.1 GB。`verifier` 是 `reward.py` 的数值容差和文本重叠，不另调模型。`agent` 的已发表循环不在这个 commit。没有镜像可接成 `environment`。

10. 本地摘录。[`notes/sources/officeqa-pro-v2/MANIFEST.md`](../../notes/sources/officeqa-pro-v2/MANIFEST.md)。
