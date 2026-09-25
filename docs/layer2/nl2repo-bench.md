# NL2Repo-Bench

论文项目页和环境封装是两个仓、两个 commit。每题一个容器，分数看上游 pytest。

## 测什么

测编码代理能否只拿到一份自然语言需求文档和空工作区，从零做出可安装的 Python 仓库。

## 官方源

论文 https://arxiv.org/abs/2512.12730 。论文项目页仓 https://github.com/multimodal-art-projection/NL2RepoBench ，commit `781a1da1ee41fb8edb0bed22f586d69111610edf`（2026-05-13）。环境封装仓 https://github.com/EnvCommons/NL2RepoBench ，commit `61d26cc0abd084ece8f5d805dcbd3f806a291f15`（2026-03-25）。两边关系在来源笔记里标成 medium。没有看到博客或 Hugging Face 数据集。封装仓还指向 https://openreward.ai/GeneralReasoning/NL2RepoBench ，该页没有打开。

## 形态

task、environment、verifier、agent、dataset。项目页仓 `test_files/` 有 104 个子目录。没有看到 `task.toml`、`dataset.toml` 或 adapter。

## 与 Harbor 距离

重改造。104 道题在公开仓。分数按上游 pytest 通过率计算，评分不调用 judge 模型。没有 Harbor `task.toml`。`openhands` 镜像是代理进程，runtime 镜像是它拉起的一个沙箱，不是 compose 多容器。GPU 开关在注释里，评测脚本没有写明必须显卡。

## 环境

论文写每题一个 Docker 执行环境。项目页用 python-on-whales 管容器，并要求本地有 `docker.all-hands.dev/all-hands-ai/openhands:0.56` 与 `docker.all-hands.dev/all-hands-ai/runtime:0.56-nikolaik`。默认运行时镜像带 Python 3.12。封装仓自己的 `Dockerfile` 基于 `python:3.11-slim`。每题另用 `ghcr.io/multimodal-art-projection/nl2repobench/` 上的任务镜像，一个沙箱容器，1 CPU、2 GB 内存。封装仓写为装依赖而打开网络。项目页没有写沙箱出网开关。没有看到 compose 或 Kubernetes。GPU 没写。OpenHands 点了代理镜像和运行时镜像各一份。除此之外，多容器细节记 unknown。镜像没有拉取。

## 评分

分数按执行结果计算。论文写对照上游 pytest。封装仓写 Reward = min(passed_tests / total_tests, 1.0)，并写没有用语言模型打分。评分前用原仓的包配置和测试文件换掉代理生成的对应文件。项目页有公开 issue #13。它报告 `test_commands.json` 的命令被 `shlex.split` 后不再经过 shell，影响 7/104 题。本次没有复现。

## agent / runtime

项目页当前用 OpenHands 无头批跑。模型写在 `config.toml`，只支持本地执行。论文实验的主框架也是 OpenHands-CodeAct。文中写 Gemini-3-pro 改用 Cursor-CLI，因为在 OpenHands 里经常陷入来回打转。封装仓对代理只暴露 `bash` 和 `submit`，没有再指定代理框架。

## 迁入代价

中。题目和 pytest 评分都公开，每题一个镜像。接进 Harbor 时要自己把通过率写成 verifier，并在评分前换回上游测试文件。104 个任务镜像还要另拉。issue #13 说明有 7 题的评分命令可能跑偏，本次没复现。

## 对抽象的压力

压在 verifier 和 environment。verifier 要先换回上游测试再跑 pytest，分数是通过率。environment 是每题一个执行镜像。`openhands` 与 runtime 是代理和它的一个沙箱，不是 compose 多服务。当前 agent 绑在 OpenHands 上。评测脚本没有写明必须显卡。

## 本地摘录

见 [`notes/sources/nl2repo-bench/MANIFEST.md`](../../notes/sources/nl2repo-bench/MANIFEST.md)。
