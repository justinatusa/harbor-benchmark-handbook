# Harbor 统一接入抽象 — 调研任务提示词（完整版）

> **给 Cloud Agent 跑 goal 用。发车后用户可以不管。**  
> 真人背景与动机见同目录 [`harbor-unified-abstraction-BACKGROUND.md`](./harbor-unified-abstraction-BACKGROUND.md)（**不要**把背景文件内容贴进本任务）。  
> 配套技能（若可得）：`taxonomy-deep-research` · `layered-docs-zh` · `research-preferences` · **`no-ai-slop-zh`（文风验收必用）**

---

## 0. 一句话目标

在官方 **Harbor `0.23.0`（钉死）** 语义下，对一批待接入的 agent/LLM benchmark 做**证据驱动的形态与组件分类学**，找出通性/差异，整理出**尽量薄**的统一抽象名词与转化路径，使后来者能按手册快速判断「怎么接到 Harbor、缺什么、难在哪」。  

核心是 **抽象 + 接入决策**，不是堆百科，也不是把几十个 benchmark 全部改造成可运行产物。

---

## 1. 元信息

| 项 | 值 |
|---|---|
| 读者 | 负责把外部 benchmark 接到 Harbor 的工程师 / 评测同学 |
| 代码仓 | Cursor Origin：`justin-2/benchmarkresearchanddesign` |
| 环境 | 已 Save 的环境（Docker、uv、`harbor==0.23.0`、出网放开） |
| 子代理模型 | **一律** `grok-4.7` + `reasoning_effort: high`（界面名 Grok 4.7 / High）。拉源、摘录、对抗审查、填 registry 草稿等**所有**子代理 / Project 子线程都用这一档；不得改用别的模型或更低 effort。主协调模型由开 Project 时选定，本条只约束子代理。 |
| 成稿语言 | 读者文档中文、白话；须遵守 §8 成稿文风与 §7a 禁止早停；`notes/` 可用英文 |
| 时区 | Asia/Shanghai |
| Harbor | https://github.com/laude-institute/harbor · https://harborframework.com/docs · **钉死 0.23.0** |
| 名单来源 | **权威名单**：本仓 [`prompts/bench-list.md`](./bench-list.md)（当前约 52 个）。先按该表做；表可增补。勿把内部优先级/对齐状态写进读者文档 |
| 冻结 | 不要改无关仓；不要写入任何 API Key / secret |

开工：确认本机 `harbor` 版本为 `0.23.0`，写入 `docs/sources.md` 与 Layer0，记核实日。

名单：打开并遵守 [`prompts/bench-list.md`](./bench-list.md)。Registry 行与 `notes/sources/<slug>/` 以表中 slug 为准；入口 URL 为定位起点。

---

## 2. 你要说清楚的事（对外目标）

完成调研后，读者应能：

1. 用**同一套组件名词**（你裁决后的 taxonomy）看懂 30～40 个 benchmark 的同与不同。  
2. 对照 **Harbor 0.23.0 官方扩展点 / 任务模型**，判断某一题：原生可接 / 需轻适配 / 需重改造 / 暂不宜接。  
3. 知道每类题的**转化步骤、提前准备、常见坑**（出网、GPU、LLM judge、多容器等）。  
4. 看到「官方语义下还缺哪类扩展点」的**缺口清单**（只基于 Harbor 官方能力 + 样本压力，不臆造某公司内部实现）。

---

## 3. 最终产出清单（必须全部落地）

### A. 中文分层调研报告（`docs/`）

| 交付 | 作用 |
|---|---|
| **Layer0 导读** | 开篇必懂 + 词表（含缩写）+ Harbor 官方组件地图 + 你定的统一抽象 + 怎么用本手册做接入判断；文风见 §8 |
| **Layer1 总表** | 全量 registry 精简版：每行一个 benchmark，关键轴列齐 |
| **Layer2** | 按集群或按题的细节；20～30 个重点对象要有完整介绍卡（见 §6） |
| **`docs/abstraction.md`** | 专门写：组件抽象有几层、每层名词、与 Harbor 官方 noun 的对应、为何不多不少 |
| **`docs/conversion-playbook.md`** | 接入手册雏形：按类型（原生 / 镜像 / 自造 / 需 judge / 需 GPU / 需出网…）分路径 + 检查清单 |
| **`docs/sources.md` / `conflicts.md`** | 来源与冲突；缩写表 |

### B. 对象登记表（权威数据）

- `docs/registry.md` 或 `docs/registry.csv`（二选一或并存；以 md 可读为准）  
- 一行一个 benchmark；单元格可 `unknown`；每格尽量有来源  
- 覆盖：用户 list + 为撑开轴而加的对照样本（对照样本要标记 `pilot`）

