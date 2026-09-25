# MANIFEST

- slug: `perception-bench`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://github.com/MoonshotAI/PerceptionBench

## 官方仓

- 核实到的官方仓: https://github.com/MoonshotAI/PerceptionBench
- 默认分支: `master`（不是 `main`）
- commit SHA: `ba032c06e9b6ee3679171ff6ba643b7a0cfebe2e`
- 核实方式: `git ls-remote` 的 HEAD 与 GitHub commits API 均为该 SHA。提交说明为 “docs: update paper link and citation to arXiv 2607.24957”，committer 时间 2026-08-03T08:32:51Z。仓库描述为 “PerceptionBench: Evaluating Atomic Visual Perception in Multimodal Large Language Models”。许可证 Apache-2.0。

## 论文 / blog / HF

- 论文: arXiv:2607.24957，标题 “PerceptionBench: Evaluating Atomic Visual Perception in Multimodal Large Language Models”（arXiv abs 页 citation_title，citation_date 2026/07/27）。abs URL 抓取日返回 200。仓内 `paper/PerceptionBench.pdf` 约 11 MB。未比对 PDF 与 arXiv PDF。
- Blog: README 写 https://www.kimi.com/blog/perception-bench 。抓取日 HEAD 落到 https://www.kimi.ai/blog/perception-bench 并返回 200。正文未摘。
- 数据集: https://huggingface.co/datasets/moonshotai/PerceptionBench 。HF dataset API 的 `sha` 为 `6ba8c3135c7675ad6a5c141536a86b9460c70960`，tag 含 `arxiv:2607.24957`。tree 上 `PerceptionBench.jsonl` 为 1,626.80 MB，13 个文件合计 1,629,854,904 字节（约 1.63 GB）。该 git commit 的工作树里没有这份 jsonl。

## 一句话测什么

测多模态大模型的原子视觉感知：3000 道短答案题，每题只压一个感知能力，难度来自感知而不是推理或知识。出处：该 commit 的 `README.md` Abstract 与 Dataset Statistics（“3,000 verified questions across the ten atomic perceptual capabilities”；十类在榜单表头展开为 visual relation、counting、attribute、depth & 3D、localization、comparison、fine-grained recognition、contextual integration、OCR、perception-related hallucination）。

## 环境线索

- 容器: unknown。该 commit 未见 Dockerfile 或 compose。
- 出网: 被测模型和 judge 都走同一个 OpenAI 兼容 HTTP 端点。`eval/eval.py` 读取 `OPENAI_API_KEY` 与 `OPENAI_BASE_URL`。数据集在 HF，不在 git 里，下载要出网。
- GPU: unknown。仓库评测脚本不加载本地权重，也未见 CUDA。若端点背后的模型要 GPU，脚本未写。
- K8s: unknown。未见清单。
- 多容器: unknown。未见多容器编排。并发是本机 `ThreadPoolExecutor`（默认 `CONCURRENCY=16`）。

## 评分

要另外的 judge 模型。`README.md` Leaderboard：“GPT-oss-120B judges each response against the reference”。`eval/eval.py` 默认 `JUDGE_MODEL=gpt-oss-120b`，与必填的 `MODEL` 分开。judge 调用 `temperature=0.3`。提示词在 `eval/judge_prompt.txt`，要求输出 `[reason]` 与 `[judge]`，`[judge]` 里出现 `true` 记 1，否则记 0。预测拿不到或 judge 抛错时记 0。汇总是 overall 与按 `error_category` 的准确率，写入 `results/PerceptionBench_<model>_scores.json`。`.env.example` 写被测模型与 judge 共用这一套 endpoint 凭据。

## agent / runtime 线索

`eval/eval.py` 对每条记录发一次 chat completion（题面文本加 `image_url`），再发一次 judge completion。未见工具调用、多步计划或独立 agent runtime。图片在消息里是 URL 字符串；jsonl 本体未下载，不知道这些 URL 是 http 链接还是 data URL。

## 体积与是否入 git

- GitHub API `size`: 13216 KB。浅克隆在 `/tmp` 约 27 MB：`.git` 约 14 MB，`paper/` 约 11 MB，`images/` 约 3.0 MB，`eval/` 约 20 KB。
- 题目文件在 HF，约 1.63 GB，不在该 git commit。
- 本目录不放入克隆、PDF 或 jsonl。只留本文件与 `excerpt.md`。本线程不 git commit。

## 未抓取项与原因

- 未把约 27 MB 的浅克隆留在 `/workspace`。
- 未下载约 1.63 GB 的 `PerceptionBench.jsonl`，因此没有核对 3000 行，也没有看图片字段的实际编码。
- 未把 11 MB 论文 PDF 复制进本目录。
- Blog 只确认了跳转后的 URL 返回 200，未摘正文。
- 未跑 `eval/eval.py`（需要端点凭据，且本地没有数据集文件）。

MANIFEST-END
