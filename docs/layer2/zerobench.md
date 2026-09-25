# ZeroBench

这个 commit 的文件只有 README、LICENSE 和一张分数图。题目和图片在 Hugging Face，`gated` 为 `auto`。仓内 pass@1 片段是字符串比较。项目页写 2026-08 改正过一小部分判分，改正后的程序不在这个 commit。

1. 一句话测什么。测大型多模态模型答 100 道人工编写的高难度视觉推理题，并附 334 道对应子问题。出处是该 commit 的 README：“a main set of 100 high-quality, manually curated questions”，子问题示例 `num_rows: 334`。论文 https://arxiv.org/abs/2502.09696 。项目页 https://zerobench.github.io/ 。

2. 官方源。代码 https://github.com/jonathan-roberts1/zerobench ，`main` HEAD `0debbe43deddfe54f9965a6fdfd4f70a20d8ab62`（2026-08-11，说明 “Added metric definitions and ICML tag”），MIT。论文 https://arxiv.org/abs/2502.09696 。ICML 2026 poster https://icml.cc/virtual/2026/poster/65303 。数据集 https://huggingface.co/datasets/jonathan-roberts1/zerobench ，sha `8fcdfd9138c802cac52b774b36946e70f738f500`，`gated` 为 `auto`。tree 合计约 638 MB：`images.zip` 约 446.64 MB，main 与 subquestions 两个 parquet 各约 95 MB。README 写 v3 在 HF `main`，v2 在分支 `v2`。未登录不能下 parquet，100 与 334 没有在本地数行。

3. 形态。`dataset`、`verifier`。官方片段把推理函数留空，没有 `agent` runtime，也没有 `environment` 容器。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。暂不宜接。题目与图片 gated。清单没有给出 `task.toml` 或 `dataset.toml`。

5. 环境。该 commit 没有 Dockerfile 或 compose。题目在 HF，下载要出网并接受条款。仓内片段没有写死模型端点。GPU、Kubernetes、多容器在官方片段里都没写，记 unknown。项目页外部结果表里，有些 “w/ tools” 行的 Notes 写 Containerized coding+GUI tools 或 Claude Code harness。那是外部报告的跑法，不是这个仓附带的环境。

6. 评分。复现仓内片段不需要 judge。README 要求模型把最终答案放在花括号里，取最后一对花括号，与 `question_answer` 做去首尾空白、忽略大小写的等长比较。指标：pass@1 为单次采样平均分（发布期模型用一次 greedy）；pass@5 为 5 次里至少对一次的题比例；pass^5 为 5 次全对的题比例。项目页写 2026-08 用 Fable 5 做评测协议检查后，0.71% 的 grading 被改正，题目本身不变。该 commit 没有给出改正后的判分程序。外部榜若干行的 Notes 写 “graded by an LLM judge”。README 把官方榜最高写为 GPT-5.6 Sol (max) 的 pass@5 30.0。同日项目页官方表第一行是 GPT-6 Astra (max)，pass@5 52.0，并仍列 GPT-5.6 Sol (max) 为 30.0。两处数字以各自页面为准。

7. agent/runtime。官方片段是 `for` 循环加一行留空的 `YOUR_MODEL_INFERENCE_FUNCTION(prompt, images)`，没有 runtime。被测对象在官方代码里是 unknown。外部表里的工具环境不是本仓的实现。

8. 迁入代价。高。题面和图片要先过 HF 门禁，合计约 638 MB。仓内没有可运行的评测包。项目页后期改正的判分步骤不在 git 里。

9. 对抽象的压力。`dataset` 接不上可再分发的任务目录，图片 gated。`verifier` 在这个 commit 里是花括号字符串比较；项目页写过判分改正，程序不在仓内。官方代码没有 `agent` 回路，也没有容器可接成 `environment`。

10. 本地摘录。[`notes/sources/zerobench/MANIFEST.md`](../../notes/sources/zerobench/MANIFEST.md)。
