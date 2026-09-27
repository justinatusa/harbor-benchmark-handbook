# 密钥和数据分三类

36 个 server 的准备方式分三类。README 写：20 个不用额外准备，11 个要接口密钥，5 个要接口密钥还要准备数据。加起来是 36。

**20。** 是什么：不往 `.env` 填这个程序的密钥，默认也会启动的 server 个数。不是什么：不是「这 20 个都在容器里算完、不再访问网络」。其中不少在被调用时会查询公开网站。

**11。** 是什么：模板要求密钥，但数据说明没有要求你再上传一份业务数据的 server 个数。密钥为空时，自动模式不启动它们。不是什么：不是 11 道题。

**5。** 是什么：Airtable、日历所用的 `google-workspace`、Notion、MongoDB、Slack。要密钥，还要把样例放进你自己的账号。不是什么：不是镜像里已经登录好的五个线上账号。样例文件在仓库里，账号是你的。

要不要密钥，和会不会访问外网，是两件分开的事。

**8。** 是什么：那 20 个里，按模板只在容器内做计算、读文件、跑受限制的命令或记笔记的程序。它们是 calculator、cli-mcp-server、desktop-commander、filesystem、git、memory、mcp-code-executor、mcp-server-code-runner。不是什么：不是「绝对不会产生网络包」。两个跑代码的程序如果模型写出了带网页请求的代码，那段代码仍可能出网。`desktop-commander` 也能起进程。公开参考轨迹里抽到的代码调用，做的是本地计算。

**12。** 是什么：那 20 个里，启动时不带账号，工具一被调用就会从沙箱出去访问网站的程序。它们是 arxiv、clinicaltrialsgov-mcp-server、context7、ddg-search、fetch、met-museum、open-library、osm-mcp-server、pubmed、weather、whois、wikipedia。不是什么：不是 12 个容器，也不是「这 12 个都会立刻被封掉」。12 等于 20 减 8。

**28。** 是什么：会离开本机的 server 个数。12 个匿名，加上 11 加 5 共 16 个带着密钥或账号。不是什么：不是每道题会打 28 个网站。一道题的候选名单通常只点到其中几个。

## 20 个不要求密钥

名单在沙箱代码的 `DEFAULT_SERVERS` 里，也写在 `env.template` 的注释里。`ENABLED_SERVERS` 留空时，这 20 个会启动。

它们是 arxiv、calculator、cli-mcp-server、clinicaltrialsgov-mcp-server、context7、ddg-search、desktop-commander、fetch、filesystem、git、mcp-code-executor、mcp-server-code-runner、memory、met-museum、open-library、osm-mcp-server、pubmed、weather、whois、wikipedia。

下面只写模板和沙箱代码里能直接看到的限制。包在运行时会请求哪一台主机，看那个包自己的实现。

arxiv、calculator、clinicaltrialsgov-mcp-server、context7、ddg-search、fetch、git、met-museum、mcp-server-code-runner、open-library、osm-mcp-server、whois 都是带版本号的 `npx` 或 `uvx` 包，构建时预装，模板里没有密钥占位符。

另外几个有更具体的约束：

- `cli-mcp-server` 只能在 `/data` 下执行 `ls`、`cat`、`find`，并且关掉了 shell 运算符。
- `desktop-commander` 在沙箱启动时，如果工具列表里有 `desktop-commander_set_config_value`，会被设成只允许目录 `/data`。
- `filesystem` 的启动参数把根目录设为 `/data`。
- `mcp-code-executor` 的代码目录是 `/data/repos/mcp_code_executor_workspace`。
- `memory` 的记忆文件是 `/data/repos/memory_mcp_server/memories-for-mcp.json`。
- `pubmed` 的启动参数指向 `git+https://github.com/geobio/PubMed-MCP-Server.git`，不在预装脚本里，也没有密钥占位符。
- `weather` 的启动参数指向 `https://github.com/geobio/smitheryai-mcp-servers-weather`，不在预装脚本里，没有密钥。它和下面要密钥的 `weather-data` 是两行配置。
- `wikipedia` 的版本是 `wikipedia-mcp==2.0.1`。预装脚本里有对应的 `uv tool install`，模板里没有密钥占位符。

## 11 个只要密钥

这 11 个不在默认的 20 个里。自动模式下，对应变量都不是空的才会启动。

alchemy 读 `ALCHEMY_API_KEY`。brave-search 读 `BRAVE_API_KEY`。e2b-server 读 `E2B_API_KEY`。exa 读 `EXA_API_KEY`。github 读 `GITHUB_TOKEN`。google-maps 读 `GOOGLE_MAPS_API_KEY`。lara-translate 读 `LARA_ACCESS_KEY_ID` 和 `LARA_ACCESS_KEY_SECRET`。national-parks 读 `NPS_API_KEY`。oxylabs 读 `OXYLABS_USERNAME` 和 `OXYLABS_PASSWORD`。twelvedata 读 `TWELVE_DATA_API_KEY`。weather-data 读 `WEATHER_API_KEY`。

这些密钥给子进程去对应服务上表明身份。循环不会把它们写进题面。`env.template` 里这些行是空的。公开仓库没有附带能用的密钥值。

github 是两件事叠在一起：包从 GitHub 地址取，调用时再用令牌访问 GitHub 的接口。

## 5 个还要你自己的数据

数据说明把要求写成三条：有该服务的账号，把样例放进那个账号，再用密钥或连接串去读。

Airtable 用 `AIRTABLE_API_KEY`。样例是一个分享链接，在页面上点 Copy base，复制到你自己的 Airtable。

`google-workspace` 用 `GOOGLE_CLIENT_ID`、`GOOGLE_CLIENT_SECRET`、`GOOGLE_REFRESH_TOKEN`。样例是 `calendar_mcp_eval_export.zip`，解开是日历文件，导入你自己的 Google 日历。`env.template` 的注释同时提到 Gmail API 和 Google Calendar API。数据说明里的导入步骤只覆盖日历，没有一份邮箱导出。

Notion 用 `NOTION_TOKEN`。样例是 `mcp-atlas-notion-data.zip`，导入你自己的 Notion。

MongoDB 用 `MONGODB_CONNECTION_STRING`。样例是 `mongo_dump_video_game_store-UNZIP-FIRST.zip`，恢复到你自己的 MongoDB Atlas。说明写免费的 M0 就够，恢复后是库 `video_game_store`，6 个集合、大约 1.68 万条文档。连接串指向你的集群，不是镜像内部的一个数据库端口。

Slack 用 `SLACK_MCP_XOXC_TOKEN` 和 `SLACK_MCP_XOXD_TOKEN`。样例是 `slack_mcp_eval_export.zip`，导入你自己的工作区。说明写免费账号会隐藏超过 90 天的消息，样例时间在 2025 年 12 月初。

没有这些数据时，程序仍可能启动，但题目点名的记录会是空的，或直接报错。

复制 `env.template` 为 `.env` 再填写。`make run-docker` 用这份文件启动容器。被测模型的 `LLM_API_KEY` 和评判用的 `EVAL_LLM_API_KEY` 也在同一个文件里。它们交给宿主机上的循环和评分脚本，不是上面这些 MCP 程序的密钥。
