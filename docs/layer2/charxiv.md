# CharXiv

公开 JSON 里 val 有答案，test 的 `answer` 全是 null。README 写内部端到端评测应使用 val。

1. 一句话测什么。测多模态模型对科学论文图表的理解，分描述题和推理题。出处是 commit `7ebe88f78dee387691551f071abcb2b9e1a8025b` 的 README Introduction：2323 张来自科学论文的图。浅克隆里描述和推理的 val 各 1000 条，test 各 1323 条。README 另写实际 2333 张图且编号不连续，清单没有逐张核对这两套数字是不是同一批。

2. 官方源。仓库 https://github.com/princeton-nlp/CharXiv ，commit `7ebe88f78dee387691551f071abcb2b9e1a8025b`（2025-04-22，说明 “Merge pull request #14 from qzyou/patch-1”）。论文 https://arxiv.org/abs/2406.18521 。项目页 https://charxiv.github.io/ 。数据集 https://huggingface.co/datasets/princeton-nlp/CharXiv ，修订 `f441eb632fc62f6f777830a0f47619e6e86459b0`。

3. 形态。`dataset`、`verifier`。生成入口是单张图加一道题。公开材料没有 environment、agent 或 adapter。

4. 与 Harbor 距离。重改造。`src/descriptive_utils.py` 与 `src/reasoning_utils.py` 把打分模型固定为 `gpt-4o-2024-05-13`。清单没有给出 `task.toml` 或 `dataset.toml`。

5. 环境。该 commit 没有 Dockerfile、compose 或镜像名。打分要调用 OpenAI，`evaluate.sh` 和 `src/evaluate.py` 要密钥参数。图片在 Hugging Face 的 `images.zip`，约 141MB，不在 git 里。打分脚本不用 GPU。`src/generate_lib/` 里部分本地模型把权重放到 CUDA，可占多卡。走云端模型时不要求本机 GPU。Kubernetes 和多容器是 unknown。

6. 评分。要另调模型。`src/evaluate.py` 用 OpenAI 客户端给描述题和推理题打分。描述题调用使用 `temperature=0`、`top_p=1`、`seed=42`、`response_format=json_object`。`evaluate.sh` 注释写用 GPT-4o 打分。

7. agent/runtime。没有代理框架、工具循环或独立 runtime 进程。`src/generate.py` 对每道题调用用户实现的 `generate_response`。云端模型要另写 `get_client_model`。

8. 迁入代价。中。val 的题面和答案、打分脚本都在公开仓库里。要做的是把固定的 GPT-4o 打分接进 `verifier`，并把 `images.zip` 放进环境。test 答案是 null。清单没有给出 Harbor 的 task 目录。

9. 对抽象的压力。`verifier` 绑在 `gpt-4o-2024-05-13` 上。`dataset` 的图不在 git commit 里，test 答案是 null。现有生成入口是一次 `generate_response`，没有代理循环可以接到 `agent`。

10. 本地摘录。[`notes/sources/charxiv/MANIFEST.md`](../../notes/sources/charxiv/MANIFEST.md)。
