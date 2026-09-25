# SpreadsheetBench 2

可视化不走单元格那套比较。导出图要在 Windows 上用 Excel 或 WPS 做，评分还要另调视觉模型。

1. 一句话测什么。测表格代理能否在真实商业工作簿上做完财务建模、模板、纠错和可视化，共 321 题。出处是 https://arxiv.org/abs/2606.29955 摘要。README 把题放在 `Debugging`、`Financial_Model`、`Template`、`Visualization`。

2. 官方源。仓库 https://github.com/RUCKBReasoning/SpreadsheetBench-2 ，commit `5c160265aa93c15b38e4034cbf1e09ab498335d9`（2026-08-22，说明 “docs: add dataset recalculation reminder”）。论文 https://arxiv.org/abs/2606.29955 。数据集 https://huggingface.co/datasets/KAKA22/SpreadsheetBench-v2 ，修订 `5a2215ed4121945ab09d8723df2995602090b042`。题面不在该 commit 的 git 树里，README 要求放到 `data/`。

3. 形态。`task`、`environment`、`verifier`、`agent`、`dataset`。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。可视化脚本默认模型是 `glm-4.6v`。README 写这一步要在 Windows 上通过 Excel 或 WPS 把图导出来。清单没有给出 `task.toml` 或 `dataset.toml`。

5. 环境。每题一个 Docker 容器。镜像由 `SWE-agent/spreadsheet.Dockerfile` 构建，标签 `spreadsheetbench-v2`，基础镜像 `python:3.11.10-bullseye`，装了 LibreOffice。论文附录写执行期间不提供网络。Dockerfile 和沙箱描述没写 GPU，这项是 unknown。没看到 Kubernetes。`--num_workers` 是每个并发任务各起一个容器，输出在容器停止后拷回。

6. 评分。单元格题用程序比较输出和标准答案。数值相对误差默认 0.01。不该改的单元格正确率达到 0.998 就当成 1。该改的和不该改的都全对，任务分才是 1，否则是 0。比较前 README 要求用 LibreOffice 重算。可视化走 `evaluation/run_visual_vlm_checklist_eval.py`，清单里通过的比例高于 0.7 算对。

7. agent/runtime。有。README 用仓内 SWE-agent：`sweagent run --config config/spreadsheet.yaml`，可视化用 `config/visualisation.yaml`。工具是 `bash`、`view_xlsx`、`submit`。一次回复只能调一个工具。`execution_timeout` 是 60 秒，`per_instance_call_limit` 是 50。人工操作的 Excel 产品不在这个仓里。

8. 迁入代价。高。单元格比较能放进单个容器，可视化却要另调模型，还要 Windows 上的 Excel 或 WPS 导出。全量题面在 Hugging Face 的压缩包里，该 commit 的 git 树没有 `data/`。清单没有给出 Harbor 的 task 目录。

9. 对抽象的压力。`verifier` 要同时容纳单元格的程序比较，和可视化的模型打分。`environment` 在可视化导出这一步要离开 Linux 容器，改到 Windows 上的 Excel 或 WPS。`agent` 是仓内 SWE-agent 的单工具循环。

10. 本地摘录。私有摘录未随公开手册发布。
