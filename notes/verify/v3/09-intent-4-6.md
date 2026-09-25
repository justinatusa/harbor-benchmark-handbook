# V3-09 意图面 4、5、6

材料是 `docs/layer0.md` 的「怎么用」、`docs/registry.md`、`docs/conversion-playbook.md`、`notes/final-report.md`、`notes/rounds/post-final-spotcheck.md`。本线程不改 `docs/conversion-playbook.md`、`docs/abstraction.md`。距离格不改。清单没有支撑句的行，压力列只追加「证据不足、勿升档」。登记仍是 52 行。距离档与 `notes/verify/v3/01-distance-counts.md` 相同：原生可接 3、轻适配 5、重改造 25、暂不宜接 14、`unknown` 5。

## 4. 读者能否判断原生 / 轻 / 重 / 暂不宜

registry 五行已补，其余缺口仍在。`27448b4` 已给 `mmmu-pro`、`mathvision`、`video-mme`、`automationbench`、`nl2repo-bench` 写勿当能接和 blocker，距离仍是 `unknown`。

`unknown` 五题有 blocker，不是空档。`docs/layer0.md` 怎么用第 3 步、`docs/registry.md` 表前、`notes/final-report.md` 未核实，都点名 `mmmu-pro`、`mathvision`、`video-mme`、`automationbench`、`nl2repo-bench`，并写「清单没写评测是否不要 GPU」。`nl2repo-bench` 另写「还没写死两个镜像算不算多容器」。五行压力格都有 GPU 这句。`mathvision` 行另有「Qwen-VL 脚本的设备要求没有打开」。`automationbench` 行另有「且运行不是多容器」。`docs/layer1.md` 把 `unknown` 写成「还没核实」，这五个格子旁边的句子比这四个字具体。

暂不宜接有一句可对。怎么用第 4 步写「任务不公开或 gated 的，停在暂不宜接」。`docs/conversion-playbook.md`「任务不公开或 gated」要求该行距离格是暂不宜接。登记这 14 行的压力格都写了不公开、gated，或正式评分不在公开仓：`aa-briefcase`、`agents-last-exam`、`analystbench`、`officeqa-pro`、`officeqa-pro-v2`、`finance-agent-v2`、`apex-agents`、`osworld-2-0`、`zerobench`、`frontierswe-v2`、`frontiercode-1-1`、`cursorbench`、`hle`、`critpt`。

原生、轻、重没有判定句。`docs/layer1.md` 只写允许值是这四个词，没有证据时写 `unknown`。`docs/abstraction.md` 只否定两行：`swe-atlas` 因 Harbor 版本不是 0.23.0，不是原生可接；`deepswe-v1-1` 没有 v1.1 tag，所以不是原生可接。没有写轻适配和重改造怎么分开，也没有写有 `task.toml` 时怎样才算原生可接。

同一类依赖对上不同的档。`terminal-bench-4-0` 是原生可接，压力列写部分题要 GPU、11 题要多服务容器。`mls-bench-lite` 是轻适配，压力列写多数题要 GPU。`spreadsheetbench` 是重改造，压力列写代码执行要两个镜像。`docs/abstraction.md` 把 GPU、多容器留在依赖里，不写它们改哪一档。

三行轻适配的压力格是「无」：`omnidocbench`、`benchcad`、`programbench`。`docs/layer2/programbench.md` 写清单没有 `task.toml`。`docs/layer2/omnidocbench.md` 与 `docs/layer2/benchcad.md` 不在。怎么用让读者查登记距离，不把「无」解释成轻适配。

三行原生可接是 `terminal-bench-4-0`、`terminal-bench-2-1`、`swe-bench-pro`。三份 `notes/sources/<slug>/MANIFEST.md` 都没有 `0.23.0`。`swe-bench-pro` 的运行时句子是 `harbor[modal]>=0.22`。`swe-atlas` 用「不是 0.23.0」离开原生可接。读者用同一句读 `swe-bench-pro`，对不上它为什么仍是原生可接。

其余八个 slug 只对照 `notes/sources/<slug>/MANIFEST.md` 和登记该行。距离格不改。

`mls-bench-lite` 有证据。登记距离是轻适配。`notes/sources/mls-bench-lite/MANIFEST.md`：「Harbor README 写 bundles 在 Harbor 0.6.6 和 0.22.0 上跑过，Modal 路径要求 Harbor ≥ 0.22。」

