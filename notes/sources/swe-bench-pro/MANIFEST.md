# swe-bench-pro

- slug: `swe-bench-pro`
- 抓取日: 2026-09-24 Asia/Shanghai

## 入口与官方仓

- 入口: https://arxiv.org/html/2509.16941
- 论文首页写的代码仓: https://github.com/scaleapi/SWE-bench_Pro-os
- 数据: https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro （论文首页同一链接）
- 公开 git commit: tag `v2.0.0` 剥开后 = `main` HEAD = `66f92766bba642462d4bbe5479e83f91f9211862`（2026-09-22 -0400，“Merge pull request #119 from scaleapi/release/v2.0.0”）。annotated tag 对象是 `056ad93f2ad44ea529a65f2fcd4dcdd801c7bcc3`。
- 同日 `git ls-remote --tags` 只有 `v2.0.0`。HF 卡写原始 731 题也是 git tag `v1.0`；远端 tags 列表里没有 `v1.0`。

## 论文 / blog / HF

- 论文: arXiv:2509.16941 ，Deng, Da 等，Scale AI。HTML 即入口。
- HF 卡还链了一份 Scale PDF: https://static.scale.com/uploads/654197dc94d34f66c0f5184e/SWEAP_Eval_Scale%20(9).pdf 。本清单以 arXiv HTML 和仓内 `v2/README.md` 为准，没有下该 PDF。
- 公开榜（HF 卡）: https://scale.com/leaderboard/swe_bench_pro_public
- HF `ScaleAI/SWE-bench_Pro`: config `default` = V2，642 题；`hard` = 51；`v1` = 731（卡写 2026-02-23 发布，revision `v1.0`）。V2 卡写 changelog 日期 2026-09-22。

论文里的全集是 1865 题：public 731（11 个 copyleft 仓库）、commercial 276（18 个创业公司私有仓，只公布结果）、held-out 858（另 12 个仓库，不公开）。这是论文口径。仓和 HF 在 2026-09-22 把公开集收成 V2 的 642，并保留 v1 的 731 列。commercial / held-out 仍然不在这个公开仓里。

## 测什么

论文摘要：在 SWE-Bench 的做法上做更难的长程软件工程题；agent 拿到整个代码库和自然语言任务说明，要交出能通过仓库测试的 code patch。§3.2：每题还有人工写的 requirements，以及在需要时给出测试所期望的 interface。V2 README：公开集是 11 个仓库上的 642 个 Harbor 任务目录（Go/Python/JS/TS 的划分以 HF 卡为准：go 256、python 237、js 145、ts 4）。

## 环境线索

- 容器: 有。论文 §3.2：每题在容器化、按语言装好依赖的环境里评测，并说环境会以预构建 Docker image 发布。V2 每题 `environment/Dockerfile` 从 `ghcr.io/scaleapi/swe-bench_pro-v2:<instance_id>` 而来（linux/amd64，匿名 pull）。仓内 `v2/tasks/*/task.toml` 共 642，与 README 一致。样本里仓库在镜像内的 `/app`。
- 出网: 642/642 的 `task.toml` 都是 `[agent] network_mode = "no-network"`，`[environment] network_mode = "public"`，`[verifier] network_mode = "public"`。`v2/README.md` “locked protocol”：agent 阶段离线，`--allow-agent-host` 只放行模型 endpoint；WebFetch/WebSearch 关掉；setup 和 verifier 保持正常网络，并写明少数 Go 题在测试时会拉模块。
- GPU: 642 个 `task.toml` 都没有 `gpus` 键。论文 §5 写开源 LLM 用 vLLM、单机 8×H100 来托管模型；这是模型服务，不是任务容器的 `gpus` 字段。任务沙箱要不要 GPU：unknown。
- K8s: unknown。已检出的 md/toml/yaml/py/sh 中没有 `kubernetes` 或 `k8s`。
- 多容器: 未见 compose。642 题各用一个镜像。verifier 按 locked protocol 不在 agent 沙箱里跑，而是把 `model.patch` 放到干净镜像上再跑（`patch_replay`）。这是两次单容器，不是 compose 多服务。
- 资源（样本 `task.toml`）: `cpus = 1`，`memory_mb = 4096`，`storage_mb = 10240`，agent 与 verifier `timeout_sec = 3000.0`。V2 README 把 locked protocol 的预算写成每题 50 分钟。

## 评分

公开集的解题分是测试，不是 judge 模型。论文 §3.2 / §5：fail2pass 与 pass2pass；表里的 Resolve (%) 是 Pass@1。抽到的 `v2/tasks/*/tests/test.sh` 在退出时写 `/logs/verifier/reward.txt` 为 1 或 0，并 `git apply` 隐藏的 `test_patch.patch`。V2 README：权威分数是在干净镜像上重放 diff 之后的重评分；oracle 642/642 通过，空 patch 642/642 不通过。

论文 §6.3 另用 GPT-5 做 LLM-as-a-judge，只给失败轨迹分桶（wrong solution、tool-use 等），并引用 Yang et al. 与人工分桶的对齐。这不是 Resolve 率。DeepSWE 论文 §3.4 在抽查 SWE-Bench Pro 时也写明：他们的外部 judge 是 verifier 的审计，executable verifier 仍是榜上的 grader。

## agent / runtime

论文 §5：结果用 SWE-Agent scaffold；也试过 Agentless，但多文件编辑差，正文以 SWE-Agent 为准。最多 50 turns。开源模型用 vLLM。

V2 README 的运行时是 Harbor（`harbor[modal]>=0.22`，Modal >= 1.5.1，用于分阶段网络策略）。locked agents：`locked_claude_code:LockedClaudeCode`、`locked_mini_swe:LockedMiniSwe`、`locked_codex:LockedCodex`，加上 `patch_replay:PatchReplayAgent`、`oracle`、`nop`。工具在 `v2/tooling/`。

## 体积与是否入 git

- GitHub API `size`（2026-09-24，KB）: 38706。
- 同日 `--depth 1` 完整克隆工作树约 159MB（`/tmp`，未放入 `/workspace`）。树清单约 11025 个路径；其中 `v2/tasks` 的 `task.toml` 为 642。
- HF 卡页面写 downloads 与一个约 15.1 MB 的展示字段；那不是本清单对仓库的测量。
- 本目录只留这份 `MANIFEST.md`。官方仓不入本仓库 git。GHCR 镜像未 pull。

## 未能抓取

- commercial 276 与 held-out 858：论文写明不公开代码，公开仓里没有。
- GitHub 上没有 HF 卡所说的 tag `v1.0`（2026-09-24 `ls-remote --tags` 只有 `v2.0.0`）。v1 的 731 行在 HF config `v1`，本清单没有把这 731 行下载到本地。
- Scale 的 PDF 副本未下。
- 642 个 GHCR 镜像未 pull。
- 论文 §5 的 8×H100 是模型托管；任务容器 GPU 需求没有写在 `task.toml` 里。

MANIFEST-END
