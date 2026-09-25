# CursorBench

榜页看得到分数。题目、打分说明和环境镜像都不提供下载。

## 测什么

测代理在真实 Cursor 会话里那些含糊、跨多个文件的任务上表现如何。抓取时页标题是 CursorBench 4.0，页眉写分数越高越好。

## 官方源

榜页 https://cursor.com/cursorbench 。博客 https://cursor.com/blog/cursorbench （Naman Jain，2026-03-11，文内生产版本注记是 3.1）。技术报告 https://cursor.com/blog/composer-2-technical-report 与 https://cursor.com/resources/Composer2.pdf ，第 7.1 节写的是 CursorBench-3。没有公开 Git 仓，没有 commit，没有 arXiv，没有 Hugging Face 数据集。

## 形态

agent、environment、verifier、dataset。4.0 页没有公开 task 目录。没有 `task.toml`、`dataset.toml` 或 adapter。

## 与 Harbor 距离

暂不宜接。任务集不开源，页面不提供下载。4.0 也没有把评分规则重写在榜页上。

## 环境

4.0 公开页没有写 Docker、出网或图形处理器（GPU）。Composer 2 报告第 6.2 节和第 7.1 节写 CursorBench-3 的代码库环境跑在内部平台 Anyrun 上。每个 pod 是一台 Firecracker 虚拟机，可以带浏览器和图形界面。4.0 页没有重述 Anyrun。同一报告写 pod 出网经过内部代理，这是 3 代材料。没有看到 Kubernetes，也没有看到多容器。

## 评分

4.0 榜页公开 Score、Cost/task、Tokens/task、Steps/task，并写小分差未必有统计意义。页上没有写这些分数怎么从单测算出来。2026-03-11 的博客写由另一个代理打分（原文 agentic graders）。维度包括解答是否正确、代码质量、效率和交互行为，正文只展开正确性。这篇博客的生产版本注记是 3.1。Composer 2 报告还为意图、遵从指令、过早编辑、代码质量和打断写了量表。对 CursorBench-3 报的是准确率，外加完成 token、延迟和成本。4.0 是否仍用同一套打分，页面没说。

## agent / runtime

公开页报的是 steps/task，没有公开运行仓库。博客写这是 Cursor 内部评测，任务来自 Cursor 会话。报告第 7.1 节写 CursorBench-3 是在 Anyrun 里直接跑 Cursor 代理，跑法与生产环境相同。4.0 的运行时在榜页上没有另一套说明。https://cursor.com/docs/evals 讲的是用 Cursor SDK 跑用户自己的评测，不是这个数据集。

## 迁入代价

高。没有可下载的题目、打分说明或环境镜像。公开页写这是内部套件。

## 对抽象的压力

压在 dataset 和 verifier。dataset 不公开，接不进 Harbor 的 dataset。3.x 材料里的 verifier 要另跑一套代理来打分。4.0 没给出可复写的规则。3.x 的 environment 还可以带图形界面，4.0 没确认。

## 本地摘录

见 [`notes/sources/cursorbench/MANIFEST.md`](../../notes/sources/cursorbench/MANIFEST.md)。
