# Gentoo MangoPi MQ Pro 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/RevySR/riscv-calculate/releases/download/v20220929/gentoo-d1-20220929153235.img.zst
- 参考安装文档：https://github.com/RevySR/riscv-calculate

> Note: 此镜像为社区开发者提供，非官方镜像。

### 硬件信息

- MangoPi MQ Pro
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `zstd` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
zstd -d gentoo-d1-20220929153235.img.zst
sudo dd if=/path/to/gentoo-d1-20220929153235.img.zst of=/dev/your_device bs=1M status=progress
```

### 登录系统

注意 Type-C 电源线应插入板子的 OTG 接口而不是 Host 接口，以避免出现供电不稳；参见 https://forums.100ask.net/t/topic/876/6。

通过串口登录系统。

默认用户名：`root`
默认密码：`Riscv2022#`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，能够通过板载串口登录。

### 启动信息

```log
[   31.849891] fbcon: Taking over console


This is gentoo-riscv.unknown_doma

This is gentooin (Linux riscv64-riscv.unknown_d 5.19.0-rc1-gfe178cf0153d-dirty) 09:10:30

gentoo-riscv login: omain (Linux riscv64 5.19.0-rc1-gfe178cf0153d-dirty) 09:10:30

gentoo-riscv login: root
Password: 

root@gentoo-riscv ~ # uname -a
Linux gentoo-riscv 5.19.0-rc1-gfe178cf0153d-dirty #1 PREEMPT Thu Sep 29 15:28:12 UTC 2022 riscv64 GNU/Linux
root@gentoo-riscv ~ # ls
root@gentoo-riscv ~ # cat /etc/os-release 
NAME=Gentoo
ID=gentoo
PRETTY_NAME="Gentoo Linux"
ANSI_COLOR="1;32"
HOME_URL="https://www.gentoo.org/"
SUPPORT_URL="https://www.gentoo.org/support/"
BUG_REPORT_URL="https://bugs.gentoo.org/"
VERSION_ID="2.9"

root@gentoo-riscv ~ # portageq  --help
>>> Portage information query tool
>>> 3.0.37
>>> Usage: portageq <command> [<option> ...]

```
## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。