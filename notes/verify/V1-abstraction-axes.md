# V1 三层裁决

轴数是 3。材料是 `notes/verify/v1/` 的 01 到 10，以及 `docs/abstraction.md` 的当前结论。`docs/registry.md` 仍是 52 行。这次只收束轴，不把 52 题写成已经抽象完。09 和 10 各套了五题。下面六题的格子仍然写不清。其余 slug 没有在这两份笔记里填三格。

`docs/abstraction.md` 写的是「层只有三层，这里定稿，不多加」。judge 写在依赖里，原文是「grader / judge 不是新类型」，以及「不发明新轴、只写成依赖」。这篇没有「可以收成两层」，也没有把 judge 写成轴。读者文档不改。registry 距离不改。

## 三层

- task。instruction、environment、verifier。
- 运行。agent、trial、job。agent 在 environment 里做题。trial 是一次。job 是一批。
- 接入。adapter 只生成目录，dataset 列 task。job 不加载 adapter。

不能收成两层。

sandbox 不新造词，继续对应 environment。02 对准的原句是：「文档里的 sandbox 和 CLI 里的 environment 是同一个东西。」回路在 environment 里面还是外面，写在 agent 上，不单列类型。

## 每层删掉会混的两类

引用 `notes/verify/v1/01-collapse.md`。

删运行。剩下 task 和接入。混成一类的是：

- `browsecomp`。没有 agent 回路。01 的原句：「官方参考实现没有浏览器或 agent 循环。」
- `mcp-atlas`。有自己的多轮回路，不是 Harbor 的 trial/job。01 的原句：「`services/agent-harness/` 是 TypeScript 多轮循环，CHANGELOG 写 v2.0.0 从 Python harness 换过来。」

01 的收束句：删掉运行，会把没有 agent 回路的 `browsecomp` 和自带多轮 harness 的 `mcp-atlas` 混成一类。两边接入都是外部表，adapter 生成目录，dataset 再列。这盖不住有没有 agent。

删接入。剩下 task 和运行。混成一类的是：

- `terminal-bench-4-0`。已经是 dataset，运行就是 job。01 的原句：「正文给出 `harbor run -d terminal-bench/terminal-bench@4.0.0`」。
- `osworld-verified`。官方单位不是 task 目录。01 的原句：「任务 JSON 在 git 的 `evaluation_examples/`。」

01 的收束句：删掉接入，会把已经是 dataset 的 `terminal-bench-4-0` 和官方单位仍是 JSON 的 `osworld-verified` 混成一类。两边 task 都能写成 instruction、容器 environment、程序 verifier，运行也都能填上 agent、一次、一批。这盖不住目录是已经列好的，还是还要生成。

删 task。01 没有做这一组对照，这里不补一对 slug。前两处已经说明三层收不成两层。

## 不升轴的名单

judge、GPU、出网、多容器、图形桌面、四档距离。都不升成轴。

judge。03：Harbor 0.23.0 没有 judge 类型。程序比对和另调评判模型仍用 verifier 这个词，分开靠 playbook 的两条结束条件。

GPU、出网、多容器、图形桌面。07：建议轴数是 3，这四项留在依赖里。最不该加的是 GPU，同一块 H100 已经同时出现在原生可接和重改造里。

四档距离。距离是接入结论。06：允许值是 `原生可接`、`轻适配`、`重改造`、`暂不宜接`。`unknown` 在四档外面。四档不写进三层，也不写进名词对照表。登记里的距离格不改。

## tool 缺口

04 证明的是：不加 tool，会把「只聊天的题」和「要调外部工具的题」混成一类。只聊天的例子是 `aa-omniscience`、`browsecomp` 的参考实现、`hle` 的简单评测。要调外部工具的例子是 `mcp-atlas`、`toolathlon-verified`、`hle` 的 “Evaluating HLE-Diamond with tools”。

`tool` 先不升成第 4 根轴。04 把 tool 写进运行层，这一步 V1 不采纳。

V2 须用 Harbor 0.23.0 官方词核对 tool / MCP / function calling 落在哪一层。没有官方出处就不要写进 abstraction.md 当新轴。

## 过空的词

08 的结论是对照表过空。缺的官方词有三个，出处都在 08 已核对的笔记里，不在这里改写成中文轴名：

- judge。文档笔记官方用词有，对照表没有。
- Installed agent 与 External agent。文档笔记有，对照表只有 Agent。
- schema_version。两份笔记都有，对照表没有。安装包笔记里 task 默认 `"1.4"`，dataset、compile、exec 默认 `"1.0"`。

NetworkMode 不补进这列。08 写明文档笔记的官方用词节没有这个词。

这些词列在本篇。不在 `docs/abstraction.md` 里发明中文轴名。

## 写不清的 slug

09 和 10 写不清的是下面六个。每个只标缺的那一类。不改 registry 距离。

- `terminal-bench-4-0`。缺证据。09：有 environment，有 Harbor 的 agent 名，缺控制回路相对 environment 的位置。
- `browsecomp`。缺证据。09：缺浏览回路落在哪个进程。单轮 sampler 在本仓，浏览运行时是 unknown，而且没有 environment，内外两个位置都无处可写。
- `aa-briefcase`。缺证据。09：有 E2B sandbox，有框架名 Stirrup，缺的仍是控制回路相对 environment 的位置。
- `charxiv`。缺证据。10：缺这个调用在任务 environment 的里面还是外面。容器是 unknown，这句补不上。
- `spreadsheetbench`。缺证据。10：缺持有 ReAct 循环的进程在这些容器里面，还是外面。
- `nl2repo-bench`。缺证据。10：运行位置缺控制回路在任务容器的里面还是外面；接入方式缺 Harbor 侧的题单是 adapter 生成的 task 目录，还是一份 dataset 列表。Harbor 距离保持 unknown，不当能接。

09 里三格都写完的是 `osworld-verified`、`posttrainbench-v1-1`。10 里三格都写完的是 `mcp-atlas`、`swe-atlas`。09 写没有两题并成一类，所以不发明第四个组件名词。10 写轴不加，总数仍是 3。`swe-atlas` 的任务文件按 v0.18.0 写，本机安装包是 0.23.0，这不改成原生可接。

V1-END
