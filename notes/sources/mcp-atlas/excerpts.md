# mcp-atlas excerpts

抓取日 2026-09-24 Asia/Shanghai。不含 `.env`、不含任务 parquet。

## README @ f24ba3fb0bfa484c86acb28431fad6d7282455f9

> MCP-Atlas evaluates how well AI agents use tools to complete real-world tasks, across 36 Model Context Protocol (MCP) servers in a reproducible Docker sandbox, scored with an LLM-as-judge.

- Paper: https://arxiv.org/abs/2602.00933
- Dataset: https://huggingface.co/datasets/ScaleAI/MCP-Atlas
- 预构建镜像: `ghcr.io/scaleapi/mcp-atlas:1.2.7`
- judge 默认: `gemini/gemini-3.1-pro-preview`（也见于 `services/scoring/score_claims.py` 的默认参数）

## HF README @ 8c563b55d7c967755f474299848049834d624617

公开集是 500 条，字段包括 `TASK`、`ENABLED_TOOLS`、`PROMPT`、`GTFA_CLAIMS`、`TRAJECTORY`。卡片写 36 个 server、220 个工具。与 GitHub README 里 “307 tools” 的 gist 说法并存，摘录不合并这两个数字。

## 工具数冲突的论文侧

arXiv HTML https://arxiv.org/html/2602.00933 摘要: 1,000 个任务、36 个真实 MCP server、220 个工具；公开代码仓为 https://github.com/scaleapi/mcp-atlas。
