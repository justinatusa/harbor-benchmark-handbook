# V3-08 意图面 1、2、3

材料是 `docs/abstraction.md`、`docs/layer0.md`、`notes/verify/V1-abstraction-axes.md`、`notes/verify/V2-morphology-lexicon.md`，以及它们点名的 `notes/verify/v1/`、`notes/verify/v2/`。不改 `docs/`。登记仍是 52 行。这篇只记这三面交了什么、哪一面还空。

## 1. 薄抽象钉 Harbor

缺口。

轴数是 3，没有超过 5。`docs/abstraction.md` 写「层只有三层，这里定稿，不多加」。三层是 task（instruction、environment、verifier）、运行（agent、trial、job）、接入（adapter 只生成目录，dataset 列 task）。`notes/verify/V1-abstraction-axes.md` 复述同一句，并写没有「可以收成两层」。`docs/layer0.md` 的地图是这九个词，不是第四层。

「每加一根写会混掉哪两类」只交了两根。

删运行。`notes/verify/v1/01-collapse.md` 写会把没有 agent 回路的 `browsecomp` 和自带多轮 harness 的 `mcp-atlas` 混成一类。原句分别是「官方参考实现没有浏览器或 agent 循环」和「`services/agent-harness/` 是 TypeScript 多轮循环」。两边接入都是外部表，盖不住有没有 agent。

删接入。同一篇写会把已经是 dataset 的 `terminal-bench-4-0` 和官方单位仍是 JSON 的 `osworld-verified` 混成一类。原句分别是「正文给出 `harbor run -d terminal-bench/terminal-bench@4.0.0`」和「任务 JSON 在 git 的 `evaluation_examples/`」。两边都能写成 instruction、容器 environment、程序 verifier，盖不住目录是已经列好的还是还要生成。

删 task。`notes/verify/V1-abstraction-axes.md` 写：「删 task。01 没有做这一组对照，这里不补一对 slug。」`notes/verify/v1/01-collapse.md` 的结论只收了前两处。task 这一层没有写出删掉之后会混掉的两个 slug。

没升上去的项写过另一类混法，填不上这个空。`notes/verify/v1/07-deps-not-axes.md` 写 GPU、出网、多容器、图形桌面若升成轴，会把距离不同的题收成同一格，所以留在依赖里。`notes/verify/v1/04-agent-tool-mcp.md` 写不加 tool 会把只聊天的题和要调外部工具的题混成一类，V1 不把 tool 升成第 4 根轴。这些是「不加」的记录。task 仍然没有自己的一对。

## 2. 官方形态压力

缺口。七项目录里有难样。浏览没有落到三层上。

容器。不是只对着 Terminal-Bench。`notes/verify/v2/04-no-adapter-exams.md` 对 `browsecomp`、`hle`、`charxiv`、`mmmu-pro`、`video-mme` 写「容器还是脚本」。`browsecomp` 该 commit 没有 Dockerfile 或 compose。`notes/verify/v1/09-apply-set-a.md` 把 `posttrainbench-v1-1` 写成 Apptainer `.sif`，把 `aa-briefcase` 写成 E2B sandbox。`notes/verify/v2/09-spreadsheet-repo.md` 写 `programbench` 一题一镜像、`vision2web` 一个 sandbox 镜像。这几题的登记距离不是原生可接。

桌面。`notes/verify/v2/05-desktop.md` 用 `osworld-verified` 的 QEMU（镜像 `happysixd/osworld-docker`）和 `osworld-2-0` 的桌面 VM 之外的应用容器。不写明时，会和 `terminal-bench-2-1` 那种一个 Docker image 的题混成一类。`notes/verify/v1/07-deps-not-axes.md` 另有 `agents-last-exam` 要桌面动作，距离是暂不宜接。

