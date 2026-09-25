# A1 回应

只根据 `r1-package-map.md` 与 `r1-docs-nouns.md`。不改这两份笔记。

记入 conflicts 的五条追加在 `docs/conflicts.md`。A1-10、A1-12、A1-14 的处理写在 `docs/abstraction.md` 的「A1 之后仍未定的点」。

## A1-01

处理：不接受

扩展点「Task 目录」写的是：`Task.is_valid_dir` 要求 `task.toml` 与 `environment/`。扩展点「Environment」写的是：选择键在 trial 或 job 的 `environment.type`，不在 `task.toml`。名词表已分行。`environment/` 是题目环境目录。`EnvironmentConfig` 是 task 侧 `[environment]`，资源与镜像，不是 provider 类型。`EnvironmentType` 是运行时 sandbox 枚举，不是 task.toml 字段。文档名词另有 Sandbox、Environment（运行时类型）、`BaseEnvironment`，并写同一页承认这个名字不好。这是文档用词有三处，包地图没有把目录和运行时收成同一个定义。

## A1-02

处理：记入 conflicts

说法一：自定义 sandbox 要实现 `type`、`start`、`stop`、`upload`、`download`、`exec`。
来源：`r1-package-map.md` 名词表 `BaseEnvironment`。源文件 `environments/base.py`。

说法二：一个 `BaseEnvironment` 实现，方法是 `exec`、`upload_file`、`upload_dir`、`download_file`、`download_dir`、`start`、`stop`。
来源：`r1-docs-nouns.md`。出处 `https://docs.harborframework.com/core-concepts/tasks/environment`。

同文件另一条把 `BaseEnvironment` 写成「自定义 sandbox 要实现的接口」，出处 `…/sandboxes/custom-sandboxes`，那里没有方法名单。包地图不确定点写：`import_path` 不检查基类，缺方法时的失败形态是 unknown。两份方法名单对不上。本回应不选哪一份当接口。

## A1-03

处理：记入 conflicts

说法一：`TaskConfig` 的 `schema_version` 默认字符串 `"1.4"`。旧键 `version` 会改名为 `schema_version`。本安装没有枚举校验。`DatasetManifest`、`CompileConfig`、`ExecConfig` 默认 `"1.0"`。`PackageInfo` 是可选 `[task]` 段，字段有 `authors`，没有 `author_name`。`template-task` 写 1.4，`template-adapter` 的 `task.toml` 写 1.0。1.0 会不会在别处被拒绝：unknown。
来源：`r1-package-map.md` 名词表 `schema_version`、`TaskConfig`、`PackageInfo`，以及不确定点。安装版本是 harbor 0.23.0。

说法二：字段参考页示例是 `schema_version` `"1.3"`。创建教程示例写 `version = "1.0"` 和 `[metadata] author_name`。configuration 参考写 `schema_version = "1.3"` 和 `[task] authors`。文档站未标版本，不能当成 0.23.0 定论。
来源：`r1-docs-nouns.md` 开头，以及官方用词 `schema_version`、文末 `version` 与 `schema_version` 条。

任务默认、数据集默认、文档示例 `"1.3"`、教程 `version = "1.0"`、`author_name` 与 `authors`，这几处同时在。本回应不把其中任何一处写成 0.23.0 的唯一格式版本。

## A1-04

处理：接受

新句子：「`llms.txt` 没有 adapter 专页，也没有 benchmark 专页。metric 的已读页面是 `https://docs.harborframework.com/core-concepts/datasets/metrics`。`https://www.harborframework.com/docs/datasets/adapters` 是 HTTP 308，落到文档根。`https://docs.harborframework.com/datasets/adapters` 与 `…/datasets/adapters.md` 是 HTTP 404。文档站没有 adapter 页。」

将改 `r1-docs-nouns.md` 这句：「`llms.txt` 全文索引里没有 adapter、benchmark、metric 以外的同名专页。benchmark 没有专页。」

这句按字面会读成 adapter 与 benchmark 在索引里有专页。下一句又写 benchmark 没有专页。同文件已经写出三个 URL 的 308 或 404，以及「也没有 adapter 页」。模板 README 仍指向这些 URL。页是死的。文档站未标版本，这句不补版本号。

## A1-05

处理：记入 conflicts

存放位置，说法一：`trajectory.json` 是可选 ATIF 先验轨迹，agent 跑之前种入。单步在任务根，多步在 step 目录。接入列是「可选，任务作者」。没有版本号。
来源：`r1-package-map.md` 名词表 `trajectory.json`、`TaskPaths`。源文件 `models/task/paths.py`。

