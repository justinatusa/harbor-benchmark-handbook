# MMMU-Pro

代码仓同时装着 MMMU 本体。MMMU-Pro 的题在 Hugging Face，不在仓内的图片副本里。GPU 没有写成评测条件。

1. 一句话测什么。测多模态模型是不是真的要同时看图和读题：从 MMMU 里去掉纯文本模型就能答对的题，把选项扩到最多 10 个，并增加一套题目嵌在截图或照片里的输入。总分是 10 选项设置和 vision 设置的平均。出处是 https://arxiv.org/abs/2409.02813 摘要与第 3.1 节。

2. 官方源。代码仓 https://github.com/MMMU-Benchmark/MMMU ，commit `268471d0d488258990025331c7528359c324aa25`（2026-07-28，说明 “Merge pull request #86 from Yunnglin/evalscope-mmmu-docs-20260728-102038”）。MMMU-Pro 的推理和评分在子目录 `mmmu-pro/`。论文 https://arxiv.org/abs/2409.02813 。数据集 https://huggingface.co/datasets/MMMU/MMMU_Pro ，修订 `563f3e84bb3b90893083a1f039cfa13077f2302b`。三个 config 都是 test：`standard (10 options)`、`standard (4 options)`、`vision`，各 1730 行。

3. 形态。`task`、`dataset`、`verifier`、`agent`。清单没写容器形式的 `environment`，也没写 `adapter`。

4. 与 Harbor 距离。unknown。题目和 `mmmu-pro/evaluate.py` 公开，比对选项字母，不另调模型。入口是 Python 脚本。清单没有给出 `task.toml` 或 `dataset.toml`。缺一句评测不要 GPU，证据不够放进其余四档。

5. 环境。`mmmu-pro/README.md` 是 `python infer/infer_xxx.py` 和 `python evaluate.py`，未见 Dockerfile。容器：unknown。下载数据和调用闭源模型时要出网。题目本身是本地图文。GPU：unknown。本地开源模型通常要 GPU，走模型服务则不要本地 GPU。Kubernetes 和多容器都是 unknown。

6. 评分。不另调模型。`eval_multi_choice` 要求解析后的选项字母和标准答案完全相同。括号和 “Answer:” 这几种匹配都失败时，会随机抽一个选项。复现分数要固定随机种子。这个兜底不是另一个模型。论文把总分定义成 10 选项设置和 vision 设置的平均。4 选项设置只作对照。

7. agent/runtime。官方路径是单轮脚本。`infer_xxx.py` 接收模型名、`cot` 或 `direct`，以及 `standard(10 options)`、`standard(4 options)` 或 `vision`。一次调用模型，没有多步工具回路。

8. 迁入代价。中。评分脚本短，图像约 2849.76 MiB，而且不在 git 里。没有 task 目录。GPU 仍是 unknown。

9. 对抽象的压力。缺一句评测不要 GPU。压力在 `dataset`。三套配置在 Hugging Face，没有 `dataset.toml`。`agent` 是一次模型调用，没有多步工具回路。`environment` 没有镜像。

10. MANIFEST 路径。`notes/sources/mmmu-pro/MANIFEST.md`
