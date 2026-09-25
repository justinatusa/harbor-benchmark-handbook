# excerpt: charxiv

来源 commit `7ebe88f78dee387691551f071abcb2b9e1a8025b`。

`README.md` Introduction: “we propose CharXiv, a comprehensive evaluation suite involving 2,323 natural, challenging, and diverse charts from scientific papers. CharXiv includes two types of questions: (1) descriptive questions about examining basic chart elements and (2) reasoning questions that require synthesizing information across complex visual elements in the chart.”

`README.md` 评测: `python src/evaluate.py` 需要 OpenAI API key；结果文件 “stores your model's evaluation results graded by LLMs”。test 答案 “intentionally made to `null`”。图片下载命令为 `wget https://huggingface.co/datasets/princeton-nlp/CharXiv/resolve/main/images.zip`。

`src/descriptive_utils.py` 的 `get_descriptive_result_gpt` 调用 `model="gpt-4o-2024-05-13"`。`src/reasoning_utils.py` 同样写死该模型名。

本地核对（未把 JSON 复制进本目录）: descriptive/reasoning 的 val 各 1000 条且答案非空；test 各 1323 条且答案字段为 null。
