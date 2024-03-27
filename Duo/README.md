# Milk-V Duo

## 测试环境

### 操作系统信息

- BuildRoot & FreeRTOS
  - 下载链接：https://github.com/milkv-duo/duo-buildroot-sdk/releases
    - Milk-V 官方提供的 BuildRoot SDK，同时包含了 FreeRTOS
  - 参考安装文档：https://github.com/milkv-duo/duo-buildroot-sdk
- Arch Linux
  - 下载链接：https://drive.google.com/file/d/1Qf8ioR29KCsvt2MIWre168Um9Q8ot_z5/view?usp=sharing
  - 参考安装文档：https://xyzdims.com/3d-printers/misc-hardware-notes/iot-milk-v-duo-risc-v-esbc-running-linux/#ArchLinux_Disk_Image
- Debian trixie/sid
  - 下载链接：https://drive.google.com/file/d/1TqMuFsRo5Es2Y6-qAyxV8jnFdAkcCp4v/view?usp=sharing
  - 参考安装文档：https://github.com/hongwenjun/riscv64/tree/main/milkv-duo
- Fedora 38
  - 下载链接：https://github.com/chainsx/fedora-riscv-builder/releases/download/20230719-1650/Fedora-38-Minimal-MilkV-Duo-riscv64.img.xz
  - 参考安装文档：https://github.com/chainsx/fedora-riscv-builder
- RT-Thread 5.1.0
  - 源码链接：https://github.com/RT-Thread/rt-thread
  - 参考安装文档：https://github.com/RT-Thread/rt-thread/tree/master/bsp/cvitek/cv1800b

### 硬件开发板信息

- Milk-V Duo (64M, CV1800B)

## 测试结果

| 软件分类                 | 软件包名 | 测试结果（测试报告）                          |
|------------------------|----------|-------------------------------------------|
| BuildRoot 镜像启动       | N/A      | [成功][Duo]（通过 `ruyi` CLI 刷写）           |
| FreeRTOS 启动            | N/A      | [成功][FreeRTOS]（已包含在 BuildRoot 镜像内） |
| Arch Linux 镜像启动      | N/A      | [成功][Arch]                                |
| Debian 镜像启动          | N/A      | [成功][Debian]                              |
| RT-Thread 镜像构建及启动 | N/A      | [成功][RT-Thread]                           |
| Fedora 镜像启动          | N/A      | [失败][Fedora]                              |

[Duo]: ./BuildRoot/README.md
[Arch]: ./ArchLinux/README.md
[Debian]: ./Debian/README.md
[Fedora]: ./Fedora/README.md
[RT-Thread]: ./RT-Thread/README.md
[FreeRTOS]: ./FreeRTOS/README.md