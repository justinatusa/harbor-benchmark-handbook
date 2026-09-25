# MANIFEST

- slug: frontierswe-v2
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://www.frontierswe.com/

## 官方仓

- 核实到的公开 Git 仓: https://github.com/Proximal-Labs/frontier-swe
- 默认分支: main
- commit SHA: 422b9bb95deb8efe436becb0ed3c44be23611e10
- commit 说明: update: fix grok cli list if else bug (#84)
- committer 日期: 2026-08-07T08:18:30Z
- 仓库 pushed_at: 2026-08-13T14:12:48Z
- GitHub API `size`: 512911 KB
- 该 SHA 没有 `LICENSE`（HTTP 404）。API license 为空
- 首页字段: https://frontierswe.com
- 该 SHA 的 `tasks/` 只有 17 个目录。tag `pins/final-run`（8ba3afe785a0f99a78d1017127b97eef60e63b3b，2026-07-13）也是这 17 个名字
- 没有找到包含站上 34 题的公开 commit

## 论文 / blog / HF

- 论文: 没有看到 arXiv
- blog: https://www.frontierswe.com/blog/v2 （页首 September 2026；文末 bibtex 题为 FrontierSWE v2）
- 榜: https://www.frontierswe.com/
- README 还指向 Prime Intellect 环境页 https://app.primeintellect.ai/dashboard/environments/proximal/frontier-swe 。该页本次没有打开
- HF id: 没有看到

## 测什么

测编码代理在超长程技术题上能做多远：站上的 FrontierSWE V2 是 34 道实现、性能、科学计算、视觉推理和 AI 研究题，每题最多 20 小时、5 次试验，验证器给 0 到 1 的部分分，榜上报 mean@5。出处：https://www.frontierswe.com/ 与 https://www.frontierswe.com/blog/v2 开头。公开 Git 的 README 只写超长程技术挑战，没有写 “v2” 或 34。

## 环境线索

- 容器: 公开仓有。17 题都有 `environment/` 与 `docker_image`（`ghcr.io/proximal-labs/frontier-swe/...`）。另有 `docker/first_party_cli/`，含 `cuda12.4.1-ubuntu22.04.Dockerfile`。镜像层没有拉取。
- 出网: 按题。17 份 `task.toml` 里只有 `frogsgame-rl` 和 `pcqm4mv2-autoresearch` 是 `allow_internet = true`，其余为 false。`frogsgame-rl` 注释写训练/推理走 Tinker API，本地 `gpus = 0`。
- GPU: 按题，不是全集。`gpus = 1` 的是 granite-mamba2 与 inference-system-optimization（`B200`），modular-stack-wan21、optimizer-design、pcqm4mv2-autoresearch（`H100`）。其余 12 题 `gpus = 0`。
- K8s: 该 SHA 的树路径没有 k8s 或 kubernetes。unknown。
- 多容器: 每题一个 `docker_image`。树里没有 `docker-compose.yaml`（仅有 git 源码里的 precompose 文件名）。多容器：没看到。
- v2 blog 的作弊复盘写试跑在 Modal 上。公开仓有 `harbor_ext/modal_managed.py`、`modal_exec.py`、`modal_transfer.py`，以及若干 `scripts/seed_modal_volume.py`

## 评分

公开仓里的分数是程序算的，不是另要一个 judge 模型。`SCORING.md` 与 `scripts/score_from_reward.py` 从 `reward.json` 取 correctness 和 speedup，再按 implementation / performance / ml_research 做门控；部分题有部分分。该脚本的任务表只有上述 17 题。`SCORING.md` 写事后审计 `scoring/anticheat.json` 可把一试记 0；这个路径不在该 commit 的树里，审计程序本身没看到。v2 blog 的 34 题 mean@5 与 20 小时预算是站上的协议；对应验证器不在这个 commit。

## agent / runtime

两套线索，不要合成一件事。v2 blog：默认 harness 是 Proximus，博文说它在 mini-swe-agent 上加了 compaction、vision 和 `submit`，每题 20 小时。该 Proximus 源码不在这个 commit。这个 commit 里另有 `harbor_ext/`（claude、codex、gemini、grok、kimi、opencode 等 CLI 文件）和 `pyproject.toml` 可选依赖组 `harbor`（`harbor>=0.2.0`、`modal==1.4.1`）。抽到的 `tasks/frogsgame-rl/job.yaml` 把 environment 指到 `harbor_ext.modal_managed:ManagedModalEnvironment`，agents 指到同目录的 CLI 类。

## 体积与是否入 git

GitHub API size 512911 KB，大于 5MB，没有把克隆留在 `/workspace`。ghcr 镜像没有拉。本目录只有本文件和 `excerpt-public-tasks.txt`，可以进 git。本次没有 git commit。

## 未抓取项与原因

- 站上 34 题里相对这 17 题新增的题目、其 Dockerfile 和验证器：公开 main 与 `pins/final-run` 都没有。
- blog 说已从 v2 退役、但仍在这 17 题里的四题：PCQM4Mv2、Pyright、Revideo、Dependent Type Checker。退役后的题面没有另仓。
- Proximus 源码、`scoring/anticheat.json`、ghcr 镜像、Prime Intellect 环境页：不在已读的公开文本里，或体积不适合留下。
- 没有跑 `score_from_reward.py`。

MANIFEST-END
