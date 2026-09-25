# Layer1 总表

全量行在 `docs/registry.md`。一行一个 benchmark。

这一页只说明怎么读表：

- `slug` 与 `prompts/bench-list.md` 一致。
- `unknown` 表示还没核实。
- `pilot` 为 `no` 的行来自名单。后来为了撑开某个轴而加的对照样本，`pilot` 写成 `yes`。
- 「与 Harbor 距离」只允许这四个值：`原生可接`、`轻适配`、`重改造`、`暂不宜接`。没有证据时写 `unknown`，不要猜。

对照一个 slug 打勾。用词与 `docs/registry.md` 的「与 Harbor 距离」列一致。

- 轻适配。官方或仓内已有可对上的 Harbor task 形态：有 task 目录，或 MANIFEST、介绍卡里已写出的等价证据。
- 重改造。需要新写或大改 task、环境或评分回路。

`notes/verify/v2/08-closed-gated.md` 的原句是「`docs/layer1.md` 的轻适配要有能交出去的 task 目录」。本轮把「能交出去的 task 目录」收成上面的轻适配句。那份笔记没有写后半句：MANIFEST、介绍卡里已写出的等价证据，以及重改造这句。

`programbench` 对不上轻适配。`notes/sources/programbench/MANIFEST.md` 与 `docs/layer2/programbench.md` 都没有 task 目录，也没有可对上的 Harbor task 形态。MANIFEST 没有写明需要新写或大改 task、环境或评分。`docs/registry.md` 该行距离是 `unknown`。上面两句单独用来打勾。

表的列还会删。一列如果不能改变接入判断，就从 registry 拿掉，细节留在 `notes/`。
