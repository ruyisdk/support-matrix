# Ubuntu 23.10 VisionFive 2 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：Ubuntu 24.04
- 下载链接：https://cdimage.ubuntu.com/releases/noble/release/ubuntu-24.04-preinstalled-server-riscv64+nezha.img.xz?
- 参考安装文档：https://wiki.ubuntu.com/RISC-V/Nezha%20D1?

### 硬件信息

- D1s NeZha
- USB-A to C 或 C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 解压并刷写镜像到 microSD 卡

假定 `/dev/sdc` 为存储卡。

```bash
xz -d ubuntu-24.04-preinstalled-server-riscv64+licheerv.img.xz
sudo dd if=ubuntu-24.04-preinstalled-server-riscv64+licheerv.img of=/dev/sdc bs=1m status=progress
```

### 登录系统

通过串口登录系统。

默认用户名：`ubuntu`
默认密码：`ubuntu`

初次登录时，会提示更改默认密码。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。


屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/gPmHuofP650Kl9mTp8xLk1tod.svg)](https://asciinema.org/a/gPmHuofP650Kl9mTp8xLk1tod)

### 启动信息

```log
ubuntu@ubuntu:~$ cat /proc/cpuinfo                                              processor       : 0                                                             hart            : 0                                                             isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm                        mmu             : sv39                                                          uarch           : thead,c906                                                    mvendorid       : 0x5b7                                                         marchid         : 0x0                                                           mimpid          : 0x0                                                           hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm
```
## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。