# 文风检测

依据 `notes/refs/no-ai-slop-zh/SKILL.md` 的具名模式，加上点名的那些词。缩写看 `docs/sources.md` 的表：正文里的缩写不在表内就记。反引号内的代码和路径、URL、引号里的上游原文、产品名和基准正式名称、文件名、单位符号、版本号不记。

## 第一遍

31 条。都是无定义缩写。二元对立、废话开头、伪洞察铺垫、冒号揭示、表面分析、重要性吹捧、模糊引用、虚假强动词、同义词轮换、否定列举、戏剧化碎片、机械节奏、反问铺垫、伪深刻结尾、总结性重复结尾、格式套话、破折号，以及点名的那些词，这六份里没有。

### docs/layer0.md

零命中

### docs/abstraction.md

- 无定义缩写。`docs/abstraction.md`。原句：A1 的三点仍约束写法。
- 无定义缩写。`docs/abstraction.md`。原句：A1 之后仍未定的点
- 无定义缩写。`docs/abstraction.md`。原句：`VerifierResult` 只有 rewards，字符串键到有限 int 或 float。

### docs/conversion-playbook.md

- 无定义缩写。`docs/conversion-playbook.md`。原句：`osworld-verified` 每题 JSON 带 evaluator，实现在 `desktop_env/evaluators/`。
- 无定义缩写。`docs/conversion-playbook.md`。原句：`posttrainbench-v1-1` 的 GPQA 脚本使用 `scorer=choice()`，该脚本里没有 `JUDGE_MODEL`。
- 无定义缩写。`docs/conversion-playbook.md`。原句：`posttrainbench-v1-1` 的 GPQA 用 `scorer=choice()`，按它的选项结果写数字，不要改成调用 judge 模型。
- 无定义缩写。`docs/conversion-playbook.md`。原句：`charxiv` 公开 JSON 里 test 的答案是 `null`。
- 无定义缩写。`docs/conversion-playbook.md`。原句：`posttrainbench-v1-1` 的 `src/commit_utils/single_task.sub` 为 `num_gpus = 1`，`request_gpus`，要求 `NVIDIA H100 80GB HBM3`，内存 131072、16 CPU、磁盘 400G。
- 无定义缩写。`docs/conversion-playbook.md`。原句：`src/generate_lib/` 里多个本地模型把权重放到 CUDA，`internvl2.py` 与 `nvlm.py` 按 `torch.cuda.device_count()` 切层。
- 无定义缩写。`docs/conversion-playbook.md`。原句：API 模型路径不要求本机 GPU。
- 无定义缩写。`docs/conversion-playbook.md`。原句：`spreadsheetbench` 的执行器镜像安装 CPU 版 torch，Docker 限制是 8GB 内存和 2 CPU，没有 GPU device。
- 无定义缩写。`docs/conversion-playbook.md`。原句：镜像使用带 CUDA 的基座，或写明运行时如何把显卡传进环境。
- 无定义缩写。`docs/conversion-playbook.md`。原句：只走 API 的路径不要填 `gpus`。
- 无定义缩写。`docs/conversion-playbook.md`。原句：`charxiv` 的 API 模型路径不要求本机 GPU。
- 无定义缩写。`docs/conversion-playbook.md`。原句：`spreadsheetbench` 的执行器保持 CPU 限制。
- 无定义缩写。`docs/conversion-playbook.md`。原句：卡没有挂上时，记失败，不要把 CPU 跑通当成 GPU 已接。
- 无定义缩写。`docs/conversion-playbook.md`。原句：`posttrainbench-v1-1` 还要 16 CPU、内存 131072、磁盘 400G。
- 无定义缩写。`docs/conversion-playbook.md`。原句：首次运行还要下载 VM 快照。
- 无定义缩写。`docs/conversion-playbook.md`。原句：有 `/dev/kvm` 时把 KVM 设备传进容器，否则环境变量 `KVM=N`。
- 无定义缩写。`docs/conversion-playbook.md`。原句：agent 进哪个 service，两份 R1 笔记都没有写规则。
- 无定义缩写。`docs/conversion-playbook.md`。原句：密钥、账号、VM 口令都不要写入仓库。
- 无定义缩写。`docs/conversion-playbook.md`。原句：仓库里没有私有题面，没有编出来的数据 URL，没有解密后的明文。
- 无定义缩写。`docs/conversion-playbook.md`。原句：`browsecomp` 的 CSV 是公开的，单元格用该行 `canary` 做 XOR。

