# Alpine Linux VisionFive 2 测试报告

## 测试环境

### 操作系统信息

- 系统版本：3.20.0_alpha20231219 (edge)
- 下载链接：https://dev.alpinelinux.org/~mps/riscv64/visionfive-v2-mmc.img.xz
- 参考安装文档：https://arvanta.net/alpine/alpine-on-visionfive/

### 硬件信息

- StarFive VisionFive 2
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `xz` 解压镜像。
使用 `dd` 或`balenaEtcher`等工具将镜像写入 microSD 卡

```bash
xz -d visionfive-v2-mmc.img.xz
dd if=visionfive-v2-mmc.img of=/dev/<your-device> 
```

### 引导模式选择

StarFive VisionFive 2 提供了多种引导模式，可在上电前通过板载拨码开关进行配置，可参考 StarFive [官方文档](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_SDK_QSG/boot_mode_settings.html)。

开发板本体上亦有丝印标注。

为了启动 Alpine 镜像，选择 SDIO3.0 模式（即：`RGPIO_0 = 1`, `RGPIO_1 = 0`）。

### 登录系统

通过串口登录系统。

直接登录到 root,无密码。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```log

Welcome to Alpine Linux 3.20.0_alpha20231219 (edge)
Kernel 6.7.4-0-starfive on an riscv64 (ttyS0)

[press ENTER to login]
localhost login: root (automatic login)

Welcome to Alpine!

The Alpine Wiki contains a large amount of how-to guides and general
information about administrating Alpine systems.
See <https://wiki.alpinelinux.org/>.

You can setup the system with the command: setup-alpine

You may change this message by editing /etc/motd.

localhost:~# uname -a
Linux localhost 6.7.4-0-starfive #1-Alpine SMP PREEMPT_DYNAMIC Tue, 06 Feb 2024 12:21:03 +0000 riscv64 Linux
localhost:~# [   12.258155] mmc0: Failed to initialize a non-removable card
[   22.005472] platform 16000000.crypto: deferred probe pending

localhost:~# cat /etc/os-release 
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.20.0_alpha20231219
PRETTY_NAME="Alpine Linux edge"
HOME_URL="https://alpinelinux.org/"
BUG_REPORT_URL="https://gitlab.alpinelinux.org/alpine/aports/-/issues"
localhost:~# 

``` 

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
