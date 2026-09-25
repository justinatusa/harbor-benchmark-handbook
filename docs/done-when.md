# Done-when 勾选

对照 `prompts/harbor-unified-abstraction-research.md` 第 7 节。没勾上的项不能当成做完。勾选旁要有文件路径、commit 或抽样记录。

- [x] `harbor==0.23.0` 已核实写入（`docs/sources.md`；命令 `harbor --version` 与包元数据均为 0.23.0；commit `3574c4f`）
- [x] `abstraction.md`：组件层数少、名词稳、对齐官方语义的说明齐全（`docs/abstraction.md`）
- [x] `conversion-playbook.md`：按类型可照着做的检查清单（含 judge / GPU / 出网 / 多容器等已发现类型）（`docs/conversion-playbook.md`）
- [x] Registry 覆盖 `prompts/bench-list.md` 全表；重点 20～30 个有介绍卡（`docs/registry.md`，`prompts/bench-list.md`，`docs/layer2/`）
- [x] 每个已深挖对象有 `notes/sources/<id>/MANIFEST.md`（`notes/sources/`）
- [x] 至少 4 个完整大轮回；至少 2 次对抗审查，且每条攻击有回应（`notes/rounds/R1.md`，`notes/rounds/R2.md`，`notes/rounds/R3.md`，`notes/rounds/R4.md`，`notes/adversarial/A1-response.md`，`notes/adversarial/A2-response.md`）
- [x] Layer0、Layer1、必要的 Layer2、sources、conflicts（`docs/layer0.md`，`docs/layer1.md`，`docs/layer2/`，`docs/sources.md`，`docs/conflicts.md`）
- [x] 抽样至少 20 个链接核对；`notes/final-report.md` 列出未核实项（`notes/rounds/R3.md`，`notes/final-report.md`）
- [x] `docs/` 通过文风抽查：`no-ai-slop-zh` 具名模式清零或已改；无套话、无自创词、无未定义缩写（`notes/verify/V-final.md` 文风抽查；`notes/rounds/style-check.md`）
- [x] 过程中已多次合入 `main`；`notes/orchestration-log.md` 或 `notes/rounds/` 能看出增量合入（`notes/orchestration-log.md`）

未完成以上不得宣称完成。大纲、空表、只有官方地图、只有试点、没有对抗回应，都不算完成。

允许停下的情况只有：上面每一项都有证据；或写出具体 blocker 并继续做不依赖它的部分；或用户明确 pause / stop。
