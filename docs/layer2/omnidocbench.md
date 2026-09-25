# OmniDocBench

评分是程序比对，不另调模型。README 推荐的评测镜像不在这个 commit 的文件树里，它点名的构建脚本也不在。

1. 一句话测什么。测真实版式 PDF 页的文档解析：把模型输出的页面 Markdown 对到人工标注，分文本、公式、表格和阅读顺序打分。出处是 commit `f133a71e9e91c3621c7ce8994200a7b394a06eb3` 的 README 开头（“1651 PDF pages”；“designed for Document Parsing”）以及 End-to-End Evaluation 一节的 Overall 公式。论文 https://arxiv.org/abs/2412.07626 。

2. 官方源。仓库 https://github.com/opendatalab/OmniDocBench ，`main` HEAD `f133a71e9e91c3621c7ce8994200a7b394a06eb3`（2026-09-11，说明 “Merge pull request #257 from dt-yy/main”），Apache-2.0。同远程还有分支 `v1_0`、`v1_5`，没有名为 `v1_6` 或 `v1_7` 的分支。数据集 https://huggingface.co/datasets/opendatalab/OmniDocBench ，sha `aa1ee96d106dbe53d0ae59474d75c6e6d9b53fec`。分页 tree 合计约 1.55 GB，其中 `OmniDocBench.json` 约 42.21 MB。`pyproject.toml` 的 `version` 是 `1.6.0`。README 2026/04/10 写 main 为 v1.6，2026/04/30 写更新到 v1.7，榜单表题为 `v1.6_full`。清单没有用数据集卡片裁定这个版本号。

3. 形态。`dataset`、`verifier`。评分入口是 `python pdf_validation.py`。被测解析器不在评分进程里。`tools/model_infer/` 是按模型分开的单页推理脚本，不是多步 `agent`。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。公开仓没有 Harbor `task.toml`。评分脚本公开，接入要新写 task 目录。清单没有给出 `dataset.toml`。

5. 环境。README “Option A: Docker” 推荐单容器镜像 `ghcr.io/zeng-weijun/omnidocbench-eval:repro-ubuntu2204`。抓取日读到该 tag 的 manifest，digest `sha256:6116ad72172e763b5c43e963d5efebf2093f2362b975f58156ce4f6c9142e617`，layer `size` 合计 13,650,069,890 字节。镜像在个人命名空间 `zeng-weijun`，不在 `opendatalab`。该 commit 树里没有 `Dockerfile`、compose，也没有 README 点名的 `script/build_repro_docker_image.sh`。未拉取镜像，因此 README 写的 Python 3.10 / TeX Live 2025 / ImageMagick 7.1.1-47 / Ghostscript 9.55.0 没有在镜像内核对。评分 README 未要求 GPU；`tools/model_infer/` 里部分本地模型脚本使用 CUDA。仓库内未见 Kubernetes 清单。文档中的推荐跑法是一个容器，未见 compose。

6. 评分。确定性程序分，不另调 judge。`configs/end2end.yaml` 与 README 使用归一化编辑距离、CDM、TEDS；README 另列 BLEU、METEOR、COCODet。Overall 为 `((1 - Text Edit Distance) * 100 + Table TEDS + Formula CDM) / 3`。CDM 依赖 pdflatex、ImageMagick、Ghostscript 做渲染比对。`quick_match` 超时会改匹配，但仍是程序规则。

7. agent/runtime。未见被测模型的多步 agent。`pdf_validation.py` 把参数交给 `src.cli.main`。`skills/SKILL.md` 是给操作者用的评测助手说明（name: `omnidocbench-eval-helper`），不是被测对象的控制回路。推理脚本按模型分开，形态是单页图转 Markdown。

8. 迁入代价。中。评分脚本公开，不另调模型。没有 Harbor task 目录。推荐镜像约 13.65 GB，而且构建脚本不在这个 SHA 的 git 树里。HF 页面图约 1.55 GB。

9. 对抽象的压力。`verifier` 是编辑距离、TEDS 和 CDM，CDM 还要本机排版工具链。`dataset` 的页面图和 `OmniDocBench.json` 不在该 git commit。`environment` 的推荐镜像不在官方命名空间，这个 commit 也没有 Dockerfile。没有代理循环可以接到 `agent`。

10. 本地摘录。[`notes/sources/omnidocbench/MANIFEST.md`](../../notes/sources/omnidocbench/MANIFEST.md)。
