# MANIFEST

- slug: vision2web
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://github.com/zai-org/Vision2Web

## 官方仓

- 核实到的官方仓: https://github.com/zai-org/Vision2Web
- 默认分支: main
- commit SHA: 577f9397b3db8fc6d828adde254a830caa65d515
- 核实: `git ls-remote` HEAD 与 commits API 一致。message 为 “fix call_vlm async”，committer 日期 2026-08-05T08:59:56Z。
- GitHub API `size`: 4082 KB。该 SHA 的递归 git tree 未截断，43 个 blob，合计 5,067,606 字节。体积主要来自 `docs/images/`。
- GitHub `license` 字段为空。该 SHA 的 README「License」写 CC-BY-NC-SA-4.0，并写仅供学术研究。
- 评测代码在仓内：`docker/Dockerfile.sandbox`、`vision2web/core/sandbox.py`、`vision2web/evaluation/`、`vision2web/inference/adapters/`（claude_code、codex、openhands）。题目数据不在这个 git 里。

## 论文 / blog / HF

- 论文: arXiv [2603.26648](https://arxiv.org/abs/2603.26648)，“Vision2Web: A Hierarchical Benchmark for Visual Website Development with Agent Verification”。
- 项目页: https://vision2web-bench.github.io/
- README 新闻写 2026.04.30 被 ICML 2026 接收为 Spotlight。没有单独的产品 blog URL。
- HF 数据集 id: `zai-org/Vision2Web`。API `sha` `8f03299d92b9bd852e93852d0c21e8a4848ab661`，`lastModified` 2026-03-30T04:14:38.000Z，卡片 `license: apache-2.0`，`gated` false。
- 该 HF 修订的 tree 有 27 个文件，合计 4,113,600,887 字节。三个压缩包：`archives/frontend.tar.gz` 2,633.5 MB，`archives/website.tar.gz` 1,043.5 MB，`archives/webpage.tar.gz` 431.2 MB。
- 同一张 HF 卡片的 YAML 还列了 `webpage/test.parquet`、`frontend/test.parquet`、`website/test.parquet`。这次拉到的 27 文件树里是 `archives/*.tar.gz`，没有这三个 parquet 路径。卡片日期早于代码仓 HEAD。
- 提交榜: `zai-org/Vision2Web-Leaderboard`（API 只有 2 个 sibling：`.gitattributes` 与 README）。

## 测什么

测多模态编程智能体能否按 UI 原型和文字需求做出静态网页、交互式多页前端和全栈网站。出处: 该 SHA 的 README 首段，以及 arXiv:2603.26648 摘要（193 题、16 类、918 张原型图、1,255 个测试用例）。README 统计与摘要一致：webpage 100、frontend 66、website 27。

## 环境线索

- 容器: 有。`docker/build.sh` 构建 `vision2web-sandbox:latest`。`docker/Dockerfile.sandbox` 基于 `ubuntu:22.04`，在同一镜像里安装 PostgreSQL、Redis、nginx、SQLite、Node 20、Playwright/Chrome，以及 Claude Code、Codex、OpenHands。
- 出网: 构建镜像时要拉 apt、npm 和 Chrome 安装包。评测要打功能测试模型和视觉 judge 的 API（`scripts/run_evaluation.sh` 的 `--functional-*` 与 `--visual-*`）。数据集在 HF。`sandbox.py` 的 `docker create` 没有 `--network none`，并会把 proxy 环境变量传进容器。
- GPU: Dockerfile 与 `docker create` 参数里没有 CUDA 或 `--gpus`。沙箱本身未见 GPU。被测模型和 judge 走 HTTP API。
- K8s: 该 SHA 的文件名里没有 kubernetes、helm 或 k8s。unknown。
- 多容器: 没有 docker-compose。每个 workspace 一个容器（`docker create … sleep infinity`）。`run_evaluation.sh` 默认 `MAX_WORKERS=1`，参数可以加大，从而同时开多个同镜像容器。Postgres、Redis、nginx 装在这个镜像里面，不是旁路容器。

## 评分

要另外的模型，不是确定性打分。README Step 4：功能分由 Claude Code 会话用 `playwright-cli` 按 `workflow.json` 跑，记录 Pass/Fail/Blocked；视觉分由 VLM judge 比较原型图和运行中截图。官方榜由维护者用当时的 VLM Judge 和 GUI Agent 重评，提交方只交推理产物。论文的利益声明写评测里的 GUI agent verifier 用的是 GLM-4.6V。该 SHA 的 README 新闻（2026.06.15）写功能测试改为 Claude Code + `playwright-cli`。两处说法都保留。

## agent / runtime

有证据。被测对象是 coding agent。`scripts/run_inference.sh` 的 README 参数 `--framework` 取 `claude_code`、`codex` 或 `openhands`，跑在上面的 sandbox 里。功能测试本身也是一轮 Claude Code。单题默认超时 7200 秒。

## 体积与是否入 git

- 代码仓 blob 合计 5,067,606 字节，超过 5 MB，没有克隆进 `/workspace`。
- HF 三个 tar.gz 约 4.1 GB，没有下载。
- 本目录只有 MANIFEST 和短摘录。本次没有 git commit。

## 未抓取项与原因

- `archives/*.tar.gz`：超过 5 MB，且是题目资源而不是说明文本。
- 论文 PDF 与项目页全文：摘要和 README 已核对，没有存页面副本。
- HF 卡片许可证 apache-2.0 与代码仓 README 的 CC-BY-NC-SA-4.0 不一致，没有改成单一结论。
- 论文里的 GLM-4.6V verifier 与当前 README 的 Claude Code verifier 没有合并成一个实现描述。
- 卡片 YAML 里的 parquet 路径没有在这次 tree 里出现，没有再猜文件名去下。

MANIFEST-END
