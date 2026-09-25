# V-final

轴、词、覆盖、意图面的收束。§7 的文风项本轮已勾，不把清单写成全项目完成。52 题没有全部抽象完。例子仍是 8 个 slug，其余 44 个不在清单里。本轮只把 `programbench` 的距离从轻适配改为 `unknown`。

## 轴

最终 3 根。没有第 4 根。`docs/abstraction.md`：「层只有三层，这里定稿，不多加。」

每一根都要写没有它会混掉哪两类。`docs/abstraction.md` 里已有 slug 的，只引用那句。

1. task。没有它会把 `terminal-bench-2-1` 和 `posttrainbench-v1-1` 混掉。`docs/abstraction.md` 原句：「删掉 task 层会把 `terminal-bench-2-1` 和 `posttrainbench-v1-1` 混掉。「89 个终端环境任务，每题有独立环境」，「每个任务是一个基座加一个下游基准」。这只说明任务粒度不同，不是距离档。」前半句在 `notes/sources/terminal-bench-2-1/MANIFEST.md`，后半句在 `notes/sources/posttrainbench-v1-1/MANIFEST.md`。这只是任务粒度，不是距离档。

2. 运行。已写入 `docs/abstraction.md`：「删掉运行层会把 `browsecomp` 和 `mcp-atlas` 混掉。`notes/sources/browsecomp/MANIFEST.md`：「官方参考实现没有浏览器或 agent 循环。」`notes/sources/mcp-atlas/MANIFEST.md`：「`services/agent-harness/` 是 TypeScript 多轮循环，CHANGELOG 写 v2.0.0 从 Python harness 换过来。」」两句都在对应清单里逐字出现。不记「混类原句对不上」。

3. 接入。已写入 `docs/abstraction.md`：「删掉接入层会把 `terminal-bench-4-0` 和 `osworld-verified` 混掉。`notes/sources/terminal-bench-4-0/MANIFEST.md`：「正文给出 `harbor run -d terminal-bench/terminal-bench@4.0.0`，以及 Harbor Hub URL `https://hub.harborframework.com/datasets/terminal-bench/terminal-bench/4`。」`notes/sources/osworld-verified/MANIFEST.md`：「任务 JSON 在 git 的 `evaluation_examples/`。」」`osworld-verified` 这句在清单里逐字出现。`terminal-bench-4-0` 用的是清单整句。`notes/verify/V1-abstraction-axes.md` 的引号停在命令后面，少了「，以及 Harbor Hub URL …」。读者文档用清单整句。slug 对得上。不记「混类原句对不上」。

judge、GPU、出网、多容器、图形桌面、gated 数据在 `docs/abstraction.md` 写成依赖，不新加轴。浏览只有停句，没有升成第 4 根轴。见下面的「浏览」。

## 关键词

只写仓内已有对照。没有另造一层。

| 词 | 落到 | 仓内句子 |
|---|---|---|
| agent | 运行 | `notes/verify/v2/01-lexicon.md`：「落在运行。」`docs/abstraction.md` 名词表：Agent。 |
| environment | task | `notes/verify/v2/01-lexicon.md`：「落在 task。」`docs/abstraction.md`：「文档里的 sandbox 和 CLI 里的 environment 是同一个东西。」 |
| runtime | 不是组件名 | `notes/verify/v2/01-lexicon.md`：「笔记没有写 runtime 等于 sandbox，也没有写 runtime 等于 agent。」 |
| sandbox | task | `notes/verify/V2-morphology-lexicon.md`：「sandbox。task。和 environment 同一个名字。」 |
| tool | 不是组件名 | `notes/verify/V2-morphology-lexicon.md`：「tool。02：没有组件名。」不升成轴。 |
| MCP | 不单开一层 | `notes/verify/V2-morphology-lexicon.md`：「MCP 不单开一层。写在 task 的 environment，键是 `[[environment.mcp_servers]]`，也写在运行的 agent 配置。不是接入。」 |
| function calling | 不是组件名 | `notes/verify/v2/01-lexicon.md`：「Harbor 0.23.0 笔记里没有这个词，不落到某一层。」`notes/verify/v2/02-tool-mcp.md` 只把它记在 `tool_definitions` 的 schema 说明：OpenAI's function calling schema。 |
| grader | 不是组件名 | `notes/verify/v2/01-lexicon.md`：「Harbor 0.23.0 笔记里没有这个词。」`docs/abstraction.md` 种子写 grader / judge 不是新类型，文档站用来评估 agent 的词是 Verifier。那是种子，不是组件名。 |
| verifier | task | `docs/abstraction.md` 名词表：Verifier。产出 reward。 |
| task | task | `notes/verify/v2/01-lexicon.md`：「层名就是这个词。」 |
| episode | 不是组件名 | `notes/verify/v2/10-trial-job.md`：「episode 留在一次 trial 里面。不单开轴。」当前文档站概念列表没有 episode。 |

