# 导读

名字里带 Harbor，不代表这个 benchmark 已经能接。

本页按 Harbor 0.23.0 安装包笔记和公开文档笔记写组件地图。安装包路径都相对于 `site-packages/harbor`。笔记里没有的句子，这里写 unknown。

## 官方组件地图

文档站 <https://docs.harborframework.com/> 未标版本。旁边这句要留着：文档站上的句子不能当成 0.23.0 的定论。本机安装包版本见 `docs/sources.md`。

地图只写这九个词：task、environment、verifier、agent、dataset、adapter、trial、job、metric。

### task

安装包里，task 是一个可运行题目目录的加载结果：读 `task.toml`，校验 instruction、environment、tests。出处：`models/task/task.py`。

单题目录约定这些文件名：`instruction.md`、可选 `trajectory.json`、`task.toml`、`environment/`、`solution/`、`tests/`，多步再加 `steps/<name>/`。出处：`models/task/paths.py`。

`Task.is_valid_dir` 要求 `task.toml` 与 `environment/`。单步还要 `instruction.md`。共享 verifier 还要与 `[environment].os` 匹配的 `test.sh` 或 `test.bat`。缺文件则目录不算 task。出处：安装包笔记里的 task 目录检查；文件名约定在 `models/task/paths.py`。

文档站写 task 是一条或多条 instruction、一个 sandbox environment，外加一个 verifier，实现成 Harbor task format 的目录。出处：<https://docs.harborframework.com/core-concepts>。另一句是 an instruction, environment, and test script。出处：<https://docs.harborframework.com/core-concepts/tasks/overview>。

`task.toml` 在这里只是目录里的文件名。笔记没有给出一份可以打开的 `task.toml` 磁盘路径，路径 unknown。

### environment

文档把 sandbox 叫成 environment。文档写跑 task 的隔离环境叫 Sandbox，CLI `--env` / `-e` 和 job config `environment.type` 使用 environment 这个名字。出处：<https://docs.harborframework.com/core-concepts/sandboxes/pre-integrated-sandboxes>。

题目目录里的 `environment/` 是环境定义目录。`is_valid_dir` 要求该目录存在。里面放镜像定义，不在这里选择 docker 还是 singularity。出处：`models/task/paths.py`。文档站写这个目录多数时候放 `Dockerfile` 或 `docker-compose.yaml`。出处：<https://docs.harborframework.com/core-concepts/tasks/environment>。

运行期仍要 `docker_image`、`Dockerfile` 或 `docker-compose.yaml` 之一，否则 `FileNotFoundError`。出处：`environments/definition.py`。

`NetworkMode` 可省略时默认 `public`。另外两个取值是 `no-network` 和 `allowlist`。出处：`models/task/config.py`。

`EnvironmentType` 是运行时 sandbox 枚举，不是 `task.toml` 字段。trial 和 job 的 environment 类型都空时，默认 `docker`。出处：`models/environment_type.py`。默认 `docker` 这一句的安装包行为见笔记里的 `set_default_type`。

### verifier

verifier 只认 `reward.txt` 或 `reward.json`，没有 LLM judge 类型。

默认评分器上传 tests，执行 `test.sh` 或 `test.bat`，再读 reward 文件。解析器先认 `reward.json`，再认 `reward.txt`。出处：`verifier/verifier.py`。

`reward.txt` 解析成 `{"reward": float}`，容器路径 `/logs/verifier/reward.txt`。`reward.json` 是多键奖励，优先于 `reward.txt`。出处：`models/trial/paths.py`。两个文件都没有则 `RewardFileNotFoundError`。这个错误名见安装包笔记对 `verifier/verifier.py` 的说明。

本安装的 Python 源码里没有 `LLMJudge` 或等价 verifier 接口，也没有名为 LLM judge 的类或方法。`cli/adapter_review.py` 把 LLM 评分写成 `tests/` 里的 prompt、model、rubric，由 test 脚本自己调模型，再写 reward 文件。`verifier/verifier.py` 只在 `verifier.env` 里出现 `api_key` 时打日志。未随这个 wheel 安装的 LLM judge 基类是否存在：unknown。

文档站写 verifier 评估 agent 的工作并产出 reward，且必须把数值写到 `/logs/verifier/` 的 `reward.txt` 或 `reward.json`，两者都在时优先 `reward.json`。出处：<https://docs.harborframework.com/core-concepts>，<https://docs.harborframework.com/core-concepts/tasks/verifier>。

### agent

