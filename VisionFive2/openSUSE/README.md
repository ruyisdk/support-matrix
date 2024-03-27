# openSUSE Tumbleweed VisionFive 2 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：openSUSE-Tumbleweed-RISC-V-JeOS-starfivevisionfive2.riscv64-2024.03.15-Build23.14.raw.xz
- 下载链接：https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/StarFive:/VisionFive2/images/
- 参考安装文档：https://en.opensuse.org/HCL:VisionFive2

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
xzcat openSUSE-Tumbleweed-RISC-V-JeOS-starfivevisionfive2.riscv64-2024.03.15-Build23.14.raw.xz | sudo dd of=/dev/sdc iflag=fullblock status=progress bs=4M
```

### 引导模式选择

StarFive VisionFive 2 提供了多种引导模式，可在上电前通过板载拨码开关进行配置；开发板本体上亦有丝印标注。

为了启动 openSUSE 镜像，需要选择 microSD 卡引导模式（即：`RGPIO_0 = 1`, `RGPIO_1 = 0`）。

> 注意，此模式下有小概率出现启动失败的情况，如遇到启动失败，串口输出类似如下信息：
>
>```log
>dwmci_s: Response Timeout.                                                                                            
>dwmci_s: Response Timeout.                                                                                            
>BOOT fail,Error is 0xffffffff
>```
>
> 您可以尝试重新给开发板上电，或点按一下 USB Type-C 供电接口附近的按钮。通常这可以解决无法启动的问题。


### 登录系统

通过串口登录系统。

用户名：`root`
默认密码：`linux`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```log
Welcome to openSUSE Tumbleweed 20240322 - Kernel 6.8.1-85-default (ttyS0).                                                          
                                                                                                                                    
end0:  fe80::ecba:cd3:320d:39f8                                                                                                     
end1:                                                                                                                               
                                                                                                                                    
                                                                                                                                    

localhost login: root                                                                                                               
Password:                                                                                                                           
Have a lot of fun...                                                                                                                
localhost:~ # uname -a                                                                                                              
Linux localhost.localdomain 6.8.1-85-default #1 SMP PREEMPT_DYNAMIC Fri Mar 22 07:05:00 UTC 2024 (c838682) riscv64 riscv64 riscv64 x
localhost:~ # cat /etc/os-release                                                                                                   
NAME="openSUSE Tumbleweed"                                                                                                          
# VERSION="20240322"                                                                                                                
ID="opensuse-tumbleweed"                                                                                                            
ID_LIKE="opensuse suse"                                                                                                             
VERSION_ID="20240322"                                                                                                               
PRETTY_NAME="openSUSE Tumbleweed"                                                                                                   
ANSI_COLOR="0;32"                                                                                                                   
# CPE 2.3 format, boo#1217921                                                                                                       
CPE_NAME="cpe:2.3:o:opensuse:tumbleweed:20240322:*:*:*:*:*:*:*"                                                                     
#CPE 2.2 format                                                                                                                     
#CPE_NAME="cpe:/o:opensuse:tumbleweed:20240322"                                                                                     
BUG_REPORT_URL="https://bugzilla.opensuse.org"                                                                                      
SUPPORT_URL="https://bugs.opensuse.org"                                                                                             
HOME_URL="https://www.opensuse.org"                                                                                                 
DOCUMENTATION_URL="https://en.opensuse.org/Portal:Tumbleweed"                                                                       
LOGO="distributor-logo-Tumbleweed"                                                                                                  
localhost:~ # 
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/z3xt9HGtT5iVtI7tbtQNi9rHf.svg)](https://asciinema.org/a/z3xt9HGtT5iVtI7tbtQNi9rHf)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。

