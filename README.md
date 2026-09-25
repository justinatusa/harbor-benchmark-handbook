# Harbor 0.23.0 薄抽象与转化手册（公开镜像）

来源 Origin tip：`1976a2fdacc358ffaa207184fbca9409e78a638b`（justin-2/benchmarkresearchanddesign）。

## 怎么读

先 `docs/abstraction.md` / `docs/layer0.md`，再 `docs/layer1.md`，再 `docs/registry.md`，再 `docs/conversion-playbook.md`，最后按需翻 `docs/layer2/` 介绍卡。

## 这份手册能做什么、不能做什么

- **能**：通读后做接入判断——三层轴与混类例子、轻适配/重改造怎么打勾、何处该停、哪些距离是 `unknown`。
- **不能**：当成端到端可照做的转化操作手册。`conversion-playbook` 里多条检查项已写明「本仓缺 …，停在这里、勿假装可照做」。
- **覆盖诚实**：例子大约盖住 8 个 slug，其余约 44 个不在那份例子清单里；52 题没有全部抽象完。出现在例子名单里 ≠ 距离档已核实可接。
- **浏览**：暂不写入依赖列；缺的是「浏览属于哪一层」的仓内句。勿自行升成新轴。
- **`programbench`**：距离是 `unknown`（原标轻适配但缺 `task.toml`，与仓内 08 规则冲突，勿当能接）。
- **不是收工证明**：本仓不是 Harbor 全项目 Done-when 全勾的证明，也不宣称 §7 已齐。

## 文件

见 `MANIFEST.txt`。不含私有调研笔记与合同全文。
