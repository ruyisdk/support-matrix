---
sys: openeuler
sys_ver: "23.09"
sys_var: null

status: basic
last_update: 2024-11-06
---

# openEuler 23.09 riscv64 Milk-V Duo Test Report

## Test Environment

### Operating System Information

- System Version: openEuler 23.09 riscv64
- Download Links:
    - buildroot: https://github.com/milkv-duo/duo-buildroot-sdk.git
    - rootfs: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/openeuler-rootfs.tar.gz
- Reference Installation Document: https://blog.inuyasha.love/linuxeveryday/33.html

> Note: This image is provided as a rootfs.

### Hardware Information

- Milk-V Duo 64M
- A USB power adapter
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires
- The necessary headers for debugging pre-soldered on the Milk-V Duo
- Optional: Milk-V Duo IOB (baseboard)

## Installation Steps

### Building the Image

#### Build the buildroot

Clone buildroot to build the image:
```bash
git clone https://github.com/milkv-duo/duo-buildroot-sdk.git
cd duo-buildroot-sdk/
```

Modify the kernel configuration:
```bash
cat <<EOF >> build/boards/cv180x/cv1800b_milkv_duo_sd/linux/cvitek_cv1800b_milkv_duo_sd_defconfig
# for openEuler
CONFIG_CGROUPS=y
CONFIG_CGROUP_FREEZER=y
CONFIG_CGROUP_PIDS=y
CONFIG_CGROUP_DEVICE=y
CONFIG_CPUSETS=y
CONFIG_PROC_PID_CPUSET=y
CONFIG_CGROUP_CPUACCT=y
CONFIG_PAGE_COUNTER=y
CONFIG_MEMCG=y
CONFIG_CGROUP_SCHED=y
CONFIG_NAMESPACES=y
CONFIG_OVERLAY_FS=y
CONFIG_AUTOFS4_FS=y
CONFIG_SIGNALFD=y
CONFIG_TIMERFD=y
CONFIG_EPOLL=y
CONFIG_IPV6=y
CONFIG_FANOTIFY
EOF
```

Change line 43 of memmap.py to 0:
```bash
vim build/boards/cv180x/cv1800b_milkv_duo_sd/memmap.py

ION_SIZE = 0
```

Compile in Docker (recommended):
```bash
docker run -itd --name duodocker -v $(pwd):/home/work milkvtech/milkv-duo:latest /bin/bash
docker exec -it duodocker /bin/bash -c "cd /home/work && cat /etc/issue && ./build.sh milkv-duo-sd"
```

#### Insert rootfs

Copy the compiled image:
```bash
cd ..
cp duo-buildroot-sdk/out/milkv-duo-sd-20241106-0012.img .
```

Write to the SD card:
```bash
sudo dd if=milkv-duo-sd-20241106-0012.img of=/dev/your-device bs=1M status=progress
```

Prepare to replace the rootfs. Since the space for the original image's rootfs is insufficient, re-partitioning is needed. As we won't use the original rootfs, simply delete the original rootfs partition (the ~700MB one) and create a new one in place:
```bash
sudo fdisk /dev/your-device

# In fdisk
d
2
n
p
2
# First cylinder
# Last cylinder
w

# In bash
sudo mkfs.ext4 /dev/your-device-p2
```

Note: The new rootfs will be mounted to mnt, while the original rootfs will be mounted to mnt2.

Next, decompress the rootfs to the newly created partition:
```bash
mkdir mnt
mkdir mnt2
sudo mount /dev/your-device-p2 mnt
sudo tar -zxvf /path/to/openeuler-rootfs.tar.gz -C mnt
```

Mount the original image and copy some necessary files (adjust loop device as needed):
```bash
sudo losetup -f -P milkv-duo-sd-20241106-0012.img
sudo mount /dev/loop0p2 mnt2
sudo cp -r mnt2/mnt/system mnt/mnt
sudo cp mnt2/etc/run_usb.sh mnt/etc/
sudo cp mnt2/etc/uhubon.sh mnt/etc/
sudo cp mnt2/etc/init.d/S99user mnt/etc/init.d/
```

Prepare to enter the image, first create DNS resolution:
```bash
echo "nameserver 8.8.8.8" | sudo tee mnt/etc/resolv.conf
```

Then enter the image:
```bash
chroot mnt
```

Install some necessary packages (e.g., dhcp):
```bash
dnf install dhcp
cat <<EOF >> /etc/dhcp/dhcpd.conf
subnet 192.168.42.0 netmask 255.255.255.0 {
        option routers 192.168.42.1;
        range 192.168.42.100 192.168.42.200;
}
EOF
```

Unmount:
```bash
exit
sudo umount mnt
sudo umount mnt2
```

### Logging into the System

Note that RNDIS may not be available, so it's recommended to have a UART connection.

Log into the system via the serial port.

Username: `root`
Password: `openEuler12#$`

> Note: Due to the Duo's limited performance, the system might freeze for several minutes at login prompt before entering the shell

## Expected Results

The system should boot normally and allow login via the serial port.

## Actual Results

The system booted successfully and login via the serial port was also successful.

### Boot Log

Screen recording (skipping compilation, from image creation to system login):