十一个词都有仓内对照。没有标成缺词的项。

## 覆盖

盖住的是 playbook 例子里的 8 个。`docs/layer0.md` 照抄：`spreadsheetbench`、`posttrainbench-v1-1`、`osworld-verified`、`charxiv`、`browsecomp`、`aa-briefcase`、`deepswe-v1-1`、`swe-bench-pro`。

盖不住的是其余 44 个。`notes/verify/v3/09-intent-4-6.md` 列出：`gdpval-aa-v2-1`、`agents-last-exam`、`draco`、`onemillion-bench`、`spreadsheetbench-2`、`analystbench`、`officeqa-pro`、`officeqa-pro-v2`、`finance-agent-v2`、`apex-agents`、`frontier-finance`、`big-finance-bench`、`osworld-2-0`、`gdp-pdf`、`mmmu-pro`、`omnidocbench`、`babyvision`、`perception-bench`、`zerobench`、`chartography`、`vision2web`、`benchcad`、`3dcodebench`、`mathvision`、`video-mme`、`automationbench`、`toolathlon-verified`、`mcp-atlas`、`terminal-bench-4-0`、`frontierswe-v2`、`nl2repo-bench`、`terminal-bench-2-1`、`programbench`、`swe-marathon`、`swe-atlas`、`mls-bench-lite`、`frontiercode-1-1`、`cursorbench`、`sec-bench-pro`、`exploitgym`、`hle`、`critpt`、`aa-omniscience`、`aa-lcr-v1-1`。

原因：`docs/conversion-playbook.md` 开篇写例子只来自本轮打开过的 MANIFEST。`docs/layer0.md` 与 `notes/final-report.md` 都写其余 44 个不在这份清单里。52 题没有全部抽象完。

`swe-bench-pro` 在上面 8 个里。这不等于距离档已有判定。登记格仍是原生可接。本篇不改格。

## 意图面 1–9

| 面 | 终态 |
|---|---|
| 1 | 已交。`docs/abstraction.md`「层只有三层」；task 混类句在同一文件，并写明只是任务粒度，不是距离档。运行与接入的混类原句已在同一文件，路径见上面「轴」。 |
| 2 | 停句已交，落层仍缺口。`docs/abstraction.md`：「浏览暂不写入依赖列。缺的是「浏览属于哪一层」的仓内句。读者勿自行升成新轴。」 |
| 3 | 已交。上表十一词。路径是 `notes/verify/v2/01-lexicon.md`、`notes/verify/V2-morphology-lexicon.md`、`docs/abstraction.md`。 |
| 4 | 已交。`docs/layer1.md` 与 `docs/abstraction.md`：「轻适配。官方或仓内已有可对上的 Harbor task 形态：有 task 目录，或 MANIFEST、介绍卡里已写出的等价证据。」「重改造。需要新写或大改 task、环境或评分回路。」 |
| 5 | 部分已交。pytest 那条仍点名 `notes/sources/spreadsheetbench/MANIFEST.md`、`notes/sources/osworld-verified/MANIFEST.md`、`notes/sources/posttrainbench-v1-1/MANIFEST.md`。要 GPU、要出网、多容器的勾选，以及 judge 节里已标不可执行的勾选，在 `docs/conversion-playbook.md` 补了停句。不宣称能跑通完整评测。 |
| 6 | 已交。`docs/layer0.md` 与 `notes/final-report.md` 写例子盖住 8 个，其余 44 个不在清单里，52 题没有全部抽象完。 |
| 7 | 部分已交。`swe-marathon`、`frontierswe-v2` 以及 `browsecomp`、`hle`、`charxiv`、`mmmu-pro`、`video-mme` 的压力列已写依据和为何保持现档。距离格未改。未点名的其余 slug 仍没有这句。已合 `main` 不顶替。 |
| 8 | 部分已交。本轮 1～5 在 `notes/orchestration-log.md` 各写了一句改进了读者手册的哪一块，或写明哪一块没有新句子。更早的增量列表仍是提交标题。已勾的「多次合入 main」不拿来挡。 |
| 9 | 已交。抽查命中 0，见「文风抽查」。`docs/done-when.md` 文风项已勾。其他勾选未改。 |

