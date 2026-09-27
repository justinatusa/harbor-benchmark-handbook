# 版本

跑的时候要对上的是镜像标签和包版本。提交号、数据集修订号、许可证三句话对不上的地方，都在 [99-evidence.md](99-evidence.md)。

公开推荐拉取 `ghcr.io/scaleapi/mcp-atlas:1.2.7`，再打上本地名 `agent-environment:latest`。Makefile 写的是 `VERSION = 1.2.7`。

**1.2.7。** 是什么：现在这份 Makefile 和 README 让你拉取的沙箱镜像标签。不是什么：不是论文编号 arXiv 2602.00933，也不是变更记录标题 v2.0.0。题目表没有一列镜像号。发布这一标签的提交还写，exa 会多暴露一个清单里没有的工具，见证据页。早期模板曾经是 45 个 server，当前模板是 36 个，也记在证据页。

## 登记过的镜像标签

2026-09-27 匿名请求 `https://ghcr.io/v2/scaleapi/mcp-atlas/tags/list`。返回的标签是 `1.2.0`、`1.2.1`、`1.2.2`、`1.2.3`、`1.2.4`、`1.2.5`、`1.2.6`、`1.2.7` 和 `latest`。没有 `1.1.x`，也没有 `1.0.x`。

**1.2.0 到 1.2.7。** 是什么：这次标签列表里，沙箱镜像从 `1.2.0` 排到 `1.2.7` 的那一串。不是什么：不是 `1.1` 或 `1.0`。这两段不在列表里，不要写进拉取命令。

`latest` 也在列表里。README 的做法是把 `1.2.7` 拉下来，再在本机标成 `agent-environment:latest`。本机这个名字和仓库上的 `latest` 标签不是同一次核对。跑的时候以 Makefile 钉住的 `1.2.7` 为准。

变更记录把循环从 Python 改成 TypeScript 的那一节标成 v2.0.0。它描述的是 TypeScript 循环和 `/v2/` 路径。旧的 Python 循环目录已经不在这个公开提交里。这个标题不是镜像号。镜像标签是上面那一串 `1.2.0` 到 `1.2.7`，外加 `latest`。

**v2.0.0。** 是什么：变更记录里那次循环改写的标题。不是什么：不是 `ghcr.io/scaleapi/mcp-atlas` 上的镜像标签。标签列表里没有 `v2.0.0`。

基础镜像是 `ghcr.io/astral-sh/uv:python3.12-bookworm-slim`。Dockerfile 另外安装 Node.js 20。注释写 Debian bookworm 自带的 Node 18 太旧。容器里的应用虚拟环境用 Python 3.12。

## 每个程序钉住的包版本

版本字符串写在 `mcp_server_template.json` 的启动参数里，并和预装脚本对应。从 git 地址启动的 pubmed、weather-data、github、weather 没有 npm 或 uv 的版本号，见 [05-how-tools-exist.md](05-how-tools-exist.md)。

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

8 个题目仓库在构建镜像时检出，不是每次容器启动再拉。提交号在证据页。
