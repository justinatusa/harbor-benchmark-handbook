来源：https://github.com/zapier/AutomationBench/blob/4a8e1061254004d9dac807054eed33fad7d1ff14/README.md
抓取：2026-09-24。只摘评分与范围，不含密钥。

## Principles

- Verifiability - All tasks must be programmatically verifiable.

## Scoring

- partial_credit (0.0 - 1.0) - fraction of assertions satisfied.
- task_completed_correctly (0.0 or 1.0) - 1.0 only if every assertion passes.
  The average of this across scored tasks (simple excluded) is the official AutomationBench pass rate.

Public set: 100 tasks per domain across sales, marketing, operations, support, finance, and HR (600).
simple domain: 200 tasks, not included in the benchmark score.
Official leaderboard uses a separate held-out private set.
CLI: uv run auto-bench; default --max-steps 50; --toolset api|zapier|limited_zapier.
