---
sys: ubuntu
sys_ver: null
sys_var: null

status: basic
last_update: 2024-11-13
---

# Ubuntu Milk-V Duo Test Report

## Test Environment

### Operating System Information

- System Version: milkv-duo-ubuntu-22.04-riscv64-v0.0.4-spiritdude.img
- Download Link: https://drive.google.com/file/d/1y1NQamzUDzot_kVT2yKkbusoJmtvH5tD/view?usp=sharing
- Reference Installation Document:
  - https://xyzdims.com/3d-printers/misc-hardware-notes/iot-milk-v-duo-risc-v-esbc-running-linux/#Ubuntu_Disk_Image
  - https://github.com/bassusteur/milkv-duo-ubuntu

> Note: This image is provided by community developers and is not an official image.

### Hardware Information

- Milk-V Duo 64M
- A USB Power Adapter
- A USB-A to C or USB C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont Wires
- Milk-V Duo with necessary header pins pre-soldered for debugging
- Optional: Milk-V Duo IOB (Baseboard)

## Installation Steps

### Using `dd` to Flash the Image to the microSD Card 

```shell
unzip milkv-duo-ubuntu-22.04-riscv64-v0.0.4-spiritdude.zip
dd if=milkv-duo-ubuntu-22.04-riscv64-v0.0.4-spiritdude.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Username: `root`
Password: `milkv`

> Note: `apt` might become unresponsive or unable to function properly due to the tight memory constraints.

## Expected Results

The system boots up normally and allows login through the serial port.

## Actual Results

The system boots up normally and login through the serial port is successful.

### Boot Log

```log
Welcome to Ubuntu 22.04 LTS!

[    1.696687] systemd[1]: Hostname set to <milkv-duo>.
[    2.160028] systemd-fstab-generator[94]: Ignoring "noauto" option for root device
[    3.111135] systemd[1]: Queued start job for default target Graphical Interface.
[    3.122288] random: systemd: uninitialized urandom read (16 bytes read)
[    3.137377] systemd[1]: Created slice Slice /system/modprobe.
[  OK  ] Created slice Slice /system/modprobe.
[    3.159605] random: systemd: uninitialized urandom read (16 bytes read)
[    3.170528] systemd[1]: Created slice Slice /system/serial-getty.
[  OK  ] Created slice Slice /system/serial-getty.
[    3.191614] random: systemd: uninitialized urandom read (16 bytes read)
[    3.201785] systemd[1]: Created slice User and Session Slice.
[  OK  ] Created slice User and Session Slice.
[    3.224298] systemd[1]: Started Dispatch Password Requests to Console Directory Watch.
[  OK  ] Started Dispatch Password …ts to Console Directory Watch.
[    3.252167] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[  OK  ] Started Forward Password R…uests to Wall Directory Watch.
[    3.279996] systemd[1]: Condition check resulted in Arbitrary Executable File Formats File System Automount Point being skipped.
[    3.292725] systemd[1]: Reached target Local Encrypted Volumes.
[  OK  ] Reached target Local Encrypted Volumes.
[    3.316185] systemd[1]: Reached target Remote File Systems.
[  OK  ] Reached target Remote File Systems.
[    3.335717] systemd[1]: Reached target Slice Units.
[  OK  ] Reached target Slice Units.
[    3.355910] systemd[1]: Reached target System Time Set.
[  OK  ] Reached target System Time Set.
[    3.375995] systemd[1]: Reached target Local Verity Protected Volumes.
[  OK  ] Reached target Local Verity Protected Volumes.
[    3.401707] systemd[1]: Listening on Syslog Socket.
[  OK  ] Listening on Syslog Socket.
[    3.424966] systemd[1]: Listening on fsck to fsckd communication Socket.
[  OK  ] Listening on fsck to fsckd communication Socket.
[    3.452305] systemd[1]: Listening on initctl Compatibility Named Pipe.
[  OK  ] Listening on initctl Compatibility Named Pipe.
[    3.497037] systemd[1]: Condition check resulted in Journal Audit Socket being skipped.
[    3.507153] systemd[1]: Listening on Journal Socket (/dev/log).
[  OK  ] Listening on Journal Socket (/dev/log).
[    3.529180] systemd[1]: Listening on Journal Socket.
[  OK  ] Listening on Journal Socket.
[    3.552444] systemd[1]: Listening on udev Control Socket.
[  OK  ] Listening on udev Control Socket.
[    3.572892] systemd[1]: Listening on udev Kernel Socket.
[  OK  ] Listening on udev Kernel Socket.
[    3.591708] systemd[1]: Reached target Socket Units.
[  OK  ] Reached target Socket Units.
[    3.612597] systemd[1]: Condition check resulted in Huge Pages File System being skipped.
[    3.629671] systemd[1]: Mounting POSIX Message Queue File System...
         Mounting POSIX Message Queue File System...
