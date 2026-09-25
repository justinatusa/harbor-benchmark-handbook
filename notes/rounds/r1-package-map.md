# Harbor 0.23.0 package map

## 版本证据

importlib.metadata.version("harbor") == 0.23.0（解释器：/home/ubuntu/.local/share/uv/tools/harbor/bin/python）
distribution location：/home/ubuntu/.local/share/uv/tools/harbor/lib/python3.12/site-packages
METADATA：Name: harbor，Version: 0.23.0

路径均相对于 site-packages/harbor。同名类用源文件区分：task 侧配置在 models/task/config.py，一次运行的覆盖在 models/trial/config.py，job 再包一层 models/job/config.py。

## 名词表

| 英文名 | 定义一句话 | 源文件 | 接入时谁必须提供 |
| --- | --- | --- | --- |
| Task | 一个可运行题目目录的加载结果：读 task.toml，校验 instruction、environment、tests。 | models/task/task.py | 任务作者给出目录 |
| TaskPaths | 约定单题目录：instruction.md、可选 trajectory.json、task.toml、environment/、solution/、tests/，多步再加 steps/<name>/。 | models/task/paths.py | 任务作者按这些文件名放文件 |
| TaskConfig | task.toml 的根模型，schema_version 默认字符串 "1.4"，旧键 version 会改名为 schema_version；本安装没有枚举校验。 | models/task/config.py | 任务作者写 toml；缺省段由模型补默认值 |
| schema_version | TaskConfig 默认 "1.4"；DatasetManifest、CompileConfig、ExecConfig 默认 "1.0"。 | models/task/config.py | 可省略 |
| PackageInfo | 可选 [task] 段：出现时 name 必填且为 org/name，version、description、authors、keywords 可选。 | models/task/config.py | 要进 registry 的任务作者 |
| instruction.md | 单步任务给 agent 的指令；is_valid_dir 要求存在；多步任务改放在每个 step 目录里，根指令可为空。 | models/task/paths.py | 任务作者 |
| trajectory.json | 可选 ATIF 先验轨迹，agent 跑之前种入；单步在任务根，多步在 step 目录。 | models/task/paths.py | 可选，任务作者 |
| environment/ | 题目环境目录，is_valid_dir 要求该目录存在；里面放镜像定义，不在这里选择 docker 还是 singularity。 | models/task/paths.py | 任务作者 |
| EnvironmentConfig | task 侧 [environment]：资源与镜像，不是 provider 类型。 | models/task/config.py | 任务作者；全部有默认或可选 |
| docker_image | 预构建镜像名；设置后 Dockerfile 对支持的环境类型可选；Singularity 则强制要这个字段。 | models/task/config.py | 无 Dockerfile 时任务作者必填 |
| Dockerfile | 环境定义文件之一；与 docker-compose.yaml、docker_image 三选一即可通过 require_agent_environment_definition。 | environments/definition.py | 任务作者三选一 |
| docker-compose.yaml | 官方认的 compose 文件名常量 COMPOSE_FILE_NAME。 | environments/definition.py | 任务作者三选一 |
| TaskOS | [environment].os，linux（默认）或 windows。 | models/task/config.py | 可省略，默认 linux |
| NetworkMode | 网络策略：no-network、public（环境默认）、allowlist；配套 allowed_hosts。 | models/task/config.py | 可省略 |
| HealthcheckConfig | 可选健康检查；出现时 command 必填。 | models/task/config.py | 可选 |
| MCPServerConfig | 可选 MCP server；name 必填，transport 默认 sse。 | models/task/config.py | 可选 |
| solution/ | Oracle 解法目录，OracleAgent 拷到容器 /solution；solve.sh 优先于 solve.bat。 | models/task/paths.py | 可选；要用 oracle 则任务作者提供 |
| tests/ | 评分脚本目录，Verifier 在 agent 之后拷到容器 /tests；共享 verifier 时必须有对应 OS 的 test.sh 或 test.bat。 | models/task/paths.py | 共享评分时任务作者必提供 |
| VerifierConfig | task 侧 [verifier]：timeout_sec 默认 600，env、user 可选，environment_mode 与 environment 决定评分容器。 | models/task/config.py | 可省略，用默认 Verifier |
| VerifierEnvironmentMode | shared：评分跑在 agent 同一环境；separate：独立容器；省略时有 [verifier.environment] 则 separate，否则 shared。 | models/task/config.py | 可省略 |
| StepConfig | [[steps]] 一步：name 必填且可做目录名，可覆盖 agent、verifier、min_reward、artifacts。 | models/task/config.py | 多步任务作者 |
| MultiStepRewardStrategy | 多步汇总：mean（默认）或 final。 | models/task/config.py | 多步可省略 |
| ArtifactConfig | 要从容器收回的路径；source 必填。 | models/task/config.py | 可选 |
| Dataset | 一组要一起跑的 task；本地目录、package、registry 或 git repo 四种来源。 | models/job/config.py | 数据集作者或运行方 |
| dataset.toml | package 数据集清单文件名，类名 DatasetManifest。 | models/dataset/paths.py | package 数据集作者 |
| DatasetManifest | schema_version、必填 [dataset]、可选 [[tasks]] 与 [[files]]。 | models/dataset/manifest.py | package 数据集作者 |
| DatasetInfo | [dataset]：name 必填 org/name，version、description、authors、keywords 可选。 | models/dataset/manifest.py | package 数据集作者 |
| DatasetTaskRef | [[tasks]] 一项：name 与 digest（sha256:64hex）都必填，用来钉内容哈希。 | models/dataset/manifest.py | package 数据集作者 |
| DatasetFileRef | [[files]] 一项：path 必须是无目录分隔符的文件名，digest 发布时可后补。 | models/dataset/manifest.py | 可选 |
| DatasetPaths | 数据集目录约定：dataset.toml，可选 metric.py 与 README.md。 | models/dataset/paths.py | package 数据集作者 |
| DatasetConfig | job 里怎么选数据集：path、name、version 或 ref、registry_url、registry_path、repo，以及 task_names、exclude_task_names、n_tasks。 | models/job/config.py | 运行方；path 与 name 互斥 |
| Registry | registry.json 的模型：datasets 是 DatasetSpec 列表，来自 URL 或本地 path。 | models/registry.py | registry 维护者 |
| registry.json | git registry 文件名；默认远程 URL 在 RemoteRegistryInfo。 | registry/client/git_repo.py | registry 维护者 |
| DatasetSpec | registry 里的一个数据集：name、version、description、tasks，可选 metrics。 | models/registry.py | registry 维护者 |
| DatasetMetadata | 解析后的数据集：task_ids、metrics、files。 | models/registry.py | Harbor 解析，作者提供清单 |
| LocalTaskId | 本地任务 id，只有 path。 | models/task/id.py | 运行方给 path |
| GitTaskId | git 任务 id：git_url 必填，git_commit_id 可选，path 为仓内相对路径。 | models/task/id.py | registry 或运行方 |
| PackageTaskId | 包任务 id：org、name，ref 可为 tag、revision 或 sha256 digest。 | models/task/id.py | 运行方给 org/name |
| Trial | 一次具体运行的生命周期基类：环境、agent、verifier、hooks、result；用 Trial.create 构造。 | trial/trial.py | Harbor 从 Job 展开；单题调试由运行方给 TrialConfig |
| TrialConfig | 一次 trial 的输入：必填 task（path 或 name 二选一），以及 agent、environment、verifier 覆盖。 | models/trial/config.py | Job 生成，或运行方手写 |
| SingleStepTrial | 没有 [[steps]] 的 trial：一次 instruction、一次 agent run、一次可选 verifier。 | trial/single_step.py | Harbor 按任务形状选择 |
| MultiStepTrial | task.has_steps 时使用的 trial。 | trial/multi_step.py | Harbor 按任务形状选择 |
| Job | 一组 trial 的唯一启动入口：把 datasets 与 tasks、agents、n_attempts 展开成 TrialConfig，并汇总 metric。 | job.py | 运行方提供 JobConfig |
| JobConfig | job 配置：agents 默认一个 oracle，datasets 与 tasks 可空，n_attempts 默认 1，n_concurrent_trials 默认 4，metrics 默认为空列表。 | models/job/config.py | 运行方 |
| JobResult | 一次 job 的结果：id、stats、trial_results。 | models/job/result.py | Harbor 写出 |
| TrialResult | 一次 trial 的结果：agent_info、agent_result、verifier_result、step_results。 | models/trial/result.py | Harbor 写出 |
| EnvironmentType | 运行时 sandbox 枚举，不是 task.toml 字段。 | models/environment_type.py | 运行方可选；缺省 docker |
| BaseEnvironment | 自定义 sandbox 要实现的抽象：type、start、stop、upload、download、exec。 | environments/base.py | 自定义环境的作者 |
| EnvironmentFactory | 按 EnvironmentType 懒加载内置类，或按 import_path 加载第三方类。 | environments/factory.py | Harbor；自定义时运行方给 import_path |
| DockerEnvironment | EnvironmentType.DOCKER 的实现，registry 项无额外 pip extra。 | environments/docker/docker.py | Harbor 内置 |
| SingularityEnvironment | EnvironmentType.SINGULARITY；把 Docker 镜像转成 .sif，要求 task 的 docker_image。 | environments/singularity/singularity.py | Harbor 内置；运行方选中该 type |
| Verifier | 默认评分器：上传 tests，执行 test.sh 或 test.bat，再读 reward 文件。 | verifier/verifier.py | Harbor 内置 |
| BaseVerifier | 自定义评分器抽象，必须实现 verify() 并返回 VerifierResult。 | verifier/base.py | 自定义评分器作者 |
| VerifierFactory | import_path 存在时加载 BaseVerifier 子类，否则构造 Verifier。 | verifier/factory.py | 运行方可选 import_path |
| VerifierResult | 评分结果，只有 rewards：字符串键到有限 int 或 float。 | models/verifier/result.py | 评分脚本或自定义 verifier |
| reward.txt | 单标量奖励文件，解析成 {"reward": float}；容器路径 /logs/verifier/reward.txt。 | models/trial/paths.py | 评分脚本必须写 reward.txt 或 reward.json |
| reward.json | 多键奖励文件，JSON 对象的值必须是有限数；优先于 reward.txt。 | models/trial/paths.py | 与 reward.txt 二选一，评分脚本提供 |
| BaseAgent | 被测对象抽象：name、version、setup、run；可选 resume、load、handoff。 | agents/base.py | agent 作者 |
| AgentFactory | 内置名字表加 import_path；--agent 里的 module.path:ClassName 当作 import_path。 | agents/factory.py | Harbor；自定义 agent 作者给类路径 |
| AgentName | 内置 agent 名字枚举，含 oracle、nop、terminus-2、claude-code 等。 | models/agent/name.py | 运行方选一个，或改用 import_path |
| AgentConfig | trial 侧 agent：name 与 import_path 都空则默认 oracle；另有 model_name、kwargs、env、mcp_servers。 | models/trial/config.py | 运行方 |
| AgentCapabilities | agent 声明的能力：atif、resume、轨迹加载、handoff、windows、bridges。 | agents/capabilities.py | agent 作者声明 |
| ACPAgentMixin | agents/protocols 里唯一协议：acp_command，供 ACP bridge 把目标 agent 当 ACP server 拉起。 | agents/protocols/acp.py | 要接 ACP bridge 的 agent 作者 |
| BridgeConfig | 模拟用户通道，目前 kind 只有 acp。 | models/bridge.py | 可选，运行方 |
| Adapter | CLI 子命令 harbor adapter 的生成期脚手架，不是运行时插件；init 复制 template-adapter，review 做结构检查。 | cli/adapters.py | adapter 作者在生成任务时提供，运行 job 不加载它 |
| TemplateAdapter | 模板类，约定 run() 把上游题写成 Harbor task 目录；wizard 会按 adapter id 改类名。 | cli/template-adapter/adapter.py.tmpl | adapter 作者实现 |
| BaseMetric | 对一列 reward dict 做汇总的抽象，compute(rewards) 返回 dict。 | metrics/base.py | 自定义 metric 仅能通过已注册 MetricType 或 uv-script |
| MetricType | 只有 sum、min、max、mean、uv-script。 | models/metric/type.py | 运行方或 registry 的 metrics 列表 |
| MetricConfig | type 默认 mean，kwargs 传给构造器；uv-script 要 kwargs script_path。 | models/metric/config.py | 可选 |
| Mean | 指标列表为空时 Job 自动补上的默认汇总。 | metrics/mean.py | Harbor 内置 |
| UvScript | 用 uv run 执行外部脚本：输入 rewards.jsonl，输出 metric.json。 | metrics/uv_script.py | 数据集作者提供 metric.py |
| metric.py | 数据集目录里的自定义汇总脚本；package 数据集下载后会自动包成 UvScript。 | models/dataset/paths.py | 可选，数据集作者 |
| JobPlugin | 协议：on_job_start(job) 与 on_job_end(job_result)。 | models/job/plugin.py | 可选，插件作者 |
| BaseJobPlugin | JobPlugin 的抽象基类；HarborHubUploadPlugin 是进程内例子，不走 entry point。 | models/job/plugin.py | 插件作者可继承 |
| Compiler | 把 CompileConfig 交叉乘积写成具体 task 目录。 | compile/compiler.py | 要用 harbor compile 流程的作者 |
| CompileConfig | 轻量输入：instructions、environments、verifiers 的变体列表，output_dir 在 compile() 时必填。 | models/compile/config.py | compile 调用方 |
| Executor | harbor exec：先 compile map 任务并跑 Job，可选再 compile 一个 reduce 任务。 | exec/executor.py | exec 调用方 |
| ExecConfig | map 必填，reduce 可选；reduce 要求 map.compile.artifacts。 | models/exec/config.py | exec 调用方 |
| TrialEvent | trial 生命周期钩子名：start、environment-start、agent-start、agent-end、verification-start、end、cancel。 | trial/hooks.py | 代码调用方可选注册 |
| BaseLLM | agent 用的 LLM 客户端抽象，call(prompt)；不是 verifier 的 judge 接口。 | llms/base.py | agent 作者可选使用 |
| OracleAgent | 内置对照 agent，跑 solution/solve 脚本。 | agents/factory.py | Harbor 内置 |
| NopAgent | 内置空 agent。 | agents/factory.py | Harbor 内置 |
| compute_pass_at_k_by_evals | 按 evals 分组算 pass@k 的函数，不在 MetricType 里。 | utils/pass_at_k.py | Harbor 内置，调用方可选 |