judge。`notes/verify/v1/03-verifier-judge.md` 核对安装包没有 Judge 类，`VerifierResult` 只有数字 rewards。程序比对用 `spreadsheetbench`，另调模型用 `charxiv`、`gdpval-aa-v2-1`。`notes/verify/v2/06-judge-morphology.md` 再对 `aa-briefcase`、`agents-last-exam`、`draco`。`aa-briefcase` 停在任务不公开，不写 `tests/`。

出网。`notes/verify/v1/07-deps-not-axes.md` 用 `browsecomp` 必须访问的主机，对照 `terminal-bench-2-1` 允许出网（原生可接）和 `aa-briefcase` 容器没有出站（暂不宜接）。`notes/verify/v2/07-gpu-network.md` 对 `posttrainbench-v1-1`、`browsecomp`、`spreadsheetbench`、`automationbench` 逐个查 `network_mode`。缺字段记 blocker，不改写成不需要出网。

GPU。`notes/verify/v1/07-deps-not-axes.md` 写同一块 H100 同时出现在原生可接（`mls-bench-lite`、`terminal-bench-4-0`）和重改造（`posttrainbench-v1-1` 的 `apptainer exec --nv`）。`notes/verify/v2/07-gpu-network.md` 写 `num_gpus` 对不上 `gpus`，记 blocker。

多容器。`notes/verify/v1/07-deps-not-axes.md` 用 `terminal-bench-4-0` 已有 compose 的题，对照 `spreadsheetbench` 两个镜像、清单没有 service 名。`notes/verify/v2/05-desktop.md` 把 `osworld-2-0` 的网站应用容器算在桌面 VM 外面。`notes/verify/v2/09-spreadsheet-repo.md` 写 `nl2repo-bench` 的 OpenHands 镜像和 runtime 镜像这一对没有被判成算或多容器，也没有被判成不算，blocker。距离保持 unknown。

数据不公开。`notes/verify/v2/08-closed-gated.md` 五题：`aa-briefcase`、`cursorbench`、`frontiercode-1-1`、`officeqa-pro`、`analystbench`。登记距离都是暂不宜接。共同形态是没有公开任务包。`cursorbench`、`frontiercode-1-1`、`officeqa-pro`、`analystbench` 在 playbook 里没有一条 `- [ ]` 能勾。

浏览没有这一格。点名的标本是 `browsecomp`。`notes/verify/v1/09-apply-set-a.md` 写运行回路写不清：本仓没有浏览器，也没有 agent 循环；缺浏览回路落在哪个进程；没有 environment，内外两个位置都无处可写。`docs/conversion-playbook.md`「要另调 judge 模型」的坑写：参考实现没有浏览器，只接 grader 时浏览仍是 unknown。`notes/verify/v2/04-no-adapter-exams.md` 把形态写成单轮 `SamplerBase`，并写论文要求的浏览互联网不在这个脚本里；该篇没有另起一行 blocker。`notes/verify/V2-morphology-lexicon.md` 写 V1 写不清的格子没有改成已填完。`notes/verify/v2/09-spreadsheet-repo.md` 里 `vision2web` 的 `playwright-cli` 记在 verifier，是给生成页面做功能分，不是把浏览回路放进 environment 或 agent。三层因此没有一组「有浏览器的题 / 没有浏览器的题」可以对照。登记压力列写「题目要浏览互联网」（`docs/registry.md` 的 `browsecomp` 行），格子本身仍空着。

## 3. 关键词

已交证据。

十一个词都在 `notes/verify/v2/01-lexicon.md` 对过 Harbor 0.23.0 的两份笔记：`notes/rounds/r1-package-map.md`、`notes/rounds/r1-docs-nouns.md`。文档站未标版本。一个词不在这两份里，该篇就写笔记里没有这个词。

落到现有层上的：