[    3.668945] systemd[1]: Mounting Kernel Debug File System...
         Mounting Kernel Debug File System...
[    3.704596] systemd[1]: Condition check resulted in Kernel Trace File System being skipped.
[    3.719571] systemd[1]: systemd-journald.service: unit configures an IP firewall, but the local system does not support BPF/cgroup firewalling.
[    3.733117] systemd[1]: (This warning is only shown for the first unit using IP firewalling.)
[    3.749695] systemd[1]: Starting Journal Service...
         Starting Journal Service...
[    3.794473] systemd[1]: Starting Set the console keyboard layout...
         Starting Set the console keyboard layout...
[    3.831778] systemd[1]: Condition check resulted in Create List of Static Device Nodes being skipped.
[    3.893304] systemd[1]: Starting Load Kernel Module configfs...
         Starting Load Kernel Module configfs...
[    3.980085] systemd[1]: Starting Load Kernel Module drm...
         Starting Load Kernel Module drm...
[    4.050796] systemd[1]: Starting Load Kernel Module efi_pstore...
         Starting Load Kernel Module efi_pstore...
[    4.160720] systemd[1]: Starting Load Kernel Module fuse...
         Starting Load Kernel Module fuse...
[    4.208277] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
[    4.286144] systemd[1]: Starting Load Kernel Modules...
         Starting Load Kernel Modules...
[    4.358691] systemd[1]: Starting Remount Root and Kernel File Systems...
         Starting Remount Root and Kernel File Systems...
[    4.451180] systemd[1]: Starting Coldplug All udev Devices...
         Starting Coldplug All udev Devices...
[    4.664484] systemd[1]: Mounted POSIX Message Queue File System.
[    4.702079] EXT4-fs (mmcblk0p2): re-mounted. Opts: (null)
[  OK  ] Mounted POSIX Message Queue File System.
[    4.783527] ext4 filesystem being remounted at / supports timestamps until 2038 (0x7fffffff)
[    4.805532] systemd[1]: Mounted Kernel Debug File System.
[  OK  ] Mounted Kernel Debug File System.
[    4.871633] systemd[1]: modprobe@configfs.service: Deactivated successfully.
[    4.907627] systemd[1]: Finished Load Kernel Module configfs.
[  OK  ] Finished Load Kernel Module configfs.
[    4.999751] systemd[1]: Finished Set the console keyboard layout.
[  OK  ] Finished Set the console keyboard layout.
[    5.040531] systemd[1]: Started Journal Service.
[  OK  ] Started Journal Service.
[  OK  ] Finished Load Kernel Module drm.
[  OK  ] Finished Load Kernel Module efi_pstore.
[  OK  ] Finished Load Kernel Module fuse.
[  OK  ] Finished Load Kernel Modules.
[  OK  ] Finished Remount Root and Kernel File Systems.
         Mounting Kernel Configuration File System...
         Starting Flush Journal to Persistent Storage...
         Starting Load/Save Random Seed...
         Starting Apply Kernel Variables...
         Starting Create System Users...
