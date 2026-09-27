# 出处、提交号和勘误

主阅读讲评测由哪几块组成、一只镜像怎么挂 server、一个 server 为什么有很多 tool、每题为什么只开一小撮。这一页给核对原句的人。数字的两句定义在 [03-numbers-glossary.md](03-numbers-glossary.md)。前面的说明不依赖这一页也能读。

核对日 2026-09-27。没有启动镜像，没有对在线服务调用 `/list-tools`，没有读取不公开的 500 道题。

## 四份公开材料

代码仓是 https://github.com/scaleapi/mcp-atlas ，提交 `f24ba3fb0bfa484c86acb28431fad6d7282455f9`。GitHub 的 git tree 接口返回 `truncated: false`，102 个条目。正文使用的 raw 地址形如 `https://raw.githubusercontent.com/scaleapi/mcp-atlas/f24ba3fb0bfa484c86acb28431fad6d7282455f9/<路径>`。提交说明的日期是 2026-08-03，内容是把沙箱依赖里的 starlette 从 0.46.2 升到 1.0.1。

论文是 https://arxiv.org/abs/2602.00933 ，HTML 在 https://arxiv.org/html/2602.00933 。用到的是摘要、第 3 节、表 2、表 5、附录 B、附录 C、附录 D、附录 E、附录 H、附录 J。

数据集是 https://huggingface.co/datasets/ScaleAI/MCP-Atlas ，修订 `8c563b55d7c967755f474299848049834d624617`。数据集 API 的 `sha` 与此相同，`lastModified` 为 2026-08-03。parquet 地址是 `https://huggingface.co/datasets/ScaleAI/MCP-Atlas/resolve/8c563b55d7c967755f474299848049834d624617/MCP-Atlas.parquet` ，15,638,757 字节。卡片许可证是 CC-BY-4.0。这个文件没有放进本仓库。

接口目录是 https://gist.github.com/geobio/d0272d41ea395376233f1617a3988860 。gist API 的 `updated_at` 为 2025-12-18T05:41:19Z，文件名 `mcp-atlas-tools.txt`。README 在提交 `f24ba3f` 的 Overview 里链到这个 gist。gist 早于上面的代码提交。

仓根的 `LICENSE` 是 MIT，版权行写 2026 Scale。论文附录 H 写循环和评分器以 Apache 2.0 发布，题面、事实句、调用记录和干扰项的选择以 CC-BY-4.0 发布。三句话分别对应这一提交的许可证文件、论文对代码许可的说法、Hugging Face 卡片上的数据许可。

2026-09-27 匿名请求 `https://ghcr.io/v2/scaleapi/mcp-atlas/tags/list`。返回 `1.2.0`、`1.2.1`、`1.2.2`、`1.2.3`、`1.2.4`、`1.2.5`、`1.2.6`、`1.2.7`、`latest`。没有 `1.0` 或 `1.1` 开头的标签，也没有 `v2.0.0`。Makefile 的 `VERSION = 1.2.7`。

若同仓存在 Harbor 手册，介绍卡路径是 `docs/layer2/mcp-atlas.md`，摘录路径是 `notes/sources/mcp-atlas/MANIFEST.md`。摘录抓取日是 2026-09-24。那里的提交号、镜像标签、500 行，以及 220 与 307 并存，和这次核对一致。本目录不依赖这两份文件。

## 读过的文件

都在提交 `f24ba3f`：`README.md`、`CHANGELOG.md`、`Makefile`、`LICENSE`、`.gitmodules`、`env.template`、`data_exports/README.md`、`run_eval.py`。沙箱侧读了 Dockerfile、`entrypoint.sh`、`dev_scripts/install_mcp_packages.sh`、`data/repos/git_submodule_info.csv`、`src/agent_environment/main.py`、`mcp_client.py`、`mcp_server_template.json`，以及该目录的 README。循环侧读了 `src/index.ts`、`src/config.ts`、`src/mcp-agent/schema.ts`、`agent-evals/agent-eval.ts`、`helpers/mcp-client/sandbox-client.ts`、`helpers/mcp-server-configs.ts`。评分脚本读了 `services/scoring/score_claims.py` 的默认模型参数，以及 `pass_rate_0.50`、`pass_rate_0.75` 两处输出。另读了 `services/mcp_eval/convert_tasks_to_harbor.py` 的文件头，和 `extract_mcp_servers_per_task.py` 如何从轨迹里取工具名。计数不以那份抽取脚本为准。

