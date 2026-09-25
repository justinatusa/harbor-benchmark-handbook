# MANIFEST

- slug: mathvision
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://github.com/mathvision-cuhk/MATH-V

## 官方仓

- 入口 URL 会打开到 https://github.com/mathllm/MATH-V 。对 `mathvision-cuhk/MATH-V` 的 GitHub API 返回的 `full_name` 是 `mathllm/MATH-V`。
- 核实到的官方仓: https://github.com/mathllm/MATH-V
- 两个 URL 的 `git ls-remote` HEAD 是同一个 SHA。
- 默认分支: main
- commit SHA: a1f5cc3add200c0cd080fad463e500f44ef1fb41
- message: “Update README.md”。committer 日期 2025-05-16T04:37:15Z。
- 许可证: MIT（仓内 `LICENSE`，GitHub license 字段 MIT）。
- GitHub API `size`: 71908 KB。该 SHA 的递归 git tree 未截断，3126 个 blob，合计 145,726,794 字节。大头是 `images/` 以及 `data/`、`outputs/` 里的 jsonl。
- 评测代码在仓内：`evaluation/evaluate.py`、`evaluation/utils.py`、`models/` 下的各模型脚本。没有 Dockerfile。

## 论文 / blog / HF

- 论文: arXiv [2402.14804](https://arxiv.org/abs/2402.14804)，“Measuring Multimodal Mathematical Reasoning with MATH-Vision Dataset”。NeurIPS 2024 Datasets and Benchmarks。会议 PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/ad0edc7d5fa1a783f063646968b7315b-Paper-Datasets_and_Benchmarks_Track.pdf
- 项目页 / 榜: https://mathllm.github.io/mathvision/ （README 另给 `#leaderboard` 与 `#openleaderboard`）。
- 没有单独的产品 blog URL。README 新闻里点了别人的模型报告，那些不是本数据集的官方说明。
- HF id: `MathLLMs/MathVision`。API `sha` `2837ddb3f13abaf6b3997c12d80753e5470bd46a`，`lastModified` 2026-06-10T07:04:16.000Z，卡片许可证 mit，`gated` false。卡片 tags 里还有 arXiv:2501.12599，那是 README 新闻引用的 Kimi k1.5 报告，不是本数据集论文。
- 该 HF 修订 7 个文件，合计 116,304,351 字节：`data/test-….parquet` 56.9 MB，`images.zip` 52.4 MB，`data/testmini-….parquet` 7.0 MB，另有 `eval.yaml`。
- HF README 还介绍了 Math-Vision-Wild（`MathLLMs/MathVision-Wild`）。那是后来的实拍变体，不是这次入口指向的 MATH-V 主集。

## 测什么

测多模态模型做带图数学竞赛题的准确率。出处: 该 SHA 的 README「Introduction」，以及 arXiv:2402.14804 摘要：3,040 题，16 个学科，5 档难度，来自真实数学竞赛。README 写开卷与选择大约各半（论文摘要的原句是 1,532 道开放题、1,508 道选择题）。

## 环境线索

- 容器: 该 SHA 没有 Dockerfile 或 compose。unknown。
- 出网: README 的 Gemini / GPT 示例是调用 API 并写出 jsonl。数据集也可以从 HF 下。官方仓自己带了 `data/test.jsonl` 和 `images/`，所以计分不必再下 HF。
- GPU: README 的评测步骤没有写 GPU。`models/` 里有 Qwen-VL 等脚本，本次没有打开它们的设备要求。GPU: unknown。
- K8s: 没看到。unknown。
- 多容器: 没看到。unknown。

## 评分

官方 `evaluation/evaluate.py` 不另调 judge 模型。它从回答里用规则抽出最终答案（`boxed`、`the answer is`、选项字母），再调用 `utils.is_equal` 做字符串与 LaTeX 数值等价，按学科和难度算准确率。抽不出或对不上记为不正确。README 新闻（2024-07-19）另写 VLMEvalKit 支持 MATH-V，并用 LLM 做答案抽取。那是另一条路径，本次没有打开 VLMEvalKit 的代码。

## agent / runtime

`models/*.py` 是直接调 Gemini、GPT-4V、Qwen-VL 等的脚本。仓内没有工具循环、沙箱或 agent harness。agent 线索：unknown。

## 体积与是否入 git

- 官方 git checkout 约 145.7 MB，GitHub `size` 也大于 5 MB，没有克隆进 `/workspace`。
- HF 约 116.3 MB，没有下载。
- 本目录只有 MANIFEST 和 `evaluate.py` 的短摘录。本次没有 git commit。

## 未抓取项与原因

- `images/`、`data/*.jsonl`、`outputs/`：整仓超过 5 MB。`data/gpt4v-captions.jsonl` 单文件 4,539,741 字节，`data/test.jsonl` 1,741,681 字节。
- HF `images.zip` 与 parquet：同样超过 5 MB，且与 git 里的图重复存放。
- Math-Vision-Wild：HF 卡片上的另一数据集，不是本 slug 的入口。
- VLMEvalKit 的 LLM 抽取实现：README 只点了名字。
- 论文 PDF 没有存本地。
- 没有跑 `evaluation/evaluate.py`。

MANIFEST-END
