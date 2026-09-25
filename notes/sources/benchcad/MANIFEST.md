# MANIFEST

- slug: benchcad
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://github.com/BenchCAD/BenchCAD-main

## 官方仓

- 入口 URL 可打开，未改地址。
- 核实到的官方仓: https://github.com/BenchCAD/BenchCAD-main
- 交叉: https://benchcad.com 与 https://benchcad.github.io/BenchCAD_webpage/ 在 2026-09-24 均返回 200。网站页链到上述 GitHub 与 HF。`CITATION.cff` 的 `repository-code` 也是这个 GitHub URL。
- 默认分支: main
- commit SHA: 52087ef4b08811c21c09b8b16d0ae36c70844865
- 核实: `git ls-remote` HEAD 与 commits API 一致。message 为 “Merge pull request #47 from BenchCAD/feat/openai-responses-max”，committer 日期 2026-07-24T06:06:22Z。仓库 API `pushed_at` 是 2026-08-20T06:03:58Z，默认分支 tip 仍是这个 SHA。
- GitHub API `size`: 856 KB。该 SHA 的递归 git tree 未截断，137 个 blob，合计 1,929,796 字节。
- 代码许可证: 根目录 `LICENSE` 为 MIT（README 徽章 “Code License: MIT”）。数据许可证 README 写 CC BY 4.0。

## 论文 / blog / HF

- 论文: arXiv [2605.10865](https://arxiv.org/abs/2605.10865)，“BenchCAD: A Comprehensive, Industry-Standard Benchmark for Programmatic CAD”。
- 项目页: https://benchcad.com ；论文 HTML 另写 https://benchcad.github.io/BenchCAD_webpage/ 。
- 榜: 仓内 `LEADERBOARD.md`。没有单独的产品 blog URL。
- HF id: `BenchCAD/BenchCAD`。API `sha` `5919f578ab09ec283603a082fab07c7639ab56eb`，`lastModified` 2026-06-28T09:31:03.000Z，卡片许可证 cc-by-4.0，`gated` false。
- 该 HF 修订的 tree 有 29 个文件，合计 962,894,926 字节。最大单文件是 `edit-bench/data/edit_bench-00000-of-00001.parquet`（114.5 MB）。另有 `vlmevalkit/BenchCAD_QA.tsv`（69.5 MB）。

## 测什么

测模型能否看懂并写出可执行的工业零件 CadQuery 程序，以及根据渲染图或代码回答零件上的数值问题。出处: 该 SHA 的 README 开篇（17,900 个执行通过的 CadQuery 程序，106 个零件族，47 个工程标准）和任务表：Vision2Code、CodeEdit、Vision-QA、Code-QA。论文摘要同题，arXiv:2605.10865。

## 环境线索

- 容器: 该 SHA 没有 Dockerfile 或 compose。`.github/workflows/ci.yml` 在 `ubuntu-latest` 上 `uv sync` 后跑 pytest，不是自建镜像。unknown。
- 出网: `prod` 运行从 HF 拉数据（README：第一次 prod 拉到 gitignore 的 `data/`）。调用模型要 API key（`.env.example` 只列供应商 key 名，本次没有抄文件）。CI 里的 pytest 步骤名写 “no API keys, no network”。仓内每个任务有很小的 `test_data/`，可以不下载 HF。
- GPU: `pyproject.toml` 的依赖是 CadQuery、VTK、numpy 等，没有 CUDA 或 torch。CI 也没有 GPU runner。评分路径未见 GPU。
- K8s: 没看到。unknown。
- 多容器: 没看到。unknown。

## 评分

确定性，README 与 `CITATION.cff` 都写没有 LLM judge。Vision2Code 用模型 STEP 与标准 STEP 的 voxel IoU；CodeEdit 用相对基线的 normalized IoU；QA 用对称比例准确率（计数题是精确匹配）。不可执行的程序在 Vision2Code 环境 README 里记 0 分。`environments/benchcad-vision2code/README.md` 写体素网格是归一化 64³。

## agent / runtime

主入口 `benchcad.py` 直接调模型 API（根 `pyproject.toml` 依赖 openai、anthropic、google-genai）。不是多步工具循环。`environments/benchcad-qa` 与 `environments/benchcad-vision2code` 是另外两个 Python 包，依赖 `verifiers>=0.1.6`，README 的用法是 `uv run vf-eval` 和 `vf.load_environment`。QA 环境 README 写它不执行 CAD。没有在仓里看到独立的 coding-agent CLI。

## 体积与是否入 git

- 代码仓 checkout 约 1.93 MB，低于 5 MB，但仍只按本任务要求留下说明，没有把克隆放进 `/workspace`。`uv.lock` 与 `environments/benchcad-qa/uv.lock`（805,717 字节）没有抄过来。
- HF 数据集约 962.9 MB，没有下载。
- 本目录只有 MANIFEST 和短摘录。本次没有 git commit。

## 未抓取项与原因

- HF parquet 与 `vlmevalkit/BenchCAD_QA.tsv`：接近 1 GB。VLMEvalKit 那份 TSV 没有当成第二条官方评测实现打开。
- 论文 PDF 与两个项目页的正文：只确认了 URL 可打开和仓库互链。
- 没有跑 `uv run pytest` 或 CadQuery。

MANIFEST-END
