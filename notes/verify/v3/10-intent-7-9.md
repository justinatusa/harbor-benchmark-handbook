# 意图面 7、8、9

材料是 `notes/verify/v2/03-existing-harbor-files.md`、`notes/verify/v2/04-no-adapter-exams.md`、`notes/orchestration-log.md`、`docs/done-when.md`、`notes/final-report.md`，以及现行 `docs/registry.md`、`docs/layer2/`、`notes/sources/<slug>/MANIFEST.md`。`docs/` 未改。本轮不做文风大修。HEAD `c7b2595`。

## 7. 已有 Harbor 接入要对照

缺口。

有 `task.toml` 的清单是 8 份：`terminal-bench-4-0`、`terminal-bench-2-1`、`swe-bench-pro`、`swe-atlas`、`mls-bench-lite`、`deepswe-v1-1`、`swe-marathon`、`frontierswe-v2`。优先核 `notes/verify/v2/03-existing-harbor-files.md` 只写了前 6 个，并用当时的 Harbor 0.23.0 读入。后两个不在这份优先核里。

`swe-marathon`：清单写 20 个任务的 `task.toml`，安装句是 `harbor[modal]==0.20.0`。登记距离是重改造。`docs/layer2/swe-marathon.md` 不存在。`notes/verify/v3/05-cards.md` 把它列在缺介绍卡里。没有 0.23.0 读入记录。

`frontierswe-v2`：清单写 17 份 `task.toml`。登记与 `docs/layer2/frontierswe-v2.md` 都是暂不宜接。优先核没有用 0.23.0 读入这 17 份。

`mls-bench-lite` 的优先核写登记是原生可接，并写 `docs/layer2/mls-bench-lite.md` 不存在。现行登记与这张介绍卡都是轻适配。这份优先核和现行格子对不上。

全无 Harbor adapter：52 份 `MANIFEST.md` 里，没有一份把 Harbor adapter 写成已有文件。`vision2web` 的 `vision2web/inference/adapters/` 是被测 CLI 目录，不是 Harbor adapter。52 减去上面 8 个有 `task.toml` 的，剩 44 个。`notes/verify/v2/04-no-adapter-exams.md` 只归类了其中 5 个：`browsecomp`、`hle`、`charxiv`、`mmmu-pro`、`video-mme`。材料是 `docs/abstraction.md` 和这五份清单，没有写先读 Harbor 官方再归类。其余 39 个没有同样的归类笔记。登记 52 行都有距离档，这不是那条归类记录。`programbench` 登记是轻适配，介绍卡写清单没有 `task.toml`、也没写 Harbor adapter。

### swe-marathon

仓内有 `task.toml` 记录。`notes/sources/swe-marathon/MANIFEST.md` 写任务出网在 `task.toml`，点名 `slack-clone` 的 `task.toml`，并写 4 道 CUA 题的 `task.toml` 把 UX 称为 LLM judge。运行说明是 Harbor CLI，安装句是 `harbor[modal]==0.20.0`。这份清单没有把 Harbor adapter 写成已有文件。`docs/registry.md` 这一行 runtime 是 Harbor CLI，距离是重改造，没有写 `task.toml`，也没有写 adapter。`docs/layer2/swe-marathon.md` 不存在。`notes/verify/v2/03-existing-harbor-files.md` 没有这个 slug。Harbor adapter 仓内未见，本轮不升档。原文未写明这是 Harbor task，不升档。

### frontierswe-v2

仓内有 `task.toml` 记录。`notes/sources/frontierswe-v2/MANIFEST.md` 写 17 份 `task.toml`。`docs/registry.md` 这一行写 17 份 `task.toml`，距离是暂不宜接。`docs/layer2/frontierswe-v2.md` 写公开仓 17 题各有一份 `task.toml`，并写没有看到 adapter。`notes/verify/v2/03-existing-harbor-files.md` 没有这个 slug。Harbor adapter 仓内未见，本轮不升档。原文未写明这是 Harbor task，不升档。

## 8. 过程可进化

缺口。

`notes/orchestration-log.md`「2026-09-24 多次增量」写 `git log --oneline origin/main` 当时指到 `fb12bd1`，并抄了 10 个 SHA 的提交标题：`3574c4f`、`1956220`、`78e6dbb`、`e1be71e`、`f46bcbd`、`7d8078f`、`9550f99`、`f7096bd`、`bc6476d`、`caea6be`。每条是提交标题。没有写这次合入改进了哪一面。`notes/rounds/R1.md` 到 `R4.md` 没有把某次合入对应到某一面。

这份列表停在 `caea6be`。HEAD `c7b2595` 在它之后还有提交，包括 `5e6e2f6`、`fb12bd1`、`490cef6`、`d165123`、`79dd569`、`97c951e`、`c7b2595`。这些也没有写入「改进了哪一面」。

`docs/done-when.md` 里「过程中已多次合入 `main`」是已勾，旁证指向 `notes/orchestration-log.md`。这勾不拿来挡这次核验。`notes/rounds/completion-audit.md` 文末写十项都已勾，其中文风项保持已勾。现行 `docs/done-when.md` 的文风项是未勾。那份审计不拿来当核验结论。

文风项现在是未勾。`docs/done-when.md` 该行是 `- [ ]`，并写旧零命中在 `d165123` 改 Layer0 之后已过期，须他检。未勾，所以「文风项已勾」这一条目前不成立。

## 9. 文风最后

缺口。文风面未交，留给 Harbor③。

`docs/done-when.md` 文风项未勾。`notes/final-report.md` 写「文风须 Harbor③ 他检，不采信本次自勾的 §8。」`notes/rounds/style-check.md` 文末写「零命中。文风项不勾。」同文件「第二遍」的零命中，以及 `notes/rounds/completion-audit.md` 里「文风项保持已勾」，不采信。本轮不改 `docs/`，不做文风大修，不把文风写成收工。

## 主控裁决

面 7 成立。优先核没覆盖 `swe-marathon`、`frontierswe-v2` 的 0.23.0 读入；`mls-bench-lite` 旧核写原生可接，现行登记和介绍卡是轻适配。本轮不改距离，不动 `docs/registry.md`。39 个没有先读官方再归类的笔记，证据不够，不补一句。`docs/abstraction.md` 没有写只缺一句，不改。缺卡进 `notes/verify/v3/05-cards.md`。优先核进 `notes/verify/v2/03-existing-harbor-files.md` 的后续收束。无 adapter 归类进 `notes/verify/v2/04-no-adapter-exams.md` 的后续收束。本轮不改 `docs/`。

面 8 成立。合入列表只有提交标题。`caea6be` 之后到现行 HEAD `53f4885` 仍没有「改进了哪一面」。逐次说明写不进 `docs/layer0.md`、`docs/sources.md` 或 `notes/final-report.md` 的一句。不用 `docs/done-when.md` 里「过程中已多次合入 `main`」的已勾挡核验。应进 `notes/orchestration-log.md` 的后续收束。本轮不改 `docs/`。

面 9 成立。文风项未勾。本轮故意未做 no-ai-slop / Harbor③ 文风，不勾 `docs/done-when.md` 的文风项，不改读者文档文风。

V3-10-END
