# 运行时：一只镜像，里面挂着多个 server

上一页的 sandbox 在运行时是一只镜像。README 推荐拉取 `ghcr.io/scaleapi/mcp-atlas:1.2.7`，打上本地名 `agent-environment:latest`，再用 `make run-docker` 启动。镜像标签的两句定义在数字词典。

容器里先起来的是沙箱自己的网页服务。它再按配置拉起 MCP server。配置在 `mcp_server_template.json`，一个键一条启动命令，例如 `calculator`、`filesystem`、`github`。不需要密钥的那一组默认会启动。需要密钥的，要等 `.env` 里对应变量有值，才会在自动模式下加进来。你如果写了 `ENABLED_SERVERS`，就只启动你点名的那些。

所以「一只镜像」和「很多个 server」同时成立。镜像是一个。server 是镜像里面的多个子进程。

## 一次调用经过的四段

```text
被测模型
  ^  对话接口，地址在 LLM_BASE_URL
  v
run_eval.py
  |  把一题交给循环
  v
harness，宿主机进程，默认端口 3001
  |  向沙箱要工具列表，再提交一次工具调用
  v
sandbox，容器里的网页服务，端口 1984
  |  用标准输入输出交给本机子进程
  v
MCP server（npx 或 uvx 拉起的程序）
  |
  v
有的只读容器里的文件，有的再去访问外部网站
```

`run_eval.py` 把一题交给 harness 的 `/v2/mcp_eval/run_agent`。默认地址是 `http://localhost:3001`。请求里有题号、题面、这一题允许的工具名、被测模型名，以及镜像名。这份公开客户端不会因为请求里写了镜像名就当场执行 `docker run`。容器要先启动。客户端实际使用的沙箱地址只有 `MCP_SANDBOX_URL`。

harness 要工具列表时，访问沙箱的 `/list-tools`。要执行工具时，把工具名和参数 POST 到 `/call-tool`。沙箱地址默认 `http://localhost:1984`。Makefile 把容器的 1984 映到本机的 1984。

沙箱这个网页服务自己不搜仓库，也不读文件。它把调用交给本机的 MCP 客户端。客户端按模板里的命令启动子进程，用标准输入输出跟子进程说话。slack 的启动参数里写了 `--transport stdio`，stdio 就是这种本机传输。端口 1984 上的路径是沙箱自己的 `/list-tools`、`/call-tool`、`/enabled-servers`、`/health`。

子进程拿到调用之后，有的只碰容器里的 `/data`，例如读文件、跑计算。有的会再访问外部网站，例如搜索和查仓库。密钥在容器启动时从 `.env` 注入，不写进镜像。哪些程序要密钥，见 [06-network-and-keys.md](06-network-and-keys.md)。程序是预先装进镜像的，还是启动时才去取，见 [05-how-tools-exist.md](05-how-tools-exist.md)。

## 模型看见的名单是后一步裁的

容器可以挂着很多 server。一道题不会把它们的全部动作都给模型。

harness 先拿到沙箱当前的工具列表。请求里如果带了 `enabledTools`，就只留下这些名字，再交给模型。模型返回工具调用之后，harness 才 POST `/call-tool`。模型不再调用工具时，循环停下，最后的文字拿去评分。

名单里多写一个沙箱没加载的名字，模型看不见。沙箱加载了、名单里没有的动作，模型也看不见。这个名单为什么又短、里面为什么还有用不上的动作，下一页讲。

`ENABLED_SERVERS` 决定哪些程序会启动。`ENABLED_TOOLS` 决定这一题让模型看见哪些动作。两个开关都带 enable，管的不是一件事。

## 同一题留在同一个沙箱

README 写，一道题的全部工具调用要打到同一个沙箱。filesystem、memory、git、MongoDB 假定这一题内部看到的是同一份文件和数据。按每一次调用分到不同容器，这些工具会对不上。

公开的这份循环不在题和题之间重置沙箱。源码写，不调用 `/reset-state`，因为镜像对这个路径返回 404。论文写他们评测时会在题之间重启容器。那是论文里的实验跑法。按公开 README 在本机跑，默认是一只容器一直开着。对照写在证据页。

被测模型和 judge 都不在这只容器里。沙箱镜像基于 Python 3.12 的瘦镜像，构建文件里没有安装显卡驱动的步骤。显卡不是这只沙箱的要求。
