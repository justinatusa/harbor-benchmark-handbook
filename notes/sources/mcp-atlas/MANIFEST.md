# mcp-atlas

- slug: `mcp-atlas`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://github.com/scaleapi/mcp-atlas

## 官方仓

- 有。https://github.com/scaleapi/mcp-atlas
- 默认分支 `main` HEAD: `f24ba3fb0bfa484c86acb28431fad6d7282455f9`
- 核实: `git ls-remote` HEAD 与 commits API 一致。该 commit 的 committer 日期是 2026-08-03，message 为 “Bump starlette from 0.46.2 to 1.0.1 in /services/agent-environment (#38)”。仓库 API 的 `pushed_at` 是 2026-09-19，但默认分支 tip 仍是上面的 SHA。
- 许可证: MIT。GitHub `size` 字段 17,262 KB。该 SHA 的递归 git tree 未截断，102 个条目，blob 合计 2,875,509 字节。未克隆到 `/workspace`（GitHub 报告的仓体积大于 5 MB）。

## 论文 / blog / HF

- 论文: arXiv [2602.00933](https://arxiv.org/abs/2602.00933)，“MCP-Atlas: A Large-Scale Benchmark for Tool-Use Competency with Real MCP Servers”。
- 排行榜: https://labs.scale.com/leaderboard/mcp_atlas （README 写的是 https://scale.com/leaderboard/mcp_atlas）。
- HF: [ScaleAI/MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas)，API `sha` `8c563b55d7c967755f474299848049834d624617`，`gated` 为 false，许可证卡片写 CC-BY-4.0。
- 没有单独的产品 blog URL；入口就是 GitHub 仓。

## 测什么

测智能体能否在真实 MCP server 上自己选定工具并完成多步任务；公开子集 500 题，提示不点名 server 或工具。出处: 仓库 README @ 上述 SHA 的首段，以及 HF README（“500 sample tasks … 36 real MCP servers”）。论文摘要写全量 1,000 题、公开/私有各 500，36 个 server、220 个工具（https://arxiv.org/html/2602.00933）。同一 README 又写 gist 列出 36 个 server 和 307 个工具。220 与 307 的差异保留，不在这里裁成一个数。

## 环境线索

- 容器: 有。Makefile `VERSION = 1.2.7`，预构建镜像 `ghcr.io/scaleapi/mcp-atlas:1.2.7`，本地 tag 为 `agent-environment:latest`。Dockerfile 在 `services/agent-environment/Dockerfile`，基础镜像 `ghcr.io/astral-sh/uv:python3.12-bookworm-slim`，构建时安装 Node 20 和 MCP 包。`make run-docker` 把容器 1984 端口映到本机。
- 出网: 需要。20 个 server 无 key；11 个要 API key；5 个要 key 加数据（README 指向 `data_exports/README.md`）。key 从 `.env` 注入，镜像不烘焙密钥。真实 server 会访问外部 API。
- GPU: 沙箱镜像未见 GPU。被测模型和 judge 走 OpenAI 兼容 HTTP（README 提到可指向自建 vLLM/TGI，那是模型服务，不是这个沙箱的要求）。
- K8s: 该 SHA 的文件名里没有 kubernetes、helm 或 k8s。CHANGELOG 写 Scale 内部用 Modal 做按任务沙箱，该 proxy 不在公开发布里。
- 多容器: 可选。一个沙箱镜像里跑 36 个 MCP server；TypeScript harness 默认是宿主机进程（端口 3001），不是第二个容器。README 的扩容示例是再起多个 `docker run` 沙箱，每个任务的全部 tool call 必须打到同一个沙箱。

## 评分

要另外的 judge 模型。`services/scoring/score_claims.py` 文件头写 “LLM-as-judge”，默认 `gemini/gemini-3.1-pro-preview`（参数 `--evaluator-model`，否则读 `EVAL_LLM_MODEL`）。README: 每个 claim 打分后取覆盖率；输出含 0.50 与 0.75 两档 pass rate。诊断脚本 `services/diagnostics/single_model_diagnostic.py` 会再调模型，但是失败分类，不是主分。

## agent / runtime

证据在仓内。`services/agent-harness/` 是 TypeScript 多轮循环，CHANGELOG 写 v2.0.0 从 Python harness 换过来。`run_eval.py` 把 HF 数据集（或本地 CSV）打到 harness 的 `/v2/mcp_eval/run_agent`。README 默认 `--max-turns 256`、`--max-tool-calls 100`、`--concurrency 5`、`--timeout 1800`。`.gitmodules` 列出 8 个 MCP 相关 submodule；Dockerfile 改为按 `/data/repos/git_submodule_info.csv` 在构建时 clone 并 checkout。这些 submodule 本次没有单独克隆。

## 体积与是否入 git

- 不要把整个 mcp-atlas 克隆或 HF parquet 放进本仓库。`MCP-Atlas.parquet` API 大小 15,638,757 字节。
- 仓内 blob 约 2.9 MB，其中 `data_exports/` 1,692,439 字节、`assets/` 571,240 字节（README 链到 `assets/MCP_Atlas.pdf`）。这些没有抄进本目录。
- 本目录只有 MANIFEST 和短摘录，可以进 git。`env.template` 里是空的 key 名，没有写入任何密钥值。

## 未抓取项与原因

- 未克隆仓库，也未 `git submodule update`。GitHub `size` 大于 5 MB，且 submodule 会再拉外部仓。
- 未下载 `MCP-Atlas.parquet` 和论文 PDF。
- 私有 500 题不在公开 HF 集里，无法抓取。
- 排行榜页面只作检索对照，未存全文。

MANIFEST-END
