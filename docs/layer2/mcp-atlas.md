# MCP-Atlas

公开子集 500 题。另外 500 题是私有的，不在公开数据集里。每个 claim 还要另调 judge。

1. 一句话测什么。测智能体能否在真实 Model Context Protocol（MCP）server 上自己选定工具并完成多步任务。提示不点名 server 或工具。论文写全量 1,000 题、36 个 server。工具数量 README 写 307，论文摘要写 220，两数都保留。

2. 官方源。https://github.com/scaleapi/mcp-atlas ，`main` HEAD `f24ba3fb0bfa484c86acb28431fad6d7282455f9`（2026-08-03）。论文 https://arxiv.org/abs/2602.00933 。数据集 https://huggingface.co/datasets/ScaleAI/MCP-Atlas ，修订 `8c563b55d7c967755f474299848049834d624617`。

3. 形态。`dataset`、`environment`、`verifier`、`agent`。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。评分要 judge 模型。清单没有给出 `task.toml` 或 `dataset.toml`。默认一个沙箱镜像。再起多个沙箱只是可选扩容。

5. 环境。预构建镜像 `ghcr.io/scaleapi/mcp-atlas:1.2.7`，本地 tag `agent-environment:latest`。Dockerfile 在 `services/agent-environment/Dockerfile`。一个沙箱里跑 36 个 MCP server，`make run-docker` 把容器 1984 端口映到本机。20 个 server 无密钥，11 个要接口密钥，5 个要密钥加数据。真实 server 会访问外部接口。沙箱未见 GPU。该 commit 的文件名里没有 Kubernetes 清单。TypeScript harness 默认是宿主机进程，端口 3001。

6. 评分。`services/scoring/score_claims.py` 文件头写 “LLM-as-judge”（large language model 作评判）。默认 `gemini/gemini-3.1-pro-preview`，参数 `--evaluator-model`，否则读 `EVAL_LLM_MODEL`。每个 claim 打分后取覆盖率，输出含 0.50 与 0.75 两档通过率。

7. agent/runtime。`services/agent-harness/` 是 TypeScript 多轮循环。`run_eval.py` 把数据集或本地表格打到 harness 的 `/v2/mcp_eval/run_agent`。README 默认 `--max-turns 256`、`--max-tool-calls 100`、`--concurrency 5`、`--timeout 1800`。同一任务的全部工具调用必须打到同一个沙箱。

8. 迁入代价。高。要拉起带 36 个真实 MCP server 的沙箱，其中一部分要外部密钥，评分再调一个 judge。私有 500 题不在公开集里。

9. 对抽象的压力。`environment` 要求同一任务的工具调用固定在同一个沙箱，`agent` 循环在宿主机进程里。`verifier` 由另一个模型给 claim 打覆盖率，有两档通过率。

10. 本地摘录。[`notes/sources/mcp-atlas/MANIFEST.md`](../../notes/sources/mcp-atlas/MANIFEST.md)。
