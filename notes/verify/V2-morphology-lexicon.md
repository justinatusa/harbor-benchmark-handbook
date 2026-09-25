# V2 形态词表

轴数仍是 3。材料是 `notes/verify/v2/` 的 01 到 10，以及 `notes/verify/V1-abstraction-axes.md`。登记仍是 52 行。这次收束官方词和形态，不把 52 题写成已经抽象完。tool、runtime、function calling、grader、episode 不升成轴。

三层仍是 task、运行、接入。task 是 instruction、environment、verifier。运行是 agent、trial、job。接入是 adapter 只生成目录，dataset 列 task。

## 官方词对照

- agent。运行。完成 task 的程序。回路在 environment 里面还是外面，写在 agent 上，不单列类型。
- environment。task。题目目录里的 `environment/`。trial 或 job 上的 `environment.type` 是同一个词的选择位置，不是另一层。
- sandbox。task。和 environment 同一个名字。文档里的 sandbox 和 CLI 里的 environment 是同一个东西。不新造词。
- verifier。task。评估 agent 的工作并产出 reward。
- task。task。层名就是这个词。一条或多条 instruction、一个 environment，外加一个 verifier。
- trial。运行。一个 agent 对一个 task 的一次尝试。一道题一次运行是 trial。
- job。运行。一组 trial。一批 task 仍叫 dataset。job 把 task 再乘上 agent 和 `n_attempts`。没有把「一道题一次运行」和「一批题」收成一个词。

MCP 不单开一层。写在 task 的 environment，键是 `[[environment.mcp_servers]]`，也写在运行的 agent 配置。不是接入。

## 不是官方组件名

- runtime。01：Harbor 0.23.0 笔记里没有这个词。笔记没有写它等于 sandbox，也没有写它等于 agent。
- function calling。01：Harbor 0.23.0 笔记里没有这个词，不落到某一层。02：两份笔记都没有这个短语。安装包里它只出现在 ATIF `tool_definitions` 的 schema 说明。不升成轴。
- grader。01：Harbor 0.23.0 笔记里没有这个词。笔记没有写它和 verifier 或 judge 是同一个词。
- episode。01：Harbor 0.23.0 笔记里没有这个词，也没有把它和 trial 写成同一个词。10：tag `v0.23.0` 的 SFT 页和 Terminus-2 页有这个词，安装包把 `episodes` 当作 `max_turns` 的别名。概念列表没有 episode。它留在一次 trial 里面。不单开轴，不升成组件名。
- tool。02：没有组件名。两份官方笔记没有 tool 的组件定义。短语 tool calls、tools 挂在已有名词上。不升成轴。

## 形态

桌面题用 environment。不新造中文轴名。图形桌面留在依赖里。客机是镜像里的 QEMU，写在 environment 格里。多容器数的是 compose，或桌面 VM 之外的应用容器。sandbox 仍是这个 environment 的文档叫法。

judge 仍是 verifier 脚本里的依赖。Harbor 没有 judge 类型。另调模型发生在 tests 脚本里，再把返回收成数字，写入 reward 文件。`VerifierResult` 只有数字 rewards。不单列类型。

GPU 和出网是 environment 字段。GPU 写入 `gpus`，上游写了型号就写入 `gpu_types`。出网写入 `network_mode`。缺字段不改写成不需要显卡或不需要出网。

07 点名缺这些字段的 slug：

- `posttrainbench-v1-1`。没有 `gpus`、`gpu_types`、`cpus`、`memory_mb`、`storage_mb`、`network_mode`、`NetworkMode`、`allowed_hosts`。blocker。
- `browsecomp`。没有 `gpus`、`gpu_types`、`network_mode`、`NetworkMode`、`allowed_hosts`、`cpus`、`memory_mb`、`storage_mb`。blocker。
- `spreadsheetbench`。没有 `gpus`、`gpu_types`、`cpus`、`memory_mb`、`storage_mb`、`NetworkMode`、`allowed_hosts`。`network_mode` 只出现在「`jupyter.py` 里 `containers.run` 没有 `network_mode`」，出网记 unknown。缺 `gpus`，blocker。
- `automationbench`。没有 `gpus`、`gpu_types`、`network_mode`、`NetworkMode`、`allowed_hosts`、`cpus`、`memory_mb`、`storage_mb`。blocker。距离保持 unknown，不升档。

## 已有 task.toml

`swe-atlas` 保持重改造。Harbor 版本是 v0.18.0，不是 0.23.0。登记和介绍卡都是重改造。能读入不改版本。

`deepswe-v1-1` 不是原生可接。没有 v1.1 tag，`main` 上的 `task.toml` 不能当成 v1.1。登记和介绍卡都是轻适配。

`mls-bench-lite` 的 MANIFEST 写了 `harbor/tasks-docker/mls-bench__<id>/task.toml`，Harbor 版本写的是 0.6.6 和 0.22.0，没有写成 0.23.0。不写成原生可接。登记和介绍卡都是轻适配。

## 闭源走不通

08 的五题：`aa-briefcase`、`cursorbench`、`frontiercode-1-1`、`officeqa-pro`、`analystbench`。登记距离都是暂不宜接。共同形态是没有公开任务包。这五格里没有轻适配。

- `aa-briefcase`。无 git。正榜 91 题没有公开 git。题面私有。无评分表。正榜 rubric 没有公开 URL。
- `cursorbench`。无 git。不公开。任务、grader prompt、环境镜像没有下载。无评分。
- `frontiercode-1-1`。无 git。不公开。原文写不打算公开任务以免污染。无评分包。可运行的 rubric 和 runner 未抓取。
- `officeqa-pro`。gated。HF `databricks/officeqa`，`gated` 为 `auto`。评分脚本在公开仓，这一题的 blocker 不是无评分。题目 gated，写不出带题面的 `instruction.md`。
- `analystbench`。无 git。不公开。20 个任务和重建脚本没有下载地址。无评分表。要另外的 judge 模型，checklist 不在页上。

`cursorbench`、`frontiercode-1-1`、`officeqa-pro`、`analystbench` 在 playbook 里没有一条 `- [ ]` 能勾。清单走不通。

## blocker

`browsecomp`。07：缺上面那些 environment 字段，blocker。04 的形态能写上的是：environment 是脚本，该 commit 没有 Dockerfile 或 compose；verifier 另调模型；脚本要出网；agent 是单轮 `SamplerBase`，论文要求的浏览互联网不在这个脚本里。04 没有另起一行 blocker。

`nl2repo-bench`。距离保持 unknown，不当能接。09：项目页同时点名 OpenHands 镜像和 runtime 镜像。这一对没有被写成算多容器，也没有被写成不算。除这一对之外，多容器细节是 unknown。blocker。不补。

`agents-last-exam`。06：本地任务包 `ale-tasks-data.tar.gz` 是 gated（manual），约 202 GiB，未下载。6.8% 那一部分还缺模型名和提示词。暂不宜接的理由保持：本地任务包 gated，公开框架还要图形桌面。主路径是确定性程序分，整包不标成另调模型。

V1 写不清的格子没有在这里改成已填完。其余 slug 没有在这两份核对里填三格。

V2-END
