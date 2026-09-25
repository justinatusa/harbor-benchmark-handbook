# BenchCAD

评分是体素 IoU 和精确匹配。README 与 `CITATION.cff` 都写没有 LLM judge。这个 commit 没有 Dockerfile。主入口直接调模型 API，不是多步工具循环。

1. 一句话测什么。测模型能否看懂并写出可执行的工业零件 CadQuery 程序，以及根据渲染图或代码回答零件上的数值问题。出处是 commit `52087ef4b08811c21c09b8b16d0ae36c70844865` 的 README 开篇：17,900 个执行通过的 CadQuery 程序，106 个零件族，47 个工程标准。任务表是 Vision2Code、CodeEdit、Vision-QA、Code-QA。论文摘要同题，https://arxiv.org/abs/2605.10865 。

2. 官方源。仓库 https://github.com/BenchCAD/BenchCAD-main ，`main` HEAD `52087ef4b08811c21c09b8b16d0ae36c70844865`（2026-07-24，说明 “Merge pull request #47 from BenchCAD/feat/openai-responses-max”）。代码许可 MIT，数据许可 README 写 CC BY 4.0。论文 https://arxiv.org/abs/2605.10865 。项目页 https://benchcad.com 与 https://benchcad.github.io/BenchCAD_webpage/ 。榜在仓内 `LEADERBOARD.md`。数据集 https://huggingface.co/datasets/BenchCAD/BenchCAD ，sha `5919f578ab09ec283603a082fab07c7639ab56eb`（2026-06-28，`gated` false，cc-by-4.0）。该修订 tree 合计约 962.9 MB。`CITATION.cff` 的 `repository-code` 就是这个 GitHub URL。

3. 形态。`dataset`、`verifier`。主入口 `benchcad.py` 直接调模型 API。`environments/benchcad-qa` 与 `environments/benchcad-vision2code` 是另外两个 Python 包，用法是 `uv run vf-eval`。没有自建 `environment` 镜像，也没有独立 coding-agent CLI。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。公开仓没有 Harbor `task.toml`。评分是程序计算的 IoU，接入要新写 task 目录，并准备 CadQuery 运行环境。清单没有给出 `dataset.toml`。

5. 环境。该 SHA 没有 Dockerfile 或 compose。`.github/workflows/ci.yml` 在 `ubuntu-latest` 上 `uv sync` 后跑 pytest，不是自建镜像。`prod` 运行从 HF 拉数据，第一次拉到 gitignore 的 `data/`。调用模型要 API key。CI 里的 pytest 步骤名写 “no API keys, no network”。仓内每个任务有很小的 `test_data/`，可以不下载 HF。`pyproject.toml` 的依赖是 CadQuery、VTK、numpy 等，没有 CUDA 或 torch。CI 也没有 GPU runner。Kubernetes、多容器没看到，记 unknown。

6. 评分。确定性，没有 LLM judge。Vision2Code 用模型 STEP 与标准 STEP 的 voxel IoU；CodeEdit 用相对基线的 normalized IoU；QA 用对称比例准确率（计数题是精确匹配）。`environments/benchcad-vision2code/README.md` 写体素网格是归一化 64³，不可执行的程序记 0 分。QA 环境 README 写它不执行 CAD。

7. agent/runtime。根 `pyproject.toml` 依赖 openai、anthropic、google-genai。不是多步工具循环。两个环境包依赖 `verifiers>=0.1.6`，入口是 `vf.load_environment`。没有在仓里看到独立的 coding-agent CLI。

8. 迁入代价。高。评分不另调模型，但没有 Harbor task 目录。正式数据约 963 MB 在 HF。要准备能跑 CadQuery 的环境，这个 commit 没有给出镜像。

9. 对抽象的压力。`verifier` 是 64³ 体素 IoU 和精确匹配，不经过模型。`dataset` 的大 parquet 在 HF，仓内 `test_data/` 只是小样本。`environment` 没有 Dockerfile，CI 跑在 `ubuntu-latest`。现有入口是一次 API 调用，没有代理循环可以接到 `agent`。

10. 本地摘录。[`notes/sources/benchcad/MANIFEST.md`](../../notes/sources/benchcad/MANIFEST.md)。