存放位置，说法二：写在 trial 的 agent log。下载后路径是 `agent/trajectory.json`。不是 task 源目录。
来源：`r1-docs-nouns.md`「trajectory、ATIF、`trajectory.json`」条。

版本号，说法一：ATIF 页写当前格式 `ATIF-v1.7`。
说法二：changelog 写 ATIF v1.8。
来源：同一条，`r1-docs-nouns.md`。包地图 `AgentCapabilities` 只列能力名 `atif`，没有写校验哪一版。

任务根里的先验文件，和 trial 日志 `agent/trajectory.json`，两处都记着。v1.7 与 v1.8 也并着。本回应不删任何一处，也不指定 agent 校验哪一版。

## A1-06

处理：接受

新句子：「`DockerEnvironment` 是 `EnvironmentType.DOCKER` 的内置实现，没有额外 pip extra。名词表里的 `Registry` 与 `registry.json` 是数据集登记。pyproject 的 optional extra 名叫 `adapter`，依赖 `claude-agent-sdk`。这个 extra 不装 `cli/adapters.py` 的 Adapter 脚手架。云类型缺依赖时 `ImportError`，并提示 pip extra。笔记没有写出那些 extra 的名字。」

将改名词表 `DockerEnvironment` 这句：「`EnvironmentType.DOCKER` 的实现，registry 项无额外 pip extra。」

将在名词表 `Adapter` 定义后加上 extra 这一句。现在 83 行和扩展点清单都没有这个 extra。文档名词写明它「同名但不是上面那个 Adapter」，出处是 tag `v0.23.0` 的 `pyproject.toml`。

## A1-07

处理：不接受

扩展点已经写：「Adapter。不是运行时扩展点。」入口是 `harbor adapter` 的 `init` 与 `review`。又写：「运行 job 不 import 这个类。」`scripts/validate_adapter.py` 在本安装的 site-packages 里没有，「找不到只警告」也写了。`parity_experiment.json` 是 init 复制的文件。文档名词写：上传到 `harbor-datasets` 并改那份 `registry.json`，是 GitHub 模板说明，不是当前文档站步骤。邻近做法是 `harbor run -p`、`dataset.toml`、`harbor publish`。地图没有把 Adapter 写成 job 会加载的类。

## A1-08

处理：接受

新句子：「`--agent` 里含冒号时，`acp:<agent_id>` 与 `acp:<agent_id>@<version>` 是 ACP Registry 简写，不走 `import_path`。文档写这条从 ACP Registry 安装，并在 task environment 里运行。`ACPAgentMixin` 实现 `acp_command`，供 ACP bridge 把目标 agent 当 ACP server 拉起。`BridgeKind` 只有 `acp`。缺 mixin 时不能当这个 bridge 的目标 agent。」

将改扩展点 Agent 这句：「`--agent` 里含冒号且不是 ACP registry 简写时也走 import_path。」

包地图只把简写从 `import_path` 里划了出去，没有写它装在哪里。文档名词写了简写，没有写 `ACPAgentMixin`。两句都保留，分成两扇门。

## A1-09

处理：记入 conflicts

说法一：名词表只有 `BaseAgent`，方法是 `name`、`version`、`setup`、`run`，可选 `resume`、`load`、`handoff`。扩展点 Agent 写类必须实现 `name`、`version`、`setup`、`run`。83 行没有 `BaseInstalledAgent`，也没有 `install`。
来源：`r1-package-map.md`。这是本机 harbor 0.23.0 的 site-packages。

说法二：新 agent 优先继承 `BaseInstalledAgent`，实现 `name()`、`install()`、`run()`。agent loop 必须在 environment 外时才继承 `BaseAgent`，实现 `name()`、`version()`、`setup()`、`run()`。
来源：`r1-docs-nouns.md`。出处 `https://docs.harborframework.com/core-concepts/agents/custom-agents`。文档站未标版本，不能当成 0.23.0 定论。

0.23.0 名词表里的基类，和文档写的优先基类，对不上。本回应不把 `BaseInstalledAgent` 补进 0.23.0 的 83 行，也不把文档的 `install()` 删掉。

## A1-10

处理：接受

