# MANIFEST

- slug: `babyvision`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://github.com/UniPat-AI/BabyVision

## 官方仓

- 核实到的官方仓: https://github.com/UniPat-AI/BabyVision
- 默认分支: `main`
- commit SHA: `7f92fd4b1dc1c68b7b936a9bc09c68b4a944a55a`
- 核实方式: `git ls-remote` 的 HEAD 与 GitHub commits API 均为该 SHA。提交说明为 “add hf datasets”，作者 `callanwu`，committer 时间 2026-01-13T07:03:50Z。仓库描述为 “We introduce BabyVision, a benchmark revealing the infancy of AI vision.” GitHub API 的 license 字段为空。HF 数据集卡片写 MIT，与 GitHub 元数据不一致，未再核对仓内 LICENSE 文件（浅克隆根目录未见 LICENSE 文件名）。

## 论文 / blog / HF

- 论文: arXiv:2601.06521，标题 “BabyVision: Visual Reasoning Beyond Language”（arXiv abs 页 citation_title，citation_date 2026/01/10）。abs URL 抓取日返回 200。README 链到 https://arxiv.org/pdf/2601.06521 ，仓内另有 `BabyVision_Paper.pdf`（5,348,580 字节）。未比对 PDF 与 arXiv PDF 是否同一文件。
- Blog: https://unipat.ai/blog/BabyVision （抓取日 HEAD 200）。榜: https://unipat.ai/benchmarks/BabyVision （抓取日 HEAD 200）。正文未摘。
- README 的数据集徽章指向组织集合 https://huggingface.co/UnipatAI/collections ，不是单个 dataset id。按组织名查到并打开卡片、卡片回链同一 GitHub 的两个数据集:
  - https://huggingface.co/datasets/UnipatAI/BabyVision ，HF `sha` `849cbeea2b1d00ad334e9e1e2b49a1960c9ff3f3`，`data/train-00000-of-00001.parquet` 50.80 MB，tree 合计约 50.8 MB。
  - https://huggingface.co/datasets/UnipatAI/BabyVision-Gen ，HF `sha` `d4d7096acebfa778764aecb71dcbb52b74f7ec68`，parquet 75.30 MB，tree 合计约 75.3 MB。
- 同名搜索还出现 `kcz358/babyvision_gen` 与 `issai/BabyVision_Kazakh`。卡片不回链本仓，不当作官方集。

## 一句话测什么

测多模态模型做幼儿可解的视觉题，以及图像生成模型按指令在图上做标注。出处：该 commit 的 `README.md`：“Can MLLMs See Like a 3-Year-Old?”，以及 “BabyVision provides two evaluation tracks”：`babyvision_eval/`（MLLM）与 `babyvision_gen_eval/`（generation）。四类为 Fine-grained Discrimination、Visual Tracking、Spatial Perception、Visual Pattern Recognition。

在 `/tmp` 从 git 内 zip 抽出 `meta_data.jsonl` 计数（jsonl 大于 200 KB，未放入本目录）: MLLM 388 条（163 / 83 / 91 / 51，顺序同上四类）；生成 280 条（128 / 55 / 59 / 38）。生成轨 README 也写 280 tasks。zip 解压前体积: `babyvision_data.zip` 48 MB（列出 784 个成员、未压缩 51,484,537 字节），`babyvision_gen_data.zip` 71 MB（1132 个成员、76,131,269 字节），`mllm_results.zip` 37 MB。

## 环境线索

- 容器: unknown。该 commit 未见 Dockerfile 或 compose。
- 出网: 两条轨的推理和评判都走 HTTP API。MLLM 默认 `MODEL_BASE_URL` / `JUDGE_BASE_URL` 为 `https://openrouter.ai/api/v1`。生成轨要求 `OPENROUTER_API_KEY`。
- GPU: unknown。评测脚本用 API，未见 CUDA。本地图片解码只用 Pillow。
- K8s: unknown。未见清单。
- 多容器: unknown。未见多容器编排。`evaluate_model.py` 用本机 `multiprocessing.Pool`。

## 评分

两条轨都要另外的 judge 模型。

- MLLM: `README.md` 写 “Judging: LLM judge compares model output to ground truth”。`babyvision_eval/README.md` 默认 `JUDGE_MODEL_NAME=openai/gpt-5.2`，并注明 “or Qwen-Max”。`evaluate_model.py` 先让被测模型回答，再把抽出的 `\boxed{}` 答案交给另一个 OpenAI 兼容客户端；judge 回复里出现 `true` / `false` 才记对错，解析失败记错。`compute_score.py` 把多轮结果收成正确数/题数以及按 type、subtype 的均值和标准差。默认 `NUM_PASSES=3`。
- 生成: `babyvision_gen_eval/README.md` 写用 LLM 把生成图对到 ground-truth 图。默认 `LLM_MODEL=google/gemini-3-flash-preview`，与默认生成模型 `google/gemini-3-pro-image-preview` 不是同一个名字。指标仍是准确率及多轮 mean/std。

## agent / runtime 线索

MLLM 路径是单次 chat completion（图 + 文本），`extra_body` 里打开 `reasoning.enabled`，没有工具循环。生成路径是图像 API 再加一次评判调用。未见独立 agent runtime。被测模型和 judge 的密钥是分开的环境变量（MLLM 轨为 `MODEL_API_KEY` 与 `JUDGE_API_KEY`）。

## 体积与是否入 git

- GitHub API `size`: 172296 KB。浅克隆在 `/tmp` 约 329 MB：`.git` 约 164 MB，`data/` 约 155 MB，PDF 约 5.2 MB，`babyvision_gen_eval/` 约 3.8 MB（含若干生成样例图），`assets/` 约 1.9 MB，`babyvision_eval/` 约 188 KB。
- 题目与图片已经在该 git commit 的 zip 里，同时 HF 上有 parquet。
- 本目录不放入克隆、zip、PDF 或 jsonl。只留本文件与 `excerpt.md`。本线程不 git commit。

## 未抓取项与原因

- 未把约 329 MB 的浅克隆留在 `/workspace`。
- 未把 HF parquet 再下一次；git zip 已含 meta 与图片，parquet 是否与 zip 逐条相同未比对。
- 未把 5.2 MB 论文 PDF 复制进本目录，也未逐页读论文。
- Blog 与榜页只做了 HEAD，没有摘正文。
- 未跑推理或 judge（需要 API key）。
- GitHub license 为空与 HF 卡片 MIT 的差异未查到仓内许可证正文。

MANIFEST-END
