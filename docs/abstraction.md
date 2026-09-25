# 组件抽象

名词要少，并且尽量用 Harbor 文档里已经有的词。下面的文档站指 <https://docs.harborframework.com/> ，页面未标版本。本机安装包是 0.23.0。官方词盖不住的地方只补安装包笔记里的事实。

## 种子

六个种子用来找材料。

1. `agent`。文档站把完成 task 的程序叫 Agent，见 `core-concepts`。预置集成和自定义类都算。Oracle 跑 `solution/solve.sh`，见 `core-concepts/tasks/solution`。`nop` 是另一个 agent 名。
2. `agent runtime`。文档站用 Installed agent 和 External agent 写明回路在哪，见 `core-concepts/agents/custom-agents`。Installed agent 由 Harbor 装进 task environment 再运行。External agent 的回路在 Harbor 进程里，通过 `BaseEnvironment` 操作 task environment。同一页建议新 agent 优先继承 `BaseInstalledAgent`。回路必须留在 environment 外面时，继承 `BaseAgent`。
3. `environment`。task 目录里的环境定义是 `environment/`，多数时候放 `Dockerfile` 或 `docker-compose.yaml`，也可以只设 `docker_image`，见 `core-concepts/tasks/environment` 和 `core-concepts/tasks/overview`。跑 task 的隔离环境叫 Sandbox，自定义实现继承 `BaseEnvironment`，见 `core-concepts/sandboxes/custom-sandboxes`。sandbox 页写明命令行参数 `--env` 和 job 里的 `environment.type` 使用 environment 这个名字。多容器不用 Compose 时，`core-concepts/tasks/multi-container` 写 Harbor 没有现成实现，要自己写 custom environment。
4. `grader` / `judge`。文档站用来评估 agent 的词是 Verifier，它产出 reward，见 `core-concepts`。task 目录提供 `tests/test.sh`，Windows 是 `tests/test.bat`，把数字写到 `/logs/verifier/reward.txt` 或 `reward.json`，见 `core-concepts/tasks/verifier`。RewardKit 里的 judge 是一份 TOML（Tom's Obvious Minimal Language）配置，用来做语言模型（LLM）或 agent 评分。criterion 可以是 Python 函数，也可以是这种 TOML，见 `core-concepts/rewardkit/quick-start`。要换掉默认流程时，写 `BaseVerifier`，`verify()` 返回 `VerifierResult`，见 `core-concepts/jobs/custom-verifiers`。
5. harness / dataset 接入。`core-concepts` 写 usually, a dataset corresponds to a benchmark，另外没有 benchmark 这种目录格式。一组 task 做成 Dataset，用 `dataset.toml`、git repo 或 registry。Job 是一组 trial。harness 在 Agent Sandbox Protocol 页上指 agent loop、模型调用、凭据那一侧，见 `core-concepts/sandboxes/asp`。tag `v0.23.0` 的 README 有一句 Harbor is the official harness for Terminal-Bench-2.0。Adapter 出现在该 tag 的 template-adapter README 里，是把既有 benchmark 生成成 task 目录的脚手架。文档站没有 adapter 页。
6. `prep`。准备物对上 `solution/`（给 Oracle）、`environment/` 或 `docker_image`（给镜像）、`dataset.toml` 和 `registry.json`（给数据集）。

## 官方词盖不住的地方

下面八条只抄安装包笔记，沿用已有的词。

