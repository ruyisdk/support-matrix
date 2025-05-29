# NixOS Pine64 Star64 测试报告

## 测试环境

### 操作系统信息

- 系统版本：24.05.20231124
- 源码链接: https://git.sr.ht/~fgaz/nixos-star64
- 参考安装文档: https://git.sr.ht/~fgaz/nixos-star64

### 硬件信息

- Pine64 Star64
- microSD 卡一张
- DC 12V5A 圆头电源适配器
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 编译镜像

如果主机运行 NixOS, 使用 `nix build .#sd-image-cross` 编译镜像即可。如使用 8GB 版 Star64, 使用 `nix build .#sd-image-cross-8gb`。

对于其他发行版，不建议直接安装并使用 `nix` 包管理器，推荐使用 Nix 的官方 Docker 镜像：
```shell
docker run -ti -v $(pwd):/work ghcr.io/nixos/nix
```

在 Docker 容器中：

```shell
echo "max-jobs = auto" >> /etc/nix/nix.conf # 使用多核编译
echo "substituters = https://mirrors.tuna.tsinghua.edu.cn/nix-channels/store https://cache.nixos.org/" >> /etc/nix/nix.conf # 更换镜像源
cd /work
nix build .#sd-image-cross --extra-experimental-features nix-command --extra-experimental-features flakes
```

生成的镜像文件名形如`nixos_sd_image_24_05_20231124_5a09cb4_riscv64_linux_pine64_star64.zst`。

### 刷写镜像到 microSD 卡

使用 `dd` 将镜像写入至 microSD 卡。

### 登录系统

通过串口登录系统。

默认用户：`nixos`

默认密码：`nixos`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

启动时 Kernel panic，无法进入系统。

### 启动信息

