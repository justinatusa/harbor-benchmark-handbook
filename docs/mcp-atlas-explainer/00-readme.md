# MCP-Atlas 说明书

这份说明给没读过 MCP-Atlas 的人。MCP 是 Model Context Protocol，语言模型用来调用外部程序的一套约定。

## 一页全景

MCP-Atlas 出一道自然语言的题，看模型能不能自己挑工具、把工具串起来，写出一份对得上事实的回答。题面不写该用哪个程序，也不写该调哪个接口。

它有四块：

- dataset 是题库。一行一道题。公开题在 Hugging Face。每一行有题面，还有一列写这一题允许模型看见哪些工具。
- sandbox 是一只 Docker 镜像里的沙箱。容器起来之后，里面挂着一批 MCP server。server 是一个单独启动的程序。
- harness 是宿主机上的循环。它问被测模型，再替模型去沙箱调工具。
- judge 是另一个模型。它对照事实句给最终回答打分，不把回答送回那些工具。

后面先讲这四块，再讲运行时一只镜像怎么挂住那些 server，再讲一个 server 为什么有很多个 tool，最后讲一道题为什么只打开一小撮，其中还夹着故意放进来的干扰项。

## 阅读顺序

1. [01-what-is-mcp-atlas.md](01-what-is-mcp-atlas.md)：评测是什么，dataset、sandbox、harness、judge 各管什么。
2. [02-architecture.md](02-architecture.md)：一只镜像，里面挂多个 server。一次调用从循环走到沙箱，再走到本机程序。
3. [04-from-36-to-300.md](04-from-36-to-300.md)：一个 server 下面有多个 tool，所以几十个 server 会变成大约三百个接口。然后讲每题的 `ENABLED_TOOLS` 只打开一小撮，并混进干扰项。
4. [05-how-tools-exist.md](05-how-tools-exist.md)：这些程序是镜像里预装的、启动时从 git 取的、用本机标准输入输出说话的，还是自己再去访问外网。
5. [06-network-and-keys.md](06-network-and-keys.md)：哪些程序不用密钥，哪些要密钥，哪些还要你自己准备数据。
6. [03-numbers-glossary.md](03-numbers-glossary.md)：关键数字的两句定义。查数时翻，不必先读。
7. [07-versions.md](07-versions.md) 和 [08-run-shapes.md](08-run-shapes.md)：版本标签，以及按 README 怎么跑。
8. [99-evidence.md](99-evidence.md)：提交号、计数过程、论文和文件对不上的句子。核对时再看。

按上面的顺序，这一目录自己能读完。

若同仓还放着 Harbor 手册，介绍卡在 `docs/layer2/mcp-atlas.md`，摘录在 `notes/sources/mcp-atlas/MANIFEST.md`。这两份不在本目录里。路径断了也不影响上面的阅读。
