# MATH-Vision

官方仓没有 Dockerfile。评测步骤没有写 GPU，`models/` 里 Qwen-VL 的设备要求没有打开。

1. 一句话测什么。测多模态模型做带图数学竞赛题的准确率，3,040 题，16 个学科，5 档难度，来自真实数学竞赛。出处是 commit `a1f5cc3add200c0cd080fad463e500f44ef1fb41` 的 README「Introduction」，以及 https://arxiv.org/abs/2402.14804 摘要。README 写开卷与选择大约各半。论文摘要写 1,532 道开放题、1,508 道选择题。

2. 官方源。仓库 https://github.com/mathllm/MATH-V ，commit `a1f5cc3add200c0cd080fad463e500f44ef1fb41`（2025-05-16，说明 “Update README.md”）。入口 https://github.com/mathvision-cuhk/MATH-V 与这个仓的 HEAD 是同一个 SHA。论文 https://arxiv.org/abs/2402.14804 。项目页 https://mathllm.github.io/mathvision/ 。数据集 https://huggingface.co/datasets/MathLLMs/MathVision ，修订 `2837ddb3f13abaf6b3997c12d80753e5470bd46a`，`gated` 为 false。许可证 MIT。

3. 形态。`dataset`、`verifier`。`models/*.py` 是直接调模型的脚本。公开材料没有容器形式的 environment，也没有 Harbor adapter。agent 线索是 unknown。

4. 与 Harbor 距离。重改造。题和 `evaluation/evaluate.py` 公开，规则抽出答案后做字符串和数值等价，不另调模型。没有 Harbor `task.toml`。抽到的 Qwen-VL 脚本调用 DashScope 的 `qwen-vl-max`，不要求本机显卡。

5. 环境。该 SHA 没有 Dockerfile 或 compose。调用 Gemini、GPT 的示例要出网。仓内自带 `data/test.jsonl` 和 `images/`，计分不必再下 Hugging Face。GPU：unknown。Kubernetes：unknown。多容器：unknown。

6. 评分。不另调模型。`evaluation/evaluate.py` 从回答里抽出最终答案（`boxed`、`the answer is`、选项字母），再调用 `utils.is_equal` 做字符串与 LaTeX 数值等价，按学科和难度算准确率。抽不出或对不上记为不正确。README 新闻（2024-07-19）另写 VLMEvalKit 支持 MATH-V，并用 LLM 做答案抽取。那是另一条路径，清单没有打开那份代码。

7. agent/runtime。`models/*.py` 直接调 Gemini、GPT-4V、Qwen-VL。仓内没有工具循环、沙箱或 agent harness。

8. 迁入代价。中。评分脚本在仓内。没有 task 目录。抽到的 Qwen-VL 路径走 API，不要求本机显卡。

9. 对抽象的压力。`dataset` 没有 `dataset.toml`。`environment` 没有镜像。Qwen-VL 脚本走 API。

10. 本地摘录。[`notes/sources/mathvision/MANIFEST.md`](../../notes/sources/mathvision/MANIFEST.md)。
