# 抽查

走了两节，都在 `docs/conversion-playbook.md`。一节是「任务不公开或 gated」。A2 接受过：这节不要求 `tests/test.sh`。另一节是「确定性 verifier」。

## 任务不公开或 gated

1. 打开 `docs/registry.md` 的 `aa-briefcase` 行，看「与 Harbor 距离」。能落到。该格是「暂不宜接」。不是这个词就停。
2. 打开 `notes/sources/aa-briefcase/MANIFEST.md` 的「未抓取项与原因」。能落到。该节写正榜题面没有公开 URL。停止条件：没有任务文件就停，不写 `tests/test.sh`，也不写 `tests/test.bat`。
3. 打开同一份 MANIFEST 的 HF 段。能落到。数据集卡写明这是第五个场景里的一周，不进计分榜。不要把这一周写成正榜 91 题。
4. 打开 `notes/sources/deepswe-v1-1/MANIFEST.md` 的 HF 行。能落到。该行写 held-out、gated，行数据未下载，任务数 113。停止条件：不写从 gated 库取出 113 行的命令。
5. 打开 `notes/sources/swe-bench-pro/MANIFEST.md`。第一次写的是「未抓取项」，文件标题是 `## 未能抓取`，对不上。清单已改成这个标题。能落到。该节写 commercial 276 与 held-out 858 不在公开仓。停止条件：不为这两部分写 `tests/test.sh`。公开的 642 不在本节处理。

## 确定性 verifier

1. 打开 `notes/sources/spreadsheetbench/excerpt-scoring.py`。能落到。文件里有 `soft_restriction`，单元格用 `==`。这份摘录里没有 judge 模型名。
2. 打开 `notes/sources/posttrainbench-v1-1/MANIFEST.md` 下游任务分。能落到。GPQA 脚本使用 `scorer=choice()`。`gsm8k`、`humaneval`、`aime2025`、`gpqamain`、`bfcl` 没有 `JUDGE_MODEL`。Arena Hard Writing 与 HealthBench 写了 `JUDGE_MODEL`，这两题改走「要另调 judge 模型」。
3. 打开 `notes/rounds/r1-package-map.md`。第一次把 `/logs/verifier/reward.json` 写进这一条，该文件只给出 `/logs/verifier/reward.txt`，以及注释里的 `/logs/verifier/rewards.json`。清单已改成文件里的句子。能落到。解析器先认 `reward.json`，再认 `reward.txt`。两个都没有则 `RewardFileNotFoundError`。不要写 `/logs/verifier/rewards.json`。
4. pytest 这一条不能勾。原因写在清单里。转化步骤第 4 步写本轮打开的清单没有点名 pytest 文件，不要另编文件名。停止条件：工作区没有那份文件，停住。
5. 打开 `notes/sources/spreadsheetbench/excerpt-scoring.py` 的 `proc_path` 注释。能落到。当前指向 `*_input.xlsx`，`*_output.xlsx` 那行被注释。没改成比模型输出就停在这一步。
6. 打开 `notes/sources/osworld-verified/MANIFEST.md` 评分段。能落到。比对目录是 `desktop_env/evaluators/`。`compare_docx_files` 按程序规则看。不要去配 judge 密钥。

SPOTCHECK-END
