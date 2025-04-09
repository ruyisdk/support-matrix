# Debian Milk-V Duo 256M 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Debian
- 下载链接：https://github.com/scpcom/sophgo-sg200x-debian/releases/download/v1.6.7/duo256-e_sd.img.lz4
- 参考安装文档：https://github.com/scpcom/sophgo-sg200x-debian/

> Note: 此镜像为社区开发者提供，非官方镜像。

### 硬件信息

- Milk-V Duo 256M
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 可选：Milk-V Duo IOB（底板）

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
wget https://github.com/scpcom/sophgo-sg200x-debian/releases/download/v1.6.7/duo256-e_sd.img.lz4
lz4 -d duo256-e_sd.img.lz4
sudo dd if=duo256-e_sd.img of=/dev/your/device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

用户名：`root`
密码：`rv`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```log
[   21.658971] RTOS_CMDQU_SEND_WAIT timeout
[   21.666545] SYS_CMD_INFO_LINUX_INIT_DONE fail
[   21.695036] communicate with rtos fail
         Starting systemd-hostnamed.service - Hostname Service...
[  OK  ] Started systemd-logind.service - User Login Management.
[  OK  ] Finished load-systemko.service - Load System Modules.
         Starting sensor-config.service - Configure Sensor...
[  OK  ] Finished sensor-config.service - Configure Sensor.
         Starting device-key.service - Store Device Key...
[  OK  ] Finished device-key.service - Store Device Key.
         Starting usb-device.service - USB Device...
[  OK  ] Finished usb-device.service - USB Device.
         Starting enable-backlight.service - Enable backlight...
[  OK  ] Finished enable-backlight.service - Enable backlight.
         Starting load-fb.service - Load fb...
[  OK  ] Started systemd-hostnamed.service - Hostname Service.
[  OK  ] Finished load-fb.service - Load fb.
         Starting load-tp.service - Load tp...
         Starting NetworkManager-dispatcher…anager Script Dispatcher Service...
[  OK  ] Started NetworkManager.service - Network Manager.
[  OK  ] Finished load-tp.service - Load tp.
         Starting device-uuid.service - Set MAC address...
[  OK  ] Started NetworkManager-dispatcher.… Manager Script Dispatcher Service.
[  OK  ] Finished device-uuid.service - Set MAC address.
         Starting load-wifimod.service - Load wifimod...
[  OK  ] Finished e2scrub_reap.service - Re…line ext4 Metadata Check Snapshots.
[  OK  ] Finished load-wifimod.service - Load wifimod.
[  OK  ] Finished finalize-image.service - Finalize the Image.
         Starting gadget-nic.service - Start Gadget NIC...
[  OK  ] Started ifup@end0.service - ifup for end0.
[  OK  ] Finished gadget-nic.service - Start Gadget NIC.
[  OK  ] Reached target network.target - Network.
         Starting gadget-nic-usb0.service - USB NIC DHCP Gadget Support...
         Starting lldpd.service - LLDP daemon...
         Starting ssh.service - OpenBSD Secure Shell server...
         Starting systemd-user-sessions.service - Permit User Sessions...
[  OK  ] Started gadget-nic-usb0.service - USB NIC DHCP Gadget Support.
[  OK  ] Finished systemd-user-sessions.service - Permit User Sessions.
[  OK  ] Started getty@tty1.service - Getty on tty1.
[  OK  ] Started serial-getty@ttyS0.service - Serial Getty on ttyS0.
[  OK  ] Reached target getty.target - Login Prompts.
[  OK  ] Started lldpd.service - LLDP daemon.
[  OK  ] Started ssh.service - OpenBSD Secure Shell server.
[  OK  ] Reached target multi-user.target - Multi-User System.
[  OK  ] Reached target graphical.target - Graphical Interface.

Debian GNU/Linux trixie/sid duo256-b327 ttyS0

duo256-b327 login: root
Password:
Linux duo256-b327 5.10.235-20250403-6+duo256 #1 PREEMPT Sat Apr 5 17:40:54 UTC 2025 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@duo256-b327:~# uname -a
Linux duo256-b327 5.10.235-20250403-6+duo256 #1 PREEMPT Sat Apr 5 17:40:54 UTC 2025 riscv64 GNU/Linux
root@duo256-b327:~# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@duo256-b327:~# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                1
  On-line CPU(s) list: 0
root@duo256-b327:~# cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

root@duo256-b327:~#

```


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。