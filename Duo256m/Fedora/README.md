---
sys: fedora
sys_ver: 41
sys_var: null

status: basic
last_update: 2024-11-06
---

# Fedora 41 Milk-V Duo 256M Test Report

## Test Environment

### Operating System Information

- System Version: Fedora 41
- Download Link: https://mirror.iscas.ac.cn/fedora-riscv/dl/Milk-V/Duo256M/images/latest/milkv-duo-256m-fedora-minimal.img.gz
- Reference Installation Document: https://github.com/chainsx/fedora-riscv-builder

### Hardware Information

- Milk-V Duo 256M
- A USB power adapter
- A USB-A to C or USB-C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three DuPont wires
- The Milk-V Duo has pre-soldered pin headers required for debugging
- Optional: Milk-V Duo IOB (baseboard)

## Installation Steps

### Download image

```shell
wget https://mirror.iscas.ac.cn/fedora-riscv/dl/Milk-V/Duo256M/images/latest/milkv-duo-256m-fedora-minimal.img.gz
gzip -d milkv-duo-256m-fedora-minimal.img.gz
```

### Flash the image to microSD card via `dd`

```shell
sudo dd if=milkv-duo-256m-fedora-minimal.img of=/dev/your/device bs=4M status=progress 
```

### Logging into the System

Log into the system via the serial port.

Username: `root`
Password: `riscv`

## Expected Results

The system should boot normally and allow login via the serial port.

## Actual Results

The system boots up normally and login through the serial port is successful.

### Boot Log

