# Arch Linux VisionFive 2 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：ArchLinux-VF2_5.15.2_v5.11.3-cwt21.1.img.xz
- 下载链接：https://github.com/cwt-vf2/archlinux-image-vf2/releases/tag/cwt21.1
- 参考安装文档：https://forum.rvspace.org/t/arch-linux-image-for-visionfive-2/1459

> 此镜像为社区开发者提供，非官方镜像。Arch Linux RISC-V 目前仅提供 `rootfs`。

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
xzcat ArchLinux-VF2_5.15.2_v5.11.3-cwt21.1.img.xz | sudo dd of=/dev/sdc iflag=fullblock bs=4M status=progress
```

### 引导模式选择

StarFive VisionFive 2 提供了多种引导模式，可在上电前通过板载拨码开关进行配置；开发板本体上亦有丝印标注。

为了启动 Arch 镜像，可以选择 1-bit QSPI Nor Flash 模式（即：`RGPIO_0 = 0`, `RGPIO_1 = 0`）。注意，此模式可能需要提前更新 Flash 内的固件，若您启动不成功，请参考官方文档进行固件升级：[更新 SPL 和 U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)


### 登录系统

通过串口登录系统。

用户名：`root`
默认密码：`archriscv`

或者

用户名：`user`
密码：`user`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```log
Arch Linux 5.2-cwt-5.11.3-2 (hvc0)                                                                                                  
                                                                                                                                    
ArchVF2 login: 15.2-cwt-5.11.3-2 (ttyS0)                                                                                            
                                                                                                                                    
ArchVF2 login: root                                                                                                                 
Password:                                                                                                                           
Login incorrect                                                                                                                     
                                                                                                                                    
ArchVF2 login: root                                                                                                                 
Password:                                                                                                                           
[root@ArchVF2 ~]# uname -a                                                                                                          
Linux ArchVF2 5.15.2-cwt-5.11.3-2 #1 SMP PREEMPT Fri Mar 22 19:02:42 +07 2024 riscv64 GNU/Linux                                     
[root@ArchVF2 ~]# cat /etc/os-release                                                                                               
NAME="Arch Linux"                                                                                                                   
PRETTY_NAME="Arch Linux"                                                                                                            
ID=arch                                                                                                                             
BUILD_ID=rolling                                                                                                                    
ANSI_COLOR="38;2;23;147;209"                                                                                                        
HOME_URL="https://archlinux.org/"                                                                                                   
DOCUMENTATION_URL="https://wiki.archlinux.org/"                                                                                     
SUPPORT_URL="https://bbs.archlinux.org/"                                                                                            
BUG_REPORT_URL="https://gitlab.archlinux.org/groups/archlinux/-/issues"                                                             
PRIVACY_POLICY_URL="https://terms.archlinux.org/docs/privacy-policy/"                                                               
LOGO=archlinux-logo                                                                                                                 
[root@ArchVF2 ~]# 
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/X6MYCn6vv0n6Es38KHhC1uOmc.svg)](https://asciinema.org/a/X6MYCn6vv0n6Es38KHhC1uOmc)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。