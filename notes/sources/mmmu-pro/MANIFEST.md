# mmmu-pro

- slug: `mmmu-pro`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://huggingface.co/datasets/MMMU/MMMU_Pro

## 官方仓

有评测代码仓，数据集不在 git 里。

- 代码: https://github.com/MMMU-Benchmark/MMMU ，默认分支 `main`，抓取时 HEAD `268471d0d488258990025331c7528359c324aa25`（2026-07-28T02:29:25Z，`Merge pull request #86 from Yunnglin/evalscope-mmmu-docs-20260728-102038`）。Apache-2.0。GitHub `size` 字段 195094（KB）。MMMU-Pro 的推理与评分在子目录 `mmmu-pro/`，README 指向 `evaluate.py`。
- 这个仓同时装 MMMU 本体和 MMMU-Pro。MMMU-Pro 的数据入口是下面的 HF 数据集，不是仓内的图片副本。

## 论文 / blog / HF

- 论文: arXiv:2409.02813（https://arxiv.org/abs/2409.02813），题名 MMMU-Pro: A More Robust Multi-discipline Multimodal Understanding Benchmark。抓取的是 arXiv HTML。
- HF: `MMMU/MMMU_Pro`。数据集仓 sha `563f3e84bb3b90893083a1f039cfa13077f2302b`。`gated: false`。card license `apache-2.0`。三个 config 都是 `test`：`standard (10 options)` 1730 行，`standard (4 options)` 1730 行，`vision` 1730 行。datasets-server 合计 `num_rows` 5190。
- 项目站: https://mmmu-benchmark.github.io/ 。2026-09-24 打开返回 200，标题仍是 MMMU 本体，导航里有 MMMU-Pro。未另存 Pro 子页。
- 数据集卡引用同一篇 arXiv，并给出 `load_dataset("MMMU/MMMU_Pro", "vision" | "standard (4 options)" | "standard (10 options)")`。

## 一句话测什么

测多模态模型是不是真的要同时看图和读题：从 MMMU 里去掉纯文本模型就能答对的题，把选项扩到最多 10 个，并增加一套题目嵌在截图或照片里的 vision-only 输入；论文把总分定义成 10 选项设置与 vision 设置的平均。（arXiv:2409.02813 摘要与第 3.1 节；HF 数据集卡 “Increased Complexity”）

## 环境线索

- 容器: `mmmu-pro/README.md` 是 `python infer/infer_xxx.py` 与 `python evaluate.py`，未见 Dockerfile。unknown。
- 出网: 下载 HF parquet 和调用闭源模型 API 时要。题目本身是本地图文，不再访问别的网站。
- GPU: 本地开源 VLM 推理通常要，仓的 README 没把 GPU 型号写成评测条件。走 API 则不要本地 GPU。记 unknown。
- K8s: 未见。unknown。
- 多容器: 未见。unknown。

## 评分

确定性核对，不另调 judge 模型。`mmmu-pro/evaluate.py`（钉在上述 commit）的 `eval_multi_choice` 写明 “only they are exactly the same, we consider it as correct”，比较的是解析后的选项字母和金标。`evaluate_mmmu` 里的 `judge_dict` 只是 Correct/Wrong 字典，不是 LLM judge。

解析不是纯规则到底：`parse_multi_choice_response` 在几种括号和 “Answer:” 匹配都失败时，会 `random.choice(all_choices)`。所以分数可复现性依赖随机种子，但失败兜底不是另一个模型。

论文第 3.1 节写 MMMU-Pro 总分是设置 (2) 10 选项与设置 (3) vision 的平均；4 选项设置只作对照。HF 三个 split 都在，各 1730 行。

## agent / runtime

官方路径是单轮多模态推理脚本：`infer_xxx.py` 接收模型名、`cot` 或 `direct`、以及 `standard(10 options)` / `standard(4 options)` / `vision`。runtime 是跑这个脚本的 Python 进程，一次调用模型，没有多步工具循环。

## 体积与是否入 git

- 代码仓约 190.5 MiB（GitHub size 195094 KB），未克隆。单独拉了 `mmmu-pro/evaluate.py`，16,621 bytes，只在摘录里留评分函数说明。
- HF 文件树合计 2,988,188,497 bytes（约 2849.76 MiB），11 个文件，与 datasets-server 的 `num_bytes_parquet_files` 2,988,175,948 同量级。最大的 vision parquet 单文件约 441 MiB。
- 入 git: 本目录只留本文件和 `excerpt.md`。仓与 parquet 都不放进工作区。

## 未抓取项与原因

- 全仓与全部 parquet：都超过 5MB。
- 项目站只确认了首页标题和 MMMU-Pro 导航，未存 HTML。
- 未跑 `evaluate.py`，未抽查 parquet 行数以外的图片字节（行数来自 datasets-server）。
- 第三方套件（例如 VLMEvalKit 对 MMMU-Pro 解析的修复提交）不是本官方仓，未当作评分实现。

MANIFEST-END
