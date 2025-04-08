# BuildRoot Milk-V Duo 256M 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Duo-V1.1.4
- 下载链接：https://github.com/milkv-duo/duo-buildroot-sdk/releases
- 参考安装文档：https://github.com/milkv-duo/duo-buildroot-sdk

### 硬件信息

- Milk-V Duo 256M
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张

## 安装步骤

### 下载 Duo 的镜像

```bash
wget https://github.com/milkv-duo/duo-buildroot-sdk/releases/download/v1.1.4/milkv-duo256m-sd-v1.1.4.img.zip
unzip milkv-duo256m-sd-v1.1.4.img.zip
```

### 刷写镜像

用 dd 刷写镜像到 sd 卡：
```bash
sudo dd if=milkv-duo256m-sd-v1.1.4.img of=/dev/your/device bs=1M status=progress
```

### 登录系统

通过串口或 ssh 登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
Starting kernel ...

[    0.000000] Linux version 5.10.4-tag- (root@6af018e1172e) (riscv64-unknown-linux-musl-gcc (Xuantie-900 linux-5.10.4 musl gcc Toolchain V2.6.1 B-20220906) 10.2.0, GNU ld (GNU Binutils) 2.35) #1 PREEMPT Fri Nov 22 11:42:16 CST 2024
[    0.000000] earlycon: sbi0 at I/O port 0x0 (options '')
[    0.000000] printk: bootconsole [sbi0] enabled
[    0.000000] efi: UEFI not found.
[    0.000000] Ion: Ion memory setup at 0x000000008b300000 size 75 MiB
[    0.000000] OF: reserved mem: initialized node ion, compatible id ion-region
[    0.000000] Zone ranges:
[    0.000000]   DMA32    [mem 0x0000000080000000-0x000000008fdfffff]
[    0.000000]   Normal   empty
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000080000000-0x000000008fdfffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000080000000-0x000000008fdfffff]
[    0.000000] On node 0 totalpages: 65024
[    0.000000]   DMA32 zone: 889 pages used for memmap
[    0.000000]   DMA32 zone: 0 pages reserved
[    0.000000]   DMA32 zone: 65024 pages, LIFO batch:15
[    0.000000] SBI specification v0.3 detected
[    0.000000] SBI implementation ID=0x1 Version=0x9
[    0.000000] SBI v0.2 TIME extension detected
[    0.000000] SBI v0.2 IPI extension detected
[    0.000000] SBI v0.2 RFENCE extension detected
[    0.000000] riscv: ISA extensions acdfimsuv
[    0.000000] riscv: ELF capabilities acdfimv
[    0.000000] pcpu-alloc: s0 r0 d32768 u32768 alloc=1*32768
[    0.000000] pcpu-alloc: [0] 0
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 64135
[    0.000000] Kernel command line: root=/dev/mmcblk0p2 rootwait rw console=ttyS0,115200 earlycon=sbi riscv.fwsz=0x80000 loglevel=9
[    0.000000] Dentry cache hash table entries: 32768 (order: 6, 262144 bytes, linear)
[    0.000000] Inode-cache hash table entries: 16384 (order: 5, 131072 bytes, linear)
[    0.000000] Sorting __ex_table...
[    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
[    0.000000] Memory: 169576K/260096K available (4430K kernel code, 525K rwdata, 1917K rodata, 156K init, 213K bss, 90520K reserved, 0K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=1, Nodes=1
[    0.000000] rcu: Preemptible hierarchical RCU implementation.
[    0.000000] rcu:     RCU event tracing is enabled.
[    0.000000]  Trampoline variant of Tasks RCU enabled.
[    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
[    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
[    0.000000] riscv-intc: 64 local interrupts mapped
[    0.000000] plic: interrupt-controller@70000000: mapped 101 interrupts with 1 handlers for 2 contexts.
[    0.000000] random: get_random_bytes called from start_kernel+0x2e0/0x41c with crng_init=0
[    0.000000] riscv_timer_init_dt: Registering clocksource cpuid [0] hartid [0]
[    0.000000] clocksource: riscv_clocksource: mask: 0xffffffffffffffff max_cycles: 0x5c40939b5, max_idle_ns: 440795202646 ns
[    0.000008] sched_clock: 64 bits at 25MHz, resolution 40ns, wraps every 4398046511100ns
[    0.008408] Calibrating delay loop (skipped), value calculated using timer frequency.. 50.00 BogoMIPS (lpj=100000)
[    0.019122] pid_max: default: 4096 minimum: 301
[    0.024015] Mount-cache hash table entries: 512 (order: 0, 4096 bytes, linear)
[    0.031425] Mountpoint-cache hash table entries: 512 (order: 0, 4096 bytes, linear)
[    0.040830] ASID allocator initialised with 65536 entries
[    0.046506] rcu: Hierarchical SRCU implementation.
[    0.051882] EFI services will not be available.
[    0.056902] devtmpfs: initialized
[    0.065834] early_time_log: do_initcalls: 5048348us
[    0.071446] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.081483] futex hash table entries: 16 (order: -4, 384 bytes, linear)
[    0.088448] pinctrl core: initialized pinctrl subsystem
[    0.094290] NET: Registered protocol family 16
[    0.099281] DMA: preallocated 128 KiB GFP_KERNEL pool for atomic allocations
[    0.106584] DMA: preallocated 128 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
[    0.115348] thermal_sys: Registered thermal governor 'step_wise'
[    0.129909] OF: /gpio@03020000/gpio-controller@0: could not find phandle
[    0.143114] OF: /gpio@03021000/gpio-controller@1: could not find phandle
[    0.150103] OF: /gpio@03022000/gpio-controller@2: could not find phandle
[    0.157092] OF: /gpio@03023000/gpio-controller@3: could not find phandle
[    0.164076] OF: /gpio@05021000/gpio-controller@4: could not find phandle
[    0.172840] clk reset: nr_reset=64 resource_size=8
[    0.178354] get audio clk=24576000
[    0.181881] cvitek-i2s-subsys 4108000.i2s_subsys: Set clk_sdma_aud0~3 to 24576000
[    0.203791] dw_dmac 4330000.dma: CVITEK DMA Controller, 8 channels, probe done!
[    0.212250] SCSI subsystem initialized
[    0.216534] usbcore: registered new interface driver usbfs
[    0.222271] usbcore: registered new interface driver hub
[    0.227822] usbcore: registered new device driver usb
[    0.234721] Ion: ion_parse_dt_heap_common: id 0 type 2 name carveout align 1000
[    0.242788] Ion: rmem_ion_device_init: heap carveout base 0x000000008b300000 size 0x0000000004b00000 dev (____ptrval____)
[    0.254060] ion_carveout_heap_create, size=0x4b00000
[    0.259367] cvi_get_rtos_ion_size, rtos ion_size get:0x1600000
[    0.265336] ion_carveout_heap_create, size(exclusion of rtos_ion_size)=0x3500000
[    0.487406] platform carveout: [ion] add heap id 0, type 2, base 0x8b300000, size 0x4b00000
[    0.496331] Advanced Linux Sound Architecture Driver Initialized.
[    0.503805] clocksource: Switched to clocksource riscv_clocksource
[    0.511991] NET: Registered protocol family 2
[    0.517475] tcp_listen_portaddr_hash hash table entries: 256 (order: 0, 4096 bytes, linear)
[    0.526161] TCP established hash table entries: 2048 (order: 2, 16384 bytes, linear)
[    0.534156] TCP bind hash table entries: 2048 (order: 2, 16384 bytes, linear)
[    0.541598] TCP: Hash tables configured (established 2048 bind 2048)
[    0.548332] UDP hash table entries: 128 (order: 0, 4096 bytes, linear)
[    0.555079] UDP-Lite hash table entries: 128 (order: 0, 4096 bytes, linear)
[    0.562495] NET: Registered protocol family 1
[    0.567528] RPC: Registered named UNIX socket transport module.
[    0.573647] RPC: Registered udp transport module.
[    0.578518] RPC: Registered tcp transport module.
[    0.583442] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    0.592539] Initialise system trusted keyrings
[    0.597352] workingset: timestamp_bits=62 max_order=16 bucket_order=0
[    0.611921] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    0.618863] jffs2: version 2.2. (NAND) © 2001-2006 Red Hat, Inc.
[    0.625964] Key type asymmetric registered
[    0.630167] Asymmetric key parser 'x509' registered
[    0.640591] cvi_rtos_cmdqu_init
[    0.644024] cvi_rtos_cmdqu_probe start ---
[    0.648210] name=1900000.rtos_cmdqu
[    0.652038] res-reg: start: 0x1900000, end: 0x1900fff, virt-addr(ffffffd00573f000).
[    0.659927] RTOS_CMDQU_INIT
[    0.662821] mbox_reg=(____ptrval____)
[    0.666701] mbox_done_reg=(____ptrval____)
[    0.670995] mailbox_context=(____ptrval____)
[    0.675518] cvi_rtos_cmdqu_probe DONE
[    0.679453] cvi_rtos_cmdqu_init done
[    0.683110] [cvi_spinlock_init] success
[    0.687297] Serial: 8250/16550 driver, 5 ports, IRQ sharing disabled
[    0.695587] printk: console [ttyS0] disabled
[    0.700084] 4140000.serial: ttyS0 at MMIO 0x4140000 (irq = 15, base_baud = 156250[    0.709107] printk: console [ttyS0] enabled
[    0.709107] printk: console [ttyS0] enabled
[    0.717697] printk: bootconsole [sbi0] disabled
[    0.717697] printk: bootconsole [sbi0] disabled
[    0.727933] 4150000.serial: ttyS1 at MMIO 0x4150000 (irq = 16, base_baud = 1562500) is a 16550A
[    0.737685] 4160000.serial: ttyS2 at MMIO 0x4160000 (irq = 17, base_baud = 1562500) is a 16550A
[    0.747483] 4170000.serial: ttyS3 at MMIO 0x4170000 (irq = 18, base_baud = 1562500) is a 16550A
[    0.761383] libphy: Fixed MDIO Bus: probed
[    0.766163] bm-dwmac 4070000.ethernet: IRQ eth_wake_irq not found
[    0.772514] bm-dwmac 4070000.ethernet: IRQ eth_lpi not found
[    0.778478] bm-dwmac 4070000.ethernet: Hash table entries set to unexpected value 0
[    0.786531] bm-dwmac 4070000.ethernet: no reset control found
[    0.792711] bm-dwmac 4070000.ethernet: User ID: 0x10, Synopsys ID: 0x37
[    0.799612] bm-dwmac 4070000.ethernet:       DWMAC1000
[    0.804506] bm-dwmac 4070000.ethernet: DMA HW capability register supported
[    0.811723] bm-dwmac 4070000.ethernet: RX Checksum Offload Engine supported
[    0.818939] bm-dwmac 4070000.ethernet: COE Type 2
[    0.823823] bm-dwmac 4070000.ethernet: TX Checksum insertion supported
[    0.830589] bm-dwmac 4070000.ethernet: Normal descriptors
[    0.836192] bm-dwmac 4070000.ethernet: Ring mode enabled
[    0.841704] bm-dwmac 4070000.ethernet: Enable RX Mitigation via HW Watchdog Timer
[    0.849460] bm-dwmac 4070000.ethernet: device MAC address ca:dc:10:b8:92:4b
[    0.880790] libphy: stmmac: probed
[    0.884520] CVITEK CV182XA stmmac-0:00: attached PHY driver [CVITEK CV182XA] (mii_bus:phy_addr=stmmac-0:00, irq=POLL)
[    0.895587] CVITEK CV182XA stmmac-0:01: attached PHY driver [CVITEK CV182XA] (mii_bus:phy_addr=stmmac-0:01, irq=POLL)
[    0.907919] bm-dwmac 4070000.ethernet: Cannot get clk_500m_eth!
[    0.914130] bm-dwmac 4070000.ethernet: Cannot get gate_clk_axi4!
[    0.921393] dwc2 4340000.usb: axi clk installed
[    0.926133] dwc2 4340000.usb: apb clk installed
[    0.930844] dwc2 4340000.usb: 125m clk installed
[    0.935643] dwc2 4340000.usb: 33k clk installed
[    0.940352] dwc2 4340000.usb: 12m clk installed
[    0.945136] dwc2 4340000.usb: EPs: 8, dedicated fifos, 3072 entries in SPRAM
[    0.952936] dwc2 4340000.usb: DWC OTG Controller
[    0.957790] dwc2 4340000.usb: new USB bus registered, assigned bus number 1
[    0.965049] dwc2 4340000.usb: irq 37, io mem 0x04340000
[    0.971328] hub 1-0:1.0: USB hub found
[    0.975324] hub 1-0:1.0: 1 port detected
[    0.980598] usbcore: registered new interface driver usb-storage
[    0.987306] mousedev: PS/2 mouse device common for all mice
[    0.993413] i2c /dev entries driver
[    0.998609] sdhci: Secure Digital Host Controller Interface driver
[    1.005056] sdhci: Copyright(c) Pierre Ossman
[    1.009584] sdhci-pltfm: SDHCI platform and OF driver helper
[    1.015708] cvi:sdhci_cvi_probe
[    1.063821] mmc0: SDHCI controller on 4310000.cv-sd [4310000.cv-sd] using ADMA 64-bit
[    1.071978] cvi_proc_init cvi_host 0x(____ptrval____)
[    1.077850] usbcore: registered new interface driver usbhid
[    1.087822] usbhid: USB HID core driver
[    1.093032] usbcore: registered new interface driver snd-usb-audio
[    1.100340] cvitek-i2s 4100000.i2s: cvi_i2s_probe
[    1.112246] cvitek-i2s 4130000.i2s: cvi_i2s_probe
[    1.117820] cviteka-adc sound_adc: cviteka_adc_probe, dev name=sound_adc
[    1.124895] cviteka-adc sound_adc: cviteka_adc_probe start devm_snd_soc_register_card
[    1.133416] cvitekaadc 300a100.adc: cvitekaadc_probe
[    1.144373] cviteka-dac sound_dac: cviteka_dac_probe, dev name=sound_dac
[    1.151710] cvitekadac 300a000.dac: cvitekadac_probe
[    1.157148] cvitekadac_probe gpio_is_valid mute_pin_l
[    1.163635] NET: Registered protocol family 10
[    1.169579] Segment Routing with IPv6
[    1.173580] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
[    1.180800] NET: Registered protocol family 17
[    1.185718] Loading compiled-in X.509 certificates
[    1.227079] mmc0: new high speed SDHC card at address aaaa
[    1.233476] i2c_designware 4010000.i2c: running with gpio recovery mode! scl,sda
[    1.241580] mmcblk0: mmc0:aaaa SP32G 29.7 GiB
[    1.247231] i2c_designware 4020000.i2c: running with gpio recovery mode! scl,sda
[    1.255977] i2c_designware 4030000.i2c: running with gpio recovery mode! scl,sda
[    1.265123] cviteka-adc sound_adc: cviteka_adc_probe, dev name=sound_adc
[    1.272257]  mmcblk0: p1 p2
[    1.275371] cviteka-adc sound_adc: cviteka_adc_probe start devm_snd_soc_register_card
[    1.289546] cviteka-dac sound_dac: cviteka_dac_probe, dev name=sound_dac
[    1.301907] cfg80211: Loading compiled-in X.509 certificates for regulatory database
[    1.312554] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
[    1.319603] cfg80211: failed to load regulatory.db
[    1.324819] ALSA device list:
[    1.328273] dw-apb-uart 4140000.serial: forbid DMA for kernel console
[    1.343396] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
[    1.351931] VFS: Mounted root (ext4 filesystem) on device 179:2.
[    1.361452] devtmpfs: mounted
[    1.364751] Freeing unused kernel memory: 156K
[    1.369380] Kernel memory protection not selected by kernel config.
[    1.375893] Run /sbin/init as init process
[    1.380152]   with arguments:
[    1.383220]     /sbin/init
[    1.386074] usb 1-1: new high-speed USB device number 2 using dwc2
[    1.392495]   with environment:
[    1.395742]     HOME=/
[    1.398288]     TERM=linux
[    1.401219] early_time_log: run_init_process: 6383734us
[    1.463417] EXT4-fs (mmcblk0p2): re-mounted. Opts: errors=remount-ro
[    1.549007] random: fast init done
[    1.610469] hub 1-1:1.0: USB hub found
[    1.615253] hub 1-1:1.0: 4 ports detected
Starting syslogd: OK
Starting klogd: OK
Running sysctl: OK
Saving random seed: [    1.922972] random: dd: uninitialized urandom read (512 bytes read)
OK
Starting network: OK
Starting dhcpcd...
dhcpcd-9.4.0 starting
[    2.012736] random: dhcpcd: uninitialized urandom read (112 bytes read)
dhcp_vendor: Invalid argument
forked to background, child pid 137
Bad system call
[    2.148640] bm-dwmac 4070000.ethernet eth0: PHY [stmmac-0:00] driver [CVITEK CV182XA] (irq=POLL)
Starting ntpd: [    2.171870] dwmac1000: Master AXI performs any burst length
[    2.178886] bm-dwmac 4070000.ethernet eth0: No Safety Features support found
[    2.187237] bm-dwmac 4070000.ethernet eth0: IEEE 1588-2002 Timestamp supported
[    2.196110] bm-dwmac 4070000.ethernet eth0: configuring for phy/rmii link mode
OK
Starting dropbear sshd: OK
Starting dnsmasq: [    2.407958] random: dnsmasq: uninitialized urandom read (128 bytes read)
OK
init mpp system...
[    2.444394] cv181x_sys: bad vermagic: kernel tainted.
[    2.449690] Disabling lock debugging due to kernel taint
[    2.455609] cv181x_sys: loading out-of-tree module taints kernel.
[    2.481082] res-reg: start: 0xa0c8000, end: 0xa0c801f, virt-addr(ffffffd00409e000).
[    2.489578] CVITEK CHIP ID = 18
[    2.506675] cif a0c2000.cif: cam0 clk installed
[    2.511489] cif a0c2000.cif: cam1 clk installed
[    2.516671] cif a0c2000.cif: vip_sys_2 clk installed
[    2.522122] cif a0c2000.cif: clk_mipimpll clk installed (____ptrval____)
[    2.529359] cif a0c2000.cif: clk_disppll clk installed (____ptrval____)
[    2.536508] cif a0c2000.cif: clk_fpll clk installed (____ptrval____)
[    2.543383] cif a0c2000.cif: (0) res-reg: start: 0xa0c2000, end: 0xa0c3fff.
[    2.550866] cif a0c2000.cif:  virt-addr((____ptrval____))
[    2.556746] cif a0c2000.cif: (1) res-reg: start: 0xa0d0000, end: 0xa0d0fff.
[    2.564231] cif a0c2000.cif:  virt-addr((____ptrval____))
[    2.570114] cif a0c2000.cif: (2) res-reg: start: 0xa0c4000, end: 0xa0c5fff.
[    2.577619] cif a0c2000.cif:  virt-addr((____ptrval____))
[    2.583505] cif a0c2000.cif: (3) res-reg: start: 0xa0c6000, end: 0xa0c7fff.
[    2.590990] cif a0c2000.cif:  virt-addr((____ptrval____))
[    2.596872] cif a0c2000.cif: (4) res-reg: start: 0x3001c30, end: 0x3001c5f.
[    2.604356] cif a0c2000.cif:  virt-addr((____ptrval____))
[    2.610227] cif a0c2000.cif: no pad_ctrl for cif
[    2.615354] cif a0c2000.cif: request irq-26 as cif-irq0
[    2.621118] cif a0c2000.cif: request irq-27 as cif-irq1
[    2.626862] cif a0c2000.cif: rst_pin = 433, pol = 1
[    2.639327] snsr_i2c snsr_i2c: i2c:-------hook 1
[    2.644330] snsr_i2c snsr_i2c: i2c:-------hook 2
[    2.649757] snsr_i2c snsr_i2c: i2c:-------hook 3
[    2.697847] vi_core_probe:203(): res-reg: start: 0xa000000, end: 0xa07ffff, virt-addr(ffffffd004180000).
[    2.707735] vi_core_probe:216(): irq(28) for isp get from platform driver.
[    2.715771] vi_tuning_buf_setup:253(): tuning fe_addr[0]=0x81bdf490, be_addr[0]=0x81bd7290, post_addr[0]=0x81bc0000
[    2.726998] vi_tuning_buf_setup:253(): tuning fe_addr[1]=0x81bff490, be_addr[1]=0x81bf7290, post_addr[1]=0x81be0000
[    2.738152] vi_tuning_buf_setup:253(): tuning fe_addr[2]=0x81edf490, be_addr[2]=0x81ed7290, post_addr[2]=0x81ec0000
[    2.749265] sync_task_init:177(): sync_task_init vi_pipe 0
[    2.755258] sync_task_init:177(): sync_task_init vi_pipe 1
[    2.761219] sync_task_init:177(): sync_task_init vi_pipe 2
[    2.767669] vi_core_probe:252(): isp registered as cvi-vi
[    2.825213] cvi_dwa_probe:487(): done with rc(0).
[    2.869174] cv181x-cooling cv181x_cooling: elems of dev-freqs=6
[    2.875476] cv181x-cooling cv181x_cooling: dev_freqs[0]: 850000000 500000000
[    2.883250] cv181x-cooling cv181x_cooling: dev_freqs[1]: 425000000 375000000
[    2.890862] cv181x-cooling cv181x_cooling: dev_freqs[2]: 425000000 300000000
[    2.898563] cv181x-cooling cv181x_cooling: Cooling device registered: cv181x_cooling
[    2.934434] jpu ctrl reg pa = 0xb030000, va = (____ptrval____), size = 256
[    2.942100] end jpu_init result = 0x0
[    3.053306] cvi_vc_drv_init result = 0x0
[    3.122741] sh (175): drop_caches: 3
Starting app...

[root@milkv-duo]~# uname -a
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Fri Nov 22 11:42:16 CST 2024 riscv64 GNU/Linux
[root@milkv-duo]~# cat /etc/os-release
NAME=Buildroot
VERSION=20241122-1150
ID=buildroot
VERSION_ID=2021.05
PRETTY_NAME="Buildroot 2021.05"
[root@milkv-duo]~# cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

[root@milkv-duo]~#

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。