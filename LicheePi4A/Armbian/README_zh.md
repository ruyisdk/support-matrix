# Armbian LPi4A 测试报告

## 测试环境

### 系统信息

- 系统版本：Ubuntu 22.04 LTS 
- 下载链接：[Releases · chainsx/armbian-riscv-build](https://github.com/chainsx/armbian-riscv-build/releases)
  - u-boot:[Releases · chainsx/armbian-riscv-build](https://github.com/chainsx/armbian-riscv-build/releases)
- fastboot 链接：
  - [https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ](https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ)
  - [https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)

### 硬件信息

- Lichee Pi 4A (16G RAM + 128G eMMC)
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `unxz` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
unxz /path/to/Armbian.img.xz
sudo dd if=/path/to/Armbian.img of=/dev/your_device bs=1M status=progress
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

初次启动会要求设置用户及密码。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写uboot到登录系统，刷写镜像进SD卡已先行完成）：

[![asciicast](https://asciinema.org/a/iqZzdZPNfgzAo3RiIYRjk1TU3.svg)](https://asciinema.org/a/iqZzdZPNfgzAo3RiIYRjk1TU3)

```log
[  OK  ] Started Network Name Resolution.
[  OK  ] Finished Armbian hardware monitoring.
[  OK  ] Reached target Host and Network Name Lookups.
[  OK  ] Finished Armbian filesystem resize.
[  OK  ] Reached target Basic System.
         Starting Save/Restore Sound Card State...
[  OK  ] Started Armbian first run tasks.
[  OK  ] Started Regular background program processing daemon.
[  OK  ] Started D-Bus System Message Bus.
         Starting Network Manager...
[  OK  ] Started Save initial kernel messages after boot.
         Starting Remove Stale Onli…t4 Metadata Check Snapshots...
         Starting Dispatcher daemon for systemd-networkd...
         Starting resolvconf-pull-resolved.service...
         Starting System Logging Service...
         Starting LSB: Set sysfs variables from /etc/sysfs.conf...
         Starting Resets System Activity Logs...
         Starting User Login Management...
         Starting WPA supplicant...
[  OK  ] Finished Remove Stale Onli…ext4 Metadata Check Snapshots.
[  OK  ] Started System Logging Service.
[  OK  ] Finished Resets System Activity Logs.
[  OK  ] Finished Save/Restore Sound Card State.
[  OK  ] Finished resolvconf-pull-resolved.service.
[  OK  ] Started WPA supplicant.
[  OK  ] Started Network Manager.
[  OK  ] Started LSB: Set sysfs variables from /etc/sysfs.conf.
[  OK  ] Reached target Network.
[  OK  ] Reached target Network is Online.
[  OK  ] Reached target Sound Card.
         Starting chrony, an NTP client/server...
         Starting Access point and …rver for Wi-Fi and Ethernet...
         Starting NFS Mount Daemon...
         Starting OpenVPN service...
         Starting /etc/rc.local Compatibility...
         Starting NFS status monitor for NFSv2/3 locking....
         Starting OpenBSD Secure Shell server...
         Starting Hostname Service...
         Starting Permit User Sessions...
[  OK  ] Started vnStat network traffic monitor.
[FAILED] Failed to start Access poi…server for Wi-Fi and Ethernet.
See 'systemctl status hostapd.service' for details.
[  OK  ] Started NFS Mount Daemon.
[  OK  ] Started chrony, an NTP client/server.
[  OK  ] Finished OpenVPN service.
[  OK  ] Started /etc/rc.local Compatibility.
[  OK  ] Started NFS status monitor for NFSv2/3 locking..
[  OK  ] Finished Permit User Sessions.
[  OK  ] Started User Login Management.
[  OK  ] Reached target System Time Synchronized.
[  OK  ] Started Daily apt download activities.
[  OK  ] Started Daily apt upgrade and clean activities.
[  OK  ] Started Daily dpkg database backup timer.
[  OK  ] Started Periodic ext4 Onli…ata Check for All Filesystems.
[  OK  ] Started Discard unused blocks once a week.
[  OK  ] Started Daily rotation of log files.
[  OK  ] Started Daily man-db regeneration.
[  OK  ] Started Run system activit…ounting tool every 10 minutes.
[  OK  ] Started Generate summary o…esterday's process accounting.
[  OK  ] Reached target Timer Units.
         Starting NFS server and services...
[  OK  ] Started Serial Getty on ttyS0.
         Starting Set console scheme...
[  OK  ] Started Unattended Upgrades Shutdown.
Welcome to ARMBIAN! 

Documentation: https://docs.armbian.com | Community: https://forum.armbian.com

Create root password: ****
Repeat root password: ****
Rejected - it is too short. Try again [3].
Create root password: ****
Repeat root password: ****
Rejected - it is too short. Try again [2].
Create root password: ****
Repeat root password: ****
Rejected - it is too short. Try again [1].
root@licheepi-4a-16gb:~# neofetch
            .-/+oossssoo+/-.                                                    
        `:+ssssssssssssssssss+:`           --------------------- 
      -+ssssssssssssssssssyyssss+-         OS: Ubuntu 22.04.3 LTS riscv64 
    .ossssssssssssssssssdMMMNysssso.       Host: T-HEAD Light Lichee Pi 4A conf 
   /ssssssssssshdmmNNmmyNMMMMhssssss/      Kernel: 5.10.113-thead-g052b22ef8baf 
  +ssssssssshmydMMMMMMMNddddyssssssss+     Uptime: 1 min 
 /sssssssshNMMMyhhyyyyhmNMMMNhssssssss/    Packages: 509 (dpkg) 
.ssssssssdMMMNhsssssssssshNMMMdssssssss.   Shell: bash 5.1.16 
+sssshhhyNMMNyssssssssssssyNMMMysssssss+   Terminal: /dev/ttyS0 
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   CPU: (4) @ 1.848GHz 
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   Memory: 200MiB / 15773MiB 
+sssshhhyNMMNyssssssssssssyNMMMysssssss+
.ssssssssdMMMNhsssssssssshNMMMdssssssss.                           
 /sssssssshNMMMyhhyyyyhdNMMMNhssssssss/                            
  +sssssssssdmydMMMMMMMMddddyssssssss+
   /ssssssssssshdmNNNNmyNMMMMhssssss/                
    .ossssssssssssssssssdMMMNysssso.                 
      -+sssssssssssssssssyyyssss+-                   
        `:+ssssssssssssssssss+:`                     
            .-/+oossssoo+/-.


```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。