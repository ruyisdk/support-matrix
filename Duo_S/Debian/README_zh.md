# Debian Milk-V Duo S 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/Fishwaldo/sophgo-sg200x-debian/releases/tag/v1.4.0
- 参考安装文档：https://github.com/Fishwaldo/sophgo-sg200x-debian

### 硬件信息

- Milk-V Duo S (512M, SG2000)
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条，用于给开发板供电
- microSD 卡一张
- USB 读卡器一个
- USB to UART 调试器一个
    - 仅推荐使用 CP210x 系列如 CP2102/CP2104，注意不可使用 CH340/341 系列，会输出乱码；FT232/CH343P 等其他串口调试器在启动至 U-Boot 之前也会出现乱码，启动后可正常使用，这是预期结果，如果持续只能得到乱码输出请尝试更换使用 CP210x 系列芯片的调试器
- 杜邦线三根

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
lz4 -dk duos_sd.img.lz4
sudo dd if=duos_sd.img of=/dev/sdX bs=1M status=progress
```

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
Debian GNU/Linux trixie/sid duos ttyS0

duos login: debian
Password:
Linux duos 5.10.4-20240527-2+ #1 Sat Jun 1 14:15:39 UTC 2024 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
2004hdebian@duos:~$ cat /[  OK  ] Finished finalize-image.service - Finalize the Image.
         Starting ssh.service - OpenBSD Secure Shell server...
[  OK  ] Started ssh.service - OpenBSD Secure Shell server.
[  OK  ] Reached target multi-user.target - Multi-User System.
[  OK  ] Reached target graphical.target - Graphical Interface.
         Starting systemd-update-utmp-runle…- Record Runlevel Change in UTMP...
[  OK  ] Finished systemd-update-utmp-runle…e - Record Runlevel Change in UTMP.
[   84.662830] cvi_rtc 5026000.rtc: time set to 1721370282. 7/19/2024 6:24:42
[   84.676348] cvi_rtc 5026000.rtc: time read as 1721370282. 7/19/2024 6:24:42
^C
debian@duos:~$ cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
4hdebian@duos:~$ uname -a
Linux duos 5.10.4-20240527-2+ #1 Sat Jun 1 14:15:39 UTC 2024 riscv64 GNU/Linux
debian@duos:~$ cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

[?2004hdebian@duos:~$
```

屏幕录像：

[![asciicast](https://asciinema.org/a/SJ7sck8RtdUvHapuyqs0rPmS4.svg)](https://asciinema.org/a/SJ7sck8RtdUvHapuyqs0rPmS4)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。