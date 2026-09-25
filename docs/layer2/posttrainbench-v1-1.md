# PostTrainBench v1.1

网站标题写 Version 1.1，仓库没有 v1.1 标签。下面这个 commit 不能说成榜页面的同一次发布。

1. 一句话测什么。测命令行代理能否在一块 H100 上、10 小时内把给定基座模型后训练完，分数是后训练模型在下游基准上的成绩。出处是 https://posttrainbench.com/ 首段、仓库 README 首段，以及 https://arxiv.org/abs/2603.08640 摘要。

2. 官方源。仓库 https://github.com/aisa-group/PostTrainBench ，commit `3ed1d32ff1ec1f41282be6f8ebbcec07b19fc3d1`（2026-08-21，说明 “Merge pull request #70 from aisa-group/readme_trim”）。网站 https://posttrainbench.com/ 。论文 https://arxiv.org/abs/2603.08640 。没有单独的 Hugging Face 数据集 id。`git ls-remote --tags` 没有 tag。

3. 形态。`task`、`environment`、`verifier`、`agent`。清单没写 `adapter`，也没给出 main 上的 `task.toml` 或 `dataset.toml`。

4. 与 Harbor 距离。重改造。作业文件要求一块 NVIDIA H100 80GB HBM3。Arena Hard Writing、HealthBench，以及污染和接口使用审查，都要另调模型。README 写正在加 Harbor 支持，链接是 https://github.com/aisa-group/PostTrainBench/pull/8 。清单只核实了 main。

5. 环境。容器定义是 Apptainer，`From: nvidia/cuda:12.9.1-cudnn-devel-ubuntu22.04`。运行用 `apptainer exec --nv` 进入 `.sif`。代理提示词写可以上网，评判前还会请求 `https://chatgpt.com/backend-api/codex/models`。调度是 HTCondor，README 写目前只支持 HTCondor。没看到 Kubernetes，也没看到多容器。

6. 评分。榜上最终分不单靠程序比较。`gsm8k`、`humaneval`、`aime2025`、`gpqamain`、`bfcl` 从 Inspect 的 metrics 取值，这五份脚本里没有 `JUDGE_MODEL`。Inspect 内部计分器没逐行打开，只记下 pin `06001a83e6d7c709c2ede0570dce7f1031a0bad8`。Arena Hard Writing 和 HealthBench 的 `JUDGE_MODEL` 是 `gpt-5-mini`。轨迹审查里，contamination 和 api-usage 用 GPT-5.4，general judge 用 GPT-5.6 Terra。`model_identity_check.py` 按 `reference_configs/` 做程序化身份检查。

7. agent/runtime。有。README 写 Claude Code、Codex CLI、Gemini CLI、OpenCode。`agents/` 下还有 cursor_cli、grok_cli、glm5、kimi、qwen 的 `solve.sh`。`src/run_task.sh` 在容器里跑 `agent_solve.sh`，时限来自 `num_hours`。结束时要交出 `final_model`。

8. 迁入代价。高。要一块 H100、Apptainer 和 HTCondor，单次任务窗口是 10 小时。下游分和轨迹审查还要另调模型。清单没有给出 main 上的 Harbor task 目录。

9. 对抽象的压力。`environment` 绑在 Apptainer、指定型号的 GPU 和 HTCondor 上。`verifier` 要接下游分数、轨迹审查和程序化身份检查。`agent` 在容器里跑外部命令行工具，时限按小时计。

10. MANIFEST 路径。`notes/sources/posttrainbench-v1-1/MANIFEST.md`
