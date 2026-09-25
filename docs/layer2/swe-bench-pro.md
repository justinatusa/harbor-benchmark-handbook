# SWE-Bench Pro

公开仓当前 tip 是 V2。论文里的 commercial 与 held-out 不在这个仓里。

1. 一句话测什么。在 SWE-Bench 的做法上做更难的长程软件工程题：agent 拿到整个代码库和自然语言任务说明，要交出能通过仓库测试的 code patch。出处是论文摘要（https://arxiv.org/html/2509.16941）。§3.2 还写每题有人工写的 requirements，需要时给出测试所期望的 interface。V2 README 写公开集是 11 个仓库上的 642 个 Harbor 任务目录。HF 卡对这 642 题的语言划分是 go 256、python 237、js 145、ts 4。

2. 官方源。入口 https://arxiv.org/html/2509.16941 。代码仓 https://github.com/scaleapi/SWE-bench_Pro-os 。tag `v2.0.0` 剥开后 = `main` HEAD = `66f92766bba642462d4bbe5479e83f91f9211862`（2026-09-22 -0400，说明 “Merge pull request #119 from scaleapi/release/v2.0.0”）。annotated tag 对象是 `056ad93f2ad44ea529a65f2fcd4dcdd801c7bcc3`。`git ls-remote --tags` 只有 `v2.0.0`。HF https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro ：config `default` = V2 的 642 题，`hard` = 51，`v1` = 731。公开榜 https://scale.com/leaderboard/swe_bench_pro_public 。论文全集是 1865 题：public 731、commercial 276、held-out 858。HF 卡写原始 731 题对应 git tag `v1.0`，远端 tags 列表里没有 `v1.0`。Scale PDF 没有下载。

3. 形态。`task`、`dataset`、`environment`、`verifier`、`agent`。`v2/tasks/*/task.toml` 共 642 个。V2 README 的命令是 `harbor run -p v2/tasks`。清单没有写出 `dataset.toml`，也没有写 `adapter`。locked agents 在 `v2/tooling/`。

4. 与 Harbor 距离。原生可接。公开仓能指出 `v2/tasks/*/task.toml`（642 个），V2 README 把这些目录称为 Harbor task。commercial 276 与 held-out 858 不在这个公开仓里，这两部分没有可指的 `task.toml`。

5. 环境。论文 §3.2 写每题在容器化、按语言装好依赖的环境里评测，环境以预构建 Docker image 发布。V2 每题 `environment/Dockerfile` 从 `ghcr.io/scaleapi/swe-bench_pro-v2:<instance_id>` 而来（linux/amd64，匿名 pull）。样本里仓库在镜像内的 `/app`。642/642 的 `[agent] network_mode = "no-network"`，`[environment] network_mode = "public"`，`[verifier] network_mode = "public"`。locked protocol 写 agent 阶段离线，`--allow-agent-host` 只放行模型 endpoint，WebFetch/WebSearch 关掉；setup 和 verifier 保持正常网络，少数 Go 题在测试时会拉模块。642 个 `task.toml` 都没有 `gpus` 键。论文 §5 的单机 8×H100 是用 vLLM 托管开源模型。任务沙箱要不要 GPU 是 unknown。K8s 是 unknown。未见 compose。642 题各用一个镜像。locked protocol 把 `model.patch` 放到干净镜像上再跑 verifier，清单记为两次单容器。样本资源是 `cpus = 1`、`memory_mb = 4096`、`storage_mb = 10240`，agent 与 verifier `timeout_sec = 3000.0`。V2 README 把 locked protocol 的预算写成每题 50 分钟。

6. 评分。公开集的解题分来自测试。论文 §3.2 / §5 写 fail2pass 与 pass2pass，表里的 Resolve (%) 是 Pass@1。抽到的 `v2/tasks/*/tests/test.sh` 在退出时写 `/logs/verifier/reward.txt` 为 1 或 0，并 `git apply` 隐藏的 `test_patch.patch`。V2 README 写权威分数是在干净镜像上重放 diff 之后的重评分；oracle 642/642 通过，空 patch 642/642 不通过。论文 §6.3 用 GPT-5 做 LLM-as-a-judge，只给失败轨迹分桶。DeepSWE 论文 §3.4 在抽查 SWE-Bench Pro 时写外部 judge 是 verifier 的审计，executable verifier 仍是榜上的 grader。

7. agent/runtime。论文 §5 的结果用 SWE-Agent scaffold，最多 50 turns；Agentless 因多文件编辑差，正文以 SWE-Agent 为准。开源模型用 vLLM。V2 README 的运行时是 Harbor（`harbor[modal]>=0.22`，Modal >= 1.5.1，用于分阶段网络策略）。locked agents 是 `locked_claude_code:LockedClaudeCode`、`locked_mini_swe:LockedMiniSwe`、`locked_codex:LockedCodex`，加上 `patch_replay:PatchReplayAgent`、`oracle`、`nop`。工具在 `v2/tooling/`。

8. 迁入代价。中。公开 V2 的 642 个目录已是 Harbor task，README 有 `harbor run -p v2/tasks`。权威分还要 `patch_replay` 在干净镜像上重评分，locked agent 在 `v2/tooling/`，并要求 `harbor[modal]>=0.22`。commercial 276 与 held-out 858 没有公开代码。642 个 GHCR 镜像未 pull。GitHub 上没有 HF 卡所说的 tag `v1.0`，v1 的 731 行没有下载到本地。

9. 对抽象的压力。`agent` 的 `network_mode` 是 `no-network`，`environment` 与 `verifier` 是 `public`。`verifier` 的权威分在另一份干净镜像上重跑，agent 阶段只留下 `model.patch`。`dataset` 在公开仓里是 `v2/tasks` 的 642 题；HF 另有 `hard` 51 与 `v1` 731。commercial 与 held-out 不在公开仓。任务容器没有 `gpus` 键，论文里的 8×H100 记在模型托管上。

10. MANIFEST 路径。`notes/sources/swe-bench-pro/MANIFEST.md`
