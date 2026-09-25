# gdp-pdf

- slug: `gdp-pdf`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://surgehq.ai/benchmarks/gdp-pdf

## 官方仓

有。评测 harness https://github.com/surge-ai/gdp-pdf ，默认分支 `main`，抓取时只有一次提交，HEAD `7a72a514a6ab19c90babb00adc817e4ae86b9c1b`（2026-08-14T18:51:22Z，`Initial commit`）。GitHub license 字段为空。论文脚注 1 把这个 URL 写成 evaluation harness。仓里没有 100 份正式 PDF，只有 `task_packs/sample_pdf/` 两个合成占位 PDF。

## 论文 / blog / HF

- 论文: arXiv:2607.11192（https://arxiv.org/abs/2607.11192）。抓取的是 arXiv HTML。页眉写 Accepted at KnowledgeMR, CVPR 2026。
- 榜页: https://surgehq.ai/benchmarks/gdp-pdf
- HF: `surgeai/GDP.pdf`（id 里有点号）。数据集仓 sha `8d1efb32cb57baec2265bb84da03b30654761373`。`gated: false`。card license `mit`。datasets-server：`default/test` 100 行。
- 另有第三方复现页，不是官方仓：https://artificialanalysis.ai/evaluations/gdp-pdf 。搜索摘要写 AA 用 LiteParse 文本加页面图，judge 是 GPT-5.6 Luna Medium，并写明 harness、送文档方式和 judge 与 Surge 不同，分数不能直接互换。本次未保存该页 HTML。

## 一句话测什么

测多模态模型能不能对着从业者留下的原始 PDF 回答职业问题，并且答案落在该落的证据上：100 道题、十个领域，候选题至少要让两个前沿模型在实质内容上失败才留下。（arXiv:2607.11192 摘要；数据集句在论文第 1 节，URL 为 https://huggingface.co/datasets/surgeai/GDP.pdf）

## 环境线索

- 容器: harness 的 README 与文件树未见 Dockerfile。官方跑法是本机 `uv run inspect eval`。题目环境不是容器。
- 出网: 跑官方评测要出网，因为要调被测模型 API 和 judge API，并从 HF 取 PDF。论文第 5.1 节写单题输入只有问题和 PDF，`No tools and no additional context`，所以题目本身不再去访问互联网。
- GPU: 论文写 frontier models 走 public APIs。未见本地 GPU 要求。记 unknown。
- K8s: 未见。unknown。
- 多容器: 未见。unknown。

## 评分

要另外的 judge 模型。论文第 4 节：每条原子标准单独交给 Gemini 3.5 Flash，二元过/不过；judge 看不到源 PDF，也看不到 gold answer。严格通过率要求该题每条标准都过；另外报 rubric 均分。harness README 的榜配置是 `-T judge_model=google/gemini-3.5-flash`，五次 epoch，指标名 `all_pass/mean` 与 `mean_criteria/mean`。`scorer.py` 文件头写每条 criterion 一次 judge 调用。不是确定性字符串匹配。

AA 页用的是另一个 judge（搜索摘要写 GPT-5.6 Luna Medium）。那是复现，不是 Surge harness 的默认 judge。

## agent / runtime

官方 harness 是 Inspect AI 的单轮任务，论文写不给工具。没有多步 agent 循环，也没有单独的 agent runtime。被测对象是直接吃 PDF 的模型 API。

## 体积与是否入 git

- 代码仓: GitHub `size` 字段 254（KB）。`git/trees` 递归 blob 合计 719,410 bytes，16 个文件；其中 `uv.lock` 689,965 bytes。小于 5MB，但本次未克隆，只拉了 README 与 `src/gdp_pdf/scorer.py` 到临时目录做摘录。
- HF 文件树合计 467,834,031 bytes（约 446.16 MiB），103 个文件，大头是 `pdfs/`。datasets-server 的 size 只统计进数据集配置的 parquet：100 行、原始字节 376,960，不含 `pdfs/`。两边都记，避免把 377KB 当成全库。
- 入 git: 本目录只留本文件和 `excerpt.md`。PDF 与整仓不放进工作区。

## 未抓取项与原因

- 100 份职业 PDF：合计约 446 MiB，超过留存上限。
- AA 榜页正文：只用了搜索摘要确认它是另一套 harness / judge，未存 HTML。
- 论文 HTML 已读部分没有写出 “4,592 页 / 1,275 条标准” 这两个总数；这两个数字出现在 AA 文章摘要里，本文件不把它们写成论文数字。
- 未安装 Inspect，未跑 eval。

MANIFEST-END