### C. 本地源码/资料镜像（云机器工作区，可部分入仓）

- 目录约定：`notes/sources/<benchmark-id>/`  
- 每个 benchmark **一个文件夹**：克隆公开 git、下载可公开的 PDF/HTML 摘录、记录镜像名与 digest、HF 数据集 id  
- 超大 blob **不要**强行 commit；在该目录放 `MANIFEST.md`（URL、commit、抓取日、体积、是否入 git）  
- 工作区在 session 内应保持可回看；重要 MANIFEST 与小文本必须进 git

### D. 过程与对抗审查记录

- `notes/rounds/R1.md` …：每大轮「展/收/验」结论  
- `notes/adversarial/A1.md` …：对抗式审查（见 §5）  
- 最终 `notes/final-report.md`：改了哪些文件、未核实项、建议的小下一步（含「是否值得把 playbook 再收成 skills」——**本任务默认不写 skills 正文**，只许在最终报告里提一句可选下一步）

### E. 明确不做

- 不实现公司内部镜像/adapter 业务代码  
- 不要求把 list 里每一项都跑通完整评测  
- 不写入 secret；需要凭据的步骤只写「需要何种凭据」  
- 不把用户未提供的内部约束写进文档标题党

---

## 4. 种子词（引导，非强制轴）

可增删合并，但须在 `abstraction.md` 记录裁决：

| 种子 | 提示展开 |
|---|---|
| agent | 被测对象形态 |
| agent runtime | 控制回路跑在哪（相对任务环境） |
| environment | 题目环境：容器数、K8s、GPU、出网、MCP/外网服务 |
| grader / judge | 确定性 vs LLM judge（是否额外 judge 模型） |
| harness / dataset 接入 | Harbor 官方接入方式 vs 外部形态 |
| prep | 数据、镜像、oracle、密钥位 |

最终名词尽量**对齐 Harbor 官方文档用词**；对不上的新词要证明「官方词盖不住」。

---

## 5. 「葫芦」大轮回 + 对抗审查（必须）

禁止只扩张。默认 **4～6 个大轮回**；若 list 很大或抽象反复破裂，可做到 **7～8 轮**，但每轮都必须完整「展→收→验→提交」。

### 每大轮四拍

1. **展**：拉源、补行、记新轴与例外  
2. **收**：合并轴、删弱列、重写通性；服务不了接入决策的信息降到 notes  
3. **验**：抽链接；用难样冲击抽象；读完声明附行数+文末关键词+SHA  
4. **提交**：更新 `docs/` + registry + push

### 对抗式审查（两大轮之间插入一次）

在 R2 与 R3 之间、R4 与 R5 之间（若轮次更多则每隔一轮）必须做一次 **Adversarial Pass**：

- 另起视角（可用子代理，但结论由主协调写入 `notes/adversarial/`）专门找：  
  - 轴名空洞、同义反复、盖不住的反例  
  - 链接/版本张冠李戴  
  - 「看起来已接入 Harbor」其实只是名字像  
  - 转化步骤漏掉的硬依赖（judge 模型、GPU、出网、多容器）  
  - `docs/` 套话、自创词、无定义缩写、教学法标签；对照 `no-ai-slop-zh` 模式表  
- 主协调必须**回应每条攻击**：改轴 / 改文档 / 记入 conflicts（不接受的要写理由）  
- 没有对抗记录，不得进入下一轮「收束定稿」

### 建议轮次主题

| 轮 | 重点 |
|---|---|
| R1 | Harbor 0.23.0 官方：CLI、任务/数据集模型、扩展点、官方 noun |
| A1 | 对抗：扩展点地图是否过厚/过空 |
| R2 | 8～12 个形态极不相同的公开试点 |
| R3 | `bench-list.md` 全表进入；补官方源包与 `notes/sources/<slug>/` |
| A2 | 对抗：抽象是否被 list 打穿；playbook 是否可执行 |
| R4 | 统一抽象定稿；conversion-playbook 按类型写全 |
| R5+ | 仅当仍有系统性破洞；否则冻结并出 final-report |

### 主协调 vs 子代理（硬规矩）

