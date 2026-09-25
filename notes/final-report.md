# 未完成说明

本文是过程记录。距离与终报里的旧数字对不上时，以 `docs/registry.md` 为准。2026-09-25 以后的读者路径以 `docs/` 为准。下面的「未核实」名单写于更早的 tip，其中 `unknown` 与轻适配已经改过。是否把转化路径再收成 skills：不写 skills 正文。现有 `docs/conversion-playbook.md` 已按依赖分节。



Done-when 的勾选以 `docs/done-when.md` 为准。证据在各文件，不在这份报告里重复成新结论。

## 改过的主要文件

- `docs/layer0.md`
- `docs/abstraction.md`
- `docs/conversion-playbook.md`
- `docs/registry.md`
- `docs/conflicts.md`
- `docs/sources.md`
- `docs/layer2/`
- `notes/rounds/R1.md`
- `notes/rounds/R2.md`
- `notes/rounds/R3.md`
- `notes/rounds/R4.md`
- `notes/adversarial/A1-response.md`
- `notes/adversarial/A2-response.md`

`git log --oneline -20`：

```
caea6be Freeze the Harbor noun set in the R4 round note.
cb1994d Answer the A2 attacks and fix the distance mismatches.
bc6476d Record R3 exceptions and check twenty entry URLs.
cb61726 Fill the next Harbor research gap in dependency order.
80084d1 Correct OfficeQA Pro distance when the dataset is gated.
f7096bd Add Layer2 cards for tools, GDP tasks, exams, and program reconstruction.
7d5e2a0 Add the four missing terminal and SWE source manifests.
b34271b Fill registry distance from source manifests.
9550f99 Add Layer2 cards for browse, desktop, MCP, exam, and spreadsheet tasks.
01e006b Add Layer2 cards for long SWE, physics, office, and chart tasks.
7d8078f Decide the thin Harbor noun set and write the conversion checklists.
a6132bd Add Layer2 cards for spreadsheet v2, video, GPU training, private work, charts, and SWE-Atlas.
47d74a9 Write the Harbor 0.23.0 component map into the reader entry.
9fc7ef0 Record responses to the A1 attacks on the Harbor extension map.
01029b9 Add source manifests for Terminal-Bench 4.0, Terminal-Bench 2.1, DeepSWE, and SWE-Bench Pro.
1f8e23d Record Harbor 0.23.0 nouns from the package and the docs.
2ba00a8 Add source manifests for SWE-Marathon, SWE-Atlas, MLS-Bench-Lite, FrontierCode, and CursorBench.
582000f Add source manifests for SEC-bench Pro, ExploitGym, CritPt, AA-Omniscience, and AA-LCR.
6057f61 Add source manifests for FrontierFinance, BigFinanceBench, OSWorld 2.0, GDP.pdf, and MMMU-Pro.
dc012c2 Add source manifests for the chart and code set and the knowledge-work set.
```

## 已核实

- Harbor 版本是 0.23.0。
- 52 个 slug 都有 MANIFEST。
- 介绍卡 30 张。数的是 `docs/layer2/*.md`。`.gitkeep` 不算。
- A1 17 条都有回应。
- A2 21 条都有回应。
- R3 抽了 20 个入口。`browsecomp` 为 403。

## 未核实

`docs/registry.md` 里「与 Harbor 距离」仍为 `unknown` 的 slug：

- `mmmu-pro`
- `mathvision`
- `video-mme`
- `automationbench`
- `nl2repo-bench`
- `programbench`。原标轻适配但缺 `task.toml`。MANIFEST 没有写明需要新写或大改 task、环境或评分，所以不是重改造。

上面前五题勿当能接。距离保持 unknown。缺的是清单没写评测是否不要 GPU。`nl2repo-bench` 还没写死两个镜像算不算多容器。`programbench` 另因缺 `task.toml` 记 unknown，勿当能接。BrowseComp 入口曾返回 403。DeepSWE 没有 v1.1 tag。文档站未标版本。SWE-Atlas 的任务文件不是 Harbor 0.23.0。

怎么用见 `docs/layer0.md`：先对版本，再查距离，然后按 `docs/conversion-playbook.md` 的清单做。`docs/conversion-playbook.md` 的例子盖住 8 个 slug（`spreadsheetbench`、`posttrainbench-v1-1`、`osworld-verified`、`charxiv`、`browsecomp`、`aa-briefcase`、`deepswe-v1-1`、`swe-bench-pro`），其余 44 个不在这份清单里，因为例子只来自本轮打开过的 MANIFEST，52 题没有全部抽象完。

文风抽查见 `notes/verify/V-final.md`。不把 §7 写成全项目完成。

FINAL-REPORT-END
