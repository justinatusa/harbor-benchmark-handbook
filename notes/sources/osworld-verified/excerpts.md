# osworld-verified excerpts

抓取日 2026-09-24 Asia/Shanghai。不含 VM 口令、不含 AMI、不含镜像。

## 入口如何指向仓库

博客 https://xlang.ai/blog/osworld-verified （2025-07-28）:

- Data: `https://github.com/xlang-ai/OSWorld/tree/main/evaluation_examples`
- Code: `https://github.com/xlang-ai/OSWorld`
- “OSWorld-Verified is an in-place upgrade of OSWorld with enhanced infrastructure and improved task quality. You can always still use providers like VMware and Docker with the new task suites.”

## README @ b138d348256078fa634fc3b73567a7337c793e6b

- 2025-07-28 更新条目把 OSWorld-Verified 指到同一博客，并写 AWS 并行可以把评测压到 1 小时内。
- 论文链接: https://arxiv.org/abs/2404.07972
- Docker 并行示例使用 `--provider_name docker`、`--num_envs 10`、`--observation_type screenshot`。

## 镜像与容器

`desktop_env/providers/docker/manager.py` 同一 SHA:

- `UBUNTU_X86_URL = "https://huggingface.co/datasets/xlangai/ubuntu_osworld/resolve/main/Ubuntu.qcow2.zip"`
- Windows zip: `https://huggingface.co/datasets/xlangai/windows_osworld/resolve/main/Windows-10-x64.qcow2.zip`

`desktop_env/providers/docker/provider.py` 同一 SHA: `containers.run("happysixd/osworld-docker", ...)`，存在 `/dev/kvm` 时加入该设备。

## K8s 只出现在可选 provider

`desktop_env/providers/pyromind/PYROMIND_GUIDELINE.md`: StatefulSet 只读挂载 `/System.qcow2`，用副本缩放模拟 `vmrun revertToSnapshot`。该 provider 还写明只能在平台内网调用，公网直接跑不受支持。
