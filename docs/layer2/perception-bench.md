# PerceptionBench

3,000 道短答案题在 Hugging Face 的 `PerceptionBench.jsonl` 里，不在这个 git 工作树。每题一次作答，再由 `gpt-oss-120b` 对照参考答案记 0 或 1。

1. 一句话测什么。测多模态模型的原子视觉感知：3,000 道短答案题，每题只压一个感知能力，难度来自感知而不是推理或知识。出处是 commit `ba032c06e9b6ee3679171ff6ba643b7a0cfebe2e` 的 README Abstract 与 Dataset Statistics。十类在榜单表头展开为 visual relation、counting、attribute、depth & 3D、localization、comparison、fine-grained recognition、contextual integration、OCR、perception-related hallucination。论文 https://arxiv.org/abs/2607.24957 。

2. 官方源。仓库 https://github.com/MoonshotAI/PerceptionBench ，默认分支是 `master`，HEAD `ba032c06e9b6ee3679171ff6ba643b7a0cfebe2e`（2026-08-03，说明 “docs: update paper link and citation to arXiv 2607.24957”），Apache-2.0。论文 https://arxiv.org/abs/2607.24957 。README 写 blog https://www.kimi.com/blog/perception-bench ，抓取日 HEAD 落到 https://www.kimi.ai/blog/perception-bench 。数据集 https://huggingface.co/datasets/moonshotai/PerceptionBench ，sha `6ba8c3135c7675ad6a5c141536a86b9460c70960`。tree 上 `PerceptionBench.jsonl` 为 1,626.80 MB，13 个文件合计约 1.63 GB。jsonl 正文未下载，因此没有在本地数到 3,000 行。

3. 形态。`dataset`、`verifier`。`eval/eval.py` 对每条记录发一次 chat completion，再发一次 judge。没有工具循环，没有 `environment` 容器。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。评分要另调 judge。清单没有给出 `task.toml` 或 `dataset.toml`。

5. 环境。该 commit 未见 Dockerfile 或 compose。被测模型和 judge 都走同一个 OpenAI 兼容 HTTP 端点。`eval/eval.py` 读取 `OPENAI_API_KEY` 与 `OPENAI_BASE_URL`。数据集在 HF，下载要出网。评测脚本不加载本地权重，也未见 CUDA。若端点背后的模型要 GPU，脚本未写，记 unknown。Kubernetes、多容器未见。并发是本机 `ThreadPoolExecutor`（默认 `CONCURRENCY=16`）。

6. 评分。要另调模型。README Leaderboard：“GPT-oss-120B judges each response against the reference”，并写与人工判断的一致率是 99.7%（300 条抽查）。`eval/eval.py` 默认 `JUDGE_MODEL=gpt-oss-120b`，与必填的 `MODEL` 分开。judge 调用 `temperature=0.3`。提示词在 `eval/judge_prompt.txt`，要求输出 `[reason]` 与 `[judge]`，`[judge]` 里出现 `true` 记 1，否则记 0。预测拿不到或 judge 抛错时记 0。汇总是 overall 与按 `error_category` 的准确率。`.env.example` 写被测模型与 judge 共用这一套 endpoint 凭据。

7. agent/runtime。没有工具调用、多步计划或独立 agent runtime。图片在消息里是 URL 字符串。jsonl 未下载，不知道这些 URL 是 http 链接还是 data URL，记 unknown。

8. 迁入代价。高。评测脚本公开，题面 jsonl 约 1.63 GB 且不在 git 里。每题要两次模型调用。没有任务目录。

9. 对抽象的压力。`verifier` 绑在 `gpt-oss-120b` 上，温度不是 0。`dataset` 的 jsonl 不在该 commit，图片字段的实际编码未核对。现有入口是一次补全，没有代理循环可以接到 `agent`，也没有镜像可接成 `environment`。

10. 本地摘录。[`notes/sources/perception-bench/MANIFEST.md`](../../notes/sources/perception-bench/MANIFEST.md)。
