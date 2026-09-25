# OfficeQA Pro

评分脚本在 GitHub。133 道题和公报在 Hugging Face 上，下载前要同意门禁。

## 测什么

测系统能否在 1939 到 2025 年的美国财政部公报上，把散在表格和正文里的数字找出来，并做有依据的推理。

## 官方源

代码仓 https://github.com/databricks/officeqa ，commit `7b9a3c154ef9fb40215bb67934afc43e6799de16`（2026-08-06），代码许可 Apache-2.0。论文 https://arxiv.org/abs/2603.08655 。博客 https://www.databricks.com/blog/introducing-officeqa-benchmark-end-to-end-grounded-reasoning 。题目在 Hugging Face（HF）https://huggingface.co/datasets/databricks/officeqa ，修订 `763a8366abf2a3605c381d53586d844dc60fa756`，许可 CC-BY-SA-4.0。Pro 题文件是 `officeqa_pro.csv`，133 题。同仓的 Full 不是这个 slug。

## 形态

dataset、verifier、agent。评分在公开仓的 `reward.py`。没有 `task.toml`、`dataset.toml` 或 adapter。这个 commit 的树里没有 environment 定义。

## 与 Harbor 距离

暂不宜接。题目与语料 gated。评分是公开脚本，脚本不调用 judge 模型。材料没写图形处理器（GPU），也没写图形桌面。公开仓给出的是评分脚本和语料脚本。没有 `task.toml` 或 `dataset.toml`。

## 环境

这个 commit 没有 Dockerfile 或 compose。论文把 Python 交互解释器写成沙箱，用来挡住对语料的批量扫目录，没有写镜像。语料文件在本地。带网页搜索的设置要出网。只给提示、不用文档也不用工具的设置则不出网取公报。GPU、Kubernetes、多容器、图形桌面都没有写。

## 评分

`reward.py` 的 `score_answer` 做规范化后的数值容差和文本模糊匹配，返回 1.0 或 0.0。论文默认报告 0.0% 的绝对相对误差。容差是参数。

## agent / runtime

论文把 agent 基线写成自主调用工具、多步推理。工具有网页搜索接口、Python 解释器、`fs_search` / `fs_read`。README 记录的结果来自 Claude Agent SDK、Codex SDK、Gemini / Antigravity 命令行。这些循环不在本 commit 里。本仓提供评分和语料脚本。

## 迁入代价

中。评分函数已经在公开仓，但没有 Harbor 的 task 目录。语料约 4GB。HF 的 gated 为 auto，未登录不能下 `officeqa_pro.csv` 和公报文件。

## 对抽象的压力

压在 dataset 和 environment。题目和公报不在代码仓，下载前要在 HF 上同意条款。environment 没有镜像，论文里的沙箱只是一段说明。

## 本地摘录

私有摘录未随公开手册发布。
