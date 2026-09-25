# 质量审查

审查对象：Origin `justin-2/benchmarkresearchanddesign` main tip `1976a2fdacc358ffaa207184fbca9409e78a638b`（2026-09-25 与 `origin/main` 一致）。本页记录审查时的问题和随后写进 `docs/` 的修改。读者手册以修改后的 `docs/` 为准。过程勾选不在读者正文里。

本机 `harbor --version` 为 `0.23.0`。分面核对克隆了钉死 commit，并对照安装包源码。子代理模型为 grok-4.7 high。

## 结论

修改后的 `docs/` 可以当接入判断手册用：先对版本，再查 registry 距离，再按依赖打开转化路径。距离档不再把「没有 Harbor task 目录」写成轻适配或 `unknown`。公开读者不用打开 `notes/`。

它还不是 52 题各自的逐步施工单。转化路径的可勾选例子仍是 8 个 slug。其余题只给出距离和依赖，不给出该题自己的逐步清单。

## 改前问题

1. 假完成。`docs/done-when.md` 曾把合同第 7 节全部打勾。当时 `omnidocbench`、`benchcad` 没有 `task.toml` 仍标轻适配；六题以「清单没写评测是否不要 GPU」停在 `unknown`；`conflicts.md` 写 0.23.0 没有 `BaseInstalledAgent`。
2. 距离档错。克隆后这 8 个公开题都没有 Harbor task 目录，应是重改造：`mmmu-pro`、`mathvision`、`video-mme`、`automationbench`、`nl2repo-bench`、`programbench`、`omnidocbench`、`benchcad`。评测脚本都没有写明必须显卡。`nl2repo-bench` 的 openhands 镜像和 runtime 镜像是代理和它的一个沙箱，不是 compose 多容器。
3. 代价不一致。`deepswe-v1-1`、`swe-bench-pro`、`swe-atlas`、`programbench` 的介绍卡写中，registry 写低。
4. 安装包事实写错。0.23.0 的 `agents/installed/base.py` 有 `BaseInstalledAgent.install()`。缺 `environment/` 时 `is_valid_dir` 返回假，不抛 `FileNotFoundError`。缺 `gpus` 不等于「进默认 docker、没有 H100」。`DockerEnvironment` 不认 `docker-compose.yml`。任务配置不拒绝 `schema_version = "1.0"`。本安装不读 `rewards.json`。
5. 公开路径名实不符。`layer0` 让读者打开 `notes/final-report.md`。registry「本地目录」和介绍卡第 10 项指向 `notes/sources/...`。转化清单的勾选写「打开 notes」。不含 notes 的公开镜像打不开这些路径。
6. 调研腔。压力格里的「证据不足、勿升档」「清单没写」「blocker」把核对笔记写成了读者结论。

维持原生可接：`terminal-bench-4-0`、`terminal-bench-2-1`、`swe-bench-pro`。轻适配现为四行：`deepswe-v1-1`、`mls-bench-lite`、`swe-atlas`、`swe-marathon`。暂不宜接现为 13 行。`finance-agent-v2` 改为重改造。

## 已修

- registry 52 行仍与 `prompts/bench-list.md` 一一对应。`pilot` 全是 `no`。距离现为：原生可接 3、轻适配 2、重改造 33、暂不宜接 14、`unknown` 0。去掉「本地目录」和内部「置信」列。压力格不再引用 `notes/`。
- 上列 8 题改为重改造，并改了已有介绍卡的距离句。`deepswe-v1-1`、`swe-bench-pro`、`swe-atlas`、`programbench` 的迁入代价改为中。`benchcad` 改为高。
- `layer0`、`abstraction`、`conflicts`、`conversion-playbook` 按安装包改了 `BaseInstalledAgent`、缺目录、缺 `gpus`、compose 文件名、`schema_version`。
- 轻适配收成：必须已有 Harbor task 目录。没有目录、题又公开，记重改造。同一句写在 `layer1` 和 `abstraction`。
- 介绍卡的本地摘录改为「私有摘录未随公开手册发布」，不再给 `notes/sources` 路径。
- 转化清单的勾选改为公开仓 URL、钉死 commit 和仓内路径。打不开就停。例子仍只覆盖 8 个 slug，并写明例子不等于距离档。
- `docs/done-when.md` 移到 `notes/done-when.md`。全勾记录保留为过程，并注明不能当完成证明。

Harbor 0.23.0 解释器执行 playbook 里的核对命令，输出是 `False` 与 `['rewards']`。

## 2026-09-25 第二轮行/不行

