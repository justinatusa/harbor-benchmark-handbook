# MANIFEST

- slug: `zerobench`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://zerobench.github.io/

## 官方仓

- 核实到的官方仓: https://github.com/jonathan-roberts1/zerobench
- 入口页与 README 都把该仓标为 Code。GitHub 仓库描述为 “[ICML '26] Code, Data and Red Teaming for ZeroBench”。
- 默认分支: `main`
- commit SHA: `0debbe43deddfe54f9965a6fdfd4f70a20d8ab62`
- 核实方式: `git ls-remote` 的 HEAD 与 GitHub commits API 均为该 SHA。提交说明为 “Added metric definitions and ICML tag”，committer 时间 2026-08-11T10:31:36Z。许可证 MIT。
- 该 commit 的文件只有 `README.md`、`LICENSE`、`assets/zerobench_scores_over_time.png`。没有独立评测包。

## 论文 / blog / HF

- 论文: arXiv:2502.09696，标题 “ZeroBench: An Impossible Visual Benchmark for Contemporary Large Multimodal Models”（arXiv abs 页 citation_title，citation_date 2025/02/13）。abs URL 抓取日返回 200。README 链 PDF https://arxiv.org/pdf/2502.09696 。
- 项目页即入口: https://zerobench.github.io/ （抓取日取回正文）。ICML 2026 poster: https://icml.cc/virtual/2026/poster/65303 （抓取日 HEAD 200）。
- 数据集: https://huggingface.co/datasets/jonathan-roberts1/zerobench 。HF dataset API 的 `sha` 为 `8fcdfd9138c802cac52b774b36946e70f738f500`，`gated` 为 `auto`，tag 含 `arxiv:2502.09696`。tree 合计 637,688,498 字节（约 638 MB）: `images.zip` 446.64 MB，`data/zerobench-00000-of-00001.parquet` 95.39 MB，`data/zerobench_subquestions-00000-of-00001.parquet` 95.65 MB。README 写 main 100 行、subquestions 334 行；v3 在 HF `main`，v2 在分支 `v2`。未登录、未点 gated 条款，所以没有下到 parquet 去数行。

## 一句话测什么

测大型多模态模型答 100 道人工编写的高难度视觉推理题，并附 334 道对应子问题。出处：该 commit 的 `README.md`：“ZeroBench is a challenging visual reasoning benchmark for Large Multimodal Models (LMMs). It consists of a main set of 100 high-quality, manually curated questions …”。项目页标题同论文名。

## 环境线索

- 容器: 官方仓 unknown。该 commit 没有 Dockerfile 或 compose。项目页的外部结果表里，有些 “w/ tools” 行的 Notes 写 Containerized coding+GUI tools 或 Claude Code harness。那是外部报告的跑法，不是这个仓附带的环境。
- 出网: 题目与图片在 HF（且 gated auto），下载要出网并接受条款。仓内代码片段把推理函数留空，若模型是 API 则还要出网；仓本身未写死端点。
- GPU: unknown。片段没有设备字段。
- K8s: unknown。未见清单。
- 多容器: unknown。官方片段是单进程循环。外部笔记里的容器化工具环境没有在本仓给出 compose。

## 评分

仓内公开的 pass@1 是确定性字符串规则，不调用 judge 模型。`README.md` 的片段要求模型把最终答案放在花括号里，取最后一对花括号，与 `question_answer` 做去首尾空白、忽略大小写的等长比较。指标定义（同一 README）: pass@1 为单次采样平均分（发布期模型用一次 greedy）；pass@5 为 5 次里至少对一次的题比例；pass^5 为 5 次全对的题比例。发布期采样参数写在项目页：temperature=0.7、top_p=0.95；较新的官方评测改用模型默认参数，thinking 模型的 pass@1 由这 5 次的均值算出，而不是一次 greedy。

项目页同时写：2026-08 用 Fable 5 做 evaluation protocol red team 后，0.71% 的 grading 被改正，pass@5 平均上升 0.79 个百分点，题目本身不变。该 commit 没有给出这套改正后的判分程序，只有上面的字符串比较。外部榜若干行的 Notes 写 “graded by an LLM judge”。因此：复现仓内片段不需要 judge 模型；官方榜后期改正过程和部分外部上报用了别的判分，细节不在这个 commit 里。

README（2026-08-11 这一 commit）把官方榜最高写为 GPT-5.6 Sol (max) 的 pass@5 30.0、pass^5 13.0。同日抓到的项目页官方表第一行是 GPT-6 Astra (max)，pass@5 52.0、pass^5 35.0，并仍列 GPT-5.6 Sol (max) 为 pass@5 30.0、pass^5 13.0。页首统计写 76% 的题至少被解出一次、72 个官方评测模型。仓内 README 则写 70% 与 “best model now reaches 30.0% pass@5”。两处数字不一致，以各自页面为准，未再找更新的 git commit（`ls-remote` HEAD 就是这个 SHA）。

## agent / runtime 线索

官方片段是 `for` 循环加一行 `YOUR_MODEL_INFERENCE_FUNCTION(prompt, images)`，没有 runtime。项目页外部表有带工具的上报（容器里的 coding+GUI、Python tools、最多 30 step 等）。那些不是本仓的实现。被测对象在官方代码里是 unknown。

README 含一条 BIG-bench 风格 canary，要求不要把数据放进训练语料。本摘录不复制该字符串。

## 体积与是否入 git

- GitHub API `size`: 487 KB。浅克隆在 `/tmp` 约 1.2 MB：`.git` 约 640 KB，`assets/` 约 520 KB。
- 题目、答案和图片在 HF，约 638 MB，不在该 git commit。
- 本目录不放入克隆或数据集。只留本文件与 `excerpt.md`。本线程不 git commit。浅克隆小于 5 MB，仍不复制进 `/workspace`。

## 未抓取项与原因

- 未下载 HF parquet 与 `images.zip`：gated auto，且合计约 638 MB。因此 100/334 行只来自 README 与项目页，没有本地数行。
- 未接受 HF gated 条款，未登录。
- 2026-08 判分改正的操作步骤不在 git 里，项目页只给了改正比例。
- 项目页榜比 README 多出的模型与更高分数，没有对应的更新 commit。
- 外部工具环境只在榜的 Notes 里出现，没有可克隆的官方 harness。
- 未跑通任何模型推理。

MANIFEST-END
