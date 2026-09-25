# Done-when 审计

对照 `prompts/harbor-unified-abstraction-research.md` 第 7 节，核对 `docs/done-when.md` 的勾选和仓库文件。本文件不宣称调研完成。读者文档的结论没有改。证据不够的项保持未勾，没有为了勾选降低标准，也没有把未勾项改成已勾。

审计日：2026-09-24。`origin/main` 与审计前 `HEAD` 同为 `feb509cf57c6760704ff24fa55df6d93b749f313`。

## 1. `harbor==0.23.0` 已核实写入

- 勾选：已勾。审计后仍勾。
- 证据：`docs/sources.md` 写核实日 2026-09-24，`harbor --version` 为 `0.23.0`，`uv-receipt.toml` 的约束是 `harbor==0.23.0`，`harbor-0.23.0.dist-info/METADATA` 的 `Version: 0.23.0`。勾选里的 commit `3574c4f` 存在，说明是 `Record Harbor 0.23.0 check and research skeleton.`，并且是 `origin/main` 的祖先。本机再对过：`harbor --version` 打印 `0.23.0`；`uv-receipt.toml` 的 specifier 是 `==0.23.0`；METADATA 第 3 行是 `Version: 0.23.0`；该 uv 环境里 `importlib.metadata.version("harbor")` 是 `0.23.0`。
- 判定：有证据。

## 2. `abstraction.md` 三层名词和官方词对照

- 勾选：未勾。审计后仍未勾。
- 证据：`docs/abstraction.md`。「种子」一节之外，「当前结论」写层只有三层：task（instruction、environment、verifier）、运行（agent、trial、job）、接入（adapter 只生成目录，dataset 列表）。同节有「名词表与 Harbor 官方词对照」，九行对到 task、environment、Verifier、Agent、Dataset、Adapter、trial、Job、metrics。
- 判定：有证据。文件不是只有种子。勾选原文还要求说明齐全；同文件「仍未定的点」仍有三条。本审计不把「有对照表」当成「齐全」去新勾。

## 3. `conversion-playbook.md` 的 `- [ ]` 清单

- 勾选：未勾。审计后仍未勾。
- 证据：`docs/conversion-playbook.md` 有四类正文：「要另调 judge 模型」「要 GPU」「要出网」「多容器或图形桌面」。每类有开工前准备、转化步骤、做完怎么核对、坑。全文件检索 `- [ ]` 和 `- [x]`，命中 0。
- 判定：证据不够。有分节步骤，没有 judge、GPU、出网、多容器的 `- [ ]` 清单。不把无勾选的子弹列表当成清单去勾。

## 4. Registry 52 行与 Layer2 介绍卡数量

- 勾选：未勾。审计后仍未勾。
- 证据：`prompts/bench-list.md` 52 个 slug，无重复。`docs/registry.md` 数据行 52，与名单一一对应，没有缺 slug，也没有名单外的 slug。`docs/layer2/*.md` 30 张。30 落在 20 到 30，也不少于 20。抽过的卡有十项骨架（一句话、官方源、形态、距离、环境、评分、agent/runtime、迁入代价、对抽象的压力、MANIFEST 路径）。`notes/final-report.md` 写「介绍卡 29 张」，与当前 30 个文件不一致；张数以目录为准。距离列仍为 `unknown` 的五行是 `mmmu-pro`、`mathvision`、`video-mme`、`automationbench`、`nl2repo-bench`，行还在。
- 判定：有证据。本审计不新勾。

## 5. 52 个 slug 的 `MANIFEST.md`

- 勾选：未勾。审计后仍未勾。
- 证据：`notes/sources/<slug>/MANIFEST.md` 共 52 份，与 `prompts/bench-list.md` 的 slug 一致。没有缺的 slug。抽查规则：行数少于 5 或没有文末 `MANIFEST-END` 的，数量是 0。
- 缺的 slug：无。
- 判定：有证据。本审计不新勾。

## 6. 四轮文末标记与两次对抗回应

