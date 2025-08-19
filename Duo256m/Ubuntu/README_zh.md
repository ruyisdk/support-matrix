# Ubuntu Milk-V Duo 256M 测试报告

## 测试环境

### 操作系统信息

- 系统版本：milkv-duo-256m-ubuntu-22.04-riscv64-v0.0.4-spiritdude.img
- 下载链接：https://drive.google.com/file/d/1mkzLhvtjJup3GbgWKZdwL80PZMMXg7n1/view?usp=drive_link
- 参考安装文档：https://xyzdims.com/3d-printers/misc-hardware-notes/iot-milk-v-duo-risc-v-esbc-running-linux/#Ubuntu_Disk_Image

> Note: 此镜像为社区开发者提供，非官方镜像。

### 硬件信息

- Milk-V Duo 256M
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根
- Milk-V Duo 本体上预先焊接好调试所需的排针
- 可选：Milk-V Duo IOB（底板）

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
unzip milkv-duo-256m-ubuntu-22.04-riscv64-v0.0.4-spiritdude.zip
dd if=milkv-duo-256m-ubuntu-22.04-riscv64-v0.0.4-spiritdude.img of=/dev/your/device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

用户名：`root`
密码：`milkv`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```log
Welcome to Ubuntu 22.04 LTS!

[    1.763725] systemd[1]: Hostname set to <milkv-duo>.
[    2.208805] systemd-fstab-generator[97]: Ignoring "noauto" option for root device
[    2.294427] systemd-fstab-generator[97]: Swap not supported, ignoring fstab swap entry for /dev/mmcblkXp3.
[    3.158107] random: crng init done
[    3.201494] systemd[1]: Queued start job for default target Graphical Interface.
[    3.219878] systemd[1]: Created slice Slice /system/modprobe.
[  OK  ] Created slice Slice /system/modprobe.
[    3.246636] systemd[1]: Created slice Slice /system/serial-getty.
[  OK  ] Created slice Slice /system/serial-getty.
[    3.269840] systemd[1]: Created slice User and Session Slice.
[  OK  ] Created slice User and Session Slice.
[    3.291467] systemd[1]: Started Dispatch Password Requests to Console Directory Watch.
[  OK  ] Started Dispatch Password …ts to Console Directory Watch.
[    3.319388] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[  OK  ] Started Forward Password R…uests to Wall Directory Watch.
[    3.347342] systemd[1]: Condition check resulted in Arbitrary Executable File Formats File System Automount Point being skipped.
[    3.359865] systemd[1]: Reached target Local Encrypted Volumes.
[  OK  ] Reached target Local Encrypted Volumes.
[    3.383275] systemd[1]: Reached target Remote File Systems.
[  OK  ] Reached target Remote File Systems.
[    3.402853] systemd[1]: Reached target Slice Units.
[  OK  ] Reached target Slice Units.
[    3.422938] systemd[1]: Reached target Swaps.
[  OK  ] Reached target Swaps.
[    3.442875] systemd[1]: Reached target System Time Set.
[  OK  ] Reached target System Time Set.
[    3.463151] systemd[1]: Reached target Local Verity Protected Volumes.
[  OK  ] Reached target Local Verity Protected Volumes.
[    3.488593] systemd[1]: Listening on Syslog Socket.
[  OK  ] Listening on Syslog Socket.
[    3.508113] systemd[1]: Listening on fsck to fsckd communication Socket.
[  OK  ] Listening on fsck to fsckd communication Socket.
[    3.535376] systemd[1]: Listening on initctl Compatibility Named Pipe.
[  OK  ] Listening on initctl Compatibility Named Pipe.
[    3.579725] systemd[1]: Condition check resulted in Journal Audit Socket being skipped.
[    3.589711] systemd[1]: Listening on Journal Socket (/dev/log).
[  OK  ] Listening on Journal Socket (/dev/log).
[    3.612436] systemd[1]: Listening on Journal Socket.
[  OK  ] Listening on Journal Socket.
[    3.635630] systemd[1]: Listening on udev Control Socket.
[  OK  ] Listening on udev Control Socket.
[    3.656124] systemd[1]: Listening on udev Kernel Socket.
[  OK  ] Listening on udev Kernel Socket.
[    3.674858] systemd[1]: Reached target Socket Units.
[  OK  ] Reached target Socket Units.
[    3.695798] systemd[1]: Condition check resulted in Huge Pages File System being skipped.
[    3.712621] systemd[1]: Mounting POSIX Message Queue File System...
         Mounting POSIX Message Queue File System...
[    3.753466] systemd[1]: Mounting Kernel Debug File System...
         Mounting Kernel Debug File System...
[    3.791609] systemd[1]: Condition check resulted in Kernel Trace File System being skipped.
[    3.802129] systemd[1]: systemd-journald.service: unit configures an IP firewall, but the local system does not support BPF/cgroup firewalling.
[    3.815695] systemd[1]: (This warning is only shown for the first unit using IP firewalling.)
[    3.831886] systemd[1]: Starting Journal Service...
         Starting Journal Service...
[    3.877139] systemd[1]: Starting Set the console keyboard layout...
         Starting Set the console keyboard layout...
[    3.914954] systemd[1]: Condition check resulted in Create List of Static Device Nodes being skipped.
[    3.972870] systemd[1]: Starting Load Kernel Module configfs...
         Starting Load Kernel Module configfs...
[    4.051644] systemd[1]: Starting Load Kernel Module drm...
         Starting Load Kernel Module drm...
[    4.119426] systemd[1]: Starting Load Kernel Module efi_pstore...
         Starting Load Kernel Module efi_pstore...
[    4.225823] systemd[1]: Starting Load Kernel Module fuse...
         Starting Load Kernel Module fuse...
[    4.275605] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
[    4.348483] systemd[1]: Starting Load Kernel Modules...
         Starting Load Kernel Modules...
[    4.417835] systemd[1]: Starting Remount Root and Kernel File Systems...
         Starting Remount Root and Kernel File Systems...
[    4.515690] systemd[1]: Starting Coldplug All udev Devices...
         Starting Coldplug All udev Devices...
[    4.710084] systemd[1]: Mounted POSIX Message Queue File System.
[    4.765492] EXT4-fs (mmcblk0p2): re-mounted. Opts: (null)
[  OK  ] Mounted POSIX Message Queue File System.
[    4.839592] ext4 filesystem being remounted at / supports timestamps until 2038 (0x7fffffff)
[    4.864736] systemd[1]: Mounted Kernel Debug File System.
[  OK  ] Mounted Kernel Debug File System.
[    4.934872] systemd[1]: Finished Set the console keyboard layout.
[  OK  ] Finished Set the console keyboard layout.
[    5.007446] systemd[1]: modprobe@configfs.service: Deactivated successfully.
[    5.042845] systemd[1]: Finished Load Kernel Module configfs.
[  OK  ] Finished Load Kernel Module configfs.
[    5.086127] systemd[1]: modprobe@drm.service: Deactivated successfully.
[    5.118999] systemd[1]: Finished Load Kernel Module drm.
[  OK  ] Finished Load Kernel Module drm.
[    5.162179] systemd[1]: modprobe@efi_pstore.service: Deactivated successfully.
[    5.193353] systemd[1]: Finished Load Kernel Module efi_pstore.
[  OK  ] Finished Load Kernel Module efi_pstore.
[    5.228233] systemd[1]: Started Journal Service.
[  OK  ] Started Journal Service.
[  OK  ] Finished Load Kernel Module fuse.
[  OK  ] Finished Load Kernel Modules.
[  OK  ] Finished Remount Root and Kernel File Systems.
         Mounting Kernel Configuration File System...
         Starting Flush Journal to Persistent Storage...
         Starting Load/Save Random Seed...
         Starting Apply Kernel Variables...
         Starting Create System Users...
[    5.563420] systemd-journald[110]: Received client request to flush runtime journal.
[  OK  ] Mounted Kernel Configuration File System.
[  OK  ] Finished Load/Save Random Seed.
[  OK  ] Finished Apply Kernel Variables.
[  OK  ] Finished Create System Users.
         Starting Create Static Device Nodes in /dev...
[  OK  ] Finished Create Static Device Nodes in /dev.
[  OK  ] Finished Flush Journal to Persistent Storage.
[  OK  ] Reached target Preparation for Local File Systems.
         Mounting /tmp...
         Starting Rule-based Manage…for Device Events and Files...
[  OK  ] Mounted /tmp.
[  OK  ] Reached target Local File Systems.
         Starting Set console font and keymap...
         Starting Create Volatile Files and Directories...
[  OK  ] Finished Set console font and keymap.
[  OK  ] Finished Coldplug All udev Devices.
         Starting Helper to synchronize boot up for ifupdown...
[  OK  ] Finished Helper to synchronize boot up for ifupdown.
         Starting Raise network interfaces...
[  OK  ] Started Rule-based Manager for Device Events and Files.
[  OK  ] Finished Create Volatile Files and Directories.
[  OK  ] Finished Raise network interfaces.
[  OK  ] Reached target Network.
[  OK  ] Started Entropy Daemon based on the HAVEGE algorithm.
         Starting Record System Boot/Shutdown in UTMP...
[  OK  ] Found device /dev/ttyS0.
[  OK  ] Finished Record System Boot/Shutdown in UTMP.
[  OK  ] Reached target Sound Card.
[  OK  ] Reached target System Initialization.
[  OK  ] Started Trigger to poll fo…y enabled on GCP LTS non-pro).
[  OK  ] Started Daily Cleanup of Temporary Directories.
[  OK  ] Started Ubuntu Advantage Timer for running repeated jobs.
[  OK  ] Reached target Path Units.
[  OK  ] Reached target Basic System.
[  OK  ] Reached target Hardware activated USB gadget.
[  OK  ] Listening on D-Bus System Message Bus Socket.
[  OK  ] Listening on Load/Save RF …itch Status /dev/rfkill Watch.
         Starting chrony, an NTP client/server...
[  OK  ] Started Regular background program processing daemon.
[  OK  ] Started D-Bus System Message Bus.
[  OK  ] Started Save initial kernel messages after boot.
         Starting dnsmasq - A light…DHCP and caching DNS server...
         Starting LSB: Lightweight SSH server...
         Starting Remove Stale Onli…t4 Metadata Check Snapshots...
         Starting Dispatcher daemon for systemd-networkd...
[  OK  ] Started RNDIS.
         Starting System Logging Service...
         Starting User Login Management...
         Starting Permit User Sessions...
         Starting Initializes zram swaping...
[  OK  ] Finished Permit User Sessions.
[FAILED] Failed to start Initializes zram swaping.
See 'systemctl status zram-config.service' for details.
[  OK  ] Started System Logging Service.
[  OK  ] Started Serial Getty on ttyS0.
[  OK  ] Created slice Slice /system/getty.
[  OK  ] Reached target Login Prompts.
[  OK  ] Started LSB: Lightweight SSH server.
[  OK  ] Started chrony, an NTP client/server.
[  OK  ] Reached target System Time Synchronized.
[  OK  ] Started Daily apt download activities.
[  OK  ] Started Daily apt upgrade and clean activities.
[  OK  ] Started Daily dpkg database backup timer.
[  OK  ] Started Periodic ext4 Onli…ata Check for All Filesystems.
[  OK  ] Started Discard unused blocks once a week.
[  OK  ] Started Daily rotation of log files.
[  OK  ] Started Message of the Day.
[  OK  ] Reached target Timer Units.
[  OK  ] Started dnsmasq - A lightw…t DHCP and caching DNS server.
[  OK  ] Reached target Host and Network Name Lookups.
[  OK  ] Started User Login Management.

Ubuntu 22.04 LTS milkv-duo ttyS0

milkv-duo login: root
Password: 
Welcome to Ubuntu 22.04 LTS (GNU/Linux 5.10.4-tag- riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

root@milkv-duo:~# cat /etc/os-release 
PRETTY_NAME="Ubuntu 22.04 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04 (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy
root@milkv-duo:~# neofetch
            .-/+oossssoo+/-.               root@milkv-duo 
        `:+ssssssssssssssssss+:`           -------------- 
      -+ssssssssssssssssssyyssss+-         OS: Ubuntu 22.04 LTS riscv64 
    .ossssssssssssssssssdMMMNysssso.       Host: Cvitek. CV181X ASIC. C906. 
   /ssssssssssshdmmNNmmyNMMMMhssssss/      Kernel: 5.10.4-tag- 
  +ssssssssshmydMMMMMMMNddddyssssssss+     Uptime: 1 min 
 /sssssssshNMMMyhhyyyyhmNMMMNhssssssss/    Packages: 245 (dpkg) 
.ssssssssdMMMNhsssssssssshNMMMdssssssss.   Shell: bash 5.1.16 
+sssshhhyNMMNyssssssssssssyNMMMysssssss+   Terminal: /dev/ttyS0 
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   CPU: (1) 
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   Memory: 38MiB / 240MiB 
+sssshhhyNMMNyssssssssssssyNMMMysssssss+
.ssssssssdMMMNhsssssssssshNMMMdssssssss.                           
 /sssssssshNMMMyhhyyyyhdNMMMNhssssssss/                            
  +sssssssssdmydMMMMMMMMddddyssssssss+
   /ssssssssssshdmNNNNmyNMMMMhssssss/
    .ossssssssssssssssssdMMMNysssso.
      -+sssssssssssssssssyyyssss+-
        `:+ssssssssssssssssss+:`
            .-/+oossssoo+/-.

root@milkv-duo:~# 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。