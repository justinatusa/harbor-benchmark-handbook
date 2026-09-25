# 待接入 Benchmark 名单（bench-list）

> 本文件是 Harbor 调研任务的**权威名单**。主提示词见同目录 `harbor-unified-abstraction-research.md`。
> 不要把公司内部「接入优先级 / 对齐状态」写进本文件；Agent 只按下列 slug 与入口拉源。

合计：**52** 个（斜杠版本已拆开；SWE-Atlas 三轨仍算 1）。

| # | slug | 常用名 | 入口 URL | 备注 |
|---|---|---|---|---|
| 1 | `gdpval-aa-v2-1` | GDPval-AA v2.1 | https://artificialanalysis.ai/evaluations/gdpval-aa | Artificial Analysis 对 OpenAI GDPval 的评测；数据 openai/gdpval；harness Stirrup |
| 2 | `aa-briefcase` | AA-Briefcase v1.1 | https://artificialanalysis.ai/evaluations/aa-briefcase | 闭源/私有任务；HF 有 AA-Briefcase-Lite 示例；非开源 |
| 3 | `agents-last-exam` | Agents' Last Exam (ALE) | https://agents-last-exam.org/ | GitHub rdi-berkeley/agents-last-exam；arXiv 2606.05405 |
| 4 | `draco` | DRACO | https://huggingface.co/datasets/perplexity-ai/draco | Perplexity Deep Research；博客+arXiv 2602.11685 |
| 5 | `browsecomp` | BrowseComp | https://openai.com/index/browsecomp | OpenAI；数据在 openai/simple-evals；arXiv 2504.12516 |
| 6 | `onemillion-bench` | $OneMillion-Bench / OneMillion-Bench | https://github.com/humanlaya/OneMillion-Bench | HF OneMillionBench/OneMillion-Bench；arXiv 2603.07980 |
| 7 | `spreadsheetbench` | SpreadsheetBench | https://github.com/RUCKBReasoning/SpreadsheetBench | V1 孤立操作；站点 spreadsheetbench.github.io |
| 8 | `spreadsheetbench-2` | SpreadsheetBench 2 | https://github.com/RUCKBReasoning/SpreadsheetBench-2 | 端到端工作流；arXiv 2606.29955；与 V1 分开 |
| 9 | `analystbench` | AnalystBench | https://aclanthology.org/2026.findings-acl.1197/ | ACL 2026 Findings；长报告生成；用户标注非开源，未见公开数据集仓 |
| 10 | `officeqa-pro` | OfficeQA Pro | https://github.com/databricks/officeqa | Databricks；企业 grounded reasoning |
| 11 | `officeqa-pro-v2` | OfficeQA Pro V2 | https://huggingface.co/datasets/databricks/officeqa-pro-v2 | 与 Pro 分开；Databricks blog 介绍 V2 |
| 12 | `finance-agent-v2` | Finance Agent Benchmark v2 | https://vals.ai/benchmarks/fabv2 | Vals AI；github.com/vals-ai/finance-agent-v2 |
| 13 | `apex-agents` | APEX–Agents | https://huggingface.co/datasets/mercor/apex-agents | Mercor；arXiv 2601.14242；Epoch/AA 有复现 |
| 14 | `frontier-finance` | FrontierFinance | https://research.samaya.ai/benchmarks/frontier-finance | Samaya AI；arXiv 2608.11683 |
| 15 | `big-finance-bench` | BigFinanceBench | https://github.com/Rogo-Technologies/big-finance-benchmark | Rogo；arXiv 2606.03829 |
| 16 | `osworld-2-0` | OSWorld 2.0 | https://osworld-v2.xlang.ai/ | 长程工作流；arXiv 2606.29537；与 Verified 不同产品 |
| 17 | `osworld-verified` | OSWorld-Verified | https://xlang.ai/blog/osworld-verified | 原 OSWorld 修复版；github.com/xlang-ai/OSWorld |
| 18 | `gdp-pdf` | GDP.pdf | https://surgehq.ai/benchmarks/gdp-pdf | Surge AI；AA 有独立复现页；arXiv 2607.11192 |
| 19 | `mmmu-pro` | MMMU-Pro | https://huggingface.co/datasets/MMMU/MMMU_Pro | MMMU-Benchmark/MMMU；arXiv 2409.02813 |
| 20 | `omnidocbench` | OmniDocBench | https://github.com/opendatalab/OmniDocBench | OpenDataLab；HF 有数据集 |
| 21 | `charxiv` | CharXiv | https://github.com/princeton-nlp/CharXiv | Princeton NLP；科学论文图表 |
| 22 | `babyvision` | BabyVision | https://github.com/UniPat-AI/BabyVision | 儿童级视觉推理 |
| 23 | `perception-bench` | PerceptionBench | https://github.com/MoonshotAI/PerceptionBench | MoonshotAI；原子视觉感知 |
| 24 | `zerobench` | ZeroBench | https://zerobench.github.io/ | jonathan-roberts1/zerobench；HF 数据集 |
| 25 | `chartography` | Chartography | https://github.com/surge-ai/chartography | Surge AI；arXiv 2608.10677 |
| 26 | `vision2web` | Vision2Web | https://github.com/zai-org/Vision2Web | 视觉到建站；arXiv 2603.26648 |
| 27 | `benchcad` | BenchCAD | https://github.com/BenchCAD/BenchCAD-main | 程序化 CAD；仓名 BenchCAD-main |
| 28 | `3dcodebench` | 3DCodeBench | https://www.3dcodebench.com/ | 程序化 3D/Blender 代码生成 |
| 29 | `mathvision` | MATH-Vision (MathVision) | https://github.com/mathvision-cuhk/MATH-V | CUHK；亦称 MATH-V |
| 30 | `video-mme` | Video-MME | https://github.com/MME-Benchmarks/Video-MME | 视频多模态理解 |
| 31 | `automationbench` | AutomationBench | https://github.com/zapier/AutomationBench | Zapier；AA 跑 AutomationBench-AA 私有 split |
| 32 | `toolathlon-verified` | Toolathlon-Verified | https://github.com/hkust-nlp/Toolathlon | HKUST-NLP；HF hkust-nlp/Toolathlon |
| 33 | `mcp-atlas` | MCP-Atlas | https://github.com/scaleapi/mcp-atlas | Scale AI；真实 MCP servers |
| 34 | `terminal-bench-4-0` | Terminal-Bench 4.0 | https://www.tbench.ai/news/terminal-bench-4-0 | harbor-framework/terminal-bench；Laude/Stanford |
| 35 | `deepswe-v1-1` | DeepSWE v1.1 | https://github.com/datacurve-ai/deep-swe | DataCurve；deepswe.datacurve.ai；Harbor 兼容 |
| 36 | `frontierswe-v2` | FrontierSWE v2 | https://www.frontierswe.com/ | Proximal Labs；blog/v2；github.com/Proximal-Labs/frontier-swe |
| 37 | `nl2repo-bench` | NL2Repo-Bench | https://arxiv.org/abs/2512.12730 | EnvCommons/NL2RepoBench 为环境封装；官方以论文为主 |
| 38 | `terminal-bench-2-1` | Terminal-Bench v2.1 | https://github.com/harbor-framework/terminal-bench-2-1 | 与 4.0 分开版本；AA 有 leaderboard |
| 39 | `swe-bench-pro` | SWE-Bench Pro | https://arxiv.org/html/2509.16941 | 长程 SE；常见引用 SWE-Bench Pro |
| 40 | `programbench` | ProgramBench | https://github.com/facebookresearch/programbench | Meta/FAIR；programbench.com；从行为重建程序 |
| 41 | `swe-marathon` | SWE-Marathon | https://www.swe-marathon.org/ | 超长程 SE；arXiv 2606.07682；版本号以站点为准 |
| 42 | `swe-atlas` | SWE Atlas | https://github.com/scaleapi/SWE-Atlas | Scale；三轨 Codebase QnA / Test Writing / Refactoring，同一产品 |
| 43 | `mls-bench-lite` | MLS-Bench-Lite | https://github.com/Imbernoulli/MLS-Bench | MLS-Bench 轻量子集；ML 系统构建 |
| 44 | `posttrainbench-v1-1` | PostTrainBench v1.1 | https://posttrainbench.com/ | aisa-group/PostTrainBench；单卡 H100 后训练 |
| 45 | `frontiercode-1-1` | FrontierCode 1.1 | https://cognition.com/blog/frontier-code-1.1 | Cognition；任务未公开 GitHub |
| 46 | `cursorbench` | CursorBench | https://cursor.com/cursorbench | Cursor 专有/内部会话评测；公开页有，数据集不开源；版本号随产品更新 |
| 47 | `sec-bench-pro` | SEC-bench Pro | https://github.com/SEC-bench/SEC-bench-Pro | 长程安全漏洞挖掘；arXiv 2605.26548 |
| 48 | `exploitgym` | ExploitGym | https://arxiv.org/html/2605.11086v1 | 漏洞→真实 exploit；未见稳定官方 GitHub，以论文页为准 |
| 49 | `hle` | Humanity's Last Exam (HLE) | https://huggingface.co/datasets/cais/hle | CAIS；arXiv 2501.14249 |
| 50 | `critpt` | CritPt | https://critpt.com/ | 前沿物理推理；github CritPt-Benchmark/CritPt；私有 grading |
| 51 | `aa-omniscience` | AA-Omniscience | https://artificialanalysis.ai/evaluations/omniscience | 知识+幻觉；HF ArtificialAnalysis/AA-Omniscience-Public |
| 52 | `aa-lcr-v1-1` | AA-LCR v1.1 | https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning | Artificial Analysis Long Context Reasoning；HF ArtificialAnalysis/AA-LCR |

## 使用约定

1. Registry 与 `notes/sources/<slug>/` 的目录名优先用上表 **slug**。
2. 入口 URL 为公开定位起点；深挖时再补官方仓 / HF / 论文，并写入 MANIFEST。
3. 置信度为 medium 的项（analystbench、benchcad、nl2repo-bench、cursorbench、exploitgym）允许 URL 后续纠正，但不得空着不登。
4. 名单可增删：改本文件并 commit；主提示词不用整表重贴。

