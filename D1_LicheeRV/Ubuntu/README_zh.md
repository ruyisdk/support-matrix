# Ubuntu 24.04 D1 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Ubuntu 24.04
- 下载链接：https://ubuntu.com/download/risc-v
    - 或者镜像站：[Nezha](https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/mantic/release/ubuntu-23.10-preinstalled-server-riscv64+nezha.img.xz) | [Lichee RV](https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/mantic/release/ubuntu-23.10-preinstalled-server-riscv64+licheerv.img.xz)
- 参考安装文档：https://wiki.ubuntu.com/RISC-V/LicheeRV

### 硬件信息

- AWOL Nezha D1 / Sipeed Lichee RV Dock
- USB-A 电源一个
- USB-A to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 刷写镜像到 microSD 卡

使用 `dd` 将镜像写入至 microSD 卡。

### 登录系统

通过串口登录系统。

默认用户名：`ubuntu`
默认密码：`ubuntu`

初次登录时，系统会提示更改密码。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
ubuntu@ubuntu:~$ cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : thead,c906
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/zwX03rXaG8pP6mQMDYuSzb0Eb.svg)](https://asciinema.org/a/zwX03rXaG8pP6mQMDYuSzb0Eb)
## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。