# excerpt: omnidocbench

来源 commit `f133a71e9e91c3621c7ce8994200a7b394a06eb3`，文件 `README.md`。

测什么（README 开头）: “OmniDocBench is a benchmark for evaluating diverse document parsing in real-world scenarios” ；“This benchmark includes 1651 PDF pages”。

指标（README “Currently supported metrics”）: Normalized Edit Distance、BLEU、METEOR、TEDS、COCODet。

Overall（README End-to-End Evaluation）: `((1 - Text Edit Distance) * 100 + Table TEDS + Formula CDM) / 3`。

容器（README Option A）: `docker pull ghcr.io/zeng-weijun/omnidocbench-eval:repro-ubuntu2204`。同段写构建命令 `bash script/build_repro_docker_image.sh`。该 SHA 的 `git ls-tree` 没有 `script/` 或 Dockerfile。

`pyproject.toml` `[project].version` 为 `1.6.0`。`[tool.omnidocbench.system-dependencies]` 要求 CDM 时具备 Ghostscript、ImageMagick（PDF 读写）、TeX Live（pdflatex、kpsewhich、CJK）。
