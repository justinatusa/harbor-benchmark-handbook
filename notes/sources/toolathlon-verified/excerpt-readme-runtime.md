来源：https://github.com/hkust-nlp/Toolathlon/blob/9be8d8fe07a497b18ee61e3f2ae694e9797f39eb/README.md
抓取：2026-09-24。运行时摘录，不含账号、密钥或示例命令里的主机地址。

- 本仓对应 Toolathlon-Verified final release。
- 每题一个容器；Docker 或 Podman，写在 configs/global_configs.py。
- 自建安装建议 Linux，且能直接访问 Internet。k8s 相关配置写在 global_preparation/install_env_minimal.sh。
- 本地应用由 global_preparation/deploy_containers.sh 部署；细节在 deployment/*/scripts/setup.sh。
- 镜像名出现在 README：docker.io/lockon0927/toolathlon-task-image:1016beta。
- Toolathlon-Verified：单题最长 5400 秒；每轮默认最大输出 64K，并指定 reasoning effort。
- 默认脚手架基于 openai-agents-python。解耦模式的 agent_framework：toolathlon_default、claude_agent_sdk。
- OpenHands 集成在分支 openhands-compatibility，不在本次钉住的 main。
- 另有公开评测服务，说明在 EVAL_SERVICE_README.md。本次没有连接该服务。