文档站写 agent 是完成 task 的程序，预置集成，或用 `BaseAgent` 自己写。出处：<https://docs.harborframework.com/core-concepts>。

安装包里 `BaseAgent` 有 `name`、`version`、`setup`、`run`。出处：`agents/base.py`。内置名字走 `AgentFactory`，`module.path:ClassName` 走 `import_path`。出处：`agents/factory.py`。

task 目录不包含 agent 实现。文档站没写新 agent 要往任务目录加哪个文件。出处：<https://docs.harborframework.com/core-concepts/agents/custom-agents>。

### dataset

安装包里 dataset 是一组要一起跑的 task。来源有本地目录、package、registry、git repo 四种。出处：`models/job/config.py`。

package 清单文件名是 `dataset.toml`。里面必填 `[dataset]`，可选 `[[tasks]]`。出处：`models/dataset/manifest.py`。文件名约定出处：`models/dataset/paths.py`。

文档站写 dataset 是 task 的集合，用于 evaluation 和 training。出处：<https://docs.harborframework.com/core-concepts/datasets/datasets>。文档站没有单独的 benchmark 类型，只写 usually, a dataset corresponds to a benchmark。出处：<https://docs.harborframework.com/core-concepts>。

### adapter

adapter 只生成 task 目录，job 不加载它。

安装包里它是子命令 `harbor adapter` 的生成期脚手架，不是运行时插件。`init` 复制 template-adapter，`review` 做结构检查。出处：`cli/adapters.py`。模板约定 `run()` 把上游题写成 Harbor task 目录。出处：`cli/template-adapter/adapter.py.tmpl`。运行 job 不 import 这个类。

文档站当前没有 adapter 页。tag `v0.23.0` 的模板 README 把它写成把既有 benchmark 生成成 Harbor task 目录的脚手架。出处：<https://github.com/harbor-framework/harbor/blob/v0.23.0/src/harbor/cli/template-adapter/README.md>。

### trial

文档站写 trial 是一个 agent 对一个 task 的一次尝试。出处：<https://docs.harborframework.com/core-concepts>。

安装包里 trial 是一次具体运行的生命周期，带 environment、agent、verifier、hooks、result。出处：`trial/trial.py`。

### job

安装包里 job 是一组 trial 的唯一启动入口。它把 datasets 与 tasks、agents 展开成 trial，并汇总 metric。出处：`job.py`。job 不加载 adapter。这一句的出处是 `cli/adapters.py`：运行 job 不 import adapter 类。

文档站写 job 是一组 trial，用来评估 agents 和 models。出处：<https://docs.harborframework.com/core-concepts>。

### metric

文档站写 metrics 是把一个 job 或 dataset 里各 task 的 rewards 聚合起来的规则。默认对 task 取平均，缺失 reward 当 0。出处：<https://docs.harborframework.com/core-concepts/datasets/metrics>。

安装包里 `MetricType` 只有 `sum`、`min`、`max`、`mean`、`uv-script`。出处：`models/metric/type.py`。列表为空时 job 补上 mean。出处：`metrics/mean.py`。

## 词表

每个词一行。中文一句。出处一条。

| 词 | 中文 | 出处 |
|---|---|---|
| task | 一个可运行题目目录的加载结果，读 task.toml，并校验 instruction、environment 和 tests。 | 安装包 `models/task/task.py` |
| environment | 文档把跑 task 的 sandbox 叫成 environment，命令行 `--env` 和 job 配置 `environment.type` 用的就是这个名字。 | <https://docs.harborframework.com/core-concepts/sandboxes/pre-integrated-sandboxes> |
| verifier | 默认评分器执行测试脚本后读取 reward 文件，解析器先认 reward.json，再认 reward.txt。 | 安装包 `verifier/verifier.py` |
| agent | 完成 task 的程序，可以是预置集成，也可以用 BaseAgent 自己写。 | <https://docs.harborframework.com/core-concepts> |
| dataset | 一组要一起跑的 task，来源是本地目录、package、registry 或 git repo。 | 安装包 `models/job/config.py` |
| adapter | 生成期脚手架，只把上游题写成 task 目录，job 运行时不加载它。 | 安装包 `cli/adapters.py` |
| trial | 一个 agent 对一个 task 的一次尝试。 | <https://docs.harborframework.com/core-concepts> |
| job | 一组 trial 的唯一启动入口，把 datasets、tasks、agents 展开，并汇总 metric。 | 安装包 `job.py` |
| metric | 安装包里的汇总类型只有 sum、min、max、mean、uv-script。 | 安装包 `models/metric/type.py` |

