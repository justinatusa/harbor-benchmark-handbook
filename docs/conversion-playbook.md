# 转化路径

按依赖写检查清单。例子只覆盖 8 个 slug，出现在例子里不等于距离档。核对上游文件时打开公开仓的钉死 commit。本手册里的摘录在 `notes/sources/`。文件对不上就停。这份清单不是端到端可照做的完整评测。

任务公开、且不是 gated 的节，要交出 Harbor 的 task 目录：`instruction.md`、`environment/`、与操作系统匹配的评分脚本（`tests/test.sh` 或 `tests/test.bat`）。评分脚本最后要写出 reward 文件：`/logs/verifier/reward.txt` 或 `/logs/verifier/reward.json`。两份都在时，Harbor 先读 `reward.json`。任务不公开或 gated 的节不要求 `tests/test.sh`，也不要求 `tests/test.bat`。

adapter 只用来生成这些目录。job 运行时不加载它。多题用 dataset 把 task 列出来。

## 原生可接

registry 该行是「原生可接」时走这一节。不要另写一套 task 目录。

### 开工前准备

- 本机 Harbor 是 0.23.0。核对见 `docs/sources.md`。
- 打开该行「来源包」里的 commit，确认 `task.toml`、`environment/`、评分脚本还在。

### 转化步骤

1. 按上游说明执行 `harbor run`。Terminal-Bench 4.0 的发布说明是 `harbor run -d terminal-bench/terminal-bench@4.0.0`。Terminal-Bench 2.1 的 README 是 `harbor run -d terminal-bench/terminal-bench-2-1`。SWE-Bench Pro 公开集的 V2 README 是 `harbor run -p v2/tasks`。
2. 上游钉的 Harbor 版本不是 0.23.0 时，不要把这一行留在原生可接。改回 registry 的轻适配，先看版本差。
3. 公开集之外的 commercial、held-out 不在这条命令里。那些部分停在「任务不公开或 gated」。

### 做完怎么核对

- 命令指向的是 Harbor task 目录或 Harbor dataset 名，不是上游自己的评测脚本。
- 跑起来的 Harbor 版本是 0.23.0。上游只写了更低版本时，这一节停住。

### 坑

- 名字里带 Harbor，或仓库里有 `task.toml`，都不够。还要有 `harbor run` 说明，并且版本能对上 0.23.0。
- SWE-Bench Pro 公开说明写 `harbor[modal]>=0.22`。目录是 Harbor task，所以公开 642 题保持原生可接。本手册没有一份 0.23.0 上跑完全集的记录。

### 可勾选步骤

- [ ] 打开 `docs/registry.md` 该行。距离不是「原生可接」就离开本节。
- [ ] 对上上面三条 `harbor run` 之一，或该行来源包里另一条写明的 `harbor run`。对不上就停。
- [ ] `harbor --version` 输出 `0.23.0`。不是这个版本就停。

## 程序比对 verifier

答案比对、pytest、选项字母，都走这一节。最后写 reward 文件。

### 开工前准备

- 确认分数由程序算出。`spreadsheetbench` 的 `evaluation/evaluation.py` 把单元格和答案表做相等比较，数值先四舍五入到 2 位小数。公式重算用 LibreOffice 或 Excel。
- `osworld-verified` 每题 JSON（JavaScript Object Notation）带 evaluator，实现在 `desktop_env/evaluators/`。getters 取虚拟机状态，metrics 做表、文档、幻灯片、浏览器比对。
- `posttrainbench-v1-1` 的 GPQA（Graduate-Level Google-Proof Q&A）脚本使用 `scorer=choice()`，该脚本里没有 `JUDGE_MODEL`。选项比对走本节。
- 准备标准答案、比对脚本，以及重算公式需要的 LibreOffice 7.5+ 或 Windows Excel。材料不进 git 的大包不要复制进仓库。

### 转化步骤

