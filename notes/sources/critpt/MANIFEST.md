# critpt

- slug: `critpt`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://critpt.com/

## 官方仓

- 代码仓有。https://github.com/CritPt-Benchmark/CritPt
- 默认分支 `main` HEAD: `17c2545c302762d2f2d644d923ea4c301605cb08`
- 核实: `git ls-remote` HEAD 与 commits API 一致。commit 日期 2025-11-21T19:04:06Z，message 为 “Fixed hyper link formatting in README.md”。
- GitHub `size` 字段 264 KB。该 SHA 的 tree 未截断，blob 合计 928,543 字节。浅克隆到 `/tmp` 后已删除，没有留在 `/workspace`。许可证字段为空；HF 卡片写 apache-2.0。
- 组织下另一个仓 https://github.com/CritPt-Benchmark/CritPt-Benchmark.github.io 是网站，HEAD `792275d0c7bcb9611ee637eaaefacd19b889a4c2`（2026-06-22），GitHub `size` 5,078 KB。没有克隆。
- HF 卡片写的评测仓 https://github.com/CritPt-Benchmark/CritPt_Eval 本次 API 返回 404。公开评测代码就在 `CritPt` 这个仓里。

## 论文 / blog / HF

- 论文: arXiv [2509.26574](https://arxiv.org/abs/2509.26574)。abs 页写提交 2025-09-30（v1），最后修订 2026-05-08（当前 v4）。
- 网站: https://critpt.com/ 。站点文案与论文一致：71 个复合挑战、190 个 checkpoint，答案按设计可机器核验。
- HF: [CritPt-Benchmark/CritPt](https://huggingface.co/datasets/CritPt-Benchmark/CritPt)。API `sha` `9b9fc8498596ec08ab5437a72f4aa18beef2b876`（2025-11-21，message “Update README.md”）。train split 70 例，`download_size` 161,246，`dataset_size` 307,246。parquet 为 `data/train-00000-of-00001.parquet`，161,246 字节。
- 没有单独的 blog id。榜单由 Artificial Analysis 继续记，站点与 README 都这么写。

## 测什么

用物理研究者新写的、未发表的研究级题目测 LLM 推理：71 个入门研究规模的复合挑战，并拆成 190 个 checkpoint。出处: arXiv 2509.26574 摘要，以及 https://critpt.com/ 首页同一组数字。

## 环境线索

- 容器: 公开生成代码没有 Dockerfile 或 compose。`critpt_generate.py` 把 inspect-ai 的 `sandbox` 设为 `"local"`。
- 出网: 生成要模型 API key。配置可打开 `use_web_search`。评分客户端默认 POST 到 `https://artificialanalysis.ai/api/v2/critpt/evaluate`。
- GPU: 未见。记 unknown。
- K8s: 未见。记 unknown。
- 多容器: 未见。记 unknown。

## 评分

论文写的是确定性脚本，不是另调一个 judge 模型。答案先收成代码块，再用自定义脚本比较数值、SymPy 表达式和带测试用例的 Python 函数，并使用专家给的容差和等价形式。这篇论文明确把该流程和 LLM judge 分开。

实现不在公开仓。公开仓的 inspect scorer 只保存生成结果；正式分数要提交私有 grading server。AA 文档写该接口需要获批的 `x-api-key`，默认 24 小时 10 次，一次请求必须带齐公开集的全部题，成功响应只给 `accuracy`、`timeout_rate`、`server_timeout_count`、`judge_error_count`。文档把 `judge_error_count` 解释成评分进程失败，不是另一个评判模型的名字。服务器里的脚本本次看不到。

## agent / runtime

有生成侧证据，没有容器 agent。`python -m critpt generate` 走 inspect-ai。默认配置 `multiturn_without_answer_without_tool.json` 关闭 python 和 web search；另两份配置分别打开 python，或同时打开 python 与 web search。工具是 inspect-ai 的 `bash`、`python`、`web_search`。`requirements.txt` 含 `inspect-ai>=0.3.0`、`sympy`、`fastapi`，文件头注释写 “For evaluation server”，但该 commit 没有服务器实现。主指标在 README 里是 5 次运行 × 70 道测试挑战的平均准确率。

## 体积与是否入 git

- 代码仓约 0.9 MB。按本任务只留摘录，没有把克隆留在 `/workspace`，也不把全仓抄进本目录。
- HF parquet 161,246 字节，含答案字段，没有下载。
- 网站仓 GitHub size 5,078 KB，没有克隆。
- 本目录的 MANIFEST 和 `excerpt-scoring.txt` 可以进 git。

## 未抓取项与原因

- 私有 grading 的服务器源码不在公开仓，也没有凭据，没有提交评测。
- `CritPt_Eval` 404。
- 未下载 HF parquet，未把 70 道公开挑战或示例答案抄进本目录。
- 网站仓超过 5 MB 的 GitHub size，未克隆；首页文字来自 https://critpt.com/ 的抓取，不是来自整仓。

MANIFEST-END
