# Harbor 接入判断手册（公开镜像）

本包导出 Origin 仓库 `justin-2/benchmarkresearchanddesign` 在 commit `225745ef690ed03f8ec679029f2531af78a8282a` 的读者路径。手册按 Harbor 0.23.0 写接入判断。

本公开镜像不含 `notes/`。转化清单里若出现 `notes/` 路径，该路径只指出处。文件打不开时，按该清单的停句停住。

本包不含调研合同全文。`prompts/bench-list.md` 开头指向同目录的 `harbor-unified-abstraction-research.md`，该文件不在本镜像中。slug 仍以 `prompts/bench-list.md` 为准。

## 阅读顺序

1. [组件抽象](docs/abstraction.md)
2. [导读](docs/layer0.md)
3. [Layer1 总表](docs/layer1.md)
4. [Registry](docs/registry.md)
5. [转化路径](docs/conversion-playbook.md)
6. 需要核对单题、冲突或版本出处时，再打开 [layer2](docs/layer2/)、[冲突](docs/conflicts.md)、[来源](docs/sources.md)

slug 名单在 [bench-list](prompts/bench-list.md)。

层只有三层。task 层是 instruction、environment、verifier。运行层是 agent、trial、job，由 metric 汇总。接入层是 adapter 生成目录、dataset 列出任务。与 Harbor 的距离只取原生可接、轻适配、重改造、暂不宜接；没有证据时写 unknown。

转化路径里的例子只覆盖 8 个 slug。出现在例子里，不等于距离档。核对上游时打开公开仓的钉死 commit。文件对不上就停。