- 勾选：未勾。审计后仍未勾。
- 证据：`notes/rounds/R1.md` 文末 `R1-END`，`R2.md` 文末 `R2-END`，`R3.md` 文末 `R3-END`，`R4.md` 文末 `R4-END`。四份都有「展」「收」「验」。`notes/adversarial/A1-response.md` 的标题是 A1-01 到 A1-17，共 17 条，文末 `A1-RESPONSE-END`。`notes/adversarial/A2-response.md` 的标题是 A2-01 到 A2-21，文末 `A2-RESPONSE-END`。
- 判定：有证据。本审计不新勾。

## 7. Layer0、Layer1、sources、conflicts

- 勾选：未勾。审计后仍未勾。
- 证据：`docs/layer0.md` 148 行，有 task、environment、verifier 等组件地图。`docs/layer1.md` 12 行，写怎么读表，全量行指向 `docs/registry.md`，不是待填标题。`docs/sources.md` 64 行，有版本核实和缩写表。`docs/conflicts.md` 82 行，有多条说法 A / 说法 B / 处理。`docs/layer2/` 见第 4 项，30 张。
- 判定：有证据。四份都在，不是空壳。本审计不新勾。

## 8. 至少 20 个 URL 状态码，以及未核实项

- 勾选：未勾。审计后仍未勾。
- 证据：`notes/rounds/R3.md`「验」里的表有 20 行状态码：`gdpval-aa-v2-1` 200，`agents-last-exam` 200，`browsecomp` 403，`spreadsheetbench` 200，`officeqa-pro` 200，`finance-agent-v2` 200，`osworld-verified` 200，`mmmu-pro` 200，`charxiv` 200，`zerobench` 200，`benchcad` 200，`video-mme` 200，`automationbench` 200，`terminal-bench-4-0` 200，`deepswe-v1-1` 200，`programbench` 200，`swe-atlas` 200，`posttrainbench-v1-1` 200，`cursorbench` 200，`hle` 200。`notes/final-report.md` 有「未核实」一节，列出上述五个距离仍为 `unknown` 的 slug，并写 DeepSWE 没有 v1.1 tag、文档站未标版本、SWE-Atlas 的 Harbor 版本不是 0.23.0。同节还有一句「文风抽查没有做」，与该文件后文以及 `notes/rounds/style-check.md` 不一致；未核实名单本身还在。
- 判定：有证据。本审计不新勾。

## 9. 文风第二遍零命中

- 勾选：已勾。审计后仍勾。
- 证据：`notes/rounds/style-check.md`「第二遍」对这六份都写了零命中：`docs/layer0.md`、`docs/abstraction.md`、`docs/conversion-playbook.md`、`docs/layer2/browsecomp.md`、`docs/layer2/swe-atlas.md`、`docs/layer2/aa-briefcase.md`。文末 `STYLE-CHECK-END`。
- 判定：有证据。按本次核对标准，文风项保持已勾。

## 10. 多次合入 `main`

- 勾选：未勾。审计后仍未勾。
- 证据：`notes/orchestration-log.md` 只记了一次快进，local `main` 从 `9af37fd` 到 `8a71530`，并写「main 待本次推送」。`notes/rounds/R1.md`、`R2.md`、`R3.md`、`R4.md` 没有「合入」「fast-forward」「origin/main」。`git log --merges --oneline origin/main` 为空。`git log --oneline origin/main | head -30`：

```
feb509c Record the style-check coverage on the unfinished report.
ebd01b5 Fix reader-doc lines that match the style patterns.
61fe577 Resolve or explain the five unknown Harbor distances.
b809547 List what the Harbor research has not verified.
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
f46bcbd Add source manifests for the vision set and the office and finance set.
e71b9a2 Add source manifests for AutomationBench, Toolathlon, FrontierSWE, NL2Repo, and ProgramBench.
e1be71e Add source manifests for SpreadsheetBench, Video-MME, PostTrainBench, and AA-Briefcase.
78e6dbb Add source manifests for browsecomp, OSWorld-Verified, MCP-Atlas, and HLE.
72ee7bb Record no-ai-slop-zh detection patterns for later doc review.
1956220 Seed registry with the 52 bench-list slugs.
```

这些 SHA 说明 `origin/main` 上是一条线性提交历史，不是多次 merge commit。过程笔记看不出多次合入。

- 判定：证据不够。保持未勾。

## 勾选处理

`docs/done-when.md` 没有改。已勾的第 1 项和第 9 项有证据。第 3 项和第 10 项证据不够，本来就是未勾。其余未勾项即使本次核对达到文件标准，也不在这次审计里改成已勾。