`terminal-bench-4-0` 无证据。登记距离是原生可接。`notes/sources/terminal-bench-4-0/MANIFEST.md` 有 66 个 `tasks/*/task.toml` 和 `harbor run -d terminal-bench/terminal-bench@4.0.0`，全文没有 `0.23.0`。blocker：证据不足、勿升档。

`terminal-bench-2-1` 无证据。登记距离是原生可接。`notes/sources/terminal-bench-2-1/MANIFEST.md` 有 89 个 `tasks/*/task.toml` 和 `harbor run -d terminal-bench/terminal-bench-2-1`，全文没有 `0.23.0`。blocker：证据不足、勿升档。

`swe-bench-pro` 无证据。登记距离是原生可接。`notes/sources/swe-bench-pro/MANIFEST.md`：「V2 README 的运行时是 Harbor（`harbor[modal]>=0.22`，Modal >= 1.5.1，用于分阶段网络策略）。」全文没有 `0.23.0`。blocker：证据不足、勿升档。

`spreadsheetbench` 无证据。登记距离是重改造。`notes/sources/spreadsheetbench/MANIFEST.md`：「代码执行路径是两个镜像（execute-api 与 executor）。」这句不把重改造和其他档分开。blocker：证据不足、勿升档。

`omnidocbench` 无证据。登记距离是轻适配，压力列是「无」。`notes/sources/omnidocbench/MANIFEST.md` 没有把轻适配和其他档分开的句子。blocker：证据不足、勿升档。

`benchcad` 无证据。登记距离是轻适配，压力列是「无」。`notes/sources/benchcad/MANIFEST.md` 没有把轻适配和其他档分开的句子。blocker：证据不足、勿升档。

`programbench` 无证据。登记距离是轻适配，压力列是「无」。`notes/sources/programbench/MANIFEST.md` 没有把轻适配和其他档分开的句子。blocker：证据不足、勿升档。

## 5. playbook 按类型可勾，抽节走得通或写明硬原因

缺口。

`docs/conversion-playbook.md` 六节都有 `- [ ]`：确定性 verifier、要另调 judge 模型、要 GPU、要出网、多容器或图形桌面、任务不公开或 gated。

两节抽查走通。`notes/rounds/post-final-spotcheck.md` 走了「任务不公开或 gated」和「确定性 verifier」。本轮再对过落点：

- `notes/sources/aa-briefcase/MANIFEST.md` 标题是「未抓取项与原因」，正文写正榜题面没有公开 URL。HF 段写第五个场景里的一周，不进计分榜。
- `notes/sources/deepswe-v1-1/MANIFEST.md` 写 held-out、gated，任务数 113，行数据未下载。
- `notes/sources/swe-bench-pro/MANIFEST.md` 有 `## 未能抓取`，commercial 276 与 held-out 858 不在公开仓。
- `notes/sources/spreadsheetbench/excerpt-scoring.py` 有 `soft_restriction`，`proc_path` 指向 `*_input.xlsx`，`*_output.xlsx` 那行被注释。
- `notes/sources/posttrainbench-v1-1/MANIFEST.md` 写 GPQA 的 `scorer=choice()`，并写哪几个下游脚本没有 `JUDGE_MODEL`。
- `notes/rounds/r1-package-map.md` 写 `/logs/verifier/reward.txt`，两个 reward 文件都没有则 `RewardFileNotFoundError`。
- `notes/sources/osworld-verified/MANIFEST.md` 写比对在 `desktop_env/evaluators/`。

确定性 verifier 里 pytest 那一条写了硬原因：本轮打开的清单没有点名 pytest 文件，工作区没有那份文件，停住。多容器节写「写出 agent 进入的 service……写不出就停在这一步」。

另外四节有勾选对不上文件，旁边没有同样的停句。

要另调 judge 模型。模型名在 `notes/sources/charxiv/excerpt.md` 和 `notes/sources/charxiv/MANIFEST.md`，勾选写的是打开 `src/descriptive_utils.py`。工作区没有这个路径。勾选「打开 `tests/test.sh`」和「拿掉 judge 密钥再跑评分脚本」没有对应文件。同一份 MANIFEST 写未跑 `evaluate.py`，没有 OpenAI key。这两条没有写成不能勾。

