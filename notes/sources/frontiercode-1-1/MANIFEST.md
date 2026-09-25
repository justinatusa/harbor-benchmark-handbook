# MANIFEST

- slug: `frontiercode-1-1`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://cognition.com/blog/frontier-code-1.1
- 官方仓: 没有
- commit: 没有
- 论文: 没有 arXiv id。方法页是这篇 blog，原文是 https://cognition.com/blog/frontier-code （2026-06-08），榜是 https://cognition.com/frontiercode
- HF: 没有

GitHub 仓库搜索 `frontiercode in:name` 的前几条是别的项目（商业站、航空公司笔试等），对不上 Cognition 这篇评测。`kimjune01/frontiercode-audit` 是第三方审计，不是任务集。Cognition 原文写：“While we don’t currently plan to release the tasks publicly to avoid contamination”。

## 测什么

测模型交出的改动是否达到维护者会合并的生产代码质量，标准包括正确性、测试、范围、风格和仓库规范，而不只是功能正确。出处：https://cognition.com/blog/frontier-code “Would the maintainer actually merge this PR?”，以及榜页 https://cognition.com/frontiercode “FrontierCode is the first benchmark to measure mergeability”。1.1（2026-07-07，https://cognition.com/blog/frontier-code-1.1）改的是方法：区分合法出网和能看到答案的出网；审计 1000+ blocker 后把 75 条过严项降为非 blocker；不再报 Diamond。之后报 Main 和 Extended。原文对子集的定义是 Extended 全量 150，Main 为其中最难的 100，Diamond 为最难的 50；1.1 写 Diamond 在修订后不再代表最难的 50，且太吵，所以弃用。

## 环境

- 容器: 官方 blog 和榜页没有写任务跑在哪种容器里。
- 出网: 开着。1.1 不把网关掉。合法用途包括查文档和报错；查到上游 PR、补丁、solution-bearing mirror 或 vendored copy 的 run 被程序判为 0 分。他们试过约 1200 域的 blocklist 和按题 allowlist，文中写这两条都放弃了，改用提示词加扫描器。部分题按设计就要出网，例如查 API contract。
- GPU: 没看到。
- K8s: 没看到。
- 多容器: 没看到。

第三方页面（Epoch、BenchLM）写过 container 和 harness 名字。那些不是 Cognition 的任务规格，这里不采用。

## 评分

混合，有的检查要另外的模型。原文表：classical 单测、command 退出码、reverse-classical（agent 的测试在 base commit 上必须失败）、scope 的 files/size，这些是程序化的。scope 的 semantic 和 “Code quality / prompt” 用 LLM。adaptive classical grading 用他们的 `mutagent`，由 LLM 改测试或应用代码以对齐实现细节，然后再跑测试。blocker 全过才有分，否则为 0；分数是 rubric 加权。1.1 的不公平出网扫描是程序化的，命中即 0 分。所以整套分数不是纯确定性测试。

## agent / runtime

unknown。1.1 blog 和榜页抓到的正文没有写被测 agent 的名字、进程放在哪、或任务沙箱的实现。原文 QC 段写他们也让 Devin 想办法钻 rubric，那是出题质量控制，不是榜上的 runtime 规格。榜页导航里的 Devin 是产品链接。

## 体积与是否入 git

没有公开任务树可克隆。本目录只留本文件和 `excerpts.md`，可以进 git。交互演示里的单题说明（`LOG_WARNING` / `jsonschema`）在 blog 正文里，已摘进 `excerpts.md`，不是可运行的任务包。

## 未抓取

- 任务、rubric 全文、镜像、runner。官方写不公开任务。
- 榜上的模型分数表。页面是客户端渲染，本次抓到的是方法说明和 changelog，没有一份稳定的分数 TSV。
- 第三方审计仓。它不提供官方任务。

MANIFEST-END
