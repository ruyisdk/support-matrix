# Fedora 41 Milk-V Duo 256M 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Fedora 41
- 下载链接：https://mirror.iscas.ac.cn/fedora-riscv/dl/Milk-V/Duo256M/images/latest/milkv-duo-256m-fedora-minimal.img.gz
- 参考安装文档：https://github.com/chainsx/fedora-riscv-builder

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

### 下载镜像

```shell
wget https://mirror.iscas.ac.cn/fedora-riscv/dl/Milk-V/Duo256M/images/latest/milkv-duo-256m-fedora-minimal.img.gz
gzip -d milkv-duo-256m-fedora-minimal.img.gz
```

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
sudo dd if=milkv-duo-256m-fedora-minimal.img of=/dev/your/device bs=4M status=progress 
```

### 登录系统

通过串口登录系统。

用户名：`root`
密码：`riscv`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，能够通过串口登录。

### 启动信息

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

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
