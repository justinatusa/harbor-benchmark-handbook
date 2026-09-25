# Toolathlon-Verified

每题一个任务容器还不够。`deploy_containers.sh` 还要再起一批本地应用。108 个评测脚本没有读完。

1. 一句话测什么。测语言代理在多种真实软件环境里完成多样、长程的工具调用。介绍页写 32 个应用、604 个工具、108 道人工收集或编写的题，并用专用评测脚本验收。出处是 https://toolathlon.xyz/introduction ，以及该 commit README 的 Introduction。

2. 官方源。仓库 https://github.com/hkust-nlp/Toolathlon ，commit `9be8d8fe07a497b18ee61e3f2ae694e9797f39eb`（2026-08-06，说明 “Remove outdated contact email”）。该仓 `pushed_at` 晚于这个 commit，清单只钉 main 的这个 SHA。论文 https://arxiv.org/abs/2510.25726 。站 https://toolathlon.xyz/ 。Hugging Face `hkust-nlp/Toolathlon`，修订 `b5092f978818c6c757a26cc027b3a0e5849392cd`。`tasks/finalpool` 在该 commit 有 108 个任务目录。

3. 形态。`task`、`environment`、`verifier`、`agent`、`dataset`。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。清单没有给出 `task.toml` 或 `dataset.toml`。每题任务容器之外，`global_preparation/deploy_containers.sh` 还部署本地应用。这是多容器。

5. 环境。要 Docker 或 Podman，每题一个容器。镜像名 `docker.io/lockon0927/toolathlon-task-image:1016beta`。根 Dockerfile 基于 `ubuntu:22.04`。没有 Docker 或 Podman 时，部分题跑不了。机器要能直接访问互联网。自建还要配置外部应用凭据。抽到的 `tasks/finalpool/find-alita-paper/evaluation/main.py` 在评分时调用 arXiv。GPU：unknown。有 Kubernetes 迹象：`deployment/k8s`，以及题目 `tasks/finalpool/k8s-deployment-cleanup`。多容器：有。`deployment/` 下还有 `canvas`、`poste`、`woocommerce`。

6. 评分。介绍页写每题由专用评测脚本验收。抽到的 `find-alita-paper` 用 PDF 的 MD5 和正则字段对比标准答案，失败则退出，脚本里没有调用评判模型。108 个评测器没有逐个读完，不能排除个别题另有模型调用。

7. agent/runtime。有。默认脚手架基于 openai-agents-python。统一入口用 OpenAI SDK 兼容的 `TOOLATHLON_OPENAI_BASE_URL`。解耦模式可选 `toolathlon_default` 或 `claude_agent_sdk`。另有公开评测服务。这次没有连接服务。

8. 迁入代价。高。一道题要任务容器，还要 canvas、poste、woocommerce 和 Kubernetes 上的本地应用。外部账号不在公开文本里。评测脚本没有读完。

9. 对抽象的压力。压力在 `environment`。任务容器之外还要一组本地应用容器。`verifier` 是每题一份脚本，108 份没读完。`agent` 回路在本仓的 openai-agents 脚手架里。

10. 本地摘录。[`notes/sources/toolathlon-verified/MANIFEST.md`](../../notes/sources/toolathlon-verified/MANIFEST.md)。
