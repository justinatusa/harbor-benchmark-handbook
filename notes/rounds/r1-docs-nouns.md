# R1 公开文档名词

记录范围：公开文档站，加上 GitHub tag `v0.23.0` 上能对上的发布信息与 adapter 模板。不读本机已安装包，不裁决 taxonomy。

文档站未标版本，不能当成 0.23.0 定论。

## 版本

查询入口是 `https://github.com/laude-institute/harbor`。Git refs API 返回的 `url` 落在 `harbor-framework/harbor`，两边的 `v0.23.0` 是同一对象。

- tag 名：`v0.23.0`
- annotated tag 对象 SHA：`3c305dc5611e3600afc3c818735a82322f0264f8`
- tag 指向的 commit：`1e5c5c6db929a10a140d05e606882c671ae20729`
- tagger：Alex Shaw，`2026-09-12T04:55:13Z`
- GitHub Release 页标注 Published：`2026-09-12T04:55:17Z`，作者 `alexgshaw`
- Release 页仓库名：`harbor-framework/harbor`
- 该 commit 的 `pyproject.toml` 写 `version = "0.23.0"`。这只证明 tag 上的包版本，不能给文档站盖章。
- 出处：`https://github.com/laude-institute/harbor/releases/tag/v0.23.0`，`https://api.github.com/repos/harbor-framework/harbor/git/tags/3c305dc5611e3600afc3c818735a82322f0264f8`，`https://raw.githubusercontent.com/harbor-framework/harbor/v0.23.0/pyproject.toml`

文档站证据：

- `https://docs.harborframework.com/llms.txt` 无版本号。
- `https://docs.harborframework.com/changelog` 的条目没有 release 版本标题。
- `https://docs.harborframework.com/contributing/release-policy` 把 `0.22.x` 到 `0.23.0` 当作 minor release 的例子，不是「本文档对应 0.23.0」。
- tag 上的 `CHANGELOG.md` 开头仍是多段 `Unreleased`，没有 `## 0.23.0` 标题。出处：`https://github.com/harbor-framework/harbor/blob/v0.23.0/CHANGELOG.md`

## 读过的 URL

文档站首页与索引：

- `https://harborframework.com/docs`（307 到 `https://www.harborframework.com/docs`，正文与下面的 docs 根相同）
- `https://docs.harborframework.com/`
- `https://docs.harborframework.com/llms.txt`

任务：

- `https://docs.harborframework.com/core-concepts/tasks/overview`
- `https://docs.harborframework.com/core-concepts/tasks/instruction`
- `https://docs.harborframework.com/core-concepts/tasks/configuration`
- `https://docs.harborframework.com/core-concepts/tasks/environment`
- `https://docs.harborframework.com/core-concepts/tasks/skills`
- `https://docs.harborframework.com/core-concepts/tasks/solution`
- `https://docs.harborframework.com/core-concepts/tasks/verifier`
- `https://docs.harborframework.com/core-concepts/tasks/artifacts`
- `https://docs.harborframework.com/core-concepts/tasks/resources`
- `https://docs.harborframework.com/core-concepts/tasks/multi-container`
- `https://docs.harborframework.com/core-concepts/tasks/multi-step`
- `https://docs.harborframework.com/core-concepts/tasks/separate-verifier`
- `https://docs.harborframework.com/tutorials/create-a-task`

数据集、registry、metric：

- `https://docs.harborframework.com/core-concepts/datasets/datasets`
- `https://docs.harborframework.com/core-concepts/datasets/create-a-dataset`
- `https://docs.harborframework.com/core-concepts/datasets/git-repos`
- `https://docs.harborframework.com/core-concepts/datasets/registries`
- `https://docs.harborframework.com/core-concepts/datasets/metrics`
- `https://docs.harborframework.com/news/harbor-registry`

agent、environment / sandbox、verifier：

