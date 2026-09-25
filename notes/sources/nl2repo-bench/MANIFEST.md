# MANIFEST

- slug: nl2repo-bench
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://arxiv.org/abs/2512.12730

## 官方仓

- 论文项目页写出的仓: https://github.com/multimodal-art-projection/NL2RepoBench
- 该仓默认分支 main
- commit SHA: 781a1da1ee41fb8edb0bed22f586d69111610edf
- commit 说明: modify test cases
- committer 日期: 2026-05-13T14:53:11Z
- 仓库 pushed_at: 2026-05-13T15:09:30Z
- GitHub API `size`: 2088 KB
- API license: 没有。EnvCommons README 链到该仓 `LICENSE`，本次没有打开该文件
- `test_files/` 在该 SHA 有 104 个子目录
- 环境封装仓（入口说明：置信度 medium，不是论文项目页）: https://github.com/EnvCommons/NL2RepoBench
- 该封装仓 main SHA: 61d26cc0abd084ece8f5d805dcbd3f806a291f15
- commit 说明: NL2RepoBench
- committer 日期: 2026-03-25T19:14:49Z
- GitHub API `size`: 11 KB
- 封装仓 README 把数据来源指回 multimodal-art-projection/NL2RepoBench，并引用同一篇 arXiv

## 论文 / blog / HF

- 论文: https://arxiv.org/abs/2512.12730 （抓到的 PDF 页眉日期 January 9, 2026；项目页即上面的 GitHub）
- blog: 没有看到
- HF id: 没有看到
- 封装仓另指向 OpenReward: https://openreward.ai/GeneralReasoning/NL2RepoBench 。该页本次没有打开
- 每题镜像名写在封装仓 README：`ghcr.io/multimodal-art-projection/nl2repobench/`

## 测什么

测编码代理能否只拿到一份自然语言需求文档和空工作区，从零做出可安装的 Python 仓库，再用该仓库上游 pytest 的通过率评分。出处：arXiv:2512.12730 摘要，以及论文项目页仓 `readme.md`（104 道从零生成完整仓库的长程题）。

## 环境线索

- 容器: 有。论文写每题一个 Docker 执行环境。项目页 `readme.md` 用 python-on-whales 管容器，并要求本地有 `docker.all-hands.dev/all-hands-ai/openhands:0.56` 与 `docker.all-hands.dev/all-hands-ai/runtime:0.56-nikolaik`；默认运行时镜像带 Python 3.12。封装仓自己的 `Dockerfile` 是 `python:3.11-slim` 上的 HTTP 服务，另写每题使用 GHCR 上的任务镜像。
- 出网: 封装仓 README 写为装依赖而打开网络。项目页 `readme.md` 没有写沙箱出网开关。
- GPU: 论文摘要、两份 README 和封装 `Dockerfile` 都没写 GPU。unknown。
- K8s: 没看到。unknown。
- 多容器: 项目页同时点名 OpenHands 镜像和 runtime 镜像，并用 Docker 跑任务。封装仓写每题一个 sandbox 容器（1 CPU / 2 GB RAM）。没有看到 compose 或 K8s。除这一对 OpenHands 镜像外，多容器细节：unknown。

## 评分

确定性执行分，不另要 judge 模型。论文写评估严格基于执行，对照上游 pytest。封装仓 README 写 Reward = min(passed_tests / total_tests, 1.0)，“No LLM grader”；评分前用原仓的包配置和测试文件换掉代理生成的对应文件。项目页仓在该 SHA 有公开 issue #13，报告 `test_commands.json` 的命令被 `shlex.split` 后不再经过 shell，影响 7/104 题。那是评分实现问题，不是第二个 judge。本次没有复现该 issue。

## agent / runtime

项目页 `readme.md`：当前用 OpenHands headless batch，模型写在 `config.toml`，只支持本地执行。论文实验主框架也是 OpenHands-CodeAct；文中写 Gemini-3-pro 改用 Cursor-CLI，因为 OpenHands 里经常出现 agent-in-a-loop。封装仓 README 对代理只暴露两个工具名：`bash` 和 `submit`，没有再指定代理框架。

## 体积与是否入 git

项目页仓 API size 2088 KB，封装仓 11 KB。两仓都没有克隆进 `/workspace`。GHCR 任务镜像和 OpenHands 镜像没有拉。本目录只有本文件和 `excerpt-env-readme.md`，可以进 git。本次没有 git commit。

## 未抓取项与原因

- 104 个任务镜像与 OpenHands 镜像：不在 git 文本里，且会超过 5MB 上限。
- OpenReward 页面：没有打开。
- 项目页 `LICENSE`：没有打开。
- issue #13 的复现实验：没有跑。
- 封装仓与论文项目页的关系只按双方 README 和用户给出的 medium 置信度记录。104（论文与 `test_files/`）和 103（封装仓去掉 `arxiv-mcp-server`）的差异没有再对目录名单。
- 没有跑评测。

MANIFEST-END
