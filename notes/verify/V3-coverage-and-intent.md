# V3 覆盖与意图面

材料是现行 `docs/abstraction.md`、`docs/layer0.md`、`docs/conversion-playbook.md`、`docs/registry.md`、`docs/layer1.md`、`docs/done-when.md`、`notes/final-report.md`，以及 `notes/verify/v3/`、`notes/verify/V1-abstraction-axes.md`、`notes/verify/V2-morphology-lexicon.md`。这不是收工。§7 文风项不勾。52 题没有全部抽象完。

## 覆盖

`docs/layer0.md` 怎么用第 4 步写：`docs/conversion-playbook.md` 的例子盖住 8 个 slug（`spreadsheetbench`、`posttrainbench-v1-1`、`osworld-verified`、`charxiv`、`browsecomp`、`aa-briefcase`、`deepswe-v1-1`、`swe-bench-pro`），其余 44 个不在这份清单里，因为例子只来自本轮打开过的 MANIFEST，52 题没有全部抽象完。

`notes/final-report.md` 是同一句。名单见 `notes/verify/v3/09-intent-4-6.md` 的 44 个 slug。`prompts/bench-list.md` 合计 52。

`swe-bench-pro` 出现在这 8 个例子里。playbook「任务不公开或 gated」写 commercial 276 与 held-out 858 不公开，公开的 642 不在这一节整包标成暂不宜接。出现在例子名单不等于距离档已有判定。登记距离格仍是原生可接，本篇不改格。

`notes/verify/v3/05-cards.md` 数 `docs/layer2/*.md` 为 31 张。`notes/final-report.md` 写介绍卡 30 张。张数对不上，本篇不改终报。

## 意图面

| 面 | 终态 |
|---|---|
| 1 薄抽象钉 Harbor | 已交。见下。 |
| 2 官方形态压力 | 仍缺口。浏览没有落层依据。 |
| 3 关键词与关键语 | 已交。十一个词的对照都在仓内。 |
| 4 接入决策可用性 | 仍缺口。原生、轻、重没有判定句。 |
| 5 转化可照做 | 仍缺口。06 的 7 条有结束条件或缺文件；GPU、出网、多容器节仍有对不上的勾选。 |
| 6 覆盖诚实 | 已交。8 与 44 已写入 layer0 与终报。 |
| 7 已有 Harbor 接入要对照 | 仍缺口。见 `notes/verify/V-final.md` 面 7。 |
| 8 过程可进化 | 仍缺口。合入记录没有写改进了哪一面。 |
| 9 文风最后 | 仍缺口。本轮故意未做，留给 Harbor③。 |

### 1

`docs/abstraction.md`：「层只有三层，这里定稿，不多加。」删 task：「删掉 task 层会把 `terminal-bench-2-1` 和 `posttrainbench-v1-1` 混掉。「89 个终端环境任务，每题有独立环境」，「每个任务是一个基座加一个下游基准」。这只说明任务粒度不同，不是距离档。」

删运行、删接入的两对不在 `docs/abstraction.md`。在 `notes/verify/V1-abstraction-axes.md`：删运行会把没有 agent 回路的 `browsecomp` 和自带多轮 harness 的 `mcp-atlas` 混成一类；删接入会把已经是 dataset 的 `terminal-bench-4-0` 和官方单位仍是 JSON 的 `osworld-verified` 混成一类。

### 2

桌面、judge、出网、GPU、多容器、数据不公开、容器在 `notes/verify/v3/04-morphology-coverage.md` 与 `notes/verify/v3/08-intent-1-3.md` 有难样。浏览没有。`docs/conversion-playbook.md`：「只接 grader 时，浏览仍是 unknown。」`notes/sources/browsecomp/MANIFEST.md`：「官方参考实现没有浏览器或 agent 循环。」两句都没有把浏览写成 task、运行或接入的依赖。缺这一句。不写入 abstraction 或 playbook。

### 3

对照在 `notes/verify/v2/01-lexicon.md`、`notes/verify/V2-morphology-lexicon.md`、`docs/abstraction.md`。表在 `notes/verify/V-final.md`。没有缺词。

### 4

`docs/layer1.md`：「与 Harbor 距离」只允许 `原生可接`、`轻适配`、`重改造`、`暂不宜接`。没有证据时写 `unknown`。`docs/abstraction.md` 只否定两行：`swe-atlas` 因 Harbor 版本不是 0.23.0，不是原生可接；`deepswe-v1-1` 没有 v1.1 tag，所以不是原生可接。没有写轻适配和重改造怎么分开。`notes/verify/v3/09-intent-4-6.md` 记这一缺口。五行 `unknown` 的 blocker 见 `notes/verify/V-final.md`，不把 blocker 当成分档句。距离格不改。

### 5

`notes/verify/v3/06-playbook-walk.md` 的 7 条，加上 `473ab21`、`141e886` 之后的勾选，本轮再打开过。结束条件或缺什么写在 `notes/verify/V-final.md`。pytest 那条当时没有点名清单，随后只改这一条。

要 GPU、要出网、多容器或图形桌面的勾选，`notes/verify/v3/09-intent-4-6.md` 仍写对不上可打开文件，旁边没有同样的停句。本轮不改那三节。

### 6

已交句是上面「覆盖」里 layer0 与终报的那句。52 题没有全部抽象完。

### 7

`notes/sources/swe-marathon/MANIFEST.md` 有 `task.toml` 记录，安装句是 `harbor[modal]==0.20.0`。原文没有写明这是 Harbor task。登记距离是重改造。不升档。

`notes/sources/frontierswe-v2/MANIFEST.md` 写 17 份 `task.toml`。原文没有写明这是 Harbor task。登记距离是暂不宜接。不升档。

`notes/verify/v2/04-no-adapter-exams.md` 只归类了 `browsecomp`、`hle`、`charxiv`、`mmmu-pro`、`video-mme`，没有写先读 Harbor 官方再归类。其余没有同样的笔记。已合 `main` 不顶替。

### 8

`notes/verify/v3/10-intent-7-9.md`：`notes/orchestration-log.md` 的增量列表是提交标题，没有写这次合入改进了哪一面。`docs/done-when.md` 里「过程中已多次合入 `main`」的已勾不拿来当这一面的证据。

### 9

`docs/done-when.md` 文风项是 `- [ ]`。`notes/final-report.md`：「文风须 Harbor③ 他检，不采信本次自勾的 §8。」本轮不做文风大修，不跑 no-ai-slop 清零，不勾这一项。

V3-COVERAGE-END
