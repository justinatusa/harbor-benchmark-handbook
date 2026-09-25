# GDPval-AA v2.1

金标在 Hugging Face。跑分脚本、评判提示词全文和 E2B 镜像构建文件没有公开仓库。方法页写明评分要另调模型。

1. 一句话测什么。测模型能否在隔离沙箱里做出真实职业任务的交付文件，再用盲评两两比较合成 Elo。评测页写 220 题、44 个职业、9 个行业。出处是 https://artificialanalysis.ai/evaluations/gdpval-aa 页首。

2. 官方源。评测页 https://artificialanalysis.ai/evaluations/gdpval-aa 。方法 https://artificialanalysis.ai/methodology/intelligence-benchmarking 的 “GDPval-AA v2.1” 一节。数据集论文 https://arxiv.org/abs/2510.04374 。金标 https://huggingface.co/datasets/openai/gdpval ，git 修订 `11e7900cdcac61bc4daf59e65feb238acda98fbf`。没有公开的任务 git 仓。https://github.com/openai/gdpval 返回 404。方法页点名的框架 https://github.com/ArtificialAnalysis/Stirrup ，commit `247f24d56b2108235880ed2a2baea5d35b5a67ee`（2026-08-04，说明 “chore: add 7 day exclusion rule (#81)”）。对该 commit 检索 `gdpval` 为 0 处。

3. 形态。`task`、`environment`、`verifier`、`agent`、`dataset`。公开材料没有 Harbor adapter。Stirrup 不含本榜的任务循环。

4. 与 Harbor 距离。重改造。清单没有给出 `task.toml` 或 `dataset.toml`。金标数据集公开。方法页写两阶段里的第二阶段要另调模型做盲评。

5. 环境。每题新建一个 E2B sandbox。提示词写隔离的 Linux 沙箱，用户 `user`，家目录 `/home/user`。镜像是 Debian trixie，并预装 LibreOffice、Pandoc 等。没看到多容器。Kubernetes：unknown。GPU：unknown。`code_exec` 能否直接出网：unknown。代理有 Web Fetch 和 Web Search。最多 250 轮。单条命令 10 分钟。

6. 评分。要另调模型。三模型面板里抽一个做盲评，比较同一题的两份提交。面板是 GPT-5.6 Sol（medium reasoning）、Gemini 3.8 Flash（high reasoning）、Claude Opus 5（high effort）。含音频或视频的题改由 Gemini 3.8 Flash 单独看。汇总是 Crowd-BT 拟合的 Elo，把 DeepSeek V4.1 Flash (max) 钉在 1600。Elo 计算是程序，胜负来自评判模型。评判提示词全文没有公开仓库。

7. agent/runtime。方法页写所有模型用 Stirrup，在 E2B 里调用工具。本榜的任务运行时源码没有公开。评判是另一套三个模型。

8. 迁入代价。高。要按方法页重做盲评。跑分脚本、评判提示词全文和 E2B 镜像构建文件都没有仓库可搬。Stirrup 仓没有这套题。

9. 对抽象的压力。压力在 `verifier`。胜负来自模型盲评，程序再把胜负拟合成分数。`environment` 的镜像构建文件没有公开。`agent` 指定了 Stirrup，该仓没有 gdpval 任务循环。

10. 本地摘录。[`notes/sources/gdpval-aa-v2-1/MANIFEST.md`](../../notes/sources/gdpval-aa-v2-1/MANIFEST.md)。
