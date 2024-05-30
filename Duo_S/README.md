# Milk-V Duo S

## 测试环境

### 操作系统信息

- BuildRoot & FreeRTOS
  - 下载链接：https://github.com/milkv-duo/duo-buildroot-sdk/releases
    - Milk-V 官方提供的 BuildRoot SDK，同时包含了 FreeRTOS
  - 参考安装文档：https://github.com/milkv-duo/duo-buildroot-sdk
- Apache NuttX RTOS
  - 源码链接
    - NuttX: https://github.com/lupyuen2/wip-nuttx/tree/sg2000
    - NuttX Apps: https://github.com/lupyuen2/wip-nuttx-apps/tree/sg2000
  - 参考安装文档；https://github.com/lupyuen/nuttx-sg2000

### 硬件开发板信息

- Milk-V Duo S (512M, SG2000)

## 测试结果

| 软件分类                | 软件包名     | 测试结果（测试报告）  |
|-----------------------|--------------|---------------------|
| BuildRoot 镜像启动      | N/A          | [Basic][BuildRoot]  |
| FreeRTOS 启动           | mailbox-test | [Basic][FreeRTOS]   |
| Apache NuttX 构建及启动 | N/A          | [Basic, WIP][NuttX] |
| Zephyr 镜像构建及启动    | N/A          | [Basic][Zephyr]   |

[BuildRoot]: ./BuildRoot/README.md
[FreeRTOS]: ./FreeRTOS/README.md
[NuttX]: ./NuttX/README.md
[Zephyr]: ./Zephyr/README.md