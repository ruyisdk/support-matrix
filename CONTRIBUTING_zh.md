# RISC-V 开发板与操作系统支持矩阵贡献指南

[English](./CONTRIBUTING.md) / [中文](./CONTRIBUTING_zh.md)

## 概述

本文档面向希望为 RuyiSDK 支持矩阵项目贡献内容的开发者。项目采用 GitHub Pull Request 机制进行协作。

参与贡献前，您需要：
1. 拥有 [GitHub 账号](https://github.com/signup)
2. 熟悉基本的 Git 操作和 GitHub 工作流
3. 了解项目数据结构规范（见下文）

如果您不熟悉 GitHub 和 Git，建议先查看 [GitHub 快速入门指南](https://docs.github.com/cn/get-started/quickstart/hello-world)。

本文档包含一般性贡献信息，项目的各个部分也有更具体的说明：
- [开发板（示例 VisionFive2）](./VisionFive2/README.md)：支持的开发板列表和说明。
- [系统（示例 VisionFive2/Alpine）](./VisionFive2/Alpine/README.md)：支持的操作系统变体。
- [本仓库元数据解析、SVG 生成、镜像源同步等工具](./assets/)：新增开发板或操作系统时，其中的 [metadata.yml](./assets/metadata.yml) 可能需要同步修改。
- [镜像源同步用元数据解析插件](./assets/src/ruyi_index_updator/upload_plugin)：部分 metadata 中 sys_ver 不符合 semver 标准的，可能会以插件形式进行调整。

项目结构分层：

```plaintext
支持矩阵
 |
 |--- 开发板
    |
    |--- README.md # 开发板的说明文档，开发板的基本metadata包含其中
    |
    |--- 各个系统
    |    |
    |    |--- README.md # 该系统主变体的说明文档，系统的基本metadata包含其中
    |    |
    |    |--- README_变体.md # 该系统的其他变体的说明文档，变体的metadata包含其中
    |    |
    |    |--- README(_变体)_lang.yaml # 各种语言的翻译，**不包含metadata！**
    |
    |--- others.yml # 没有文档的系统的metadata
```

## 快速开始

### 创建 PR 流程

1. Fork 并克隆仓库到本地
2. 创建分支并更新/新增开发板、测试报告
3. 提交更改，确保提交信息清晰易懂（最好在推送之前合并 / 压缩您的提交。）
4. 推送提交到您的 Fork 仓库并创建 Pull Request

> [!Note]
> 如果元数据无法解析或文档内容不符合要求，您的拉取请求可能会被要求修改。

## 数据结构规范

### 元数据定义

所有文档必须包含 YAML 元数据头，字段定义如下：

```yaml
# /开发板/README.md
---
vendor: _     # 厂商标识（小写字母+下划线）
product: _    # 产品全称
cpu: _        # 处理器型号
cpu_core: _   # CPU 核心架构
board_variant: [] # 开发板变体（可选，如 8g/16g 版本）
---
```

vendor 字段目前有部分板子暂缺，可以留空。如需填写，需要遵照 RuyiSDK 命名规则。

```yaml
# /开发板/发行版/README.md
sys: armbian          # 系统标识（参考 assets/metadata.yml）
sys_ver: "24.05"        # 系统版本（应当和镜像的版本相同，不要强行加入其余部分来满足如语义化版本号等格式。前导 `v` 可省略。 *注意：如 `24.05` 会被视为一个数字，必要时请添加引号。*）
sys_var: minimal      # 变体标识（可选）
status: basic         # 支持状态（none/wip/cft/cfh/partial/basic/good）
last_updated: 2024-03-01  # 报告最后更新时间
---
```

注意，某某 OS 的 LTS 版本单独算一个 variant。

LTS 标识因历史原因存在于部分 sys_var 中作为变体，但目前通行写法是置于 sysver 中。

理想情况下 NeZha-D1s/Ubuntu/README_LTS.md 中 Ubuntu 24.04.1 应当写作：

```yaml
sys_ver: 24.04-LTS-SP1        # 系统版本（应当和镜像的版本相同，不要强行加入其余部分来满足如语义化版本号等格式。前导 `v` 可省略）
sys_var: LTS                  # 变体标识（可选）
```

如还有不清楚的部分，可以联系 @wychlw。

---

注：

下面是一些您可能会在元数据头中遇到的字段，但未在上面列出。这些字段通常在其他工具中发挥特定作用，以满足某些特殊需求。

```yaml
skip_sync: true/false # 是否跳过与 RuyiSDK 的同步。
link: some_link # 镜像源链接。由于某些原因，可能无法生成镜像源链接，因此使用此字段直接提供链接。
symlink: [xxx, yyy] # 让工具将当前文件视为多个文件的列表。有时一个报告可以覆盖多个 OS 变体，因此使用此字段提供 OS 变体列表。比如，一个带 GUI 的镜像，或者一个带有或不带有某些特殊功能的镜像。
```

### 状态枚举说明

请参考 [README_zh.md](./README_zh.md) 的 `说明` 部分。

| 状态值   | 说明                          |
|----------|-----------------------------|
| none     | 该 OS/开发板组合没有官方或其他来源的支持      |
| wip      | 官方公告称将要/正在支持该 OS/开发板组合，但暂无镜像或其他资源（如源代码）      |
| cfi      | 官方文档声称支持该 OS，但暂无可用的 OS 镜像      |
| cft      | 可用的 OS 镜像，需要在真实硬件上进一步验证      |
| cfh      | 官方文档/社区论坛显示该 OS/开发板组合支持，但实际上无法启动      |
| partial  | 部分功能可用                      |
| basic    | 基础功能正常                      |
| good     | 完整支持                      |

## 文档编写规范

### 测试报告要求

请参考以下模板：

- [单个操作系统的报告模板](./report-template/[board-name]/[os-name]/README.md)
- [开发板概览的报告模板](./report-template/[board-name]/README.md)

### 国际化 (i18n)
- 主文档使用英文编写（README.md）
- 翻译文档使用 README_{lang}.md 格式（如中文文档可使用 README_zh.md）
- 翻译文档 **不包含** 元数据头
- 保持文档间超链接的正确性
- 使用与其他同语言文档一致的术语