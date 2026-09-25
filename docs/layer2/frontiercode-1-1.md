# FrontierCode 1.1

任务不公开。1.1 改的是出网判定和过严的 blocker，不是放出题面。被测 agent 的进程和沙箱，1.1 的 blog 和榜页没写。

1. 一句话测什么。测模型交出的改动是否达到维护者会合并的生产代码质量，标准包括正确性、测试、范围、风格和仓库规范，而不只是功能正确。出处是 https://cognition.com/blog/frontier-code “Would the maintainer actually merge this PR?”，以及榜页 https://cognition.com/frontiercode “FrontierCode is the first benchmark to measure mergeability”。

2. 官方源。没有官方 GitHub 任务仓，没有 arXiv id，没有 Hugging Face dataset id。方法页是 https://cognition.com/blog/frontier-code-1.1 （2026-07-07）。原文是 https://cognition.com/blog/frontier-code （2026-06-08）。榜是 https://cognition.com/frontiercode 。原文写 “we don’t currently plan to release the tasks publicly to avoid contamination”。GitHub 上名称相近的仓对不上这篇评测，不记为官方仓。

3. 形态。公开文字能对上 `verifier` 的混合检查。`task` 的题面不公开。`agent` 与 `environment` 在官方材料里是 unknown。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。暂不宜接。任务不公开。部分检查要另调模型。清单没有给出 `task.toml` 或 `dataset.toml`。

5. 环境。官方 blog 和榜页没有写任务跑在哪种容器里。出网开着。1.1 不把网关掉。合法用途包括查文档和报错；查到上游 PR、补丁、solution-bearing mirror 或 vendored copy 的 run 被程序判为 0 分。文中写约 1200 域的 blocklist 和按题 allowlist 都放弃了，改用提示词加扫描器。部分题按设计就要出网，例如查 API contract。GPU、Kubernetes、多容器都没看到，记 unknown。第三方页面写过 container 和 harness 名字，那些不是 Cognition 的任务规格，这里不采用。

6. 评分。混合，有的检查要另外的模型。原文表：classical 单测、command 退出码、reverse-classical（agent 的测试在 base commit 上必须失败）、scope 的 files/size，这些是程序化的。scope 的 semantic 和 “Code quality / prompt” 用 LLM。adaptive classical grading 用他们的 `mutagent`，由 LLM 改测试或应用代码以对齐实现细节，然后再跑测试。blocker 全过才有分，否则为 0；分数是 rubric 加权。1.1 审计 1000+ blocker 后把 75 条过严项降为非 blocker，不公平出网扫描命中即 0 分。1.1 不再报 Diamond。之后报 Main 和 Extended。原文对子集的定义是 Extended 全量 150，Main 为其中最难的 100，Diamond 为最难的 50；1.1 写 Diamond 在修订后不再代表最难的 50，且太吵，所以弃用。

7. agent/runtime。unknown。1.1 blog 和榜页抓到的正文没有写被测 agent 的名字、进程放在哪、或任务沙箱的实现。原文质量控制段写他们也让 Devin 想办法钻 rubric，那是出题检查，不是榜上的 runtime 规格。榜页导航里的 Devin 是产品链接。

8. 迁入代价。高。没有公开任务树、rubric 全文、镜像或 runner。语义和质量检查要另调模型。不公平出网的扫描规则写在 blog 里，没有可克隆的实现。

9. 对抽象的压力。`dataset` 接不上，题面不公开。`verifier` 要同时接程序检查、模型改写测试的 adaptive grading，以及模型对 diff 的质量分。`environment` 和 `agent` 的实现官方材料没写，记 unknown。

10. 本地摘录。[`notes/sources/frontiercode-1-1/MANIFEST.md`](../../notes/sources/frontiercode-1-1/MANIFEST.md)。
