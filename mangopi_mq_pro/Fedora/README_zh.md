# Fedora MangoPi MQ Pro 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://mirror.iscas.ac.cn/fedora-riscv/old_dl/Allwinner/Nezha_D1/images-release/Fedora/fedora-riscv64-d1-developer-xfce-rawhide-Rawhide-20220117-135925.n.0-sda.raw.zst
- 参考安装文档：https://popolon.org/depots/RISC-V/D1/ovsienko/_index.html

### 硬件信息

- MangoPi MQ Pro
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `zstd` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
zstd -kd fedora-riscv64-d1-developer-xfce-rawhide-Rawhide-20220117-135925.n.0-sda.raw.zst
sudo dd if=/path/to/fedora-riscv64-d1-developer-xfce-rawhide-Rawhide-20220104-012902.n.0-sda.raw of=/dev/your_device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名：`root`
默认密码：`fedora_rocks!`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，能够通过板载串口登录。

### 启动信息

```log
         Starting D-Bus System Message Bus...
[  OK  ] Started D-Bus System Message Bus.
[  OK  ] Reached target Basic System.
         Starting Avahi mDNS/DNS-SD Stack...
         Starting Builds and install new kernel modules through DKMS...
         Starting firewalld - dynamic firewall daemon...
         Starting GSSAPI Proxy Daemon...
         Starting LSB: Init script for live image....
         Starting RealtimeKit Scheduling Policy Service...
[  OK  ] Reached target sshd-keygen.target.
         Starting System Security Services Daemon...
         Starting Resets System Activity Logs...
         Starting Home Area Manager...
         Starting Disk Manager...
         Starting Daemon for power management...
[  OK  ] Started GSSAPI Proxy Daemon.
[  OK  ] Finished Resets System Activity Logs.
[  OK  ] Reached target NFS client services.
[  OK  ] Reached target Remote File Systems (Pre).
[  OK  ] Reached target Remote File Systems.
[  OK  ] Started RealtimeKit Scheduling Policy Service.
[  OK  ] Started Avahi mDNS/DNS-SD Stack.
[  OK  ] Started Home Area Manager.
         Starting Load Kernel Module drm...
[  OK  ] Finished Load Kernel Module drm.
         Starting Authorization Manager...
[  OK  ] Started Authorization Manager.
[  OK  ] Finished Builds and install new kernel modules through DKMS.
[  OK  ] Started LSB: Init script for live image..
         Starting NTP client/server...
[  OK  ] Started NTP client/server.
[  OK  ] Started Disk Manager.
[  OK  ] Started System Security Services Daemon.
[  OK  ] Reached target User and Group Name Lookups.
         Starting Accounts Service...
         Starting User Login Management...
[  OK  ] Started Accounts Service.
[  OK  ] Started User Login Management.
[  OK  ] Started Daemon for power management.
[  OK  ] Started firewalld - dynamic firewall daemon.
[  OK  ] Reached target Network (Pre).
         Starting Network Manager...
[  OK  ] Started Network Manager.
[  OK  ] Reached target Network.
         Starting Network Manager Wait Online...
         Starting /etc/rc.d/rc.local Compatibility...
         Starting OpenSSH server daemon...
         Starting Permit User Sessions...
         Starting Hostname Service...
[  OK  ] Finished Permit User Sessions.
[  OK  ] Started OpenSSH server daemon.
[  125.764679] sunxi-rfkill soc@3000000:rfkill@0: block state already is 1
[  OK  ] Started Hostname Service.
         Starting Network Manager Script Dispatcher Service...
[  126.849352] sunxi-rfkill soc@3000000:rfkill@0: set block: 0
[  OK  ] Started Network Manager Script Dispatcher Service.
[  126.964162] sunxi-rfkill soc@3000000:rfkill@0: bt power on success
         Starting Load/Save RF Kill Switch Status...
[  OK  ] Started Load/Save RF Kill Switch Status.
[  128.132882] sunxi-rfkill soc@3000000:rfkill@0: set block: 1
[  128.213790] sunxi-rfkill soc@3000000:rfkill@0: bt power off success
[  128.804497] sunxi-rfkill soc@3000000:rfkill@0: set block: 0
[  128.911636] sunxi-rfkill soc@3000000:rfkill@0: bt power on success
[  129.373465] sunxi-rfkill soc@3000000:rfkill@0: set block: 1
[  129.443708] sunxi-rfkill soc@3000000:rfkill@0: bt power off success
[  129.553369] libphy: 4500000.eth: probed
[  129.613798] sunxi-gmac 4500000.eth eth0: eth0: Type(8) PHY ID 0000ffff at 0 IRQ poll (4500000.eth-0:00)
[  129.681471] sunxi-gmac 4500000.eth eth0: Initialize hardware error
[  129.705082] ------------[ cut here ]------------
[  129.731337] called from state READY
[  129.752993] WARNING: CPU: 0 PID: 535 at drivers/net/phy/phy.c:839 phy_stop+0x84/0x94
[  129.779649] Modules linked in: ip_set nfnetlink ebtable_filter ebtables xradio_btlpm snd_soc_sunxi_daudio snd_soc_sunxi_dmic snd_soc_sunxi_simple_card snd_soc_simple_card_utils snd_soc_sunxi snd_soc_sunxi_hdmi snd_soc_dmic bluetooth ecdh_generic ecc zram i2c_dev libarc4 cfg80211
[  129.850839] CPU: 0 PID: 535 Comm: NetworkManager Not tainted 5.4.61 #5
[  129.876834] sepc: ffffffe00077a900 ra : ffffffe00077a900 sp : ffffffe071f23380
[***   ] (1 of 2) A start job is running for /etc/rc.d/rc.local Compatibility (1min 7s / no limit)
[  129.928383]  gp : ffffffe001268958 tp : ffffffe008801c40 t0 : 0000000000000000
[  129.955513]  t1 : 0000000001806000 t2 : 0000000000000000 s0 : ffffffe071f233b0
[  129.981402]  s1 : ffffffe07999c800 a0 : 0000000000000017 a1 : ffffffe0010ced78
[  130.005777]  a2 : ffffffe0010eb050 a3 : 0000000000000000 a4 : 0000000000000000
[  130.030895]  a5 : 0000000000000000 a6 : 00000000000101a6 a7 : 0000000000000003
[  130.053258] sunxi-rfkill soc@3000000:rfkill@0: set block: 0
[  130.077812]  s2 : 0000000000000002 s3 : ffffffe07999c800 s4 : 0000000000001000
[  130.123611]  s5 : 0000000000001000 s6 : fffffffffffff000 s7 : ffffffe071f23640
[  130.160954] sunxi-rfkill soc@3000000:rfkill@0: bt power on success
[  130.188736]  s8 : ffffffe07afa9010 s9 : 0000000000000000 s10: 0000000000000000
[  130.253787]  s11: 0000000000000000 t3 : 0000000000000000 t4 : 0000000048d18000
[  130.277122]  t5 : 0000000000000003 t6 : 0000000000000001
[  130.301036] sstatus: 0000000200000120 sbadaddr: 0000000000000000 scause: 0000000000000003
[ ***  ] (2 of 2) A start job is running for Network Manager Wait Online (1min 8s / no limit)
[  130.609345] sunxi-rfkill soc@3000000:rfkill@0: set block: 1
[  *** ] (2 of 2) A start job is running for Network Manager Wait Online (1min 8s / no limit)
[   ***] (2 of 2) A start job is running for Network Manager Wait Online (1min 9s / no limit)
[    **] (1 of 2) A start job is running for /etc/rc.d/rc.local Compat[  131.910364] sunxi-rfkill soc@3000000:rfkill@0: set block: 1
ibility (1min 9s / no limit)
[     *] (1 of 2) A start job is running for /etc/rc.d/rc.local Compatibility (1min 10s / no limit)
[  132.545915] sunxi-rfkill soc@3000000:rfkill@0: set block: 0
[    **] (1 of 2) A start job is running for /etc/rc.d/rc.local Compatibility (1min 10s / no limit)
[  133.092570] sunxi-rfkill soc@3000000:rfkill@0: set block: 1
[  133.155100] sunxi-rfkill soc@3000000:rfkill@0: bt power off success
[  133.312801] libphy: 4500000.eth: probed
[   ***] (2 of 2) A start j[  133.406705] sunxi-gmac 4500000.eth eth0: Initialize hardware error
ob is running for Network Manage[  133.429678] ------------[ cut here ]------------
r Wait Online (1min 11s / no limit)
[  133.460930] called from state READY
[  133.487744] WARNING: CPU: 0 PID: 535 at drivers/net/phy/phy.c:839 phy_stop+0x84/0x94
[  133.518538] Modules linked in: ip_set nfnetlink ebtable_filter ebtables xradio_btlpm snd_soc_sunxi_daudio snd_soc_sunxi_dmic snd_soc_sunxi_simple_card snd_soc_simple_card_utils snd_soc_sunxi snd_soc_sunxi_hdmi snd_soc_dmic bluetooth ecdh_generic ecc zram i2c_dev libarc4 cfg80211
[  133.602041] CPU: 0 PID: 535 Comm: NetworkManager Tainted: G        W         5.4.61 #5
[  133.635536] sepc: ffffffe00077a900 ra : ffffffe00077a900 sp : ffffffe071f23380
[  133.663232]  gp : ffffffe001268958 tp : ffffffe008801c40 t0 : 0000000000000000
[  133.689107]  t1 : 0000000001806000 t2 : 0000000000000000 s0 : ffffffe071f233b0
[  133.714933]  s1 : ffffffe07aea6800 a0 : 0000000000000017 a1 : ffffffe0010ced78
[  133.741089]  a2 : ffffffe0010eb050 a3 : 0000000000000000 a4 : 0000000000000000
[  133.767368] sunxi-rfkill soc@3000000:rfkill@0: set block: 0
[  133.790838]  a5 : 0000000000000000 a6 : 00000000000101a6 a7 : 0000000000000003
[  133.835180]  s2 : 0000000000000002 s3 : ffffffe07aea6800 s4 : 0000000000001000
[  133.867529] sunxi-rfkill soc@3000000:rfkill@0: bt power on success
[  *** ] (2 of 2) A start job is running for Network Manager Wait Online (1min 11s / no limit)
[  133.968491]  s8 : ffffffe00884ec10 s9 : 0000000000000000 s10: 0000000000000000
[  134.002467]  s11: 0000000000000000 t3 : 0000000000000000 t4 : 0000000048d18000
[  134.034470]  t5 : 0000000000000003 t6 : 0000000000000001
[  134.063624] sstatus: 0000000200000120 sbadaddr: 0000000000000000 scause: 0000000000000003
[  134.092194] ---[ end trace 9f1d33515090392d ]---
[ ***  ] (2 of 2) A start job is running for Network Manager Wait Online (1min 12s / no limit)
[***   ] (1 of 2) A start job is running for /etc/rc.d/rc.local Compatibility (1min 12s / no limit)
[  135.106282] sunxi-rfkill soc@3000000:rfkill@0: set block: 0
[**    ] (1 of 2) A start job is running for /etc/rc.d/rc.local Compatibility (1min 13s / no limit)
[  135.660365] sunxi-rfkill soc@3000000:rfkill@0: set block: 1
[*     ] (1 of 2) A start job is running for /etc/rc.d/rc.local Compatibility (1min 13s / no limit)
[**    ] (2 of 2) A start job is running for Network Manager Wait Online (1min 14s / no limit)
[  136.496727] sunxi-rfkill soc@3000000:rfkill@0: bt power on success
[  136.769516] libphy: 4500000.eth: probed
[  136.832972] sunxi-gmac 4500000.eth eth0: eth0: Type(8) PHY ID 0000ffff at 0 IRQ poll (4500000.eth-0:00)
[***   ] (2 of 2) A start job is running for Network Manager Wait Online (1min 14s / no limit)
[  136.963626] ------------[ cut here ]------------
[  137.013723] called from state READY
[  137.058026] sunxi-rfkill soc@3000000:rfkill@0: set block: 1
[  137.093692] WARNING: CPU: 0 PID: 535 at drivers/net/phy/phy.c:839 phy_stop+0x84/0x94
[  137.143773] sunxi-rfkill soc@3000000:rfkill@0: bt power off success
[  137.183615] Modules linked in: ebtable_broute ip_set nfnetlink ebtable_filter ebtables xradio_btlpm snd_soc_sunxi_daudio snd_soc_sunxi_dmic snd_soc_sunxi_simple_card snd_soc_simple_card_utils snd_soc_sunxi snd_soc_sunxi_hdmi snd_soc_dmic bluetooth ecdh_generic ecc zram i2c_dev libarc4 cfg80211
[ ***  ] (2 of 2) A start job is running for Network Manager Wait Online (1min 15s / no limit)
[  137.438991] sepc: ffffffe00077a900 ra : ffffffe00077a900 sp : ffffffe071f23380
[  137.513792]  gp : ffffffe001268958 tp : ffffffe008801c40 t0 : 0000000000000000
[  137.555436]  t1 : 0000000001806000 t2 : 0000000000000000 s0 : ffffffe071f233b0
[  137.617643]  s1 : ffffffe0783f1000 a0 : 0000000000000017 a1 : ffffffe0010ced78
[  137.676733]  a2 : ffffffe0010eb050 a3 : 0000000000000000 a4 : 0000000000000000
[  137.737005]  a5 : 0000000000000000 a6 : 000000000001031c a7 : 0000000400000000
[  137.777757]  s2 : 0000000000000002 s3 : ffffffe0783f1000 s4 : 0000000000001000
[  137.805894] sunxi-rfkill soc@3000000:rfkill@0: set block: 0
[  137.852448] sunxi-rfkill soc@3000000:rfkill@0: bt power on success
[  *** ] (1 of 2) A start job is running for /etc/rc.d/rc.local Compatibility (1min 15s / no limit)
[  137.931182]  s8 : ffffffe07aa5b810 s9 : 0000000000000000 s10: 0000000000000000
[  138.003440]  s11: 0000000000000000 t3 : 0000000000000001 t4 : ffffffe0010c7a60
[  138.092390]  t5 : 0000000000000003 t6 : 0000000000000001
[  138.173639] sstatus: 0000000200000120 sbadaddr: 0000000000000000 scause: 0000000000000003
[  OK  ] Started /etc/rc.d/rc.local Compatibility.
         Starting Light Display Manager...
         Starting Hold until boot process finishes up...
[  141.924021] libphy: 4500000.eth: probed
[  141.951430] sunxi-gmac 4500000.eth eth0: eth0: Type(8) PHY ID 0000ffff at 0 IRQ poll (4500000.eth-0:00)
[  142.003782] sunxi-gmac 4500000.eth eth0: Initialize hardware error
[  142.020095] ------------[ cut here ]------------
[  142.038717] called from state READY
[  142.053774] WARNING: CPU: 0 PID: 535 at drivers/net/phy/phy.c:839 phy_stop+0x84/0x94
[  142.073621] Modules linked in: ebtable_nat ebtable_broute ip_set nfnetlink ebtable_filter ebtables xradio_btlpm snd_soc_sunxi_daudio snd_soc_sunxi_dmic snd_soc_sunxi_simple_card snd_soc_simple_card_utils snd_soc_sunxi snd_soc_sunxi_hdmi snd_soc_dmic bluetooth ecdh_generic ecc zram i2c_dev libarc4 cfg80211
[  142.153165] CPU: 0 PID: 535 Comm: NetworkManager Tainted: G        W         5.4.61 #5
[  142.174999] sepc: ffffffe00077a900 ra : ffffffe00077a900 sp : ffffffe071f23380
[  142.193638]  gp : ffffffe001268958 tp : ffffffe008801c40 t0 : 0000000000000000
[  142.220237]  t1 : 0000000001806000 t2 : 0000000000000000 s0 : ffffffe071f233b0
[  142.243413]  s1 : ffffffe078214000 a0 : 0000000000000017 a1 : ffffffe0010ced78
[  142.260552]  a2 : ffffffe0010eb050 a3 : 0000000000000000 a4 : 0000000000000000
[  142.293577]  a5 : 0000000000000000 a6 : 0000000000010327 a7 : 0000000000000000
[  142.301637]  s2 : 0000000000000002 s3 : ffffffe078214000 s4 : 0000000000001000
[  142.343600]  s5 : 0000000000001000 s6 : fffffffffffff000 s7 : ffffffe071f23640
[  142.351660]  s8 : ffffffe008823e10 s9 : 0000000000000000 s10: 0000000000000000
[  142.393574]  s11: 0000000000000000 t3 : 6bcdf87751cf6cdb t4 : 0000000000000000
[  142.401661]  t5 : 0000000000000003 t6 : 0000000000000001
[  142.433624] sstatus: 0000000200000120 sbadaddr: 0000000000000000 scause: 0000000000000003
[  142.442779] ---[ end trace 9f1d33515090392f ]---
[  145.704015] libphy: 4500000.eth: probed
[  145.720359] sunxi-gmac 4500000.eth eth0: eth0: Type(8) PHY ID 0000ffff at 0 IRQ poll (4500000.eth-0:00)
[  145.793747] sunxi-gmac 4500000.eth eth0: Initialize hardware error
[  145.800681] ------------[ cut here ]------------
[  145.833651] called from state READY
[  145.837621] WARNING: CPU: 0 PID: 535 at drivers/net/phy/phy.c:839 phy_stop+0x84/0x94
[  145.873607] Modules linked in: ebtable_nat ebtable_broute ip_set nfnetlink ebtable_filter ebtables xradio_btlpm snd_soc_sunxi_daudio snd_soc_sunxi_dmic snd_soc_sunxi_simple_card snd_soc_simple_card_utils snd_soc_sunxi snd_soc_sunxi_hdmi snd_soc_dmic bluetooth ecdh_generic ecc zram i2c_dev libarc4 cfg80211
[  145.963609] CPU: 0 PID: 535 Comm: NetworkManager Tainted: G        W         5.4.61 #5
[  145.972445] sepc: ffffffe00077a900 ra : ffffffe00077a900 sp : ffffffe071f23380
[  146.013573]  gp : ffffffe001268958 tp : ffffffe008801c40 t0 : ffffffe0012880c8
[  146.021632]  t1 : 0000000000000064 t2 : 0000000000000000 s0 : ffffffe071f233b0
[  146.063603]  s1 : ffffffe07afd4000 a0 : 0000000000000017 a1 : 000000000000000a
[  146.071662]  a2 : 0000000000000000 a3 : 0000000000000007 a4 : 0000000000000001
[  146.123597]  a5 : 0000000000000000 a6 : 00000000000002b3 a7 : 0000000000000006
[  146.134252]  s2 : 0000000000000002 s3 : ffffffe07afd4000 s4 : 0000000000001000
[  146.142341]  s5 : 0000000000001000 s6 : fffffffffffff000 s7 : ffffffe071f23640
[  146.179496]  s8 : ffffffe07aa5ba10 s9 : 0000000000000000 s10: 0000000000000000
[  146.195528]  s11: 0000000000000000 t3 : ffffffe001273df8 t4 : 000000000002eb40
[  146.222785]  t5 : 000000000002eb40 t6 : ffffffe0012743be
[  146.235756] sstatus: 0000000200000120 sbadaddr: 0000000000000000 scause: 0000000000000003
[  146.263656] ---[ end trace 9f1d335150903930 ]---

Welcome to the Fedora/RISC-V disk image
https://fedoraproject.org/wiki/Architectures/RISC-V

Build date: Tue Nov 16 19:18:13 UTC 2021

Kernel 5.4.61 on an riscv64 (ttyS0)

The root password is 'fedora_rocks!'.
root password logins are disabled in SSH starting Fedora 31.
User 'riscv' with password 'fedora_rocks!' in 'wheel' group is provided.

To install new packages use 'dnf install ...'

To upgrade disk image use 'dnf upgrade --best'

If DNS isn’t working, try editing ‘/etc/yum.repos.d/fedora-riscv.repo’.

For updates and latest information read:
https://fedoraproject.org/wiki/Architectures/RISC-V

Fedora/RISC-V
-------------
Koji:               http://fedora.riscv.rocks/koji/
SCM:                http://fedora.riscv.rocks:3000/
Distribution rep.:  http://fedora.riscv.rocks/repos-dist/
Koji internal rep.: http://fedora.riscv.rocks/repos/
fedora-riscv login: root
Password: 
[  231.444955] systemd-xdg-autostart-generator[902]: Not generating service for XDG autostart app-xdg\x2duser\x2ddirs-autostart.service, startup phases are not supported.
[  231.462071] systemd-xdg-autostart-generator[902]: Not generating service for XDG autostart app-gsettings\x2ddata\x2dconvert-autostart.service, startup phases are not supported.
[  231.481650] systemd-xdg-autostart-generator[902]: Not generating service for XDG autostart app-gnome\x2dkeyring\x2dssh-autostart.service, startup phases are not supported.
[  231.501057] systemd-xdg-autostart-generator[902]: Not generating service for XDG autostart app-xapp\x2dsn\x2dwatcher-autostart.service, startup phases are not supported.
[  231.519883] systemd-xdg-autostart-generator[902]: Not generating service for XDG autostart app-at\x2dspi\x2ddbus\x2dbus-autostart.service, startup phases are not supported.
[  231.540705] systemd-xdg-autostart-generator[902]: gnome-systemd-autostart-condition not found: No such file or directory
[  231.554114] systemd-xdg-autostart-generator[902]: Not generating service for XDG autostart app-gnome\x2dkeyring\x2dsecrets-autostart.service, startup phases are not supported.
[  231.573831] systemd-xdg-autostart-generator[902]: Not generating service for XDG autostart app-gnome\x2dkeyring\x2dpkcs11-autostart.service, startup phases are not supported.
Last login: Mon Dec 13 02:41:09 on pts/0
[root@fedora-riscv ~]# uname -a
Linux fedora-riscv 5.4.61 #5 PREEMPT Tue Dec 7 21:35:21 CST 2021 riscv64 riscv64 riscv64 GNU/Linux
[root@fedora-riscv ~]# cat /etc/os-release 
NAME=Fedora
VERSION="33 (Rawhide)"
ID=fedora
VERSION_ID=33
VERSION_CODENAME=""
PLATFORM_ID="platform:f33"
PRETTY_NAME="Fedora 33 (Rawhide)"
ANSI_COLOR="0;34"
LOGO=fedora-logo-icon
CPE_NAME="cpe:/o:fedoraproject:fedora:33"
HOME_URL="https://fedoraproject.org/"
DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora/rawhide/system-administrators-guide/"
SUPPORT_URL="https://fedoraproject.org/wiki/Communicating_and_getting_help"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=rawhide
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=rawhide
PRIVACY_POLICY_URL="https://fedoraproject.org/wiki/Legal:PrivacyPolicy"
[root@fedora-riscv ~]# lscpu
Architecture:        riscv64
Byte Order:          Little Endian
CPU(s):              1
On-line CPU(s) list: 0
Thread(s) per core:  1
Core(s) per socket:  1
Socket(s):           1
CPU max MHz:         1008.0000
CPU min MHz:         1008.0000
[root@fedora-riscv ~]# 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。