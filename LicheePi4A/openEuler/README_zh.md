# openEuler RISC-V 24.03 LPi4A 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：openEuler 24.03 RISC-V LTS
- 下载链接：https://www.openeuler.org/zh/download/?version=openEuler%2024.03%20LTS
- 参考安装文档：https://docs.openeuler.org/zh/docs/24.03_LTS/docs/Installation/RISC-V-LicheePi4A.html

### 硬件信息

- Lichee Pi 4A (16G RAM + 128G eMMC)
- USB-C 电源适配器 / DC 电源一个
- USB-UART 调试器一个

## 安装步骤

### 下载并解压镜像

从 [官网](https://www.openeuler.org/zh/download/?version=openEuler%2024.03%20LTS) 下载镜像：

选择 `RISC-V - 嵌入式 - lpi4a`。

### 使用 `fastboot` 刷写镜像到板载 eMMC

由于 LPi4A 默认的 USB VID/PID 通常不在默认 udev 规则内，在 Linux 下烧写时可能需要在 `fastboot` 前添加 `sudo`。

按住板上的 **BOOT** 按键不放，然后插入 USB-C 线缆上电（线缆另一头接 PC），即可进入 USB 烧录模式。

在 Windows 下使用设备管理器查看，会出现 `USB download gadget` 设备。

在 Linux 下，使用 `lsusb` 查看设备，会显示以下设备：`ID 2345:7654 T-HEAD USB download gadget`。

使用如下指令刷写镜像。

```shell
fastboot flash ram u-boot-with-spl-lpi4a-16g.bin
fastboot reboot
# 稍等几秒，等待开发板重启后重新连接至电脑
fastboot flash uboot u-boot-with-spl-lpi4a-16g.bin
fastboot flash boot openEuler-24.03-LTS-riscv64-lpi4a-base-boot.ext4
fastboot flash root openEuler-24.03-LTS-riscv64-lpi4a-base-root.ext4
```

### 登录系统

通过串口登录系统。

默认用户名：`openeuler` 或 `root`
默认密码：`openEuler12#$`

## 预期结果

系统正常启动，能够通过串口登录。

若接入网络，可通过 SSH 登录。

## 实际结果

系统正常启动，成功通过串口或 SSH 登录。

### 启动信息

```log
Welcome to 6.6.0-27.0.0.31.oe2403.riscv64                                                                               
                                                                                                                        
System information as of time:  Thu Sep  5 18:03:57 CST 2024                                                            
                                                                                                                        
System load:    2.50                                                                                                    
Memory used:    1.2%                                                                                                    
Swap used:      0.0%                                                                                                    
Usage On:       2%                                                                                                      
IP address:     10.0.0.8                                                                                                
Users online:   1                                                                                                       
To run a command as administrator(user "root"),use "sudo <command>".                                                    
[openeuler@openeuler-riscv64 ~]$ cat /etc/os-release                                                                    
NAME="openEuler"                                                                                                        
VERSION="24.03 (LTS)"                                                                                                   
ID="openEuler"                                                                                                          
VERSION_ID="24.03"                                                                                                      
PRETTY_NAME="openEuler 24.03 (LTS)"                                                                                     
ANSI_COLOR="0;31"                                                                                                       
                                                                                                                        
[openeuler@openeuler-riscv64 ~]$ uname -a                                                                               
Linux openeuler-riscv64 6.6.0-27.0.0.31.oe2403.riscv64 #1 SMP Fri May 24 21:52:58 CST 2024 riscv64 riscv64 riscv64 GNU/Linux
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/Jo6gwkRgaOBAeXgbwIuK4OWel.svg)](https://asciinema.org/a/Jo6gwkRgaOBAeXgbwIuK4OWel)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。