## 扩展点清单

Task 目录。不注册。Task.is_valid_dir 要求 task.toml 与 environment/。单步还要 instruction.md。共享 verifier 还要与 [environment].os 匹配的 test.sh 或 test.bat。缺文件则目录不算 task，显式加载抛 FileNotFoundError。separate verifier 跳过宿主机 test 脚本检查。运行期环境定义仍要 docker_image、Dockerfile 或 docker-compose.yaml 之一，否则 FileNotFoundError（environments/definition.py）。

Agent。两种插法：AgentName 命中 AgentFactory._AGENT_MAP，或 import_path 形式 module.path:ClassName（--agent 里含冒号且不是 ACP registry 简写时也走 import_path）。没有 setuptools entry point。name 与 import_path 都空则变成 oracle。未知名字 ValueError。import_path 不检查是否继承 BaseAgent。类必须实现 name、version、setup、run。

Environment。选择键在 trial 或 job 的 environment.type，不在 task.toml。两者都空时 set_default_type 设为 docker。import_path 优先于 type（environments/factory.py create_environment_from_config）。CLI 是 -e/--env，可写枚举值或 module.path:ClassName。枚举：docker、podman、daytona、e2b、modal、runloop、langsmith、ec2、gke、ack、openshift、novita、apple-container、singularity、islo、tensorlake、cwsandbox、wandb、use-computer、cua-cloud、blaxel、opensandbox、beam、skypilot、hf-sandbox、hyperbrowser、vercel、runta、kata。未注册 type 抛 ValueError。云类型缺依赖时 ImportError，并提示 pip extra。Singularity 额外 kwargs：singularity_image_cache_dir、singularity_force_pull、singularity_no_mount；且 task 必须有 docker_image。task 侧配置键是 docker_image、os、cpus、memory_mb、storage_mb、gpus、gpu_types、tpu、mcp_servers、env、skills_dir、healthcheck、workdir、network_mode、allowed_hosts、build_timeout_sec。