```log

Welcome to NixOS 24.05 (Uakari)!

[   12.206584] systemd[1]: Hostname set to <nixos>.
[   12.753590] systemd[1]: bpf-lsm: BPF LSM hook not enabled in the kernel, BPF LSM not supported
[   13.844478] systemd[1]: Queued start job for default target Multi-User System.
[   13.863717] systemd[1]: Created slice Slice /system/getty.
[  OK  ] Created slice Slice /system/getty.
[   13.908384] systemd[1]: Created slice Slice /system/modprobe.
[  OK  ] Created slice Slice /system/modprobe.
[   13.948702] systemd[1]: Created slice Slice /system/serial-getty.
[  OK  ] Created slice Slice /system/serial-getty.
[   13.988167] systemd[1]: Created slice User and Session Slice.
[  OK  ] Created slice User and Session Slice.
[   14.025937] systemd[1]: Started Dispatch Password Requests to Console Directory Watch.
[  OK  ] Started Dispatch Password Requests to Console Directory Watch.
[   14.065833] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[  OK  ] Started Forward Password Requests to Wall Directory Watch.
[   14.105786] systemd[1]: Reached target Local Encrypted Volumes.
[  OK  ] Reached target Local Encrypted Volumes.
[   14.145699] systemd[1]: Reached target Containers.
[  OK  ] Reached target Containers.
[   14.175857] systemd[1]: Reached target Path Units.
[  OK  ] Reached target Path Units.
[   14.205621] systemd[1]: Reached target Remote File Systems.
[  OK  ] Reached target Remote File Systems.
[   14.245571] systemd[1]: Reached target Slice Units.
[  OK  ] Reached target Slice Units.
[   14.275640] systemd[1]: Reached target Swaps.
[  OK  ] Reached target Swaps.
[   14.318648] systemd[1]: Listening on Process Core Dump Socket.
[  OK  ] Listening on Process Core Dump Socket.
[   14.356304] systemd[1]: Listening on Journal Socket (/dev/log).
[  OK  ] Listening on Journal Socket (/dev/log).
[   14.396564] systemd[1]: Listening on Journal Socket.
[  OK  ] Listening on Journal Socket.
[   14.436591] systemd[1]: Listening on Userspace Out-Of-Memory (OOM) Killer Socket.
[  OK  ] Listening on Userspace Out-Of-Memory (OOM) Killer Socket.
[   14.502117] systemd[1]: Listening on udev Control Socket.
[  OK  ] Listening on udev Control Socket.
[   14.536324] systemd[1]: Listening on udev Kernel Socket.
[  OK  ] Listening on udev Kernel Socket.
[   14.581983] systemd[1]: Mounting Huge Pages File System...
         Mounting Huge Pages File System...
[   14.622134] systemd[1]: Mounting POSIX Message Queue File System...
         Mounting POSIX Message Queue File System...
[   14.661923] systemd[1]: Mounting Kernel Debug File System...
         Mounting Kernel Debug File System...
[   14.702258] systemd[1]: Starting Create List of Static Device Nodes...
         Starting Create List of Static Device Nodes...
[   14.742681] systemd[1]: Starting Load Kernel Module configfs...
         Starting Load Kernel Module configfs...
[   14.782217] systemd[1]: Starting Load Kernel Module drm...
         Starting Load Kernel Module drm...
[   14.822119] systemd[1]: Starting Load Kernel Module efi_pstore...
         Starting Load Kernel Module efi_pstore...
[   14.862241] systemd[1]: Starting Load Kernel Module fuse...
         Starting Load Kernel Module fuse...
[   14.901923] systemd[1]: Starting mount-pstore.service...
         Starting mount-pstore.service...
[   14.943249] systemd[1]: Starting Create SUID/SGID Wrappers...
         Starting Create SUID/SGID Wrappers...
[   14.976167] systemd[1]: File System Check on Root Device was skipped because of an unmet condition check (ConditionPathIsReadWrite=!/).
[   14.999335] systemd[1]: Starting Journal Service...
         Starting Journal Service...
[   15.048735] systemd[1]: Starting Load Kernel Modules...
         Starting Load Kernel Modules...
[   15.072078] systemd[1]: Starting Remount Root and Kernel File Systems...
         Starting Remou[   15.082470] fuse: init (API version 7.34)
nt Root and Kernel File Systems...
[   15.121679] EXT4-fs (mmcblk1p3): re-mounted. Opts: (null). Quota mode: none.
[   15.123234] systemd[1]: Starting Coldplug All udev Devices...
[   15.137639] systemd-journald[355]: Collecting audit messages is disabled.
         Startin[   15.145417] pps_core: LinuxPPS API ver. 1 registered
g Coldp[   15.150961] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
lug All udev Devices...
[   15.188237] PTP clock support registered
[   15.209501] systemd[1]: Mounted Huge Pages File System.
[  OK  ] Mounted Huge Pages File System.
[   15.246419] systemd[1]: Mounted POSIX Message Queue File System.
[  OK  ] Mounted POSIX Message Queue File System.
[   15.286430] systemd[1]: Started Journal Service.
[  OK  ] Started Journal Service.
[  OK  ] Mounted Kernel Debug File System.
[  OK  ] Finished Create List of Static Device Nodes.
[  OK  ] Finished Load Kernel Module configfs.
[  OK  ] Finished Load Kernel Module drm.
[  OK  ] Finished Load Kernel Module efi_pstore.
[  OK  ] Finished Load Kernel Module fuse.
[  OK  ] Finished Remount Root and Kernel File Systems.
         Mounting FUSE Control File System...
         Mounting Kernel Configuration File System...
         Starting Flush Journal to Persistent Storage...
[   15.743323] systemd-journald[355]: Received client request to flush runtime journal.
         Starting Load/Save OS Random Seed...
[   15.756850] systemd-journald[355]: File /var/log/journal/7d2afd7d963849a5aeb1f01b9da54783/system.journal corrupted or uncleanly shut down, renaming and replacing.
         Starting Create Static Device Nodes in /dev gracefully...
[  OK  ] Finished Create SUID/SGID Wrappers.
[   15.868873] starfive-eth-plat 16030000.ethernet: User ID: 0x41, Synopsys ID: 0x52
[   15.880919] starfive-eth-plat 16030000.ethernet:     DWMAC4/5
[   15.886504] starfive-eth-plat 16030000.ethernet: DMA HW capability register supported
[   15.894384] starfive-eth-plat 16030000.ethernet: RX Checksum Offload Engine supported
[   15.894396] starfive-eth-plat 16030000.ethernet: Wake-Up On Lan supported
[   15.894622] starfive-eth-plat 16030000.ethernet: TSO supported
[   15.915013] starfive-eth-plat 16030000.ethernet: Enable RX Mitigation via HW Watchdog Timer
[  OK     15.924500] starfive-eth-plat 16030000.ethernet: Enabled L3L4 Flow TC (entries=1)
0m] Mounted    15.932858] starfive-eth-plat 16030000.ethernet: Enabled RFS Flow TC (entries=8)
1;39mFUSE Contro[   15.941608] starfive-eth-plat 16030000.ethernet: TSO feature enabled
l File System   15.949324] starfive-eth-plat 16030000.ethernet: Using 40 bits DMA width
m.
[  OK  ] Mounted Kernel Configuration File System.
[  OK  ] Finished Flush Journal to Persistent Storage.
[  OK  ] Finished Create Static Device Nodes in /dev gracefully.
         Starting Create Static Device Nodes in /dev...
[  OK  ] Finished Create Static Device Nodes in /dev.
[  OK  ] Reached target Preparation for Local File Systems.
[  OK  ] Reached target Local File Systems.
[   16.479546] YT8531 Gigabit Ethernet stmmac-0:00: attached PHY driver (mii_bus:phy_addr=stmmac-0:00, irq=POLL)
[   16.489529] YT8531 Gigabit Ethernet stmmac-0:01: attached PHY driver (mii_bus:phy_addr=stmmac-0:01, irq=POLL)
         Starting Create Volatile Files and Directories[   16.515305] starfive-eth-plat 16040000.ethernet: User ID: 0x41, Synopsys ID: 0x52
...
[   16.524026] starfive-eth-plat 16040000.ethernet:     DWMAC4/5
[   16.530264] starfive-eth-plat 16040000.ethernet: DMA HW capability register supported
[   16.538150] starfive-eth-plat 16040000.ethernet: RX Checksum Offload Engine supported
[   16.546028] starfive-eth-plat 16040000.ethernet: Wake-Up On Lan supported
[   16.552942] starfive-eth-plat 16040000.ethernet: TSO supported
[   16.558844] starfive-eth-plat 16040000.ethernet: Enable RX Mitigation via HW Watchdog Timer
[   16.558859] starfive-eth-plat 16040000.ethernet: Enabled L3L4 Flow TC (entries=1)
[   16.558871] starfive-eth-plat 16040000.ethernet: Enabled RFS Flow TC (entries=8)
[   16.558884] starfive-eth-plat 16040000.ethernet: TSO feature enabled
[   16.588705] starfive-eth-plat 16040000.ethernet: Using 40 bits DMA width
         Starting Rule-based Manager for Device Events and Files...
[  OK  ] Finished Coldplug All udev Devices.
[  OK  ] Finished Create Volatile Files and Directories.
         Starting Userspace Out-Of-Memory (OOM) Killer...
         Starting Network Time Synchronization...
         Starting Record System Boot/Shutdown in UTMP...
[  OK  ] Started Rule-based Manager for Device Events and Files.
[   16.892044] YT8531 Gigabit Ethernet stmmac-1:00: attached PHY driver (mii_bus:phy_addr=stmmac-1:00, irq=POLL)
[   16.916648] YT8531 Gigabit Ethernet stmmac-1:01: attached PHY driver (mii_bus:phy_addr=stmmac-1:01, irq=POLL)
[  OK  ] Finished Record System Boot/Shutdown in UTMP.
[  OK  ] Found device /dev/hvc0.
[   17.176677] starfive-eth-plat 16030000.ethernet end0: renamed from eth0
[  OK  ] Started Userspace Out-Of-Memory (OOM) Killer.
[  OK  ] Finished mount-pstore.service.
[   17.578975] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
[  OK  ] Started Network Time Synchronization.
[   17.921204] tun: Universal TUN/TAP device driver, 1.6
[   17.986837] loop: module loaded
[  OK  ] Finished Load Kernel Modules.
[   18.515268] cpu cpu0: cpufreq_init: failed to get clk: -2
[   18.521602] cpu cpu0: cpufreq_init: failed to get clk: -2
[   18.527197] cpu cpu0: cpufreq_init: failed to get clk: -2
[   18.566801] cpu cpu0: cpufreq_init: failed to get clk: -2
[   18.591274] cpufreq-dt cpufreq-dt: failed register driver: -19
[   18.667164] cdns3-starfive 10210000.usbdrd: usb mode 1 3.0 probe success
[   18.831029] mailbox 13060000.mailbox: Mailbox enabled
[   18.854267] ssp-pl022 10060000.spi: ARM PL022 driver, device ID: 0x00041022
[   18.925559] thermal thermal_zone0: failed to read out thermal zone (-110)
[   18.933456] mailbox_test mailbox_client: invalid resource
[   18.938943] mailbox_test mailbox_client: invalid resource
[   18.944484] mailbox_test mailbox_client: Successfully registered
[   19.015436] random: crng init done
[   19.026461] ssp-pl022 10060000.spi: mapped registers from 0x0000000010060000 to 000000004bbe1b92
[  OK  ] Finished Load/Save OS Random Seed.
[   19.073503] starfive-wdt 13070000.wdog: Heartbeat: timeout=15, count/2=180000000 (0aba9500)
[   19.085780] mc: Linux media interface: v0.10
[   19.149708] ssp-pl022 10060000.spi: setup for DMA on RX dma1chan0, TX dma1chan1
[   19.170895] starfive-rtc 17040000.rtc: registered as rtc0
[   19.205425] dwmmc_starfive 16020000.sdio1: Unexpected interrupt latency
[   19.391297] Unable to handle kernel paging request at virtual address fffffffffffffff8
[   19.391313] jh7110-sec 16000000.crypto: Unable to request sec_m dma channel in DMA channel
[   19.399254] Oops [#1]
[   19.399263] Modules linked in: jh7110_crypto(+) snd starfive_trng(+) rtc_starfive rng_core mc starfive_wdt rtc_hym8563(+)
[   19.407597] jh7110-sec 16000000.crypto: Cannot initial dma chan
[   19.409855]  crypto_engine firmware_class watchdog sfctemp spi_cadence_quadspi spi_pl022 starfive_mailbox_test starfive_mailbox leds_gpio rfkill_gpio led_class rfkill pwm_starfive_ptc soundcore cdns3_starfive usb_common cpufreq_dt atkbd libps2 serio loop tun uio_pdrv_genirq tap uio macvlan bridge stp llc motorcomm dwmac_starfive_plat stmmac_platform stmmac pcs_xpcs phylink of_mdio fixed_phy fwnode_mdio libphy ptp pps_core fuse pstore ip_tables x_tables autofs4 ext4 crc32c_generic crc16 mbcache jbd2 mmc_block axp15060_regulator regmap_i2c dw_mmc_starfive dw_mmc_pltfm dw_mmc mmc_core i2c_designware_platform 8250_dw i2c_designware_core dm_mod
[   19.483750] CPU: 0 PID: 531 Comm: (udev-worker) Not tainted 5.15.131 #1-NixOS
[   19.490898] Hardware name: Pine64 Star64 (DT)
[   19.495263] epc : swake_up_locked+0x1e/0x4e
[   19.499467]  ra : complete+0x3e/0x58
[   19.503054] epc : ffffffff80059716 ra : ffffffff80059a1e sp : ffffffd0047435a0
[   19.510288]  gp : ffffffff815593e8 tp : ffffffe0c5f55240 t0 : 0000000000046000
[   19.517521]  t1 : 00000000b964e27c t2 : 0000000000000001 s0 : ffffffd0047435c0
[   19.524753]  s1 : 0000000000000000 a0 : ffffffe0c7e986d0 a1 : ffffffe0c7e98628
[   19.531985]  a2 : 0000000000000000 a3 : 0000000000000001 a4 : 0000000000000000
[   19.539216]  a5 : ffffffe0c7e986d8 a6 : c8a2e0c3e8ea2bc6 a7 : a29f7bb400000000
[   19.546450]  s2 : ffffffe0c7e986d0 s3 : 0000000200000120 s4 : ffffffd004743684
[   19.553683]  s5 : 0000000000000001 s6 : 0000000000000016 s7 : 0000000000000002
[   19.560914]  s8 : ffffffff8152e700 s9 : ffffffff8152e6c0 s10: ffffffe0c0010800
[   19.568146]  s11: 0000000000000016 t3 : 000000000000ff3d t4 : 0000000000000d48
[   19.575377]  t5 : 000000ff00000000 t6 : ffffffff81495ce8
[   19.580695] status: 0000000200000100 badaddr: fffffffffffffff8 cause: 000000000000000d
[   19.588622] [<ffffffff80059716>] swake_up_locked+0x1e/0x4e
[   19.594121] [<ffffffff80059a1e>] complete+0x3e/0x58
[   19.599015] [<ffffffff02fde86e>] starfive_trng_irq+0x7c/0x114 [starfive_trng]
[   19.606270] [<ffffffff80076c74>] __handle_irq_event_percpu+0x5e/0x1a4
[   19.612725] [<ffffffff80076eac>] handle_irq_event+0x7a/0xe6
[   19.618311] [<ffffffff8007b382>] handle_fasteoi_irq+0xa4/0x202
[   19.624159] [<ffffffff80075ddc>] generic_handle_domain_irq+0x28/0x36
[   19.630530] [<ffffffff803f5d9e>] plic_handle_irq+0x86/0xf2
[   19.636034] [<ffffffff8007655c>] handle_domain_irq+0x68/0x9c
[   19.641704] [<ffffffff803f5baa>] riscv_intc_irq+0x3e/0x66
[   19.647118] [<ffffffff800029b0>] ret_from_exception+0x0/0xc
[   19.652712] ---[ end trace 81585e2092073ed8 ]---
[   19.657339] Kernel panic - not syncing: Fatal exception in interrupt
[   19.663697] SMP: stopping secondary CPUs
[   19.667642] ---[ end Kernel panic - not syncing: Fatal exception in interrupt ]---
```


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试失败。