要 GPU。数量和型号写在 `notes/sources/posttrainbench-v1-1/MANIFEST.md`。勾选写的路径是 `src/commit_utils/single_task.sub`，工作区没有这个文件。同一份清单没有 `task.toml`，只写正在加 Harbor 支持的 PR。勾选仍要打开 `task.toml` 的 `[environment]`，并写「启动一次环境」。没有写成文件不在或这次不能启动。

要出网。`aa-briefcase` 无出站、`browsecomp` 的下载地址、`spreadsheetbench` 的 `jupyter.py` 没有 `network_mode`、`posttrainbench-v1-1` 评判前的 `curl`，这些句子在对应 MANIFEST 里。第一节勾选仍是「打开 `task.toml`」。这节用的例子没有一份可打开的 `task.toml`。`spreadsheetbench` 的出网在清单里保持 unknown，勾选写了不要补禁网或放行。

多容器或图形桌面。两个镜像、`happysixd/osworld-docker`、一个 `.sif`、`COMPOSE_FILE_NAME`，分别在 `notes/sources/spreadsheetbench/MANIFEST.md`、`notes/sources/osworld-verified/MANIFEST.md`、`notes/sources/posttrainbench-v1-1/MANIFEST.md`、`notes/rounds/r1-package-map.md`。service 写不出就停，这句在。勾选「打开评分结果」要有 `/logs/verifier/reward.txt` 或 `reward.json`。工作区没有这份评分结果，这条没有写成停住。

走不通的条目留给正在改清单的线程，本线程不改 `docs/conversion-playbook.md`。

## 6. 覆盖诚实

范围句已写入 `notes/final-report.md` 与 `docs/layer0.md`。playbook 仍只点名 8 个，44 个盖不住的名单在下面。

`docs/conversion-playbook.md` 点名的 slug 是 8 个：`spreadsheetbench`、`posttrainbench-v1-1`、`osworld-verified`、`charxiv`、`browsecomp`、`aa-briefcase`、`deepswe-v1-1`、`swe-bench-pro`。`prompts/bench-list.md` 与 `docs/registry.md` 是 52 行。其余 44 个 slug 在 playbook 里没有出现。

这 44 个是：`gdpval-aa-v2-1`、`agents-last-exam`、`draco`、`onemillion-bench`、`spreadsheetbench-2`、`analystbench`、`officeqa-pro`、`officeqa-pro-v2`、`finance-agent-v2`、`apex-agents`、`frontier-finance`、`big-finance-bench`、`osworld-2-0`、`gdp-pdf`、`mmmu-pro`、`omnidocbench`、`babyvision`、`perception-bench`、`zerobench`、`chartography`、`vision2web`、`benchcad`、`3dcodebench`、`mathvision`、`video-mme`、`automationbench`、`toolathlon-verified`、`mcp-atlas`、`terminal-bench-4-0`、`frontierswe-v2`、`nl2repo-bench`、`terminal-bench-2-1`、`programbench`、`swe-marathon`、`swe-atlas`、`mls-bench-lite`、`frontiercode-1-1`、`cursorbench`、`sec-bench-pro`、`exploitgym`、`hle`、`critpt`、`aa-omniscience`、`aa-lcr-v1-1`。

三行原生可接里，`swe-bench-pro` 在上面 8 个中：gated 节写了 commercial 276、held-out 858，以及公开的 642。出现在例子名单不等于距离档已有判定。`terminal-bench-4-0` 与 `terminal-bench-2-1` 在那 44 个里，整篇 playbook 没有出现。

怎么用第 4 步写：距离不是 `unknown` 时，打开 playbook 里对应的节，按 `- [ ]` 做。距离不是 `unknown` 的是 47 行。playbook 开篇写「例子只来自本轮打开过的 MANIFEST」，没有列出上面 8 个，也没有列出其余 44 个。`notes/final-report.md` 写 52 个 slug 都有 MANIFEST，介绍卡 30 张，并让读者按 playbook 的清单做。终报写的 30 张不是这 8 个例子。pull 之后 `docs/layer2/*.md` 是 31 个文件，本线程不改终报里的张数。

本线程在 `notes/final-report.md` 与 `docs/layer0.md` 各补了一句：例子盖住这 8 个，其余 44 个不在 playbook 里，因为例子只来自本轮打开过的 MANIFEST。52 题没有全部抽象完。44 个 slug 的名单留在本节。

V3-09-END