Verifier。默认不注册类：Verifier 跑 tests 脚本。确定性评分就是脚本把结果写成 reward.json（优先）或 reward.txt。reward.txt 非有限数或空文件会 VerifierOutputParseError 或 RewardFileEmptyError；两个文件都没有则 RewardFileNotFoundError。自定义评分：trial 或 job 的 verifier.import_path，必须是 BaseVerifier 子类；kwargs 没有 import_path 会 ValueError。没有名为 LLM judge 的类或方法。adapter 检查清单把 LLM judge 写成 tests/ 里的 prompt、model、rubric，由 test 脚本自己调模型再写 reward 文件（cli/adapter_review.py）。verifier.env 里出现 api_key 时只打日志，提醒可能是 LLM-based verifier（verifier/verifier.py）。analyze/ 用 rubric 生成 analysis.json，不写 VerifierResult。

Agent protocol。agents/protocols 只导出 ACPAgentMixin。注册方式是 agent 类继承该 mixin 并实现 acp_command；BridgeKind 只有 acp。缺了 mixin 只是不能当 ACP bridge 的目标 agent，普通 setup 加 run 仍然可跑。

Adapter。不是运行时扩展点。入口：cli/main.py 的 harbor adapter，命令 init 与 review（cli/adapters.py）。init 调用 AdapterWizard，从 cli/template-adapter 复制 README、adapter_metadata.json、parity_experiment.json、adapter.py.tmpl、main.py.tmpl、task-template。运行 job 不 import 这个类。缺 adapter 目录时 review 以 SystemExit 结束。结构校验还会找仓库里的 scripts/validate_adapter.py，本安装的 site-packages 里没有该脚本，找不到只警告。