- `https://docs.harborframework.com/core-concepts/index`
- `https://docs.harborframework.com/core-concepts/agents/pre-integrated-agents`
- `https://docs.harborframework.com/core-concepts/agents/acp`
- `https://docs.harborframework.com/core-concepts/agents/custom-agents`
- `https://docs.harborframework.com/core-concepts/agents/atif`
- `https://docs.harborframework.com/core-concepts/sandboxes/pre-integrated-sandboxes`
- `https://docs.harborframework.com/core-concepts/sandboxes/asp`
- `https://docs.harborframework.com/core-concepts/sandboxes/custom-sandboxes`
- `https://docs.harborframework.com/core-concepts/jobs/custom-verifiers`
- `https://docs.harborframework.com/core-concepts/jobs/run-a-job`
- `https://docs.harborframework.com/core-concepts/jobs/artifact-collection`
- `https://docs.harborframework.com/getting-started/quick-start`

RewardKit、plugin、发布政策：

- `https://docs.harborframework.com/core-concepts/rewardkit/quick-start`
- `https://docs.harborframework.com/core-concepts/rewardkit/motivation-and-design`
- `https://docs.harborframework.com/core-concepts/plugins/existing-plugins`
- `https://docs.harborframework.com/core-concepts/plugins/custom-plugins`
- `https://docs.harborframework.com/contributing/contributing`
- `https://docs.harborframework.com/contributing/release-policy`
- `https://docs.harborframework.com/changelog`
- `https://docs.harborframework.com/news`

adapter 相关（文档站当前没有这一页）：

- `https://www.harborframework.com/docs/datasets/adapters`：HTTP 308，`Location: https://docs.harborframework.com/`
- `https://www.harborframework.com/docs/datasets/adapters-human`：同样 308 到文档根
- `https://docs.harborframework.com/datasets/adapters`：HTTP 404
- `https://docs.harborframework.com/datasets/adapters.md`：HTTP 404
- GitHub tag 模板：`https://github.com/harbor-framework/harbor/blob/v0.23.0/src/harbor/cli/template-adapter/README.md`

`llms.txt` 全文索引里没有 adapter、benchmark、metric 以外的同名专页。benchmark 没有专页。

## 官方用词

每条保持文档原名。定义只覆盖该 URL 写出的意思。

