# MANIFEST

- slug: `omnidocbench`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://github.com/opendatalab/OmniDocBench

## 官方仓

- 核实到的官方仓: https://github.com/opendatalab/OmniDocBench
- 默认分支: `main`
- commit SHA: `f133a71e9e91c3621c7ce8994200a7b394a06eb3`
- 核实方式: `git ls-remote` 的 HEAD 与 GitHub commits API 均为该 SHA。提交说明为 “Merge pull request #257 from dt-yy/main”，committer 时间 2026-09-11T10:01:16Z。仓库描述为 “[CVPR 2025] A Comprehensive Benchmark for Document Parsing and Evaluation”。许可证 Apache-2.0。
- 同远程上还看到分支 `v1_0`（`337cc26965893db3ef53ddc119a6d6bb5bde096f`）、`v1_5`（`59b103c4b47d3a01fada83491585d6512a40c0bc`）、`feature/multipage-table-chart-eval`（`147cd5ac9472002f5751221d390bf00abdbc0d2f`）。没有名为 `v1_6` 或 `v1_7` 的分支。

## 论文 / blog / HF

- 论文: arXiv:2412.07626，标题 “OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations”（arXiv abs 页 citation_title，citation_date 2024/12/10）。abs URL 抓取日返回 200。README 另称 CVPR 2025（2025/03/10 更新条）。
- 数据集: https://huggingface.co/datasets/opendatalab/OmniDocBench 。HF dataset API 的 `sha` 为 `aa1ee96d106dbe53d0ae59474d75c6e6d9b53fec`，tag 含 `arxiv:2412.07626`。分页 tree API 合计 1662 个文件、1,550,688,430 字节（约 1.55 GB），其中 `OmniDocBench.json` 为 42.21 MB。
- 其他入口（README 链接，抓取日 HEAD 200）: https://opendatalab.com/omnidocbench ；OpenDataLab 数据集页 https://opendatalab.com/OpenDataLab/OmniDocBench （只按 README 记录，未再展开）。
- 社区评测封装（README 2026/07/27 更新条，未克隆）: https://github.com/modelscope/evalscope 与 https://evalscope.readthedocs.io/en/latest/benchmarks/omni_doc_bench.html

## 一句话测什么

测真实版式 PDF 页的文档解析：把模型输出的页面 Markdown 对到人工标注，分文本、公式、表格、阅读顺序打分。出处：该 commit 的 `README.md` 开头（“benchmark for evaluating diverse document parsing in real-world scenarios”；“1651 PDF pages”；“designed for Document Parsing”）以及 End-to-End Evaluation 一节的 Overall 公式。

## 环境线索

- 容器: README “Option A: Docker” 推荐单容器镜像 `ghcr.io/zeng-weijun/omnidocbench-eval:repro-ubuntu2204`，用一次 `docker run` 挂载 GT、预测目录和输出目录。抓取日用 GHCR 匿名 pull token 读到该 tag 的 manifest，digest `sha256:6116ad72172e763b5c43e963d5efebf2093f2362b975f58156ce4f6c9142e617`，24 个 layer，`size` 合计 13,650,069,890 字节。镜像在个人命名空间 `zeng-weijun`，不在 `opendatalab`。该 commit 树里没有 `Dockerfile`、compose 或 README 点名的 `script/build_repro_docker_image.sh`、`script/verify_repro_runtime.sh`。未拉取镜像，因此 README 写的 Python 3.10 / TeX Live 2025 / ImageMagick 7.1.1-47 / Ghostscript 9.55.0 没有在镜像内核对。
- 出网: 拉上述镜像要出网。Conda 路线要 wget CTAN 的 TeX Live 与 ImageMagick 源码。`pyproject.toml` 的 `[tool.omnidocbench.runtime]` 写 `needs_writable_hf_cache = true`，并 prefetch `bleu`、`meteor`。`tools/model_infer/` 里有打外部 API 或本地 OpenAI 兼容服务的推理脚本。评分命令本身假定 GT 与预测已在本地。
- GPU: 评分 README 与 Docker 段落未要求 GPU；worker 按 CPU 核数设置。`tools/model_infer/` 中部分本地模型脚本使用 CUDA（例如 `GOT-OCR_formula.py`、`Dolphin_img2md.py`）。
- K8s: unknown。仓库内未见 Kubernetes 清单。`skills/SKILL.md` 文案提到 remote SSH/H-cluster，没有展开成清单。
- 多容器: 未见 compose。文档中的推荐跑法是一个容器。

## 评分

确定性程序分，不另调 judge 模型。`configs/end2end.yaml` 与 README 使用归一化编辑距离、CDM、TEDS；README 另列 BLEU、METEOR、COCODet。Overall 为 `((1 - Text Edit Distance) * 100 + Table TEDS + Formula CDM) / 3`。CDM 依赖 pdflatex / ImageMagick / Ghostscript 做渲染比对，不是 LLM。`quick_match` 有超时回退（`quick_match_truncated_timeout_sec` 等），超时路径会改匹配，但仍是程序规则。

版本字符串没有对齐：`pyproject.toml` 的 `version` 是 `1.6.0`；README 2026/04/10 写 main 的代码和数据集为 v1.6；2026/04/30 写从 v1.6 更新到 v1.7；榜单表题为 `v1.6_full`。未再下载 HF README 去裁定数据集卡片上的版本号。

## agent / runtime 线索

评分入口是 `python pdf_validation.py --config <config_path>`。`pdf_validation.py` 把命令行参数交给 `src.cli.main`；`pyproject.toml` 也写了这个入口。被测解析器不在评分进程里；`tools/model_infer/` 是按模型分开的推理脚本，形态是单页图转 Markdown。`skills/SKILL.md` 是给操作者用的评测助手说明（name: `omnidocbench-eval-helper`），不是被测对象的控制回路。未见被测模型的多步 agent runtime。

## 体积与是否入 git

- GitHub API `size`: 10224 KB。浅克隆（`--depth 1`，仅在 `/tmp`）整目录约 22 MB，其中 `.git` 约 8.6 MB，工作树约 13 MB（`demo_data` 约 9.3 MB）。
- HF 数据集约 1.55 GB，不在该 git commit 里。
- 推荐镜像 layer size 合计约 13.65 GB，未拉取。
- 本目录不放入克隆、数据集或镜像。只留本文件与 `excerpt.md`。本线程不 git commit。

## 未抓取项与原因

- 未把克隆留在 `/workspace`：浅克隆约 22 MB，超过 5 MB 上限。
- 未下载 HF 上约 1.55 GB 的页面图与 `OmniDocBench.json`。
- 未拉取 GHCR 镜像，未执行 `pdf_validation.py`。镜像内版本与构建脚本内容因此未核对；构建脚本在该 SHA 的 git 树中不存在。
- 未克隆 EvalScope，未打开 OpenDataLab 数据集页正文。
- v1.6 / v1.7 文案冲突未用数据集卡片裁定。

MANIFEST-END