[![asciicast](https://asciinema.org/a/eoIznNZpjPZSb9mI2NE4wwdzQ.svg)](https://asciinema.org/a/eoIznNZpjPZSb9mI2NE4wwdzQ)

```log
[  OK  ] Started Show Plymouth Boot Screen.
[  OK  ] Started Forward Password R…s to Plymouth Directory Watch.
[  OK  ] Reached target Path Units.
[  OK  ] Reached target Basic System.
         Starting NTP client/server...
         Starting D-Bus System Message Bus...
         Starting Restore /run/initramfs on shutdown...
         Starting Update RTC With System Clock...
         Starting irqbalance daemon...
[  OK  ] Started libstoragemgmt plug-in server daemon.
         Starting Authorization Manager...
[  OK  ] Started Hardware RNG Entropy Gatherer Daemon.
         Starting Self Monitoring a…g Technology (SMART) Daemon...
         Starting OpenSSH ecdsa Server Key Generation...
         Starting OpenSSH ed25519 Server Key Generation...
         Starting OpenSSH rsa Server Key Generation...
         Starting User Login Management...
         Starting Run a configured … scripts at system startup....
[  OK  ] Started D-Bus System Message Bus.
[  OK  ] Finished Restore /run/initramfs on shutdown.
[  OK  ] Finished Update RTC With System Clock.
[  OK  ] Started irqbalance daemon.
[  OK  ] Finished OpenSSH ecdsa Server Key Generation.
[  OK  ] Finished OpenSSH ed25519 Server Key Generation.
[  OK  ] Reached target Sound Card.
[  OK  ] Started Self Monitoring an…ing Technology (SMART) Daemon.
[  OK  ] Started NTP client/server.
[  OK  ] Started Authorization Manager.
         Starting firewalld - dynamic firewall daemon...
[  OK  ] Finished Run a configured …ap scripts at system startup..
[  OK  ] Started User Login Management.
[  OK  ] Started PC/SC Smart Card Daemon.
[  OK  ] Started firewalld - dynamic firewall daemon.
[  OK  ] Reached target Preparation for Network.
         Starting Network Manager...
[  OK  ] Finished OpenSSH rsa Server Key Generation.
[  OK  ] Reached target sshd-keygen.target.
[  OK  ] Stopped firewalld - dynamic firewall daemon.
         Starting firewalld - dynamic firewall daemon...
[  OK  ] Started Network Manager.
[  OK  ] Reached target Network.
         Starting Network Manager Wait Online...
         Starting GSSAPI Proxy Daemon...
         Starting /etc/rc.d/rc.local Compatibility...
         Starting OpenSSH server daemon...
         Starting Dynamic System Tuning Daemon...
[  OK  ] Started /etc/rc.d/rc.local Compatibility.
[  OK  ] Started GSSAPI Proxy Daemon.
[  OK  ] Reached target NFS client services.
[  OK  ] Reached target Preparation for Remote File Systems.
[  OK  ] Reached target Remote File Systems.
         Starting Hostname Service...
         Starting Permit User Sessions...
[  OK  ] Started OpenSSH server daemon.
[  OK  ] Finished Permit User Sessions.
[  OK  ] Started Deferred execution scheduler.
[  OK  ] Started Command Scheduler.
         Starting Hold until boot process finishes up...
         Starting Terminate Plymouth Boot Screen...
[  OK  ] Finished Hold until boot process finishes up.
[  OK  ] Finished Terminate Plymouth Boot Screen.

openEuler 23.09
Kernel 5.10.4-tag- on an riscv64

openeuler-riscv64 login: root
openEuler12#$
Password: 
login: timed out after 60[FAILED] Failed to start Dynamic System Tuning Daemon.
[FAILED] Failed to start firewalld - dynamic firewall daemon.
[  275.471596] bm-dwmac 4070000.ethernet end0: PHY [stmmac-0:00] driver [Generic PHY] (irq=POLL)
[  275.564174] dwmac1000: Master AXI performs any burst length
[  275.612691] bm-dwmac 4070000.ethernet end0: No Safety Features support found
[  275.658329] bm-dwmac 4070000.ethernet end0: IEEE 1588-2002 Timestamp supported
[  275.746979] bm-dwmac 4070000.ethernet end0: configuring for phy/rmii link mode

openEuler 23.09
Kernel 5.10.4-tag- on an riscv64

openeuler-riscv64 login: root
Password: 


Welcome to 5.10.4-tag-

System information as of time:  Mon Sep 18 08:06:49 CST 2023

System load:    8.62
Processes:      67
Memory used:    79.0%
Swap used:      0.0%
Usage On:       7%
Users online:   1


[root@openeuler-riscv64 ~]# ./neofetch
-bash: ./neofetch: No such file or directory
[root@openeuler-riscv64 ~]# uname -a
Linux openeuler-riscv64 5.10.4-tag- #1 PREEMPT Tue Nov 5 23:54:15 CST 2024 riscv64 riscv64 riscv64 GNU/Linux
[root@openeuler-riscv64 ~]# cat /etc/os-release
NAME="openEuler"
VERSION="23.09"
ID="openEuler"
VERSION_ID="23.09"
PRETTY_NAME="openEuler 23.09"
ANSI_COLOR="0;31"

[root@openeuler-riscv64 ~]# 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

