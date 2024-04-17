# openEuler RISC-V 23.09 LPi4A 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：openEuler 23.09 RISC-V preview
- 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/lpi4a/
- 参考安装文档：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/lpi4a/README.lpi4a.txt

### 硬件信息

- Lichee Pi 4A (16G RAM + 128G eMMC)
- USB-C 电源适配器 / DC 电源一个
- microSD 卡一张（Sandisk Extreme Pro 64G UHS-I）
- USB-UART 调试器一个

## 安装步骤

### 使用 `ruyi` CLI 刷写镜像到板载 eMMC

安装 [`ruyi`](https://github.com/ruyisdk/ruyi) 包管理器，运行 `ruyi device provision` 并按提示操作。

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
System load:    1.47                                                                                                                                                         
Processes:      130                                                                                                                                                          
Memory used:    .6%                                                                                                                                                          
Swap used:      0.0%                                                                                                                                                         
Usage On:       2%                                                                                                                                                           
IP address:     10.0.0.8                                                                                                                                                     
Users online:   1                                                                                                                                                            
To run a command as administrator(user "root"),use "sudo <command>".                                                                                                         
[openeuler@openeuler-riscv64 ~]$ cat /etc/os-release                                                                                                                         
NAME="openEuler"                                                                                                                                                             
VERSION="23.09"                                                                                                                                                              
ID="openEuler"                                                                                                                                                               
VERSION_ID="23.09"                                                                                                                                                           
PRETTY_NAME="openEuler 23.09"                                                                                                                                                
ANSI_COLOR="0;31"                                                                                                                                                            
                                                                                                                                                                             
[openeuler@openeuler-riscv64 ~]$ uname -a                                                                                                                                    
Linux openeuler-riscv64 5.10.113 #1 SMP PREEMPT Wed Nov 22 16:04:58 UTC 2023 riscv64 riscv64 riscv64 GNU/Linux
[openeuler@openeuler-riscv64 ~]$ cat /proc/cpuinfo                                                                                                                           
processor       : 0                                                                                                                                                          
hart            : 0                                                                                                                                                          
isa             : rv64imafdcvsu                                                                                                                                              
mmu             : sv39                                                                                                                                                       
cpu-freq        : 1.848Ghz                                                                                                                                                   
cpu-icache      : 64KB                                                                                                                                                       
cpu-dcache      : 64KB                                                                                                                                                       
cpu-l2cache     : 1MB                                                                                                                                                        
cpu-tlb         : 1024 4-ways                                                                                                                                                
cpu-cacheline   : 64Bytes                                                                                                                                                    
cpu-vector      : 0.7.1                                                                                                                                                      
                                                                                                                                                                             
processor       : 1                                                                                                                                                          
hart            : 1                                                                                                                                                          
isa             : rv64imafdcvsu                                                                                                                                              
mmu             : sv39                                                                                                                                                       
cpu-freq        : 1.848Ghz                                                                                                                                                   
cpu-icache      : 64KB                                                                                                                                                       
cpu-dcache      : 64KB                                                                                                                                                       
cpu-l2cache     : 1MB                                                                                                                                                        
cpu-tlb         : 1024 4-ways                                                                                                                                                
cpu-cacheline   : 64Bytes                                                                                                                                                    
cpu-vector      : 0.7.1                                                                                                                                                      
                                                                                                                                                                             
processor       : 2                                                                                                                                                          
hart            : 2                                                                                                                                                          
isa             : rv64imafdcvsu                                                                                                                                              
mmu             : sv39                                                                                                                                                       
cpu-freq        : 1.848Ghz                                                                                                                                                   
cpu-icache      : 64KB                                                                                                                                                       
cpu-dcache      : 64KB                                                                                                                                                       
cpu-l2cache     : 1MB                                                                                                                                                        
cpu-tlb         : 1024 4-ways                                                                                                                                                
cpu-cacheline   : 64Bytes                                                                                                                                                    
cpu-vector      : 0.7.1                                                                                                                                                      
                                                                                                                                                                             
processor       : 3                                                                                                                                                          
hart            : 3                                                                                                                                                          
isa             : rv64imafdcvsu                                                                                                                                              
mmu             : sv39                                                                                                                                                       
cpu-freq        : 1.848Ghz                                                                                                                                                   
cpu-icache      : 64KB                                                                                                                                                       
cpu-dcache      : 64KB                                                                                                                                                       
cpu-l2cache     : 1MB                                                                                                                                                        
cpu-tlb         : 1024 4-ways                                                                                                                                                
cpu-cacheline   : 64Bytes                                                                                                                                                    
cpu-vector      : 0.7.1 
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/oXGHqeiBmb0n5zIKHnbGnnRb2.svg)](https://asciinema.org/a/oXGHqeiBmb0n5zIKHnbGnnRb2)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。