1. 写 `instruction.md`，把上游题面放进去。
2. 写 `environment/`。文档允许只留 `docker_image` 并省略这个目录。安装包的 `is_valid_dir` 要求目录在。冲突保持 unknown。接入时仍放上 `environment/`。单容器走 Harbor task 的 environment，不单列轴；多容器才走「多容器或图形桌面」。`omnidocbench` 的清单写推荐单容器镜像 `ghcr.io/zeng-weijun/omnidocbench-eval:repro-ubuntu2204`。只作单容器镜像例子，不是距离档已有判定。
3. 答案比对：`tests/test.sh` 读取模型产物和标准答案，逐项比较。`spreadsheetbench` 用 `soft_restriction` 记三个测试用例的通过比例，用 `hard_restriction` 在三题全过时写 1。
4. pytest：上游测试是 pytest 时，`test.sh` 跑这些用例，再把通过与否写成数字。下面三个例子没有点名某份 pytest 文件，不要另编文件名。
5. 选项字母：把模型输出收成选项字母，和标准答案比较。`posttrainbench-v1-1` 的 GPQA 用 `scorer=choice()`，按它的选项结果写数字，不要改成调用 judge 模型。
6. 通过写 1，失败写 0。多个分项写 `reward.json`。单值可写 `reward.txt`。路径是 `/logs/verifier/`。

### 做完怎么核对

- 容器里有 `reward.txt` 或 `reward.json`，值是有限数。
- 两个文件都没有，安装包会给出 `RewardFileNotFoundError`。`reward.txt` 空或不是有限数，会 `RewardFileEmptyError` 或 `VerifierOutputParseError`。
- 打开 `test.sh`，里面没有第二个模型的调用。
- `osworld-verified` 的模糊匹配、感知哈希、`compare_docx_files` 的 0–1 分仍是程序规则。核对时按程序规则看，不要去配 judge 密钥。

### 坑

- `spreadsheetbench` 这一次 commit 的 `evaluation()` 把 `proc_path` 设成 `*_input.xlsx`，模型输出路径 `*_output.xlsx` 被注释。照抄会拿答案表去比输入表。转化时改成比模型输出。
- 填色和字体颜色的比较函数在，但在 `cell_level_compare` 里被注释掉。不要把它算进 reward，除非你先把比较接回去并核对过。
- 模板 `cli/template-task/tests/test.sh` 的注释写 `/logs/verifier/rewards.json`。解析器只认 `reward.json`，然后 `reward.txt`。本安装没有读取这个复数文件名的代码。脚本不要写它。

### 可勾选步骤

- [ ] 打开 SpreadsheetBench commit `49b73a94775fb489063f60ca1865e3a650079a79` 的 `evaluation/evaluation.py`。文件里有 `soft_restriction`。单元格用相等比较。这份文件里没有 judge 模型名。仓：<https://github.com/RUCKBReasoning/SpreadsheetBench>。
- [ ] 打开 PostTrainBench commit `3ed1d32ff1ec1f41282be6f8ebbcec07b19fc3d1` 的 `src/eval/tasks/gpqamain/evaluate.py`。脚本使用 `scorer=choice()`，文件里没有 `JUDGE_MODEL`。Arena Hard Writing 与 HealthBench 的 `evaluate.py` 写了 `JUDGE_MODEL`，这两题改走「要另调 judge 模型」。仓：<https://github.com/aisa-group/PostTrainBench>。
- [ ] 在 Harbor 0.23.0 安装包里打开 `verifier/verifier.py`。`reward.txt` 的容器路径是 `/logs/verifier/reward.txt`。解析器先认 `reward.json`，再认 `reward.txt`。两个都没有时停，错误名是 `RewardFileNotFoundError`。注释里的 `/logs/verifier/rewards.json` 不要写。
- [ ] pytest：上游测试是 pytest 时，`test.sh` 跑这些用例，再把通过与否写成数字。SpreadsheetBench、OSWorld-Verified、PostTrainBench 这三个例子没有点名某份 pytest 文件。不要另编文件名。没有可打开的上游测试文件就停。
- [ ] 打开同一份 SpreadsheetBench `evaluation/evaluation.py` 的 `proc_path`。当前指向 `*_input.xlsx`。`*_output.xlsx` 那行被注释。转化时改成比模型输出。没改就停在这一步。
- [ ] 打开 OSWorld commit `b138d348256078fa634fc3b73567a7337c793e6b` 的 `desktop_env/evaluators/`。模糊匹配、感知哈希、`compare_docx_files` 按程序规则看。不要去配 judge 密钥。仓：<https://github.com/xlang-ai/OSWorld>。


