# openSUSE Tumbleweed HiFive Unmatched 测试报告

## 测试环境

### 操作系统信息

- 系统版本：openSUSE Tumbleweed
- 下载链接：https://download.opensuse.org/repositories/home:/Andreas_Schwab:/riscv:/unmatched/images/openSUSE-Tumbleweed-RISC-V-JeOS-hifiveunmatched.riscv64-2024.03.15-Build1.7.raw.xz
- 参考安装文档：https://en.opensuse.org/HCL:HiFive_Unmatched

### 硬件信息

- HiFive Unmatched Rev A
- microUSB 线缆一条（随 HiFive Unmatched 附赠）
- ATX 电源一个
- microSD 卡一张（Sandisk Extreme Pro 64G UHS-I）

## 安装步骤

### 引导设备选择

确保拨码开关已调整为从 microSD 卡引导。若您未更改，出厂默认即为从 microSD 卡引导。

拨码开关应如下设置：`MSEL[3:0]=1011`

### 解压并烧录镜像到 microSD 卡

`/dev/sdX` 为 microSD 卡所在位置，请根据实际情况更改。

```bash
xzcat openSUSE-Tumbleweed-RISC-V-JeOS-hifiveunmatched.riscv64-2024.03.15-Build1.7.raw.xz | sudo dd bs=4M of=/dev/sdX iflag=fullblock status=progress
```

### 登录系统

通过板载串口（使用 microUSB 线缆连接至其他计算机）登录系统。

默认用户名：`root`
默认密码：`linux`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
Welcome to openSUSE Tumbleweed 20240320 - Kernel 6.8.1-1-default (ttySIF0).                                                         
                                                                                                                                    
end0:                                                                                                                               
                                                                                                                                    
                                                                                                                                    
localhost login: root                                                                                                               
Password:                                                                                                                           
Have a lot of fun...                                                                                                                
stty: 'standard input': unable to perform all requested operations                                                                  
localhost:~ # cat /etc/os-release                                                                                                   
NAME="openSUSE Tumbleweed"                                                                                                          
# VERSION="20240320"                                                                                                                
ID="opensuse-tumbleweed"                                                                                                            
ID_LIKE="opensuse suse"                                                                                                             
VERSION_ID="20240320"                                                                                                               
PRETTY_NAME="openSUSE Tumbleweed"                                                                                                   
ANSI_COLOR="0;32"                                                                                                                   
# CPE 2.3 format, boo#1217921                                                                                                       
CPE_NAME="cpe:2.3:o:opensuse:tumbleweed:20240320:*:*:*:*:*:*:*"                                                                     
#CPE 2.2 format                                                                                                                     
#CPE_NAME="cpe:/o:opensuse:tumbleweed:20240320"                                                                                     
BUG_REPORT_URL="https://bugzilla.opensuse.org"                                                                                      
SUPPORT_URL="https://bugs.opensuse.org"                                                                                             
HOME_URL="https://www.opensuse.org"                                                                                                 
DOCUMENTATION_URL="https://en.opensuse.org/Portal:Tumbleweed"                                                                       
LOGO="distributor-logo-Tumbleweed"
localhost:~ # uname -a                                                                                                              
Linux localhost.localdomain 6.8.1-1-default #1 SMP PREEMPT_DYNAMIC Tue Mar 19 07:32:20 UTC 2024 (d922afa) riscv64 riscv64 riscv64 Gx
localhost:~ # 
```

屏幕录像（从刷写镜像到登录系统）

[![asciicast](https://asciinema.org/a/Yq2qb4xYNEMzUBxIcUkdyI2pp.svg)](https://asciinema.org/a/Yq2qb4xYNEMzUBxIcUkdyI2pp)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。