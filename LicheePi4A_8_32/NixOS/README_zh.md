# NixOS LPi4A 测试报告

## 测试环境

### 系统信息

- 系统版本：NixOS 23.05
- 下载链接：[Releases · ryan4yin/nixos-licheepi4a](https://github.com/ryan4yin/nixos-licheepi4a/releases)
  - u-boot:[Releases · ryan4yin/nixos-licheepi4a](https://github.com/ryan4yin/nixos-licheepi4a/releases)
- fastboot 链接：
  - [https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ](https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ)
  - [https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)

### 硬件信息

- Lichee Pi 4A (8G RAM + 32G eMMC)
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `zstd` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
zstd -d /path/to/nixos-licheepi4a-sd-image-23.05.20230806.240472b-riscv64-linux.img.zst
sudo dd if=/path/to/nixos-licheepi4a-sd-image-23.05.20230806.240472b-riscv64-linux.img.zst of=/dev/your_device bs=1M status=progress
```

### 刷写 bootloader

进入 fastboot。

- 按动 BOOT 同时上电。
- （详见官方教程）
  使用 fastboot 按命令烧录 u-boot。

```bash
sudo ./fastboot flash ram ./path/to/your/u-boot-with-spl.bin
sudo ./fastboot reboot
sudo ./fastboot flash uboot ./path/to/your/u-boot-with-spl.bin
```

### 登录系统

通过串口登录系统。

默认用户名：`lp4a`  默认密码：`lp4a`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像：

[![asciicast](https://asciinema.org/a/1tapS19lE8Mnlsr8tHgjT3bOr.svg)](https://asciinema.org/a/1tapS19lE8Mnlsr8tHgjT3bOr)


```log
[  OK  ] Mounted FUSE Control File System.
[  OK  ] Mounted Kernel Configuration File System.
[  OK  ] Finished Load/Save OS Random Seed.
[  OK  ] Finished Apply Kernel Variables.
[  OK  ] Finished Flush Journal to Persistent Storage.
         Starting Create Volatile Files and Directories...
[  OK  ] Started Rule-based Manager for Device Events and Files.
[FAILED] Failed to start Firewall.
See 'systemctl status firewall.service' for details.
[  OK  ] Finished Create Volatile Files and Directories.
         Starting Rebuild Journal Catalog...
         Starting Network Time Synchronization...
         Starting Record System Boot/Shutdown in UTMP...
[  OK  ] Finished Rebuild Journal Catalog.
[  OK  ] Finished Record System Boot/Shutdown in UTMP.
         Starting Update is Completed...
[  OK  ] Finished Update is Completed.
[  OK  ] Started Network Time Synchronization.
[  OK  ] Found device /dev/ttyS0.
[  OK  ] Finished Coldplug All udev Devices.
[  OK  ] Created slice Slice /system/systemd-backlight.
[  OK  ] Reached target Sound Card.
[  OK  ] Listening on Load/Save RF …itch Status /dev/rfkill Watch.
         Starting Load/Save Screen …f backlight:pwm-backlight@0...
[  OK  ] Finished Load/Save Screen … of backlight:pwm-backlight@0.
[  OK  ] Reached target System Initialization.
[  OK  ] Started logrotate.timer.
[  OK  ] Started Daily Cleanup of Temporary Directories.
[  OK  ] Reached target Timer Units.
[  OK  ] Listening on D-Bus System Message Bus Socket.
[  OK  ] Listening on Nix Daemon Socket.
[  OK  ] Reached target Socket Units.
[  OK  ] Reached target Basic System.
         Starting Kernel Auditing...
         Starting CPU Frequency Setup...
         Starting DHCP Client...
         Starting Logrotate configuration check...
         Starting Name Service Cache Daemon (nsncd)...
[  OK  ] Started Reset console on configuration changes.
         Starting resolvconf update...
         Starting Load/Save RF Kill Switch Status...
[  OK  ] Started Name Service Cache Daemon (nsncd).
[  OK  ] Started Load/Save RF Kill Switch Status.
[  OK  ] Finished Kernel Auditing.
[  OK  ] Finished CPU Frequency Setup.
[  OK  ] Finished Logrotate configuration check.
[  OK  ] Reached target Host and Network Name Lookups.
[  OK  ] Reached target User and Group Name Lookups.
         Starting D-Bus System Message Bus...
         Starting User Login Management...
[  OK  ] Stopped target Host and Network Name Lookups.
         Stopping Host and Network Name Lookups...
[  OK  ] Stopped target User and Group Name Lookups.
         Stopping User and Group Name Lookups...
         Stopping Name Service Cache Daemon (nsncd)...
[  OK  ] Stopped Name Service Cache Daemon (nsncd).
[  OK  ] Finished resolvconf update.
[  OK  ] Started D-Bus System Message Bus.
[  OK  ] Reached target Preparation for Network.
[  OK  ] Reached target All Network Interfaces (deprecated).
         Starting Networking Setup...
         Starting Name Service Cache Daemon (nsncd)...
[  OK  ] Started User Login Management.
[  OK  ] Started Name Service Cache Daemon (nsncd).
[  OK  ] Reached target Host and Network Name Lookups.
[  OK  ] Reached target User and Group Name Lookups.
[  OK  ] Finished Networking Setup.
         Starting Extra networking commands....
[  OK  ] Finished Extra networking commands..
[  OK  ] Reached target Network.
         Starting SSH Daemon...
         Starting Permit User Sessions...
[  OK  ] Finished Permit User Sessions.
[  OK  ] Started Getty on tty1.
[  OK  ] Started Serial Getty on ttyS0.
[  OK  ] Reached target Login Prompts.


<<< Welcome to NixOS 23.05.20230806.240472b (riscv64) - ttyS0 >>>

Run 'nixos-help' for the NixOS manual.

lp4a login: lp4a
Password:

[lp4a@lp4a:~]$ uname -a
Linux lp4a 5.10.113 #1-NixOS SMP PREEMPT Tue Jan 1 00:00:00 UTC 1980 riscv64 GNU/Linux

[lp4a@lp4a:~]$ neofetch
          ▗▄▄▄       ▗▄▄▄▄    ▄▄▄▖            lp4a@lp4a
          ▜███▙       ▜███▙  ▟███▛            ---------
           ▜███▙       ▜███▙▟███▛             OS: NixOS 23.05.20230806.240472b (Stoat) riscv64
            ▜███▙       ▜██████▛              Host: T-HEAD Light Lichee Pi 4A configuration for 8GB DDR board
     ▟█████████████████▙ ▜████▛     ▟▙        Kernel: 5.10.113
    ▟███████████████████▙ ▜███▙    ▟██▙       Uptime: 1 min
           ▄▄▄▄▖           ▜███▙  ▟███▛       Packages: 306 (nix-system)
          ▟███▛             ▜██▛ ▟███▛        Shell: bash 5.2.15
         ▟███▛               ▜▛ ▟███▛         Terminal: /dev/ttyS0
▟███████████▛                  ▟██████████▙   CPU: (4) @ 1.848GHz
▜██████████▛                  ▟███████████▛   Memory: 172MiB / 7781MiB
      ▟███▛ ▟▙               ▟███▛
     ▟███▛ ▟██▙             ▟███▛
    ▟███▛  ▜███▙           ▝▀▀▀▀
    ▜██▛    ▜███▙ ▜██████████████████▛
     ▜▛     ▟████▙ ▜████████████████▛
           ▟██████▙       ▜███▙
          ▟███▛▜███▙       ▜███▙
         ▟███▛  ▜███▙       ▜███▙
         ▝▀▀▀    ▀▀▀▀▘       ▀▀▀▘
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
