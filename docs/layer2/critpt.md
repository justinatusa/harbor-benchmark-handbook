# CritPt

论文写答案可以用脚本核验。公开仓算不出正式分，分在私有评分服务上。

## 测什么

用物理研究者新写的、尚未发表的研究级题目测模型推理。站点与论文写 71 个复合挑战、190 个检查点。Hugging Face 的 train split 是 70 例。

## 官方源

站点 https://critpt.com/ 。论文 https://arxiv.org/abs/2509.26574 。代码仓 https://github.com/CritPt-Benchmark/CritPt ，commit `17c2545c302762d2f2d644d923ea4c301605cb08`（2025-11-21）。Hugging Face（HF）数据集 https://huggingface.co/datasets/CritPt-Benchmark/CritPt ，修订 `9b9fc8498596ec08ab5437a72f4aa18beef2b876`。评测仓 `CritPt_Eval` 本次返回 404。

## 形态

dataset、verifier、agent。生成走 inspect-ai。没有 `task.toml` 或 `dataset.toml`，没有 Dockerfile，没有 adapter。

## 与 Harbor 距离

暂不宜接。正式评分脚本不在公开仓。分数要交给私有评分服务。

## 环境

`critpt_generate.py` 把 inspect-ai 的 sandbox 设为 `local`。没有看到容器、Kubernetes 或图形桌面。生成要模型接口密钥。配置可以打开网页搜索。评分客户端默认把结果发到 `https://artificialanalysis.ai/api/v2/critpt/evaluate`。图形处理器（GPU）没有写，记 unknown。

## 评分

论文写由脚本比较数值、SymPy 表达式和带测试的 Python 函数，并使用专家给的容差。公开仓的 inspect scorer 只保存生成结果。正式分数要提交私有评分服务。该接口要获批的密钥。成功时只返回准确率、超时比例和若干计数。文档里的 `judge_error_count` 指评分进程失败。服务里的脚本看不到。

## agent / runtime

`python -m critpt generate` 走 inspect-ai。默认配置关掉 Python 和网页搜索。另两份配置分别打开 Python，或同时打开 Python 与网页搜索。工具是 inspect-ai 的 `bash`、`python`、`web_search`。主指标是 5 次运行、70 道测试挑战的平均准确率。没有放在容器里的 agent。

## 迁入代价

高。公开材料没有可运行的 verifier。正式分在私有服务上，还要获批密钥。

## 对抽象的压力

压在 verifier。公开流程只留下生成结果。reward 要等私有服务返回。本地没有可放进 Harbor `tests/test.sh` 的评分脚本。

## 本地摘录

见 [`notes/sources/critpt/MANIFEST.md`](../../notes/sources/critpt/MANIFEST.md)。
