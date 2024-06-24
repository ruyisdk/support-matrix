# Star64

## 测试环境

### 操作系统信息

**注：Star64 可以使用所有 Visionfive2 镜像，但 USB、Wifi 和 PCI 可能不工作（见[Bringup Notes](https://wiki.pine64.org/wiki/STAR64)）**

- NuttX
    - 源码链接：https://github.com/apache/nuttx
    - 参考安装文档：https://nuttx.apache.org/docs/latest/platforms/risc-v/jh7110/boards/star64/index.html
    - 工具链：
        - 启动镜像：https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/sdcard.img
        - DTB：https://github.com/starfive-tech/VisionFive2/releases
        - toolchain: https://github.com/sifive/freedom-tools/releases
        - kflash：https://github.com/kendryte/kflash.py
- Armbian
    - 下载链接：https://www.armbian.com/star64/
    - 参考安装文档：https://www.hackster.io/lupyuen/rtos-on-a-risc-v-sbc-star64-jh7110-apache-nuttx-2a7429
- Yocto
    - 下载链接：https://github.com/Fishwaldo/meta-pine64/releases/tag/v2.1
    - 参考安装文档：https://github.com/Fishwaldo/meta-pine64

### 硬件开发板信息

- Star64

## 测试结果

| 软件分类                | 软件包名 | 测试结果（测试报告）             |
|------------------------|----------|-----------------------------|
| NuttX 镜像构建及启动     | N/A      | [CFT][NuttX]                |
| Armbian 镜像启动        | N/A      | [CFT][Armbian]              |
| Yocto 镜像启动          | N/A      | [CFT][Yocto]                |

[NuttX]: ./NuttX/README_zh.md
[Armbian]: ./Armbian/README_zh.md
[Yocto]: ./Yocto/README_zh.md