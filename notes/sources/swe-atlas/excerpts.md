# swe-atlas 摘录

抓取日 2026-09-24 Asia/Shanghai。树：`49e4af3b6c803dd54a1cd60ead703aac25de4e21`。

## README 出网与 judge

来源：https://raw.githubusercontent.com/scaleapi/SWE-Atlas/49e4af3b6c803dd54a1cd60ead703aac25de4e21/README.md

“The SWE Atlas Test Writing (TW) and Refactoring (RF) tasks now run with internet access disabled — agents can reach only an allowlist of select domains (package registries and language toolchains) required to build and run tests.”

“LLM Judge (any OpenAI-compatible endpoint). We use Claude Opus 4.5 as the Judge model for rubric grading.”

Harbor 安装说明是 `git clone --branch v0.18.0`。数据目录：`data/qa`、`data/tw`、`data/rf`。

## 三轨示例命令

- QnA `run_config/qa/opus-4p6_claude-code.sh`：`harbor run -p ./data/qa -a claude-code -m anthropic/claude-opus-4-6 -e modal`。这份脚本没有 `--allow-agent-host`。
- TW `run_config/tw/opus-4p6_claude-code.sh`：同一模型，另有 `--ak disallowed_tools=WebSearch,WebFetch` 和 `--allow-agent-host`。
- RF `run_config/rf/opus-4p6_claude-code.sh`：同上，再加 `--ek modal_vm_runtime=true`。

## 论文评估句

来源：https://arxiv.org/html/2605.08366v1 第 2.1 节。

- QnA：rubric 全是 must-have，全部通过才算过。
- Test Writing：manifest 用 LLM judge；mutation 是程序化 no-op；rubric 用 judge LLM。通过条件是 manifest、mutation 和全部必须 rubric。
- Refactoring：回归测试是程序化的；rubric 用 judge LLM。通过条件是行为保持和全部必须 rubric。

## 浅克隆计数

`/tmp` 浅克隆上：qa 124 个 `task.toml` 都没有 `network_mode`、都 `gpus = 0`、都有 `EVAL_MODEL`；tw 90 个都是 allowlist 且 `gpus = 0`；rf 70 个都是 allowlist，都没有 `gpus` 键。三轨 compose 文件数 0。