## playbook 7 条

对照 `notes/verify/v3/06-playbook-walk.md`，以及 `473ab21`、`141e886` 改过的勾选。pytest 那条仍点名三份清单，没有回退。judge 节里已标不可执行的勾选补了「本仓缺 …，停在这里、勿假装可照做」。要 GPU、要出网、多容器的勾选同样补了停句，点名仓内摘录或清单，缺文件的不写成可跑。不宣称能跑通完整评测。

1. pytest。结束条件是停住。缺的是 pytest 路径和 Harbor task 的 `tests/test.sh`。抽查时原句只写「本轮打开的清单」和「命令输出」，没有点名文件或命令。就地改成：`notes/sources/spreadsheetbench/MANIFEST.md`、`notes/sources/osworld-verified/MANIFEST.md`、`notes/sources/posttrainbench-v1-1/MANIFEST.md` 都没有 pytest 这个词，也没有 `test_*.py` 的路径；工作区没有 `tests/test.sh`。本轮打开这三份清单，没有 pytest；`tests/test.sh` 不在工作区。

2. 打开评分脚本。不可执行。缺 `src/descriptive_utils.py`、`simple_evals.py`、两份 `evaluate.py`。本轮这三个路径都不在工作区。同仓没有 `JUDGE_MODEL` 的五个脚本名留在第一节，这一句不把整条变成可执行。

3. 两份密钥。不可执行。缺两份密钥的路径。`notes/sources/charxiv/MANIFEST.md` 写「没有 OpenAI key」。本轮对上这一句：「未跑 `generate.py` / `evaluate.py`，没有 OpenAI key。」

4. 打开 `tests/test.sh`。不可执行。缺被点名的 task 目录，以及这份 `tests/test.sh`。本轮工作区没有 `tests/test.sh`。

5. Harbor 0.23.0 解释器。结束条件是输出第一行 `False`、第二行 `['rewards']`，或者 `import harbor` 失败就停。本轮执行该命令，`ModuleNotFoundError: No module named 'harbor'`。停在这一步。

6. 拿掉 judge 密钥再跑评分脚本。不可执行。缺评分脚本、judge 密钥、退出码、运行后的目录。`notes/sources/charxiv/MANIFEST.md` 写未跑 `evaluate.py`、没有 OpenAI key。本轮 `src/evaluate.py` 不在工作区，清单句对得上。

7. `charxiv` 改用 val。不可执行。缺公开 JSON，也没有改成使用 val 的 task。`notes/sources/charxiv/excerpt.md` 写「未把 JSON 复制进本目录」。本轮对上这一句。

## 距离为 unknown 的行

`docs/registry.md` 里「与 Harbor 距离」为 `unknown` 的有六行：`mmmu-pro`、`mathvision`、`video-mme`、`automationbench`、`nl2repo-bench`、`programbench`。

前五题的 blocker 仍是清单没写评测是否不要 GPU。`nl2repo-bench` 另有「还没写死两个镜像算不算多容器」。这五格本轮不改。

