# 检查清单

这是对照 `prompts/harbor-unified-abstraction-research.md` 第 7 节留下的检查清单。它不是收工宣告。勾选不能当成手册已经做完。

过程里曾经把下列项全部打勾，审查后那些勾不能当完成证明。过程原文在 `notes/done-when.md`。本页不重复那些勾。

现在仍不能据此宣布做完：

- 转化路径盖住 8 个例子，不是 52 题的端到端步骤。文件对不上就停。
- Registry 距离列可以没有 `unknown`。这只表示每行落在某一档，不等于这些题都能接。
- 浏览没有写成 task、运行或接入里的单独一层。
- 介绍卡没有覆盖全部 52 个 slug。没有卡的题看 registry 距离，摘录在 `notes/sources/<slug>/`。

清单本身：

- [ ] `harbor==0.23.0` 已核实写入
- [ ] `abstraction.md`：组件层数少、名词稳、对齐官方语义
- [ ] `conversion-playbook.md`：按类型可照着做的检查清单（含 judge、GPU、出网、多容器）
- [ ] Registry 覆盖 `prompts/bench-list.md` 全表；重点 20～30 个有介绍卡
- [ ] 每个已深挖对象有 `notes/sources/<id>/MANIFEST.md`
- [ ] 至少 4 个完整大轮回；至少 2 次对抗审查，且每条攻击有回应
- [ ] Layer0、Layer1、必要的 Layer2、sources、conflicts
- [ ] 抽样至少 20 个链接核对；`notes/final-report.md` 列出未核实项
- [ ] `docs/` 通过文风抽查
- [ ] 过程中已多次合入 `main`；`notes/orchestration-log.md` 或 `notes/rounds/` 能看出增量合入

未完成以上不得宣称完成。合入 `main` 或公开仓库，也不等于上面各项已经做完。