- **子代理模型钉死**：凡 spawn / 派发的子代理与 Project 子线程，**全部**使用 **Grok 4.7 · High**（模型 id：`grok-4.7`，参数 `reasoning_effort=high`）。禁止 Auto、禁止换 Claude/GPT/Composer、禁止 medium/low。UI 或工具若要显式选模型与 effort，按此填写；写给子代理的提示词开头也写一句「本线程模型：grok-4.7 high」。
- **主模型（主协调）默认只 lead**：定轮次目标、写/改子代理提示词、裁决轴与结构、汇总进 `docs/` 与 registry、必要时抽查子代理产物。  
- **主模型不要默认通读每个子代理的全部原始输出**；只在汇总冲突、对抗审查、抽检质量、或怀疑跑偏时深入看。  
- 子代理：并行拉源、克隆、摘录、填 registry 草稿、写 `notes/`；**不得**擅自改 taxonomy 定稿与读者向 `docs/` 结构（除非主协调明确授权某一文件）。  
- **子代理产出不符合需求 = 子代理提示词/分工写错了**：主协调必须改提示词（或改分工），**作废或重跑该批**，不得把半截错结果硬揉进定稿凑数。  
- **一直做**：一轮结束立刻开下一轮；没有用户 pause/stop，就按 §7a 连续推进到 Done-when。  
- **允许随时合入 `main`**：每完成可独立使用的增量（官方地图、试点表、某批介绍卡、abstraction 一版、playbook 一节等）即可 merge/push 到 `main`，不要囤到「全部完美」才合；合入后继续下一增量。冲突用小步提交解决。

子代理可并行克隆与摘录；**taxonomy 与 docs 定稿只许主协调改**。

---

## 6. 单个 benchmark 介绍卡（统一骨架）

20～30 个重点对象（用户 list 优先）必须具备：

1. 一句话：测什么  
2. 官方源包链接（站/blog/论文/GitHub/榜/HF/镜像…）  
3. 形态标签（用你的轴）  
4. 与 Harbor 官方接入的距离：原生 / 轻适配 / 重改造 / 未知  
5. 环境：容器、出网、GPU、K8s 迹象  
6. 评分：确定性 vs 需 judge 模型  
7. Agent / runtime 线索（有证据才写）  
8. 迁入代价：低/中/高 + 依据  
9. 对抽象的压力：逼改了哪条轴  
10. 本地目录：`notes/sources/<id>/` 的 MANIFEST 指针

---

## 7. Done-when

- [ ] `harbor==0.23.0` 已核实写入  
- [ ] `abstraction.md`：组件层数少、名词稳、对齐官方语义的说明齐全  
- [ ] `conversion-playbook.md`：按类型可照着做的检查清单（含 judge / GPU / 出网 / 多容器等已发现类型）  
- [ ] Registry 覆盖 `prompts/bench-list.md` 全表；重点 20～30 个有介绍卡  
- [ ] 每个已深挖对象有 `notes/sources/<id>/MANIFEST.md`  
- [ ] ≥4 个完整大轮回；≥2 次对抗审查且每条有回应  
- [ ] Layer0/1 + 必要 Layer2 + sources + conflicts  
- [ ] 抽样 ≥20 链接核对；final-report 列出未核实项  
- [ ] `docs/` 通过 §8 文风抽查（含 **`no-ai-slop-zh` 检测模式**：具名模式清零或已改；无套话、无自创词/教学法标签、缩写有表）  
- [ ] 过程中已多次合入 `main`（非囤到最后一次大爆）；orchestration-log 或 rounds 能看出增量合入  
- [ ] 未完成以上不得宣称完成

---

## 7a. 禁止早停（硬规矩）

未完成 §7 **每一项**并留下证据，**不得**宣称完成、收工，也不得只发「进度汇报」就停。

**假完成（一律不算 Done）：**

- 只提交大纲 / 空 registry / 目录骨架  
- 只写完 Harbor 官方地图或 R1  
- 只做完 8～12 个试点  
- 只有 Layer0，没有 `abstraction.md` / `conversion-playbook.md` / 重点介绍卡  
- 对抗审查没做，或攻击条目没有逐条回应  
- 「大体核实了」「庭审齐了」「本轮差不多了」「先交一版再补」

**必须继续：**

- 大轮之间**禁止停下来等人确认**；勾选未齐就立刻进入下一轮「展→收→验→提交」  
- 增量可随时合 `main` 后继续；**合入 ≠ 收工**  
- 不得为勾选而降低门槛、缩减介绍卡数量、跳过对抗、或把未核实写成定论  
- 自认接近完成时：必须重读 §7；任一未勾则继续；**全部勾齐**才写 `notes/final-report.md`

**允许停下的情况只有：**

1. §7 全齐且有证据；或  
2. 写出**具体 blocker**（例如缺 list 某一项、某官方源不可达），并继续做**不依赖**该 blocker 的工作；或  
3. 用户明确说 pause / stop

---

## 8. 成稿文风（去 AI 味，硬规矩）

适用于全部读者向 `docs/`（Layer0/1/2、`abstraction.md`、`conversion-playbook.md`、registry 说明文字）。`notes/` 可用英文，但**不得**把 notes 里的口号/自创标签原样搬进 `docs/`。

### 额外必读（文风）

