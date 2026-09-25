来源：
- https://github.com/facebookresearch/ProgramBench/blob/b08d8621031f5f5abc4d3ffc2950256c83fbfe42/docs/README.md
- arXiv:2605.03546 HTML（2026-09-24 抓取）

docs/README.md:
  Docker Hub 镜像只构建 linux/amd64。
  推理镜像 tag：task_cleanroom_v6，组织 programbench。
  The agent MUST NOT have access to internet during inference.
  评测会拉取例如 ffmpeg_1776_ffmpeg.360a402:task_v6。
  测试 blob 按需从 Hugging Face 下载。
  论文里非确定性或有缺陷的分支/单测会被忽略，看 tests.json；最终分用 programbench info。

论文实验配置（摘要附近与 agent scaffold 段）:
  推理容器无互联网。
  mini-SWE-agent；每题容器 20 CPU、60GB RAM；1000 steps、6 小时。
  主指标 % Resolved：该题全部测试通过，且没有被标为作弊。
  另报 % Tests Passed。
  给互联网的消融实验才用 9 个 LM judge 做作弊多数票，不是默认功能分。
