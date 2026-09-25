# BabyVision

两条轨都要另调 judge。题目和图片在 git 的 zip 里，也在 Hugging Face。清单没有比对两处是否逐条相同。GitHub 的 license 字段为空，HF 卡片写 MIT，浅克隆根目录未见 LICENSE 文件。

1. 一句话测什么。测多模态模型做幼儿可解的视觉题，以及按指令在图上做标注。出处是 commit `7f92fd4b1dc1c68b7b936a9bc09c68b4a944a55a` 的 README：“Can MLLMs See Like a 3-Year-Old?”，以及 “BabyVision provides two evaluation tracks”：`babyvision_eval/`（MLLM）与 `babyvision_gen_eval/`（generation）。四类为 Fine-grained Discrimination、Visual Tracking、Spatial Perception、Visual Pattern Recognition。论文 https://arxiv.org/abs/2601.06521 。

2. 官方源。仓库 https://github.com/UniPat-AI/BabyVision ，`main` HEAD `7f92fd4b1dc1c68b7b936a9bc09c68b4a944a55a`（2026-01-13，说明 “add hf datasets”）。论文 https://arxiv.org/abs/2601.06521 。blog https://unipat.ai/blog/BabyVision 。榜 https://unipat.ai/benchmarks/BabyVision 。README 徽章指向 https://huggingface.co/UnipatAI/collections ，不是单个 dataset id。卡片回链本仓的两个数据集：https://huggingface.co/datasets/UnipatAI/BabyVision ，sha `849cbeea2b1d00ad334e9e1e2b49a1960c9ff3f3`；https://huggingface.co/datasets/UnipatAI/BabyVision-Gen ，sha `d4d7096acebfa778764aecb71dcbb52b74f7ec68`。从 git 内 zip 抽出的 meta：MLLM 388 条，生成 280 条。生成轨 README 也写 280 tasks。

3. 形态。`dataset`、`verifier`。两条轨都是一次生成再一次评判，没有独立 `agent` runtime，也没有 `environment` 容器。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。两条轨都要另调 judge。清单没有给出 `task.toml` 或 `dataset.toml`。

5. 环境。该 commit 未见 Dockerfile 或 compose。两条轨的推理和评判都走 HTTP API。MLLM 默认 `MODEL_BASE_URL` / `JUDGE_BASE_URL` 为 `https://openrouter.ai/api/v1`。生成轨要求 `OPENROUTER_API_KEY`。评测脚本未见 CUDA。GPU、Kubernetes、多容器都没看到，记 unknown。`evaluate_model.py` 用本机 `multiprocessing.Pool`。`babyvision_data.zip` 约 48 MB，`babyvision_gen_data.zip` 约 71 MB。

6. 评分。两条轨都要另调模型。MLLM：README 写 “Judging: LLM judge compares model output to ground truth”。`babyvision_eval/README.md` 默认 `JUDGE_MODEL_NAME=openai/gpt-5.2`，并注明 “or Qwen-Max”。`evaluate_model.py` 先让被测模型回答，再把抽出的 `\boxed{}` 答案交给另一个 OpenAI 兼容客户端；judge 回复里出现 `true` / `false` 才记对错，解析失败记错。默认 `NUM_PASSES=3`。生成轨：`babyvision_gen_eval/README.md` 写用 LLM 把生成图对到 ground-truth 图。默认 `LLM_MODEL=google/gemini-3-flash-preview`，与默认生成模型 `google/gemini-3-pro-image-preview` 不是同一个名字。

7. agent/runtime。MLLM 路径是单次 chat completion（图 + 文本），`extra_body` 里打开 `reasoning.enabled`，没有工具循环。生成路径是图像 API 再加一次评判调用。被测模型和 judge 的密钥是分开的环境变量（MLLM 轨为 `MODEL_API_KEY` 与 `JUDGE_API_KEY`）。

8. 迁入代价。高。题面在公开 git zip 里，但没有任务目录。两条轨都要准备 judge 密钥。浅克隆约 329 MB，不适合整仓塞进任务目录而不加筛选。

9. 对抽象的压力。`verifier` 两条轨都绑在另一个模型上，生成轨的评判模型名和生成模型名还不一样。`dataset` 同时在 git zip 和 HF parquet，清单没有做逐条核对。现有入口是一次补全，没有代理循环可以接到 `agent`，也没有镜像可接成 `environment`。

10. 本地摘录。[`notes/sources/babyvision/MANIFEST.md`](../../notes/sources/babyvision/MANIFEST.md)。