## 公开 500 行怎样数

用 pyarrow 读取上述 parquet。列是 `TASK`、`ENABLED_TOOLS`、`PROMPT`、`GTFA_CLAIMS`、`TRAJECTORY`。

工具名来自 `json.loads` 之后的 `ENABLED_TOOLS`。495 行是字符串列表。5 行是对象列表，取其中的 `name`。没有一行出现重复名字。

参考调用来自 `json.loads` 之后的 `TRAJECTORY`，收集 `tool_calls[].function.name`。调用次数按条数计。不同工具按集合计。程序前缀是名字在第一个下划线处切开的前半段。模板里的程序键用连字符，不用下划线。

干扰项按「这一行的允许名单，去掉这一行轨迹里出现过的名字」计数。这与论文附录 J 的定义一致：看见的集合减去必需集合。只在轨迹里的名字都落在允许名单内时，这个减法才严格成立。有 4 道题不满足，题号写在下面。

题面是否写下工具 id：若任一允许的名字是 `PROMPT` 的子串，算命中。500 行的命中数是 0。

事实句条数用 `ast.literal_eval`。499 行得到列表。题 `689cd6f8522029b7ad7b1fe5` 的字符串没有闭合，不计入均值。

gist 里以 `- ` 开头的行是 307。程序标题里的个数相加也是 307。

精确分数：允许名单长度 7598/500 = 15.196。轨迹调用条数 2423/500 = 4.846。轨迹中不同工具名 2055/500 = 4.11。允许名单减去轨迹名字 5547/500 = 11.094。论文印刷的 15.2、4.1、11.1、9.8 是全量 1,000 题上的表述。

## 20、11、5 怎样核对

模板 `mcpServers` 的键是 36 个。`DEFAULT_SERVERS` 是其中 20 个，与 `env.template` 的注释一致。数据说明点名的 5 个服务对应 `airtable`、`google-workspace`、`notion`、`mongodb`、`slack`。剩下 11 个键带有 `${变量}`，并且不在这 5 个里。

## 调用经过的代码

端口 3001 在 `services/agent-harness/src/config.ts`，未设置 `PORT` 时用 3001，`env.template` 写着 `PORT=3001`。`POST /v2/mcp_eval/run_agent` 在 `src/index.ts`。沙箱默认地址在同一份 `config.ts`。`make run-docker` 映射 `-p 1984:1984`。`/call-tool` 由 `sandbox-client.ts` 拼出来，由 `main.py` 接收。本地标准输入输出来自模板的 `command` 和 `args`，slack 的参数包含 `--transport stdio`，`mcp_client.py` 把配置交给 FastMCP 客户端。每题按名字过滤在 `sandbox-client.ts` 的 `listTools`。镜像不烤密钥，来自 README 和 `entrypoint.sh` 的 `envsubst`。构建时克隆题目仓库，来自 Dockerfile 读取 `git_submodule_info.csv` 的那一层。

## 45 个键怎么变成 36 个

初始提交 `51bf4797d43566b0b6ff1c2c484e7262582da792`（2025-12-03）的 `mcp_server_template.json` 有 45 个键。提交 `01b94cce39ac71873a915f891873c7bbfbbc0cd0`（2025-12-15）删掉 9 个：airbnb、anili、balldontlie、f1-mcp-server、reddit、rijksmuseum-server、yfmcp、youtube、youtube-transcript。提交说明写，这 9 个对当时说的公开数据集不再需要。当前 HEAD 的模板是 36 个键。

这 9 个里，公开允许名单还出现 `anili`、`balldontlie`、`f1-mcp-server`、`rijksmuseum-server`。另外 5 个公开名单里没有。`balldontlie-mcp` 仍在 `/data/repos` 的题目材料里，当前模板不启动它。

发布镜像 1.2.7 的提交是 `b6edd44b69892894ffa282f356e2dba41b41e298`（2026-07-17）。说明写 exa 从旧版换到 3.2.1，`exa_web_search_exa` 的名字不变，另外默认多暴露 `exa_web_fetch_exa`。gist 仍把 exa 算成 1 个工具。没有对运行中的镜像做 `list_tools`，文档口径维持 gist 的 307。

