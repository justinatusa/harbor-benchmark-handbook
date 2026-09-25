# AnalystBench

Anthology 页和 PDF 都没有给出代码或数据仓地址。论文说只发来源网址和重建脚本、不发抓下来的正文，公开页上这些文件的地址也没找到。

1. 一句话测什么。测模型能否在多模态文档集合上写出长篇专业报告，并用专家校验过的质量清单和 groundedness 打分。出处是 https://aclanthology.org/2026.findings-acl.1197/ 摘要。摘要写 20 个真实报告任务，模型要处理百万级输入 token。

2. 官方源。没有官方任务仓。论文 ACL Findings 2026，DOI `10.18653/v1/2026.findings-acl.1197`，PDF https://aclanthology.org/2026.findings-acl.1197.pdf 。作者 Chau Minh Pham 等。没有 arXiv id，没有 Hugging Face dataset id。GitHub 搜索命中 https://github.com/wsjq5477/AnalystBench （HEAD `7e3eed05a2a98dee39d3229fcc913918f36a7533`，2026-09-02）。该仓 README 是中文自托管评测平台，未见本篇作者或 anthology 链接，不记为官方仓。

3. 形态。论文能对上 `task`、`verifier`、`agent`。公开页没有可下载的 `dataset`。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。暂不宜接。20 个任务、来源网址、重建脚本、质量清单和参考报告都没有公开下载地址。清单没有给出 `task.toml` 或 `dataset.toml`。

5. 环境。PDF 抽取文本里没有 Dockerfile、镜像或容器运行时。脚注写评测时关闭 web search，源文档在本地提供。按论文去抓 source URL 做重建，那一步要出网。评测时 agent 是否还能另走出网，正文只明确写了关闭 web search。GPU、Kubernetes、多容器都没写，记 unknown。

6. 评分。要另调模型。PDF §4.1 写每份报告由 GPT-5.1 按每条 criterion 打 1–5 分。§4.3 的图按 caption 相似度配对后，由 GPT-5.1 对 readability、groundedness、utility、reproducibility 打分。§2.3 用 GPT-5 判断 claim 是否被源文档支持。脚注写另用 Claude-4.5-Sonnet 对 100 个 OpenHands 任务做了对照重打分。没有看到确定性脚本打分。

7. agent/runtime。论文评测的 coding agent 是 OpenHands（Wang et al., 2025），并与不用该 agent 的直接生成对比。OpenHands 的安装方式、步数上限和是否在容器里跑，本篇公开页没有写，记 unknown。

8. 迁入代价。高。计分用的任务包没有公开网址。评分仍是 1–5 的模型打分。伦理声明写美国政府域名任务称将立即提供，其余要等法律审查，本次没有找到对应下载。

9. 对抽象的压力。`dataset` 接不上：正文不发布，重建材料的地址也没公开。`verifier` 由 GPT-5.1 按条目打 1–5，另有 GPT-5 做 groundedness。`agent` 点名 OpenHands，运行时细节是 unknown。没有容器可接成 `environment`。

10. 本地摘录。[`notes/sources/analystbench/MANIFEST.md`](../../notes/sources/analystbench/MANIFEST.md)。