新句子：「LLM judge 不在 `VerifierResult` 里。`VerifierResult` 只有 rewards：字符串键到有限 int 或 float。评分文件是 `/logs/verifier/reward.json`，其次 `/logs/verifier/reward.txt`。模型调用写在 tests 脚本里。adapter 检查清单把 prompt、model、rubric 放在 `tests/`，由 test 脚本自己调模型，再写 reward 文件。文档侧由 `test.sh` 调用 `rewardkit /tests`，包名 `harbor-rewardkit`。`analyze/` 的 rubric 写出 `analysis.json`，不写 `VerifierResult`。`verifier.env` 里出现 `api_key` 时只打日志。`VerifierConfig` 可省略，省略后仍用这套 reward 文件，不是省掉评分文件。」

将改扩展点 Verifier 这句：「没有名为 LLM judge 的类或方法。adapter 检查清单把 LLM judge 写成 tests/ 里的 prompt、model、rubric，由 test 脚本自己调模型再写 reward 文件（cli/adapter_review.py）。」

将改不确定点这句：「是否存在未随这个 wheel 安装的 LLM judge 基类：unknown。此 site-packages 的 Python 源码里没有 LLMJudge 或等价 verifier 接口。」

wheel 外有没有另一套基类，不改变上面的评分约定。本安装的评分读 reward 文件。模型调用在 tests 脚本里。

## A1-11

处理：接受

新句子：「只调 API 的 agent 仍要起 sandbox。`BaseLLM.call` 与 `AgentConfig.model_name` 不代替环境。名词表没有 Model 行。文档里 Model 是 `harbor run -m` 的参数，task 目录无此文件。`environment.type` 为空时默认 docker。枚举里没有空实现。`Task.is_valid_dir` 要求 `environment/`。运行期还要 `docker_image`、`Dockerfile` 或 `docker-compose.yaml` 之一，否则 `FileNotFoundError`。`NopAgent` 也走 trial 的环境。separate 跳过宿主机 test 脚本检查。文档写专用镜像要自己带 `/tests/test.sh`。」

将改扩展点 Environment 这句：「两者都空时 set_default_type 设为 docker。」

## A1-12

处理：记入 conflicts

说法一：`environment/` 必须有。`is_valid_dir` 要求该目录存在。缺了则目录不算 task，显式加载抛 `FileNotFoundError`。`docker_image` 设置后，Dockerfile 对支持的环境类型可以不写。目录这一条仍在。Singularity 另外强制要 `docker_image`。
来源：`r1-package-map.md` 名词表 `environment/`、`docker_image`，扩展点「Task 目录」。源文件 `models/task/paths.py`、`environments/definition.py`。安装是 harbor 0.23.0。

说法二：可以只设 `[environment].docker_image`，并省略 `environment/`。
来源：`r1-docs-nouns.md`「task 目录里的 environment」。出处 `https://docs.harborframework.com/core-concepts/tasks/overview` 与 `https://docs.harborframework.com/core-concepts/tasks/environment`。文档站未标版本。

按文档省略目录，对不上包地图的 `is_valid_dir`。按包地图保留 `environment/`，对不上文档这句「可省略」。本回应两句都留下。Singularity 要 `docker_image` 是 `docker_image` 行里的另一条，不用来取消目录去留的冲突。

## A1-13

处理：接受

新句子：「task 侧配置键是 `docker_image`、`os`、`cpus`、`memory_mb`、`storage_mb`、`gpus`、`gpu_types`、`tpu`、`mcp_servers`、`env`、`skills_dir`、`healthcheck`、`workdir`、`network_mode`、`allowed_hosts`、`build_timeout_sec`。`cpus`、`memory_mb`、`storage_mb`、`gpus`、`gpu_types`、`tpu` 没有单独名词行。`EnvironmentConfig` 的接入列写这些键全部有默认或可选。笔记没有写哪个 `EnvironmentType` 会把 `gpus` 或 `tpu` 传进容器。」

将改扩展点 Environment 这句：「task 侧配置键是 docker_image、os、cpus、memory_mb、storage_mb、gpus、gpu_types、tpu、mcp_servers、env、skills_dir、healthcheck、workdir、network_mode、allowed_hosts、build_timeout_sec。」

键列表还在。不补 30 个 type 与 GPU 的对应，笔记里没有。文档名词读过 `…/tasks/resources`，官方用词节没有抄这些字段。用词节的空白不改写成该页没有这些词。

## A1-14

处理：接受

新句子：「可省略。省略后的默认是 public，环境能出网。另两个值是 `no-network` 与 `allowlist`。`allowlist` 配套 `allowed_hosts`。笔记没有写 `allowed_hosts` 为空时拒绝还是放行。」

将改名词表 `NetworkMode` 的接入列：「可省略」。

