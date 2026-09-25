# 来源

读者文档里的缩写在这里登记。冲突记在 `docs/conflicts.md`。

## Harbor 版本核实

核实日：2026-09-24（Asia/Shanghai，UTC+8）。

钉死版本：Harbor `0.23.0`。

本机证据：

| 检查 | 结果 |
|---|---|
| `command -v harbor` | `/home/ubuntu/.local/bin/harbor`（符号链接到 uv tool 环境） |
| `harbor --version` | `0.23.0` |
| 安装约束 | `/home/ubuntu/.local/share/uv/tools/harbor/uv-receipt.toml` 写着 `harbor==0.23.0` |
| 包元数据 | `harbor-0.23.0.dist-info/METADATA` 的 `Version: 0.23.0` |
| Python 导入 | 该环境里 `importlib.metadata.version("harbor")` 为 `0.23.0` |
| 包路径 | `/home/ubuntu/.local/share/uv/tools/harbor/lib/python3.12/site-packages/harbor` |

官方仓库：<https://github.com/laude-institute/harbor>

GitHub tag `v0.23.0` 指向 commit `1e5c5c6db929a10a140d05e606882c671ae20729`。tagger 时间是 `2026-09-12T04:55:13Z`。出处在 `notes/rounds/r1-docs-nouns.md`。

文档站：<https://docs.harborframework.com/>

该站未标版本。`llms.txt` 没有版本号。站上 changelog 的条目没有 release 版本标题。tag 上的 `CHANGELOG.md` 也没有 `## 0.23.0` 标题。文档站上的句子不能当成 0.23.0 的定论。

<https://harborframework.com/docs> 会跳到文档站。跳转不提供版本号。

## 缩写

首次在读者文档里出现的缩写，写全称，并加到下表。没有定义的缩写不要当轴名。

| 缩写 | 全称 | 在本文里指什么 |
|---|---|---|
| Harbor | Harbor（包名 `harbor`） | 官方评测框架，本手册只认 0.23.0 |
| CLI | command-line interface | `harbor` 命令行 |
| GPU | graphics processing unit | 任务要不要显卡 |
| HF | Hugging Face | 数据集或模型页面所在站点 |
| MCP | Model Context Protocol | 任务要不要接外部 MCP 服务。定义以该 benchmark 自己的材料为准，不在这里扩写协议 |
| ATIF | Agent Trajectory Interchange Format | 轨迹格式。文档站两处版本号不一致，见 `docs/conflicts.md` |
| ASP | Agent Sandbox Protocol | sandbox 文档里的草案。harness 在该页指 agent loop 那一侧 |
| TOML | Tom's Obvious Minimal Language | `task.toml` 和 RewardKit judge 用的配置格式 |
| LLM | large language model | RewardKit 的 judge 可以调的语言模型 |
| JSON | JavaScript Object Notation | 题面或数据的文本格式 |
| GPQA | Graduate-Level Google-Proof Q&A | 题集名。本文里指选项字母比对那一套 |
| CPU | central processing unit | 中央处理器 |
| CUDA | Compute Unified Device Architecture | 显卡计算平台 |
| API | application programming interface | 程序接口。本文里多指模型接口 |
| VM | virtual machine | 虚拟机 |
| KVM | Kernel-based Virtual Machine | 内核虚拟机 |
| CSV | comma-separated values | 逗号分隔的表格 |
| XOR | exclusive or | 按位异或 |
| URL | uniform resource locator | 网址 |
| UID | user identifier | 数字用户号 |
| Q&A | questions and answers | 问答 |
| QnA | questions and answers | 与 Q&A 相同的另一种写法 |
| no-op | no operation | 不改变实际行为的代码替换 |

## 名单

权威名单：`prompts/bench-list.md`（52 个 slug）。Registry 行和 `notes/sources/<slug>/` 用表里的 slug。
