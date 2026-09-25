# officeqa-pro-v2

- slug：`officeqa-pro-v2`
- 抓取日：2026-09-24 Asia/Shanghai
- 入口 URL：https://huggingface.co/datasets/databricks/officeqa-pro-v2
- 官方仓 URL 与 commit SHA：
  - 数据集 git：https://huggingface.co/datasets/databricks/officeqa-pro-v2 。Hub API `sha` 为 `65a2b315780417bc50d7bfe6e5bdb904e63fda65`，`lastModified` 2026-08-06，`gated` 为 `auto`，`pretty_name` 为 OfficeQA Pro v2，许可 CC-BY-SA-4.0。未登录 `git ls-remote` 被要求账号，没有再用 git 核对这个 SHA。
  - 没有单独的 Pro v2 代码仓。评分脚本在 https://github.com/databricks/officeqa 的 `reward.py`，HEAD `7b9a3c154ef9fb40215bb67934afc43e6799de16`。该 commit 信息是 `Merge pull request #53 from databricks/readme-officeqa-suite-pro-v2`。HF 树上另有 `render_officeqa_json_simple.py`，属于数据集仓，不在 GitHub 那 17 个文件里。
- 论文 / blog / HF id：
  - HF：`databricks/officeqa-pro-v2`。题文件 `officeqa_pro_v2.csv`，90 题。
  - Blog：https://www.databricks.com/blog/introducing-officeqa-pro-v2-new-benchmark-enterprise-grounded-reasoning 。相关竞赛记录：https://www.databricks.com/blog/evaluating-ai-agents-live-grounded-reasoning-cup 。
  - 卡片引用的技术报告仍是 Pro 的 https://arxiv.org/abs/2603.08655 。没有看到单独的 Pro v2 arXiv id。卡片自带 bib 是 `@dataset{officeqa_pro_v2, ... year = {2026}}`。
- 一句话测什么：测 agent 能否在 1793–2024 年美国联邦收支账的 1,435 份 PDF 上做跨文档数值推理，并作为 OfficeQA Pro 之外的一份新语料。出处：HF 卡片与上述 Pro v2 博客。
- 环境线索：
  - 容器：unknown。GitHub 代码树没有 Dockerfile。数据集卡片没有容器说明。
  - 出网：README @ `7b9a3c15` 写 Pro v2 的已发表 agent harness 与 Pro 相同，包含 web search、文件搜索和代码执行。只读本地解析 JSON 时，卡片没有把出网写成必选项。
  - GPU：unknown。
  - K8s：unknown。
  - 多容器：unknown。
- 评分：确定性程序，不另调 judge 模型。与 Pro 共用 `reward.py`。卡片写它会规范化货币符号、千分位、会计负号、单位和百分号，标签类答案再退到文本重叠。返回 1.0 或 0.0，`tolerance` 可调。
- agent / runtime 线索：README 写已发表的 v2 harness 结果使用 Claude Agent SDK、Codex SDK、Gemini / Antigravity CLI 这一套，并打开 file search、web search、code execution。这套循环的代码不在 GitHub 该 commit 里，也不在已读到的 HF 卡片文件列表里。
- 体积与是否入 git：
  - Hub API `usedStorage` 14,131,884,104 字节。卡片写总大小 14.1 GB，PDF 约 13.3 GB，解析 JSON 约 794 MB，文件数在 API 里是 2879（含 1,435 个 PDF 与 1,435 个解析 JSON）。
  - 卡片写 90 题只引用其中 249 份文档。即便只下这 249 份，也没有在本次拉取，且不宜留在 `/workspace`。
  - 数据集与 PDF 都不进本仓库 git。本目录只留 `MANIFEST.md` 与 `excerpt-card.txt`。
- 未抓取项与原因：
  - `officeqa_pro_v2.csv`、`pdfs/`、`parsed_corpus/jsons/`、`render_officeqa_json_simple.py`：gated，且总体积远大于 5MB。
  - 未登录不能列出每个文件的字节数，API 的 `siblings[].size` 为空，体积用 `usedStorage` 和卡片数字。
  - Pro 的财政部公报语料在另一个 HF 仓 `databricks/officeqa`，本 slug 不收。

同目录摘录：`excerpt-card.txt`。

MANIFEST-END