定义句里已有「public（环境默认）」。接入列要写上这个默认。文档名词读过 environment 页，官方用词节没有 `NetworkMode`、`allowed_hosts`、`no-network`。用词节没写，不推翻包地图这一行的默认 public。空名单的运行规则笔记里没有，这里不补。

## A1-15

处理：接受

新句子：「官方认的 compose 文件名是 `docker-compose.yaml`，常量 `COMPOSE_FILE_NAME`。它与 `Dockerfile`、`docker_image` 三选一，用来通过 `require_agent_environment_definition`。笔记没有写 agent 进入哪个 service，没有写 verifier 是否同一 service，也没有写 `gpus` 挂在哪个 service。`docker-compose.yml` 不是这个常量。OpenSandbox 见到 yml 会拒绝。DockerEnvironment 是否另认 yml：笔记标 unknown。`singularity-compose.yaml` 只出现在目录注释里。本安装没有读取它的代码。Singularity 校验只要求 `docker_image`。不用 Compose 时，文档写 Harbor 没有原生多容器实现，用户可以自己实现 custom environment。」

将改名词表 `docker-compose.yaml` 这句：「官方认的 compose 文件名常量 COMPOSE_FILE_NAME。」

改名放进 `environment/` 只满足文件名这一条。service 怎么进，笔记里没有，不写成规则。

## A1-16

处理：接受

新句子：「接入列只写可省略时，改成省略后的具体默认。`schema_version`：任务省略后 `TaskConfig` 用 `"1.4"`，`DatasetManifest`、`CompileConfig`、`ExecConfig` 用 `"1.0"`。这是包的默认。文档示例见 A1-03，两说都留着。`VerifierEnvironmentMode`：省略时若有 `[verifier.environment]` 则为 separate，否则为 shared。`MultiStepRewardStrategy`：多步省略后默认 mean。`VerifierConfig`：省略后 `timeout_sec` 为 600，用内置 Verifier 读 `reward.json` 或 `reward.txt`。`NetworkMode` 按 A1-14。`TaskOS` 已写默认 linux，保持。`JobResult`、`TrialResult` 由 Harbor 写出。`SingleStepTrial`、`MultiStepTrial` 由 Harbor 按有没有 `[[steps]]` 选择。三个 Factory 由 Harbor 构造，自定义时运行方给 `import_path`。这些不是上游题要交的文件。`compute_pass_at_k_by_evals` 是 `utils/pass_at_k.py` 里的函数，不能写入 `MetricConfig.type`。`MetricType` 只有 sum、min、max、mean、uv-script。未知 type 抛 `ValueError`。不传 `--plugin` 时 job 照常跑。不登记 `TrialEvent` 时 trial 仍跑完。缺 `ACPAgentMixin` 时普通 setup 加 run 仍可跑。缺 `environment/` 时目录不算 task。两个 reward 文件都没有则 `RewardFileNotFoundError`。ASP 在文档里是 RFC draft。`.asp.json` 由 orchestrator 在 agent 启动前准备。文档写它不是 task format 列出的文件。不把它收进 Environment 扩展点。」

将改这些接入列：

- `schema_version` 的「可省略」
- `VerifierEnvironmentMode` 的「可省略」
- `MultiStepRewardStrategy` 的「多步可省略」
- `VerifierConfig` 的「可省略，用默认 Verifier」
- `compute_pass_at_k_by_evals` 的「Harbor 内置，调用方可选」

将在名词表标题下、表前加「Harbor 写出 / 按任务形状选择 / 内置」那一句。将在扩展点 Environment 的配置键那句后加 ASP 那一句。`BaseInstalledAgent` 仍按 A1-09 两说并记。`gpus` 按 A1-13，不在接入列另写默认值。

## A1-17

处理：接受

新句子：「评分文件只认 `/logs/verifier/reward.json`，其次 `/logs/verifier/reward.txt`。两者都在时优先 `reward.json`。两个都没有则 `RewardFileNotFoundError`。`cli/template-task/tests/test.sh` 的注释写 `/logs/verifier/rewards.json`。`verifier/verifier.py` 不按这个复数名字读。模板注释不进入评分文件名。」

将改不确定点这句：「cli/template-task/tests/test.sh 注释写 /logs/verifier/rewards.json。解析器只认 reward.json，然后 reward.txt（verifier/verifier.py）。rewards.json 是否另有读者：unknown。」

注释里的复数名字留在这句话里，说明它是注释。评分约定仍是 `reward.json` 与 `reward.txt`。

A1-RESPONSE-END