写任何读者向 `docs/` 之前，**额外对照** skill / 仓库 **`no-ai-slop-zh`**（https://github.com/shenxianpeng/no-ai-slop-zh 的 `SKILL.md` + `eval.md`）。本省禁令与该 skill **同时生效**；冲突时取更严的一侧。不要只凭感觉「写得通顺」就交差。

### 必须

- 白话中文；短句；具体动词；开篇先写读者会踩的坑或必须先懂的事  
- 官方字段名、CLI、路径、镜像名、包名保留英文，用中文解释  
- 专有缩写**首次出现写全称**；并在 `docs/sources.md`（或 Layer0 词表）维护缩写表  
- 轴名 / 组件名词尽量对齐 **Harbor 官方文档用词**；确需新词时，在 `abstraction.md` 写明「官方哪几个词盖不住、为何要新词」——**禁止为酷炫自创**  

### 禁止（AI slop + 自创词）

- 套话堆砌：「在当今…」「值得注意的是」「让我们一起…」「全面深入探讨」「落地路径」「助力」等空话（完整模式表见 `no-ai-slop-zh`）  
- **禁止自创词 / 黑话当术语**写进 `docs/`。点名举例（不限于此）：**闭环、多臂、赋能、抓手、拉通、颗粒度、赛道、飞轮、护城河、降维打击、心智、触达、组合拳**，以及任何你现场造的「听起来很 AI / 很咨询」的中文词。意思用普通句子说清楚即可，**不要造标签**。  
- **自创口号、教学法品牌名**进正文（标签扔掉）。禁止文档方法论品牌名、自造「门槛盒」一类叫法  
- **无定义的自创英文缩写或拼音缩写**当轴名或章节标题（仓内临时代号只许留在 `notes/`）  
- 把冲突 / 未核实写成假装已定论  
- 标题腔：「完整知识体系」「建议背诵」「一文打通」  

### 好 / 坏（Harbor / 接入语境）

**好：**「名字里带 Harbor 不代表已经能接；先对官方任务模型和扩展点，再看要不要自己写适配。」

**坏：**「在评测基建快速发展的今天，我们需要用统一抽象闭环赋能接入，打造可落地的知识体系。」

**好：**「LLM judge 表示评分要另调一个评判模型；密钥和被测模型不是同一套。」

**坏：**「本章将全面深入探讨 Judge 维度的方方面面，帮助你更好地建立 threshold concept。」

**好表注：**「写适配时查；不要通读。」

**坏表注：**「完整能力地图（建议背诵）。」

### 验收（必须跑 `no-ai-slop-zh`）

文风验收以 skill **`no-ai-slop-zh`**（来源 https://github.com/shenxianpeng/no-ai-slop-zh）为准，并叠加本节省禁：

1. 对 Layer0、`abstraction.md`、`conversion-playbook.md` 及至少 3 张重点介绍卡跑 **检测模式**（列出模式名 + 原文引用；不要猜「是不是 AI 写的」）。  
2. 检出的模式必须改掉，再对照该 skill 的 `eval.md` 自检；未清零不得勾 §7 文风项。  
3. 对抗审查与 `notes/final-report.md` 各附一次检测摘要（模式清单或「零命中」）。  
4. 同时扫：自创词/教学法标签、无表缩写（§8 本省禁令）。  

若环境挂不上该 skill：把 https://github.com/shenxianpeng/no-ai-slop-zh 的 `skills/no-ai-slop-zh/SKILL.md` + `eval.md` 拷进工作区参照执行，效果等同。

---

## 9. 开场第一次 commit

1. 大纲 + taxonomy 计划（种子词如何处理）  
2. 空 registry 表头  
3. Done-when 勾选副本（含文风与禁止早停）  
4. Harbor 0.23.0 核实  
5. 目录骨架：`docs/`、`notes/sources/`、`notes/rounds/`、`notes/adversarial/`

然后进入 R1。以 `bench-list.md` 灌入 registry；可并行领活深挖（子代理一律 Grok 4.7 high）。

---

## 10. 手机最短口令

> 执行本仓 `prompts/harbor-unified-abstraction-research.md`；名单以 `prompts/bench-list.md` 为准。Harbor 钉死 0.23.0。主协调只 lead/汇总，必要才深挖子代理结果；**所有子代理一律 Grok 4.7 high**；子代理不对就改提示词重跑。按「葫芦」展收验 + 对抗审查，持续推进并允许随时合 `main`。产出分层报告、`abstraction.md`、`conversion-playbook.md`、registry 与 `notes/sources/<slug>/`。禁止早停；`docs/` 须过 `no-ai-slop-zh` 检测，禁自创词与未定义缩写。不要只扩张条目，不要写内部业务代码。
