# NixOS LicheeRV 测试报告

## 测试环境

### 操作系统信息

- 下载链接: https://github.com/chuangzhu/nixos-sun20iw1p1/releases
- 参考安装文档: https://github.com/chuangzhu/nixos-sun20iw1p1

### 硬件信息

- Sipeed Lichee RV Dock
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

无密码,初次登录时，系统会提示更改密码。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
<<< Welme to NixOS 22.11come to NixOS 22..11.20221014.4428e23 (riscv64) - ttyS0 >>>
The "nixos" and 20221014.4428e23"root" accounts have empty passwords.

An ssh daemon is running. You then must set a password
for either "roo (riscv64) - hvc0 >>>
t" or "nixos" with `passwd` or add an ssh key
to /home/nixos/.ssh/authorized_keys be able to loThe "nixos" and "root" accounts have empty passworgin.

If you need a wireless connection, type
`sudo systemctl start wpa_supplicant` and configure a
network using `wpa_cli`. See the NixOS mds.

An ssh daemon is running. You theanual for details.


Run 'nixos-help' for the NixOS manual.

nixos login: nixos (automatic login)

n must set a password
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
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
