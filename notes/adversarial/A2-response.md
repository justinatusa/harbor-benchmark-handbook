# A2 回应

## A2-01

处理：不接受

`docs/conversion-playbook.md` 这一句是停手规则：上游是 pytest 时由评分脚本跑用例，但本轮打开的清单没有点名某份 pytest 文件，不要另编文件名。`nl2repo-bench` 的登记距离仍是 `unknown`。补一个 `test_*.py` 会违反同一句。

## A2-02

处理：接受

改了 `docs/conversion-playbook.md` 文首。原句「每节都要交出 Harbor 的 task 目录：`instruction.md`、`environment/`、`tests/test.sh`（Windows 用 `tests/test.bat`）。」改为：任务不公开或 gated 的节不要求 `tests/test.sh`，也不要求 `tests/test.bat`。其余节仍要求评分脚本最后要写出 reward 文件。Harbor 0.23.0 笔记写的是 `test.sh` 或 `test.bat`，没有把 `test.sh` 写成唯一文件名。

## A2-03

处理：不接受

核对句已经写「卡没有挂上时，记失败，不要把 CPU 跑通当成 GPU 已接」。坑写哪个 `environment.type` 会把 `gpus` 传进容器，安装包笔记没写，不要在 docker、podman 到 kata 里猜。补一条启动命令就是在猜 type。

## A2-04

处理：记入 conflicts

说法一：漏写会进默认 docker，没有 H100。来源：`docs/conversion-playbook.md`「要 GPU」的坑。

说法二：8 题缺 `gpus`，不能从缺键推出运行时默认值。来源：`docs/layer2/terminal-bench-4-0.md`。核对句「不需要显卡的题，`gpus` 没有被填上」不是「缺键等于不需要显卡」。`notes/rounds/r1-package-map.md` 里默认 docker 写的是 `environment.type` 两边都空，不是缺 `gpus`。

已追加到 `docs/conflicts.md`。不把这 8 题标成不需要显卡，也不选一个运行时默认。

## A2-05

处理：不接受

`cli/adapter_review.py` 的笔记把 judge 写成 `tests/` 里的 prompt、模型名、rubric，没有三个文件名，也没有密钥路径或变量名。核对已经写不提供密钥时脚本失败退出、reward 文件不出现。补文件名或启动命令是另编。

## A2-06

处理：不接受

第 4 步已经写「写不出就停」。坑写两份 R1 笔记都没有 agent 进哪个 service 的规则。核对写指不出就不要标成已经接上。`spreadsheetbench` 点名的是两个 Dockerfile，没有 service 名。同节写不要凭记忆补 service 名。

## A2-07

处理：接受

改了 `docs/conversion-playbook.md` 第六节。原句「在转化记录里写暂不宜接。」改为「在 `docs/registry.md` 该行的「与 Harbor 距离」写暂不宜接。」原句「记录的状态是暂不宜接。」改为「`docs/registry.md` 该行的「与 Harbor 距离」是暂不宜接。」

## A2-08

处理：不接受

登记和 `docs/layer2/terminal-bench-2-1.md` 都是原生可接。介绍卡已经写没有 git tag、commit 是抓取日的 `main`，并写两题当前树没有 `docker-compose.yaml`、多容器形态 unknown。89 个 `task.toml` 与 README 的 `harbor run` 仍在。清单没有把任务文件的 Harbor 钉在 0.23.0 以外的版本。不把这一行降档。

## A2-09

处理：不接受

登记压力列已经写多数题要 GPU，且 `task.toml` 允许出网。清单写 bundles 在 Harbor 0.6.6 和 0.22.0 上跑过，Modal 路径要求 Harbor ≥ 0.22。这不是把任务文件钉死成必须安装某一个旧版本。没有介绍卡与登记距离不一致。不把这一行从原生可接改掉。

## A2-10

处理：接受

`notes/sources/swe-atlas/MANIFEST.md` 写没有 git tag，README 要求安装 Harbor `v0.18.0`。两边都写成重改造，不升成原生可接。

改了 `docs/registry.md` 的 `swe-atlas` 行：距离由「原生可接」改为「重改造」，压力列写上「任务文件的 Harbor 版本不是 0.23.0。」

改了 `docs/layer2/swe-atlas.md` 第 4 节：距离保持「重改造」，补上「任务文件的 Harbor 版本是 v0.18.0，不是 0.23.0。没有 git tag。」

