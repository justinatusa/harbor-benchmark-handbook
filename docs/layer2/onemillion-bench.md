# OneMillion-Bench

代码仓 HEAD 的安装说明指向旧的 Hugging Face 仓。入口名单上的组织仓更新，两边的金融题文件字节数也不一样。清单没有判定哪一份才是论文用的原件。

1. 一句话测什么。测语言代理在法律、金融、工业、医疗和自然科学里做专家级开放题时，事实、推理、可行性和职业规范是否过关。400 题，中英双语。出处是 arXiv 2603.07980 摘要。HF 卡写同样的 400 条和五个域。

2. 官方源。代码 https://github.com/humanlaya/OneMillion-Bench ，`main` 的 commit `eb1ad8061152ae6d05a2adcc3c0d983675da962c`（2026-07-30，说明 “Merge pull request #4 from jacklanda/fix/append_omb_norm”），Apache-2.0。论文 https://arxiv.org/abs/2603.07980 。题面不在这个 git 里。入口指定的数据集 https://huggingface.co/datasets/OneMillionBench/OneMillion-Bench ，修订 `f0378e7226a867fd6db9a8d4a8b5750f1cb9ded5`（2026-05-07）。该 commit 的 README 仍指向 https://huggingface.co/datasets/humanlaya-data-lab/OneMillion-Bench ，修订 `5cf9d5005e2e1f20b4481ed50846161697e82a73`（2026-03-11）。旧仓没有 `economic_value.csv`。`economics_and_finance/test.json` 的 Content-Length：新仓 718,833 字节，旧仓 640,599 字节。

3. 形态。`dataset`、`verifier`。CLI `omb` 读 JSON、调生成模型、再调 judge。供应商自带的 search agent 当黑盒，循环不在本仓。文件树没有 `environment` 定义。公开材料没有 Harbor adapter。

4. 与 Harbor 距离。重改造。judge 对每条 rubric 做 yes 或 no。清单没有给出 `task.toml` 或 `dataset.toml`。

5. 环境。README、`docs/arch.md` 和论文都没写 Docker 或其他沙箱。harness 是本机 Python CLI。生成和评判都打模型 API（OpenRouter、DashScope、VolcEngine、Hunyuan、Ling、LiteLLM）。`--enable-search` 打开网页搜索。GPU、Kubernetes、多容器都没看到，记 unknown。

6. 评分。要另调模型。README 写 judge 对每条 rubric 做 yes/no，再按权重加总。`src/omb/config/default.yaml` 在这个 commit 里把 `JUDGE_MODELS` 设为 `google/gemini-3.1-pro-preview`，`REASONING_EFFORT` 为 `high`，并注释旧的 `google/gemini-3-pro-preview` 已不可用、新 judge 大约严 5–6 个点。论文式 (2) 把 Expert Score ≥ 0.7 记为通过；这个阈值作用在 judge 加权分上，不是字符串相等。论文 4.5 节写换六个 judge 时名次大致稳定，绝对分会变。

7. agent/runtime。仓内运行时是异步 HTTP 客户端，默认生成并发 128、超时 600 秒。论文另评供应商自带的 search agent 和 deep research 产品（官方 scaffold、OpenRouter、无搜索）。那些产品的内部 runtime 不在本仓，记 unknown。

8. 迁入代价。高。要先选定哪一份 HF 题面。评分要固定 `default.yaml` 里的 judge。打开搜索时还要出网。没有任务目录。

9. 对抽象的压力。`verifier` 的通过线是另一个模型的加权分，换 judge 绝对分会变。`dataset` 有两个 HF 仓，字节不一致。`agent` 的网页搜索是可选开关，供应商产品的循环不在本仓。没有容器可接成 `environment`。

10. 本地摘录。[`notes/sources/onemillion-bench/MANIFEST.md`](../../notes/sources/onemillion-bench/MANIFEST.md)。
