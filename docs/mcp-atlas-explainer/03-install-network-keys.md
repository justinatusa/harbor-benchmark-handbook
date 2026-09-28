# 程序怎么放进沙箱，调用会不会出网

「有一个 MCP 工具」在公开代码里分成几段。镜像构建时装包。少数程序要等容器起来、子进程被拉起时才去取代码。调用时，沙箱用本机标准输入输出跟子进程说话。子进程需要时才自己访问外网。

默认路径是这四步。题面是自然语言，脚本把它放进一条用户消息。模型返回函数调用，名字来自它看见的工具列表。harness 把这个名字提交到沙箱的 `/call-tool`。沙箱用标准输入输出调用本机子进程。子进程若需要，再自己去访问外网。题面不会被拿去对 Brave、GitHub 或 Notion 发 HTTP POST。

## 构建时已经在镜像里的

沙箱的 Dockerfile 在构建时运行一份安装脚本。脚本用 `npm install -g` 装带版本号的 Node 包，用 `uv tool install` 装带版本号的 Python 包。注释写，预先装好是为了省掉大约一分钟的启动下载。脚本末尾写，从 GitHub 地址安装的那些被跳过。

装进镜像的是程序。接口密钥不进镜像。无论拉取现成镜像还是自己构建，密钥都在容器启动时从 `.env` 注入。入口脚本把模板里的变量换成当时的环境变量，再启动服务。

同一次构建把数据目录挪到容器内的 `/data`。那里有 CSV，例如 `Barber Shop.csv`，也有 memory 程序用的一份 JSON。读文件和记忆的默认路径指向这些容器里的文件。

构建镜像时，Dockerfile 读 `git_submodule_info.csv`，把 8 个仓库克隆到 `/data/repos/`，并检出固定提交。`.gitmodules` 是同一批：`balldontlie-mcp`、`mcp-server-calculator`、`metmuseum-mcp`、`mongodb-mcp-server`、`slackr`、`snake-game`、`storyteller`、`tree-sitter-diff`。它们是题目要读的代码和数据，给 filesystem 和 git 用。36 个 MCP 进程是另一批，由模板里的启动命令拉起。直接用预构建镜像时，这 8 份检出已经在镜像层里，每次启动不会再克隆。提交号在证据页。

## 启动时才去取代码的四个程序

另外 4 个 server 的启动参数直接指向 GitHub，预装脚本又跳过这类安装。容器起来、客户端按命令拉起子进程时，才会去取这些地址。它们是 `pubmed`、`weather-data`、`github`、`weather`。`weather` 不需要密钥。`weather-data` 需要密钥。两个都和天气有关，是两行不同的命令。

上面那 8 个仓库在构建时克隆进 `/data/repos`，给读文件的题目用。这 4 个是 MCP server 本身，要等子进程被拉起才取代码。

## 本机 stdio，出网发生在子进程里

模板里每一项都是一条本地命令。沙箱用 MCP 客户端拉起这些进程，经标准输入输出收发调用。模型只和 harness 对话。harness 用网页请求访问沙箱的 `/call-tool`。沙箱再写给本机子进程。端口 1984 上的网页接口是沙箱自己的。它不把上游厂商的地址原样转出去。

进程跑起来之后，有的只碰 `/data`。有的会发出自己的网页请求。论文第 3.1 节写，任务打到真实的线上端点。`data_exports/README.md` 写，许多 MCP 程序连接的是外部服务。某个包具体请求哪一台主机，看那个包自己的实现。这份说明没有逐个打开那些安装包，主机名也就没有逐个写下来。

沙箱对一部分工具结果做缓存，默认大约 48 小时，代码里的常数是 `CACHE_TTL_HOURS = 48`。arxiv、cli-mcp-server、filesystem、git 在这份缓存名单里被注释掉了。缓存只是同一条调用在这段时间里可以复用上次的返回。请求如果发生，仍是那个 MCP 进程自己发出的。

论文还写，他们评测用的容器有出网允许列表。公开仓库的文件名里没有防火墙清单。变更记录写，内部用另一套按题开沙箱的代理，那个代理不在公开发布里。公开构建文件能确认的是：包装在镜像里，进程由本地命令启动，密钥在运行时注入。

仓库里另有 `services/mcp_eval/convert_tasks_to_harbor.py`。它假设镜像在 `http://localhost:<端口>/mcp` 上提供接口，并用一份名单文件限制工具。README 的默认跑法走沙箱 1984 上的 `/call-tool`。

上一页那些模板外的名字（`anili`、`balldontlie`、`f1-mcp-server`、`rijksmuseum-server`，一共 25 个工具名）只是短名单上的字符串。容器不会为它们起进程，所以也没有再去访问外网这一步。公开参考轨迹里，这 4 个前缀一次都没有被调用。

## 密钥和自备数据

36 个 server 的准备方式，README 分成三类，加起来正好 36。要不要密钥，和会不会访问外网，是两件分开的事。

20 个不用往 `.env` 填这个程序的密钥。`ENABLED_SERVERS` 留空时，这 20 个会启动。名单在沙箱代码的 `DEFAULT_SERVERS` 里，也写在 `env.template` 的注释里：

arxiv、calculator、cli-mcp-server、clinicaltrialsgov-mcp-server、context7、ddg-search、desktop-commander、fetch、filesystem、git、mcp-code-executor、mcp-server-code-runner、memory、met-museum、open-library、osm-mcp-server、pubmed、weather、whois、wikipedia。