## 要另调 judge 模型

密钥和被测模型分开。官方没有 judge 类型。

### 开工前准备

- 记下 judge 模型名，单独准备它的密钥。被测模型的密钥放另一处。两边都不要写入 git，也不要写进读者文档。
- `charxiv` 的 `src/descriptive_utils.py` 与 `src/reasoning_utils.py` 把模型固定为 `gpt-4o-2024-05-13`。descriptive 调用使用 `temperature=0`、`top_p=1`、`seed=42`、`response_format=json_object`。`evaluate.sh` 注释写 Query GPT-4o to grade responses。评分要 `api_key`。
- `browsecomp` 的 `simple_evals.py` 在 `case "browsecomp"` 传入 `grading_sampler`，写死为 `gpt-4.1-2025-04-14`（`max_tokens=2048`）。`browsecomp_eval.py` 让模型回答 `correct: yes|no`。
- `posttrainbench-v1-1` 里，Arena Hard Writing 与 HealthBench 的 `evaluate.py` 写 `JUDGE_MODEL = "gpt-5-mini"`，并要求 `OPENAI_API_KEY`。同仓 `gsm8k`、`humaneval`、`aime2025`、`gpqamain`、`bfcl` 的脚本里没有 `JUDGE_MODEL`。合规审查里的 contamination、api-usage、ptb-lookup 用另一套模型，密钥同样分开。
- 官方没有 judge 类型。`VerifierResult` 只有数字 rewards。

### 转化步骤

1. 在 `tests/` 放下 prompt、模型名、rubric。`cli/adapter_review.py` 把 LLM judge 写成这三样，由 test 脚本自己调模型。
2. `tests/test.sh` 调用 judge，把返回收成有限数字，写入 `/logs/verifier/reward.txt` 或 `reward.json`。
3. judge 的密钥放进评分进程能读到的位置。不要和被测 agent 的密钥写成同一份。
4. 控制回路：judge 调用发生在 tests 脚本里。被测 agent 的回路在 environment 里面还是外面，按该 agent 自己的写法，不给 judge 单列类型。
5. `charxiv` 公开 JSON 里 test 的答案是 `null`。README 写 in-house 端到端评测应使用 `val`。转化时用 val 那套有答案的题，不要把空答案送去打分。

### 做完怎么核对

- 不提供 judge 密钥时，`test.sh` 失败退出，reward 文件不出现。
- 提供密钥时，reward 文件是有限数。
- job 配置里没有名为 judge 的类型字段。分数只从 reward 文件进 `VerifierResult`。
- `analyze/` 若另写了 `analysis.json`，确认 job 的分数不是从那里读的。安装包里 analyze 的 rubric 写 `analysis.json`，不写 `VerifierResult`。

### 坑

- `verifier.env` 里出现 `api_key` 时，安装包只打日志，提醒可能是 LLM-based verifier。它不会替你调用模型。
- 不要把 rubric 只放进 `analyze/`。那样分数进不了 `VerifierResult`。
- `browsecomp` 的参考实现没有浏览器。论文要求的浏览不在这个脚本里。grader 和被测模型都要调接口。只接 grader 时，浏览仍是 unknown。
- `posttrainbench-v1-1` 不要整包标成 judge。只有写了 `JUDGE_MODEL` 的下游任务，以及合规审查那些 judge，才走本节。
- `charxiv` 的评分要出网调接口。出网见下一类依赖，不要在本节假设容器默认离线。