Metric。MetricFactory 只认 MetricType 五个值，不能靠 entry point 加新类。job.metrics、registry DatasetSpec.metrics、package 的 metric.py 会挂上；列表仍空则补 Mean。未知 type 抛 ValueError。UvScript 脚本不存在则 FileNotFoundError。本地数据集目录里的 metric.py 不会在 Job._resolve_dataset_metrics 的 is_local 分支自动加载。

Plugins。entry point group 名 harbor.plugins（cli/plugin_registry.py）。--plugin 可写已注册名字，或直接写 module:Class。类要满足 JobPlugin（有 on_job_start 与 on_job_end）。未知名字 ValueError，并列出已安装插件。不传 --plugin 时 job 照常跑。job 配置文件里的 plugins 键已废弃且被忽略。on_job_end 抛错只记日志。本包 entry_points.txt 只有 console_scripts harbor、hb、hr，没有 harbor.plugins。

Compile。Compiler.compile 写 task 目录，不是插件注册表。output_dir 为空则 ValueError。指令、环境、verifier 列表为空时各用一个默认槽。CompileVerifier 必须在 path 与 auto_verifier 里恰好给一个。

Exec。Executor 串起 compile、Job、可选 reduce。没有 reduce 就只跑 map。reduce 但 map.compile.artifacts 为空则 ValueError。它复用 Job 与 Compiler，不新增 agent 或 verifier 注册通道。

