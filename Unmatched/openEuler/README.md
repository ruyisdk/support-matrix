# openEuler RISC-V 23.09 HiFive Unmatched 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：openEuler 23.09 RISC-V preview
- 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Unmatched/
- 参考安装文档：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Unmatched/README.unmatched.txt

### 硬件信息

- HiFive Unmatched Rev A
- microUSB 线缆一条（随 HiFive Unmatched 附赠）
- ATX 电源一个
- microSD 卡一张（Sandisk Extreme Pro 64G UHS-I）

## 安装步骤

### 引导设备选择

确保拨码开关已调整为从 microSD 卡引导。若您未更改，出厂默认即为从 microSD 卡引导。

拨码开关应如下设置：`MSEL[3:0]=1011`

### 使用 `ruyi` CLI 刷写镜像到 microSD 卡

安装 [`ruyi`](https://github.com/ruyisdk/ruyi) 包管理器，运行 `ruyi device provision` 并按提示操作。

### 登录系统

通过板载串口（使用 microUSB 线缆连接至其他计算机）登录系统。

默认用户名：`openeuler` 或 `root`
默认密码：`openEuler12#$`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
Welcome to 6.1.0-11.oe2309.riscv64                                                                                    
                                                                                                                      
System information as of time:  Mon Sep 18 08:03:17 AM CST 2023                                                       
                                                                                                                      
System load:    1.94                                                                                                  
Processes:      130                                                                                                   
Memory used:    1.2%                                                                                                  
Swap used:      0.0%                                                                                                  
Usage On:       16%                                                                                                   
Users online:   1                                                                                                     
To run a command as administrator(user "root"),use "sudo <command>".                                                  
[openeuler@openeuler-riscv64 ~]$
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/GzU3kCzrnvFfJMU1cJH30knrx.svg)](https://asciinema.org/a/GzU3kCzrnvFfJMU1cJH30knrx)