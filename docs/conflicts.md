# 冲突

两种公开说法对不上时记在这里。页面上没写的，仍可能有第二种说法。

格式：

- 对象：slug 或 Harbor 名词
- 说法 A / 来源
- 说法 B / 来源
- 处理：采 A、采 B，或继续标 `unknown`

## 记录

- 对象：task
- 说法 A / 文档站 <https://docs.harborframework.com/core-concepts>（未标版本）：一条或多条 instruction、一个 sandbox environment，外加一个 verifier，实现成 Harbor task format 的目录。
- 说法 B / 文档站 <https://docs.harborframework.com/core-concepts/tasks/overview>（未标版本）：an instruction, environment, and test script。
- 处理：unknown

- 对象：sandbox、environment
- 说法 A / 文档站 <https://docs.harborframework.com/core-concepts/sandboxes/pre-integrated-sandboxes>（未标版本）：Sandbox 是跑 task 的隔离环境。
- 说法 B / 同一页：命令行参数 `--env`、`-e` 和 job config `environment.type` 把 sandbox 叫成 environment。
- 处理：unknown

- 对象：task 配置里的版本字段
- 说法 A / 文档站 <https://docs.harborframework.com/tutorials/create-a-task>（未标版本）：示例写 `version = "1.0"`，作者在 `[metadata] author_name`。
- 说法 B / 文档站 <https://docs.harborframework.com/core-concepts/tasks/configuration>（未标版本）：示例写 `schema_version = "1.3"`，作者在 `[task] authors`。
- 处理：unknown

- 对象：Agent Trajectory Interchange Format（ATIF）
- 说法 A / 文档站 <https://docs.harborframework.com/core-concepts/agents/atif>（未标版本）：当前格式写 `ATIF-v1.7`。
- 说法 B / 文档站 <https://docs.harborframework.com/changelog>（未标版本）：写 ATIF v1.8。
- 处理：unknown

- 对象：adapter 文档页
- 说法 A / tag `v0.23.0` 的 <https://github.com/harbor-framework/harbor/blob/v0.23.0/src/harbor/cli/template-adapter/README.md>：模板指向 adapter 文档。
- 说法 B / 2026-09-25 对文档站的请求：<https://docs.harborframework.com/datasets/adapters> 与 <https://docs.harborframework.com/datasets/adapters.md> 返回 404。<https://www.harborframework.com/docs/datasets/adapters> 与 <https://www.harborframework.com/docs/datasets/adapters-human> 返回 308，落到文档根。文档站未标版本。
- 处理：unknown

- 对象：changelog 里的 0.23.0 标题
- 说法 A / <https://raw.githubusercontent.com/harbor-framework/harbor/v0.23.0/pyproject.toml>：tag `v0.23.0` 的包版本写 `version = "0.23.0"`。
- 说法 B / <https://github.com/harbor-framework/harbor/blob/v0.23.0/CHANGELOG.md> 与文档站 <https://docs.harborframework.com/changelog>（未标版本）：tag 上的 `CHANGELOG.md` 没有 `## 0.23.0` 标题，开头仍是多段 Unreleased。文档站 changelog 的条目没有 release 版本标题。
- 处理：unknown

- 对象：`harbor task init`、`harbor init --task`、`harbor dataset init`、`harbor init --dataset`
- 说法 A / 文档站 <https://docs.harborframework.com/core-concepts/datasets/create-a-dataset>（未标版本）：写 `harbor dataset init "<org/name>"`。`harbor task init` 也出现过，这一条没有单独的页面地址。
- 说法 B / 文档站 <https://docs.harborframework.com/news/harbor-registry>（未标版本）：写 `harbor init --task` 与 `harbor init --dataset`。
- 处理：unknown。文档没写这两套命令是否生成同一套目录。

- 对象：adapter
- 说法 A / <https://github.com/harbor-framework/harbor/blob/v0.23.0/src/harbor/cli/template-adapter/README.md>：Adapter 是把既有 benchmark 生成成 Harbor task 目录的 Python 脚手架，类上要有 `run()`。
- 说法 B / <https://raw.githubusercontent.com/harbor-framework/harbor/v0.23.0/pyproject.toml>：optional extra 也叫 `adapter`，依赖是 `claude-agent-sdk>=0.1.17`。
- 处理：unknown

