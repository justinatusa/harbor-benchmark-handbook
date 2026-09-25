# Harbor 0.23.0 薄抽象与转化手册

本仓库是 Harbor 0.23.0 钉选版薄抽象与转化手册的公开镜像。正文钉在 Origin tip `1976a2fdacc358ffaa207184fbca9409e78a638b`（`justin-2/benchmarkresearchanddesign`）。

## 阅读顺序

1. [组件抽象](docs/abstraction.md)
2. [导读](docs/layer0.md)
3. [Layer1 总表](docs/layer1.md)
4. [Registry](docs/registry.md)
5. [转化路径](docs/conversion-playbook.md)
6. 按需打开 [介绍卡](docs/layer2/)、[冲突](docs/conflicts.md)、[来源](docs/sources.md)、[Done-when 勾选](docs/done-when.md)

## 手册写什么

本手册给出三层轴与混类例子、轻适配与重改造的判定句、转化路径上的停句，以及各 benchmark 介绍卡。接入判断以 [Registry](docs/registry.md) 与 [组件抽象](docs/abstraction.md) 为准。

[转化路径](docs/conversion-playbook.md) 对缺材料的条目直接停句，不补写仓库里还没有的步骤。例子清单大约覆盖 8 个 slug，其余约 44 个不在该清单；出现在例子名单不等于距离档已核实。浏览暂不写入依赖列。[programbench](docs/layer2/programbench.md) 的距离记为 `unknown`。

## 文件

- [MANIFEST.txt](MANIFEST.txt) — 本镜像文件清单
- [待接入 Benchmark 名单](prompts/bench-list.md)

不含私有调研笔记与合同全文。
