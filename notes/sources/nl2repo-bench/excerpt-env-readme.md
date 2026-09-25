来源：https://github.com/EnvCommons/NL2RepoBench/blob/61d26cc0abd084ece8f5d805dcbd3f806a291f15/README.md
抓取：2026-09-24。这是环境封装仓，不是论文项目页仓。论文项目页仓是 multimodal-art-projection/NL2RepoBench。

Compute Requirements:
  Each task runs in its own sandbox container (1 CPU / 2 GB RAM).
  Network access is enabled for dependency installation.

Tasks:
  test split: 103 tasks.
  arxiv-mcp-server excluded because no pre-built Docker image on GHCR.

Reward:
  Reward = min(passed_tests / total_tests, 1.0)
  No LLM grader — purely execution-based against the original repository's pytest suite.
  During evaluation, the agent's package configuration files and test files are replaced with the originals.

Images: ghcr.io/multimodal-art-projection/nl2repobench/
Tools named in this README: bash, submit.
