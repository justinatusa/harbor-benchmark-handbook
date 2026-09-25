# osworld-2-0

- slug: `osworld-2-0`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://osworld-v2.xlang.ai/

## 官方仓

有，而且不是 OSWorld-Verified 那个仓。

- 代码: https://github.com/xlang-ai/OSWorld-V2 。抓取时 `main` HEAD 与推荐 tag `osworld-v2.1` 都指向 `3d778a3c9a34a079316f70df023b166700445792`（2026-09-16T17:37:44Z，`docs: update README for osworld-v2.1 benchmark release and upgrade instructions`）。Apache-2.0。GitHub `size` 字段 87273（KB）。
- 同一次提交里的 `benchmark_releases/osworld-v2.1.json` 把 `osworld_code.base_commit` 写成 `325ab352e2ff7410854bf8e3324c391bc60e7526`（2026-09-16T16:43:02Z）。GitHub compare：`325ab352...3d778a3c` 状态 `ahead`，超前 2 个提交（`ce80e4ffbd25` 加入 release manifest，`3d778a3c9a34` 改 README）。tag 名是 `osworld-v2.1`，manifest 里的 `base_commit` 没有跟着 tag 尖端走。可比运行应同时记下 tag SHA 和 manifest 里的 `base_commit`。
- 更早的 tag：`v2026.08.08` = `d578d2d4e0dc82b43e270fdaa7fa89d9708cd154`；`v2026.06.24` = `2b9b7b4eb73243d557bdbf2998fe18d8e18e19c6`。
- 自托管网站: https://github.com/Task-Web/OSWorld-web ，tag `osworld-v2.1` = `60c89fe6a8ed934668619d8d26132848239eb8ee`。与 manifest 的 `website_code.commit` 一致。GitHub `size` 字段 76（KB）。
- 任务类: HF `xlangai/osworld_v2_tasks`，tag `osworld-v2.1`，commit `0a1aadad95aa79b00b3783e717d865089ab06e26`。`gated: auto`。manifest 写 108 个 task hash。
- 完整资产: HF `xlangai/osworld_v2_assets_gated`，commit `384b3834faba5700a7b589e6cc181490c9808949`。`gated: auto`。tree 列表 1084 个文件。公开的 `xlangai/osworld_v2_assets` 被 README 写成不完整的运行时镜像，不能代替 gated 快照。

`xlang-ai/OSWorld`（抓取时 HEAD `b138d348256078fa634fc3b73567a7337c793e6b`）是 OSWorld 1.0 / OSWorld-Verified 那条产品线。论文正文把 Claude Opus 4.8 在 OSWorld-Verified 上的 83.5% 当作短任务对照。本 slug 的官方代码入口是 OSWorld-V2。

## 论文 / blog / HF

- 论文: arXiv:2606.29537（https://arxiv.org/abs/2606.29537）。抓取的是 arXiv HTML。项目页 bib 同号。
- 项目页: https://osworld-v2.xlang.ai/
- 轨迹查看: https://osworld-v2-monitor.xlang.ai/ （README 链接，本次未打开）
- 轨迹数据: HF `xlangai/osworld2.0-trajectory`，sha `fff9740b1d1a9eac03831c109ad668a001f8485a`，`gated: auto`。tree API 返回被截在 100000 个文件名前，未下。

## 一句话测什么

测电脑使用 agent 能不能做完长程、跨应用的真实工作流：108 条任务，熟练使用者中位约 1.6 小时，主指标是 500 步预算下的二元完成，同时用平均 27.25 个检查点给部分分。（项目页与 arXiv:2606.29537 摘要、第 2.1.3 节）

## 环境线索

- 容器: 有桌面 VM。`osworld-v2.1.json` 的 Docker 项：运行镜像 `happysixd/osworld-docker@sha256:0e6497a9295647cf05bf2b2af522fdd79bdeba2737595259cab310a3bcf6baa9`；磁盘制品 `xlangai/v2-image` 的 `osworld-v2-ubuntu-x86.qcow2.zip`，`artifact_size` 14,891,811,084 bytes，sha256 `14b08aa7ba6c023ecb91d46de8df5de32af4d1d6bd75ea925519caf9677fc8b3`。AWS：`us-east-1`、`1920x1080`、AMI `ami-01017272139e01feb`。manifest 的 verification 写 Docker 归档已核对，但 “VM boot remains blocked by absent KVM”，所以这份 manifest 没有声称 Docker 客机已经启动。
- 出网: 要网络，但是否访问真实第三方网站取决于部署。任务网站应自托管并设置 `WEBSITE_HOST_SUFFIX`。`osworld-v2-2026.08.08` 的托管后缀是 `site.hku.icu`；`2026.06.24` 的 `web.hku.icu` 已停。README 写部分任务要代理，缺代理会拉低分。GitLab 题要自建并设置 `GITLAB_URL` 与 `GITLAB_PRIVATE_TOKEN`（只记变量名，不记任何令牌值）。
- GPU: provider 清单写的是 KVM / AMI / 磁盘镜像，没有把 GPU 写成评测条件。记 unknown。
- K8s: README、release manifest、已读论文段落都没有 Kubernetes。unknown。
- 多容器: 有。论文写 OSWorld-web 每个应用一个容器，带 `web-compose.yml`，Caddy 按域名反代，应用共享一个 Docker network；评测时再起应用容器。这是桌面 VM 之外的第二组容器。manifest 还写网站源码含 25 个钉死的 submodule。

## 评分

混合。主路径是对最终环境状态和产物做功能检查，这部分是程序判定。论文第 2.1.3 节写 model-based evaluation 占总分 11.53%，单题不超过 50%，judge prompt 要在标注对错状态上验证后才收。附录 E.1 的校验表列出 GPT-5.4 medium、GPT-5.4 xhigh、Claude Opus 4.6、Claude Sonnet 4.6。已读 HTML 没有写死线上默认用哪一个 judge。所以不能当成纯确定性分数，要另备 judge 模型，但 judge 只覆盖少数检查点。

主报告指标仍是 500 步二元完成；部分分是检查点均值。

## agent / runtime

README 的评测入口是宿主机上的 `scripts/python/run_multienv_*.py` 和 `mm_agents`，观察类型示例是 screenshot。论文第 3 节写 Claude 走 `claude_computer_use`，其他模型发动作。环境是 Desktop VM。公开榜要求把 agent 实现交给维护者在他们那边跑（README “Public Evaluation”）。本次没有逐行读 `run_multienv.py`，进程边界以上述 README 分层为准：agent 代码在宿主机，题目环境在 VM。

## 体积与是否入 git

- OSWorld-V2 仓约 85 MiB（GitHub size 87273 KB），未克隆。
- qcow2 zip 14,891,811,084 bytes，未下载。
- gated 任务与 1084 个资产文件未下载。
- 轨迹集未下载。
- 入 git: 本目录只留本文件和 `excerpt.md`。代码仓、镜像、任务、资产、轨迹都不放进工作区。

## 未抓取项与原因

- 全仓、qcow2、gated task class、gated assets：体积或门禁，且镜像远超 5MB。
- `osworld-v2-monitor.xlang.ai` 与轨迹 zip：未打开、未下。
- 线上默认 judge 模型名：附录 E.1 只看到校验过的模型表，没看到唯一默认值。
- manifest 自己写了限制：没有跑满 108 题；Docker 客机未启动；Task029 未改版本有 120 秒 HTTP setup 超时，修复未进这个 release。这些是官方 verification 原文，本次没有复验。
- VM FAQ 公开了共享评测账号。本文件不抄口令。

MANIFEST-END
