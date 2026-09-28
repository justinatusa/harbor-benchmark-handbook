# 版本，以及按 README 怎么跑

跑的时候要对上镜像标签和包版本。论文编号 arXiv 2602.00933、数据集修订号、变更记录里的 v2.0.0，各管一件事。题目表没有一列镜像号。

## 登记过的镜像标签

公开推荐拉取 `ghcr.io/scaleapi/mcp-atlas:1.2.7`，再打上本地名 `agent-environment:latest`。Makefile 写的是 `VERSION = 1.2.7`。

2026-09-27 匿名请求 `https://ghcr.io/v2/scaleapi/mcp-atlas/tags/list`。返回的标签是 `1.2.0`、`1.2.1`、`1.2.2`、`1.2.3`、`1.2.4`、`1.2.5`、`1.2.6`、`1.2.7` 和 `latest`。列表里没有 `1.1` 开头的标签，也没有 `1.0` 开头的。要拉 `1.1.x` 或 `1.0.x` 的人，在这次登记里找不到对应标签，拉取命令里也不要写这两段。

`latest` 也在仓库的标签列表里。README 的做法是把 `1.2.7` 拉下来，再在本机标成 `agent-environment:latest`。本机这个名字来自刚拉下来的 `1.2.7`。仓库标签列表里的 `latest` 这次没有单独对过内容。跑的时候以 Makefile 钉住的 `1.2.7` 为准。

变更记录把循环从 Python 改成 TypeScript 的那一节标成 v2.0.0。它描述的是 TypeScript 循环和 `/v2/` 路径。旧的 Python 循环目录已经不在这个公开提交里。`ghcr.io/scaleapi/mcp-atlas` 的标签列表里没有 `v2.0.0`。镜像标签仍是上面那一串 `1.2.0` 到 `1.2.7`，外加 `latest`。

基础镜像是 `ghcr.io/astral-sh/uv:python3.12-bookworm-slim`。Dockerfile 另外安装 Node.js 20。注释写 Debian bookworm 自带的 Node 18 太旧。容器里的应用虚拟环境用 Python 3.12。

发布 1.2.7 的提交是 `b6edd44b69892894ffa282f356e2dba41b41e298`（2026-07-17）。说明写 exa 从旧版换到 3.2.1，`exa_web_search_exa` 的名字不变，另外默认多暴露 `exa_web_fetch_exa`。这个多出来的名字不在 gist 的 307 里。当前代码仓的 tip 是更晚的 `f24ba3fb0bfa484c86acb28431fad6d7282455f9`（2026-08-03），内容是把沙箱依赖里的 starlette 从 0.46.2 升到 1.0.1。

## 每个程序钉住的包版本

版本字符串写在 `mcp_server_template.json` 的启动参数里，并和预装脚本对应。从 git 地址启动的 pubmed、weather-data、github、weather 没有 npm 或 uv 的版本号，见 [03-install-network-keys.md](03-install-network-keys.md)。

- airtable：`@felores/airtable-mcp-server@0.3.0`
- alchemy：`@alchemy/mcp-server@0.1.8`
- arxiv：`arxiv-mcp-server==0.2.11`
- brave-search：`@modelcontextprotocol/server-brave-search@0.6.2`
- calculator：`mcp-server-calculator==0.2.0`
- cli-mcp-server：`cli-mcp-server==0.2.5`
- clinicaltrialsgov-mcp-server：`clinicaltrialsgov-mcp-server@1.0.8`
- context7：`@upstash/context7-mcp@1.0.14`
- ddg-search：`duckduckgo-mcp-server==0.5.0`
- desktop-commander：`@wonderwhy-er/desktop-commander@0.2.7`
- e2b-server：`@e2b/mcp-server@0.2.0`
- exa：`exa-mcp-server@3.2.1`
- fetch：`mcp-server-fetch==2025.4.7`
- filesystem：`@modelcontextprotocol/server-filesystem@2026.7.10`
- git：`mcp-server-git==2026.7.10`
- google-maps：`@modelcontextprotocol/server-google-maps@0.6.2`
- google-workspace：`@geobio/google-workspace-server@0.1.0`
- lara-translate：`@translated/lara-mcp@0.0.11`
- mcp-code-executor：`@geobio/code_execution_server@0.2.1`
- mcp-server-code-runner：`mcp-server-code-runner@0.1.7`
- memory：`@modelcontextprotocol/server-memory@2025.8.4`
- met-museum：`metmuseum-mcp@0.9.2`
- mongodb：`mongodb-mcp-server@0.2.0`
- national-parks：`mcp-server-nationalparks@1.0.1`
- notion：`@notionhq/notion-mcp-server@1.8.1`
- open-library：`@geobio/mcp-open-library@0.1.6`
- osm-mcp-server：`osm-mcp-server==0.1.1`
- oxylabs：`oxylabs-mcp==0.4.1`
- slack：`slack-mcp-server@1.1.23`
- twelvedata：`mcp-server-twelve-data==0.2.5`
- whois：`@bharathvaj/whois-mcp@1.0.1`
- wikipedia：`wikipedia-mcp==2.0.1`

8 个题目仓库在构建镜像时检出。容器每次启动不会再克隆它们。提交号在证据页。

## 拉现成镜像，跑公开的 500 道

README 的默认跑法是一台机器上的一条栈：一个沙箱容器，一个宿主机上的循环，一个 Python 批量脚本。扩容是多开这样的栈。题面仍然交给循环，不改成直接请求上游网站。