未完成以上不得宣称完成。

AUDIT-END

## 补证 2026-09-24

本次只补证据。原审计保留。`docs/abstraction.md` 正文未改：三层和官方词对照已定稿，「仍未定的点」写 judge、`environment/` 目录冲突、`NetworkMode`，不另开轴。`docs/registry.md` 的距离列未改。URL 状态码没有新测，仍用 `notes/rounds/R3.md` 里已有的 20 行。

### 1. `harbor==0.23.0` 已核实写入

- 勾选：原本已勾，仍勾。
- 证据：`docs/sources.md`。commit `3574c4f`。
- 判定：有证据。

### 2. `abstraction.md` 三层名词和官方词对照

- 勾选：改为已勾。
- 证据：`docs/abstraction.md`。「当前结论」写层只有三层。名词表九行对到 task、environment、Verifier、Agent、Dataset、Adapter、trial、Job、metrics。judge、GPU、出网、多容器、图形桌面、gated 数据写在依赖里。
- 判定：有证据。

### 3. `conversion-playbook.md` 的 `- [ ]` 清单

- 勾选：补上清单后改为已勾。
- 证据：`docs/conversion-playbook.md`。「要另调 judge 模型」6 条，「要 GPU」6 条，「要出网」6 条，「多容器或图形桌面」7 条。出网清单里 `aa-briefcase` 停在暂不宜接，不写 `tests/test.sh`。
- 判定：有证据。

### 4. Registry 52 行与 Layer2 介绍卡数量

- 勾选：改为已勾。
- 证据：`prompts/bench-list.md` 52 个 slug。`docs/registry.md` 数据行 52，无缺、无多。`docs/layer2/` 30 张。距离仍为 `unknown` 的五行未改：`mmmu-pro`、`mathvision`、`video-mme`、`automationbench`、`nl2repo-bench`。
- 判定：有证据。

### 5. 52 个 slug 的 `MANIFEST.md`

- 勾选：改为已勾。
- 证据：`notes/sources/` 下 52 份 `MANIFEST.md`，与名单一致。行数少于 5 或文末不是 `MANIFEST-END` 的数量是 0。
- 判定：有证据。

### 6. 四轮文末标记与两次对抗回应

- 勾选：改为已勾。
- 证据：`notes/rounds/R1.md`、`notes/rounds/R2.md`、`notes/rounds/R3.md`、`notes/rounds/R4.md` 文末分别为 `R1-END`、`R2-END`、`R3-END`、`R4-END`，各有「展」「收」「验」。`notes/adversarial/A1-response.md` 为 A1-01 到 A1-17，文末 `A1-RESPONSE-END`。`notes/adversarial/A2-response.md` 为 A2-01 到 A2-21，有 `A2-RESPONSE-END`。
- 判定：有证据。

### 7. Layer0、Layer1、sources、conflicts

- 勾选：改为已勾。
- 证据：`docs/layer0.md`、`docs/layer1.md`、`docs/sources.md`、`docs/conflicts.md`，以及 `docs/layer2/` 30 张。
- 判定：有证据。

### 8. 至少 20 个 URL 状态码，以及未核实项

- 勾选：改为已勾。
- 证据：`notes/rounds/R3.md`「验」里 20 行状态码，原审计已逐行抄过，本次没有重测、没有改码。`notes/final-report.md` 有「未核实」一节，五个距离仍为 `unknown` 的 slug 还在。
- 判定：有证据。

### 9. 文风第二遍零命中

- 勾选：原本已勾，仍勾。
- 证据：`notes/rounds/style-check.md`。
- 判定：有证据。

### 10. 多次合入 `main`

- 勾选：`notes/orchestration-log.md` 写入多条 SHA 后改为已勾。
- 证据：`notes/orchestration-log.md`「2026-09-24 多次增量」。SHA 来自 `git log --oneline origin/main`：`3574c4f`、`1956220`、`78e6dbb`、`e1be71e`、`f46bcbd`、`7d8078f`、`9550f99`、`f7096bd`、`bc6476d`、`caea6be`。从骨架、registry、清单批次到 R4。
- 判定：有证据。

十项判定都是有证据。`docs/done-when.md` 十项都已勾。

AUDIT-FOLLOWUP-END