`programbench` 本轮从轻适配改为 `unknown`。`docs/registry.md` 压力列：「原标轻适配但缺 task.toml，与 08 规则冲突，勿当能接。」`docs/layer2/programbench.md` 写同一档。MANIFEST 没有写明需要新写或大改 task、环境或评分，距离因此停在 `unknown`。

前五题压力列都有「勿当能接」，blocker 都是清单没写评测是否不要 GPU。`nl2repo-bench` 另有「还没写死两个镜像算不算多容器」。`mathvision` 行另有「Qwen-VL 脚本的设备要求没有打开」。`automationbench` 行另有「且运行不是多容器」。这三处多出来的字不改距离格。

GPU 这五题的句子还在：

- `docs/layer0.md` 仍有「这五题勿当能接：`mmmu-pro`、`mathvision`、`video-mme`、`automationbench`、`nl2repo-bench`」，同段接了 `programbench` 缺 `task.toml`。
- `docs/registry.md` 表前仍有这五题的 GPU 句，下一句是 `programbench` 的 `unknown`。
- `notes/final-report.md` 未核实名单里有这六行。

`programbench` 是第六个 `unknown`。

## 浏览

停句已交。落层仍缺口。

`docs/abstraction.md`：「浏览暂不写入依赖列。缺的是「浏览属于哪一层」的仓内句。读者勿自行升成新轴。」

仓内没有一句把浏览写成 task、运行或接入某一层的依赖。缺依据的例子仍是 `docs/conversion-playbook.md`「只接 grader 时，浏览仍是 unknown」，以及 `notes/sources/browsecomp/MANIFEST.md`「官方参考实现没有浏览器或 agent 循环」。这两句没有改写成已经落层。没有升成第 4 根轴。

## 面 7

`swe-marathon`。仓内有 `task.toml` 记录。`notes/sources/swe-marathon/MANIFEST.md`：「出网: 不一致，按任务写在 `task.toml`。」同文件：「官方运行说明用 Harbor CLI。钉死 README 写安装 `harbor[modal]==0.20.0`。」原文没有写明这是 Harbor task。`docs/registry.md` 距离格仍是重改造。压力列已写这句不升档。

`frontierswe-v2`。仓内有 `task.toml` 记录。`notes/sources/frontierswe-v2/MANIFEST.md`：「17 份 `task.toml` 里只有 `frogsgame-rl` 和 `pcqm4mv2-autoresearch` 是 `allow_internet = true`」。同文件写这个 commit 里有 `harbor_ext/`。原文没有写明这是 Harbor task。`docs/registry.md` 距离格仍是暂不宜接。压力列已写这句不升档。

`notes/verify/v2/04-no-adapter-exams.md` 点名、且本轮写进压力列的是 `browsecomp`、`hle`、`charxiv`、`mmmu-pro`、`video-mme`。每句写依据这份笔记和该 slug 的 `notes/sources/<slug>/MANIFEST.md`，缺的是先读 Harbor 官方再归类的记录，所以距离保持现档。距离格未改。`browsecomp` 与 `charxiv` 保持重改造，`hle` 保持暂不宜接，`mmmu-pro` 与 `video-mme` 保持 `unknown`。

`notes/verify/v2/03-existing-harbor-files.md` 只核了 6 个有 `task.toml` 的 slug，没有 `swe-marathon` 和 `frontierswe-v2`。未点名的其余 slug 仍没有同样的一句。已合 `main` 不顶替这一缺口。不把面 7 写成全齐。

下面 1–7 是上一轮记录。轻/重判定、浏览停句、文风抽查的现况见「修补」。

## 本轮 1–7

1. 已交。`docs/abstraction.md`：「删掉运行层会把 `browsecomp` 和 `mcp-atlas` 混掉。」原句路径是 `notes/sources/browsecomp/MANIFEST.md`、`notes/sources/mcp-atlas/MANIFEST.md`。同文件：「删掉接入层会把 `terminal-bench-4-0` 和 `osworld-verified` 混掉。」原句路径是 `notes/sources/terminal-bench-4-0/MANIFEST.md`、`notes/sources/osworld-verified/MANIFEST.md`。task 层那句未改，仍写只是任务粒度，不是距离档。