## A2-11

处理：接受

`officeqa-pro` 登记和 `docs/layer2/officeqa-pro.md` 都是暂不宜接。不改。

`agents-last-exam` 改了 `docs/layer2/agents-last-exam.md` 第 4 节。原句「与 Harbor 距离。重改造。」改为「与 Harbor 距离。暂不宜接。本地数据包 gated，约 202 GiB，要先申请。」登记本来就是暂不宜接。

## A2-12

处理：接受

改了 `docs/layer2/hle.md` 第 4 节。原句「与 Harbor 距离。重改造。」改为「与 Harbor 距离。暂不宜接。题目 gated，不能放进可再分发的 task 目录。」同卡第 8 节「迁入代价。中。」改为「迁入代价。高。」登记本来就是暂不宜接，迁入代价是高。

## A2-13

处理：接受

改了 `docs/layer2/osworld-2-0.md` 第 4 节。原句「与 Harbor 距离。重改造。」改为「与 Harbor 距离。暂不宜接。任务类和完整资产 gated。」登记本来就是暂不宜接。`notes/sources/osworld-2-0/MANIFEST.md` 写任务类与完整资产都是 `gated: auto`，且未下载。

## A2-14

处理：接受

登记本来就是轻适配，不是原生可接。`notes/sources/deepswe-v1-1/MANIFEST.md` 写没有名为 `v1.1` 的 tag，读的是 `main`。

改了 `docs/layer2/deepswe-v1-1.md` 第 4 节。原句「与 Harbor 距离。原生可接。」改为「与 Harbor 距离。轻适配。没有 v1.1 tag，main 上的 task.toml 不能当成 v1.1。」

改了 `docs/registry.md` 的 `deepswe-v1-1` 压力列，写上「没有 v1.1 tag，main 上的 task.toml 不能当成 v1.1。」距离格保持轻适配。

## A2-15

处理：接受

改了 `docs/registry.md` 的 `frontierswe-v2` 行。距离由「重改造」改为「暂不宜接」。压力列写上「站上 34 题和对应验证器不在公开 commit，17 份 task.toml 不是站上的 v2 题单。」`docs/layer2/frontierswe-v2.md` 本来就是暂不宜接，不改那句。

## A2-16

处理：接受

改了 `docs/layer2/nl2repo-bench.md`「与 Harbor 距离」一节。原句「轻适配。」改为「unknown。」并写上 GPU 和多容器细节不够，不放进其余四档。登记本来就是 `unknown`。同卡写没有 `task.toml` 或 `dataset.toml`。

## A2-17

处理：不接受

登记和 `docs/layer2/terminal-bench-4-0.md` 都是原生可接，tag `v4.0.0` 对得上。压力列已经写部分题要 GPU、11 题要多服务容器。介绍卡写了 3 题 H100 和 11 题 `main` 以外的服务。原生可接没有抹掉这两句。不把这一行降档。

## A2-18

处理：不接受

`notes/rounds/R3.md` 同页写「入口一致指最终 URL 与 `docs/registry.md` 的入口 URL 相同。」`browsecomp` 一行的最终状态是 403，入口一致是「一致」。正文写最终 403，记失败，并写 20 个里成功 19、失败 1。这一格不是成功，也不是「已核实」。不把 URL 相同改成不一致。

## A2-19

处理：不接受

收束句说的是没有新的依赖类型。`video-mme`、`mmmu-pro`、`mathvision` 的登记距离和介绍卡距离都是 `unknown`。GPU 和容器仍写 unknown。这句没有把距离改成已接。不改这句，也不为这三个 slug 补镜像名。

## A2-20

处理：不接受

`notes/rounds/R3.md` 把 `automationbench` 放进确定性 verifier，依据是公开树用程序断言。登记和 `docs/layer2/automationbench.md` 的距离都仍是 `unknown`。介绍卡写公开树没有 Dockerfile，GPU 和多容器都是 unknown。距离没有被这句移走。不把距离改掉。

## A2-21

同意不成立

A2-RESPONSE-END

第二遍零命中。
`docs/layer0.md`、`docs/abstraction.md`、`docs/conversion-playbook.md`、`docs/layer2/browsecomp.md`、`docs/layer2/swe-atlas.md`、`docs/layer2/aa-briefcase.md`。
`notes/rounds/style-check.md`