沙箱缓存：`services/agent-environment/src/agent_environment/main.py` 的 `CACHE_TTL_HOURS = 48`。`CACHEABLE_SERVERS` 里 arxiv、cli-mcp-server、filesystem、git 被注释掉。

## 名单和目录对不上的地方

公开允许名单与 gist 的交集是 194。gist 里有 113 个名字从未进入公开允许名单。113 等于 307 减 194。不要用 307 减 220，那个差是 87，对不上这 113。

220 减去模板外的 25 个名字，剩下 195。195 与 gist 相交 194 个。只在题面、不在 gist 里、但前缀仍属于当前 36 个进程的，是 `clinicaltrialsgov-mcp-server_clinicaltrials_search_studies`。

这 220 个允许名单字符串里，有 25 个的前缀不是模板里的启动键：`anili` 12 个，`balldontlie` 2 个，`f1-mcp-server` 8 个，`rijksmuseum-server` 3 个。它们出现在 85 道题的允许名单里，500 条参考调用里都没有用过。模板没有启动这四个程序。在已读的模板里，它们不是键。`balldontlie-mcp` 在镜像里是 `/data/repos` 下的一份仓库，给读文件、读 git 的题目用，不是一个被拉起的 MCP 进程。

有 4 道题，参考调用里有一个名字不在该题的允许名单里：

- `689f4d693e212e8ef339071d` 的记录里有 `github_get_pull_request`
- `689cd6f8522029b7ad7b2015` 的记录里有 `filesystem_read_file`
- `68a398aa2f58036e8d45edeb` 的记录里有 `mongodb_aggregate`
- `6896416f7b30e5d8ccd7c8b9` 的记录里有 `filesystem_list_allowed_directories`

沙箱代码里有一张旧名到新名的表，例如 `MongoDB_find` 对应 `mongodb_find`。上面这 4 个名字不在那张表里。

数据集卡片写每题暴露大约 10 到 25 个工具、每题 3 到 6 次调用。公开文件是允许名单 7 到 37 个名字，参考调用 3 到 17 次。卡片和文件不一致时，以文件计数为准。

论文附录 B 写容器会重启，避免上一题的文件留到下一题。公开循环的源码写，不调用 `/reset-state`，因为镜像对这个路径返回 404。README 允许多道题同时打到同一个沙箱。

论文附录 B 写有出网允许列表。公开提交的文件名里没有防火墙清单。变更记录写内部的 Modal 代理不在公开发布中。

论文第 3.3 节的正式实验用了三个评判，主评判是 Gemini 3.1 Pro Preview。评分脚本默认 `gemini/gemini-3.1-pro-preview`，也可以用 `--evaluator-model` 或环境变量 `EVAL_LLM_MODEL` 换。

## 8 个题目仓库的提交

构建时克隆到 `/data/repos/`，提交号在 `data/repos/git_submodule_info.csv`。直接用预构建镜像时，这些检出已经在镜像层里。

- `balldontlie-mcp`：`48048b2911e1bfada5654b7a30e482fc8f4439be`
- `mcp-server-calculator`：`a07908b443aa8494aaa08eb6f4cb6f3033532817`
- `metmuseum-mcp`：`d0097d94bd2ca1ebda34c1a31cf9f3f906ce1750`
- `mongodb-mcp-server`：`d10b4e71c02be973524ae1a8bdc53b4f9ba9f3e2`
- `slackr`：`aa52b054c77ae424e2bafdf323c4114e248b05c0`
- `snake-game`：`93c5c9a0c9105ef08c3042e6433f2e504998932b`
- `storyteller`：`0865ef487b8100848fcab25af80e60bffb4f42da`
- `tree-sitter-diff`：`e42b8def4f75633568f1aecfe01817bf15164928`

## 没有写成结论的事

镜像 `1.2.7` 运行时 `list_tools()` 是否仍返回 307。gist 早于该提交，容器没有启动。

各个不需要密钥的包内部的具体网址。只引用了论文对真实端点的总述，和数据说明里「许多程序连接外部服务」那句。

论文榜上每个模型的通过率。正文只说明 82.2% 这类百分数的分母是全量 1,000 题、主评判、覆盖率至少 0.75。没有重跑。

不公开的 500 道题的任何字段分布。
