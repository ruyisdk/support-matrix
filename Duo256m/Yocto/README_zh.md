# Yocto Milk-V Duo 256M 测试报告

## 测试环境

### 操作系统信息

- 构建系统版本：Debian 12 bookworm
- 源码链接：https://github.com/kinsamanka/meta-milkv
- 参考安装文档：https://github.com/kinsamanka/meta-milkv/blob/master/README.md

### 硬件信息

- Milk-V Duo 256M
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条
- TF 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根
- Milk-V Duo 256M 本体上预先焊接好调试所需的排针

## 安装步骤

### 准备系统环境

Debian 或 Ubuntu 下运行:

```shell
sudo apt install gawk wget git diffstat unzip texinfo gcc build-essential chrpath socat cpio python3 python3-pip python3-pexpect xz-utils debianutils iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev python3-subunit mesa-common-dev zstd liblz4-tool file locales libacl1
sudo locale-gen en_US.UTF-8 # skip if locale already set
sudo apt install kas
```

### 下载源码和构建

设置目标开发板类型：

```shell
export KAS_MACHINE=milkv-duo256m
```

拉取源码：

```shell
mkdir yocto
cd yocto
git clone https://github.com/kinsamanka/meta-milkv

```

参照 [此 PR](https://github.com/kinsamanka/meta-milkv/pull/8)，修改 `meta-milkv/recipes-kernel/linux/linux-milkv-duo-dev/0002-dts-fix-cells-sizes.patch` 文件中第 699 行

```diff
+			    <425000<425000000 300000000>;
```

为

```diff
+			    <425000000 300000000>;
```

使用 `kas` 构建:

```shell
kas build meta-milkv/kas-project.yml
```

生成的镜像位于 `build/tmp-musl/deploy/images/milkv-duo256m/core-image-minimal-milkv-duo256m.rootfs.wic.gz`.

### 烧录镜像至 SD 卡

```shell
zcat build/tmp-musl/deploy/images/milkv-duo/core-image-minimal-milkv-duo256m.rootfs.wic.gz | \
  sudo dd of=/dev/your/device bs=4M iflag=fullblock oflag=direct conv=fsync status=progress
```

### 登录系统

通过串口登录系统。

默认用户名： `root`
默认密码：无密码

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

```log
Starting kernel ...

[    0.000000] Linux version 5.10.4-yocto-standard-milkv-duo (oe-user@oe-host) (riscv64-oe-linux-musl-gcc (GCC) 13.3.0, GNU ld (GNU Binutils) 2.42.0.20240723) #1 PREEMPT Fri Oct 6 23:47:33 UTC 2023
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
[    0.000000] software IO TLB: mapped [mem 0x0000000086dac000-0x000000008adac000] (64MB)
[    0.000000] SBI specification v2.0 detected
[    0.000000] SBI implementation ID=0x1 Version=0x10004
[    0.000000] SBI v0.2 TIME extension detected
[    0.000000] SBI v0.2 IPI extension detected
[    0.000000] SBI v0.2 RFENCE extension detected
[    0.000000] riscv: ISA extensions acdfimsuv
[    0.000000] riscv: ELF capabilities acdfimv
[    0.000000] pcpu-alloc: s0 r0 d32768 u32768 alloc=1*32768
[    0.000000] pcpu-alloc: [0] 0 
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 64135
[    0.000000] Kernel command line: root=/dev/mmcblk0p2 console=ttyS0,115200 earlycon=sbi loglevel=9 rootwait rw
[    0.000000] Dentry cache hash table entries: 32768 (order: 6, 262144 bytes, linear)
[    0.000000] Inode-cache hash table entries: 16384 (order: 5, 131072 bytes, linear)
[    0.000000] Sorting __ex_table...
[    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
[    0.000000] Memory: 94392K/260096K available (4082K kernel code, 4539K rwdata, 4096K rodata, 160K init, 219K bss, 165704K reserved, 0K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=1, Nodes=1
[    0.000000] rcu: Preemptible hierarchical RCU implementation.
[    0.000000] rcu:     RCU event tracing is enabled.
[    0.000000]  Trampoline variant of Tasks RCU enabled.
[    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
[    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
[    0.000000] riscv-intc: 64 local interrupts mapped
[    0.000000] plic: interrupt-controller@70000000: mapped 101 interrupts with 1 handlers for 2 contexts.
[    0.000000] random: get_random_bytes called from start_kernel+0x300/0x454 with crng_init=0
[    0.000000] riscv_timer_init_dt: Registering clocksource cpuid [0] hartid [0]
[    0.000000] clocksource: riscv_clocksource: mask: 0xffffffffffffffff max_cycles: 0x5c40939b5, max_idle_ns: 440795202646 ns
[    0.000008] sched_clock: 64 bits at 25MHz, resolution 40ns, wraps every 4398046511100ns
[    0.008475] Console: colour dummy device 80x25
[    0.013070] Calibrating delay loop (skipped), value calculated using timer frequency.. 50.00 BogoMIPS (lpj=100000)
[    0.023771] pid_max: default: 32768 minimum: 301
[    0.028778] Mount-cache hash table entries: 512 (order: 0, 4096 bytes, linear)
[    0.036190] Mountpoint-cache hash table entries: 512 (order: 0, 4096 bytes, linear)
[    0.045708] ASID allocator initialised with 65536 entries
[    0.051399] rcu: Hierarchical SRCU implementation.
[    0.056761] EFI services will not be available.
[    0.061817] devtmpfs: initialized
[    0.070158] early_time_log: do_initcalls: 4148312us
[    0.075703] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.085750] futex hash table entries: 256 (order: 0, 6144 bytes, linear)
[    0.092824] pinctrl core: initialized pinctrl subsystem
[    0.098758] NET: Registered protocol family 16
[    0.103736] DMA: preallocated 128 KiB GFP_KERNEL pool for atomic allocations
[    0.111047] DMA: preallocated 128 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
[    0.119905] thermal_sys: Registered thermal governor 'step_wise'
[    0.134793] OF: /gpio@03020000/gpio-controller@0: could not find phandle
[    0.148011] OF: /gpio@03021000/gpio-controller@1: could not find phandle
[    0.154999] OF: /gpio@03022000/gpio-controller@2: could not find phandle
[    0.161987] OF: /gpio@03023000/gpio-controller@3: could not find phandle
[    0.168974] OF: /gpio@05021000/gpio-controller@4: could not find phandle
[    0.178136] clk reset: nr_reset=64 resource_size=8
[    0.183725] get audio clk=24576000
[    0.187271] cvitek-i2s-subsys 4108000.i2s_subsys: Set clk_sdma_aud0~3 to 24576000
[    0.206461] dw_dmac 4330000.dma: CVITEK DMA Controller, 8 channels, probe done!
[    0.214890] SCSI subsystem initialized
[    0.219115] usbcore: registered new interface driver usbfs
[    0.224875] usbcore: registered new interface driver hub
[    0.230447] usbcore: registered new device driver usb
[    0.237033] pps_core: LinuxPPS API ver. 1 registered
[    0.242164] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    0.251667] PTP clock support registered
[    0.256199] Ion: ion_parse_dt_heap_common: id 0 type 2 name carveout align 1000
[    0.264258] Ion: rmem_ion_device_init: heap carveout base 0x000000008b300000 size 0x0000000004b00000 dev (____ptrval____)
[    0.275540] ion_carveout_heap_create, size=0x4b00000
[    0.280844] cvi_get_rtos_ion_size, rtos ion_size get:0x1600000
[    0.286811] ion_carveout_heap_create, size(exclusion of rtos_ion_size)=0x3500000
[    0.509481] platform carveout: [ion] add heap id 0, type 2, base 0x8b300000, size 0x4b00000
[    0.518444] Advanced Linux Sound Architecture Driver Initialized.
[    0.525959] clocksource: Switched to clocksource riscv_clocksource
[    0.543667] NET: Registered protocol family 2
[    0.549174] tcp_listen_portaddr_hash hash table entries: 256 (order: 0, 4096 bytes, linear)
[    0.557872] TCP established hash table entries: 2048 (order: 2, 16384 bytes, linear)
[    0.565862] TCP bind hash table entries: 2048 (order: 2, 16384 bytes, linear)
[    0.573307] TCP: Hash tables configured (established 2048 bind 2048)
[    0.580048] UDP hash table entries: 256 (order: 1, 8192 bytes, linear)
[    0.586824] UDP-Lite hash table entries: 256 (order: 1, 8192 bytes, linear)
[    0.594257] NET: Registered protocol family 1
[    0.599330] RPC: Registered named UNIX socket transport module.
[    0.605458] RPC: Registered udp transport module.
[    0.610328] RPC: Registered tcp transport module.
[    0.615249] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    0.624194] Initialise system trusted keyrings
[    0.629032] workingset: timestamp_bits=62 max_order=15 bucket_order=0
[    0.644575] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    0.651690] jffs2: version 2.2. (NAND) © 2001-2006 Red Hat, Inc.
[    0.658860] Key type asymmetric registered
[    0.663064] Asymmetric key parser 'x509' registered
[    0.668213] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 249)
[    0.675866] io scheduler mq-deadline registered
[    0.680607] io scheduler kyber registered
[    0.688883] pinctrl-single 3001000.pinctrl: 1024 pins, size 4096
[    0.767899] Serial: 8250/16550 driver, 5 ports, IRQ sharing disabled
[    0.776497] printk: console [ttyS0] disabled
[    0.781008] 4140000.serial: ttyS0 at MMIO 0x4140000 (irq = 15, base_baud = 1562500) is a 16550A
[    0.790128] printk: console [ttyS0] enabled
[    0.790128] printk: console [ttyS0] enabled
[    0.798724] printk: bootconsole [sbi0] disabled
[    0.798724] printk: bootconsole [sbi0] disabled
[    0.809131] 4150000.serial: ttyS1 at MMIO 0x4150000 (irq = 16, base_baud = 1562500) is a 16550A
[    0.819162] 4160000.serial: ttyS2 at MMIO 0x4160000 (irq = 17, base_baud = 1562500) is a 16550A
[    0.829226] 4170000.serial: ttyS3 at MMIO 0x4170000 (irq = 18, base_baud = 1562500) is a 16550A
[    0.841434] cvi-spif 10000000.cvi-spif: unrecognized JEDEC id bytes: ff ff ff ff ff ff
[    0.849707] cvi-spif 10000000.cvi-spif: device scan failed
[    0.855421] cvi-spif 10000000.cvi-spif: unable to setup flash chip
[    0.867681] libphy: Fixed MDIO Bus: probed
[    0.872474] bm-dwmac 4070000.ethernet: IRQ eth_wake_irq not found
[    0.878828] bm-dwmac 4070000.ethernet: IRQ eth_lpi not found
[    0.884808] bm-dwmac 4070000.ethernet: Hash table entries set to unexpected value 0
[    0.892882] bm-dwmac 4070000.ethernet: no reset control found
[    0.899071] bm-dwmac 4070000.ethernet: User ID: 0x10, Synopsys ID: 0x37
[    0.905997] bm-dwmac 4070000.ethernet:       DWMAC1000
[    0.910897] bm-dwmac 4070000.ethernet: DMA HW capability register supported
[    0.918119] bm-dwmac 4070000.ethernet: RX Checksum Offload Engine supported
[    0.925339] bm-dwmac 4070000.ethernet: COE Type 2
[    0.930228] bm-dwmac 4070000.ethernet: TX Checksum insertion supported
[    0.937000] bm-dwmac 4070000.ethernet: Normal descriptors
[    0.942607] bm-dwmac 4070000.ethernet: Ring mode enabled
[    0.948126] bm-dwmac 4070000.ethernet: Enable RX Mitigation via HW Watchdog Timer
[    0.955887] bm-dwmac 4070000.ethernet: device MAC address 12:2d:f4:29:9f:bd
[    0.987195] libphy: stmmac: probed
[    0.992075] bm-dwmac 4070000.ethernet: Cannot get clk_500m_eth!
[    0.998436] bm-dwmac 4070000.ethernet: Cannot get gate_clk_axi4!
[    1.006367] dwc2 4340000.usb: axi clk installed
[    1.011136] dwc2 4340000.usb: apb clk installed
[    1.015877] dwc2 4340000.usb: 125m clk installed
[    1.020688] dwc2 4340000.usb: 33k clk installed
[    1.025405] dwc2 4340000.usb: 12m clk installed
[    1.030202] dwc2 4340000.usb: EPs: 8, dedicated fifos, 3072 entries in SPRAM
[    1.038117] dwc2 4340000.usb: DWC OTG Controller
[    1.042988] dwc2 4340000.usb: new USB bus registered, assigned bus number 1
[    1.050258] dwc2 4340000.usb: irq 37, io mem 0x04340000
[    1.056588] hub 1-0:1.0: USB hub found
[    1.060595] hub 1-0:1.0: 1 port detected
[    1.065842] usbcore: registered new interface driver usb-storage
[    1.072511] i2c /dev entries driver
[    1.077766] sdhci: Secure Digital Host Controller Interface driver
[    1.084206] sdhci: Copyright(c) Pierre Ossman
[    1.088737] sdhci-pltfm: SDHCI platform and OF driver helper
[    1.094865] cvi:sdhci_cvi_probe
[    1.141986] mmc0: SDHCI controller on 4310000.cv-sd [4310000.cv-sd] using ADMA 64-bit
[    1.150150] cvi_proc_init cvi_host 0x(____ptrval____)
[    1.162002] ledtrig-cpu: registered to indicate activity on CPUs
[    1.168780] usbcore: registered new interface driver usbhid
[    1.174661] usbhid: USB HID core driver
[    1.182725] cvitek-i2s 4100000.i2s: cvi_i2s_probe
[    1.188161] cvitek-i2s 4130000.i2s: cvi_i2s_probe
[    1.193871] cviteka-adc sound_adc: cviteka_adc_probe, dev name=sound_adc
[    1.205997] cviteka-adc sound_adc: cviteka_adc_probe start devm_snd_soc_register_card
[    1.214513] cvitekaadc 300a100.adc: cvitekaadc_probe
[    1.220386] cviteka-dac sound_dac: cviteka_dac_probe, dev name=sound_dac
[    1.227858] cvitekadac 300a000.dac: cvitekadac_probe
[    1.233270] cvitekadac_probe gpio_is_valid mute_pin_l
[    1.239960] NET: Registered protocol family 10
[    1.246279] Segment Routing with IPv6
[    1.250322] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
[    1.257382] NET: Registered protocol family 17
[    1.262398] Loading compiled-in X.509 certificates
[    1.298033] mmc0: new high speed SDHC card at address aaaa
[    1.306979] i2c_designware 4010000.i2c: running with gpio recovery mode! scl,sda
[    1.315096] mmcblk0: mmc0:aaaa SP32G 29.7 GiB 
[    1.320503] i2c_designware 4020000.i2c: running with gpio recovery mode! scl,sda
[    1.328909] i2c_designware 4030000.i2c: running with gpio recovery mode! scl,sda
[    1.337218] cviteka-adc sound_adc: cviteka_adc_probe, dev name=sound_adc
[    1.344203] cviteka-adc sound_adc: cviteka_adc_probe start devm_snd_soc_register_card
[    1.357423] cviteka-dac sound_dac: cviteka_dac_probe, dev name=sound_dac
[    1.369634] cfg80211: Loading compiled-in X.509 certificates for regulatory database
[    1.381599]  mmcblk0: p1 p2
[    1.385183] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
[    1.393462] cfg80211: failed to load regulatory.db
[    1.398687] ALSA device list:
[    1.402465] dw-apb-uart 4140000.serial: forbid DMA for kernel console
[    1.419441] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
[    1.427981] VFS: Mounted root (ext4 filesystem) on device 179:2.
[    1.436576] devtmpfs: mounted
[    1.439859] Freeing unused kernel memory: 160K
[    1.444530] Run /sbin/init as init process
[    1.448802]   with arguments:
[    1.451898]     /sbin/init
[    1.454723]   with environment:
[    1.457998]     HOME=/
[    1.460441]     TERM=linux
[    1.463300] usb 1-1: new high-speed USB device number 2 using dwc2
[    1.469727] early_time_log: run_init_process: 5547885us
init started: BusyBox v1.36.1 ()
[    1.662062] dwc2 4340000.usb: Not connected
[    1.731954] bm-dwmac 4070000.ethernet eth0: PHY [stmmac-0:00] driver [Generic PHY] (irq=POLL)
[    1.750001] dwmac1000: Master AXI performs any burst length
[    1.755816] bm-dwmac 4070000.ethernet eth0: No Safety Features support found
[    1.763465] bm-dwmac 4070000.ethernet eth0: IEEE 1588-2002 Timestamp supported
[    1.771408] bm-dwmac 4070000.ethernet eth0: registered PTP clock
[    1.778400] bm-dwmac 4070000.ethernet eth0: configuring for phy/rmii link mode
[    1.878014] dwc2 4340000.usb: Not connected
[   11.013433] random: chronyd: uninitialized urandom read (3 bytes read)
[   11.020289] random: chronyd: uninitialized urandom read (1024 bytes read)
[   21.930038] random: crng init done
starting pid 149, tty '/dev/ttyS0': '/usr/sbin/ttyrun ttyS0 /sbin/getty 115200 ttyS0'

OpenEmbedded 1.0 milkv-duo256m /dev/ttyS0

milkv-duo256m login: root
                                                                                  
root@milkv-duo256m:~# uname -a
Linux milkv-duo256m 5.10.4-yocto-standard-milkv-duo #1 PREEMPT Fri Oct 6 23:47:33 UTC 2023 riscv64 GNU/Linux
root@milkv-duo256m:~# cat /proc/version 
Linux version 5.10.4-yocto-standard-milkv-duo (oe-user@oe-host) (riscv64-oe-linux-musl-gcc (GCC) 13.3.0, GNU ld (GNU Binutils) 2.42.0.20240723) #1 PREEMPT Fri Oct 6 23:47:33 UTC 2023
root@milkv-duo256m:~# 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
