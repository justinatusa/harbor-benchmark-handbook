# hle excerpts

抓取日 2026-09-24 Asia/Shanghai。不含题目、答案、图像或 parquet。

## 测什么

GitHub README @ `22ed3074b1e7b134bcbc09028d0ba320839b0655`，HF card 同文:

> Humanity's Last Exam (HLE) is a multi-modal benchmark at the frontier of human knowledge, designed to be the final closed-ended academic benchmark of its kind with broad subject coverage. Humanity's Last Exam consists of 2,500 questions across dozens of subjects, including mathematics, humanities, and the natural sciences.

数据集加载名: `cais/hle`，split `test`。

## 评分

`hle_eval/run_judge_results.py` 同一 SHA:

- `--judge` 默认 `o3-mini-2025-01-31`
- judge 提示要求 `correct: yes|no`，数值题允许小误差
- 指标打印 Accuracy 与 Calibration Error

## 运行时

`hle_eval/run_model_predictions.py`: `AsyncOpenAI` 单轮补全；`question['image']` 非空时附加 `image_url`。

`docs/evaluation-with-tools.md`: 工具轨禁止代码沙箱直接访问互联网，只暴露 `web_search` 与 `web_fetch`，并按模型使用各自的厂商 CLI harness。

## 引用

`citation.txt`: arXiv 2501.14249，doi 10.1038/s41586-025-09962-4。
