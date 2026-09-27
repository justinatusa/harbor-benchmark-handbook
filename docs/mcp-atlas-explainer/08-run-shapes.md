# 公开说明里的几种跑法

README 的默认跑法是一台机器上的一条栈：一个沙箱容器，一个宿主机上的循环，一个 Python 批量脚本。扩容是多开这样的栈，不是把题面改成直接请求上游网站。

## 拉现成镜像，跑公开的 500 道

准备顺序和 README 一致。

先复制 `env.template` 为 `.env`，填被测模型的 `LLM_API_KEY` 和 `LLM_BASE_URL`。业务程序的密钥按 [06-network-and-keys.md](06-network-and-keys.md) 需要再填。

然后拉取 `ghcr.io/scaleapi/mcp-atlas:1.2.7`，打上本地标签 `agent-environment:latest`，执行 `make run-docker`。容器把 1984 映出来。README 写启动要 1 分钟以上；环境目录的说明写大约 1 到 3 分钟，视启用了多少程序而定。Docker 内存至少留 8 GB，建议 10 GB 以上。

另开一个终端，在仓库根目录执行 `make install-harness`，再 `make run-harness`。循环听 3001。

再开一个终端，`make install-python`，然后 `python run_eval.py --model "openai/gpt-4o" --output outputs.csv`。不传 `--input` 时，脚本加载 Hugging Face 上的 `ScaleAI/MCP-Atlas` 训练集，也就是公开的 500 行。不公开的一半不在这条默认路径上。

脚本把每题 POST 到循环的 `/v2/mcp_eval/run_agent`。输出 CSV 有三列：`task_id`、`raw_conversation_history`、`response`。已经写过的题号，下次再跑会跳过。同一题的工具调用打到当时 `MCP_SANDBOX_URL` 指向的那一个沙箱。单栈时就是本机 1984。

想先看调用通不通，可以用 README 里的那条 curl，打到 3001，允许的工具只有 `filesystem_read_text_file`。它仍然经过循环和沙箱，题面不会被拿去读一个上游网站。

## 自己构建镜像

只有要改程序集合、改钉死的版本，或改烤进镜像的数据时，README 才让你 `make build` 再 `make run-docker`。构建会做 [05-how-tools-exist.md](05-how-tools-exist.md) 里的预装，以及那 8 个题目仓库的克隆，所以构建机器要能访问那些地址。现成镜像把这些层已经做完。两种方式都不把 `.env` 烤进去。

## 多开几条栈

README 的例子是再起容器，端口错开。一条栈可以是容器 `1984:1984`、循环在 3001、沙箱地址指向 1984。另一条是容器 `1985:1984`、循环在 3002、沙箱地址指向 1985。然后各用一个 `HARNESS_URL` 跑一部分 CSV，再把输出接起来。

一道题从开始到结束留在同一条栈上。这样 filesystem、memory、git、MongoDB 在这一题里看到的是同一份状态。这仍然是循环的 HTTP 打到某一个沙箱的 `/call-tool`。

## 把沙箱地址指到别的实现

因为循环只通过 `MCP_SANDBOX_URL` 找沙箱，可以把这个变量指到另一个服务，只要那个服务提供同样的 `/list-tools` 和 `/call-tool`。变更记录写 Scale 内部用 Modal 做按题分配，那个实现不在公开发布里。公开仓库给出的是这个 HTTP 约定。

## 用本地表格代替 Hugging Face

`--input tasks.csv` 时不下载数据集。README 要求有 `TASK`、`PROMPT`、`ENABLED_TOOLS` 三列。评分还要 `GTFA_CLAIMS`。`ENABLED_TOOLS` 可以是 JSON 列表。元素可以是工具名字符串，也可以是带 `name` 字段的对象。公开 500 里 495 行是字符串，5 行是对象。`run_eval.py` 两种都读，交给循环的仍是名字。

## 一次运行的上限

`--max-turns` 默认 256。轮数用尽时，循环记一条轮数到达上限。

`--max-tool-calls` 默认 100。论文附录 A 也把每题预算写成 100 次。次数用尽时循环停下。

`--concurrency` 默认 5，是同时在跑的题数。

`--timeout` 默认 1800 秒，是批量脚本等待一道题的 HTTP 上限。

单次工具调用默认等 60 秒（`TOOL_CALL_TIMEOUT_MS`）。超时会变成一条工具错误文本交回模型，循环可以继续。向沙箱要工具列表默认等 180 秒。一次模型补全默认等 600 秒。

模型那一侧的 HTTP，对 500、502、503、429 和超时最多尝试 3 次。这是对模型服务的重试，不是对上游 MCP 网站的重试策略。

健康检查默认开着。`run_eval.py` 先请求沙箱的 `GET /enabled-servers`，有程序离线就退出，然后运行 `services/mcp_eval/test_servers.py`。函数注释写，每个程序一次真实调用，失败则整次运行中止。`--skip-health-check` 可以跳过。

评分是另一次命令：`python services/scoring/score_claims.py`，输入带事实句的表和带模型回答的 CSV。诊断又是一次命令：`services/diagnostics/single_model_diagnostic.py`。诊断给失败归类，不改覆盖率。

## 这条默认路径里没有的东西

不公开的 500 道题，默认加载不到。

Modal 那套按题开沙箱的实现，仓库里没有。

镜像没有 `/reset-state`。循环源码写这个路径会返回 404，所以默认不重置。论文描述的「每题重启容器」是他们那次实验的跑法。

题面不会直接 POST 到 Brave、GitHub 或 Notion。外网请求如果发生，发生在 MCP 子进程内部。

`convert_tasks_to_harbor.py` 不是 README 的默认跑法。它假设的地址是 `http://localhost:<端口>/mcp`，外加一个工具名单文件。沙箱实际提供的是 1984 上的 `/call-tool`。
