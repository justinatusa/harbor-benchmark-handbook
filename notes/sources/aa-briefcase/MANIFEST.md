# MANIFEST

- slug: aa-briefcase
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://artificialanalysis.ai/evaluations/aa-briefcase

## 官方仓

- 计分用的任务仓：没有。评测页和 2026-06-18 的公告都写四个场景的题面、输入和评分表保持私有。
- 公告点名的开源代理框架（不是任务仓）: https://github.com/ArtificialAnalysis/Stirrup
- 该仓默认分支 main 的 HEAD: 247f24d56b2108235880ed2a2baea5d35b5a67ee
- HEAD 说明: chore: add 7 day exclusion rule (#81)
- committer 日期: 2026-08-04T00:02:44Z
- GitHub API `size`: 3344 KB。本次没有克隆，只核实 HEAD。
- 公开示例数据集不是上述 git 仓，见下节 HF。

## 论文 / blog / HF

- 评测页: https://artificialanalysis.ai/evaluations/aa-briefcase （标题 AA-Briefcase v1.1）
- 公告: https://artificialanalysis.ai/articles/aa-briefcase （页面日期 June 18, 2026）
- 方法: https://artificialanalysis.ai/methodology/intelligence-benchmarking 中的 “AA-Briefcase” 一节
- 没有 arXiv id
- HF: `ArtificialAnalysis/AA-Briefcase-Lite`
- 页面: https://huggingface.co/datasets/ArtificialAnalysis/AA-Briefcase-Lite
- HF 修订: 4dec557b47d43867a1648c0974db1d8208c8b677
- HF `lastModified`: 2026-06-19T02:03:22.000Z
- 数据集卡 `license`: apache-2.0。这是公开示例集的卡，不是私有正榜任务的许可。
- 数据集卡写明：这是第五个场景里的一周，不进计分榜；正榜四个场景仍然私有。

## 测什么

测代理做长程知识工作：四个私有的多周业务项目、共 91 个任务，交付表格、演示、备忘录等文件，再按核查项给分。出处：https://artificialanalysis.ai/evaluations/aa-briefcase 页首说明。公告用同一句任务范围，并写正榜材料不公开。

## 环境线索

下列运行描述来自方法页 AA-Briefcase 实现说明，并与 HF 数据集卡 “Harness setup” 一致。正榜任务文件本身未公开，所以不能用私有作业单再核对一遍。

- 容器: 有。方法页写提交在 Stirrup 里、按周构建的 E2B sandbox 中运行；代理提示词写 “isolated Linux container”，用户 `user`（UID 1000），家目录 `/home/user`。
- 出网: 明确没有。提示词写容器没有出站连接，没有代理、白名单或开关；`pip` / `npm` / `apt` / git 远程 / HTTP 都会失败。方法页写 sandbox 无互联网，只能用提供的源文件。
- GPU: 方法页和数据集卡的运行时清单是 Python 3.13、文档工具、LibreOffice、Pandoc、FFmpeg、TeX Live、Chromium 等，没有写 GPU。unknown。
- K8s: 没看到。unknown。
- 多容器: 没看到。描述是每个场景/周一个 sandbox、一个隔离容器。unknown 是否在 E2B 内部还有旁路容器。
- 其他已写明的限制: 每题最多 500 步；单条命令 20 分钟；上下文满了由 Stirrup 摘要早期历史；工具是 `code_exec`、可选的看图、`finish` 和 `abandon_task_finish`。同场景各周共享文件，但当前每题独立运行，不带上一次提交。

## 评分

要另外的 judge 模型，不是确定性对答案。

方法页写每题有两类检查：rubric 为对单份提交的二元通过/失败；pairwise 分 Analytical Quality 与 Presentation，比较两份提交。评判面板是三个模型：Claude Opus 4.8（max effort）、GPT-5.5（high reasoning）、Gemini 3.1 Pro Preview（high reasoning）。每条 rubric 结论和每次 pairwise 由面板中的一个 judge 决定，抽样在检查之间平衡，同一条 rubric 固定同一个 judge。judge 只看提交和 rubric，不看外部源文件。二元结果和 pairwise 再用极大似然 Elo 合成 Rubric、Analytical Quality、Presentation 和总的 AA-Briefcase Elo。Elo 拟合是程序，但通过/失败和偏好来自 judge 模型。

HF 卡把公开示例的检查分成 `A`/`C`（binary）和 `AQ`/`P`（pairwise），并写示例不进榜。

## agent / runtime

有。方法页和公告写代理框架是 Stirrup。运行单位是一周范围的离线 E2B sandbox，最多 500 turns，用代码执行提交文件。这是被测模型的代理运行时。三个 frontier judge 是另一套模型，见上节。

## 体积与是否入 git

正榜 91 题没有公开 git。公开示例在 HF 数据集仓，修订 4dec557b47d43867a1648c0974db1d8208c8b677。HF 树 198 个文件、合计 104,373,012 字节（约 99.5 MiB），含示例提交的 mp4。大于 5MB，没有把数据集克隆进 `/workspace`。

本目录留下的文本都小于 200KB，且都来自该修订的 `prompts/`：

- `excerpt-eval_system.txt`（867 字节）
- `excerpt-eval_submission.txt`（4339 字节）
- `excerpt-judge_system.txt`（1171 字节）
- `excerpt-judge_user.txt`（401 字节）

本次没有 git commit。

## 未抓取项与原因

- 四个正榜场景的题面、源文件、rubric：页面写明私有，没有公开 URL。
- `checks.jsonl` 385,046 字节、`grader/grading_rubric_w1.json` 395,994 字节、`grader/traceability_w1.json` 300,865 字节：超过单文件 200KB 摘录上限，未落盘。结构以数据集卡的字段说明为准。
- 源 PDF、表格、邮件、Slack 导出和示例 mp4：非小文本，且整集约 99.5 MiB。
- Stirrup 源码树：只核实 HEAD。方法页已经给出本评测使用的提示词和 sandbox 约束。
- 没有跑 sandbox，也没有调用 judge。

MANIFEST-END