1. Agent 与 Environment 的 `import_path` 不检查基类。错误类会在调用时失败。失败形态依赖该类缺什么方法，笔记标 unknown，要等到实际构造。
2. site-packages 的 Python 源码里没有 `LLMJudge` 或等价的 verifier 接口。`cli/adapter_review.py` 把 LLM 评分放在 `tests/` 的 prompt、model、rubric，由 test 脚本调模型后写 reward 文件。wheel 之外有没有别的基类，笔记标 unknown。
3. `cli/template-task/tests/test.sh` 的注释写 `/logs/verifier/rewards.json`。解析器先认 `reward.json`，再认 `reward.txt`。`rewards.json` 是否另有读者，笔记标 unknown。
4. 本地 dataset 目录里的 `metric.py` 不会在 `Job._resolve_dataset_metrics` 的 `is_local` 分支自动挂上。package 数据集下载后会把 `metric.py` 包成 `UvScript`。已读的 `.py` 里没有别的隐式入口。动态入口若在本树之外，笔记标 unknown。
5. `harbor adapter` 是生成期命令。运行 job 时不 import 这个类。
6. `TaskConfig` 的 `schema_version` 默认是字符串 `"1.4"`。旧键 `version` 会改名为 `schema_version`。安装包没有枚举校验。template-task 写 1.4，template-adapter 的 `task.toml` 写 1.0。1.0 会不会在别处被拒绝，笔记标 unknown。`docs/conflicts.md` 里文档站的两套写法，处理仍是 unknown。
7. `COMPOSE_FILE_NAME` 是 `docker-compose.yaml`。`docker-compose.yml` 不在这个常量里。OpenSandbox 见到 yml 会拒绝。`DockerEnvironment` 是否另认 yml，笔记标 unknown。
8. `singularity-compose.yaml` 只出现在 `models/task/paths.py` 与 `models/task/task.py` 的目录注释里。本安装没有读取该文件名的代码。它是否仍被某种环境当定义文件，笔记标 unknown。

## 删留规则

种子先留着。定轴时按这三条。

- 能放进 `task`、`dataset`、`environment`、`verifier`、`agent`、`adapter` 的，不单开一个轴。
- 某一列如果不改变「原生可接 / 轻适配 / 重改造 / 暂不宜接」，就删掉。删掉的材料留在 `notes/`。
- 新词必须写明官方哪几个词盖不住、为什么盖不住。不为了好听造词。

## 当前结论

层只有三层，这里定稿，不多加。

### 1. task

定稿是 instruction、environment、verifier。删掉 task 层会把 `terminal-bench-2-1` 和 `posttrainbench-v1-1` 混掉。「89 个终端环境任务，每题有独立环境」，「每个任务是一个基座加一个下游基准」。这只说明任务粒度不同，不是距离档。

文档里的 sandbox 和 CLI 里的 environment 是同一个东西。任务目录里的环境定义写 `environment/`。运行时选哪个实现，写在 job 或 trial 的 `environment.type`。

### 2. 运行

定稿是 agent、trial、job。agent 在 environment 里做题。trial 是一次。job 是一批 trial。job 用 metric 汇总 reward。

删掉运行层会把 `browsecomp` 和 `mcp-atlas` 混掉。`notes/sources/browsecomp/MANIFEST.md`：「官方参考实现没有浏览器或 agent 循环。」`notes/sources/mcp-atlas/MANIFEST.md`：「`services/agent-harness/` 是 TypeScript 多轮循环，CHANGELOG 写 v2.0.0 从 Python harness 换过来。」

### 3. 接入

定稿是 adapter 只生成目录，dataset 列表。adapter 只生成 task 目录。job 运行时不加载它。dataset 把 task 列出来。

删掉接入层会把 `terminal-bench-4-0` 和 `osworld-verified` 混掉。`notes/sources/terminal-bench-4-0/MANIFEST.md`：「正文给出 `harbor run -d terminal-bench/terminal-bench@4.0.0`，以及 Harbor Hub URL `https://hub.harborframework.com/datasets/terminal-bench/terminal-bench/4`。」`notes/sources/osworld-verified/MANIFEST.md`：「任务 JSON 在 git 的 `evaluation_examples/`。」

名词就用这些：task、environment、verifier、agent、dataset、adapter、trial、job、metric。

种子词的对应关系：

- grader / judge 不是新类型。评分只认 `reward.txt` 或 `reward.json`。要另调模型，就写在 tests 脚本里。
- agent runtime 不单列类型。写控制回路在 environment 里面，还是外面。
- prep 不单列类型。写进检查清单要准备的东西。

下面三点仍约束写法。不要写成已经有的官方类型。

