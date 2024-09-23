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
- Debian
  - 下载链接：https://github.com/Fishwaldo/sophgo-sg200x-debian/releases/tag/v1.4.0
  - 参考安装文档：https://github.com/Fishwaldo/sophgo-sg200x-debia
- Zephyr
  - 源码链接：https://github.com/zephyrproject-rtos/zephyr/tree/main
  - 参考文档：
      - https://docs.zephyrproject.org/latest/develop/getting_started/index.html
      - https://github.com/milkv-duo/duo-buildroot-sdk

### 硬件开发板信息

- Milk-V Duo S (512M, SG2000)

## 测试结果

| 软件分类                | 软件包名     | 测试结果（测试报告）    |
| ----------------------- | ------------ | ----------------------- |
| BuildRoot 镜像启动      | N/A          | [Successful][BuildRoot] |
| Debian 镜像启动         | N/A          | [Successful][Debian]    |
| FreeRTOS 启动           | mailbox-test | [Successful][FreeRTOS]  |
| Apache NuttX 构建及启动 | N/A          | [Successful][NuttX]     |
| Zephyr 镜像构建及启动   | N/A          | [Successful][Zephyr]    |

[BuildRoot]: ./BuildRoot/README_zh.md
[Debian]: ./Debian/README_zh.md
[FreeRTOS]: ./FreeRTOS/README_zh.md
[NuttX]: ./NuttX/README_zh.md
[Zephyr]: ./Zephyr/README_zh.md