### docs/layer2/browsecomp.md

零命中

### docs/layer2/swe-atlas.md

- 无定义缩写。`docs/layer2/swe-atlas.md`。原句：Codebase Q&A 和 Test Writing 有 `dataset.toml`，Refactoring 没有。
- 无定义缩写。`docs/layer2/swe-atlas.md`。原句：Codebase Q&A 的 124 题和 Test Writing 的 90 题写 `gpus = 0`。
- 无定义缩写。`docs/layer2/swe-atlas.md`。原句：Codebase Q&A 的 `task.toml` 没有 `network_mode`，示例脚本 `run_config/qa/opus-4p6_claude-code.sh` 也没有 `--allow-agent-host`。
- 无定义缩写。`docs/layer2/swe-atlas.md`。原句：README 写 QnA 在 `agent.run()` 期间限制出网，和这两处文件不完全同一套。
- 无定义缩写。`docs/layer2/swe-atlas.md`。原句：Codebase Q&A 的 rubric 全部是必须项，全过才算过。
- 无定义缩写。`docs/layer2/swe-atlas.md`。原句：Test Writing 分三段：manifest 由模型看是否如实列出新增测试，mutation 用程序检查（原代码上测试要过，相关代码换成 no-op 后测试要失败），rubric 再由模型打。

### docs/layer2/aa-briefcase.md

- 无定义缩写。`docs/layer2/aa-briefcase.md`。原句：提示词写隔离的 Linux 容器，用户 `user`（UID 1000），家目录 `/home/user`，没有出站连接。
- 无定义缩写。`docs/layer2/aa-briefcase.md`。原句：计分用的 91 题和核查表没有公开 URL。

## 第二遍

同一条规则再扫一遍。A1、R1、int、float 已从正文去掉。其余缩写已写入 `docs/sources.md`，每个缩写在该文件第一次出现时写了全称。

### docs/layer0.md

零命中

### docs/abstraction.md

零命中

### docs/conversion-playbook.md

零命中

### docs/layer2/browsecomp.md

零命中

### docs/layer2/swe-atlas.md

零命中

### docs/layer2/aa-briefcase.md

零命中

STYLE-CHECK-END

## Layer0 在 d165123 之后

只检 `docs/layer0.md`。模式表在 `notes/refs/no-ai-slop-zh/SKILL.md`。

扫过这些模式：二元对立、废话开头、伪洞察铺垫、冒号揭示、表面分析、重要性吹捧、模糊引用、虚假强动词、同义词轮换、否定列举、戏剧化碎片、机械节奏、反问铺垫、伪深刻结尾、总结性重复结尾、格式套话、破折号。也扫了该表里点名要删的词。

冒号都在列名单或文件名，不记成冒号揭示。CLI、LLM、GPU 已在 `docs/sources.md`。README 是文件名，不记。

零命中。文风项不勾。

## 2026-09-25 修补轮

抽查文件：`docs/abstraction.md`、`docs/layer1.md`、`docs/conversion-playbook.md`、`docs/layer0.md`。

抽查词：赋能、抓手、底层逻辑、顶层设计、闭环、打法、拉通、对齐、颗粒度、沉淀、赛道、心智、链路、触达、方法论、组合拳、壁垒、护城河、势能、飞轮、降维打击、全链路、生态位、长期主义、第一性原理、确定性、范式、深耕，以及多臂、门槛盒、落地路径、助力。

四份各搜一遍，命中 0。判定句与浏览停句保留。文风项勾上。其他 Done-when 勾选未改。