- Harbor：一个可以让任意 agent、任意 model、任意 task、任意 sandbox 并行运行的框架。出处：`https://docs.harborframework.com/`
- Task：一条或多条 instruction、一个 sandbox environment，外加一个 verifier；实现成 Harbor task format 的目录。出处：`https://docs.harborframework.com/core-concepts`
- Task（另一句官方定义）：an instruction, environment, and test script。出处：`https://docs.harborframework.com/core-concepts/tasks/overview`
- `instruction.md`：trial 开始时交给 agent 的 markdown，规定要在 environment 里完成的事。出处：`https://docs.harborframework.com/core-concepts/tasks/instruction`
- `task.toml`：task configuration 与 metadata。出处：`https://docs.harborframework.com/core-concepts/tasks/configuration`
- `schema_version`：task configuration format 的版本；字段参考页示例是 `"1.3"`。出处：`https://docs.harborframework.com/core-concepts/tasks/configuration`
- `environment/`：agent 与 verifier 运行其中的环境定义目录，多数时候放 `Dockerfile` 或 `docker-compose.yaml`。出处：`https://docs.harborframework.com/core-concepts/tasks/environment`
- Environment（运行时类型）：一个 `BaseEnvironment` 实现，方法是 `exec`、`upload_file`、`upload_dir`、`download_file`、`download_dir`、`start`、`stop`。出处：`https://docs.harborframework.com/core-concepts/tasks/environment`
- Sandbox：跑 task 的隔离环境；文档写明 CLI `--env`/`-e` 和 job config `environment.type` 把 sandbox 叫成 environment。出处：`https://docs.harborframework.com/core-concepts/sandboxes/pre-integrated-sandboxes`
- `BaseEnvironment`：自定义 sandbox 要实现的接口。出处：`https://docs.harborframework.com/core-concepts/sandboxes/custom-sandboxes`
- `solution/`：可选参考脚本目录，给 oracle agent 用来检查 task 是否可解。出处：`https://docs.harborframework.com/core-concepts/tasks/solution`
- Oracle：跑 `solution/solve.sh` 的 agent；没有 `solution/` 就不能跑。出处：`https://docs.harborframework.com/core-concepts/tasks/solution`
- Verifier：评估 agent 的工作并产出 task 的 reward。出处：`https://docs.harborframework.com/core-concepts`
- `tests/test.sh`：verifier 的 entrypoint；Linux 必需，Windows 是 `tests/test.bat`。出处：`https://docs.harborframework.com/core-concepts/tasks/verifier`
- `reward.txt` / `reward.json`：verifier 必须写到 `/logs/verifier/` 的数值 reward；两者都在时 Harbor 优先 `reward.json`。出处：`https://docs.harborframework.com/core-concepts/tasks/verifier`
- RewardKit：文档标题作 Rewardkit，包名 `harbor-rewardkit`，命令 `rewardkit`；用来定义 verifier，对 workspace 与 trajectory 跑 criteria 并写 JSON 分数。出处：`https://docs.harborframework.com/core-concepts/rewardkit/quick-start`
- criterion：RewardKit 里的评分单元，可以是 Python 函数或 TOML judge。出处：`https://docs.harborframework.com/core-concepts/rewardkit/quick-start`
- judge：用 TOML 配置的 LLM 或 agent 评分。出处：`https://docs.harborframework.com/core-concepts/rewardkit/quick-start`
- `BaseVerifier`：默认 `Verifier` 的接口；自定义类用 `verify()` 返回 `VerifierResult`，由 job config `verifier.import_path` 选择。出处：`https://docs.harborframework.com/core-concepts/jobs/custom-verifiers`
- Dataset：task 的集合，用于 evaluation 和 training；有时定义自定义 metrics 来聚合 task rewards。出处：`https://docs.harborframework.com/core-concepts/datasets/datasets`
- benchmark：文档没有单独类型定义。Core concepts 写 usually, a dataset corresponds to a benchmark，例子是 Terminal-Bench 或 SWE-Bench Verified。出处：`https://docs.harborframework.com/core-concepts`
- `dataset.toml`：显式 dataset 的 manifest，里面是指向 task 目录的指针。出处：`https://docs.harborframework.com/core-concepts/datasets/create-a-dataset`
- `registry.json`：自定义 registry 的 JSON 数组，每个元素是一个 dataset 版本，必填 `name`、`version`、`description`、`tasks`，可选 `metrics`。出处：`https://docs.harborframework.com/core-concepts/datasets/registries`
- Registry：默认是 Harbor Hub；也可用 `--registry-url` 或 `--registry-path`。出处：`https://docs.harborframework.com/core-concepts/datasets/registries`
- Metrics：把一个 job 或 dataset 里各 task 的 rewards 聚合起来的规则；默认对 task 取平均，缺失 reward 当 0。出处：`https://docs.harborframework.com/core-concepts/datasets/metrics`
- `metric.py`：自定义 metric 脚本，参数是 `-i/--input-path` 与 `-o/--output-path`。出处：`https://docs.harborframework.com/core-concepts/datasets/metrics`
- Agent：完成 task 的程序；预置集成，或用 `BaseAgent` 写自定义 agent。出处：`https://docs.harborframework.com/core-concepts`
- Installed agent：Harbor 在 task environment 里安装并运行的 agent CLI。出处：`https://docs.harborframework.com/core-concepts/agents/custom-agents`
- External agent：agent loop 跑在 Harbor 里，通过 `BaseEnvironment` 控制 task environment。出处：`https://docs.harborframework.com/core-concepts/agents/custom-agents`
- `BaseInstalledAgent`：文档建议新 agent 优先继承的基类。出处：`https://docs.harborframework.com/core-concepts/agents/custom-agents`
- `BaseAgent`：agent loop 必须留在 task environment 外面时用的基类。出处：`https://docs.harborframework.com/core-concepts/agents/custom-agents`
- ACP：Agent Client Protocol；Harbor 的 `acp` 集成从 ACP Registry 安装并在 task environment 里运行 agent。出处：`https://docs.harborframework.com/core-concepts/agents/acp`
- Trial：一个 agent 对一个 task 的一次尝试。出处：`https://docs.harborframework.com/core-concepts`
- Job：一组 trial，用来评估 agents 和 models；可以组合 datasets、agents、tasks、models。出处：`https://docs.harborframework.com/core-concepts`
- Model：文档把它和 agent 并列成 job 的输入（`-m` / `model_name`），没有单独定义页。出处：`https://docs.harborframework.com/core-concepts/jobs/run-a-job`
- Trajectory：agent 与 user 完成 task 时的对话和动作历史。出处：`https://docs.harborframework.com/core-concepts`
- ATIF：Agent Trajectory Interchange Format，用 JSON 记录 messages、reasoning、tool calls、observations、metrics。出处：`https://docs.harborframework.com/core-concepts/agents/atif`
- Skill：一个含 `SKILL.md` 的目录，随 task environment 发给每个跑该 task 的 agent。出处：`https://docs.harborframework.com/core-concepts/tasks/skills`
- Artifact：agent 跑完后从 sandbox 收集的 file 或 directory，在 `task.toml` 的 `artifacts` 里声明。出处：`https://docs.harborframework.com/core-concepts/tasks/artifacts`
- Plugin：跑在 Harbor 进程里、响应 job 与 trial 事件的接口；自定义类继承 `BaseJobPlugin`。出处：`https://docs.harborframework.com/core-concepts/plugins/custom-plugins`
- MCP：在 environment 页里，可用的 MCP server 用 `[[environment.mcp_servers]]` 声明，供兼容 agent 自动注册。出处：`https://docs.harborframework.com/core-concepts/tasks/environment`
- Multi-step task：把验证插进 agent run 的中途，并测量 agent 从上一 session 继续工作的能力；目录用 `steps/<name>/`。出处：`https://docs.harborframework.com/core-concepts/tasks/multi-step`
- `workdir/`：某个 step 开始前拷进 agent working directory 的文件，可选 `setup.sh`。出处：`https://docs.harborframework.com/core-concepts/tasks/multi-step`
- ASP：Agent Sandbox Protocol；让任意 agent harness 的 tools 经 SSH 在远程 sandbox 里执行。该页标明是 RFC draft。出处：`https://docs.harborframework.com/core-concepts/sandboxes/asp`
- harness：ASP 页用来指 agent loop、LLM calls、credentials 那一侧，和执行 tools 的 sandbox 相对。出处：`https://docs.harborframework.com/core-concepts/sandboxes/asp`
- Rollout：文档首页图的节点名是 `Harbor Rollout Engine`，没有定义成一种目录或对象。出处：`https://docs.harborframework.com/`
- Harbor Hub：发布 dataset 与 task 的注册处；新闻稿把 task 称为 registry 的 atomic unit。出处：`https://docs.harborframework.com/news/harbor-registry`

