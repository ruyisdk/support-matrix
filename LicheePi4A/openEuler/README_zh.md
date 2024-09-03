# openEuler RISC-V 24.03 LPi4A 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：openEuler 24.03 RISC-V preview
- 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/testing/2403LTS-test/v1/lpi4a/
- 参考安装文档：https://docs.openeuler.org/zh/docs/24.03_LTS/docs/Installation/RISC-V-LicheePi4A.html

### 硬件信息

- Lichee Pi 4A (8G RAM + 32G eMMC)
- USB-C 电源适配器 / DC 电源一个
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
Welcome to 6.6.0

System information as of time:  Thu Jan  1 08:00:22 AM CST 1970

System load:    2.07
Processes:      191
Memory used:    3.0%
Swap used:      0.0%
Usage On:       13%
Users online:   1

[openeuler@openeuler-riscv64 ~]$ cat /etc/os-release                                                                                                                         
NAME="openEuler"
VERSION="24.03 (LTS)"
ID="openEuler"
VERSION_ID="24.03"
PRETTY_NAME="openEuler 24.03 (LTS)"
ANSI_COLOR="0;31"
                                                                                                                                                                             
[openeuler@openeuler-riscv64 ~]$ uname -a
Linux openeuler-riscv64 6.6.0 #1 SMP Tue Apr  9 02:46:40 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux

[openeuler@openeuler-riscv64 ~]$ cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 1
hart            : 0
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 2
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 3
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/oXGHqeiBmb0n5zIKHnbGnnRb2.svg)](https://asciinema.org/a/oXGHqeiBmb0n5zIKHnbGnnRb2)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。