2. 上一轮记成缺口。现况见「浏览」和「修补」：停句已写入 `docs/abstraction.md`，落层仍缺仓内句。

3. 上一轮记成缺口，当时 `programbench` 仍是轻适配。现况见「修补」：判定句已写入 `docs/layer1.md` 与 `docs/abstraction.md`，该行距离已改为 `unknown`。

4. 已交停句，不宣称可跑通完整评测。`docs/conversion-playbook.md` 要 GPU、要出网、多容器的勾选，以及 judge 节里已标不可执行的勾选，写了「本仓缺 …，停在这里、勿假装可照做」，并点名仓内已有的摘录或清单。pytest 那条仍点名三份 MANIFEST。

5. 部分已交。压力列句子在 `docs/registry.md` 的 `swe-marathon`、`frontierswe-v2`、`browsecomp`、`hle`、`charxiv`、`mmmu-pro`、`video-mme`。距离格未改。未点名的其余 slug 仍没有这句。

6. 已交本轮这五句。`notes/orchestration-log.md`「2026-09-25 读者手册」各写了改进了哪一块，或写明哪一块没有新句子。更早的列表仍是提交标题。

7. 覆盖句未改。`docs/layer0.md` 与 `notes/final-report.md` 仍是例子盖住 8 个 slug，其余 44 个不在这份清单里，52 题没有全部抽象完。这两份里没有「出现在例子名单不等于距离档已有判定」。这句留在本篇「覆盖」和 `notes/verify/V3-coverage-and-intent.md`。不抬覆盖。`swe-bench-pro` 在 8 个例子里不等于距离档已有判定，登记格仍是原生可接。本篇不改格。

## 文风与 §7

文风项已勾。抽查见下。不把 §7 写成全项目完成。52 题没有全部抽象完。

## 修补

A 已交。判定句在 `docs/layer1.md`，同一句在 `docs/abstraction.md`：「轻适配。官方或仓内已有可对上的 Harbor task 形态：有 task 目录，或 MANIFEST、介绍卡里已写出的等价证据。」「重改造。需要新写或大改 task、环境或评分回路。」`notes/verify/v2/08-closed-gated.md` 的原句是「`docs/layer1.md` 的轻适配要有能交出去的 task 目录」。本轮把「能交出去的 task 目录」收成轻适配这句。那份笔记没有写后半句。`programbench` 现在是 `unknown`。`docs/registry.md` 压力列：「原标轻适配但缺 task.toml，与 08 规则冲突，勿当能接。」`docs/layer2/programbench.md` 距离句与这一格一致。

B 停句已交，落层仍缺口。`docs/abstraction.md`：「浏览暂不写入依赖列。缺的是「浏览属于哪一层」的仓内句。读者勿自行升成新轴。」

D 已交。面 9 已勾。抽查命中 0。见「文风抽查」。

## 文风抽查

文件：`docs/abstraction.md`、`docs/layer1.md`、`docs/conversion-playbook.md`、`docs/layer0.md`。各搜一遍。

词：赋能、抓手、底层逻辑、顶层设计、闭环、打法、拉通、对齐、颗粒度、沉淀、赛道、心智、链路、触达、方法论、组合拳、壁垒、护城河、势能、飞轮、降维打击、全链路、生态位、长期主义、第一性原理、确定性、范式、深耕，以及多臂、门槛盒、落地路径、助力。

命中 0。判定句和浏览停句仍在。`docs/done-when.md` 文风项因此勾上。其他勾选未改。

全 docs/ 套话抽查词表与命中数 0。词表是技能直接禁用的那些词。`docs/done-when.md` 里「对齐官方语义」已改成「和官方语义一致」。`docs/done-when.md` 的 abstraction 验收句曾被改掉「对齐官方语义」，已恢复成与 §7 相同的措辞。

读者文档里的「确定性」改成了程序比对或程序算出。slug、距离档、URL、路径未因这次改词而动。没有往 `docs/sources.md` 加缩写。文件名 README、MANIFEST，以及产品名，仍按 `notes/rounds/style-check.md` 不记成未定义缩写。

V-FINAL-END
