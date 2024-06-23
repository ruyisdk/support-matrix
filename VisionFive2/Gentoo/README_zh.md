# Gentoo VisionFive 2 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：gentoo.img.bz2
- 下载链接：https://drive.google.com/file/d/10TDsk2FwZDJv3yJvDAfCam5Wf9ibS6Eg/view?usp=sharing
- 参考安装文档：https://forum.rvspace.org/t/experimental-gentoo-image/1807

> 此镜像为社区开发者提供，非官方镜像。

### 硬件信息

- StarFive VisionFive 2
- USB 电源适配器一个
- USB-A to C 或 C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 解压并刷写镜像到 microSD 卡

假定 `/dev/sdc` 为存储卡。

```bash
bzcat gentoo.img.bz2 | sudo dd of=/dev/sdc iflag=fullblock bs=4M status=progress
```

### 引导模式选择

StarFive VisionFive 2 提供了多种引导模式，可在上电前通过板载拨码开关进行配置；开发板本体上亦有丝印标注。

为了启动 Gentoo 镜像，可以选择 1-bit QSPI Nor Flash 模式（即：`RGPIO_0 = 0`, `RGPIO_1 = 0`）。注意，此模式可能需要提前更新 Flash 内的固件，若您启动不成功，请参考官方文档进行固件升级：[更新 SPL 和 U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)


### 登录系统

通过串口登录系统。

用户名：`root`
无密码。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```log
root@StarFive ~ # uname -a                                                                                                          
Linux StarFive 5.15.0-starfive #1 SMP Mon Feb 27 14:03:14 EST 2023 riscv64 GNU/Linux                                                
root@StarFive ~ # cat /etc/os-release                                                                                               
NAME=Gentoo                                                                                                                         
ID=gentoo                                                                                                                           
PRETTY_NAME="Gentoo Linux"                                                                                                          
ANSI_COLOR="1;32"                                                                                                                   
HOME_URL="https://www.gentoo.org/"                                                                                                  
SUPPORT_URL="https://www.gentoo.org/support/"                                                                                       
BUG_REPORT_URL="https://bugs.gentoo.org/"                                                                                           
VERSION_ID="2.13"                                                                                                                   
root@StarFive ~ #
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/HYfHc1I7NtPlUkfSuY7W1cy5e.svg)](https://asciinema.org/a/HYfHc1I7NtPlUkfSuY7W1cy5e)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。