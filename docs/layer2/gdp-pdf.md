# GDP.pdf

正式 100 份职业 PDF 在 Hugging Face。harness 仓里只有 `task_packs/sample_pdf/` 两份合成占位 PDF。评分要另调模型，judge 看不到源 PDF，也看不到 gold answer。

1. 一句话测什么。测多模态模型能不能对着从业者留下的原始 PDF 回答职业问题，并且答案落在该落的证据上。100 道题、十个领域。出处是 arXiv 2607.11192 摘要。摘要写候选题至少要让两个前沿模型在实质内容上失败才留下。页眉写 Accepted at KnowledgeMR, CVPR 2026。

2. 官方源。harness https://github.com/surge-ai/gdp-pdf ，`main` 只有一次提交，HEAD `7a72a514a6ab19c90babb00adc817e4ae86b9c1b`（2026-08-14，说明 “Initial commit”）。GitHub license 字段为空。论文 https://arxiv.org/abs/2607.11192 ，脚注 1 把这个 URL 写成 evaluation harness。榜页 https://surgehq.ai/benchmarks/gdp-pdf 。数据集 `surgeai/GDP.pdf`（id 里有点号），https://huggingface.co/datasets/surgeai/GDP.pdf ，sha `8d1efb32cb57baec2265bb84da03b30654761373`，`gated` false，卡片许可 mit。datasets-server 的 `default/test` 是 100 行。第三方复现页 https://artificialanalysis.ai/evaluations/gdp-pdf 不是官方仓；搜索摘要写它的 harness、送文档方式和 judge 与 Surge 不同，分数不能直接互换。

3. 形态。`dataset`、`verifier`。官方 harness 是 Inspect AI 单轮任务，不给工具，没有多步 `agent`。文件树未见 `environment` 容器。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。每条原子标准要另调 judge。清单没有给出 `task.toml` 或 `dataset.toml`。

5. 环境。README 与文件树未见 Dockerfile。官方跑法是本机 `uv run inspect eval`。跑评测要出网，因为要调被测模型 API 和 judge API，并从 HF 取 PDF。论文第 5.1 节写单题输入只有问题和 PDF，`No tools and no additional context`，题目本身不再去访问互联网。论文写 frontier models 走 public APIs。本地 GPU、Kubernetes、多容器都没写成评测条件，记 unknown。HF 文件树合计约 446 MiB，大头是 `pdfs/`。

6. 评分。要另调模型。论文第 4 节：每条原子标准单独交给 Gemini 3.5 Flash，二元过或不过。严格通过率要求该题每条标准都过；另外报 rubric 均分。harness README 的榜配置是 `-T judge_model=google/gemini-3.5-flash`，五次 epoch，指标名 `all_pass/mean` 与 `mean_criteria/mean`。`src/gdp_pdf/scorer.py` 文件头写每条 criterion 一次 judge 调用。不是确定性字符串匹配。

7. agent/runtime。没有多步 agent 循环，也没有单独的 agent runtime。被测对象是直接吃 PDF 的模型 API。Inspect 任务入口是 `src/gdp_pdf/task.py`。

8. 迁入代价。高。打分脚本和占位 PDF 在公开仓。正式 100 份 PDF 约 446 MiB，不在 git 里。评分要 Gemini 3.5 Flash。没有任务目录。

9. 对抽象的压力。`verifier` 的每条标准是一次模型二元判定，judge 看不到 PDF。`dataset` 的正式 PDF 在 HF，仓内样本是合成占位。现有入口是单轮 Inspect 任务，没有代理循环可以接到 `agent`，也没有镜像可接成 `environment`。

10. 本地摘录。[`notes/sources/gdp-pdf/MANIFEST.md`](../../notes/sources/gdp-pdf/MANIFEST.md)。
