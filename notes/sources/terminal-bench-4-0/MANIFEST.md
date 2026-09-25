# terminal-bench-4-0

- slug: `terminal-bench-4-0`
- 抓取日: 2026-09-24 Asia/Shanghai

## 入口与官方仓

- 入口: https://www.tbench.ai/news/terminal-bench-4-0
- 官方仓: https://github.com/harbor-framework/terminal-bench
- 4.0 快照: tag `v4.0.0` = commit `452bf305c6daa62fc59061d22133a7cbc7c1572e`（`git ls-remote` 与 `git rev-parse HEAD` 一致；提交说明 “Add prebuilt image publishing for releases (#1811)”，作者日期 2026-08-25 -0700）
- 同日 `main` HEAD 是 `4def1f367467b34b18e0dbdc086400ba71c3e037`，晚于该 tag。4.0 以 tag 为准，不以当天 `main` 为准。
- 发布页: https://github.com/harbor-framework/terminal-bench/releases/tag/v4.0.0 （`published_at` 2026-08-26T04:48:12Z）。正文给出 `harbor run -d terminal-bench/terminal-bench@4.0.0`，以及 Harbor Hub URL `https://hub.harborframework.com/datasets/terminal-bench/terminal-bench/4`。
- 运行说明: https://www.tbench.ai/run

## 论文 / blog / HF

- blog: https://www.tbench.ai/news/terminal-bench-4-0 （作者署名 Ryan Marten）
- 论文: https://arxiv.org/abs/2601.11868 （Merrill et al., Terminal-Bench）。摘要写的是 Terminal-Bench 2.0（89 tasks），不是 4.0 专文。仓内 `CITATION.cff` / README 指向同一篇。
- HF: `harborframework/terminal-bench`，Hub tag `v4.0.0`。数据集卡写明该 tag 为 66 tasks，Released 2026-08-26，对应上述 GitHub release。https://huggingface.co/datasets/harborframework/terminal-bench

## 测什么

在 tag `v4.0.0` 的 README 里，Terminal-Bench 被写成用来衡量 agent 工作前沿的、会随时间演进的多样化困难任务集；4.0 公告写的是在该数据集上校准时间/CPU/内存、修任务、并删掉饱和任务。（README @ `452bf305`；https://www.tbench.ai/news/terminal-bench-4-0）

该 tag 的 `tasks/*/task.toml` 共 66 个，与 HF 卡的 66 tasks 一致。发布说明列出删除 8 个任务、并点名一批修改过的任务。

## 环境线索

- 容器: 有。66/66 `environment_mode = "separate"`。`docs/task-template.toml` 注释写 “verifier runs in its own container (required)”。66/66 在完整检出时都有 `environment/Dockerfile`。
- 出网: 66/66 的 `task.toml` 都没有 `network_mode` 键。模板 `docs/task-template.toml` 写着 `network_mode = "public"`，注释 “Terminal-Bench is open internet”；这是模板，不是每题已写入的值。另有 2 题显式 `allow_internet = false`：`batched-eval-parity`、`lake-temp-glm`。其余 64 题未写 `allow_internet`。
- GPU: 3 题 `gpus = 1` 且 `gpu_types = ["H100"]`：`fp8-rmsnorm-gemm`、`jax-speedrun-gpu`、`math-eval-grader`。`jax-speedrun-gpu` 的 `[verifier.environment]` 同样是 1×H100。55 题 `gpus = 0`。8 题没有 `gpus` 键：`bun-sourcemap-leak`、`ctr-optimization`、`interleaved-vigenere`、`payments-pipeline-fix`、`production-planning`、`session-window-debug`、`shadow-relay`、`wal-recovery-ordering`。https://www.tbench.ai/run 写 “Terminal-Bench contains tasks that require GPUs”，示例沙箱是 Modal。
- K8s: unknown。在该 tag 已检出的 md/toml/yaml/py/sh 中没有 `kubernetes` 或 `k8s`。
- 多容器: 11 题有 `environment/docker-compose.yaml`，且都含 `main` 以外的服务：`ctr-optimization`（api）、`cumulative-layout-shift`（barber-shop-data-backend）、`freight-dispatch-shift`（event-feed）、`heat-pump-warranty`（warranty-portal、asset-ledger、document-vault、returns-ledger、compliance-ledger、warranty-inbox）、`intrastat-meldung`（odoo、compliance-hub、idev、services、dms）、`kv-live-surgery`（loadgen）、`legacy-utility-triage`（legacy-workstation、legacy-app）、`live-database-cutover`（mysql-db、redis、postgres-db、customer）、`medical-claims-processing`（playwright-mcp、workspace）、`nextjs-performance`（warehouse-api）、`payments-pipeline-fix`（seeder、kafka、customer）。
- 超时: 公告写 4.0 把 agent timeout 统一成 8 小时。抽到的 `task.toml` 里 `[agent] timeout_sec = 28800.0`。

## 评分

任务分是程序 verifier，不是另调一个 judge 模型来打分。论文 §2.1（写的是这套框架 / TB 2.0）说 tests 检查最终容器状态是否达到 instruction 里的结果，不检查 agent 的命令或控制台输出。tag 上 63/66 的 `tests/test.sh` 含 `/logs/verifier/reward` 或 `reward.txt`/`reward.json`，其中 53 个脚本出现 `pytest`。另外 3 个 `test.sh` 本身没有 “reward” 字样，但转到评分脚本：`heat-pump-warranty` 与 `legacy-utility-triage` 调用 `tests/test_scoring.py`；`vba-userform-port` 用 pytest 跑 `test_scoring.py`。抽读的 `test_scoring.py`（上述三题，外加 `freight-dispatch-shift`、`medical-claims-processing`）把 0/1 写入 `reward.json`，关键词扫描未见 OpenAI/Anthropic/LLM/judge 调用。`heat-pump-warranty`、`legacy-utility-triage`、`medical-claims-processing` 的 `verification_explanation` 写明 deterministic、no LLM judge；`freight-dispatch-shift` 写 “The verifier deterministically runs…”。未逐行审完 66 题全部测试文件。

## agent / runtime

README @ tag 用 Harbor 跑：`uv tool install 'harbor[modal]'`，示例 `--agent oracle` 与 `--agent claude-code`，`--env modal`。运行页示例是 `harbor run -d terminal-bench/terminal-bench@4.0.0 -e modal -a claude-code`。论文 §2.1 列举 Harbor 可接 Claude Code、Codex CLI、OpenHands、Mini-SWE-Agent，以及作者自己的 Terminus 2；该段对应的是论文中的框架，不是 4.0 榜单只跑了哪些 agent。

## 体积与是否入 git

- GitHub API `size`（2026-09-24，单位 KB，整仓不是单 tag）: 462845。
- release 附件 `terminal-bench-prebuilt-v4.0.0.tar.gz`: 452093597 bytes。`prebuilt-images.json`: 151063 bytes。
- 同日把 tag 的 `tasks/` 检出后，工作树约 855MB（含环境文件）。该树在 `/tmp`，未放入 `/workspace`。
- 本目录只留这份 `MANIFEST.md`。官方仓不入本仓库 git。

## 未能抓取

- 452MB 预构建包和约 855MB 任务树没有留在 `/workspace`：超过 5MB 且整仓不应进本仓库。
- Harbor Hub 页面正文没有单独抓取，只用了 release 正文里的 URL。
- 没有把 `main`（`4def1f36`）和 `v4.0.0` 做 diff。
- 8 题缺 `gpus`、64 题缺 `network_mode`，不能从缺键推出运行时默认值；只记录了模板注释。
- 论文摘要覆盖的是 2.0 的 89 题，不是 4.0 的 66 题。

MANIFEST-END
