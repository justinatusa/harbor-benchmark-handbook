# 3DCodeBench

Blender 5.0 要本机另装。这个 commit 没有 Dockerfile。部分视觉指标要 GPU。汇总脚本 `scripts/aggregate.py` 不在仓里。

1. 一句话测什么。测视觉语言模型能否写出 Blender 5.0 Python，按文字或参考图把指定物体程序化建出来。出处是 commit `42c7780ed3fcbd466f17f058f62e7996233777f7` 的 README 第二段（212 个类别；单次、多轮、coding-agent 三种设置），以及 https://www.3dcodebench.com/ 和 arXiv 2606.01057 摘要。212 个类别脚本不在这个 git 里。

2. 官方源。项目站 https://www.3dcodebench.com/ 链到 https://github.com/gaoypeng/3dcodebench 。`main` HEAD `42c7780ed3fcbd466f17f058f62e7996233777f7`（2026-06-02，说明 “Update paper links and Infinigen credits”），Apache-2.0。论文 https://arxiv.org/abs/2606.01057 。人类偏好竞技场 https://www.3dcodebench.com/arena 。数据集 https://huggingface.co/datasets/YipengGao/3DCode ，sha `0db485b63a2991231f0fad6c6e0dc01bcbbced1e`（2026-09-20，`gated` false，卡片许可 mit）。HF 上 `3DCodeBench/` 约 4.4 MB。模型日志 parquet 约 198.5 MB。`3DCodeData/` 的 tree 一次返回 1000 条且仍是子目录，全库字节没有加总。

3. 形态。`dataset`、`verifier`、`agent`。单次和多轮是 API 调用。coding-agent 轨用本机 CLI，自己调用 `blender --background`。该 SHA 没有容器形式的 `environment`。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。清单没有给出 `task.toml` 或 `dataset.toml`。部分视觉指标要 GPU。主表不是单一确定性分数。

5. 环境。该 SHA 没有 Dockerfile 或 compose。Blender 5.0 的路径放在 `BLENDER`。类别脚本、3DCodeData 和模型日志都从 HF 下载。推理要 Gemini、Anthropic 或 OpenAI 的 API，或本机已登录的 CLI。SigLIP-2、DINOv3、Uni3D 权重要另下。`metrics/README.md` 写 executability、failure taxonomy、Chamfer 不需要 GPU；SigLIP-2、DINOv3、Uni3D 需要 GPU，并给出 CUDA 12.1 的 pip 示例。`tasks/coding_agent/README.md` 写批量脚本故意不附带，以便不绑到某种集群。Kubernetes、多容器没看到，记 unknown。

6. 评分。程序分加视觉模型，另有可选 LLM judge。程序分：Blender 能否跑出非空 mesh（executability）；Chamfer 距离在 CPU 上算。还要加载 SigLIP-2、DINOv3、Uni3D。`metrics/llm_judge/README.md` 默认 Gemini 3 Pro，对代码或渲染图做 1–5 分或 A/B，需要 provider API key。首页的 Elo 来自 3DCodeArena 的人类两两偏好，不是这段代码自动算出的。`metrics/README.md` 写 `scripts/aggregate.py` 不在本仓。

7. agent/runtime。三种都有证据。单次 text-to-3D / image-to-3D 是一次 API 调用（`tasks/text_to_3d/run.py`、`tasks/image_to_3d/run.py`）。多轮是无状态重试：`tasks/multi_turn/README.md` 写最多 T=3，每次新请求只带上一份代码和 Blender traceback 末尾约 40 行。coding-agent 用本机 CLI：Claude Code、Codex、Gemini CLI、agy（Antigravity），脚本在 `tasks/coding_agent/`。Claude Code 脚本把墙钟限制写为 30 分钟。

8. 迁入代价。高。代码仓小，但没有 Harbor task 目录，也没有容器。要本机安装 Blender 5.0。视觉指标还要 GPU 和另外的权重。可选 judge 与人类 Elo 是另外两套分。

9. 对抽象的压力。`verifier` 同时有 CPU 上的可执行性和 Chamfer、要 GPU 的视觉嵌入，以及可选的模型打分。`environment` 是本机 Blender，不是镜像。`agent` 的 coding-agent 轨在本机 CLI 里，自己调 `blender --background`。`dataset` 的类别脚本和 3DCodeData 在 HF，不在这个 git commit。

10. 本地摘录。[`notes/sources/3dcodebench/MANIFEST.md`](../../notes/sources/3dcodebench/MANIFEST.md)。
