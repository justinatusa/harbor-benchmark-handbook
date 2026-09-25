# Video-MME

官方仓里没有计分脚本，也没有容器。评测步骤没写 GPU，不能据此当成已经确认不要显卡。

1. 一句话测什么。测多模态模型看视频做四选一的准确率：900 个视频、2700 道人工标注题，时长从 11 秒到 1 小时，可带字幕。出处是该仓 README 的 “Video-MME Overview”，以及 https://arxiv.org/abs/2405.21075 摘要。

2. 官方源。仓库 https://github.com/MME-Benchmarks/Video-MME ，commit `06c2315b892f88578f81d73205d07cf576f292b9`（2025-12-08，说明 “Update README.md”）。论文 https://arxiv.org/abs/2405.21075 。项目页 https://video-mme.github.io/ 。数据集现地址 https://huggingface.co/datasets/lmms-eval/Video-MME ，修订 `ead1408f75b618502df9a1d8e0950166bf0a2a0b`。计分脚本在 https://github.com/thanku-all/parse_answer ，HEAD `afd52cfe3dde5b3685e0d4f760c10c756860c758`。

3. 形态。`dataset`、`verifier`。清单没写 `environment`、`agent` 或 `adapter`。

4. 与 Harbor 距离。unknown。题和计分脚本公开，计分不另调模型。清单没有给出 `task.toml` 或 `dataset.toml`。缺一句评测不要 GPU，证据不够放进其余四档。

5. 环境。官方仓没有 Dockerfile 或镜像名。计分脚本只读本地结果文件。视频要另下 Hugging Face 上的压缩包，合计约 101GB。出网政策、GPU、Kubernetes、多容器都是 unknown。README 还点了 VLMEvalKit 和 LMMs-Eval，清单没有打开那两个仓。

6. 评分。不另调模型。README 写评测不引入 ChatGPT 这类第三方模型。`eval_your_results.py` 用正则抽出选项字母，和标注 `answer` 做字符串相等，再按时长、领域、题型汇总准确率。抽不出字母就算错。

7. agent/runtime。官方仓、README 和论文摘要都没有代理轨迹、工具协议或运行时。agent 是 unknown。

8. 迁入代价。高。计分是一个本地脚本，视频却约 101GB，而且不在官方 git 里。没有现成的 task 目录或容器，要自己做 `environment`，再把抽字母的脚本接到 `verifier`。

9. 对抽象的压力。缺一句评测不要 GPU。压力在 `dataset` 和 `verifier`。题面是视频包加选择题，计分在仓外脚本里抽字母。`agent` 和 `environment` 没有材料。

10. MANIFEST 路径。`notes/sources/video-mme/MANIFEST.md`
