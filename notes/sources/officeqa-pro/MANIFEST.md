# officeqa-pro

- slug：`officeqa-pro`
- 抓取日：2026-09-24 Asia/Shanghai
- 入口 URL：https://github.com/databricks/officeqa
- 官方仓 URL 与 commit SHA：
  - 代码仓：https://github.com/databricks/officeqa ，`git ls-remote` HEAD `7b9a3c154ef9fb40215bb67934afc43e6799de16`（2026-08-06，`Merge pull request #53 from databricks/readme-officeqa-suite-pro-v2`）。默认分支 `main`。许可：代码 Apache-2.0。
  - 题目与语料：https://huggingface.co/datasets/databricks/officeqa 。Hub API `sha` 为 `763a8366abf2a3605c381d53586d844dc60fa756`，`lastModified` 2026-07-14，`gated` 为 `auto`，许可 CC-BY-SA-4.0。未登录的 `git ls-remote` 被 Hugging Face 要求账号，没有用 git 再对一次这个 SHA。
- 论文 / blog / HF id：
  - 论文：https://arxiv.org/abs/2603.08655 （HTML：https://arxiv.org/html/2603.08655），题名 OfficeQA Pro: An Enterprise Benchmark for End-to-End Grounded Reasoning。
  - Blog：https://www.databricks.com/blog/introducing-officeqa-benchmark-end-to-end-grounded-reasoning （README 指向的 OfficeQA blog）。
  - HF：`databricks/officeqa`。Pro 题文件名是 `officeqa_pro.csv`（133 题）。同仓还有 `officeqa_full.csv`（246 题），Full 不是本 slug。
- 一句话测什么：测系统能否在 1939–2025 年美国财政部公报上，把分散在表格和正文里的数字找出来并做有依据的推理。出处：README @ `7b9a3c15` 与论文摘要 https://arxiv.org/abs/2603.08655 。
- 环境线索：
  - 容器：unknown。该 commit 的 git tree 有 17 项，没有 Dockerfile 或 compose。论文把 Python REPL 写成 sandboxed，用来挡住对语料的批量扫目录，没有写镜像。
  - 出网：论文的 Web Search Enabled、Oracle PDF + Web Search，以及第 4 节的 Web Search API，都要出网。Prompt Only 设置不用文档也不用工具。语料文件本身在本地。
  - GPU：unknown。
  - K8s：unknown。
  - 多容器：unknown。
- 评分：确定性程序，不另调 judge 模型。`reward.py` 的 `score_answer` 做规范化后的数值容差和文本模糊匹配，返回 1.0 或 0.0。论文写默认报告 0.0% absolute relative error。容差是参数，不是另一个模型。
- agent / runtime 线索：论文第 3 节把 agent baseline 定义成自主工具调用和多步推理的编排。第 4 节工具是 Web Search API、Python REPL、`fs_search` / `fs_read`。README 记录的 harness 结果来自 Claude Agent SDK、Codex SDK、Gemini / Antigravity CLI。这些循环不在本 commit 的代码里。本仓提供的是评分和语料脚本。
- 体积与是否入 git：
  - GitHub API `size` 3728 KB；该 commit 递归 blob 合计 3,267,291 字节，其中三张结果图占了大头。文本文件可以进 git。本次没有把整仓克隆进 `/workspace`。
  - HF `usedStorage` 4,782,637,610 字节，2105 个文件（含 697 个 PDF）。README 另写 PDF 约 4GB、解析 JSON 约 730MB、transformed txt 约 460MB。语料不进本仓库 git。
  - 本目录只留 `MANIFEST.md` 与 `excerpt-readme.txt`。
- 未抓取项与原因：
  - `officeqa_pro.csv` 和财政部公报 PDF / JSON / txt：数据集 `gated: auto`，未登录不能下文件。体积也超过 5MB，即使放开也不会留在 `/workspace`。
  - `reward.py` 全文 28,094 字节，已在 GitHub 上读过行为，没有整文件拷进本目录。
  - Full 的 113 道 easy 题：同一 HF 仓，不属于本 slug 的题目集。

同目录摘录：`excerpt-readme.txt`。

MANIFEST-END
