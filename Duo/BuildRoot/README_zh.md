# BuildRoot Milk-V Duo 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Duo-V1.0.7
- 下载链接：https://github.com/milkv-duo/duo-buildroot-sdk/releases
- 参考安装文档：https://github.com/milkv-duo/duo-buildroot-sdk

### 硬件信息

- Milk-V Duo 64M
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根
- Milk-V Duo 本体上预先焊接好调试所需的排针

## 安装步骤

### 使用 `ruyi` CLI 刷写镜像到 microSD 卡

安装 [`ruyi`](https://github.com/ruyisdk/ruyi) 包管理器，运行 `ruyi device provision` 并按提示操作。

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
[root@milkv-duo]~# uname -a                                                                                                                                             
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Sat Dec 23 12:29:13 CST 2023 riscv64 GNU/Linux                                                                                   
[root@milkv-duo]~# cat /proc/cpuinfo                                                                                                                                    
processor       : 0                                                                                                                                                     
hart            : 0                                                                                                                                                     
isa             : rv64imafdvcsu                                                                                                                                         
mmu             : sv39                                                                                                                                                  
                                                                                                                                                                        
[root@milkv-duo]~# 
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/rsenSOJwdlmUXcJ8sQwubPgtr.svg)](https://asciinema.org/a/rsenSOJwdlmUXcJ8sQwubPgtr)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。