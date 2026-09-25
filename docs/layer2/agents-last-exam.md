# Agents' Last Exam

本地 Docker 要下的任务包需要申请，约 202 GiB。代理要做桌面动作，部分题要 GPU，另有一小部分题要评判模型。

1. 一句话测什么。测通用计算机使用代理能否完成长程、结果可核验的专业工作。公开仓 README 写 55 个子领域、13 个行业簇，开放框架约 150 道公开任务。出处是该 README，以及 https://arxiv.org/abs/2606.05405 摘要。网站首页写已收集 1,500+ 题。三处数字不是同一口径。

2. 官方源。仓库 https://github.com/rdi-berkeley/agents-last-exam ，commit `d10fb61a14f9719774c3520c5763068b28ef5546`（2026-09-04，说明 “Merge pull request #21 from rdi-berkeley/feat/antigravity-cli”）。论文 https://arxiv.org/abs/2606.05405 。站 https://agents-last-exam.org/ 。榜 https://agenthle.org/leaderboard 。任务卡 https://huggingface.co/datasets/agents-last-exam/agents-last-exam ，修订 `ea617358e3c2e244d6f4d473c6a6a85d394bf90d`。本地数据包 https://huggingface.co/datasets/agents-last-exam/agents-last-exam-data-archive ，修订 `dedf6556c88f7dfd4fce891f9fa213e66584c71e`，gated 为 manual。

3. 形态。`task`、`environment`、`verifier`、`agent`、`dataset`。清单没写 Harbor 的 `adapter`。

4. 与 Harbor 距离。暂不宜接。本地数据包 gated，约 202 GiB，要先申请。清单没有给出 `task.toml` 或 `dataset.toml`。论文写代理动作包括浏览器、shell 和键鼠，README 写用 MCP 补桌面动作。需要 GPU 的任务用 NVIDIA L4。开源任务树 6.8% 要另调模型。

5. 环境。提供者有 Google Cloud 虚拟机、AWS EC2、阿里云 ECS、QEMU/KVM、本地 Docker，以及已有的计算机使用沙箱。Docker 镜像 `agentslastexam/ale-ubuntu22-docker:latest`，这份配置写明 no-GPU。论文附录写默认机器是 GCP `c4-standard-4`。需要 GPU 的任务（例如三维渲染、仿真）用 `g2-standard-8` 加 NVIDIA L4。默认是每题一台虚拟机或一个容器。沙箱内部出网是否放行：unknown。评测编排不是 Kubernetes。仓里的 helm 和 `k8s_migration_1` 这类题，是题目要装的软件，不是评测平台。`docker.yaml` 写四道题要在沙箱里再跑 Docker，两道要 Apptainer 或 Singularity，这两类应改走 QEMU。

6. 评分。主路径不另调模型。README 写隐藏参考和程序评分，`evaluate()` 分数在 0 到 1，参考答案在代理结束之后才放进环境。论文附录统计开源任务树：93.2% 是代码评分，6.8% 要另调模型，后者主要看画面、截图和短视频。这次没有打开各题 `main.py` 去点名模型。

7. agent/runtime。有。包名 `agent-last-exam`，入口 `ale_run`。被测对象是自带循环的 harness，再用 MCP 补桌面动作。论文写单次运行上限 5 小时。该提交的 `ale_run/agents/` 有 `ale_claw`、`antigravity_cli`、`codex`、`cursor_cli`、`droid`、`forgecode`、`gemini_cli`、`grok_build`、`grok_cli`、`hermes`、`octavus_cli`、`openclaw_cli`、`openhands_cli`、`terminus_2`。有的命令行注进虚拟机，有的在 ALE 进程里通过 MCP 遥控。

8. 迁入代价。高。要桌面动作，部分题要 NVIDIA L4，6.8% 的题要另调模型。本地数据包约 202 GiB，而且要先申请。

9. 对抽象的压力。压力在 `environment` 和 `verifier`。环境要键鼠和桌面，部分题要 GPU。`verifier` 主路径是程序分，6.8% 要在评分里再调模型。`agent` 回路有的在沙箱里，有的在外面。

10. MANIFEST 路径。`notes/sources/agents-last-exam/MANIFEST.md`
