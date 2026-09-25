# OSWorld 2.0

代码入口是 OSWorld-V2。tag `osworld-v2.1` 的尖端，和发布清单里的 `base_commit`，是两个提交。

1. 一句话测什么。测电脑使用 agent 能不能做完长程、跨应用的真实工作流。108 条任务，熟练使用者中位约 1.6 小时。主指标是 500 步预算下的二元完成，同时用平均 27.25 个检查点给部分分。出处是项目页与 arXiv:2606.29537 摘要、第 2.1.3 节。

2. 官方源。https://github.com/xlang-ai/OSWorld-V2 。抓取时 `main` 与 tag `osworld-v2.1` 都指向 `3d778a3c9a34a079316f70df023b166700445792`（2026-09-16）。`benchmark_releases/osworld-v2.1.json` 把 `osworld_code.base_commit` 写成 `325ab352e2ff7410854bf8e3324c391bc60e7526`。项目页 https://osworld-v2.xlang.ai/ 。论文 https://arxiv.org/abs/2606.29537 。任务类在 Hugging Face `xlangai/osworld_v2_tasks`，commit `0a1aadad95aa79b00b3783e717d865089ab06e26`，`gated: auto`。

3. 形态。`task`、`environment`、`verifier`、`agent`。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。暂不宜接。任务类和完整资产 gated。要图形桌面，网站应用各自一个容器，总分里还有 judge 模型。清单没有给出 `task.toml` 或 `dataset.toml`。

5. 环境。Docker 运行镜像 `happysixd/osworld-docker@sha256:0e6497a9295647cf05bf2b2af522fdd79bdeba2737595259cab310a3bcf6baa9`。磁盘制品是 `xlangai/v2-image` 的 `osworld-v2-ubuntu-x86.qcow2.zip`，14,891,811,084 字节。发布清单写 Docker 归档已核对，客机启动被缺少 KVM 挡住。任务网站应自托管，并设置 `WEBSITE_HOST_SUFFIX`。部分任务要代理，GitLab 题要自建。GPU 没有写成评测条件，记 unknown。Kubernetes 未见，记 unknown。论文写 OSWorld-web 每个应用一个容器，评测时再起这些容器，这是桌面虚拟机之外的第二组容器。网站源码含 25 个钉死的 submodule。

6. 评分。主路径对最终环境状态和产物做功能检查，这一段是程序判定。论文第 2.1.3 节写 model-based evaluation 占总分 11.53%，单题不超过 50%，judge 提示要在标注过的对错状态上验证后才收。附录 E.1 列出核过的模型，已读材料没有写死线上默认用哪一个。主报告指标仍是 500 步二元完成，部分分是检查点均值。

7. agent/runtime。README 的评测入口是宿主机上的 `scripts/python/run_multienv_*.py` 和 `mm_agents`，观察类型示例是 screenshot。论文第 3 节写 Claude 走 `claude_computer_use`，其他模型发动作。环境是桌面虚拟机。公开榜要求把 agent 实现交给维护者跑。agent 代码在宿主机，题目环境在虚拟机。

8. 迁入代价。高。桌面磁盘约 14.9 GB，网站是另一组容器，任务和完整资产要过 Hugging Face 门禁。约一成分数还要准备 judge。这份清单没有声称 Docker 客机已经启动。

9. 对抽象的压力。`environment` 有两层：桌面虚拟机，以及按应用拆开的网站容器。`verifier` 把程序检查和 judge 混在同一总分里，judge 只覆盖少数检查点。

10. 本地摘录。私有摘录未随公开手册发布。
