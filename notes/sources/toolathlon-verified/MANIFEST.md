# MANIFEST

- slug: toolathlon-verified
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://github.com/hkust-nlp/Toolathlon

## 官方仓

- 核实到的官方仓: https://github.com/hkust-nlp/Toolathlon
- 默认分支: main
- commit SHA: 9be8d8fe07a497b18ee61e3f2ae694e9797f39eb
- commit 说明: Remove outdated contact email
- committer 日期: 2026-08-06T05:51:28Z
- 仓库 pushed_at: 2026-08-18T18:27:01Z（晚于该 commit；本清单只钉 main）
- GitHub API `size`: 363233 KB
- API license: 没有。该 SHA 上请求 `LICENSE` 为 HTTP 404
- 首页: https://toolathlon.xyz/
- 描述写 [ICLR 2026]。README 写本仓对应 Toolathlon-Verified final release
- `tasks/finalpool` 在该 SHA 有 108 个任务目录
- 另有分支 `toolathlon-sandbox`、`openhands-compatibility`、`toolathlon-verified-tasks` 等。没有逐个打开

## 论文 / blog / HF

- 论文: https://arxiv.org/abs/2510.25726
- 站: https://toolathlon.xyz/introduction
- HF 任务镜像: `hkust-nlp/Toolathlon`
- HF 修订: b5092f978818c6c757a26cc027b3a0e5849392cd
- HF `lastModified`: 2026-08-31T20:33:27.000Z
- HF `usedStorage`: 270712793 字节；`gated`: auto；siblings 1815。数据集卡写这是 verified final release 的 108 题镜像，运行时仍在 GitHub
- 轨迹: `hkust-nlp/Toolathlon-Verified_Trajectories`（另有旧名 `hkust-nlp/Toolathlon-Trajectories`，见 README 新闻）。轨迹集本次没有下载

## 测什么

测语言代理在多种真实软件环境里完成多样、长程的工具调用任务；介绍页写 32 个应用、604 个工具、108 道人工收集或编写的题，并用专用评测脚本验收。出处：https://toolathlon.xyz/introduction ，以及该 commit README 的 Introduction。

## 环境线索

- 容器: 有。README 要求 Docker 或 Podman，每题一个容器。镜像名写为 `docker.io/lockon0927/toolathlon-task-image:1016beta`。根 `Dockerfile` 基于 `ubuntu:22.04`，安装 uv、Node、Docker/Podman 客户端、kubectl、kind、Helm、Playwright。无 Docker 路径见 `README_nodocker.md`，并写明部分题会因此跑不了。
- 出网: 要。README 建议机器能直接访问 Internet。自建还需按 `global_preparation/how2register_accounts.md` 配置外部应用凭据。抽到的 `tasks/finalpool/find-alita-paper/evaluation/main.py` 在评分时调用 arXiv API。
- GPU: 该 `Dockerfile` 没有 CUDA。该 SHA 的树路径里没有 `gpu` 或 `cuda` 文件名。`pyproject.toml` 有 Python 包 `gputil`，不能据此说题目要显卡。任务是否要 GPU：unknown。
- K8s: 有迹象。`deployment/k8s`，`Dockerfile` 安装 kubectl、kind、Helm。有题 `tasks/finalpool/k8s-deployment-cleanup`。`README_nodocker.md` 写没有 Docker/Podman 时不能用 kind 起集群。
- 多容器: 有。每题任务容器之外，`global_preparation/deploy_containers.sh` 部署本地应用。`deployment/` 下有 `canvas`、`poste`、`woocommerce`、`k8s`。

## 评分

官方介绍页写每题由专用评测脚本严格验收，不是另要一个 judge 模型。抽到的 `find-alita-paper` 评测器用 PDF MD5 和正则字段对比 ground truth，失败则 `exit(1)`，脚本里没有调用评判模型。108 个评测器没有逐个读完，不能排除个别题另有模型调用。

## agent / runtime

有。README：默认脚手架基于 openai-agents-python；统一入口用 OpenAI SDK 兼容的 `TOOLATHLON_OPENAI_BASE_URL`。解耦模式可选 `toolathlon_default` 或 `claude_agent_sdk`。`pyproject.toml` 含 `openai-agents==0.0.15`、`claude-agent-sdk`、`mcp`。另有公开评测服务（`EVAL_SERVICE_README.md`）和 `eval_client.py`。本次没有连服务，也没有记下示例命令里的主机或密钥。

## 体积与是否入 git

GitHub 约 363233 KB，HF 任务镜像约 270712793 字节，都大于 5MB，没有留在 `/workspace`。本目录只有本文件和 `excerpt-readme-runtime.md`，可以进 git。本次没有 git commit。

## 未抓取项与原因

- 整仓与 HF 镜像：体积超过 5MB；HF 为 gated auto，没有下文件。
- 轨迹数据集：体积和访问条款都未核，没有下载。
- 外部应用账号、token 和本地部署的应用容器：需要注册，且不是公开文本。
- 公开评测服务：没有连接。
- `openhands-compatibility`、`toolathlon-sandbox` 等分支：只记下名字。
- 除 `find-alita-paper` 外的评测脚本：没有逐个读。
- 没有运行评测。

MANIFEST-END
