# Milk-V Duo 256m

## 测试环境

### 操作系统信息

- BuildRoot & FreeRTOS
  - 下载链接：https://github.com/milkv-duo/duo-buildroot-sdk/releases
    - Milk-V 官方提供的 BuildRoot SDK，同时包含了 FreeRTOS
  - 参考安装文档：https://github.com/milkv-duo/duo-buildroot-sdk
- Debian
  - 下载链接：https://github.com/Fishwaldo/sophgo-sg200x-debian
  - 参考安装文档：https://github.com/Fishwaldo/sophgo-sg200x-debian
- RT-Thread
  - 源码链接：https://github.com/RT-Thread/rt-thread
  - 参考安装文档：https://github.com/RT-Thread/rt-thread/blob/6101f1fd29374ac69c107e3cfeadfa06b0c901f9/bsp/cvitek/cv18xx_risc-v/README_zh.md

### 硬件开发板信息

- Milk-V Duo (256M, SG2002)

## 测试结果

| 软件分类                 | 软件包名 | 测试结果（测试报告）                          |
|--------------------------|----------|-------------------------------------------|
| BuildRoot 镜像启动       | N/A      | [成功][BuildRoot]                           |
| FreeRTOS 启动            | N/A      | [成功][FreeRTOS]（已包含在 BuildRoot 镜像内） |
| Debian 镜像启动          | N/A      | [成功][Debian]                              |
| RT-Thread 镜像构建及启动 | N/A      | [成功][RT-Thread]                           |
| Zephyr 镜像构建及启动     | N/A      | [成功][Zephyr]                             |
  
[BuildRoot]: ./BuildRoot/README_zh.md
[Debian]: ./Debian/README_zh.md
[RT-Thread]: ./RT-Thread/README_zh.md
[FreeRTOS]: ./FreeRTOS/README_zh.md
[Zephyr]: ./Zephyr/README_zh.md