Trial hooks。Trial 上按 TrialEvent 登记回调，没有 entry point。不登记则只是没有旁路通知，trial 仍跑完。

## 不确定的点

- singularity-compose.yaml 只出现在 models/task/paths.py 与 models/task/task.py 的目录注释里。SingularityEnvironment._validate_definition 只要求 docker_image。本安装没有读取该文件名的代码。它是否仍被某种环境当定义文件：unknown。
- cli/template-task/tests/test.sh 注释写 /logs/verifier/rewards.json。解析器只认 reward.json，然后 reward.txt（verifier/verifier.py）。rewards.json 是否另有读者：unknown。
- task schema_version 是自由字符串。template-task 写 1.4，template-adapter 的 task.toml 写 1.0。除改名 version 以外，本安装没有拒绝其他值的校验。1.0 模板在 0.23.0 运行时是否被别处拒绝：unknown。
- 是否存在未随这个 wheel 安装的 LLM judge 基类：unknown。此 site-packages 的 Python 源码里没有 LLMJudge 或等价 verifier 接口。
- 本地 dataset 目录的 metric.py 除 Job 与 job_plan 的 package 下载路径外，是否还有 CLI 会隐式挂上：在已读的 .py 里没有。若动态入口在本树之外：unknown。
- Agent 与 Environment 的 import_path 不检查基类；错误类会在调用时失败，失败形态依赖该类缺什么方法：unknown，直到实际构造。
- docker-compose.yml 不是 environments/definition.py 的 COMPOSE_FILE_NAME。OpenSandbox 见到 yml 会拒绝。DockerEnvironment 是否另认 yml：本检索未看到，unknown。

PACKAGE-MAP-END
