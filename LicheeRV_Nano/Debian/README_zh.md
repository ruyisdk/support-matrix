# Debian LicheeRV Nano 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Initial Release
- 下载链接：https://github.com/Fishwaldo/sophgo-sg200x-debian
- 参考安装文档：https://github.com/Fishwaldo/sophgo-sg200x-debian

### 硬件信息

- LicheeRV Nano
- Type-C 电源线一根
- UART 转 USB 调试器一个

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡

下载镜像后进行解压和刷写：

```shell
lz4 -dk licheervnano_sd.img.lz4
sudo dd if=licheervnano_sd.img of=/dev/your_device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

| 用户名 | 密码 |
|--------|------|
| root   | rv   |
| debian | rv   |


## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，能够通过串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/d6uwAengdlXVbMj0KAdVbPhMX.svg)](https://asciinema.org/a/d6uwAengdlXVbMj0KAdVbPhMX)

```log
Debian GNU/Linux trixie/sid licheervnano ttyS0                                                                          
                                                                                                                        
licheervnano login: root                                                                                                
Password:                                                                                                               
Linux licheervnano 5.10.4-20240329-1+ #1 PREEMPT Sat Apr 13 07:08:27 UTC 2024 riscv64                                   
                                                                                                                        
The programs included with the Debian GNU/Linux system are free software;                                               
the exact distribution terms for each program are described in the                                                      
individual files in /usr/share/doc/*/copyright.                                                                         
                                                                                                                        
Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent                                                       
permitted by applicable law.                                                                                            
root@licheervnano:~# cat /proc/cpuinfo                                                                                  
processor       : 0                                                                                                     
hart            : 0                                                                                                     
isa             : rv64imafdvcsu                                                                                         
mmu             : sv39                                                                                                  
                                                                                                                        
root@licheervnano:~# cat /etc/os-release                                                                                
PRETTY_NAME="Debian GNU/Linux trixie/sid"                                                                               
NAME="Debian GNU/Linux"                                                                                                 
VERSION_CODENAME=trixie                                                                                                 
ID=debian                                                                                                               
HOME_URL="https://www.debian.org/"                                                                                      
SUPPORT_URL="https://www.debian.org/support"                                                                            
BUG_REPORT_URL="https://bugs.debian.org/"                                                                               
root@licheervnano:~# uname -a                                                                                           
Linux licheervnano 5.10.4-20240329-1+ #1 PREEMPT Sat Apr 13 07:08:27 UTC 2024 riscv64 GNU/Linux                         
root@licheervnano:~# 
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。