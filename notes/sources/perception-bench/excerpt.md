# excerpt: perception-bench

来源 commit `ba032c06e9b6ee3679171ff6ba643b7a0cfebe2e`，默认分支 `master`。

`README.md` Abstract: “PerceptionBench, a benchmark specifically designed to evaluate the atomic visual perception capabilities of Multimodal Large Language Models (MLLMs).” Dataset Statistics: “3,000 verified questions across the ten atomic perceptual capabilities.”

`README.md` Leaderboard: “All questions are open-ended with short, uniquely determined answers; GPT-oss-120B judges each response against the reference (agreement with human judgment: 99.7% on a 300-sample audit).”

`README.md` 配置表: `JUDGE_MODEL` 默认 `gpt-oss-120b`；`DATASET` 默认 `PerceptionBench.jsonl`。该文件不在 git 工作树中。HF 上同名文件约 1626.80 MB。

`eval/eval.py` 模块说明: “free-form predictions, judged 0/1 by an LLM (general_qa)”。judge 请求使用 `temperature=0.3`。`eval/judge_prompt.txt` 要求输出以 `[reason]` 与 `[judge]` 两段结束，verdict 为 True 或 False。

Blog 链接在 README 为 https://www.kimi.com/blog/perception-bench ；抓取日 HEAD 落到 https://www.kimi.ai/blog/perception-bench 。
