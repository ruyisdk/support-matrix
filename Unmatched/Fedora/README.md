# Fedora 38 HiFive Unmatched 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Fedora 38
- 下载链接：https://dl.fedoraproject.org/pub/alt/risc-v/disk_images/Fedora-Developer-38-20230519.n.0.SiFive.Unmatched.and.QEMU/Fedora-Developer-38-20230519.n.0-mmc.raw.img.xz
- 参考安装文档：https://dl.fedoraproject.org/pub/alt/risc-v/disk_images/Fedora-Developer-38-20230519.n.0.SiFive.Unmatched.and.QEMU/README.md

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

`/dev/sdc` 为 microSD 卡所在位置，请根据实际情况更改。

```bash
sudo wipefs -af /dev/sdc
xzcat Fedora-Developer-38-20230519.n.0-mmc.raw.img.xz | sudo dd of=/dev/sdc iflag=fullblock bs=4M status=progress
```

### 登录系统

通过板载串口（使用 microUSB 线缆连接至其他计算机）登录系统。

默认用户名：`riscv` 或 `root`
默认密码：`fedora_rocks!`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息


```log
https://fedoraproject.org/wiki/Architectures/RISC-V                                                                                 
                                                                                                                                    
Build date: Fri May 19 12:44:23 UTC 2023                                                                                            
                                                                                                                                    
Kernel 6.2.16-300.0.riscv64.fc38.riscv64 on an riscv64 (ttySIF0)                                                                    
                                                                                                                                    
The root password is 'fedora_rocks!'.                                                                                               
root password logins are disabled in SSH starting Fedora 31.                                                                        
User 'riscv' with password 'fedora_rocks!' in 'wheel' group is provided.                                                            
                                                                                                                                    
To install new packages use 'dnf install ...'                                                                                       
                                                                                                                                    
To upgrade disk image use 'dnf upgrade --best'                                                                                      
                                                                                                                                    
If DNS isn’t working, try editing ‘/etc/yum.repos.d/fedora-riscv.repo’.                                                             
                                                                                                                                    
For updates and latest information read:                                                                                            
https://fedoraproject.org/wiki/Architectures/RISC-V                                                                                 
                                                                                                                                    
Fedora/RISC-V                                                                                                                       
-------------                                                                                                                       
Koji:               http://fedora.riscv.rocks/koji/                                                                                 
SCM:                http://fedora.riscv.rocks:3000/                                                                                 
Distribution rep.:  http://fedora.riscv.rocks/repos-dist/                                                                           
Koji internal rep.: http://fedora.riscv.rocks/repos/                                                                                
fedora-riscv login: root                                                                                                            
Password:                                                                                                                           
Login incorrect                                                                                                                     
                                                                                                                                    
fedora-riscv login: root                                                                                                            
Password:                                                                                                                           
Login incorrect 

fedora-riscv login: root                                                                                                            
Password:                                                                                                                           
Last failed login: Wed May 10 20:04:31 EDT 2023 on ttySIF0                                                                          
There were 2 failed login attempts since the last successful login.                                                                 
[root@fedora-riscv ~]# cat /etc/os-release                                                                                          
NAME="Fedora Linux"                                                                                                                 
VERSION="38 (Thirty Eight)"                                                                                                         
ID=fedora                                                                                                                           
VERSION_ID=38                                                                                                                       
VERSION_CODENAME=""                                                                                                                 
PLATFORM_ID="platform:f38"                                                                                                          
PRETTY_NAME="Fedora Linux 38 (Thirty Eight)"                                                                                        
ANSI_COLOR="0;38;2;60;110;180"                                                                                                      
LOGO=fedora-logo-icon                                                                                                               
CPE_NAME="cpe:/o:fedoraproject:fedora:38"                                                                                           
DEFAULT_HOSTNAME="fedora"                                                                                                           
HOME_URL="https://fedoraproject.org/"                                                                                               
DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora/f38/system-administrators-guide/"                                    
SUPPORT_URL="https://ask.fedoraproject.org/"                                                                                        
BUG_REPORT_URL="https://bugzilla.redhat.com/"                                                                                       
REDHAT_BUGZILLA_PRODUCT="Fedora"                                                                                                    
REDHAT_BUGZILLA_PRODUCT_VERSION=38                                                                                                  
REDHAT_SUPPORT_PRODUCT="Fedora"                                                                                                     
REDHAT_SUPPORT_PRODUCT_VERSION=38                                                                                                   
SUPPORT_END=2024-05-14                                                                                                              
[root@fedora-riscv ~]#
```

屏幕录像（从刷写镜像到登录系统）

[![asciicast](https://asciinema.org/a/vulbDuQBEkAx4ldcquyMpVR2m.svg)](https://asciinema.org/a/vulbDuQBEkAx4ldcquyMpVR2m)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
