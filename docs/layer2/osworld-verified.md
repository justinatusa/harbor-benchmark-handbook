# OSWorld-Verified

博客把数据与代码指到 OSWorld 本仓。没有单独的 OSWorld-Verified 仓库，也没有同名 tag。

1. 一句话测什么。在真实桌面里评测多模态智能体完成开放式图形界面任务。OSWorld-Verified 是这套任务上的基础设施和评分修复。`evaluation_examples/test_all.json` 在该 commit 有 10 个域、369 条任务编号。出处是博客 https://xlang.ai/blog/osworld-verified 与 arXiv 2404.07972。

2. 官方源。https://github.com/xlang-ai/OSWorld ，`main` HEAD `b138d348256078fa634fc3b73567a7337c793e6b`（2026-09-14）。博客 https://xlang.ai/blog/osworld-verified 。原论文 https://arxiv.org/abs/2404.07972 。虚拟机镜像在 Hugging Face `xlangai/ubuntu_osworld`，修订 `a5d9c3eaae98eebf6e3a0beb84e7e47cf72ae133`。

3. 形态。`task`、`environment`、`verifier`、`agent`。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。环境是图形桌面，并且可以并行多个环境。清单没有给出 `task.toml` 或 `dataset.toml`。

5. 环境。Docker provider 使用镜像 `happysixd/osworld-docker`。有 `/dev/kvm` 时把 KVM 设备传进容器，否则设 `KVM=N`。容器里是 QEMU 虚拟机。Ubuntu 磁盘来自 `xlangai/ubuntu_osworld` 的 `Ubuntu.qcow2.zip`。任务会打开真实网站，首次运行还要下载虚拟机快照。视觉基线示例是接口模型加截图。`desktop_env/providers/pyromind/provider.py` 创建沙箱时写 `gpu: 0`。Kubernetes 只有可选的 pyromind 路径，仓库树里没有自带的 Helm chart。`scripts/python/run_multienv.py --provider_name docker --num_envs 10` 会并行多个环境。另有 `monitor/docker-compose.yml`。

6. 评分。每题配置带 evaluator。`desktop_env/evaluators/` 用 getters 取虚拟机状态，用 metrics 做表、文档、幻灯片、浏览器等比对。对该目录 29 个小文本文件检索 judge 相关词，两处命中都在注释里。博客描述的模糊匹配、感知哈希和文档比较仍是程序规则。

7. agent/runtime。`mm_agents/` 放 agent。入口是 `run.py`，以及 `scripts/python/run_multienv.py`。README 示例是 `--observation_type screenshot`、`--model gpt-4o`、`--max_steps 15`、动作空间 `pyautogui`。公开榜要把 agent 接到这套接口，由维护者在他们的 AWS 上跑。

8. 迁入代价。高。Ubuntu 压缩磁盘约 12.3 GB，环境是整台图形桌面，还要出网。并行评测会再起多台环境。

9. 对抽象的压力。`environment` 是容器里的桌面虚拟机，观察靠截图，动作靠 `pyautogui`。`verifier` 读的是虚拟机终态。评测还可以同时开多台环境。

10. 本地摘录。私有摘录未随公开手册发布。
