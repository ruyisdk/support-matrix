# NixOS MangoPi MQ Pro 测试报告

## 测试环境

### 操作系统信息

- 系统版本：22.11.20221014
- 下载链接: https://github.com/chuangzhu/nixos-sun20iw1p1/releases/download/hdmi/nixos-sd-image-22.11.20221014.4428e23-riscv64-linux.img.zst
- 参考安装文档: https://github.com/chuangzhu/nixos-sun20iw1p1

### 硬件信息

- MangoPi MQ Pro
- USB-A 电源一个
- USB-A to C 线缆一条
- microSD 卡一张
- microSD 读卡器一个
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 解压并刷写镜像到 microSD 卡

```shell
zstd -d https://github.com/chuangzhu/nixos-sun20iw1p1/releases/download/hdmi/nixos-sd-image-22.11.20221014.4428e23-riscv64-linux.img.zst
dd if=/path/to/your/nixos-sd-image-22.11.20221014.4428e23-riscv64-linux.img of=/dev/your/device bs=4M status=progress
```

### 登录系统

通过串口登录系统。

默认为无密码且自动登录。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
<<< Welcome to NixOS 22.11.20221014.4428e23 (riscv64) - ttyS0 >>>
<<< WelcoThe "nixos" and "root" accounts have empty passwords.

An ssh daemon is runninme to NixOS 22.11g. You then must set a password
for either "root" or "nixos" with `passwd` or a.dd an ssh key
to /home/nixos/.ssh/authorized_keys be able to login.

If you need a wireless connection, type
`sudo systemctl start wpa_supplicant` and configure a
network using `wpa_cli`.20221014.4428e23 (riscv64) - hvc0 See the NixOS manual for details.


Run 'nixos-help' for the NixOS manual.

nixos login: nixos (automatic  >>>
The "nixos" and "login)

root" accounts have empty passwords.

An ssh daemon is running. You then must set a password
for either "root" or "nixos" with `passwd` or add an ssh key
to /home/nixos/.ssh/authorized_keys be able to login.

If you need a wireless connection, type
`sudo systemctl start wpa_supplicant` and configure a
network using `wpa_cli`. See the NixOS manual for details.


Run 'nixos-help' for the NixOS manual.

nixos login: nixos (automatic login)


[nixos@nixos:~]$ 
[nixos@nixos:~]$ uname -a
Linux nixos 5.18.0-rc1 #1-NixOS PREEMPT Tue Jan 1 00:00:00 UTC 1980 riscv64 GNU/Linux

[nixos@nixos:~]$ cat /etc/os-release 
BUG_REPORT_URL="https://github.com/NixOS/nixpkgs/issues"
BUILD_ID="22.11.20221014.4428e23"
DOCUMENTATION_URL="https://nixos.org/learn.html"
HOME_URL="https://nixos.org/"
ID=nixos
LOGO="nix-snowflake"
NAME=NixOS
PRETTY_NAME="NixOS 22.11 (Raccoon)"
SUPPORT_URL="https://nixos.org/community.html"
VERSION="22.11 (Raccoon)"
VERSION_CODENAME=raccoon
VERSION_ID="22.11"

[nixos@nixos:~]$ cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdc
mmu             : sv39
uarch           : thead,c906


[nixos@nixos:~]$ 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