### 可勾选步骤

- [ ] 打开评分脚本，看是否另调模型。CharXiv commit `7ebe88f78dee387691551f071abcb2b9e1a8025b` 的 `src/descriptive_utils.py` 把模型固定为 `gpt-4o-2024-05-13`。BrowseComp 所在仓 commit `652c89d0ca9df547706735883097e9537d40dc47` 的 `simple_evals.py` 在 `browsecomp` 分支传入 `grading_sampler`，模型是 `gpt-4.1-2025-04-14`。PostTrainBench 的 Arena Hard Writing 与 HealthBench `evaluate.py` 写 `JUDGE_MODEL = "gpt-5-mini"`。打不开这些文件就停，不要凭记忆写 `tests/test.sh`。
- [ ] 核对两份密钥：judge 一份，被测模型一份。两边都不写入 git，也不写入读者文档。公开材料没有给出这两份密钥的路径。没有密钥就停，不要为了勾选去跑评分。
- [ ] 打开写出的 `tests/test.sh`，确认文件名是 `/logs/verifier/reward.txt` 或 `/logs/verifier/reward.json`。两份都在时，Harbor 先读 `reward.json`。还没有这份脚本就停。
- [ ] 用 Harbor 0.23.0 的解释器执行 `from harbor.models.job.config import JobConfig; from harbor.models.verifier.result import VerifierResult; print('judge' in JobConfig.model_fields); print(list(VerifierResult.model_fields))`。输出第一行是 `False`，第二行是 `['rewards']`。`import harbor` 失败就停在这一步。
- [ ] 拿掉 judge 密钥再跑评分脚本。脚本失败退出，reward 文件不出现。没有评分脚本或没有密钥可拿掉就停。不要把没跑写成已核对。
- [ ] CharXiv 改用 README 写的 val。commit `7ebe88f78dee387691551f071abcb2b9e1a8025b` 的 `data/descriptive_test.json` 与 `data/reasoning_test.json` 答案是 `null`。打不开 val 那套有答案的题就停，不要把空答案送去打分。


## 要 GPU

### 开工前准备

- 从上游抄下数量和型号。`posttrainbench-v1-1` 的 `src/commit_utils/single_task.sub` 为 `num_gpus = 1`，`request_gpus`，要求 `NVIDIA H100 80GB HBM3`，内存 131072、16 个中央处理器（CPU）、磁盘 400G。容器要用 `--nv`。
- 分开「评分要卡」和「被测模型要卡」。`charxiv` 的评分脚本不用 GPU。`src/generate_lib/` 里多个本地模型把权重放到 CUDA（Compute Unified Device Architecture），`internvl2.py` 与 `nvlm.py` 按 `torch.cuda.device_count()` 切层。应用程序接口（API）模型路径不要求本机 GPU。
- `spreadsheetbench` 的执行器镜像安装 CPU 版 torch，Docker 限制是 8GB 内存和 2 CPU，没有 GPU device。代码执行侧不要准备显卡。
- `osworld-verified` 的评测脚本没有把本地 GPU 写成必需。`desktop_env/providers/pyromind/provider.py` 创建沙箱时写 `gpu: 0`。

### 转化步骤

1. 在 `task.toml` 的 `[environment]` 写入 `gpus`。`posttrainbench-v1-1` 的数量是 1。上游写了型号，就把型号写入 `gpu_types`。字段名用安装包已有的 `gpus`、`gpu_types`，不要新造键。
2. 镜像使用带 CUDA 的基座，或写明运行时如何把显卡传进环境。`posttrainbench-v1-1` 的 `containers/standard.def` 是 `From: nvidia/cuda:12.9.1-cudnn-devel-ubuntu22.04`，运行是 `apptainer exec --nv`。
3. 只走 API 的路径不要填 `gpus`。`charxiv` 的 API 模型路径不要求本机 GPU。
4. `environment/` 目录仍要在。见上一节关于省略目录的 unknown。

