# mmmu-pro 摘录

抓取日 2026-09-24 Asia/Shanghai。

论文 https://arxiv.org/abs/2409.02813 摘要：

> This paper introduces MMMU-Pro, a robust version of the Massive Multi-discipline Multimodal Understanding and Reasoning (MMMU) benchmark. MMMU-Pro rigorously assesses multimodal models’ true understanding and reasoning capabilities through a three-step process based on MMMU: (1) filtering out questions answerable by text-only models, (2) augmenting candidate options, and (3) introducing a vision-only input setting where questions are embedded within images.

论文第 3.1 节：

> The overall performance score for MMMU-Pro is calculated as the average of scores from settings (2) and (3).

HF 卡 https://huggingface.co/datasets/MMMU/MMMU_Pro ：

> MMMU-Pro introduces a vision-only input setting and increases the number of candidate options from 4 to 10

datasets-server 2026-09-24：`standard (10 options)` 1730 行，`standard (4 options)` 1730 行，`vision` 1730 行，合计 5190 行；parquet 字节约 2,988,175,948。

`mmmu-pro/evaluate.py`，钉在 `268471d0d488258990025331c7528359c324aa25`：

> def eval_multi_choice: only they are exactly the same, we consider it as correct
> if len(candidates) == 0: pred_index = random.choice(all_choices)

`mmmu-pro/README.md` 同一 commit：

> python infer/infer_xxx.py [MODEL_NAME] [MODE] [SETTING]
> settings: standard(10 options) | standard(4 options) | vision
> python evaluate.py
