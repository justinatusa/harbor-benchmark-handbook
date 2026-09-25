# MANIFEST

- slug: video-mme
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://github.com/MME-Benchmarks/Video-MME

## 官方仓

- 核实到的官方仓: https://github.com/MME-Benchmarks/Video-MME
- `https://github.com/BradyFU/Video-MME` 的 API 返回同一仓库（full_name 为 `MME-Benchmarks/Video-MME`）
- 默认分支: main
- commit SHA: 06c2315b892f88578f81d73205d07cf576f292b9
- commit 说明: Update README.md
- committer 日期: 2025-12-08T06:31:54Z
- 远程 tags: 没有
- GitHub API `size`: 17595 KB；树 blob 合计 13,267,794 字节，15 个对象，`truncated=false`
- 树内容: `README.md`、`asset/` 图片、`evaluation/output_test_template.json`。没有 Dockerfile，没有评测 Python

## 论文 / blog / HF

- 论文: https://arxiv.org/abs/2405.21075 （CVPR 2025；README 同时给了 PDF 链接 https://arxiv.org/pdf/2405.21075）
- 项目页: https://video-mme.github.io/
- 榜: https://video-mme.github.io/home_page.html#leaderboard
- 数据集: README 写 https://huggingface.co/datasets/lmms-lab/Video-MME
- 2026-09-24 请求该 HF URL 得到 HTTP 307，Location 为 `/datasets/lmms-eval/Video-MME`
- HF id: `lmms-eval/Video-MME`
- HF 修订: ead1408f75b618502df9a1d8e0950166bf0a2a0b
- HF `lastModified`: 2024-07-04T08:14:20.000Z
- 评测脚本不在官方仓内。README 指向 https://github.com/thanku-all/parse_answer/blob/main/eval_your_results.py
- 该脚本仓 HEAD: afd52cfe3dde5b3685e0d4f760c10c756860c758（Update eval_your_results.py，2024-06-23T04:04:25Z）

## 测什么

测多模态模型看视频答题的准确率：900 个视频、2700 道人工标注的四选一题，时长从 11 秒到 1 小时，可带字幕。出处：官方 README「Video-MME Overview」，以及 arXiv:2405.21075 摘要。

## 环境线索

- 容器: 官方仓没有 Dockerfile 或镜像名。unknown。
- 出网: 计分脚本只读本地 JSON。取数要下 HF 上的视频 zip。官方仓没有沙箱出网政策。unknown。
- GPU: 官方仓和 README 的评测步骤没有写 GPU。unknown。
- K8s: 没看到。unknown。
- 多容器: 没看到。unknown。
- README 另建议可用 VLMEvalKit（https://github.com/open-compass/VLMEvalKit）或 LMMs-Eval（https://github.com/EvolvingLMMs-Lab/lmms-eval）。这两个仓本次没有打开。

## 评分

确定性。官方 README 写：把模型回答放进 JSON 后用评测脚本算准确率，「The evaluation does not introduce any third-party models, such as ChatGPT.」`eval_your_results.py` 用正则从回答里抽出选项字母，与标注 `answer` 做字符串相等，再按时长、领域、题型汇总准确率。没有 judge 模型。抽不出字母就算不正确。

## agent / runtime

官方仓、README 和论文摘要都没有代理轨迹、工具协议或运行时。题型是视频多选题。agent 线索：unknown。可选的 VLMEvalKit / LMMs-Eval 只在 README 里被点名为现成评测工具，本次没有核对它们的运行时。

## 体积与是否入 git

官方 git 主要是 README 和结果图，GitHub 统计约 17595 KB，大于 5MB，没有克隆进 `/workspace`。视频不在这个 git 里。HF 树 24 个文件、合计 101,001,829,951 字节（约 101GB），最大的是 `videos_chunked_*.zip`（单包约 5.1–5.3GB）。这些 zip 没有下载。本目录只留本文件和一个小于 200KB 的计分摘录，本次没有 git commit。

## 未抓取项与原因

- HF 视频 zip、字幕 zip、parquet：约 101GB，超过工作区克隆上限。
- 官方 git 里的结果图：非文本，且整仓大于 5MB。
- VLMEvalKit 与 LMMs-Eval 的实现：README 只是可选入口，没有当作本 benchmark 的官方仓打开。
- 没有跑 `eval_your_results.py`。

MANIFEST-END
