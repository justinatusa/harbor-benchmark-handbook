# MANIFEST

- slug: `cursorbench`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://cursor.com/cursorbench
- 官方仓: 没有
- commit: 没有
- 论文: 没有 arXiv id
- blog: https://cursor.com/blog/cursorbench （Naman Jain，2026-03-11；文内注记当时的生产版本是 CursorBench 3.1）
- 技术报告: https://cursor.com/blog/composer-2-technical-report 与 https://cursor.com/resources/Composer2.pdf ，其中第 7.1 节写的是 CursorBench-3
- HF: 没有
- 置信度: medium。公开页在，数据集不开源。下面凡是只在 3.x 材料里出现、4.0 页没有重述的句子，都标了版本。

GitHub 搜索 `cursorbench in:name` 与 `cursorbench org:cursor` 没有 Cursor 组织的数据集仓。搜到的是第三方曲线选择器或分数摘录，不当成官方任务集。

## 测什么

测 agent 在来自真实 Cursor 会话的含糊、多文件任务上的表现，页眉写分数越高越好。出处：https://cursor.com/cursorbench “We evaluate agents on ambiguous, multi-file tasks from real Cursor sessions.” 抓取时页标题是 CursorBench 4.0。同页 changelog 写 4.0 增加了长程题，方向是 edit、refactor、investigation、intent understanding、managing jobs、design adherence（日期行 Sep 10, 2026）。3.0 起先是 edit、refactor、bugfix；3.1 加上 codebase understanding、bugfinding、planning、code review；3.2 加上 instruction following 和 advanced tool use。

2026-03-11 blog 写任务来自 Cursor 工程团队的真实会话，用 Cursor Blame 把提交对回 agent 请求，许多题在内部代码库，题面故意短，并用 agentic graders 打分。这篇 blog 的生产版本注记是 3.1，不是 4.0。

## 环境

- 容器: 4.0 公开页没有写 Docker 或容器。Composer 2 技术报告第 6.2 / 7.1 节写 CursorBench 的 codebase environment 跑在内部平台 Anyrun 上，每个 pod 是一台 Firecracker VM，可以带浏览器和 GUI。该节的表 1 标明是 CursorBench-3。4.0 页没有重述 Anyrun。
- 出网: 4.0 页没有写。同一报告第 6.2 节写 Anyrun pod 的出网要经过内部代理 Anygress，按请求策略过滤。这是训练/环境平台的描述，报告把它和 CursorBench-3 的 agent 运行连在一起；4.0 是否仍同一策略，页上没写。
- GPU: 4.0 页没有写任务要 GPU。报告第 6 节的 GPU 句子是 Composer 2 训练和推理集群，不是 4.0 任务规格。
- K8s: 没看到 Kubernetes。报告写 Anyrun manager 调度 pod，pod 的实现是 Firecracker VM。
- 多容器: 没看到。

## 评分

要另外的 grader，而且 4.0 没有把规则重写在榜页上。2026-03-11 blog：“we use agentic graders to reliably score them.” 同文写评测维度包括 solution correctness、code quality、efficiency、interaction behavior，这篇只展开正确性。Composer 2 报告第 5 节写他们还为 intent、instruction-following、eager editing、code quality、interruption 写了 rubrics；第 7.1 节对 CursorBench-3 报的是 accuracy，外加 completion tokens、延迟和成本。4.0 页公开的是 Score、Cost/task、Tokens/task、Steps/task，并写小分差未必有统计意义。页上没有写这些分数是单测算出来的。按 3.x 材料，正确性评分用 agentic grader，不是纯确定性测试。4.0 是否仍用同一 grader：未知，页面没说。

## agent / runtime

公开页报的是 agent 的 steps/task，没有写 harness 仓库。2026-03-11 blog 写这是 Cursor 内部评测，任务来自 Cursor 会话。Composer 2 报告第 7.1 节：“We evaluate our models by running Cursor agents directly within Anyrun … and we run the agent exactly as it would execute in our production environment.” 对象是 CursorBench-3。4.0 的 runtime 在榜页上没有另一套说明。https://cursor.com/docs/evals 讲的是用 Cursor SDK 跑用户自己的评测，不是 CursorBench 数据集。

## 体积与是否入 git

没有公开数据集可克隆。本目录只留本文件和 `excerpts.md`，可以进 git。Composer 2 PDF 留在抓取缓存里，没有复制进本目录。

## 未抓取

- 任务、grader prompt、环境镜像。官方材料写这是内部套件，页面不提供下载。
- 4.0 与 3.x 的逐题差异。changelog 只有类别句子。
- 榜上 52 行模型分数。页面抓得到，但它们是滚动结果，不是任务源，本目录不复制整张表。
- 第三方 GitHub 上的 CursorBench 同名仓。没有证据表明它们是官方数据集。

MANIFEST-END
