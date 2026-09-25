# MANIFEST

- slug: posttrainbench-v1-1
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://posttrainbench.com/

## 官方仓

- 核实到的官方仓: https://github.com/aisa-group/PostTrainBench
- 首页字段: http://posttrainbench.com/
- 默认分支: main
- commit SHA: 3ed1d32ff1ec1f41282be6f8ebbcec07b19fc3d1
- commit 说明: Merge pull request #70 from aisa-group/readme_trim
- committer 日期: 2026-08-21T11:40:32Z
- `git ls-remote --tags`：没有 tag
- GitHub API `size`: 16122 KB；树 blob 合计 12,620,610 字节，254 个 blob，`truncated=false`，树 SHA 与 HEAD 相同
- 许可证: MIT
- 与 v1.1 的对应关系（没有 tag，不能把网页榜和这个 SHA 说成同一次发布）:
  - https://posttrainbench.com/ 页内标题写 Version 1.1；changelog 写 2026-07-28「Released PostTrainBench v1.1」
  - 上述 main HEAD 晚于该日期，且含 `src/judges/`（contamination、api usage、PostTrainBench lookup、general）以及 `judge_tools/model_identity_check.py`
  - `containers/standard.def` 的 `%labels` 写 `Version v1.1`
- 仓库 `pushed_at` 为 2026-09-24T09:14:43Z，但 main HEAD 的 commit 日期仍是 2026-08-21。同日还存在其他分支（含 `add_harbor_support`、`judge/migrate-to-gpt-5.6-terra`）。本清单只核实 main。

## 论文 / blog / HF

- 网站: https://posttrainbench.com/
- 论文: https://arxiv.org/abs/2603.08640
- README bibtex: `eprint = {2603.08640}`，题为 PostTrainBench: Can LLM Agents Automate LLM Post-Training?
- 网站 bibtex 把同一篇标成 ICML 2026
- 没有单独的 HF 数据集 id。评测脚本通过容器内钉死的 inspect_evals 取任务；模型权重由 `containers/download_hf_cache/` 另下，不在 git 里

## 测什么

测 CLI 代理能否在一块 H100 上、10 小时内把给定基座模型后训练好：每个任务是一个基座加一个下游基准，分数是后训练模型在该基准上的成绩。出处：https://posttrainbench.com/ 首段，以及仓库 README 首段；论文摘要用同一约束（10 hours on one H100 GPU）。

网站写榜分是 4 个基座（Qwen 3 1.7B、Qwen 3 4B、SmolLM3-3B、Gemma 3 4B）乘 7 个基准的加权平均。7 个基准与 `scripts/factors.json` 一致：AIME 2025、Arena Hard Writing、BFCL、GPQA Main、GSM8K、HealthBench、HumanEval。仓内另有 `src/eval/tasks/aime2026/`，不在这份权重文件和网站榜里。

## 环境线索

- 容器: 有。Apptainer 定义，`Bootstrap: docker`，`From: nvidia/cuda:12.9.1-cudnn-devel-ubuntu22.04`。`containers/build_container.sh` 构建；运行用 `apptainer exec --nv` 进入 `.sif`。quick start 写需要 apptainer 和 fuse-overlayfs。
- 出网: 代理提示词写 “Internet access is unrestricted.” `run_task.sh` 的 `apptainer exec` 没有禁网参数，并在评判前 `curl` `https://chatgpt.com/backend-api/codex/models`。构建阶段要 apt、npm，并 `git clone` inspect_evals。
- GPU: `src/commit_utils/single_task.sub` 为 `num_gpus = 1`，`request_gpus`，要求 `NVIDIA H100 80GB HBM3`，内存 131072、16 CPU、磁盘 400G。容器说明要用 `--nv`。
- K8s: 没看到。作业文件是 HTCondor（`executable`、`queue`、`condor_submit`）。README 写目前只支持 HTCondor（`htcondor` 或 `htcondor_mpi-is`）。
- 多容器: 没看到。一个 `.sif` 里跑代理和后续评判。README 写当前目标是内部 HPC 的 HTCondor，并注明正在加 Harbor 支持、链接 PR https://github.com/aisa-group/PostTrainBench/pull/8 。这里只记原话。

## 评分

混合，榜上最终分不是纯确定性。

下游任务分：

- `gsm8k`、`humaneval`、`aime2025`、`gpqamain`、`bfcl` 的 `evaluate.py` 调用 `inspect_ai.eval` 和 `vllm/` 本地模型，从 Inspect 的 metrics 取值。这五个脚本里没有 `JUDGE_MODEL`。GPQA 脚本使用 `scorer=choice()`。inspect_evals 内部计分器本次没有再打开，只记录容器里的 pin `06001a83e6d7c709c2ede0570dce7f1031a0bad8`。
- Arena Hard Writing 与 HealthBench 要另外的 judge 模型。两份 `evaluate.py` 都写 `JUDGE_MODEL = "gpt-5-mini"`，并要求 `OPENAI_API_KEY`。Arena Hard 是与基线回答的双向比较后算胜率。

v1.1 合规审查还要另外的 judge 模型，对象是代理轨迹而不是下游题：

- `src/judges/README.md`：contamination、api-usage、ptb-lookup 用 GPT-5.4（codex CLI）；general judge 用 GPT-5.6 Terra（codex 0.144.5）。
- 同文件写 contamination 与 api-usage 的结论会被下游采用；api 命中时 `scripts/collect.py` 退回基线分。ptb-lookup 与 general 标成归档，但 collect 在它们命中时会报错。
- `judge_tools/model_identity_check.py` 是程序化的模型身份检查，对照 `reference_configs/`。

网站「How a Run Is Scored」与上述结构一致：污染、API、lookup 审查加程序化身份检查，被标出的运行按基座模型计分。

## agent / runtime

有。README 写四个 CLI 脚手架：Claude Code、Codex CLI、Gemini CLI、OpenCode。`agents/` 下还有 cursor_cli、grok_cli、glm5、kimi、qwen 等 `solve.sh`。`src/run_task.sh` 用 `timeout` 包住 `apptainer exec`，在容器里跑 `agent_solve.sh`，时限来自 `num_hours`。提示词要求无人值守，结束时交出 `final_model`。

## 体积与是否入 git

官方仓 GitHub 统计 16122 KB，大于 5MB，没有克隆进 `/workspace`。git 内较大文本包括 `src/eval/tasks/healthbench/evaluation_code/data/healthbench.jsonl`（2,979,738 字节）和若干 Arena-Hard `model_answer` jsonl。Hugging Face 模型缓存不在 git 里，按 README 要另跑 `containers/download_hf_cache/download_hf_cache.sh`，本次没下。本目录只留本文件和一个小于 200KB 的运行摘录，不含 `.env`、`auth.json` 或 API key。本次没有 git commit。

## 未抓取项与原因

- 没有 v1.1 git tag，网页榜是否正好由 3ed1d32 生成无法从 tag 核实。
- inspect_evals 只记录了 pin，没有克隆那个仓库，所以五个 Inspect 任务的内部 scorer 细节未逐行核对。
- HF 权重缓存、`results/`、HTCondor 日志：不在这次看到的 git 树里，或体积不适合留下。
- `example.env` 只核对了变量名（API key、HF token、路径、调度器）。值没有抄。
- 没有提交或运行任何训练作业。

MANIFEST-END