对照主 prompt、安装包和钉死 commit。纯猜测放过，不改文档。

| 结论 | 判定 | 原因 |
|---|---|---|
| 三层抽象用 Harbor 已有词 | 通过 | task、运行、接入都对得上安装包名词。导读补了三层本身，不只留指针。 |
| BaseAgent / BaseInstalledAgent | 通过 | 安装包两类都在。回路留在环境外用 `BaseAgent` 的出处改回文档站，不再安到 `agents/installed/base.py`。 |
| verifier 只认 reward 文件 | 通过 | 没有 `LLMJudge`。核对命令输出 `False` 与 `['rewards']`。 |
| 缺 `gpus` 不等于默认 docker | 通过 | 有效 GPU 数为 0。默认 docker 看 `environment.type`。 |
| 空 allowlist | 不通过后已改 | `network-policy` 写明 allow 模式没有目标时拒绝全部受控 TCP 出网。 |
| 原生可接三条 | 通过 | 4.0、2.1、SWE-Bench Pro 公开集有 Harbor 目录和 `harbor run`。 |
| 轻适配：deepswe、mls-bench-lite | 通过 | 有 task 目录，入口或跑过的版本不是 0.23.0 的原生 `harbor run`。 |
| swe-atlas、swe-marathon | 不通过后已改 | 284 与 20 个 Harbor 目录，脚本是 `harbor run`，钉的是 v0.18.0 与 0.20.0。改为轻适配，不是重改造。 |
| 八题重改造（无 task.toml） | 通过 | 公开题和评分在，没有 Harbor task 目录。 |
| finance-agent-v2 | 不通过后已改 | `data/public.csv` 有 27 道题和 rubric。改为重改造。正式 Test Suite 仍不在 commit。 |
| frontierswe-v2 暂不宜接 | 通过 | 站上 v2 是 34 题。公开 commit 的 17 份 `task.toml` 不是那张题单。不改成轻适配。 |
| critpt 暂不宜接 | 通过 | 公开 JSON 有题面。`Challenge_1.json` 的 `testcases` 是 null，`answer_code` 仍是占位。正式分走私有服务。 |
| agents-last-exam 暂不宜接 | 通过 | 165 张 `task_card.json` 在 git。抽到的题没有 `input/` 文件。题包交不出。 |
| 转化路径按类型 | 不通过后已改 | 补了「原生可接」一节。judge、GPU、出网、多容器、程序比对、gated 原先已有。 |
| 例子不等于距离档 | 通过 | `layer0` 与 registry 开篇写了。8 个例子不够不成不通过。 |
| 介绍卡 20～30 | 通过 | 31 张。另外 21 个没有卡，不记不通过。 |
| 公开路径不指 notes | 通过 | `docs/` 没有 `notes/` 路径。 |
| 文风禁用词「对齐」 | 不通过后已改 | 三处「对齐 0.23.0」改成「不是 0.23.0」。 |
| 缺 `environment/` 的第四种 extra compose 参数 | 放过 | 报错原文只列 `docker_image`、Dockerfile、`docker-compose.yaml`。 |
| 未在 0.23.0 上跑完全集 | 放过 | 合同不要求跑通评测。 |
| 21 个 slug 没有介绍卡 | 放过 | 合同要的是 20～30 张重点卡。 |

## 仍记 unknown，不改成定论

- BrowseComp 入口 `https://openai.com/index/browsecomp` 抽查是 403。论文和 `simple-evals` 的 commit 是 200。
- 文档站未标版本。`environment/` 能否按文档站省略、ATIF 1.7 与 1.8、教程 `version = "1.0"` 与字段参考 `schema_version = "1.3"`，仍在 `docs/conflicts.md`。
- `singularity-compose.yaml` 只出现在安装包目录注释里。本安装没有读取它的代码。

暂不宜接的行是题面或数据包不在公开 commit 里。手册不编下载步骤。这不是缺口，是停句。

## 与合同第 7 节

勾选只在 `notes/done-when.md` 和本页。审查前的全勾不能沿用。按原文：介绍卡 31 张，落在 20～30 的上限附近，不因另外 21 个没卡而失败。转化路径按类型，不按 52 题各写一节。文风禁用词「对齐」已从 `docs/` 去掉。

## 公开可读性

读者从 `docs/layer0.md` 进入，不再被指向 `notes/final-report.md`。介绍卡和 registry 不再给出私有摘录路径。转化步骤指向公开 commit。公开镜像若只导出 `docs/`、`prompts/bench-list.md`，这条阅读顺序可以走通。镜像 README 不在本仓；本仓改的是它会导出的正文。
