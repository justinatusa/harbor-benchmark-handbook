# MANIFEST

- slug: `charxiv`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://github.com/princeton-nlp/CharXiv

## 官方仓

- 核实到的官方仓: https://github.com/princeton-nlp/CharXiv
- 默认分支: `main`
- commit SHA: `7ebe88f78dee387691551f071abcb2b9e1a8025b`
- 核实方式: `git ls-remote` 的 HEAD 与 GitHub commits API 均为该 SHA。提交说明为 “Merge pull request #14 from qzyou/patch-1”，committer 时间 2025-04-22T19:19:18Z。仓库描述为 “[NeurIPS 2024] CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs”。许可证 Apache-2.0。README 自称 Current Version: v1.0。

## 论文 / blog / HF

- 论文: arXiv:2406.18521，标题 “CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs”（arXiv abs 页 citation_title，citation_date 2024/06/26）。abs URL 抓取日返回 200。README 称 NeurIPS 2024 Datasets & Benchmarks，OpenReview https://openreview.net/forum?id=cy8mq7QYae （只按 README 记录）。
- 项目页: https://charxiv.github.io/ （抓取日 HEAD 200）。榜单锚点 README 写为 https://charxiv.github.io/#leaderboard 。
- 数据集: https://huggingface.co/datasets/princeton-nlp/CharXiv 。HF dataset API 的 `sha` 为 `f441eb632fc62f6f777830a0f47619e6e86459b0`，tag 含 `arxiv:2406.18521`。tree API 合计 240 个文件、375,857,094 字节（约 376 MB）。其中 `images.zip` 141.45 MB（对该 resolve URL 做 HEAD，content-length 141,454,217），`test.parquet` 91.67 MB，`val.parquet` 66.80 MB。已有模型输出在 `existing_evaluations/`。

## 一句话测什么

测多模态模型对科学论文图表的理解，分描述题（图表基本元素）和推理题（跨视觉元素综合）。出处：该 commit 的 `README.md` Introduction：“CharXiv, a comprehensive evaluation suite involving 2,323 natural, challenging, and diverse charts from scientific papers”，并写明 descriptive 与 reasoning 两类问题。

同一次浅克隆里数过 JSON：`data/descriptive_val.json` 与 `data/reasoning_val.json` 各 1000 条，`descriptive_test.json` 与 `reasoning_test.json` 各 1323 条。val 的 `answers` / `answer` 均非空；test 的对应字段 1323/1323 为 `null`。README 另写图片编号 0–2399、实际 2333 张且不连续；`images/README.md` 与 `data/README.md` 在该 commit 中是空文件，图片不在 git 树里。

## 环境线索

- 容器: unknown。该 commit 未见 Dockerfile、compose 或镜像名。
- 出网: 评分必须调 OpenAI API（`evaluate.sh` 与 `src/evaluate.py` 要 `api_key`）。图片要另从 HF 下载 `images.zip`。云端模型走各自 API（`src/generate_lib/` 里有 gpt、gemini、claude、reka、qwen 等）。本地权重推理不强制出网，但 README 的下载步骤要出网。
- GPU: 评分脚本不用 GPU。`src/generate_lib/` 里多个本地模型把权重放到 CUDA，`internvl2.py` 与 `nvlm.py` 按 `torch.cuda.device_count()` 切层，可占多卡。API 模型路径不要求本机 GPU。
- K8s: unknown。未见清单。
- 多容器: unknown。未见多容器编排。

## 评分

要另外的 judge 模型，不是字符串精确匹配。`src/evaluate.py` 用 OpenAI 客户端对 descriptive / reasoning 回答打分。`src/descriptive_utils.py` 与 `src/reasoning_utils.py` 把模型固定为 `gpt-4o-2024-05-13`；descriptive 调用使用 `temperature=0`、`top_p=1`、`seed=42`、`response_format=json_object`。`evaluate.sh` 注释写 “Query GPT-4o to grade responses”。test 答案在公开 JSON 里是 `null`，README 写 in-house 端到端评测应使用 `val`。

## agent / runtime 线索

生成循环是 `src/generate.py` 对每道题调用用户实现的 `generate_response`（`src/generate_lib/`）。输入是单张图路径加一道题。未见 agent 框架、工具循环或独立 runtime 进程。云端模型需要另写 `get_client_model`。

## 体积与是否入 git

- GitHub API `size`: 851 KB。浅克隆（`/tmp`，`--depth 1`）约 4.1 MB：`.git` 约 892 KB，`data/` 约 2.9 MB，`src/` 约 256 KB。
- 图表 `images.zip` 约 141 MB，在 HF，不在该 git commit。HF 全树约 376 MB。
- 本目录不放入克隆或图片包。只留本文件与 `excerpt.md`。本线程不 git commit。浅克隆虽小于 5 MB，仍不复制进 `/workspace`。

## 未抓取项与原因

- 未下载 `images.zip`、parquet，也未把 `existing_evaluations/` 的大 JSON 摘进来。
- 未跑 `generate.py` / `evaluate.py`，没有 OpenAI key。
- `images/README.md` 与 `data/README.md` 为空，图片清单以 README 正文和 HF tree 为准。
- 未逐张核对 README 的 2333 张图与 JSON 的 2323 条图题是否同一集合。

MANIFEST-END
