# osworld-verified

- slug: `osworld-verified`
- 抓取日: 2026-09-24 Asia/Shanghai
- 入口 URL: https://xlang.ai/blog/osworld-verified

## 官方仓

- 有，但是 OSWorld 本仓，不是另一个名叫 OSWorld-Verified 的仓库。博客写明数据与代码仍是:
  - https://github.com/xlang-ai/OSWorld
  - https://github.com/xlang-ai/OSWorld/tree/main/evaluation_examples
- 默认分支 `main` HEAD: `b138d348256078fa634fc3b73567a7337c793e6b`
- 核实: `git ls-remote` HEAD 与 commits API 一致。commit 日期 2026-09-14，说明 “mm_agents: recover code from replies truncated before the closing fence (#582)”。
- 没有名为 OSWorld-Verified 的 tag 或 release。现存 tag 只有 `v0.1.0`（`b1fc026bc46f5aa40c1882a7d119be2196cf5a47`，2024-04-11）和 `v0.1.16`（`0c5fbb8be4c60264133acef8032977bd6143e335`，2024-06-26），都早于 Verified 公告。
- 公告当日相关提交: `78651040e7c2`（2025-07-28，message 含 “OSWorld-Verified announcement”）。此后 main 又有提交，所以上面的 HEAD 才是 2026-09-24 看到的官方 tip。
- 许可证: Apache-2.0。GitHub `size` 字段 124,841 KB。该 HEAD 的 git tree 未截断，1,190 个 blob，合计 20,268,837 字节。未把克隆留在 `/workspace`。

## 论文 / blog / HF

- blog: https://xlang.ai/blog/osworld-verified（XLANG Lab，2025-07-28）。博客末尾 bib 的 journal 是 `xlang.ai`，没有单独的 Verified arXiv id。
- 原论文: arXiv [2404.07972](https://arxiv.org/abs/2404.07972)，“OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments”。README 引用同一 eprint。
- 任务 JSON 在 git 的 `evaluation_examples/`。虚拟机镜像在 Hugging Face，不是任务文本仓:
  - `xlangai/ubuntu_osworld`，API `sha` `a5d9c3eaae98eebf6e3a0beb84e7e47cf72ae133`
  - `xlangai/windows_osworld`（镜像文件，未下）
- 项目页 README 指向 https://os-world.github.io/ 。本次未把该站整页存下来。

## 测什么

在真实桌面环境里评测多模态计算机使用智能体完成开放式 GUI 任务；OSWorld-Verified 是同一套任务与代码上的基础设施和评分修复，不是新题集。出处: 博客 https://xlang.ai/blog/osworld-verified（“in-place upgrade”，数据与代码路径不变）；原论文标题见 arXiv 2404.07972。`evaluation_examples/test_all.json` @ HEAD 共 10 个域、369 条 id（chrome 46，gimp 26，libreoffice_calc 47，libreoffice_impress 47，libreoffice_writer 23，multi_apps 101，os 24，thunderbird 15，vlc 17，vs_code 23）。

## 环境线索

- 容器: 有。Docker provider 运行镜像 `happysixd/osworld-docker`，有 `/dev/kvm` 时把 KVM 设备传进容器，否则环境变量 `KVM=N`。镜像内是 QEMU 虚拟机，不是把宿主机当桌面。Ubuntu qcow2 来自 `https://huggingface.co/datasets/xlangai/ubuntu_osworld/resolve/main/Ubuntu.qcow2.zip`。
- 出网: 需要。任务会打开真实网站；README / SETUP 有代理和 Google 账号配置，缺了对应任务会失败。首次运行还要下载 VM 快照。
- GPU: 评测脚本没有把本地 GPU 写成必需。视觉基线示例是 API 模型加 `observation_type screenshot`。`desktop_env/providers/pyromind/provider.py` 创建沙箱时写 `gpu: 0`。
- K8s: 有一条可选路径，不是默认。`desktop_env/providers/pyromind/PYROMIND_GUIDELINE.md` 写明 StatefulSet 以只读方式挂载 `/System.qcow2`，用副本数 `1 → 0 → 1` 做 revert。README 安装节只是说：若人已经在 AWS、Azure 或 k8s 这类虚拟化环境上，就不要走裸机 VMware 步骤。仓库树里没有自带的 Helm chart 或集群清单文件名。
- 多容器 / 多环境: 有。`scripts/python/run_multienv.py --provider_name docker --num_envs 10` 会并行多个环境。provider 目录还包括 vmware、virtualbox、aws、azure、gcp、aliyun、volcengine、modal、daytona、fastvm、pyromind。`monitor/docker-compose.yml` 存在（537 字节），未整文件抄入。
- 另外: `.gitmodules` 有两个 SSH submodule（`mm_agents/surferH/rdds`、`mm_agents/surferH/agp_client`），本次未初始化。

## 评分

程序化、对着环境终态打分，不另调 judge 模型。每题 JSON 带 evaluator；实现在 `desktop_env/evaluators/`（getters 取 VM 状态，metrics 做表、文档、幻灯片、浏览器等比对）。对该目录下 29 个小于 200KB 的文本文件检索 `openai` / `gpt` / `llm` / `judge` / `claude` / `gemini`，仅两处无关命中：`metrics/slides.py` 注释 “judge if the color is red”，`getters/chrome.py` 注释 “Query to check for OpenAI cookies”。博客描述的模糊匹配、感知哈希、`compare_docx_files` 的 0–1 分仍是程序规则，不是第二个模型。

## agent / runtime

证据在仓内，不是 unknown。`mm_agents/` 放 agent；入口是 `run.py`（README 标为单线程、已不推荐）和 `scripts/python/run_multienv.py` 及 `run_multienv_xxx.py`。README 示例是 `--observation_type screenshot`、`--model gpt-4o`、`--max_steps 15`、动作空间 `pyautogui`。公开榜需要把 agent 接到这套接口后，由维护者在他们的 AWS 公共评测上跑（见博客 “How to Use” 与 README Public Evaluation）。

## 体积与是否入 git

- 不要把 OSWorld 克隆放进本仓库。GitHub 报告约 122 MB；工作树 blob 约 20.3 MB，仍大于 5 MB，且含大锁文件 `uv.lock`（1,205,286 字节）。
- 不要把 VM 镜像放进 git。`xlangai/ubuntu_osworld` 上 `Ubuntu.qcow2.zip` 的 HTTP `content-length` 为 12,273,896,463 字节；同数据集还有约 12 GB 的 `Ubuntu-x86.zip` / `Ubuntu-arm.zip`，以及约 23.7 GB 的 `Ubuntu_claude.qcow2`。`xlangai/windows_osworld` 上 `Windows-10-x64.qcow2.zip` 为 27,721,652,297 字节，未压缩 qcow2 约 49 GB。这些只做了 API / HEAD，没有下载。
- 本目录只有 MANIFEST 和短摘录，可以进 git。README 里的默认 VM 口令未转写。

## 未抓取项与原因

- 未克隆 OSWorld，避免在 `/workspace` 留下大于 5 MB 的检出。
- 未下载 Ubuntu/Windows 镜像、Google Drive cache、submodule。
- 未保存 AWS AMI 映射以外的云账号材料。AMI id 只留在上游 `desktop_env/providers/aws/manager.py`，此处不复制。
- `xlang-ai/OSWorld-V2` 是另一个仓库（说明为 OSWorld 2.0 long-horizon，GitHub `size` 87,273 KB，本次看到的 HEAD 不是本 slug 的入口）。博客把 Verified 指到 OSWorld，因此 V2 未当作本 slug 的官方仓抓取。
- 项目站 https://os-world.github.io/ 未整页存档。

MANIFEST-END