### 做完怎么核对

- 打开 `task.toml`，需要显卡的题能看到 `gpus`。
- 不需要显卡的题，`gpus` 没有被填上。`spreadsheetbench` 的执行器保持 CPU 限制。
- 跑一次环境启动。卡没有挂上时，记失败，不要把 CPU 跑通当成 GPU 已接。

### 坑

- 名词表没有 `gpus` 这一行。转化时仍要写这个键。缺 `gpus` 时有效数量是 0，不会因此改用 docker，也不会申请 H100。`environment.type` 和 `import_path` 都空时，运行时类型才默认 `docker`。Docker 这套实现的能力标志不包含 GPU；有效 GPU 数大于 0 时，环境启动前会拒绝。
- 哪个非 Docker 的 `environment.type` 会把 `gpus` 传进容器，本安装没有逐个写完。不要在 podman 到 kata 这些名字里猜。
- `posttrainbench-v1-1` 还要 16 CPU、内存 131072、磁盘 400G。只写 `gpus` 不够，`cpus`、`memory_mb`、`storage_mb` 按上游一并写入。

### 可勾选步骤

- [ ] 打开 PostTrainBench commit `3ed1d32ff1ec1f41282be6f8ebbcec07b19fc3d1` 的 `src/commit_utils/single_task.sub`。`num_gpus = 1`，型号 `NVIDIA H100 80GB HBM3`。打不开这个文件就停。
- [ ] 需要显卡的题，在写出的 `task.toml` 的 `[environment]` 里能看到 `gpus`。上游写了型号时，`gpu_types` 里有该型号。PostTrainBench 这个 commit 还没有 Harbor `task.toml`。没有写出的 `task.toml` 就停，不要假装已经接上。
- [ ] 分开「评分要卡」和「被测模型要卡」。CharXiv 的评分脚本不用 GPU。只走 API 的路径，`gpus` 留空。
- [ ] 打开 SpreadsheetBench 同一 commit 的 `code_exec_docker/Dockerfile.executor` 与 `code_exec_docker/jupyter.py`。执行器安装 CPU 版 torch。`containers.run` 限制是 8GB 内存和 2 CPU，没有 GPU device。
- [ ] PostTrainBench 再核对资源：`request_cpus = 16`、`request_memory = 131072`、`request_disk = 400G`，出处是同一份 `single_task.sub`。写进 Harbor 时用 `cpus`、`memory_mb`、`storage_mb`。没有写出的 `task.toml` 就停。
- [ ] 启动一次环境。显卡没有挂上时，把这次记成失败。没有可启动的环境就停。不要为勾选去跑完整评测。


## 要出网

默认 `NetworkMode` 是 public。限制出网要显式写。

### 开工前准备

- 列出必须访问的主机。`browsecomp` 会下载 `https://openaipublic.blob.core.windows.net/simple-evals/browse_comp_test_set.csv`，并调用被测模型与 grader 的接口。
- `charxiv` 评分要调 OpenAI 接口。图片要另从 HF 下载 `images.zip`。
- `osworld-verified` 的任务会打开真实网站。README / SETUP 有代理和 Google 账号配置，缺了对应任务会失败。首次运行还要下载虚拟机（VM）快照。
- 上游写明无出网的，把原句留下。`aa-briefcase` 的提示词写容器没有出站连接，没有代理、白名单或开关。正榜材料不公开，这句只用来决定 `network_mode`，不在这里编下载步骤。
- `spreadsheetbench` 的 `jupyter.py` 里 `containers.run` 没有 `network_mode`。运行期出网策略仓内没有写成禁网或放行，清单记 unknown。不要替它填。

### 转化步骤

