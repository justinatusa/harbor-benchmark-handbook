# Layer1 总表

全量行在 `docs/registry.md`。一行一个 benchmark。

这一页只说明怎么读表：

- `slug` 与 `prompts/bench-list.md` 一致。
- `unknown` 表示还没核实。
- `pilot` 为 `no` 的行来自名单。后来为了撑开某个轴而加的对照样本，`pilot` 写成 `yes`。
- 「与 Harbor 距离」只允许这四个值：`原生可接`、`轻适配`、`重改造`、`暂不宜接`。没有证据时写 `unknown`，不要猜。

对照一个 slug 打勾。用词与 `docs/registry.md` 的「与 Harbor 距离」列一致。

- 原生可接。官方目录已经是 Harbor task，并且说明用 `harbor run` 跑。
- 轻适配。仓内已有 Harbor task 目录（`task.toml`、`environment/`、评分脚本），但版本、入口或网络还不是 0.23.0。没有 task 目录不算轻适配。
- 重改造。题和评分公开，但没有 Harbor task 目录，接入要新写 task、环境或评分回路。
- 暂不宜接。正榜题面不公开，或数据集 gated，写不出可交付的题。

`programbench`、`omnidocbench`、`benchcad` 都没有 Harbor task 目录，距离是重改造。`mmmu-pro`、`mathvision`、`video-mme`、`automationbench`、`nl2repo-bench` 同样没有 task 目录，评测脚本没有写明必须显卡，距离也是重改造。


## 距离一览

全列在 `docs/registry.md`。这里只留判断用的三列。

| slug | 与 Harbor 距离 | 迁入代价 |
|---|---|---|
| gdpval-aa-v2-1 | 重改造 | 高 |
| aa-briefcase | 暂不宜接 | 高 |
| agents-last-exam | 暂不宜接 | 高 |
| draco | 重改造 | 高 |
| browsecomp | 重改造 | 高 |
| onemillion-bench | 重改造 | 高 |
| spreadsheetbench | 重改造 | 高 |
| spreadsheetbench-2 | 重改造 | 高 |
| analystbench | 暂不宜接 | 高 |
| officeqa-pro | 暂不宜接 | 高 |
| officeqa-pro-v2 | 暂不宜接 | 高 |
| finance-agent-v2 | 重改造 | 高 |
| apex-agents | 暂不宜接 | 高 |
| frontier-finance | 重改造 | 高 |
| big-finance-bench | 重改造 | 高 |
| osworld-2-0 | 暂不宜接 | 高 |
| osworld-verified | 重改造 | 高 |
| gdp-pdf | 重改造 | 高 |
| mmmu-pro | 重改造 | 中 |
| omnidocbench | 重改造 | 中 |
| charxiv | 重改造 | 高 |
| babyvision | 重改造 | 高 |
| perception-bench | 重改造 | 高 |
| zerobench | 暂不宜接 | 高 |
| chartography | 重改造 | 高 |
| vision2web | 重改造 | 高 |
| benchcad | 重改造 | 高 |
| 3dcodebench | 重改造 | 高 |
| mathvision | 重改造 | 中 |
| video-mme | 重改造 | 高 |
| automationbench | 重改造 | 中 |
| toolathlon-verified | 重改造 | 高 |
| mcp-atlas | 重改造 | 高 |
| terminal-bench-4-0 | 原生可接 | 低 |
| deepswe-v1-1 | 轻适配 | 中 |
| frontierswe-v2 | 暂不宜接 | 高 |
| nl2repo-bench | 重改造 | 中 |
| terminal-bench-2-1 | 原生可接 | 低 |
| swe-bench-pro | 原生可接 | 中 |
| programbench | 重改造 | 中 |
| swe-marathon | 轻适配 | 高 |
| swe-atlas | 轻适配 | 中 |
| mls-bench-lite | 轻适配 | 低 |
| posttrainbench-v1-1 | 重改造 | 高 |
| frontiercode-1-1 | 暂不宜接 | 高 |
| cursorbench | 暂不宜接 | 高 |
| sec-bench-pro | 重改造 | 高 |
| exploitgym | 重改造 | 高 |
| hle | 暂不宜接 | 高 |
| critpt | 暂不宜接 | 高 |
| aa-omniscience | 重改造 | 高 |
| aa-lcr-v1-1 | 重改造 | 高 |
