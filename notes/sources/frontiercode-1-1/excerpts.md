# frontiercode-1-1 摘录

抓取日 2026-09-24 Asia/Shanghai。没有官方 git commit。

## 1.1 改了什么

来源：https://cognition.com/blog/frontier-code-1.1 （2026-07-07）

“Fair internet use. We refined our methodology to capture the nuance between legitimate internet use (e.g., looking up documentation) and unfair use (anything that could reveal a task's solution).”

“We audited all 1000+ grading criteria and relaxed 75 overly strict ones.”

“we are deprecating the Diamond set and will rely on Main and Extended going forward.”

不公平出网的处理：“flagged runs receive a score of zero.” 检测对象包括 source pull requests、upstream patches or files、solution-bearing mirrors or vendored copies。

## 题量与通过规则

来源：https://cognition.com/blog/frontier-code （2026-06-08）

“Diamond comprises the 50 hardest tasks, Main the 100 hardest (including Diamond), and Extended the full set of 150.”

“A solution passes if it clears all blocker criteria … A solution’s score is a weighted aggregate of the rubric items. Solutions that do not pass blocking criteria receive 0.”

“While we don’t currently plan to release the tasks publicly to avoid contamination, we are opening up our evaluation to all model creators.”

## 评分手段

同一篇原文的表：behavioral correctness 用 classical（注入测试）；mechanical cleanliness / regression safety 用 command；test correctness 用 reverse-classical；复杂行为用 adaptive classical grading（LLM 改编测试或应用代码）；scope 用 files/size，semantic 可选 LLM；code quality 用 prompt，由 LLM 对 diff 打分。