- agent。运行。完成 task 的程序。回路在 environment 里面还是外面，写在 agent 上。出处是文档笔记的 core-concepts 与 custom-agents，以及安装包笔记 `agents/base.py`。
- environment。task。题目目录 `environment/`，trial 或 job 的 `environment.type` 是同一个词的选择位置。
- sandbox。task。和 environment 同一个名字。文档笔记写 CLI `--env` 和 `environment.type` 把 sandbox 叫成 environment。
- verifier。task。评估 agent 的工作并产出 reward。安装包笔记源文件 `verifier/verifier.py`。
- task。层名就是这个词。一条或多条 instruction、一个 environment，外加一个 verifier。
- MCP。不单开一层。文档笔记是 `[[environment.mcp_servers]]`。安装包笔记在 `models/task/config.py` 有 MCPServerConfig，在 `models/trial/config.py` 的 AgentConfig 另有 `mcp_servers`。`notes/verify/v2/02-tool-mcp.md` 写两处是同一份配置的两个挂载点，不是接入。

V2 说不是 Harbor 组件名的五个，对照也在，而且不是只写「没有」：

- runtime。`notes/verify/v2/01-lexicon.md` 写两份笔记没有这个官方词。`notes/rounds/r1-docs-nouns.md` 小标题「新 sandbox / 新 runtime」下一句是继承 `BaseEnvironment`，出处 `https://docs.harborframework.com/core-concepts/sandboxes/custom-sandboxes`。笔记没有写 runtime 等于 sandbox，也没有写它等于 agent。
- tool。`notes/verify/v2/02-tool-mcp.md` 写两份官方笔记没有 tool 的组件定义。短语挂在 ATIF 的 tool calls 和 ASP 的 tools 上。安装包 `models/trajectories/tool_call.py` 是轨迹字段，类说明是 `A tool call within a step.` 没有名为 tool 的组件。不升成轴。
- function calling。`notes/verify/v2/01-lexicon.md` 写两份笔记没有这个短语，不落到某一层。`notes/verify/v2/02-tool-mcp.md` 写安装包里它只出现在 `models/trajectories/agent.py` 的 `tool_definitions` 字段说明，原文是 OpenAI's function calling schema。不升成轴。
- grader。`notes/verify/v2/01-lexicon.md` 写两份笔记没有这个词，也没有把它写成 verifier 或 judge。`docs/abstraction.md` 的种子名 grader / judge，文档站用来评估 agent 的词是 Verifier。那是读者文档里的种子，不是这两份笔记里的组件名。
- episode。`notes/verify/v2/01-lexicon.md` 写两份笔记没有这个词，也没有把它和 trial 写成同一个词。`notes/verify/v2/10-trial-job.md` 补了笔记没抄到的页：tag `v0.23.0` 的 SFT 页有 `agent/episode-*`，Terminus-2 页把 `max_turns` 注释写成 Maximum number of episodes；安装包 `agents/terminus_2/terminus_2.py` 把 `episodes` 当作 `max_turns` 的别名。当前文档站概念列表没有 episode。它留在一次 trial 里面。不单开轴，不升成组件名。`notes/verify/V2-morphology-lexicon.md` 把这五个都收成「不是官方组件名」。

V3-08-END

## 主控裁决

缺口 1 成立。task 这一层没有删掉之后会混掉的两个 slug。`notes/verify/V1-abstraction-axes.md` 写「01 没有做这一组对照，这里不补一对 slug」。`docs/abstraction.md` 只有「层只有三层，这里定稿，不多加」，没有可以抄进去的那一对。本轮不改 docs。应进 `notes/verify/V1-abstraction-axes.md` 的「每层删掉会混的两类」。

缺口 2 成立。浏览没有落到三层上。`docs/conversion-playbook.md` 已写「只接 grader 时，浏览仍是 unknown」。`notes/verify/V2-morphology-lexicon.md` 写「V1 写不清的格子没有在这里改成已填完」。没有一句现成说明能把浏览放进 task、运行或接入。本轮不改 docs。应进 `notes/verify/V2-morphology-lexicon.md` 的形态收束。

意图 3 不是缺口。不改 docs。

仍缺 slug 证据。浏览落层仍无依据。
