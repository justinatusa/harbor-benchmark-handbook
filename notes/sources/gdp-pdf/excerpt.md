# gdp-pdf 摘录

抓取日 2026-09-24 Asia/Shanghai。

论文 https://arxiv.org/abs/2607.11192 摘要：

> GDP.pdf is a benchmark built to measure this directly. It consists of question–document pairs authored by working professionals in ten fields … Each item comes with a rubric of atomic criteria … The full 100-item benchmark is publicly available at https://huggingface.co/datasets/surgeai/GDP.pdf.

论文第 1 节脚注：

> Dataset: https://huggingface.co/datasets/surgeai/GDP.pdf ; evaluation harness: https://github.com/surge-ai/gdp-pdf.

论文第 4 节：

> Rubric criteria are graded by an LLM judge (Gemini 3.5 Flash) … The judge is given neither the source PDF nor the gold answer

论文第 5.1 节：

> each provider’s own document handling is therefore part of what is measured. No tools and no additional context are provided.

harness README，钉在 `7a72a514a6ab19c90babb00adc817e4ae86b9c1b`：

> This harness is a uv package, built with the Inspect AI framework.
> uv run inspect eval src/gdp_pdf/task.py -T judge_model=google/gemini-3.5-flash
> The committed task_packs/sample_pdf/ is a synthetic placeholder task.

`src/gdp_pdf/scorer.py` 文件头：

> Per-criterion model-graded scorer. One judge call per criterion.
