# hle

- slug: `hle`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://huggingface.co/datasets/cais/hle

## 官方仓

- 代码仓有。https://github.com/centerforaisafety/hle
- 默认分支 `main` HEAD: `22ed3074b1e7b134bcbc09028d0ba320839b0655`
- 核实: `git ls-remote` HEAD 与 commits API 一致。commit 日期 2026-09-23，message 为 “Block all jsDelivr hosts including npm and API paths”。
- 许可证: MIT。GitHub `size` 字段 1,531 KB。该 SHA 的文件树未截断，无 Dockerfile、compose 或 Kubernetes 文件。题目数据不在这个 git 仓里。
- 数据集仓是 Hugging Face `cais/hle`，不是 GitHub。API `sha` `5a81a4c7271a2a2a312b9a690f0c2fde837e4c29`，`gated: auto`。

## 论文 / blog / HF

- HF: [cais/hle](https://huggingface.co/datasets/cais/hle)。卡片写 test split 2,500 例，`download_size` 274,276,147，`dataset_size` 284,205,983。parquet 路径 `data/test-00000-of-00001.parquet`，API 记录的 LFS size 同为 274,276,147 字节。
- 论文: arXiv [2501.14249](https://arxiv.org/abs/2501.14249)。`citation.txt` @ 上述 GitHub SHA 记为 Nature 649, 1139–1146 (2026)，doi `10.1038/s41586-025-09962-4`，eprint 2501.14249。
- 网站: https://lastexam.ai （README 链接，本次未整站抓取）。没有单独的 blog id。

## 测什么

用学科专家写的 2,500 道封闭式题目测前沿学术能力，覆盖数学、人文学科和自然科学，题型是选择题和短答案，并且带多模态图像字段。出处: GitHub README 与 HF dataset card 的同一段简介（“final closed-ended academic benchmark … 2,500 questions”）。

## 环境线索

- 容器: 简单评测脚本里没有。`requirements.txt` 只有 `numpy==1.26.4`、`openai==1.57.0`、`datasets==3.2.0`。
- 出网: 简单评测需要。`load_dataset("cais/hle")` 访问 Hugging Face，预测和 judge 都走 OpenAI API。
- 带工具的另一份说明 `docs/evaluation-with-tools.md` 要求代码沙箱不能直接上网（不能下载、不能装包），外部信息只通过 `web_search` 和 `web_fetch`；调用被测模型的网络与题目沙箱网络分开。该文件没有给出沙箱镜像名。
- GPU: 简单脚本未见。模型是 API 名。本地权重推理未见说明，记 unknown。
- K8s: 未见。
- 多容器: 未见。

## 评分

要另外的 judge 模型。`hle_eval/run_judge_results.py` 的 `--judge` 默认 `o3-mini-2025-01-31`（注释写前一个默认是 `gpt-4o-2024-08-06`）。judge 用结构化输出判断 `correct: yes|no`，允许数值题的小误差，不是本地字符串相等。聚合指标是 accuracy 和按 Hendrycks calibration 实现算的 RMS calibration error。README 虽写 “suitable for automated grading”，发布的脚本仍是 LLM judge。

## agent / runtime

两条，都有文本证据。

- 简单评测: `hle_eval/run_model_predictions.py` 用 `AsyncOpenAI` 做单轮 chat completion。有 `image` 字段时把图像放进 `image_url`。默认温度在 README 里是 0；脚本里 `temperature=args.temperature` 一行被注释掉。这不是多轮 agent。
- 带工具: `docs/evaluation-with-tools.md` 标题是 “Evaluating HLE-Diamond with tools”。它点名外部 harness：Claude Code 2.1.278 / 2.1.280、Codex CLI 0.155.1、Gemini CLI 0.60.0、Muse Code 1.3.0，并要求加载 `docs/blocklist.json`。这些 CLI 的实现不在本仓。

数据集卡片要求不要公开再分发题目。本目录没有题目。

## 体积与是否入 git

- HF parquet 约 274 MB，且卡片写明不要公开分享或再上传。不进 git，也没有下载。
- GitHub 仓约 1.5 MB，本目录仍只留摘录，不整仓复制。
- 摘录可以进 git。公开 canary 字符串不在这里重复，见上游 README。

## 未抓取项与原因

- `eval.yaml`（API 显示 1,118 字节）匿名下载返回 401。数据集是 gated auto，没有用 token 去拉。
- 未下载 parquet，也未调用 `load_dataset`，因此没有题面、答案或图片。
- 未抓 https://lastexam.ai 全文。
- 未把 `docs/blocklist.json`（11,400 字节）整份抄进来；工具评测的屏蔽规则以 `evaluation-with-tools.md` 的字段说明为准，需要规则正文时再读上游。

MANIFEST-END
