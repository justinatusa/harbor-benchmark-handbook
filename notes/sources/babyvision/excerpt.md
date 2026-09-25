# excerpt: babyvision

来源 commit `7f92fd4b1dc1c68b7b936a9bc09c68b4a944a55a`。

`README.md`: “Can MLLMs See Like a 3-Year-Old?” “We introduce BabyVision, a benchmark revealing the infancy of AI vision.” 两条轨为 `./babyvision_eval/`（MLLM）和 `./babyvision_gen_eval/`（image generation）。评判句：“Judging: LLM judge compares model output to ground truth” 与 “Judging: LLM compares generated images to ground truth images”。

`babyvision_eval/README.md` 默认 judge: `JUDGE_MODEL_NAME=openai/gpt-5.2`，注释 “or Qwen-Max”。默认被测模型名 `google/gemini-3-flash-preview`，端点 `https://openrouter.ai/api/v1`。

`babyvision_gen_eval/README.md`: 生成默认 `MODEL=google/gemini-3-pro-image-preview`；评判默认 `LLM_MODEL=google/gemini-3-flash-preview`；`meta_data.jsonl` “Task definitions (280 tasks)”。

`/tmp` 计数（未把 jsonl 写入本目录）: MLLM zip 内 meta 388 行；生成 zip 内 meta 280 行。

HF 卡片回链本 GitHub 的数据集 id: `UnipatAI/BabyVision`、`UnipatAI/BabyVision-Gen`。README 徽章本身指向 https://huggingface.co/UnipatAI/collections 。