1. 需要出网的题，可以省略 `network_mode`。安装包里 `NetworkMode` 的默认是 public。省略等于允许出网。
2. 要禁止出网，在 `[environment]` 写 `network_mode = "no-network"`。
3. 要限制主机，写 `network_mode = "allowlist"`，并写 `allowed_hosts`。模式名和主机名单一起写。
4. `aa-briefcase` 这类上游写明无出站的，按第 2 步写 `no-network`。题面本身不公开时，停在「暂不宜接」，见最后一节。

### 做完怎么核对

- 打开 `task.toml`。留空时按 public 读，容器能出网。
- 写了 `allowlist` 的，下面有 `allowed_hosts`，名单不是空的。
- `posttrainbench-v1-1` 的代理提示词写 Internet access is unrestricted。`run_task.sh` 的 `apptainer exec` 没有禁网参数，评判前会 `curl` `https://chatgpt.com/backend-api/codex/models`。转化结果要能做这个请求，不要写成 `no-network`。

### 坑

- 出网不是「没写就没有」。离线题留空会变成 public，容器能出网。
- 只写 `allowlist`、不写 `allowed_hosts` 时，Docker 的 `network-policy` 在 allow 模式且没有目标时拒绝全部受控 TCP 出网。不要留空名单。
- `spreadsheetbench` 的出网是 unknown。不要补一句禁网或放行。
- `osworld-verified` 缺代理或账号时，对应任务会失败。出网打开仍要准备这些账号，账号值不要写进仓库。

### 可勾选步骤

- [ ] 打开写出的 `task.toml`，读 `network_mode`。环境基线不写这个字段时，按 `NetworkMode` 的默认 `public`，容器能出网。还没有 `task.toml` 就停。
- [ ] 上游写明无出站时，确认值是 `no-network`。`aa-briefcase` 正榜题面不公开，停在暂不宜接，不写 `tests/test.sh`。公开页把它写成 private evaluation，第五场景示例不进计分榜。
- [ ] 要限制主机时，确认 `network_mode = "allowlist"`，下一行有非空的 `allowed_hosts`。没有这份 `task.toml` 就停。
- [ ] 列出必须访问的主机。BrowseComp 的 `browsecomp_eval.py`（simple-evals commit `652c89d0ca9df547706735883097e9537d40dc47`）会下载 `https://openaipublic.blob.core.windows.net/simple-evals/browse_comp_test_set.csv`，并调用被测模型与 grader 的接口。CSV 不在本手册仓库里。要接浏览回路时，先拿到这份文件再继续。明文不要落盘。
- [ ] SpreadsheetBench 的 `code_exec_docker/jupyter.py` 里 `containers.run` 没有 `network_mode`。这一题的出网保持 unknown，不补禁网或放行。
- [ ] PostTrainBench 的 `src/run_task.sh` 在 `apptainer exec` 里没有禁网参数。评判前的 `curl` 在宿主机预检，URL 是 `https://chatgpt.com/backend-api/codex/models?client_version=0.124.0`。`network_mode` 不要写成 `no-network`。不要为勾选去跑 `curl`。


## 多容器或图形桌面

### 开工前准备

- 数清容器。`spreadsheetbench` 的代码执行路径是两个镜像：`code_exec_docker/Dockerfile.api`（execute-api）和 `Dockerfile.executor`（executor）。评测脚本 `evaluation/scripts/evaluation.sh` 是本机 `python evaluation.py`，另要 LibreOffice 7.5+ 或 Windows Excel，这一步不在上述容器里。
- `osworld-verified` 的 Docker provider 运行镜像 `happysixd/osworld-docker`。有 `/dev/kvm` 时把内核虚拟机（KVM）设备传进容器，否则环境变量 `KVM=N`。镜像内是 QEMU 虚拟机。`scripts/python/run_multienv.py --provider_name docker --num_envs 10` 会并行多个环境。`monitor/docker-compose.yml` 存在，清单没有把整文件抄进来。
- `posttrainbench-v1-1` 是一个 `.sif`。清单写没看到多容器。不要把它拆成 compose。
- 准备图形题的虚拟机来源。`osworld-verified` 的 Ubuntu qcow2 在 HF，体积很大，不要放进 git。

