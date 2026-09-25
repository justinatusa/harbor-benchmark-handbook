# MANIFEST

- slug: programbench
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://github.com/facebookresearch/programbench

## 官方仓

- 核实到的官方仓: https://github.com/facebookresearch/ProgramBench
- 注意路径大小写：API 返回的全名是 `facebookresearch/ProgramBench`，入口 URL 使用小写 `programbench`，指向同一仓库
- 默认分支: main
- commit SHA: b08d8621031f5f5abc4d3ffc2950256c83fbfe42
- commit 说明: Pin pytest rerun version
- committer 日期: 2026-09-08T20:34:49Z
- 仓库 pushed_at: 2026-09-18T23:23:47Z（晚于该 commit；本清单只钉 main）
- GitHub API `size`: 4202 KB
- license: MIT
- 首页: https://programbench.com
- 包版本见 `pyproject.toml`：`programbench` 1.2.4，Python `>=3.10`

## 论文 / blog / HF

- 论文: https://arxiv.org/abs/2605.03546
- 站: https://programbench.com/ （任务表 https://programbench.com/tasks/）
- blog: 没有另看到独立 blog；站和 README 即说明
- HF id: `programbench/ProgramBench-Tests`
- HF 修订: de0ddfb637590c7ecb54fa0b5301f6dc7dfbcee5
- HF `lastModified`: 2026-05-06T22:51:25.000Z
- HF `usedStorage`: 16396474170 字节；siblings 2235；license mit
- 提交榜仓被 README 点名：https://github.com/ProgramBench/submissions 。本次没有打开
- mini-swe-agent 基线文档：https://mini-swe-agent.com/latest/usage/programbench/ 。本次没有打开

## 测什么

测语言代理能否只拿到编译好的可执行文件和文档，在看不到源码、不能反编译、推理时不能上网的条件下，自己设计并实现一个行为与原程序一致的代码库。出处：https://programbench.com/ 的 About，以及 arXiv:2605.03546 摘要（200 个任务，从 jq、ripgrep 到 FFmpeg、SQLite、PHP）。

## 环境线索

- 容器: 有。`docs/README.md` 指定 Docker Hub 组织 `programbench` 的 `linux/amd64` 镜像，推理 tag `task_cleanroom_v6`，评测示例 tag `task_v6`。`src/programbench/container.py` 用 `docker run` 起一个长驻容器。论文写基础镜像来自 ubuntu:22.04。
- 出网: 推理容器禁止。`docs/README.md` 写 “The agent MUST NOT have access to internet during inference.” 论文写 no-internet 由不给容器网络来执行。评测机本身要能拉 Docker 镜像，并从 HF 下测试 blob。
- GPU: 论文实验写每题 20 CPU、60GB RAM。`container.py` 只传 `--cpus`，没有 `--gpus`。没有看到题目要求 GPU。
- K8s: 没看到。unknown。
- 多容器: 文档是一题一镜像、评测再起容器。没有看到 compose。多容器：没看到。

## 评分

默认分是确定性行为测试，不另要 judge 模型。站上写候选程序要和原程序比行为，该题全部测试通过才算过；测试由代理驱动的 fuzzing 生成，200 题合计超过 248,000 个行为测试。论文主指标是 % Resolved（全部测试通过且未标为作弊），另有 % Tests Passed 和至少 95% 测试通过的参考。`docs/README.md` 写部分分支和单测因非确定性或缺陷被忽略，最终分要用 `programbench info`。论文里“开放互联网”的消融才用 9 个 LM judge 对轨迹做作弊多数票；那不是默认功能分，默认协议是断网。

## agent / runtime

有证据，但代理不在本仓里实现。论文和 README 的基线是 mini-SWE-agent。`docs/README.md` 写论文基线用类似 SWE-bench 的 mini-swe-agent 框架，并预期基线会进 mini-swe-agent。本仓的 `programbench eval` 只评测已经打好的 `submission.tar.gz`。论文配置是每题最多 1000 步、6 小时。本次没有跑 agent。

## 体积与是否入 git

代码仓 API size 4202 KB，没有克隆进 `/workspace`。HF 测试集约 16396474170 字节，大于 5MB，没有下载。本目录只有本文件和 `excerpt-eval-runtime.md`，可以进 git。本次没有 git commit。

## 未抓取项与原因

- `programbench/ProgramBench-Tests` 的测试归档：约 16.4GB。
- Docker Hub 上的任务镜像：没有拉取。
- https://github.com/ProgramBench/submissions 和 mini-swe-agent 基线文档：只被 README 点名，没有打开。
- 站上 200 行任务表没有逐行抄进本目录。
- 没有运行 `programbench eval`。

MANIFEST-END