[    5.460156] systemd-journald[107]: Received client request to flush runtime journal.
[    5.519735] systemd-journald[107]: File /var/log/journal/bb35470655554941b9067e089febf1db/system.journal corrupted or uncleanly shut down, renaming and replacing.
[  OK  ] Mounted Kernel Configuration File System.
[FAILED] Failed to start Apply Kernel Variables.
See 'systemctl status systemd-sysctl.service' for details.
[  OK  ] Finished Create System Users.
         Starting Create Static Device Nodes in /dev...
[  OK  ] Finished Create Static Device Nodes in /dev.
[  OK  ] Reached target Preparation for Local File Systems.
         Starting Rule-based Manage…for Device Events and Files...
[  OK  ] Finished Flush Journal to Persistent Storage.
[  OK  ] Finished Coldplug All udev Devices.
         Starting Helper to synchronize boot up for ifupdown...
[  OK  ] Finished Helper to synchronize boot up for ifupdown.
[  OK  ] Started Rule-based Manager for Device Events and Files.
[  OK  ] Found device /dev/ttyS0.
[  OK  ] Reached target Hardware activated USB gadget.
[  OK  ] Finished Load/Save Random Seed.
[  OK  ] Found device /dev/mmcblk0p3.
[  OK  ] Reached target Sound Card.
[  OK  ] Listening on Load/Save RF …itch Status /dev/rfkill Watch.
         Activating swap /dev/mmcblk0p3...
[FAILED] Failed to activate swap /dev/mmcblk0p3.
See 'systemctl status dev-mmcblk0p3.swap' for details.
[DEPEND] Dependency failed for Swaps.
         Mounting /tmp...
[  OK  ] Mounted /tmp.
[  OK  ] Reached target Local File Systems.
         Starting Set console font and keymap...
         Starting Raise network interfaces...
         Starting Create Volatile Files and Directories...
[  OK  ] Finished Set console font and keymap.
[  OK  ] Finished Raise network interfaces.
[  OK  ] Reached target Network.
[  OK  ] Finished Create Volatile Files and Directories.
[  OK  ] Started Entropy Daemon based on the HAVEGE algorithm.
         Starting Record System Boot/Shutdown in UTMP...
[  OK  ] Finished Record System Boot/Shutdown in UTMP.
[  OK  ] Reached target System Initialization.
[  OK  ] Started Trigger to poll fo…y enabled on GCP LTS non-pro).
[  OK  ] Started Daily Cleanup of Temporary Directories.
[  OK  ] Started Ubuntu Advantage Timer for running repeated jobs.
[  OK  ] Reached target Path Units.
[  OK  ] Reached target Basic System.
[  OK  ] Listening on D-Bus System Message Bus Socket.
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
[  OK  ] Started System Logging Service.
[  OK  ] Finished Initializes zram swaping.
[  OK  ] Started LSB: Lightweight SSH server.
[  OK  ] Started Serial Getty on ttyS0.
[  OK  ] Created slice Slice /system/getty.
[  OK  ] Reached target Login Prompts.
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

Ubuntu 22.04 LTS milkv-duo ttyS0

milkv-duo login: root
Password: 
Welcome to Ubuntu 22.04 LTS (GNU/Linux 5.10.4-tag- riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
Last login: Tue Sep 19 16:57:28 UTC 2023 on ttyS0
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
    .ossssssssssssssssssdMMMNysssso.       Host: Cvitek. CV180X ASIC. C906. 
   /ssssssssssshdmmNNmmyNMMMMhssssss/      Kernel: 5.10.4-tag- 
  +ssssssssshmydMMMMMMMNddddyssssssss+     Uptime: 48 secs 
 /sssssssshNMMMyhhyyyyhmNMMMNhssssssss/    Packages: 245 (dpkg) 
.ssssssssdMMMNhsssssssssshNMMMdssssssss.   Shell: bash 5.1.16 
+sssshhhyNMMNyssssssssssssyNMMMysssssss+   Terminal: /dev/ttyS0 
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   CPU: (1) 
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   Memory: 30MiB / 54MiB 
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

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