### 转化步骤

1. 用 Compose 时，把编排放进 `environment/docker-compose.yaml`。安装包认的文件名是这个，常量 `COMPOSE_FILE_NAME`。
2. 不用 Compose 时，文档写 Harbor 没有原生多容器实现，要自己写 custom environment，用 `environment.type` 的 `import_path` 指向该类。
3. 图形桌面放进同一个 environment 定义。`osworld-verified` 把 QEMU 放在 `happysixd/osworld-docker` 里，并按宿主机有没有 `/dev/kvm` 传设备。
4. 在清单里写明 agent 进入哪个 service、verifier 是否同一 service。写不出就停在这一步。
5. 评分仍由 `tests/test.sh` 对终态比对并写 reward 文件。`osworld-verified` 的比对在 `desktop_env/evaluators/`，不另调 judge 模型。
6. `spreadsheetbench` 的公式重算留在容器外的 LibreOffice 或 Excel。转化时把这一步写进 `test.sh` 的调用顺序，不要假设 executor 容器里已经有 LibreOffice。

### 做完怎么核对

- `environment/` 里有 `docker-compose.yaml`，或者 job 的 `environment.type` 指向自定义类。
- 能指出 agent 的 service。指不出就不要标成已经接上。
- 图形题能进到桌面里的虚拟机。只起了一个空容器不算接上。
- `posttrainbench-v1-1` 的结果仍是一个环境定义，不是一组 service。

### 坑

- 把上游文件改名为 `docker-compose.yaml` 只满足文件名。agent 进哪个 service，安装包没有另写规则。写不出就停。
- `docker-compose.yml` 不是 `COMPOSE_FILE_NAME`。Docker 环境不认 `.yml`。OpenSandbox 见到 `docker-compose.yaml` 或 `docker-compose.yml` 都会拒绝。不要交 `.yml`。
- `singularity-compose.yaml` 只出现在安装包的目录注释里。本安装没有读取该文件名的代码。它是否算定义文件：unknown。
- `osworld-verified` 的 `monitor/docker-compose.yml` 用了 `.yml`。接到 Harbor 时要改成 `docker-compose.yaml`，并核对里面的 service。清单没抄全文，不要凭记忆补 service 名。

### 可勾选步骤

- [ ] 数容器个数。SpreadsheetBench 的代码执行是两个镜像：`code_exec_docker/Dockerfile.api` 和 `Dockerfile.executor`。`evaluation/scripts/evaluation.sh` 在本机跑，不在这两个容器里。打不开这两个 Dockerfile 就停。
- [ ] OSWorld 的 Docker provider 镜像是 `happysixd/osworld-docker`，里面是 QEMU。`scripts/python/run_multienv.py --provider_name docker --num_envs 10` 的个数是并行环境。打不开 `desktop_env/providers/docker/provider.py` 就停。
- [ ] PostTrainBench 的环境定义是一个 Apptainer 镜像，`containers/standard.def` 的基座是 `nvidia/cuda:12.9.1-cudnn-devel-ubuntu22.04`。不要把它拆成 compose。不要为勾选去启动环境。
- [ ] 用 Compose 时，路径是 `environment/docker-compose.yaml`。文件名对上安装包常量 `COMPOSE_FILE_NAME`。`.yml` 不交。还没有这份文件就停。
- [ ] 写出 agent 进入的 service，以及 verifier 是否同一 service。OSWorld 的 `monitor/docker-compose.yml` 是 `.yml`，树里没有 `docker-compose.yaml`。写不出 service 名就停。
- [ ] 图形题进到桌面里的虚拟机再算接上。OSWorld 的 Ubuntu qcow2 留在数据集站点，不放进 git。没有这份磁盘就停。只起了一个空容器不算接上。
- [ ] 评分结果的文件名是 `/logs/verifier/reward.txt` 或 `/logs/verifier/reward.json`。OSWorld 的比对在 `desktop_env/evaluators/`。还没有 reward 文件就停。


