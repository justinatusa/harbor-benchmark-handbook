# Humanity's Last Exam

GitHub 仓放评测脚本。题目在 Hugging Face `cais/hle`，要先同意门禁，卡片还要求不要公开再分发。

1. 一句话测什么。用学科专家写的 2,500 道封闭题测前沿学术能力，覆盖数学、人文学科和自然科学。题型是选择题和短答案，并带图像字段。出处是该 commit 的 README 与数据集卡片同一段简介。

2. 官方源。代码 https://github.com/centerforaisafety/hle ，`main` HEAD `22ed3074b1e7b134bcbc09028d0ba320839b0655`（2026-09-23）。数据集 https://huggingface.co/datasets/cais/hle ，修订 `5a81a4c7271a2a2a312b9a690f0c2fde837e4c29`，`gated: auto`。论文 https://arxiv.org/abs/2501.14249 。

3. 形态。`dataset`、`verifier`。简单评测是单轮补全。带工具的说明才点名外部 `agent`。清单没写 `adapter`。

4. 与 Harbor 距离。暂不宜接。题目 gated，不能放进可再分发的 task 目录。评分要 judge 模型。清单没有给出 `task.toml` 或 `dataset.toml`。

5. 环境。简单评测脚本没有容器。`requirements.txt` 只有 `numpy==1.26.4`、`openai==1.57.0`、`datasets==3.2.0`。`load_dataset("cais/hle")` 访问 Hugging Face，预测和 judge 都走 OpenAI 接口。带工具的 `docs/evaluation-with-tools.md` 要求题目沙箱不能直接上网，外部信息只通过 `web_search` 和 `web_fetch`，该文件没有给出沙箱镜像名。简单脚本未见 GPU。本地权重要不要显卡，材料没写，记 unknown。Kubernetes 未见。多容器未见。

6. 评分。`hle_eval/run_judge_results.py` 的 `--judge` 默认 `o3-mini-2025-01-31`。judge 用结构化输出判断 `correct: yes` 或 `no`，数值题允许小误差。聚合指标是准确率，以及按 Hendrycks 校准实现算的均方根校准误差。

7. agent/runtime。简单评测用 `hle_eval/run_model_predictions.py` 做单轮对话。有 `image` 字段时把图像放进 `image_url`。带工具的文档点名 Claude Code、Codex CLI、Gemini CLI、Muse Code，并要求加载 `docs/blocklist.json`。这些程序的实现不在本仓。

8. 迁入代价。高。简单路径是单轮脚本加一次 judge 调用，没有自带镜像，也没有图形桌面。题目不能放进可再分发的 task 目录。带工具路径的沙箱镜像名仍是 unknown。

9. 对抽象的压力。`verifier` 由另一个模型判断对错，数值题还允许误差。`dataset` 带图像，而且不能公开再分发。带工具时 `agent` 在外部命令行里。

10. MANIFEST 路径。`notes/sources/hle/MANIFEST.md`
