# Orchestration log

Coordinator log. Reader-facing decisions stay in `docs/`.

## 2026-09-24

- Fast-forwarded local `main` from `9af37fd` to `8a71530` (seed prompt + bench-list).
- Verified local Harbor CLI and package metadata are `0.23.0`. Evidence written to `docs/sources.md`.
- Opening skeleton (this commit series): Layer0 outline, taxonomy plan, empty-then-seeded registry, Done-when copy, conflicts/sources/playbook placeholders.
- Not a finished round. R1 has not started.
- Next commit seeds 52 registry rows from `prompts/bench-list.md`. Research columns stay `unknown`.

## 2026-09-24 R1

R1 笔记已收进 docs，main 待本次推送。Done-when 里除 Harbor 版本外都还没勾。

## 2026-09-24 多次增量

`git log --oneline origin/main` 当时指到 `fb12bd1`。下面从早到晚，SHA 按该命令的缩写抄录。每条都已在 `origin/main` 上，各是一次增量合入。

- `3574c4f` Record Harbor 0.23.0 check and research skeleton.
- `1956220` Seed registry with the 52 bench-list slugs.
- `78e6dbb` Add source manifests for browsecomp, OSWorld-Verified, MCP-Atlas, and HLE.
- `e1be71e` Add source manifests for SpreadsheetBench, Video-MME, PostTrainBench, and AA-Briefcase.
- `f46bcbd` Add source manifests for the vision set and the office and finance set.
- `7d8078f` Decide the thin Harbor noun set and write the conversion checklists.
- `9550f99` Add Layer2 cards for browse, desktop, MCP, exam, and spreadsheet tasks.
- `f7096bd` Add Layer2 cards for tools, GDP tasks, exams, and program reconstruction.
- `bc6476d` Record R3 exceptions and check twenty entry URLs.
- `caea6be` Freeze the Harbor noun set in the R4 round note.

## 2026-09-25 读者手册

- 运行层和接入层：`docs/abstraction.md` 写进删掉这两层会混掉的 slug，并抄了清单原句和路径。task 层仍只说明任务粒度。
- 浏览：没有写进 `docs/abstraction.md`。仓内没有「浏览是某一层的依赖」这句，最近句仍是 playbook 里只接 grader 时浏览仍是 unknown。
- 轻适配和重改造：没有写进 `docs/abstraction.md` 或 `docs/layer1.md`。仓内没有能对照 registry 这两档字样打勾的分开判定句。
- 这次改进的是读者能看到轻/重为什么还判不了。`docs/layer1.md` 写明仓内仍没有稳定的轻/重判定句。
- 转化清单：`docs/conversion-playbook.md` 的要 GPU、要出网、多容器勾选，以及已标不可执行的 judge 勾选，写明本仓缺哪份文件就停。pytest 仍点名三份清单。
- 归类依据：`docs/registry.md` 压力列写了 `swe-marathon` 与 `frontierswe-v2` 为何不升档，以及 `browsecomp`、`hle`、`charxiv`、`mmmu-pro`、`video-mme` 依据哪份清单、缺先读 Harbor 官方的记录所以保持现档。距离格未改。

## 2026-09-25 判定句与浏览停句

- 判定句：`docs/layer1.md` 与 `docs/abstraction.md` 各写了轻适配、重改造两句，读者可对照一个 slug 打勾。两处都引用 `notes/verify/v2/08-closed-gated.md` 的原句「轻适配要有能交出去的 task 目录」，并写明本轮把这句收成「有 task 目录，或 MANIFEST、介绍卡里已写出的等价证据」。删掉了 `docs/layer1.md` 里「仓内没有稳定的轻/重判定句」。
- programbench 距离：`docs/registry.md` 该行从轻适配改为 `unknown`，压力列写「原标轻适配但缺 task.toml，与 08 规则冲突，勿当能接」。`docs/layer2/programbench.md` 的距离句改成同一档。MANIFEST 没有写明要新写或大改 task、环境或评分，所以没有改成重改造。
- 浏览：仓内仍没有把浏览写成 task、运行或接入某一层依赖的句子。`docs/abstraction.md` 依赖说明写了停句：浏览暂不写入依赖列，缺的是「浏览属于哪一层」的仓内句，读者勿自行升成新轴。`docs/conversion-playbook.md`「只接 grader 时，浏览仍是 unknown」没有改写成已落层。