## 任务不公开或 gated

标暂不宜接。不要编步骤假装能下数据。

### 开工前准备

- 核对公开入口里有没有题面、输入和评分表。`aa-briefcase` 的评测页和 2026-06-18 的公告写四个场景的题面、输入和评分表保持私有。正榜 91 题没有公开 git。
- 公开示例不是正榜。HF `ArtificialAnalysis/AA-Briefcase-Lite` 的数据集卡写明：这是第五个场景里的一周，不进计分榜。
- `deepswe-v1-1` 的 HF 卡写明 held-out 评测数据是 gated，行数据未下载。卡上的任务数与 README 一致，为 113。清单末尾又写 HF `datacurve/deep-swe` 是 gated，行数据未下。
- `swe-bench-pro` 论文口径里 commercial 276 与 held-out 858 不公开，公开仓里没有。公开的 V2 是 642 个任务目录，不把整个 slug 标成暂不宜接。
- 公告点名的 Stirrup 仓库是代理框架，不是 `aa-briefcase` 的任务仓。

### 转化步骤

1. 在 `docs/registry.md` 该行的「与 Harbor 距离」写暂不宜接。
2. 不要写下载、申请通过后的拉取、解密或补全私有 rubric 的命令。
3. 不要把 Lite 示例、公开一周，写成正榜四场景或 91 题。
4. `deepswe-v1-1` 的行数据未下载。不要写一条从 gated 库取出 113 行的步骤。
5. `swe-bench-pro` 的 commercial 276 与 held-out 858 停在暂不宜接。公开的 642 个目录可以另按程序比对 verifier 做，不要把不公开的两部分算进这 642。
6. 密钥、账号、VM 口令都不要写入仓库。

### 做完怎么核对

- 仓库里没有私有题面，没有编出来的数据网址（URL），没有解密后的明文。
- `docs/registry.md` 该行的「与 Harbor 距离」是暂不宜接。
- `aa-briefcase` 的 judge 面板（Claude Opus 4.8、GPT-5.5、Gemini 3.1 Pro Preview）只作为上游事实留在清单。没有任务文件，就不写 `tests/` 去调用这个面板。

### 坑

- Lite 数据集约 99.5 MiB，含示例 mp4。把示例克隆进来，也不等于接上正榜。
- `browsecomp` 的 CSV（comma-separated values）是公开的，单元格用该行 `canary` 做异或（XOR）。明文不要落盘。这不是 gated 正榜，不要把它标成暂不宜接；也不要在文档里写出解密后的例题。
- `swe-bench-pro` 公开集的解题分是测试。抽到的 `tests/test.sh` 写 `/logs/verifier/reward.txt` 为 1 或 0。论文里的 GPT-5 只给失败轨迹分桶，不是 Resolve 率。分桶不要写成 verifier。

### 可勾选步骤

- [ ] 打开 `docs/registry.md` 的 `aa-briefcase` 行。看「与 Harbor 距离」。格子必须是「暂不宜接」。不是这个词就停。
- [ ] 正榜题面没有公开 URL。本节不要求 `tests/test.sh`，也不要求 `tests/test.bat`。没有任务文件就停，不要写 `tests/`。
- [ ] 公开示例是第五个场景里的一周，不进计分榜。不要把这一周写成正榜 91 题。
- [ ] DeepSWE 的 HF 数据集 `datacurve/deep-swe` 写明 held-out、gated。不要写从 gated 库取出 113 行的命令。行数据不在本手册里，这一步停住。
- [ ] SWE-Bench Pro 的 commercial 276 与 held-out 858 不在公开仓 commit `66f92766bba642462d4bbe5479e83f91f9211862`。这两部分停住，不为它们写 `tests/test.sh`。公开的 642 个 Harbor task 不在本节处理。

