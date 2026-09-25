# 分面证据摘录

审查 tip：`1976a2fdacc358ffaa207184fbca9409e78a638b`。克隆与安装包对照发生在 2026-09-25。原始长文在审查机的 `/tmp/review-facets/`，不入库。

## 1. 组件抽象 vs Harbor 0.23.0

安装包 `/home/ubuntu/.local/share/uv/tools/harbor/lib/python3.12/site-packages/harbor`。

- `agents/installed/base.py` 有 `class BaseInstalledAgent` 与抽象方法 `install()`。改前 `docs/conflicts.md` 写本安装没有这个类。
- `models/task/task.py` 的 `is_valid_dir` 在缺 `environment/` 时返回假。`FileNotFoundError` 在 `environments/definition.py`，且仅当 `docker_image`、`Dockerfile`、`docker-compose.yaml` 都没有。
- `models/task/config.py` 环境基线 `network_mode` 默认 public。`environments/base.py` 有效 GPU 数为 `gpus or 0`。默认 docker 在 `models/trial/config.py`，条件是 `type` 与 `import_path` 都空。
- `models/task/config.py` 的 `schema_version` 默认 `"1.4"`，类型是 `str`，不拒绝 `"1.0"`。
- `environments/definition.py` 的 `COMPOSE_FILE_NAME` 是 `docker-compose.yaml`。OpenSandbox 对 yaml 和 yml 都拒绝。
- 全包类定义没有 `LLMJudge`。`VerifierResult` 只有 `rewards`。核对命令输出 `False` 与 `['rewards']`。

## 2. 转化路径

五个钉死 commit 都检出。被 playbook 点名的路径在仓内：

- SpreadsheetBench `49b73a9`：`evaluation/evaluation.py` 的 `proc_path` 指向 `*_input.xlsx`，`*_output.xlsx` 被注释。
- PostTrainBench `3ed1d32`：`src/commit_utils/single_task.sub` 为 1×H100；GPQA 的 `evaluate.py` 是 `scorer=choice()` 且没有 `JUDGE_MODEL`。
- CharXiv `7ebe88f`：`src/descriptive_utils.py` 固定 `gpt-4o-2024-05-13`；test JSON 答案为 `null`。
- simple-evals `652c89d`：`browsecomp` 使用 `grading_sampler`，模型 `gpt-4.1-2025-04-14`。
- OSWorld `b138d34`：`desktop_env/evaluators/` 存在；`monitor/docker-compose.yml` 是 `.yml`。

AA-Briefcase 公开页称 private evaluation。第五场景示例不进计分榜。没有公开任务仓。

## 3. Registry 与名单

52 行与 `prompts/bench-list.md` 的 slug 一一对应，`pilot` 全是 `no`。改前介绍卡 31 张，缺 21。改前距离与卡一致，迁入代价有多处卡写中、表写低。例子 8 个 slug 分属不同距离档，不是一个档。

## 4. 介绍卡

六张 `unknown` 卡都已经写明没有 `task.toml`，却用「缺一句评测不要 GPU」停档。`programbench` 卡写迁入代价中，registry 写低，并引用 `notes/verify/v2/08-closed-gated.md`。第 10 项全部指向 `notes/sources/<slug>/MANIFEST.md`。

## 5. gated

暂不宜接 14 行的压力句都写了不公开、gated，或正式评分不在公开仓。这次没有把它们改成可接。AA-Briefcase 的公开页与「正榜不公开」一致，但页面没有逐字写「题面、输入和评分表保持私有」。

## 6. 链接

抽查 54 个 URL。Harbor 文档站多数 200。`/datasets/adapters` 仍 404。BrowseComp 入口 403（`cf-mitigated: challenge`）。由 registry 拼出的 12 个 commit URL 为 200。`github.com/laude-institute/harbor` 301 到 `harbor-framework/harbor`。

## 7. 文风

`docs/` 39 个 markdown 里，no-ai-slop-zh 的二元对立、废话开头、伪洞察、冒号揭示、表面分析、重要性吹捧、模糊引用、否定列举、反问、伪深刻结尾、总结性重复结尾为零命中。禁用词 1 条在当时的 `docs/done-when.md`（「对齐」）。调研腔主要是「清单没写」「勿升档」「本轮」「notes 出处」。

## 8. 第 7 节过程对照

改前 `docs/done-when.md` 十项全勾。`notes/final-report.md` 写介绍卡 30 张，目录当时是 31 个文件。全勾与「没有 task 目录仍标轻适配」同时存在。勾选已移出 `docs/`。

## 9. 公开读者路径

改前 `docs/layer0.md` 写「未核实的 slug 写在 `notes/final-report.md`」。registry 52 格本地目录都是 `notes/sources/<slug>/`。公开镜像不含 notes 时这些链接不可打开。