## 扩展点

接一个新 benchmark 时，实际要碰的是 task 目录和 dataset 列表。

task 目录里对应三块：

- instruction。单步任务是 `instruction.md`。多步任务改放在每个 step 目录里。出处：`models/task/paths.py`。
- environment。目录 `environment/` 必须在。运行期定义还要 `docker_image`、`Dockerfile` 或 `docker-compose.yaml` 之一。出处：`models/task/paths.py`，`environments/definition.py`。
- verifier。共享评分时要有与操作系统匹配的 `tests/test.sh` 或 `tests/test.bat`。脚本把结果写成 `reward.json` 或 `reward.txt`。出处：`models/task/paths.py`，`verifier/verifier.py`。

dataset 列表把这些 task 放在一起跑。安装包认四种来源：本地目录、package、registry、git repo。package 的任务列表在 `dataset.toml` 的 `[[tasks]]`。出处：`models/job/config.py`，`models/dataset/manifest.py`。

文档站没有名为「接一个新 benchmark」的步骤。它写明的邻近做法是把多个 task 目录收成 dataset。出处：<https://docs.harborframework.com/core-concepts/datasets/create-a-dataset>。

adapter 可以生成上述 task 目录。job 不加载它，所以它不是运行时要注册的扩展点。出处：`cli/adapters.py`。

## 本机 harbor --help 看到的命令

2026-09-24 本机执行 `harbor --help`，子命令是：`check`、`analyze`、`init`、`run`、`exec`、`publish`、`upload`、`add`、`download`、`remove`、`sync`、`view`、`adapter`、`agent`、`task`、`dataset`、`job`、`hub`、`trial`、`cache`、`plugins`、`auth`、`version`。

上面是命令清单。它不是扩展点地图。

## 怎么用

先核对版本，再查这一题的距离，然后按对应的清单做。

1. 打开 `docs/sources.md`，确认本机是 Harbor 0.23.0。文档站没有标版本，站上的句子不能单独当成 0.23.0 的定论。
2. 用本页词表看 task、environment、verifier、agent、dataset、adapter、trial、job、metric 各指什么。
3. 在 `docs/registry.md` 查这一题的「与 Harbor 距离」。格子是 `unknown` 时，不要当成能接。未核实的 slug 写在 `notes/final-report.md`。
这五题勿当能接：`mmmu-pro`、`mathvision`、`video-mme`、`automationbench`、`nl2repo-bench`，距离保持 `unknown`。缺的是清单没写评测是否不要 GPU，`nl2repo-bench` 还没写死两个镜像算不算多容器。`programbench` 距离也是 `unknown`：原标轻适配但缺 `task.toml`，勿当能接。轻适配和重改造的打勾句在 `docs/layer1.md`。
4. 距离不是 `unknown` 时，打开 `docs/conversion-playbook.md` 里对应的节，按 `- [ ]` 做。要另调模型、要 GPU、要出网、多容器或图形桌面，各有一节。任务不公开或 gated 的，停在暂不宜接，不要写 `tests/test.sh`。
`docs/conversion-playbook.md` 的例子盖住 8 个 slug（`spreadsheetbench`、`posttrainbench-v1-1`、`osworld-verified`、`charxiv`、`browsecomp`、`aa-briefcase`、`deepswe-v1-1`、`swe-bench-pro`），其余 44 个不在这份清单里，因为例子只来自本轮打开过的 MANIFEST，52 题没有全部抽象完。

名词为什么收成这三层，看 `docs/abstraction.md`。

## 未知

- 一份具体 `task.toml` 的磁盘路径：笔记没给，unknown。
- `singularity-compose.yaml` 是否仍被某种环境当定义文件：unknown。它只出现在 `models/task/paths.py` 与 `models/task/task.py` 的目录注释里。
- `cli/template-task/tests/test.sh` 注释里的 `/logs/verifier/rewards.json` 是否另有读者：unknown。解析器只认 `reward.json`，然后 `reward.txt`。
- template-adapter 的 `task.toml` 写 `schema_version` `1.0` 时，0.23.0 运行时是否被别处拒绝：unknown。笔记没给这个 `task.toml` 的磁盘路径。
- 未随这个 wheel 安装的 LLM judge 基类是否存在：unknown。
- `DockerEnvironment` 是否另认 `docker-compose.yml`：unknown。官方常量 `COMPOSE_FILE_NAME` 是 `docker-compose.yaml`。出处：`environments/definition.py`。
