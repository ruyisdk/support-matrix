# BuildRoot Milk-V Duo S 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Duo-V1.1.3
- 下载链接：https://github.com/milkv-duo/duo-buildroot-sdk/releases
- 参考安装文档：https://github.com/milkv-duo/duo-buildroot-sdk

### 硬件信息

- Milk-V Duo S (512M, SG2000)
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条，用于给开发板供电
- microSD 卡一张
- USB 读卡器一个
- USB to UART 调试器一个（如：CP2102, FT2232 等，注意不可使用 CH340/341 系列，会出现乱码）
- 杜邦线三根

## 安装步骤

###  使用 `ruyi` CLI 刷写镜像到 microSD 卡

安装 [`ruyi`](https://github.com/ruyisdk/ruyi) 包管理器，运行 `ruyi device provision` 并按提示操作。

###  使用 `balenaEtcher` 刷写镜像到 microSD 卡
安装开源跨平台工具 `balenaEtcher` 进行刷写。

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口和ssh登录。

## 实际结果

系统正常启动，成功通过板载串口与ssh登录。

### 启动信息

> 出现 aic8800 insmod 失败是因为测试时使用的是不带 Wi-Fi 芯片的 Duo S。
> 
> 这是正常情况。

```log
Starting app...                                                                                                                     
                                                                                                                                    
[root@milkv-duo]~# insmod: can't insert '/mnt/system/ko/aic8800_fdrv.ko': No such device                                            
                                                                                                                                    
[root@milkv-duo]~#                                                                                                                  
[root@milkv-duo]~# uname -a                                                                                                         
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Mon Feb 26 16:01:35 CST 2024 riscv64 GNU/Linux                                               
[root@milkv-duo]~# cat /proc/cpuinfo                                                                                                
processor       : 0                                                                                                                 
hart            : 0                                                                                                                 
isa             : rv64imafdvcsu                                                                                                     
mmu             : sv39                                                                                                              
                                                                                                                                    
[root@milkv-duo]~# cat /etc/os-release                                                                                              
NAME=Buildroot                                                                                                                      
VERSION=20240226-1609                                                                                                               
ID=buildroot                                                                                                                        
VERSION_ID=2021.05                                                                                                                  
PRETTY_NAME="Buildroot 2021.05"                                                                                                     
[root@milkv-duo]~# 
```

屏幕录像（从刷写镜像到登录系统）：

[!asciinema](https://asciinema.org/a/y74COq4Da80mjhqZygoL7i97x)(https://asciinema.org/a/y74COq4Da80mjhqZygoL7i97x)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
