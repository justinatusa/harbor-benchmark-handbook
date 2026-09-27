# 评测是什么，由哪几块组成

有人请助手查一件事：某款开源游戏的代码仓库是哪一年建的，官网域名又是哪一年注册的，两个年份差多少。助手不能凭记忆写一个数。它要自己决定去查仓库、查网页、查域名，再把结果算成一个差，写进回答。

MCP-Atlas 把这种事做成固定题目。官方 README 的第一句说，它在一个可复现的 Docker 沙箱里，用真实的 MCP server 看智能体会不会用工具，并用另一个语言模型打分。这种打分叫 LLM-as-judge：再请一个模型看回答盖住了多少条事实，不做字符串完全相等。

题面是一段话。它不写出该调用哪个程序，也不写出该调用哪个接口。论文第 3.2 节写，提示是单轮的，并且避免点名 server、工具或参数。公开 500 行上查过：把该行允许使用的工具 id 拿去在题面里搜索，500 行都没有出现这些 id。题面里仍可能出现 GitHub 这种普通词。那次搜索只检查工具 id。

## dataset：题库

dataset 是一组题。公开的那一半在 Hugging Face 的 `ScaleAI/MCP-Atlas`。`run_eval.py` 默认加载的就是这一份。论文里的全量是公开一半加上不随数据集发布的另一半。默认脚本加载不到那一半。

一行有五个字段。

`TASK` 是题号。`PROMPT` 是题面。`ENABLED_TOOLS` 是这一题允许模型看见的工具名。`GTFA_CLAIMS` 是回答里应该出现的事实句。`TRAJECTORY` 是一条够用的调用记录，含工具名、参数和当时返回的内容。

批量脚本只把题面和允许的工具名送给模型。事实句用来评分。调用记录用来事后看失败发生在哪。通过与否不看模型有没有走出和记录一模一样的调用。

## sandbox：沙箱

sandbox 是 `services/agent-environment/` 里的那只容器。镜像起来之后，一个进程在固定端口上提供网页接口。真正搜仓库、读文件的，是它再拉起的 MCP server。一个 server 是一个单独的程序。下一页讲一只镜像怎么挂住这批程序，以及调用怎么走进去。

## harness：循环

harness 是 `services/agent-harness/` 里的 TypeScript 循环，跑在宿主机上，不在沙箱容器里。变更记录写，这一版循环从 Python 改写而来，旧的 Python 循环目录已经从公开提交里删掉。

循环做两件对外的事。它按 OpenAI 对话接口去问被测模型，地址来自 `LLM_BASE_URL`。模型如果返回一次工具调用，循环就去沙箱执行，把结果塞回对话，再问模型。模型不再调用工具时，循环结束。最后那段文字就是交去评分的回答。

被测模型是模型服务。它和 GitHub、Notion 那些网站不是同一条连接。

## judge：评分

judge 是 `services/scoring/score_claims.py` 里的另一次模型调用。它读最终回答和 `GTFA_CLAIMS`。每条事实句单独看：完全盖住、盖住一部分，或没盖住。一道题的覆盖率是这些分数的平均。论文把达到主通过线的题算通过。评分脚本还会多输出一档更宽的通过率。两句定义在 [03-numbers-glossary.md](03-numbers-glossary.md)。

代码里的默认评判模型名是 `gemini/gemini-3.1-pro-preview`，可以用参数或环境变量换掉。论文那次正式实验用了三个评判模型，主评判是 Gemini 3.1 Pro Preview。本地默认值和那次三模型实验是两件分开的事。

诊断是另一支脚本，在 `services/diagnostics/`。覆盖率低于 0.75 的题才会归类。论文附录 E 写，归类标签不改通过与否。

和调用有关的有 4 类。`malformed_call`：工具选对了，参数错了。`wrong_tool`：选了一个解决不了这个子问题的工具，正确的工具当时看得到。`no_tool_use`：这题需要查外部信息，模型却直接用自己的知识作答。`err_recovery`：工具返回错误之后，模型原样重试、打转或者放弃。

和理解有关的有 7 类。`task_misunderstanding`：答成了另一个问题，或漏了题面里的要求。`faulty_synthesis`：工具返回是对的，组合或解释错了。`response_misparsing`：返回的结构读错了，或抽错了字段。`early_termination`：题意懂了，没做完就停。`hallucinated_fact`：回答里写出了任何工具输出都没出现的内容。`logical_error`：拿到的数据是对的，多步推理错了。`constraint_violation`：忽略了题面里写明的条件。

这 11 个名字在变更记录和 `mcp_failure_taxonomy.py` 里是同一套。出题时还用过一份更粗的三步核对：工具选得对不对、参数对不对、结果读得对不对。论文附录 D.3 写，那份核对和这 11 类不是同一张单子。

## 程序按什么领域放

论文把这些程序放进五个领域，用来说明题目碰到哪些软件。没有五张分开的榜。调用也不按这五类改道。

Basic 是搜索、天气、地图一类，论文写大约占三成到三成五，点名 brave_search、exa、weather、maps。Productivity 大约两成到两成五，点名 filesystem、notion、slack、arxiv。Coding 大约两成到两成五，点名 git、github、code-executor、cli。Analytics 大约一成到一成五，点名 airtable、mongodb。Financial 大约一成到一成五，点名 twelvedata、alchemy。

附录 B 给了落定后的比例：Basic 32%，Productivity 22%，Coding 22%，Analytics 12%，Financial 12%。表 2 是区间，附录是一个点。论文表 5 还统计有多少题把某个程序当作必需。那一列加起来会超过题目总数，因为一道题常常需要好几个程序。

论文选这些程序时写过一条标准：一个程序上要有多个相近的动作，才好把用不上的动作混进同一道题。这是后面「一个程序、很多接口」的原因。