GitHub `v0.23.0` 才出现、文档站索引没有的词：

- Adapter：tag 上的模板 README 标题是 `{{BENCHMARK_NAME}} → Harbor Adapter`。它是一段把既有 benchmark 生成成 Harbor task 目录的 Python 包脚手架，默认输出 `datasets/{{ADAPTER_ID}}/`，代码放 `adapters/{{ADAPTER_ID}}/`，类上要有 `run()`。这是仓库模板，不是文档站当前页面。出处：`https://github.com/harbor-framework/harbor/blob/v0.23.0/src/harbor/cli/template-adapter/README.md`
- 同名但不是上面那个 Adapter：该 tag 的 `pyproject.toml` 有 optional extra `adapter = ["claude-agent-sdk>=0.1.17"]`。出处：`https://raw.githubusercontent.com/harbor-framework/harbor/v0.23.0/pyproject.toml`
- 同 tag README 另有一句：Harbor is the official harness for Terminal-Bench-2.0，并写可以 build and share your own benchmarks and environments，以及 generate rollouts。出处：`https://github.com/harbor-framework/harbor/blob/v0.23.0/README.md`

## 文档写明的扩展点

### 新 benchmark

文档站没有名为「接一个新 benchmark」的步骤，也没有 adapter 页。

它写明的邻近做法是做一个 dataset：

