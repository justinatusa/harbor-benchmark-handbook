# cursorbench 摘录

抓取日 2026-09-24 Asia/Shanghai。没有官方 git commit。置信度 medium。

## 公开页

来源：https://cursor.com/cursorbench

“CursorBench 4.0”

“We evaluate agents on ambiguous, multi-file tasks from real Cursor sessions. Higher scores are better.”

changelog（页上 Sep 10, 2026）：4.0 “Introduced new long-horizon problems focused on edit, refactor, investigation, intent understanding, managing jobs, and design adherence.”

## 2026-03-11 blog（当时写的是 3.x）

来源：https://cursor.com/blog/cursorbench

“The offline part uses CursorBench, our internal eval suite based on real Cursor sessions from our engineering team.”

“We source tasks for CursorBench using Cursor Blame, which traces committed code back to the agent request that produced it.”

“we use agentic graders to reliably score them.”

文首注记：“The current production version is CursorBench 3.1”。

## Composer 2 报告（表 1 标的是 CursorBench-3）

来源：https://cursor.com/blog/composer-2-technical-report 对应 PDF 第 6.2、7.1 节。

“Environments are run on top of Anyrun, an internal compute platform built for running untrusted code at scale.”

“Each pod is a dedicated Firecracker VM capable of running a full development environment, including a browser and GUI for computer use.”

“Any access to the internet from a pod must go through Anygress.”

“7.1 CursorBench We evaluate our models by running Cursor agents directly within Anyrun … For each task in CursorBench, we initialize the codebase environment and initial task prompt, and we run the agent exactly as it would execute in our production environment.”

“Table 1 reports the accuracy of various models on CursorBench-3.”
