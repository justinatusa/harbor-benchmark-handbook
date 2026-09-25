# Harbor 接入判断手册

本仓按 Harbor 0.23.0 写接入判断。先用下面几页决定接不接、轻还是重。单题细节在介绍卡和 `notes/`。

不要提交 API Key。不含 `prompts/harbor-unified-abstraction-BACKGROUND.md`。

距离列里没有 `unknown`，不等于这些题都能接。转化路径不是端到端可照做的完整评测。`docs/done-when.md` 是检查清单，不是收工宣告。浏览没有单独落成一层。

## 阅读顺序

1. [组件抽象](docs/abstraction.md)
2. [导读](docs/layer0.md)
3. [Layer1 总表](docs/layer1.md)
4. [Registry](docs/registry.md)
5. [转化路径](docs/conversion-playbook.md)
6. 核对单题、冲突或版本时，打开 [介绍卡索引](docs/layer2/README.md)、[冲突](docs/conflicts.md)、[来源](docs/sources.md)
7. 深挖摘录、轮次和审查：[`notes/sources/`](notes/sources/)、[`notes/final-report.md`](notes/final-report.md)、[`notes/rounds/`](notes/rounds/)、[`notes/adversarial/`](notes/adversarial/)
8. [检查清单](docs/done-when.md)（不是收工宣告）
9. 名单与调研合同：[bench-list](prompts/bench-list.md)、[统一调研提示词](prompts/harbor-unified-abstraction-research.md)

层只有三层。task 层是 instruction、environment、verifier。运行层是 agent、trial、job，由 metric 汇总。接入层是 adapter 生成目录、dataset 列出任务。与 Harbor 的距离只取原生可接、轻适配、重改造、暂不宜接；没有证据时写 unknown。

转化路径里的例子只覆盖 8 个 slug。出现在例子里，不等于距离档。核对上游时打开公开仓的钉死 commit。文件对不上就停。