- 把多个 task 目录放在一起，形成 implicit dataset，用 `harbor run -p`。出处：`https://docs.harborframework.com/core-concepts/datasets/create-a-dataset`
- 或写 `dataset.toml`：`harbor dataset init "<org/name>"`，再用 `harbor dataset add`。出处同上。
- 发布：`harbor publish "<org/name>"`。出处同上。新闻稿另写 `harbor init --task` 与 `harbor init --dataset`。出处：`https://docs.harborframework.com/news/harbor-registry`
- Git 仓库：根上可选 `registry.json`，默认把 `tasks/` 当 implicit dataset，用 `harbor run --repo`。出处：`https://docs.harborframework.com/core-concepts/datasets/git-repos`
- 自定义 registry：提供带 `tasks[].git_url`、`git_commit_id`、`path` 的 `registry.json`，可选 `metrics`。出处：`https://docs.harborframework.com/core-concepts/datasets/registries`
- 自定义聚合：dataset 目录放 `metric.py`，或 `harbor init --dataset "<org>/<name>" --with-metric`。出处：`https://docs.harborframework.com/core-concepts/datasets/metrics`

文档站没写：从外部 benchmark 生成 task、parity、`adapters/` 包、`harbor datasets list`。这些只出现在 tag `v0.23.0` 的 README 与 `template-adapter/README.md`。该模板还要求把 task 目录上传到 `https://github.com/laude-institute/harbor-datasets` 并改仓库里的 `registry.json`。那是 GitHub 模板说明，不是当前文档站步骤。模板指向的文档 URL 现在 308/404，见上文。

### 新 agent

文档写了：

- 优先继承 `BaseInstalledAgent`，实现 `name()`、`install()`、`run()`。agent loop 必须在 environment 外时才继承 `BaseAgent`，实现 `name()`、`version()`、`setup()`、`run()`。出处：`https://docs.harborframework.com/core-concepts/agents/custom-agents`
- 自定义 agent 不按名字注册。`--agent` / `-a` 传 `module.path:ClassName`，模块要能被 Harbor 进程 import。出处同上。
- 已有安装包走预置名字，或 `acp:<agent_id>` / `acp:<agent_id>@<version>`。出处：`https://docs.harborframework.com/core-concepts/agents/pre-integrated-agents`，`https://docs.harborframework.com/core-concepts/agents/acp`
- 要进上游时，Contributing 只要求至少有一个用户要过这个集成；改接口或 Harbor format 要先写 `rfcs/` 里的 RFC。出处：`https://docs.harborframework.com/contributing/contributing`

文档没写：新 agent 在任务目录里要加哪个文件。agent 类不在 task 目录中。

### 新 environment

文档把「新 sandbox」和「task 自己的 environment 定义」分成两件事。

新 sandbox / 新 runtime：

- 继承 `BaseEnvironment`，实现 lifecycle、`exec`、文件传输，并用 `_validate_definition()` 检查 task 缺了哪些文件。`--env` / `-e` 传 `module.path:ClassName`。出处：`https://docs.harborframework.com/core-concepts/sandboxes/custom-sandboxes`
- 多容器若不用 Compose，文档写 Harbor 没有原生实现，用户可以自己实现 custom environment。出处：`https://docs.harborframework.com/core-concepts/tasks/multi-container`
- 上游集成的门槛与 agent 相同：有人要过即可。出处：`https://docs.harborframework.com/contributing/contributing`

task 目录里的 environment：

- 放 `environment/Dockerfile`，或 `environment/docker-compose.yaml`，或其他 Harbor 支持的 spec；也可以只设 `[environment].docker_image` 并省略 `environment/`。出处：`https://docs.harborframework.com/core-concepts/tasks/overview`，`https://docs.harborframework.com/core-concepts/tasks/environment`
- 文档没写一份「任意新 spec 的接入清单」，只写 consumer 得支持该 spec。

### 新 verifier

文档写了三条彼此不同的路：

- task 目录：提供 `tests/test.sh`（Windows 为 `tests/test.bat`），把数字写到 `/logs/verifier/reward.txt` 或 `reward.json`。出处：`https://docs.harborframework.com/core-concepts/tasks/verifier`
- 单独 verifier sandbox：`[verifier] environment_mode = "separate"`，或增加 `[verifier.environment]`。专用镜像要自己带 `/tests/test.sh`；也可用 `tests/Dockerfile`。出处：`https://docs.harborframework.com/core-concepts/tasks/separate-verifier`
- RewardKit：在 `tests/` 放 Python criteria 与 judge TOML，由 `test.sh` 调用 `rewardkit /tests`。出处：`https://docs.harborframework.com/core-concepts/rewardkit/quick-start`
- 换掉默认流程：写可 import 的 `BaseVerifier`，`harbor run --verifier module:Class`。文档写明它替换默认 workflow，上传、命令和算分都要自己做。出处：`https://docs.harborframework.com/core-concepts/jobs/custom-verifiers`