先复制 `env.template` 为 `.env`，填被测模型的 `LLM_API_KEY` 和 `LLM_BASE_URL`。业务程序的密钥按 [03-install-network-keys.md](03-install-network-keys.md) 需要再填。

然后拉取 `ghcr.io/scaleapi/mcp-atlas:1.2.7`，打上本地标签 `agent-environment:latest`，执行 `make run-docker`。容器把 1984 映出来。README 写启动要 1 分钟以上。环境目录的说明写大约 1 到 3 分钟，视启用了多少程序而定。Docker 内存至少留 8 GB，建议 10 GB 以上。这是 Docker 给容器留的内存。沙箱 Dockerfile 没有 GPU 安装步骤。模型推理如果要用显存，发生在 `LLM_BASE_URL` 那一头。

另开一个终端，在仓库根目录执行 `make install-harness`，再 `make run-harness`。循环听 3001。3001 是 harness 的端口。MCP 子进程走标准输入输出。上游网站的地址由各个包自己决定。

再开一个终端，`make install-python`，然后 `python run_eval.py --model "openai/gpt-4o" --output outputs.csv`。不传 `--input` 时，脚本加载 Hugging Face 上的 `ScaleAI/MCP-Atlas` 训练集，也就是公开的 500 行。不公开的一半不在这条默认路径上。

脚本把每题 POST 到循环的 `/v2/mcp_eval/run_agent`。输出 CSV 有三列：`task_id`、`raw_conversation_history`、`response`。已经写过的题号，下次再跑会跳过。同一题的工具调用打到当时 `MCP_SANDBOX_URL` 指向的那一个沙箱。单栈时就是本机 1984。1984 是沙箱自己的 HTTP 端口。子进程走标准输入输出。模型服务的地址在 `LLM_BASE_URL`。

想先看调用通不通，可以用 README 里的那条 curl，打到 3001，允许的工具只有 `filesystem_read_text_file`。它仍然经过循环和沙箱。

## 自己构建、多开、换沙箱地址、用本地表

只有要改程序集合、改钉死的版本，或改烤进镜像的数据时，README 才让你 `make build` 再 `make run-docker`。构建会做预装，以及那 8 个题目仓库的克隆，所以构建机器要能访问那些地址。现成镜像把这些层已经做完。两种方式都不把 `.env` 烤进去。

README 的扩容例子是再起容器，端口错开。一条栈可以是容器 `1984:1984`、循环在 3001、沙箱地址指向 1984。另一条是容器 `1985:1984`、循环在 3002、沙箱地址指向 1985。然后各用一个 `HARNESS_URL` 跑一部分 CSV，再把输出接起来。一道题从开始到结束留在同一条栈上，这样 filesystem、memory、git、MongoDB 在这一题里看到的是同一份状态。这仍然是循环的 HTTP 打到某一个沙箱的 `/call-tool`。

因为循环只通过 `MCP_SANDBOX_URL` 找沙箱，可以把这个变量指到另一个服务，只要那个服务提供同样的 `/list-tools` 和 `/call-tool`。变更记录写 Scale 内部用 Modal 做按题分配，那个实现不在公开发布里。公开仓库给出的是这个 HTTP 约定。

`--input tasks.csv` 时不下载数据集。README 要求有 `TASK`、`PROMPT`、`ENABLED_TOOLS` 三列。评分还要 `GTFA_CLAIMS`。`ENABLED_TOOLS` 可以是 JSON 列表。元素可以是工具名字符串，也可以是带 `name` 字段的对象。公开 500 里 495 行是字符串，5 行是对象。没有一行出现重复名字。`run_eval.py` 两种都读，交给循环的仍是名字。

## 一次运行的上限

`--max-turns` 默认 256，计的是对话轮。轮数用尽时，循环记一条轮数到达上限。一轮里可以调用多次工具。

`--max-tool-calls` 默认 100。论文附录 A 也把每题预算写成 100 次。次数用尽时循环停下。100 是调用次数的上限。这一题允许看见多少工具，看 `ENABLED_TOOLS` 的长度，公开题大多是十几个。

`--concurrency` 默认 5，是同时在跑的题数。

`--timeout` 默认 1800 秒，是批量脚本等待一道题的 HTTP 上限。沙箱从启动到就绪是另一段时间，上面写的是 1 分钟以上，或大约 1 到 3 分钟。

单次工具调用默认等 60 秒（`TOOL_CALL_TIMEOUT_MS`）。超时会变成一条工具错误文本交回模型，循环可以继续。向沙箱要工具列表默认等 180 秒。一次模型补全默认等 600 秒。

模型那一侧的 HTTP，对 500、502、503、429 和超时最多尝试 3 次。这是对模型服务的重试。上游 MCP 网站有没有自己的重试，看那个包的实现。公开循环没有替它们规定一套重试。

健康检查默认开着。`run_eval.py` 先请求沙箱的 `GET /enabled-servers`，有程序离线就退出，然后运行 `services/mcp_eval/test_servers.py`。函数注释写，每个程序一次真实调用，失败则整次运行中止。`--skip-health-check` 可以跳过。

评分是另一次命令：`python services/scoring/score_claims.py`，输入带事实句的表和带模型回答的 CSV。诊断又是一次命令：`services/diagnostics/single_model_diagnostic.py`。诊断给失败归类，不改覆盖率。

默认这条路径到不了三样东西。不公开的 500 道题，加载不到。Modal 那套按题开沙箱的实现，仓库里没有。镜像没有可用的 `/reset-state`，这个路径返回 404，循环默认不重置。论文描述的「每题重启容器」是他们那次实验的跑法。