- 对象：`BaseEnvironment` 的方法
- 说法 A / 本机 harbor 0.23.0 的 `environments/base.py`：要实现 `type`、`start`、`stop`、`upload`、`download`、`exec`。
- 说法 B / 文档站 <https://docs.harborframework.com/core-concepts/tasks/environment>（未标版本）：方法是 `exec`、`upload_file`、`upload_dir`、`download_file`、`download_dir`、`start`、`stop`。`…/sandboxes/custom-sandboxes` 只写「要实现的接口」，没有方法名单。
- 处理：unknown。A1-02。不选哪一份当接口。

- 对象：`schema_version` 在安装包里的默认
- 说法 A / 本机 harbor 0.23.0 的 `models/task/config.py`：`TaskConfig` 默认 `"1.4"`。旧键 `version` 会改名为 `schema_version`。本安装没有枚举校验，写成 `"1.0"` 不会被任务配置拒绝。`DatasetManifest`、`CompileConfig`、`ExecConfig` 默认 `"1.0"`。`PackageInfo` 在 `[task]`，作者字段是 `authors`。
- 说法 B / 文档站，见上面「task 配置里的版本字段」：教程示例 `version = "1.0"` 与 `[metadata] author_name`，字段参考示例 `schema_version = "1.3"` 与 `[task] authors`。文档站未标版本。
- 处理：unknown。A1-03。不把 `"1.4"`、`"1.3"` 或 `version = "1.0"` 写成唯一格式版本。

- 对象：`trajectory.json` 放在哪
- 说法 A / 本机 harbor 0.23.0 的 `models/task/paths.py`：可选 ATIF 先验，agent 跑之前种入。单步在任务根，多步在 step 目录。
- 说法 B / 文档站把轨迹写在 trial 的 agent log。下载后路径是 `agent/trajectory.json`。不是 task 源目录。文档站未标版本。
- 处理：unknown。A1-05。版本号 `ATIF-v1.7` 与 ATIF v1.8 已记在上面「Agent Trajectory Interchange Format」条，处理仍是 unknown。

- 对象：`BaseInstalledAgent`
- 说法 A / 本机 harbor 0.23.0 的 `agents/installed/base.py`：有 `BaseInstalledAgent`，继承 `BaseAgent`，抽象方法是 `install()`。`setup()` 会调用 `install()`。`BaseAgent` 的方法是 `name()`、`version()`、`setup()`、`run()`。
- 说法 B / 文档站 <https://docs.harborframework.com/core-concepts/agents/custom-agents>（未标版本）：新 agent 优先继承 `BaseInstalledAgent`，实现 `name()`、`install()`、`run()`。回路必须在 environment 外时才用 `BaseAgent`。
- 处理：采安装包。0.23.0 里两个类都在。文档站未标版本，方法名单若和安装包差一个 `version()`，不把文档站改写成安装包签名。

- 对象：`environment/` 能不能省略
- 说法 A / 本机 harbor 0.23.0 的 `models/task/task.py`：`is_valid_dir` 要求 `environment/` 存在。缺了返回假，目录不算 task。`Task()` 不因缺目录抛 `FileNotFoundError`。设了 `docker_image` 之后，定义检查不再要求 Dockerfile，发现任务时目录仍要在。
- 说法 B / 文档站 <https://docs.harborframework.com/core-concepts/tasks/overview> 与 <https://docs.harborframework.com/core-concepts/tasks/environment>（未标版本）：可以只设 `[environment].docker_image`，并省略 `environment/`。
- 处理：unknown。按文档省略目录，对不上这份 0.23.0 的 `is_valid_dir`。按安装包留下目录，对不上文档这句。Singularity 还要 `docker_image`，那是另一条，不取消目录去留的冲突。

- 对象：缺 `gpus` 键时的运行时
- 说法 A / 本机 harbor 0.23.0：缺 `gpus` 时有效 GPU 数是 0。`environment.type` 与 `import_path` 都空时，运行时类型才默认 `docker`。这两件事不是同一条规则。Docker 实现的能力标志不包含 GPU。
- 说法 B / `docs/layer2/terminal-bench-4-0.md`：8 题缺 `gpus`。不能从缺键推出那 8 题不需要显卡。
- 处理：采安装包的两条分开写。不把那 8 题标成不需要显卡。缺键也不写成「会进默认 docker、没有 H100」。
