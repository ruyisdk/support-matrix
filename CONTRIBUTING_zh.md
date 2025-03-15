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
3. 提交更改，确保提交信息清晰易懂
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
---
```

```yaml
# /开发板/发行版/README.md
sys: armbian          # 系统标识（参考 assets/metadata.yml）
sys_ver: 24.05        # 系统版本（尽量采用语义化版本号）
sys_var: minimal      # 变体标识（可选）
status: basic         # 支持状态（none/wip/cft/cfh/partial/basic/good）
last_updated: 2024-03-01  # 最后更新时间
---
```

### 状态枚举说明

请参考 [README_zh.md](./README_zh.md) 的 `说明` 部分。

| 状态值   | 说明                          |
|----------|-----------------------------|
| none     | 无官方支持                    |
| wip      | 支持进行中                    |  
| cft      | 需要社区测试 (Call For Test) |
| cfh      | 需要硬件支持 (Call For Hardware) |
| partial  | 部分功能可用                  |
| basic    | 基础功能正常                  |
| good     | 完整支持                      |

## 文档编写规范

### 测试报告要求
1. 测试环境必须包含：

   ```markdown
   ## 测试环境
   ### 操作系统信息（系统版本、下载链接、参考安装文档）
   ### 硬件信息（开发板信息、调试器信息）
   ```

2. **测试步骤**需包含：
   ```markdown
   ## 安装步骤
   ### 刷写镜像
   1. 下载镜像文件
   2. 如需额外操作切换到刷写模式，请一并说明
   3. 使用 dd 命令写入存储设备 / fastboot 刷写 / 使用厂商提供的工具刷写
   
   ### 系统启动过程
   1. 从串口登录
   2. 首次启动配置流程
   3. 使用 asciinema 记录终端操作过程
   ```

3. **验证结果**需包含：

   ```markdown
   ## 预期结果
   ## 实际结果
   1. 启动日志关键片段
   2. 功能测试截图/录屏
   ```

4. 建议参考项目中的示例文档进行编写。

### 国际化(I18N)
- 主文档使用英文编写（README.md）
- 中文翻译文档使用 README_zh.md 格式
- 翻译文档**不包含**元数据头
- 保持文档间超链接的正确性
- 使用与其他同语言文档一致的术语
