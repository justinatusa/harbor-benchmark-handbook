# frontier-finance

- slug: `frontier-finance`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://research.samaya.ai/benchmarks/frontier-finance

## 官方仓

有。评分代码仓 https://github.com/samaya-ai/frontier-finance ，默认分支 `main`，抓取时 HEAD `cd51ad2b14dab298cf11151fb8d28a54613d7074`（2026-09-22T19:42:22Z，`Merge pull request #4 from samaya-ai/dependabot/uv/anyio-4.14.2`）。Apache-2.0。这个仓是 grader，不含被测 agent。

## 论文 / blog / HF

- 论文: arXiv:2608.11683（https://arxiv.org/abs/2608.11683）。抓取的是 arXiv HTML，未下 PDF。
- 基准页: https://research.samaya.ai/benchmarks/frontier-finance
- blog: https://samaya.ai/blog/frontier-finance（页面标题 “Introducing FrontierFinance…”；2026-09-24 打开返回 200）
- HF: `samaya-ai/FrontierFinance`。数据集仓 sha `36afd6dc1cbb2c4512536daf917dc28b1225a720`。card 写 license `cc-by-4.0`。`gated: auto`。

## 一句话测什么

测公开数据上的投资研究全流程：220 条专家开放题、11,543 条带来源标注的二元 rubric，覆盖筛选发现到持仓监控，看长答案满足了多少专家标准。（入口页 “220 public queries…”；论文摘要与第 1 节）

## 环境线索

- 容器: 评分仓文件树 25 个 blob，未见 Dockerfile。题目环境不是现成容器。
- 出网: 要。grader 调 judge API。论文第 6 节的被测设置还要公开网页检索、SEC、行情；附录 D 写 Azure OpenAI、Vertex、Fireworks。
- GPU: 论文写被测模型走托管 API。未见把本地 GPU 写成评测条件。记 unknown。
- K8s: 未见。unknown。
- 多容器: 未见。unknown。

## 评分

要另外的 judge 模型，不是确定性打分。每条 rubric 由多名 LLM 独立打二元分，再多数票。README 与 `eval.example.yaml` 的默认三模型是 `claude-sonnet-4-6`、`gemini-3.1-pro-preview`、`gpt-5.4`。论文第 5 节写同一组：GPT 5.4、Gemini 3.1 Pro、Claude Sonnet 4.6。指标是 Rubric Qualification Rate。

## agent / runtime

公开仓只跑 grader，输入是别人交来的 `system_summaries.json`。论文第 6 节写了三种被测 harness，都限制在公开数据：厂商自带 web search；改编自 https://github.com/vals-ai/finance-agent-v2 的 LangChain 版（工具上限 200 次或 300 秒）；Samaya 内部生产 harness。内部 harness 源码不在这个公开仓。

## 体积与是否入 git

- 评分仓: GitHub `size` 字段 449（单位 KB）。`git/trees` 递归 blob 合计 424,603 bytes，25 个文件。未克隆进 `/workspace`。
- HF: tree API 列出 `frontier_finance_public.jsonl` 4,855,986 bytes，外加 README 与 `.gitattributes`，三文件合计 4,855,986 bytes 量级（JSONL 占 4.62 MiB）。匿名 `resolve` 返回 401：`Access to dataset samaya-ai/FrontierFinance is restricted`。README 写 “public — no login”，与 HF `gated: auto` 不一致。JSONL 正文未下载。
- 入 git: 本目录只留本文件和 `excerpt.md`。JSONL 与仓克隆不放进工作区，不作为本目录入库对象。

## 未抓取项与原因

- `frontier_finance_public.jsonl` 正文：HF 门禁，匿名下载 401。
- Samaya 内部 agent harness 源码：论文描述为生产系统，公开评分仓没有。
- 论文 PDF：只用 arXiv HTML。
- 未安装、未跑 grader。

MANIFEST-END
