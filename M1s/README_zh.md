# Sipeed M1s

## 测试环境

### 操作系统信息

- FreeRTOS
  - 下载链接：
    - SDK：https://gitee.com/Sipeed/M1s_BL808_SDK
    - examples：https://gitee.com/Sipeed/M1s_BL808_example
  - 参考安装文档：https://wiki.sipeed.com/hardware/zh/maix/m1s/other/start.html
- BuildRoot/postmarketOS
  - 下载链接：https://github.com/openbouffalo/buildroot_bouffalo/releases/download/v1.0.1/bl808-linux-pine64_ox64_full_defconfig.tar.gz
    - SDK：https://github.com/bouffalolab/bl_mcu_sdk
    - 烧录工具：https://openbouffalo.org/static-assets/bldevcube/BouffaloLabDevCube-v1.8.3.zip
  - 参考安装文档：https://wiki.postmarketos.org/wiki/Sipeed_M1s_DOCK_(sipeed-m1sdock)
- RT-Thread
  - 下载链接：https://github.com/DongshanPI/buildroot_dongshannezhastu
  - 参考安装文档：https://github.com/RT-Thread/rt-thread/tree/master/bsp/bouffalo_lab/bl808

### 硬件开发板信息

- Sipeed M1s Dock

## 测试结果

| 软件分类              | 软件包名    | 测试结果（测试报告） |
| --------------------- | ----------- | -------------------- |
| BuildRoot 镜像启动    | N/A         | [CFH][BuildRoot]     |
| postmarketOS 镜像启动 | N/A         | [CFH][pmOS]          |
| FreeRTOS 启动         | hello_world | [成功][FreeRTOS]     |
| RT-Thread 启动        | N/A         | [CFH][RT-Thread]     |

[BuildRoot]: ./BuildRoot/README_zh.md
[RT-Thread]: ./RT-Thread/README_zh.md
[pmOS]: ./postmarketOS/README_zh.md
[FreeRTOS]: ./FreeRTOS/README_zh.md
