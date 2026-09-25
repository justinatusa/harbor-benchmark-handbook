# osworld-2-0 摘录

抓取日 2026-09-24 Asia/Shanghai。产品入口是 OSWorld-V2，不是 `xlang-ai/OSWorld`。

项目页 https://osworld-v2.xlang.ai/ ：

> 108 Long-horizon tasks … 31 Self-hosted websites … 69.6% Tasks >1h … >250 Average agent steps … 27.25 Avg. scoring checkpoints
>
> Under our primary binary-completion metric at 500 steps, Claude Opus 4.8 … completes only 20.6% of tasks at a 54.8% partial score

论文 https://arxiv.org/abs/2606.29537 第 2.1.3 节：

> Overall, model-based evaluation contributes 11.53% of the total score, and no task relies on it for more than 50%.

论文环境段（arXiv HTML，OSWorld-web）：

> Each application exposes its web service on an internal port and provides a web-compose.yml file. A Caddy reverse proxy routes domain names … while all applications share the same Docker network.

`benchmark_releases/osworld-v2.1.json`（位于 tag `osworld-v2.1` = `3d778a3c9a34a079316f70df023b166700445792`）摘句：

> osworld_code.base_commit = 325ab352e2ff7410854bf8e3324c391bc60e7526
> website_code.commit = 60c89fe6a8ed934668619d8d26132848239eb8ee
> tasks.commit = 0a1aadad95aa79b00b3783e717d865089ab06e26
> assets.commit = 384b3834faba5700a7b589e6cc181490c9808949
> docker artifact_size = 14891811084
> docker runtime_image = happysixd/osworld-docker@sha256:0e6497a9295647cf05bf2b2af522fdd79bdeba2737595259cab310a3bcf6baa9
> aws ami_id = ami-01017272139e01feb
> verification.docker: VM boot remains blocked by absent KVM.