这 20 个里，按模板只在容器内做计算、读文件、跑受限制的命令或记笔记的有 8 个：calculator、cli-mcp-server、desktop-commander、filesystem、git、memory、mcp-code-executor、mcp-server-code-runner。另外 12 个启动时不带账号，工具一被调用就会从沙箱出去访问网站：arxiv、clinicaltrialsgov-mcp-server、context7、ddg-search、fetch、met-museum、open-library、osm-mcp-server、pubmed、weather、whois、wikipedia。12 等于 20 减 8，数的是这 12 个程序。

那 8 个按模板只碰容器里的计算和文件。模型如果让 `mcp-code-executor` 或 `mcp-server-code-runner` 跑出带网页请求的代码，那段代码仍可能出网。`desktop-commander` 也能起进程。公开参考轨迹里抽到的代码调用，做的是本地计算。

模板和沙箱代码里能直接看到的限制：

- `cli-mcp-server` 只能在 `/data` 下执行 `ls`、`cat`、`find`，并且关掉了 shell 运算符。
- `desktop-commander` 在沙箱启动时，如果工具列表里有 `desktop-commander_set_config_value`，会被设成只允许目录 `/data`。
- `filesystem` 的启动参数把根目录设为 `/data`。
- `mcp-code-executor` 的代码目录是 `/data/repos/mcp_code_executor_workspace`。
- `memory` 的记忆文件是 `/data/repos/memory_mcp_server/memories-for-mcp.json`。
- `pubmed` 的启动参数指向 `git+https://github.com/geobio/PubMed-MCP-Server.git`，不在预装脚本里，也没有密钥占位符。
- `weather` 的启动参数指向 `https://github.com/geobio/smitheryai-mcp-servers-weather`，不在预装脚本里。它和要密钥的 `weather-data` 是两行配置。
- `wikipedia` 的版本是 `wikipedia-mcp==2.0.1`。预装脚本里有对应的 `uv tool install`，模板里没有密钥占位符。

arxiv、calculator、clinicaltrialsgov-mcp-server、context7、ddg-search、fetch、git、met-museum、mcp-server-code-runner、open-library、osm-mcp-server、whois 都是带版本号的 `npx` 或 `uvx` 包，构建时预装，模板里没有密钥占位符。包在运行时会请求哪一台主机，看那个包自己的实现。

11 个只要接口密钥。数据说明没有要求再上传一份业务数据。它们不在默认的 20 个里。自动模式下，对应变量为空就不启动。

alchemy 读 `ALCHEMY_API_KEY`。brave-search 读 `BRAVE_API_KEY`。e2b-server 读 `E2B_API_KEY`。exa 读 `EXA_API_KEY`。github 读 `GITHUB_TOKEN`。google-maps 读 `GOOGLE_MAPS_API_KEY`。lara-translate 读 `LARA_ACCESS_KEY_ID` 和 `LARA_ACCESS_KEY_SECRET`。national-parks 读 `NPS_API_KEY`。oxylabs 读 `OXYLABS_USERNAME` 和 `OXYLABS_PASSWORD`。twelvedata 读 `TWELVE_DATA_API_KEY`。weather-data 读 `WEATHER_API_KEY`。

这些密钥给子进程去对应服务上表明身份。循环不会把它们写进题面。`env.template` 里这些行是空的。公开仓库没有附带能用的密钥值。github 是两件事叠在一起：包从 GitHub 地址取，调用时再用令牌访问 GitHub 的接口。

5 个还要你自己的数据：Airtable、日历所用的 `google-workspace`、Notion、MongoDB、Slack。数据说明把要求写成三条：有该服务的账号，把样例放进那个账号，再用密钥或连接串去读。样例文件在仓库里。账号要你自己的。镜像构建时不登录这五个服务。

Airtable 用 `AIRTABLE_API_KEY`。样例是一个分享链接，在页面上点 Copy base，复制到你自己的 Airtable。

`google-workspace` 用 `GOOGLE_CLIENT_ID`、`GOOGLE_CLIENT_SECRET`、`GOOGLE_REFRESH_TOKEN`。样例是 `calendar_mcp_eval_export.zip`，解开是日历文件，导入你自己的 Google 日历。`env.template` 的注释同时提到 Gmail API 和 Google Calendar API。数据说明里的导入步骤只覆盖日历，没有一份邮箱导出。

Notion 用 `NOTION_TOKEN`。样例是 `mcp-atlas-notion-data.zip`，导入你自己的 Notion。

MongoDB 用 `MONGODB_CONNECTION_STRING`。样例是 `mongo_dump_video_game_store-UNZIP-FIRST.zip`，恢复到你自己的 MongoDB Atlas。说明写免费的 M0 就够，恢复后是库 `video_game_store`，6 个集合、大约 1.68 万条文档。连接串指向你的集群。镜像内部没有一个已经装好的数据库端口在等这个连接串。

Slack 用 `SLACK_MCP_XOXC_TOKEN` 和 `SLACK_MCP_XOXD_TOKEN`。样例是 `slack_mcp_eval_export.zip`，导入你自己的工作区。说明写免费账号会隐藏超过 90 天的消息，样例时间在 2025 年 12 月初。

没有这些数据时，程序仍可能启动，但题目点名的记录会是空的，或直接报错。

把 12 个匿名出网的，和这 16 个带着密钥或账号的加在一起，调用后会离开本机的 server 是 28 个。16 是 11 加 5。28 个数的是程序。一道题的候选名单通常只点到其中几个。

复制 `env.template` 为 `.env` 再填写。`make run-docker` 用这份文件启动容器。被测模型的 `LLM_API_KEY` 和评判用的 `EVAL_LLM_API_KEY` 也在同一个文件里。它们交给宿主机上的循环和评分脚本。MCP 程序的密钥是上面那些另一组变量。
