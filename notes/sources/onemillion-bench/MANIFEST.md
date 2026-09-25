# MANIFEST

- slug: onemillion-bench
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://github.com/humanlaya/OneMillion-Bench

## 官方仓

- 核实到的代码仓: https://github.com/humanlaya/OneMillion-Bench
- 默认分支: main
- commit SHA: `eb1ad8061152ae6d05a2adcc3c0d983675da962c`
- commit 说明: Merge pull request #4 from jacklanda/fix/append_omb_norm
- committer 日期: 2026-07-30T14:30:05Z
- 许可证: Apache-2.0
- GitHub API `size`: 10493 KB
- 递归树 71 个条目，`truncated=false`
- 大文件: `assets/omb.png` 7,209,227 字节，`tech_report.pdf` 2,184,842 字节
- 题面不在这个 git 里。README 的下载命令指向 `humanlaya-data-lab/OneMillion-Bench`

入口说明里的 HF 组织也存在，而且比 README 指向的那个新：

- https://huggingface.co/datasets/OneMillionBench/OneMillion-Bench
- 修订: `f0378e7226a867fd6db9a8d4a8b5750f1cb9ded5`
- `lastModified`: 2026-05-07T12:05:29.000Z
- 许可证卡: apache-2.0
- 文件: 五个域的 `test.json`、`economic_value.csv`（26,930 字节）、`LICENSE`、`README.md`、`.gitattributes`、`.DS_Store`
- `usedStorage`: 1,916,568 字节

README 仍指向的旧位置：

- https://huggingface.co/datasets/humanlaya-data-lab/OneMillion-Bench
- 修订: `5cf9d5005e2e1f20b4481ed50846161697e82a73`
- `lastModified`: 2026-03-11T06:34:22.000Z
- 没有 `economic_value.csv`
- `usedStorage`: 1,913,093 字节
- `economics_and_finance/test.json` 的 Content-Length：OneMillionBench 718,833 字节，humanlaya-data-lab 640,599 字节。两个仓不是同一份字节。

本次没有判定哪一份才是论文用的原件。代码仓 HEAD 的安装说明写的是 `humanlaya-data-lab`。

## 论文 / blog / HF

- 论文: https://arxiv.org/abs/2603.07980
- HTML: https://arxiv.org/html/2603.07980v1
- 代码仓 README 还链到 Humanlaya 榜、xbench 和 BIGAI 新闻。这些页面没有当作题面来源。
- xbench 转述: https://xbench.substack.com/p/introducing-onemillion-bench
- HF id（入口指定）: `OneMillionBench/OneMillion-Bench`
- HF id（该 commit 的 README）: `humanlaya-data-lab/OneMillion-Bench`

## 测什么

测语言代理在法律、金融、工业、医疗和自然科学里做专家级开放题时，事实、推理、可行性和职业规范是否过关。400 题，中英双语。出处：arXiv:2603.07980 摘要。HF 卡写同样的 400 条和五个域。

## 环境线索

- 容器: 代码仓 README、`docs/arch.md` 和论文没有写 Docker 或其它沙箱。harness 是本机 Python CLI。unknown。
- 出网: 要。生成和评判都打模型 API（OpenRouter、DashScope、VolcEngine、Hunyuan、Ling、LiteLLM）。`--enable-search` 打开网页搜索。`docs/web_search.md` 是 OpenRouter 网页搜索文档的拷贝，写 `:online` 或 `web` 插件。
- GPU: 没看到。推理在供应商 API 上。unknown。
- K8s: 没看到。unknown。
- 多容器: 没看到。unknown。

## 评分

要另外的 judge 模型，不是确定性对答案。

README 写 judge 对每条 rubric 做 yes/no，再按权重加总。`src/omb/config/default.yaml` 在这个 commit 里把 `JUDGE_MODELS` 设为 `google/gemini-3.1-pro-preview`，`REASONING_EFFORT` 为 `high`，并注释旧的 `google/gemini-3-pro-preview` 已不可用、新 judge 大约严 5–6 个点。摘录见 `excerpt-judge-config.txt`。论文式 (2) 把 Expert Score ≥ 0.7 记为通过；这个阈值作用在 judge 加权分上，不是字符串相等。论文 4.5 节写换六个 judge 时名次大致稳定，绝对分会变，GPT-5.2-High 更严、GLM-5 更松。

## agent / runtime

harness 有，操作系统级代理没有。CLI 名是 `omb`：读 JSON，调生成模型，再调 judge。可选网页搜索。论文另把供应商自带的 search agent 和 deep research 产品当黑盒来评（官方 scaffold、OpenRouter、无搜索）。那些产品的内部 runtime 不在本仓。本仓看到的运行时就是异步 HTTP 客户端，默认生成并发 128、超时 600 秒。

## 体积与是否入 git

代码仓 API size 10493 KB，主要是 7.2MB 海报和 2.2MB PDF。大于 5MB，没有克隆进 `/workspace`。

两个 HF 数据仓都约 1.9MB。单个 `test.json` 约 0.6–0.7MB，超过 200KB 摘录上限，没有落盘。

本目录只有本文件和 `excerpt-judge-config.txt`。本次没有 git commit。

## 未抓取项与原因

- 五个 `test.json`：单文件超过 200KB。字段以 HF 卡和 README 的任务格式为准。
- 两个 HF 仓内容不一致：只比较了 `economics_and_finance/test.json` 的字节数和文件列表，没有做逐题 diff。
- `tech_report.pdf` 和 `assets/omb.png`：不是小文本。
- 外部 search / deep research 产品的容器和工具循环：论文按产品名报告，没有公开运行时。
- 没有跑 `omb`，也没有调用 judge。

MANIFEST-END
