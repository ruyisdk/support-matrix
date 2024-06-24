# Armbian VisionFive 2 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：Armbian Noble Minimal & Armbian Jammy Xfce
- 下载链接：https://www.armbian.com/visionfive2/
- 参考安装文档：https://www.armbian.com/visionfive2/

### 硬件信息

- StarFive VisionFive 2
- USB 电源适配器一个
- USB-A to C 或 C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根
- 可选：显示器/采集卡 & HDMI 线缆（测试 Jammny 版本 Xfce 桌面）

## 安装步骤

### 解压并刷写镜像到 microSD 卡

假定 `/dev/sdc` 为存储卡。

```bash
wipefs -af /dev/sdc
# Jammy Xfce
xzcat Armbian_community_24.5.0-trunk.278_Visionfive2_jammy_edge_5.15.0_xfce_desktop.img.xz | sudo dd of=/dev/sdc iflag=fullblock status=progress bs=4M
# Edge minimal
xzcat Armbian_community_24.5.0-trunk.278_Visionfive2_noble_edge_5.15.0_minimal.img.xz | sudo dd of=/dev/sdc iflag=fullblock status=progress bs=4M
```

### 引导模式选择

StarFive VisionFive 2 提供了多种引导模式，可在上电前通过板载拨码开关进行配置；开发板本体上亦有丝印标注。

为了启动 Armbian 镜像，选择 1-bit QSPI Nor Flash 模式（即：`RGPIO_0 = 0`, `RGPIO_1 = 0`）。注意，此模式可能需要提前更新 Flash 内的固件，若启动不成功，请参考官方文档进行固件升级：[更新 SPL 和 U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)

### 登录系统

通过串口登录系统。

启动后，系统会要求用户手动配置用户名、密码、时区、语言等。

Xfce 版本需要配置完成后方可进入桌面。

可通过串口配置。若接入了键盘和显示器，亦可通过键盘配置。

## 预期结果

系统正常启动，能够通过图形界面或串口登录。

## 实际结果

Xfce 版本和 Minimal 版本系统均正常启动，成功通过图形界面或串口登录。

### 启动信息

```log
root@visionfive2:~# uname -a
Linux visionfive2 5.15.0-edge-starfive2 #1 SMP Fri Mar 1 15:21:08 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux
root@visionfive2:~# cat /etc/os-release 
PRETTY_NAME="Armbian_community 24.5.0-trunk.278 noble"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04 (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://github.com/armbian/build"
SUPPORT_URL="https://community.armbian.com/"
BUG_REPORT_URL="https://github.com/armbian/community/issues"
PRIVACY_POLICY_URL="https://duckduckgo.com/"
UBUNTU_CODENAME=noble
LOGO="armbian-logo"
ARMBIAN_PRETTY_NAME="Armbian_community 24.5.0-trunk.278 noble"
root@visionfive2:~# 
```

Xfce 版屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/pCI6icBzsw2UrqNN5kL20LUxH.svg)](https://asciinema.org/a/pCI6icBzsw2UrqNN5kL20LUxH)

Xfce 屏幕截图：

![alt text](image.png)

屏幕录像：

https://github.com/ruyisdk/support-matrix/assets/17025286/14c27bbd-5477-426b-a3e4-85cca5f5eabd

Minimal 版屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/kLOG9FnxGs9AnXpZqpjDJeiNo.svg)](https://asciinema.org/a/kLOG9FnxGs9AnXpZqpjDJeiNo)