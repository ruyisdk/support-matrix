# Microchip PIC64GX Curiosity Kit

## 测试环境

### 操作系统信息

- Ubuntu 24.10
    - 下载链接：https://cdimage.ubuntu.com/releases/24.10/release/
    - 参考安装文档：https://wiki.ubuntu.com/RISC-V/Microchip%20PIC64GX1000%20Curiosity%20Kit
- Ubuntu 24.04.1 LTS
    - 下载链接：https://cdimage.ubuntu.com/releases/24.04/release/
    - 参考安装文档：https://wiki.ubuntu.com/RISC-V/Microchip%20PIC64GX1000%20Curiosity%20Kit
- OpenEmbedded / Yocto
    - 下载链接：https://github.com/pic64gx/meta-pic64gx-yocto-bsp
    - 参考安装文档：https://github.com/pic64gx/meta-pic64gx-yocto-bsp
- Zephyr
    - 参考安装文档：https://github.com/pic64gx/pic64gx-zephyr

### 硬件信息

- Microchip PIC64GX Curiosity Kit

## 测试结果

| 软件分类                    | 软件包名 | 测试结果（测试报告）      |
| --------------------------- | -------- | ------------------------- |
| Ubuntu Image Boot           | N/A      | [CFT][Ubuntu][Ubuntu-LTS]（官方支持） |
| Yocto Image Build and Boot  | N/A      | [CFT][Yocto]              |
| Zephyr Image Build and Boot | N/A      | [CFT][Zephyr]             |

[Ubuntu]: ./Ubuntu/README_zh.md
[Ubuntu-LTS]: ./Ubuntu/README_LTS_zh.md
[Yocto]: ./Yocto/README_zh.md
[Zephyr]: ./Zephyr/README_zh.md