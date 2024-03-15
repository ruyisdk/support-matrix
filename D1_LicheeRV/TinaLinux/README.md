# Tina Linux D1 测试报告

## 测试环境

### 操作系统信息

- 系统版本：D1-H 哪吒 HDMI 测试固件 20210804
- 下载链接：
    - Nezha D1: https://d1.docs.aw-ol.com/source/3_getimg/
- 参考安装文档：
    - Nezha D1: https://d1.docs.aw-ol.com/study/study_1tina/

### 硬件信息

- AWOL Nezha D1
- USB-A 电源一个
- USB-A to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 刷写镜像到 microSD 卡

使用 `dd` 刷入镜像到 microSD 卡。

```bash
sudo dd if=D1-H哪吒HDMI测试固件20210804（开机HDMI就有小企鹅启动logo）.img of=/dev/sdc status=progress 
```

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
BusyBox v1.27.2 () built-in shell (ash)                                                                               
                                                                                                                      
 _____  _              __     _                                                                                       
|_   _||_| ___  _ _   |  |   |_| ___  _ _  _ _                                                                        
  | |   _ |   ||   |  |  |__ | ||   || | ||_'_|                                                                       
  | |  | || | || _ |  |_____||_||_|_||___||_,_|                                                                       
  |_|  |_||_|_||_|_|  Tina is Based on OpenWrt!                                                                       
 ----------------------------------------------                                                                       
 Tina Linux (Neptune, 5C1C9C53)                                                                                       
 ----------------------------------------------                                                                       
root@TinaLinux:/# cat /proc/cpuinfo                                                                                   
processor       : 0                                                                                                   
hart            : 0                                                                                                   
isa             : rv64imafdcvu                                                                                        
mmu             : sv39                                                                                                
                                                                                                                      
root@TinaLinux:/# uname -a                                                                                            
Linux TinaLinux 5.4.61 #49 PREEMPT Wed Apr 28 09:23:43 UTC 2021 riscv64 GNU/Linux                                     
root@TinaLinux:/#
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/WSlC5RUcJFYH6hZnjxZYwqPtk.svg)](https://asciinema.org/a/WSlC5RUcJFYH6hZnjxZYwqPtk)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。