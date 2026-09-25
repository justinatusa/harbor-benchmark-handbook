# MANIFEST

- slug: spreadsheetbench-2
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://github.com/RUCKBReasoning/SpreadsheetBench-2

这是 SpreadsheetBench 2，不是 V1。V1 是 912 道论坛题，仓在 https://github.com/RUCKBReasoning/SpreadsheetBench ，论文 arXiv:2406.14991。本文件不记录 V1 的文件。

## 官方仓

- 核实到的官方仓: https://github.com/RUCKBReasoning/SpreadsheetBench-2
- 默认分支: main
- commit SHA: `5c160265aa93c15b38e4034cbf1e09ab498335d9`
- commit 说明: docs: add dataset recalculation reminder
- committer 日期: 2026-08-22T13:33:02Z
- GitHub API `license`: 空
- GitHub API `size`: 1862 KB
- 该提交递归树: 253 个条目，`truncated=false`，blob 合计 3,033,224 字节
- 仓内没有 `data/` 题面。README 要求把数据放到 `data/`，并在实验前用 `open_spreadsheet` 重算输入和 golden。
- 依赖的代理脚手架是仓内目录 `SWE-agent/`，README 致谢上游 https://github.com/SWE-agent/SWE-agent 。本次没有再对上游单独取 SHA。

## 论文 / blog / HF

- 论文: https://arxiv.org/abs/2606.29955
- HTML: https://arxiv.org/html/2606.29955
- 项目页（同一站点下半是 V2，上半是 V1）: https://spreadsheetbench.github.io/
- HF: https://huggingface.co/datasets/KAKA22/SpreadsheetBench-v2
- HF 修订: `5a2215ed4121945ab09d8723df2995602090b042`
- HF `lastModified`: 2026-09-10T07:44:04.000Z
- HF `usedStorage`: 498,704,038 字节
- HF 文件与 Content-Length:
  - `spreadsheetbench-v2.zip` 134,207,025
  - `spreadsheetbench-v2-09-10.zip` 134,232,213
  - `data_example_05_11.zip` 15,007,033
  - `trajectory_example.zip` 158,619,774

## 测什么

测表格代理能否做完真实商业工作簿上的端到端流程：财务建模/模板、纠错、可视化。321 题，平均 11.8 个工作表、593.5 处单元格修改。出处：arXiv:2606.29955 摘要。README 用同一句任务定义，并写成四个目录：`Debugging`、`Financial_Model`、`Template`、`Visualization`。

## 环境线索

- 容器: 有。每题一个 Docker 容器，镜像由 `SWE-agent/spreadsheet.Dockerfile` 构建，标签 `spreadsheetbench-v2`。基础镜像 `python:3.11.10-bullseye`，装 LibreOffice、openpyxl、numpy、pandas、matplotlib、xlsxwriter、swe-rex。全文见 `excerpt-dockerfile`。
- 出网: 论文附录写执行期间不提供网络，代理只能用沙箱里的工具和题目文件。构建镜像本身要拉 Debian 包和 pip。模型 API 在容器外。
- GPU: Dockerfile 和论文附录的沙箱描述没有写 GPU。unknown。
- K8s: 没看到。unknown。
- 多容器: 不是一道题多个协作容器。README 写 `--num_workers` 会为每个并发任务各起一个独立容器，只读挂载该题的输入文件，输出目录在容器停止后拷回。

## 评分

单元格题是确定性程序分。可视化题要另外的 judge 模型。

`evaluation/evaluation.py` 比较模型输出和 golden。数值相对误差默认 0.01；未改动单元格的正确率 ≥ 0.998 时当成 1；任务分只有在“不该改的单元格”和“该改的单元格”都全对时为 1，否则为 0。Debugging 路径里，路径含 `Color` 时比字体色，含 `Embedded` 时比公式。摘录见 `excerpt-scoring.py`。比较前 README 要求用 LibreOffice 重算缓存值（`evaluation/open_spreadsheet.py`）。

可视化不走上面的脚本。`evaluation/run_visual_vlm_checklist_eval.py` 默认模型 `glm-4.6v`，`DEFAULT_ACC_THRESHOLD = 0.7`，`score > 0.7` 则 `acc=1`。score 是 checklist 里 PASS 的比例。README 写这一步要在 Windows 上通过 Excel/WPS COM 把图导出来。项目页写 Acc = 通过条数 / 总条数，高于 70 算对。论文正文把可视化的任务分说成 rubric 通过率，并写 VLM 可能有噪声；0.7 这个阈值在评测脚本和项目页，不在摘要里。

## agent / runtime

有。README 用仓内 SWE-agent：`sweagent run --config config/spreadsheet.yaml`（可视化用 `config/visualisation.yaml`）。`spreadsheet.yaml` 的工具是 `bash`、`view_xlsx`、`submit`，一次回复只能调一个工具，`execution_timeout` 60 秒，`per_instance_call_limit` 50。论文写八个前沿模型走这套多轮脚手架，另外用人工操作 Claude for Excel、ChatGPT for Excel 等产品做对照。那些产品的 runtime 不在本仓。

## 体积与是否入 git

代码树 blob 合计约 3.0MB，其中 `images/overview.png` 396,795 字节。代码仓本身可以进 git，但题面不在仓里。

HF 上两份全量 zip 各约 134MB，轨迹示例约 159MB，样例 zip 约 15MB。都大于 5MB，没有下载，也没有克隆进 `/workspace`。

本目录是本文件、`excerpt-scoring.py`、`excerpt-dockerfile`。本次没有 git commit。

## 未抓取项与原因

- 四个数据 zip：单文件 15–159MB。
- 上游 SWE-agent 自己的 commit：本仓是拷进来的目录，没有再解析它对应的上游 SHA。
- V1 的 912 题和 `evaluation/evaluation.py` 旧逻辑：另一个 slug，不混在这里。
- 没有构建镜像，也没有跑评测。Windows COM 导出这一步只来自 README，没有在本机验证。
- 单元格比较的 0.01 容差和 0.998 回归阈值来自这份 `evaluation.py`，论文摘要只写“每个单元格都与 golden 一致”。两处口径都记在上面，没有合成一个新规则。

MANIFEST-END
