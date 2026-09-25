# browsecomp

- slug: `browsecomp`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://openai.com/index/browsecomp

## 官方仓

- 有。https://github.com/openai/simple-evals
- 默认分支 `main` HEAD: `652c89d0ca9df547706735883097e9537d40dc47`
- 核实: `git ls-remote` 的 HEAD 与 GitHub commits API 一致。commit 日期 2026-04-22（说明是 HealthBench PR 合并，仓仍托管 BrowseComp 参考实现）。
- 许可证: MIT。GitHub `size` 字段 110 KB。该 commit 的 blob 树无 Dockerfile / compose / Kubernetes 清单。

## 论文 / blog / HF

- blog 入口: https://openai.com/index/browsecomp
- 论文: arXiv [2504.12516](https://arxiv.org/abs/2504.12516)，标题 “BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents”，arXiv 页面 `citation_date` 为 2025/04/16。
- HF dataset id: 没有。题目不在 Hugging Face，而在公开 CSV。

## 测什么

测浏览智能体能否在网上持续找出难检索、彼此纠缠的短事实；共 1,266 题，答案短、可与参考答案对照。出处: arXiv 2504.12516 摘要（https://arxiv.org/html/2504.12516）；同文写明代码在 https://github.com/openai/simple-evals。

## 环境线索

- 容器: 该 commit 的文件树里没有 Dockerfile 或 compose。
- 出网: 参考实现会下载 `https://openaipublic.blob.core.windows.net/simple-evals/browse_comp_test_set.csv`，并调用被测模型与 grader 的 API。论文要求的“浏览互联网”不在这个脚本里实现。
- GPU: 未见。
- K8s: 未见。
- 多容器: 未见。

## 评分

要另外的 judge 模型，不是确定性字符串相等。`browsecomp_eval.py` 用 grader 模板让模型回答 `correct: yes|no`。`simple_evals.py` 在 `case "browsecomp"` 传入 `grading_sampler`，该 sampler 写死为 `gpt-4.1-2025-04-14`（`ChatCompletionSampler`，`max_tokens=2048`）。

## agent / runtime

官方参考实现没有浏览器或 agent 循环。`BrowseCompEval.__call__` 把解密后的题目填进单轮 `QUERY_TEMPLATE`，交给 `SamplerBase`（仓库里是 OpenAI / Claude 等 API sampler）。被测模型若自行浏览，运行时不在本仓，记 unknown。

## 体积与是否入 git

- 上游仓约 110 KB，本目录不整仓复制。
- 公开 CSV 实测 1,196,283 字节，1,266 行，列名为 `problem`、`answer`、`problem_topic`、`canary`。`Last-Modified: Thu, 10 Apr 2025 18:07:43 GMT`。单元格是用该行 `canary` 做 XOR 的密文，明文未落盘。
- 本目录只有短摘录，可以进 git。CSV、解密明文、论文中的例题不要进 git。论文要求不要以明文或图片公开例题。

## 未抓取项与原因

- 入口页 HTML: `WebFetch` 超时；直接请求返回 Cloudflare 403（`cf-mitigated: challenge`）。内容改由 arXiv HTML、simple-evals README 和该页的检索摘要核对，三处都指向同一 GitHub 仓。
- 未保存 CSV 或任何解密后的题面/答案，避免泄漏。
- 未克隆仓库到 `/workspace`。摘录来自该 SHA 的 raw 文件。

MANIFEST-END
