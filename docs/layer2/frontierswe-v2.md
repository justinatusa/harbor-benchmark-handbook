# FrontierSWE v2

站上的 v2 是 34 题。公开仓里能看到的 `task.toml` 只有 17 份，两份题单不是同一套。

## 测什么

测编码代理在 34 道超长程技术题上能做多远。题型覆盖实现、性能、科学计算、视觉推理和人工智能研究，每题最多 20 小时。

## 官方源

榜页 https://www.frontierswe.com/ 。说明页 https://www.frontierswe.com/blog/v2 。公开仓 https://github.com/Proximal-Labs/frontier-swe ，commit `422b9bb95deb8efe436becb0ed3c44be23611e10`（2026-08-07）。这个 commit 没有许可证文件。没有看到 arXiv，也没有 Hugging Face 数据集。

## 形态

task、environment、verifier、agent。公开仓里 17 题各有一份 `task.toml`。没有看到 `dataset.toml`，也没有看到 adapter。

## 与 Harbor 距离

暂不宜接。站上 34 题和对应验证器不在上述 commit。公开 main 与 tag `pins/final-run` 都只有同名的 17 题。说明页写已从 v2 退役、但仍留在这 17 题里的有 PCQM4Mv2、Pyright、Revideo、Dependent Type Checker。这 17 份 `task.toml` 盖的是公开仓，不是站上的 v2 题单。

## 环境

这 17 题都有 `environment/` 和 `docker_image`（`ghcr.io/proximal-labs/frontier-swe/...`）。每题一个镜像。树里没有 `docker-compose.yaml`。出网按题：只有 `frogsgame-rl` 和 `pcqm4mv2-autoresearch` 写了 `allow_internet = true`。图形处理器（GPU）也按题。`granite-mamba2` 与 `inference-system-optimization` 要 1 块 B200。`modular-stack-wan21`、`optimizer-design`、`pcqm4mv2-autoresearch` 要 1 块 H100。其余 12 题 `gpus = 0`。树路径里没有 Kubernetes。v2 说明页写试跑在 Modal 上。镜像没有拉取。

## 评分

公开仓用程序从 `reward.json` 取 correctness 和 speedup，再按 implementation、performance、ml_research 做门控。部分题有部分分。`scripts/score_from_reward.py` 的任务表只有这 17 题。`SCORING.md` 写事后审计可以把一试记 0，审计文件不在这个 commit 里。v2 榜上的五次平均（页上写作 mean@5）和 20 小时预算，验证器不在这个 commit。

## agent / runtime

v2 说明页写默认回路是 Proximus。文中说它在 mini-swe-agent 上加了上下文压缩、视觉和 `submit`，每题 20 小时。Proximus 源码不在这个 commit。这个 commit 另有 `harbor_ext/` 里的若干命令行类，以及可选依赖 `harbor>=0.2.0`。抽到的 `tasks/frogsgame-rl/job.yaml` 把 environment 指到 `harbor_ext.modal_managed:ManagedModalEnvironment`。

## 迁入代价

高。34 题的验证器不在公开 commit。公开的 17 题里还有要 GPU 的题，以及一份自定义 Modal environment。

## 对抽象的压力

压在 dataset 和 environment。公开 task 目录是 17 题，站上 v2 是 34 题。部分 environment 要 GPU，还指向仓库自带的 Modal environment。

## MANIFEST

`notes/sources/frontierswe-v2/MANIFEST.md`