文档没写：如何把一个新 verifier 注册成内置名字。自定义 verifier 在 job config 里，不在 task 目录里。

## 文档里出现、但讲不清怎么对应到任务目录的词

这些词在已读页面里出现。下面只记它们和 task 目录对不上的点，不把它们收成一类。

- benchmark：被说成通常对应一个 dataset，也出现在 news 标题和 “published benchmarks” 里。没有 benchmark 目录格式。
- adapter：当前文档站没有这个词的页面。tag 模板把生成结果放进 `datasets/<id>/<task_id>/`，适配器代码在 `adapters/<id>/`，两处都不是单个 task 目录的必选成员。
- sandbox 与 environment：task 目录里有 `environment/`；CLI 的 environment 又是 sandbox 实现。同一页承认这个名字不好。一个 task 目录看不出跑在哪个 sandbox。
- agent：task 目录不包含 agent 实现。`[agent]` 只是 `task.toml` 里的 timeout、user、network。`BaseAgent` 在 Harbor 进程里。
- model：只是 `harbor run -m` 的参数，task 目录无此文件。
- job、trial：跑出来的结果，不是 task 目录的子树。文档用 `jobs/` 当输出目录例子。
- trajectory、ATIF、`trajectory.json`：写在 trial 的 agent log，下载后路径是 `agent/trajectory.json`，不是 task 源目录。ATIF 页写当前格式 `ATIF-v1.7`，changelog 又写 ATIF v1.8。
- dataset、`dataset.toml`、`registry.json`、`metric.py`：都在 task 目录外边。registry 里的 task 只是 `name` + `path`，可选 git 字段。
- plugin：`--plugin` 运行时参数，文档写明不进 `config.json`，更不进 task 目录。
- rollout、harness：首页和 ASP / tag README 用了这两个词，没有对应到 task 子目录。
- oracle、`nop`：是 agent 名。oracle 消费 `solution/`，但 oracle 本身不是目录。
- skill：可以烘焙进镜像并由 `environment.skills_dir` 指向；job 级 skill 又会上传进该目录或 `/harbor/skills`。任务树里的 `environment/skills/` 只是文档示例，不是唯一位置。
- MCP：声明在 `task.toml` 的 `[[environment.mcp_servers]]`，实现可以是 compose sidecar，也可以是外部 URL。environment 页的 “MCPs” 标题下面先写了 docker-compose。
- ASP、`.asp.json`：harness 侧的连接文件，页上写由 orchestrator 在 agent 启动前准备。不是 task format 列出的文件。
- reward：既是 `/logs/verifier/` 里的运行时文件，又是 RewardKit 的 JSON 键，又是 dataset metric 的输入。源 task 目录里没有 `reward` 文件。
- criterion、judge：可放在 `tests/`，也可以是 RewardKit 包里的 built-in。目录结构决定分数名，但包本身不在 task 里。
- `BaseVerifier`：job 级 Python 类，和 `tests/test.sh` 二选一，文档没写它如何落回任务目录。
- capability：agent 或 sandbox 的功能表，不是 task 文件。
- Harbor Hub、digest、revision、tag：发布后的身份，新闻稿写开发发生在版本控制里，registry 只存 snapshot。
- 首页图里的 Analysis、Evaluation、Optimization、Task QA：只有图节点，没有目录。
- `version` 与 `schema_version`：创建教程示例写 `version = "1.0"` 和 `[metadata] author_name`；configuration 参考写 `schema_version = "1.3"` 和 `[task] authors`。看一个任务目录时，文档没有说明这两个字段谁有效。
- `harbor task init` 与 `harbor init --task`，以及 `harbor dataset init` 与 `harbor init --dataset`：两套命令都出现了，文档没写它们是否生成同一套目录。
- prompt：instruction 页说不要靠改 `instruction.md` 来改 agent prompt；prompt template 是 agent 参数，不是 task 目录项。

DOCS-NOUNS-END
