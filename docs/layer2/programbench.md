# ProgramBench

推理时容器不能上网。默认分看行为测试是否全部通过。开放互联网的消融才用评判模型，清单写那不是默认分。

1. 一句话测什么。测语言代理能否只拿到编译好的可执行文件和文档，在看不到源码、不能反编译、推理时不能上网的条件下，自己实现一个行为与原程序一致的代码库。出处是 https://programbench.com/ 的 About，以及 https://arxiv.org/abs/2605.03546 摘要。摘要写 200 个任务。

2. 官方源。仓库 https://github.com/facebookresearch/ProgramBench ，commit `b08d8621031f5f5abc4d3ffc2950256c83fbfe42`（2026-09-08，说明 “Pin pytest rerun version”）。该仓 `pushed_at` 晚于这个 commit，清单只钉 main 的这个 SHA。论文 https://arxiv.org/abs/2605.03546 。站 https://programbench.com/ 。测试集 https://huggingface.co/datasets/programbench/ProgramBench-Tests ，修订 `de0ddfb637590c7ecb54fa0b5301f6dc7dfbcee5`。

3. 形态。`task`、`environment`、`verifier`、`dataset`、`agent`。代理实现不在本仓。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。200 题和测试公开，默认分是行为测试，不另调模型。没有 Harbor `task.toml`。一题一个容器。`container.py` 的 `docker run` 只传 `--cpus`，没有 `--gpus`。没看到图形桌面，也没看到多容器。接入要新写 task 目录。

5. 环境。Docker Hub 组织 `programbench` 的 `linux/amd64` 镜像。推理 tag `task_cleanroom_v6`，评测示例 tag `task_v6`。`src/programbench/container.py` 用 `docker run` 起一个长驻容器。论文写基础镜像来自 ubuntu:22.04。推理容器禁止出网。评测机要能拉镜像，并从 Hugging Face 下测试。没看到题目要求 GPU。Kubernetes：unknown。多容器：没看到。

6. 评分。默认不另调模型。候选程序和原程序比行为，该题全部测试通过才算过。200 题合计超过 248,000 个行为测试。主指标是全部测试通过且未标为作弊的比例。另有至少 95% 测试通过的参考。部分测试因为结果不稳或缺陷被忽略，最终分用 `programbench info`。论文里开放互联网的消融用 9 个语言模型对轨迹做作弊多数票。默认协议是断网。

7. agent/runtime。代理不在本仓实现。论文和 README 的基线是 mini-SWE-agent。`programbench eval` 只评测已经打好的 `submission.tar.gz`。论文配置是每题最多 1000 步、6 小时。这次没有跑代理。

8. 迁入代价。中。一题一个镜像，默认按行为测试打分。测试集 16396474170 字节。推理必须断网。代理要另接 mini-SWE-agent。没有 Harbor 的 task 目录。

9. 对抽象的压力。压力在 `environment` 和 `agent`。推理容器必须断网，评测机却要拉镜像和测试。`agent` 基线不在本仓。`verifier` 要跑整包行为测试。`dataset` 没有 `dataset.toml`。

10. 本地摘录。私有摘录未随公开手册发布。
