# MCP-Atlas 说明书

这份说明给没读过 MCP-Atlas 的人。MCP 是 Model Context Protocol，语言模型用来调用外部程序的一套约定。读完可以回答三件事：一道题在考什么，一次评测从题面走到分数要经过哪几段，以及模型看见的短名单和仓库里那份大目录各管哪一层。

## 一页全景

有人问某款开源游戏：代码仓库是哪一年建的，官网域名又是哪一年注册的，两个年份差多少。助手不能凭记忆写一个差。它要自己决定去查仓库、查网页、查域名，再算一次减法。

MCP-Atlas 把这类事做成固定题目。题面是一段话，不写该用哪个程序，也不写该调哪个接口。模型在一份短名单里挑动作，把结果串起来，写出回答。另一个模型对照事先写好的事实句打分。

一次运行里有四块。dataset 是题库，公开的一半在 Hugging Face，一行一道题。sandbox 是一只 Docker 镜像，里面同时挂着多个 MCP server。每个 server 是一个单独启动的程序，一个程序再公布多个 tool。harness 是宿主机上的循环：它问被测模型，模型要调工具时，它替模型去沙箱执行。judge 是另一次模型调用，只看最终回答盖住了多少条事实，不再去调那些工具。

目录、短名单、干扰项、密钥和版本，都从这四块往下拆。提交号和论文对不上文件的句子放在最后，不挡阅读。

## 阅读顺序

1. [01-one-run.md](01-one-run.md)：一道题在考什么。dataset、sandbox、harness、judge 在一次运行里各做什么，分数和失败归类从哪来。
2. [02-servers-and-shortlists.md](02-servers-and-shortlists.md)：为什么不把目录里的动作全塞给模型。server 和 tool 怎么分层，全目录、公开题并集、每题短名单、参考调用真正用过的工具，各数哪一层。
3. [03-install-network-keys.md](03-install-network-keys.md)：程序是镜像里预装的、启动时从 git 取的，还是用本机标准输入输出说话；子进程什么时候再出网；密钥和自备数据要准备到哪一步。
4. [04-versions-and-running.md](04-versions-and-running.md)：镜像标签和包版本，以及 README 里的几种跑法。
5. [99-evidence.md](99-evidence.md)：出处、计数过程、对不上的句子。查数时再翻。文末有一张对照表，定义以前面的叙述为准。

同仓的介绍卡在 `docs/layer2/mcp-atlas.md`，摘录在 `notes/sources/mcp-atlas/MANIFEST.md`。本目录不依赖这两份文件。
