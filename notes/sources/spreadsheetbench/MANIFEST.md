# MANIFEST

- slug: spreadsheetbench
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://github.com/RUCKBReasoning/SpreadsheetBench

## 官方仓

- 核实到的官方仓: https://github.com/RUCKBReasoning/SpreadsheetBench
- 默认分支: main
- commit SHA: 49b73a94775fb489063f60ca1865e3a650079a79
- commit 说明: Merge pull request #32 from RyanMarten/cross-platform-evaluation
- committer 日期: 2026-03-12T03:58:22Z
- 远程 tags: 没有
- GitHub API `size`: 322841 KB；`git/trees/main?recursive=1` 的 blob 合计 139,859,609 字节，`truncated=false`，树 SHA 与 HEAD 相同
- 许可证: README 写 CC BY-SA 4.0；GitHub API 的 license 字段为空

## 论文 / blog / HF

- 论文: https://arxiv.org/abs/2406.14991 （SpreadsheetBench: Towards Challenging Real World Spreadsheet Manipulation）
- 主页: https://spreadsheetbench.github.io/
- README 新闻: NeurIPS 2024 D&B Track spotlight
- HF: https://huggingface.co/datasets/KAKA22/SpreadsheetBench
- HF 修订: ab0b742b0fc95b946f212d80ac7771b5531272e4
- HF `lastModified`: 2025-12-03T05:01:26.000Z
- HF 文件: `spreadsheetbench_912_v0.1.tar.gz`、`spreadsheetbench_verified_400.tar.gz`（API 未给出单文件字节）

## 测什么

测模型能否按真实 Excel 论坛题意改表格：912 道来自线上论坛的操作指令，每题约三个输入/答案表，用类似 Online Judge 的多测试用例看解法是否稳。出处：仓库 README Overview，以及 arXiv:2406.14991 摘要。

## 环境线索

- 容器: 有。`code_exec_docker/Dockerfile.api`（`python:3.9`，装 tornado、docker、kubernetes）和 `Dockerfile.executor`（`quay.io/jupyter/datascience-notebook:2023-10-20`，Jupyter Kernel Gateway，torch 走 CPU wheel）。
- 出网: 构建要拉镜像和 pip。`jupyter.py` 里 `containers.run` 没有 `network_mode`。运行期出网策略仓内没有单独写成禁网或放行，记 unknown。
- GPU: 执行器镜像安装 CPU 版 torch；Docker 限制是 8GB 内存和 2 CPU，没有 GPU device。推理依赖写了 `vllm` 和 OpenAI 兼容接口，仓内没有规定推理 GPU 型号。代码执行侧未见 GPU 要求。
- K8s: 可选，不是默认。`api.py` 在 `USE_KUBERNETES=1` 时用 `JupyterGatewayKubernetes`，否则用 Docker。K8s 限制示例为 memory 512Mi、cpu 1，命名空间默认 `codeact-chat-ui`。没有提交 Kubernetes 清单。
- 多容器: 代码执行路径是两个镜像（execute-api 与 executor）。评测脚本 `evaluation/scripts/evaluation.sh` 是本机 `python evaluation.py`，另要 LibreOffice 7.5+ 或 Windows Excel/pywin32 重算公式，这一步不在上述容器里。

## 评分

确定性程序分，不另调 judge 模型。`evaluation/evaluation.py` 把单元格值（数值先四舍五入到 2 位小数）与答案表做相等比较；`soft_restriction` 是三个测试用例的通过比例，`hard_restriction` 是三题全过才为 1。填色/字体颜色比较函数在，但在 `cell_level_compare` 里被注释掉。公式重算是 LibreOffice 或 Excel，不是评判模型。

同一次 commit 的 `evaluation()` 把 `proc_path` 设成 `*_input.xlsx`，模型输出路径 `*_output.xlsx` 被注释。因此这份脚本按字面会拿答案表去比输入表，而不是比模型输出。README 描述的仍是 OJ 式评测。本次没有运行脚本。

## agent / runtime

官方 `inference/` 有单轮，以及多轮 ReAct 加代码执行反馈。生成的 Python 在 Jupyter kernel 里执行，内核由上面的 Docker（或可选 K8s）网关拉起。README 致谢 code-act 的执行环境。这是仓库自带的推理脚本，不是另附的代理产品名。

## 体积与是否入 git

上游 git 含数据压缩包：`data/spreadsheetbench_912_v0.1.tar.gz` 95,752,357 字节，`data/sample_data_200.tar.gz` 19,936,871 字节，`data/spreadsheetbench_verified_400.tar.gz` 14,958,255 字节，另有数 MB 图片。整个官方仓大于 5MB，没有克隆进 `/workspace`。本目录只留本文件和两个小于 200KB 的文本摘录。这些摘录本次没有 git commit。

## 未抓取项与原因

- 三个数据 tar 和图片：体积超过本次允许留在工作区的克隆上限，也超过单文件摘录上限。
- HF 上的同名 tar：与 git 内压缩包重复，未下载。
- 没有运行推理或 `evaluation.py`，所以上面关于 `proc_path` 的说明只来自源码，不是实测分数。
- `requirements.txt` 里的 `vllm` 未钉版本，推理 GPU 规格仓内没有写。

MANIFEST-END
