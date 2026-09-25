# browsecomp excerpts

抓取日 2026-09-24 Asia/Shanghai。只保留短句。不含例题、不含解密后的 CSV。

## 测什么

arXiv HTML https://arxiv.org/html/2504.12516 摘要:

> We present BrowseComp, a simple yet challenging benchmark for measuring the ability for agents to browse the web. BrowseComp comprises 1,266 questions that require persistently navigating the internet in search of hard-to-find, entangled information.

同页写: “BrowseComp can be found at https://github.com/openai/simple-evals.”

## 评分与数据位置

`browsecomp_eval.py` @ `652c89d0ca9df547706735883097e9537d40dc47`:

- CSV URL: `https://openaipublic.blob.core.windows.net/simple-evals/browse_comp_test_set.csv`
- `problem` / `answer` 用该行 `canary` 解密后再送给 sampler 和 grader。
- grader 输出里用正则提取 `correct: (yes|no)`。

`simple_evals.py` 同一 SHA: `grading_sampler` 模型名为 `gpt-4.1-2025-04-14`，`browsecomp` 分支把该 sampler 传给 `BrowseCompEval`。

simple-evals README 同一 SHA: 2025-07 起仓库继续托管 BrowseComp 参考实现，许可证 MIT，页面为 https://openai.com/index/browsecomp。
