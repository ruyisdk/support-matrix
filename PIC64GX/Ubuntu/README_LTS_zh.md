# Ubuntu on Microchip PIC64GX Curiosity Kit

## 测试环境

### 硬件信息

- Microchip PIC64GX Curiosity Kit 开发板
- USB Type-C to Type-C 线缆一条（出厂附带）
- SanDisk Ultra microSD UHS-I Card 32GB 一张（出厂附带）

### 操作系统信息

- Ubuntu 24.04.2
    - 下载链接：https://cdimage.ubuntu.com/releases/24.04.2/release/ubuntu-24.04.2-preinstalled-server-riscv64+pic64gx.img.xz
        - TUNA 镜像源：https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/24.04.2/release/ubuntu-24.04.2-preinstalled-server-riscv64%2Bpic64gx.img.xz
    - 参考安装文档：https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/microchip-pic64gx1000-discovery/

### 其他信息

- PIC64GX Hart Software Services
    - 仓库链接：https://github.com/pic64gx/pic64gx-hart-software-services
- 开发板参考文档：https://www.microchip.com/en-us/development-tool/curiosity-pic64gx1000-kit-es
        - PDF；https://ww1.microchip.com/downloads/aemDocuments/documents/MPU64/ProductDocuments/SupportingCollateral/PIC64GX_Curiosity_Kit_User_Guide.pdf
- QuickStart Card: https://onlinedocs.microchip.com/oxy/GUID-6C67D962-A70D-4AD9-94B5-2AFDB8EFFD59-en-US-2/GUID-453EE85E-64C1-483D-9619-5CADA8E3FD8B.html

## （可选）更新 Hart Software Services (HSS)

根据 Ubuntu Wiki，Ubuntu 依赖 HSS v2024.06 或更新版本。

若开发板预装版本低于此版本则需要手动更新。

可从 Microchip 的官方 GitHub 仓库获取、构建并刷入 HSS：https://github.com/pic64gx/pic64gx-hart-software-services

## 烧录镜像至 microSD 卡

直接使用 Rufus/Win32DiskImager/dd 等工具写入镜像至 SD 卡即可。

```shell
xzcat ubuntu-24.04.2-preinstalled-server-riscv64+pic64gx.img.xz | sudo dd bs=1M conv=fsync status=progress of=/dev/sdX
```

## 启动开发板

直接使用附带的 Type-C to Type-C 线材连接计算机和开发板。

此时开发板会自动上电，板载的 USB-UART 串口会自动连接至计算机，并提供三个串口。

Windows 上会出现三个 COM 口（注意，Windows 下需要安装 FT4232HL 驱动：[链接](https://ftdichip.com/drivers/)），Linux 下会出现 /dev/ttyUSB{0,1,2}。

| 串口功能              | Windows         | Linux        |
| --------------------- | --------------- | ------------ |
| HSS 控制台            | 第一个 COM 端口 | /dev/ttyUSB0 |
| U-Boot & Linux 控制台 | 第二个 COM 端口 | /dev/ttyUSB1 |
| AMP 控制台            | 第二个 COM 端口 | /dev/ttyUSB2 |

使用任意工具连接至第一、第二个串口以查看启动信息。

> Ubuntu 首次启动会调用 `cloud-init`，受限于开发板性能，启动速度可能较慢，从上电到能够登录可能要花费数分钟时间，这是预期结果。

用户名：`ubuntu`

密码：`ubuntu`

初次登录时会强制要求修改密码，按提示操作即可。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

CFT

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT

## 参考文档
