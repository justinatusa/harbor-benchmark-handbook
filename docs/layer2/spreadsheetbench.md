# SpreadsheetBench

该 commit 的 `evaluation()` 把 `proc_path` 设成 `*_input.xlsx`，模型输出路径 `*_output.xlsx` 被注释。README 描述的仍是多测试用例评测。本次没有运行脚本。

1. 一句话测什么。测模型能否按真实 Excel 论坛题意改表格。912 道来自线上论坛的操作指令，每题约三个输入表和答案表，用多组测试看解法是否稳。出处是仓库 README Overview 与 arXiv:2406.14991 摘要。

2. 官方源。https://github.com/RUCKBReasoning/SpreadsheetBench ，`main` commit `49b73a94775fb489063f60ca1865e3a650079a79`（2026-03-12）。没有 tag。论文 https://arxiv.org/abs/2406.14991 。数据集 https://huggingface.co/datasets/KAKA22/SpreadsheetBench ，修订 `ab0b742b0fc95b946f212d80ac7771b5531272e4`。

3. 形态。`dataset`、`environment`、`verifier`、`agent`。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。代码执行路径是两个镜像。清单没有给出 `task.toml` 或 `dataset.toml`。

5. 环境。`code_exec_docker/Dockerfile.api` 基于 `python:3.9`。`Dockerfile.executor` 基于 `quay.io/jupyter/datascience-notebook:2023-10-20`，torch 走 CPU 轮子。Docker 限制是 8 GB 内存和 2 个 CPU，没有 GPU 设备。`USE_KUBERNETES=1` 时改走 Kubernetes，否则用 Docker。仓库没有提交 Kubernetes 清单。`evaluation/scripts/evaluation.sh` 在本机跑 Python，另要 LibreOffice 7.5+ 或 Windows 上的 Excel 重算公式，这一步不在上述容器里。运行期出网策略没有写成禁网或放行，记 unknown。

6. 评分。`evaluation/evaluation.py` 把单元格值与答案表做相等比较，数值先四舍五入到 2 位小数。`soft_restriction` 是三个测试用例的通过比例，`hard_restriction` 是三题全过才为 1。公式重算用 LibreOffice 或 Excel。上面的 `proc_path` 来自阅读该 commit，脚本没有在本次抓取里运行。

7. agent/runtime。`inference/` 有单轮，也有多轮推理、动作、再读代码执行反馈。生成的 Python 在 Jupyter kernel 里执行，内核由上面的 Docker 或可选的 Kubernetes 网关拉起。

8. 迁入代价。高。执行要 api 与 executor 两个镜像，评分还要本机 LibreOffice。`data/spreadsheetbench_912_v0.1.tar.gz` 为 95,752,357 字节。接入前要核对 `proc_path` 指向输入表这一处。

9. 对抽象的压力。`environment` 把代码执行放在两个镜像里，公式重算放在宿主机的 LibreOffice。`verifier` 的规则是单元格相等，但该 commit 里写入比较的路径指向输入表。

10. 本地摘录。[`notes/sources/spreadsheetbench/MANIFEST.md`](../../notes/sources/spreadsheetbench/MANIFEST.md)。
