# AutomationBench

榜上用的 private set 不发布。公开仓是另一套 600 题。GPU 和多容器在清单里都是 unknown。

1. 一句话测什么。测代理能否在销售、市场、运营、支持、财务、人力六类流程里操作 47 个模拟应用，并把环境留在断言要求的终态。出处是该 commit README 的 Overview，以及 https://arxiv.org/abs/2604.18934 摘要。

2. 官方源。仓库 https://github.com/zapier/AutomationBench ，commit `4a8e1061254004d9dac807054eed33fad7d1ff14`（2026-08-04，说明 “Add Opus 5 max public score to readme.”）。论文 https://arxiv.org/abs/2604.18934 。博客 https://zapier.com/blog/introducing-automationbench/ 。榜 https://zapier.com/benchmarks 。没有看到 Hugging Face 数据集。

3. 形态。`task`、`environment`、`verifier`、`agent`、`dataset`。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。公开 600 题按断言打分，不另调模型。没有 Harbor `task.toml`，也没有 Dockerfile。状态在进程内模拟。官方榜的 private set 不在这个 commit。

5. 环境。任务状态在进程内模拟。公开树没有 Dockerfile 或镜像名。跑分要访问模型服务，模拟应用写在本地。GPU、Kubernetes、多容器都是 unknown。`pyproject.toml` 依赖含 `verifiers>=0.2.0`。入口脚本是 `auto-bench`。

6. 评分。不另调模型。`partial_credit` 是断言通过比例。官方通过率是 `task_completed_correctly`，全部断言通过才为 1，并且不算 `simple` 域。公开题 600 道，每域 100。`simple` 另有 200 题，不进榜。榜上分数用未公开的 private set。

7. agent/runtime。有。`auto-bench` 默认模型 `gpt-5-mini`，`--max-steps` 默认 50，`--toolset` 为 `api`、`zapier` 或 `limited_zapier`。README 同时给出 Prime Intellect 入口 `prime env install zapier/AutomationBench`。这次没有安装或运行。

8. 迁入代价。中。公开题和断言脚本都在。没有 task 目录，环境是进程内模拟，容器定义没公开。评测脚本没有写明必须显卡。

9. 对抽象的压力。压力在 `environment`。47 个应用的状态在进程里，公开树没有镜像，也不是多容器。接入要新写 task 目录。`agent` 回路在 `auto-bench`。

10. 本地摘录。[`notes/sources/automationbench/MANIFEST.md`](../../notes/sources/automationbench/MANIFEST.md)。
