# BrowseComp

参考实现下载公开表格，再做单轮提问。论文里的网上浏览不在这个脚本里。

1. 一句话测什么。测浏览智能体能否在网上持续找出难检索、彼此纠缠的短事实。共 1,266 题，答案短，可与参考答案对照。出处是 arXiv 2504.12516 摘要。

2. 官方源。代码 https://github.com/openai/simple-evals ，`main` 的 commit `652c89d0ca9df547706735883097e9537d40dc47`（2026-04-22）。入口 https://openai.com/index/browsecomp 。论文 https://arxiv.org/abs/2504.12516 。题目不在 Hugging Face，在公开表格 `browse_comp_test_set.csv`。

3. 形态。`dataset`、`verifier`。该 commit 的文件树没有 `environment` 定义，也没有 `agent` 循环。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。评分要另调 judge 模型。清单没有给出 `task.toml` 或 `dataset.toml`。

5. 环境。该 commit 没有 Dockerfile、compose 或 Kubernetes 清单。脚本会下载上述表格，并调用被测模型与 grader 的接口。GPU 未见。多容器未见。

6. 评分。`browsecomp_eval.py` 用 grader 模板，让模型回答 `correct: yes` 或 `no`。`simple_evals.py` 的 `browsecomp` 分支把 `grading_sampler` 写死为 `gpt-4.1-2025-04-14`（`ChatCompletionSampler`，`max_tokens=2048`）。

7. agent/runtime。`BrowseCompEval.__call__` 把解密后的题目填进单轮 `QUERY_TEMPLATE`，交给 `SamplerBase`。仓库里的 sampler 是各家模型接口。被测模型若自己浏览，运行时不在本仓，记 unknown。

8. 迁入代价。高。仓内只有单轮提问和 grader。浏览回路要自备，才能覆盖论文里的浏览任务。

9. 对抽象的压力。`verifier` 的 reward 来自另一个模型的 yes/no。`agent` 的浏览回路没有落在这个仓库里。`dataset` 是加密表格，单元格明文未随材料落盘。

10. 本地摘录。[`notes/sources/browsecomp/MANIFEST.md`](../../notes/sources/browsecomp/MANIFEST.md)。
