# MANIFEST

- slug: 3dcodebench
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://www.3dcodebench.com/

## 官方仓

- 入口是项目站，不是 git。2026-09-24 打开首页，页内链到 https://github.com/gaoypeng/3dcodebench ，以及该仓的 CONTRIBUTING.md。
- 核实到的官方仓: https://github.com/gaoypeng/3dcodebench
- 该仓 homepage 字段为 https://www.3dcodebench.com/ 。许可证 Apache-2.0。
- 默认分支: main
- commit SHA: 42c7780ed3fcbd466f17f058f62e7996233777f7
- 核实: `git ls-remote` HEAD 与 commits API 一致。message 为 “Update paper links and Infinigen credits”，committer 日期 2026-06-02T05:08:03Z。
- GitHub API `size`: 1770 KB。该 SHA 的递归 git tree 未截断，77 个 blob，合计 822,961 字节。212 个类别脚本不在这个 git 里。

## 论文 / blog / HF

- 论文: arXiv [2606.01057](https://arxiv.org/abs/2606.01057)，“3DCodeBench: Benchmarking Agentic Procedural 3D Modeling Via Code”。首页 bibtex 与 README 新闻（2026-06-01）同一编号。
- 项目页: https://www.3dcodebench.com/
- 人类偏好竞技场: https://www.3dcodebench.com/arena
- 没有单独的产品 blog URL。
- HF id: `YipengGao/3DCode`。API `sha` `0db485b63a2991231f0fad6c6e0dc01bcbbced1e`，`lastModified` 2026-09-20T17:54:40.000Z，卡片许可证 mit，`gated` false。首页也链到这个数据集。
- HF 顶层目录: `3DCodeBench/`、`3DCodeData/`、`3DCodeBench_ModelLogs/`、`3DCodeBench_extra_ablation_logs/`、`assets/`。
- `3DCodeBench/` 递归 tree：848 个文件，4,398,687 字节。
- `3DCodeBench_ModelLogs/data/`：16 个 parquet，合计 198.5 MB。最大的是 `thinking_ablation.parquet`（72.7 MB）。
- `3DCodeData/` 的 tree 接口一次返回 1000 条且仍是子目录，没有把全库字节加总。

## 测什么

测视觉语言模型能否写出 Blender 5.0 Python，按文字或参考图把指定物体程序化建出来。出处: 该 SHA 的 README 第二段（212 个类别；单次、多轮、coding-agent 三种设置），以及首页标题和 arXiv:2606.01057 摘要。

## 环境线索

- 容器: 该 SHA 没有 Dockerfile 或 compose。Blender 5.0 要单独安装，路径放在 `BLENDER`。unknown。
- 出网: 类别脚本、3DCodeData 和模型日志都从 HF 下载。推理要 Gemini / Anthropic / OpenAI 的 API，或本机已登录的 CLI。SigLIP-2、DINOv3、Uni3D 权重要另下。
- GPU: 分项。`metrics/README.md` 写 executability、failure taxonomy、Chamfer 不需要 GPU；SigLIP-2 / DINOv3 / Uni3D 需要 GPU，并给出 CUDA 12.1 的 pip 示例。
- K8s: 没看到。`tasks/coding_agent/README.md` 写批量脚本故意不附带，以便不绑到某种集群。unknown。
- 多容器: 没看到。unknown。

## 评分

主表不是单一个 LLM judge，也不是单一确定性分数。程序分：Blender 能否跑出非空 mesh（executability）；Chamfer 距离（CPU）。还要加载别的模型：SigLIP-2、DINOv3、Uni3D。另有可选 LLM-as-judge，`metrics/llm_judge/README.md` 默认 Gemini 3 Pro，对代码或渲染图做 1–5 分或 A/B。首页的 Elo 来自 3DCodeArena 的人类两两偏好，不是这段代码自动算出的。`metrics/README.md` 写汇总脚本 `scripts/aggregate.py` 不在本仓。

## agent / runtime

三种都有证据。单次 text-to-3D / image-to-3D 是一次 API 调用（`tasks/text_to_3d/run.py`、`tasks/image_to_3d/run.py`）。多轮是无状态重试：`tasks/multi_turn/README.md` 写最多 T=3，每次新请求只带上一份代码和 Blender traceback 末尾约 40 行。coding-agent 用本机 CLI：Claude Code、Codex、Gemini CLI、agy（Antigravity），脚本在 `tasks/coding_agent/`。agent 被要求自己调用 `blender --background`。Claude Code 脚本把墙钟限制写为 30 分钟。

## 体积与是否入 git

- 代码仓 checkout 约 0.82 MB。没有把克隆放进 `/workspace`。`assets/logo.png` 271,215 字节没有抄。
- 评测用的 `3DCodeBench/` 约 4.4 MB，模型日志 parquet 约 198.5 MB，3DCodeData 未加总。这些都没有下载。
- 本目录只有 MANIFEST 和短摘录。本次没有 git commit。

## 未抓取项与原因

- `3DCodeData/` 全库字节数：tree 接口按 1000 条分页，没有逐页加总，也没有下 GLB / WebP。
- `3DCodeBench_extra_ablation_logs/`：只看到目录名，没有展开。
- `3DCodeBench_ModelLogs/data/*.parquet` 与 `agent_logs/`：日志体积已超过 5 MB。
- `scripts/aggregate.py`：README 写它不在这个仓库。
- 竞技场页面只确认了首页上的链接，没有存投票记录。
- 没有安装 Blender，也没有跑评分脚本。

MANIFEST-END
