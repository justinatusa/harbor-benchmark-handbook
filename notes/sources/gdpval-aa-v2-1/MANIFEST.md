# MANIFEST

- slug: gdpval-aa-v2-1
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://artificialanalysis.ai/evaluations/gdpval-aa

## 官方仓

- GDPval-AA 的跑分脚本、judge 提示词、E2B 镜像定义：没有公开 git 仓。方法页把流程写在网页上，不在某个任务仓库里。
- 数据不是 GitHub 仓。`https://github.com/openai/gdpval` 返回 404。
- 公开 gold 数据集在 Hugging Face：https://huggingface.co/datasets/openai/gdpval
- HF git 修订: `11e7900cdcac61bc4daf59e65feb238acda98fbf`
- HF `lastModified`: 2026-02-10T19:31:04.000Z
- HF `gated`: false
- 方法页点名的开源代理框架（不是 GDPval 任务仓）: https://github.com/ArtificialAnalysis/Stirrup
- 该仓默认分支 main 的 HEAD: `247f24d56b2108235880ed2a2baea5d35b5a67ee`
- HEAD 说明: chore: add 7 day exclusion rule (#81)
- committer 日期: 2026-08-04T00:02:44Z
- 许可证: MIT
- 对该 HEAD 做了一次浅克隆并全文检索 `gdpval`：0 处。递归树 177 个条目，路径里也没有 gdpval。Stirrup 是通用代理框架，不含本榜的任务循环。

## 论文 / blog / HF

- 评测页标题是 GDPval-AA v2.1 Leaderboard: https://artificialanalysis.ai/evaluations/gdpval-aa
- 方法: https://artificialanalysis.ai/methodology/intelligence-benchmarking 的 “GDPval-AA v2.1” 一节。v2.1 相对 v2 只改 Elo 锚定和 Crowd-BT 拟合。
- 数据集论文（不是 AA 跑分论文）: https://arxiv.org/abs/2510.04374
- 没有单独的 GDPval-AA arXiv。本次检索没有找到 AA 自己的论文页。
- HF id: `openai/gdpval`
- 数据集卡 README 含一行 canary。本笔记不抄该字符串。

## 测什么

测模型能否在隔离沙箱里做出真实职业任务的交付文件（文档、幻灯片、图、表格），再用盲评两两比较合成 Elo。评测页写本榜是 220 题、44 个职业、9 个行业。出处：https://artificialanalysis.ai/evaluations/gdpval-aa 页首。OpenAI 论文摘要写的全集是 1,320 题；AA 写明自己用的是上述 HF gold 集。

## 环境线索

运行描述来自方法页 GDPval-AA v2.1 的 Task Submission，并与同页给出的提交提示词一致。没有公开任务仓可以再对一遍。

- 容器: 有。每题新建一个 E2B sandbox。提示词写 isolated Linux sandbox，用户 `user`（UID 1000），家目录 `/home/user`。镜像是 Debian trixie，Python 3.13，并预装 LibreOffice、Pandoc、Tesseract、FFmpeg、ImageMagick、TeX Live、Chromium 等。v2 相对论文环境加了依赖，包括完整 TeX Live。方法页列出 419 个钉死的 Python 包，本笔记不抄清单。
- 出网: 代理有 Web Fetch 和 Web Search（Brave，返回前 5 条）。`code_exec` 本身能否直接出网，这段提示词没写。unknown。
- GPU: 方法页的包和系统包清单没有写 GPU。unknown。
- K8s: 没看到。unknown。
- 多容器: 没看到。描述是每题一个 sandbox。
- 其他已写明的限制: 最多 250 turns；单条命令 10 分钟；上下文超过 70% 后摘要并清掉更早的轮次；完成靠 `finish`，做不到可 `abandon_task_finish`。

## 评分

要另外的 judge 模型，不是确定性对答案。

两阶段：模型交文件，再由三模型面板里抽一个 judge 做盲评，比较同一题的两份提交。方法页写面板是 GPT-5.6 Sol（medium reasoning）、Gemini 3.8 Flash（high reasoning）、Claude Opus 5（high effort）。含音频或视频的题改由 Gemini 3.8 Flash 单独看。文档会抽成文本和图片再交给 judge。汇总是 Crowd-BT / Bradley-Terry 极大似然 Elo，把 DeepSeek V4.1 Flash (max) 钉在 1600。Elo 计算是程序，胜负来自 judge。

## agent / runtime

有框架，没有本榜的任务运行时源码。方法页写所有模型用 Stirrup，在 E2B 里调用上面六个工具。Stirrup 仓库 HEAD 已核实，但不含 gdpval 字样。judge 是另一套三个模型。

## 体积与是否入 git

HF API `usedStorage`: 2,383,025,593 字节（约 2.22 GiB）。文件 552 个。任务表 `data/train-00000-of-00001.parquet` 的 Content-Length 是 1,913,489 字节；其余是 `deliverable_files/` 里的办公文件和音视频。大于 5MB，没有克隆进 `/workspace`。

Stirrup 浅克隆约 3.9MB，只在 `/tmp` 检索后删除，没有放进本仓。

本目录文本：本文件，以及 `excerpt-task-prompt.txt`（方法页提示词摘录）。都小于 200KB。本次没有 git commit。

## 未抓取项与原因

- GDPval-AA 跑分脚本、judge 提示词全文、E2B 镜像构建文件：没有公开仓库。
- HF 上 2.22 GiB 的参考交付物：超过允许留在工作区的体积。
- 方法页 419 个 Python 包和 Debian 包钉版本：清单很长，且不是任务数据。已确认它属于 v2.1 这一节。
- `code_exec` 的出网策略：提示词只写了 Web 工具，没有写 shell 禁网或放行。
- 检索里出现过第三方仓库里的 GDPval 适配。那不是 Artificial Analysis 或 OpenAI 的官方仓，没有把它的 SHA 记成官方。

MANIFEST-END
