# openEuler RISC-V 23.03 AWOL Nezha D1 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：openEuler 23.03 RISC-V preview
- 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.03-V1-riscv64/D1/
- 参考安装文档：https://gitee.com/openeuler/RISC-V/tree/master/release/openEuler-23.03/Installation_Book/D1_and_Licheerv

> [!NOTE]
> 此镜像为使用 BSP 内核的老版本，来自 openEuler RISC-V SIG 组。
> oERV SIG 正在开发新版本；截止目前为止，经测试，这是最后已知可在 D1 实机启动的镜像。
> 更多信息请见 [此处](https://github.com/ruyisdk/support-matrix/issues/228#issuecomment-2785789283)。

### 硬件信息

- AWOL Nezha D1 
- USB-A 电源一个
- USB-A to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 使用 `ruyi` CLI 刷写镜像到 microSD 卡

安装 [`ruyi`](https://github.com/ruyisdk/ruyi) 包管理器，运行 `ruyi device provision` 并按提示操作。

### 登录系统

通过串口登录系统。

默认用户名：`openeuler` 或 `root`
默认密码：`openEuler12#$`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
openEuler 23.03                                                                                                                                   
Kernel 6.1.0-0.rv64                                                                                                                               
                                                                                                                                                  
openeuler-riscv64 login: c3.11.oe2303.riscv64 on an riscv64                                                                                       
                                                                                                                                                  
openeuler-riscv64 login: root                                                                                                                     
Password: [   57.563173] EXT4-fs (mmcblk0p4): resized filesystem to 15498496                                                                      
                                                                                                                                                  
                                                                                                                                                  
                                                                                                                                                  
Welcome to 6.1.0-0.rc3.11.oe2303.riscv64                                                                                                          
                                                                                                                                                  
System information as of time:  Fri Jan  2 08:01:41 CST 1970                                                                                      
                                                                                                                                                  
System load:    3.42                                                                                                                              
Processes:      93                                                                                                                                
Memory used:    6.8%                                                                                                                              
Swap used:      0.0%                                                                                                                              
Usage On:       2%                                                                                                                                
Users online:   1                                                                                                                                 
                                                                                                                                                  
                                                                                                                                                  
[root@openeuler-riscv64 ~]# cat /proc/cpuinfo                                                                                                     
processor       : 0                                                                                                                               
hart            : 0                                                                                                                               
isa             : rv64imafdc                                                                                                                      
mmu             : sv39                                                                                                                            
uarch           : thead,c906                                                                                                                      
mvendorid       : 0x5b7                                                                                                                           
marchid         : 0x0                                                                                                                             
mimpid          : 0x0                                                                                                                             
                                                                                                                                                  
[root@openeuler-riscv64 ~]#
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/dJV431qjqOPT6iR7hzieM3G41.svg)](https://asciinema.org/a/dJV431qjqOPT6iR7hzieM3G41)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
