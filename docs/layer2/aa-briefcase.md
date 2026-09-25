# AA-Briefcase v1.1

正榜四个场景的题面、输入和评分表不公开。Hugging Face 上的 AA-Briefcase-Lite 是第五个场景里的一周，数据集卡写明不进计分榜。

1. 一句话测什么。测代理做长程知识工作：四个私有的多周业务项目、共 91 个任务，交付表格、演示、备忘录等文件，再按核查项给分。出处是 https://artificialanalysis.ai/evaluations/aa-briefcase 页首。公告写正榜材料不公开。

2. 官方源。评测页 https://artificialanalysis.ai/evaluations/aa-briefcase 。公告 https://artificialanalysis.ai/articles/aa-briefcase （页面日期 June 18, 2026）。没有计分任务仓，也没有 arXiv。公告点名的代理框架是 https://github.com/ArtificialAnalysis/Stirrup ，main HEAD `247f24d56b2108235880ed2a2baea5d35b5a67ee`（2026-08-04，说明 “chore: add 7 day exclusion rule (#81)”）。公开示例 https://huggingface.co/datasets/ArtificialAnalysis/AA-Briefcase-Lite ，修订 `4dec557b47d43867a1648c0974db1d8208c8b677`。

3. 形态。正榜材料能对上 `task`、`environment`、`verifier`、`agent`。公开示例才有 `dataset`，而且不进榜。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。暂不宜接。正榜题面和评分表保持私有。没有公开的 `task.toml` 或 `dataset.toml`。

5. 环境。方法页写提交在 Stirrup 里、按周构建的 E2B sandbox 中运行。提示词写隔离的 Linux 容器，用户 `user`（用户号 UID 1000），家目录 `/home/user`，没有出站连接。运行时清单有 Python 3.13、文档工具、LibreOffice、Pandoc、FFmpeg、TeX Live、Chromium。没写 GPU，这项是 unknown。没看到 Kubernetes。描述是每个场景或每周一个 sandbox。每题最多 500 步，单条命令 20 分钟。

6. 评分。要另调模型。每题有两类检查：rubric 是对单份提交的通过或失败；pairwise 比较 Analytical Quality 和 Presentation。评判面板是 Claude Opus 4.8、GPT-5.5、Gemini 3.1 Pro Preview。每条结论由面板中的一个模型给出。通过失败和偏好再做极大似然 Elo，得到 Rubric、Analytical Quality、Presentation 和总的 AA-Briefcase Elo。Elo 拟合是程序，通过与否来自模型。

7. agent/runtime。有。框架是 Stirrup。运行单位是一周范围的离线 sandbox，最多 500 轮，用代码执行提交文件。三个评判模型是另一套，见上一节。

8. 迁入代价。高。计分用的 91 题和核查表没有公开网址（URL）。公开示例不进榜，而且示例的检查仍然要模型裁决。

9. 对抽象的压力。`dataset` 接不上正榜，题和评分表不公开。`verifier` 是三个模型抽样裁决，再拟合 Elo。`environment` 是没有出网的 E2B sandbox。`agent` 是 Stirrup 的代码执行循环。

10. 本地摘录。私有摘录未随公开手册发布。