```log
[   43.503010] ext4 filesystem being remounted at /run/systemd/mount-rootfs/etc supports timestamps until 2038 (0x7fffffff)
ext4 filesystem being remounted at /run/systemd/mount-rootfs/etc supports timestamps u[   43.561180] ext4 filesystem being remounted at /run/systemd/mount-rootfs/var/tmp supports timestamps until 2038 (0x7fffffff)
ntil 2038 (0x7fffffff)
[   43.618343] ext4 filesystem being remounted at /run/systemd/mount-rootfs/var/lib/systemd/linger supports timestamps until 2038 (0x7fffffff)
ext4 filesystem being remounted at /run/systemd/mount-rootfs/var/tmp supports timestamps until 2038 (0x7fffffff)
ext4 filesystem being remounted at /run/systemd/mount-rootfs/var/lib/systemd/linger supports timestamps until 2038 (0x7fffffff)
[  OK  ] Started chronyd.service - NTP client/server.
[   43.760880] ext4 filesystem being remounted at /run/systemd/mount-rootfs/etc supports timestamps until 2038 (0x7fffffff)
ext4 filesystem being remounted at /run/systemd/mount-rootfs/etc supports timestamps until 2038 (0x7fffffff)
[   44.319275] ext4 filesystem being remounted at /run/systemd/mount-rootfs/var/lib/systemd/linger supports timestamps until 2038 (0x7fffffff)
ext4 filesystem being remounted at /run/systemd/mount-rootfs/var/lib/systemd/linger supports timestamps until 2038 (0x7fffffff)
[   44.390019] ext4 filesystem being remounted at /run/systemd/mount-rootfs/var/tmp supports timestamps until 2038 (0x7fffffff)
ext4 filesystem being remounted at /run/systemd/mount-rootfs/var/tmp supports timestamps until 2038 (0x7fffffff)
[  OK  ] Started systemd-logind.service - User Login Management.
[  OK  ] Started firewalld.service - firewalld - dynamic firewall daemon.
[  OK  ] Reached target network-pre.target - Preparation for Network.
         Starting NetworkManager.service - Network Manager...
         Starting systemd-hostnamed.service - Hostname Service...
[   ***] (1 of 3) Job NetworkManager.service/start running (39s / 10min 37s)
[   52.831019] ext4 filesystem being remounted at /run/systemd/mount-rootfs/var/tmp supports timestamps until 2038 (0x7fffffff)
[   52.857149] ext4 filesystem being remounted at /run/systemd/mount-rootfs/etc supports timestamps until 2038 (0x7fffffff)
ext4 filesystem being remounted at /run/systemd/mount-rootfs/var/tmp supports timestamps until 2038 (0x7fffffff)
ext4 filesystem being remounted at /run/systemd/mount-rootfs/etc supports timestamps until 2038 (0x7fffffff)
[   52.920571] ext4 filesystem being remounted at /run/systemd/mount-rootfs/etc supports timestamps until 2038 (0x7fffffff)
[    **] (1 of 3) Job NetworkManager.service/start running (40s / 10min 37s)
[   53.296903] ext4 filesystem being remounted at /run/systemd/mount-rootfs/var/tmp supports timestamps until 2038 (0x7fffffff)
[  OK  ] Started systemd-hostnamed.service - Hostname Service.
         Starting NetworkManager-dispatcher…anager Script Dispatcher Service...
[   54.148737] bm-dwmac 4070000.ethernet end0: PHY [stmmac-0:00] driver [CVITEK CV182XA] (irq=POLL)
bm-dwmac 4070000.ethernet end0: PHY [stmmac-0:00] driver [CVITEK CV182XA] (irq=POLL)
[   54.188755] dwmac1000: Master AXI performs any burst length
[   54.203349] bm-dwmac 4070000.ethernet end0: No Safety Features support found
dwmac1000: Master AXI performs any burst length
bm-dwmac 4070000.ethernet end0: No Safety Features support found
[   54.232757] bm-dwmac 4070000.ethernet end0: IEEE 1588-2002 Timestamp supported
bm-dwmac 4070000.ethernet end0: IEEE 1588-2002 Timestamp supported
[   54.268785] bm-dwmac 4070000.ethernet end0: configuring for phy/rmii link mode
bm-dwmac 4070000.ethernet end0: configuring for phy/rmii link mode
[  OK  ] Started NetworkManager.service - Network Manager.
[  OK  ] Reached target network.target - Network.
         Starting systemd-user-sessions.service - Permit User Sessions...
[  OK  ] Started NetworkManager-dispatcher.… Manager Script Dispatcher Service.
[  OK  ] Finished systemd-user-sessions.service - Permit User Sessions.
         Starting plymouth-quit-wait.servic…d until boot process finishes up...
         Starting plymouth-quit.service - Terminate Plymouth Boot Screen...

Welcome to the Fedora RISC-V disk image
https://openkoji.iscas.ac.cn/koji/

Build date: Mon Jul  1 03:20:03 UTC 2024

Kernel 5.10.4-tag- on an riscv64 (ttyS0)

The root password is 'riscv'.
root password logins are disabled in SSH starting Fedora.

If DNS isn’t working, try editing ‘/etc/yum.repos.d/fedora-riscv.repo’.

For updates and latest information read:
https://fedoraproject.org/wiki/Architectures/RISC-V

Fedora RISC-V
-------------
fedora-riscv login: [   64.537916] bm-dwmac 4070000.ethernet end0: Link is Up - 100Mbps/Full - flow control rx/tx
[   64.546521] IPv6: ADDRCONF(NETDEV_CHANGE): end0: link becomes ready
[   65.561998] bm-dwmac 4070000.ethernet end0: Link is Down
root
[   69.658044] bm-dwmac 4070000.ethernet end0: Link is Up - 100Mbps/Full - flow control rx/tx
Password: 
[root@fedora-riscv ~]# uname -a
Linux fedora-riscv 5.10.4-tag- #1 PREEMPT Thu Jul 11 15:36:05 CST 2024 riscv64 GNU/Linux
[root@fedora-riscv ~]# cat /etc/os-release 
NAME="Fedora Linux"
VERSION="41 (Rawhide Prerelease)"
ID=fedora
VERSION_ID=41
VERSION_CODENAME=""
PLATFORM_ID="platform:f41"
PRETTY_NAME="Fedora Linux 41 (Rawhide Prerelease)"
ANSI_COLOR="0;38;2;60;110;180"
LOGO=fedora-logo-icon
CPE_NAME="cpe:/o:fedoraproject:fedora:41"
DEFAULT_HOSTNAME="fedora"
HOME_URL="https://fedoraproject.org/"
DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora/rawhide/system-administrators-guide/"
SUPPORT_URL="https://ask.fedoraproject.org/"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=rawhide
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=rawhide
SUPPORT_END=2025-05-13
[root@fedora-riscv ~]# 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
