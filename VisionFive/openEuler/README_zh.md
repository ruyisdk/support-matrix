# openEuler RISC-V 23.09 VisionFive 测试报告

## 测试环境

### 操作系统信息

- 系统版本：openEuler 23.09 RISC-V preview
- 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Visionfive/
- 参考安装文档：https://gitee.com/openeuler/RISC-V/tree/master/release/openEuler-23.03/Installation_Book/Visionfive

### 硬件信息

- StarFive VisionFive
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 使用 `ruyi` CLI 刷写镜像到 microSD 卡

安装 [`ruyi`](https://github.com/ruyisdk/ruyi) 包管理器，运行 `ruyi device provision` 并按提示操作。

### 登录系统

通过串口登录系统。

默认用户名：`openeuler`
默认密码：`openEuler12#$`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/lkduJVcErVoqb3ewZuzjl4TVi.svg)](https://asciinema.org/a/lkduJVcErVoqb3ewZuzjl4TVi)

```log
Welcome to 6.1.0-0.rc4.8.oe2309.riscv64

System information as of time:  Mon Sep 18 08:01:36 AM CST 2023

System load:    2.62
Processes:      120
Memory used:    2.4%
Swap used:      0.0%
Usage On:       4%
Users online:   1
To run a command as administrator(user "root"),use "sudo <command>".
[openeuler@openeuler-riscv64 ~]$ uname -a
Linux openeuler-riscv64 6.1.0-0.rc4.8.oe2309.riscv64 #1 SMP Fri Oct 20 08:23:28 UTC 2023 riscv64 riscv64 riscv64 GNU/Linux
[openeuler@openeuler-riscv64 ~]$ cat /etc/os-release 
NAME="openEuler"
VERSION="23.09"
ID="openEuler"
VERSION_ID="23.09"
PRETTY_NAME="openEuler 23.09"
ANSI_COLOR="0;31"

[openeuler@openeuler-riscv64 ~]$ 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
