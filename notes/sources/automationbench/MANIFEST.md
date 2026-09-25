# MANIFEST

- slug: automationbench
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://github.com/zapier/AutomationBench

## 官方仓

- 核实到的官方仓: https://github.com/zapier/AutomationBench
- 默认分支: main
- commit SHA: 4a8e1061254004d9dac807054eed33fad7d1ff14
- commit 说明: Add Opus 5 max public score to readme.
- committer 日期: 2026-08-04T21:42:13Z
- 仓库 pushed_at: 2026-08-04T21:42:22Z
- GitHub API `size`: 6048 KB
- API `license.spdx_id`: NOASSERTION。同 SHA 的 `LICENSE` 正文是 MIT License，Copyright (c) 2026 Zapier, Inc.
- 首页: https://zapier.com/benchmarks
- 根目录有 `README.md`、`pyproject.toml`、`automationbench/`、`tests/`、`visualizer/`。树里没有 Dockerfile、compose、k8s 路径

## 论文 / blog / HF

- 论文: https://arxiv.org/abs/2604.18934 （页面日期 April 2026）
- blog: https://zapier.com/blog/introducing-automationbench/
- 榜: https://zapier.com/benchmarks
- Artificial Analysis: https://artificialanalysis.ai/evaluations/automationbench-aa （只在 README 被点名，本次没有打开）
- HF id: 没有看到

## 测什么

测 AI 代理能否在销售、市场、运营、支持、财务、人力六类业务流程里，操作 47 个模拟 SaaS，并把环境留在断言所要求的终态。出处：该 commit README 的 Overview，以及 arXiv:2604.18934 摘要（跨应用 REST 工作流、终态程序化评分）。

## 环境线索

- 容器: 公开树没有 Dockerfile 或镜像名。任务状态在进程内模拟。unknown。
- 出网: 跑分要访问模型 API。README 使用 `OPENAI_API_KEY` / `ANTHROPIC_API_KEY` 和 `--base-url`。模拟应用本身写在本地。没有沙箱出网开关。
- GPU: README、`pyproject.toml` 和根目录树都没写 GPU。unknown。
- K8s: 没看到。unknown。
- 多容器: 没看到。unknown。
- `pyproject.toml` 依赖含 `verifiers>=0.2.0`、`anthropic`、`httpx`。入口脚本是 `auto-bench` → `automationbench.scripts.eval:main`

## 评分

确定性程序断言，不另要 judge 模型。README Scoring：`partial_credit` 是断言通过比例；官方通过率是 `task_completed_correctly`，全部断言通过才为 1，且不算 `simple` 域。blog 写 “Scoring is deterministic… There's no LLM-as-judge”。论文摘要写 grading is programmatic and end-state only。榜上分数用未公开的 private set；本仓是 public 600 题（每域 100）。`simple` 另有 200 题，不进榜。

## agent / runtime

有。本仓自带 `auto-bench`：默认模型 `gpt-5-mini`，`--max-steps` 默认 50，`--toolset` 为 `api`、`zapier` 或 `limited_zapier`。README 同时给出 Prime Intellect 入口 `prime env install zapier/AutomationBench`。本次没有安装或运行。

## 体积与是否入 git

GitHub API size 6048 KB，大于 5MB，没有把克隆留在 `/workspace`。本目录只有本文件和 `excerpt-readme-scoring.md`。两份都是小文本，可以进 git。本次没有 git commit。

## 未抓取项与原因

- 整仓克隆：大于 5MB。
- private 评测集：README 写明不发布。
- Prime Intellect 环境页和 Artificial Analysis 页：没有打开。
- 论文摘要写当时最强模型低于 10%；本 commit README 的 public 表约在 26%–50%。两处数字都只作出处记录，没有对过题目版本。
- 没有运行 `auto-bench`。

MANIFEST-END