1. LLM judge 不在 `VerifierResult` 里。`VerifierResult` 只有 rewards，值是有限的整数或浮点数。
2. 文档允许省略 environment。安装包地图把 `environment/` 当必有。冲突保持 unknown。接入时按安装包要求，目录里要有 environment。
3. `NetworkMode` 可省略。省略时默认是 public。出网不是「没写就没有」。

官方词盖不住、因此不发明新轴、只写成依赖的有：judge 模型、GPU、出网、多容器、图形桌面、gated 数据。

浏览暂不写入依赖列。缺的是「浏览属于哪一层」的仓内句。读者勿自行升成新轴。`docs/conversion-playbook.md` 写「只接 grader 时，浏览仍是 unknown」。`notes/sources/browsecomp/MANIFEST.md` 写「官方参考实现没有浏览器或 agent 循环」。这两句只说明缺依据，没有把浏览落进 task、运行或接入。

## 轻适配与重改造

对照一个 slug 打勾。用词与 `docs/registry.md` 的「与 Harbor 距离」列一致。同一句也在 `docs/layer1.md`。

- 轻适配。官方或仓内已有可对上的 Harbor task 形态：有 task 目录，或 MANIFEST、介绍卡里已写出的等价证据。
- 重改造。需要新写或大改 task、环境或评分回路。

`notes/verify/v2/08-closed-gated.md` 的原句是「`docs/layer1.md` 的轻适配要有能交出去的 task 目录」。本轮把「能交出去的 task 目录」收成上面的轻适配句。那份笔记没有写后半句：MANIFEST、介绍卡里已写出的等价证据，以及重改造这句。

名词表与 Harbor 官方词对照：

| 本仓库的词 | Harbor 官方词 |
|---|---|
| task | task。instruction、environment、verifier。 |
| environment | environment。文档里的 Sandbox 用的就是这个名字。 |
| verifier | Verifier。产出 reward。 |
| agent | Agent。 |
| dataset | Dataset。 |
| adapter | Adapter。只生成 task 目录。 |
| trial | trial。 |
| job | Job。 |
| metric | metrics。汇总 reward。 |

`swe-atlas` 因 Harbor 版本不是 0.23.0，不是原生可接。`deepswe-v1-1` 没有 v1.1 tag，所以不是原生可接。

## 仍未定的点

三条都写具体。出处是 `notes/rounds/r1-package-map.md`、`notes/rounds/r1-docs-nouns.md`，处理写在 `notes/adversarial/A1-response.md`。

1. LLM judge 不在 `VerifierResult` 里。`VerifierResult` 只有 rewards，字符串键到有限的整数或浮点数。评分文件是 `/logs/verifier/reward.json`，其次 `/logs/verifier/reward.txt`。模型调用写在 tests 脚本里。脚本可以自己调模型再写这两个文件。文档侧是 `test.sh` 调用 `rewardkit /tests`，包名 `harbor-rewardkit`。`analyze/` 的 rubric 写 `analysis.json`，不写 `VerifierResult`。模板注释里的 `rewards.json` 不是评分文件名。本安装源码里没有 `LLMJudge`。wheel 外有没有另一套基类，仍是 unknown。这不改评分约定。
2. `environment/` 在包地图里必有，文档名词里可省略。包地图写 `is_valid_dir` 要求该目录存在，缺了显式加载抛 `FileNotFoundError`。文档站 overview 与 environment 页写可以只设 `[environment].docker_image` 并省略 `environment/`。文档站未标版本。两句都留着，处理 unknown，记在 `docs/conflicts.md`。Singularity 强制 `docker_image` 是 `docker_image` 行的另一条，不拿来取消目录冲突。
3. `NetworkMode` 标成可省略，默认是 public。省略后环境能出网。另外两个值是 `no-network` 和 `allowlist`。`allowlist` 配套 `allowed_hosts`。名单为空时是拒绝还是放行，两份笔记都没写，这里不补。文档名词的官方用词节没有 `NetworkMode`。这不推翻安装包这一行的默认 public。
