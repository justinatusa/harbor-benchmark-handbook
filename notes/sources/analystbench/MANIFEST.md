# analystbench

- slug：`analystbench`
- 抓取日：2026-09-24 Asia/Shanghai
- 入口 URL：https://aclanthology.org/2026.findings-acl.1197/
- 官方仓 URL 与 commit SHA：没有。Anthology 页和 PDF 都没有给出代码或数据仓地址。GitHub 仓库搜索 `AnalystBench` 只命中 https://github.com/wsjq5477/AnalystBench （HEAD `7e3eed05a2a98dee39d3229fcc913918f36a7533`，2026-09-02）。该仓 README 是中文自托管评测平台，未见本篇 ACL 作者或 anthology 链接，不记为官方仓。
- 论文 / blog / HF id：ACL Findings 2026，DOI `10.18653/v1/2026.findings-acl.1197`，页码 23894–23926。Bib：https://aclanthology.org/2026.findings-acl.1197.bib 。PDF：https://aclanthology.org/2026.findings-acl.1197.pdf 。作者 Chau Minh Pham 等。未见 Hugging Face dataset id，未见单独 blog URL。
- 一句话测什么：测 LLM 和 coding agent 能否在多模态文档集合上写出长篇专业报告，并用专家校验过的质量清单和 groundedness 打分。出处：https://aclanthology.org/2026.findings-acl.1197/ 摘要。
- 环境线索：
  - 容器：unknown。PDF 抽取文本里没有 Dockerfile、镜像或容器运行时。
  - 出网：论文脚注写评测时关闭 web search，源文档在本地提供。重建输入要按论文去抓 source URL，那一步需要出网。评测时 agent 是否还能另走出网：正文只明确写了关闭 web search。
  - GPU：unknown。
  - K8s：unknown。
  - 多容器：unknown。
- 评分：要另外的 judge 模型。PDF §4.1 写每份报告由 GPT-5.1 按每条 criterion 打 1–5 分。§4.3 的图也由 GPT-5.1 打分。§2.3 用 GPT-5 判断 claim 是否被源文档支持。脚注写另用 Claude-4.5-Sonnet 对 100 个 OpenHands 任务做了对照重打分。没有看到确定性脚本打分。
- agent / runtime 线索：论文评测的 coding agent 是 OpenHands（Wang et al., 2025），并与不使用该 agent 的 vanilla generation 对比。OpenHands 的安装方式、步数上限和是否在容器里跑：本篇公开页没有写，记 unknown。
- 体积与是否入 git：公开入口是网页和一篇 ACL PDF。本次没有把 PDF 放进本仓库。本目录只有 `MANIFEST.md` 和 `excerpt-eval.txt`，两份都是小文本，可以进 git。上游重建脚本和文档正文不在本目录，也不进 git。
- 未抓取项与原因：
  - 20 个任务、五组 evergreen 变体、URL 列表、重建脚本：论文说会发 URL 和重建脚本、不发抓取正文，但公开页没有给出这些文件的地址。美国政府域名任务称将立即提供，其余要等法律审查。本次没有找到对应下载。
  - checklist、参考报告、源文档：不在 anthology 页上。
  - `wsjq5477/AnalystBench`：名称相撞，内容对不上这篇论文，未克隆。GitHub API 报的仓大小是 4528 KB。
  - 作者主页 https://chtmp223.github.io/ 本次检索没有带出本基准的代码链接。

同目录摘录：`excerpt-eval.txt`。

MANIFEST-END
