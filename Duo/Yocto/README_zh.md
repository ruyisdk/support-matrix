# Yocto Milk-V Duo 测试报告

## 测试环境

### 操作系统信息

- 构建系统版本：Debian 12 bookworm
- 源码链接：https://github.com/kinsamanka/meta-milkv
- 参考安装文档：https://github.com/kinsamanka/meta-milkv/blob/master/README.md

### 硬件信息

- Milk-V Duo 64M
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条
- TF 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根
- Milk-V Duo 本体上预先焊接好调试所需的排针

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
export KAS_MACHINE=milkv-duo
```

拉取源码：

```shell
mkdir yocto
cd yocto
git clone https://github.com/kinsamanka/meta-milkv

```

使用 `kas` 构建:

```shell
kas build meta-milkv/kas-project.yml
```

生成的镜像位于 `build/tmp-musl/deploy/images/milkv-duo/core-image-minimal-milkv-duo.rootfs.wic.gz`.

### 烧录镜像至 SD 卡

```shell
zcat build/tmp-musl/deploy/images/milkv-duo/core-image-minimal-milkv-duo.rootfs.wic.gz | \
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

```log
Starting kernel ...

[    0.000000] Linux version 5.10.4-yocto-standard-milkv-duo (oe-user@oe-host) (riscv64-oe-linux-musl-gcc (GCC) 13.3.0, GNU ld (GNU Binutils) 2.42.0.20240723) #1 PREEMPT Fri Oct 6 23:47:33 UTC 2023
[    0.000000] earlycon: sbi0 at I/O port 0x0 (options '')
[    0.000000] printk: bootconsole [sbi0] enabled
[    0.000000] efi: UEFI not found.
[    0.000000] OF: reserved mem: failed to allocate memory for node 'ion'
[    0.000000] Zone ranges:
[    0.000000]   DMA32    [mem 0x0000000080000000-0x0000000083f3ffff]
[    0.000000]   Normal   empty
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000080000000-0x0000000083f3ffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000080000000-0x0000000083f3ffff]
[    0.000000] On node 0 totalpages: 16192
[    0.000000]   DMA32 zone: 222 pages used for memmap
[    0.000000]   DMA32 zone: 0 pages reserved
[    0.000000]   DMA32 zone: 16192 pages, LIFO batch:3
[    0.000000] software IO TLB: Cannot allocate buffer
[    0.000000] SBI specification v2.0 detected
[    0.000000] SBI implementation ID=0x1 Version=0x10004
[    0.000000] SBI v0.2 TIME extension detected
[    0.000000] SBI v0.2 IPI extension detected
[    0.000000] SBI v0.2 RFENCE extension detected
[    0.000000] riscv: ISA extensions acdfimsuv
[    0.000000] riscv: ELF capabilities acdfimv
[    0.000000] pcpu-alloc: s0 r0 d32768 u32768 alloc=1*32768
[    0.000000] pcpu-alloc: [0] 0 
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 15970
[    0.000000] Kernel command line: root=/dev/mmcblk0p2 console=ttyS0,115200 earlycon=sbi loglevel=9 rootwait rw
[    0.000000] Dentry cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.000000] Inode-cache hash table entries: 4096 (order: 3, 32768 bytes, linear)
[    0.000000] Sorting __ex_table...
[    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
[    0.000000] Memory: 46412K/64768K available (4081K kernel code, 4538K rwdata, 4096K rodata, 160K init, 219K bss, 18356K reserved, 0K cma-reserved)
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
[    0.000009] sched_clock: 64 bits at 25MHz, resolution 40ns, wraps every 4398046511100ns
[    0.008494] Console: colour dummy device 80x25
[    0.013099] Calibrating delay loop (skipped), value calculated using timer frequency.. 50.00 BogoMIPS (lpj=100000)
[    0.023786] pid_max: default: 32768 minimum: 301
[    0.028825] Mount-cache hash table entries: 512 (order: 0, 4096 bytes, linear)
[    0.036250] Mountpoint-cache hash table entries: 512 (order: 0, 4096 bytes, linear)
[    0.046043] ASID allocator initialised with 65536 entries
[    0.051793] rcu: Hierarchical SRCU implementation.
[    0.057228] EFI services will not be available.
[    0.062359] devtmpfs: initialized
[    0.070738] early_time_log: do_initcalls: 4127626us
[    0.076361] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.086427] futex hash table entries: 256 (order: 0, 6144 bytes, linear)
[    0.093518] pinctrl core: initialized pinctrl subsystem
[    0.099586] NET: Registered protocol family 16
[    0.104666] DMA: preallocated 128 KiB GFP_KERNEL pool for atomic allocations
[    0.112011] DMA: preallocated 128 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
[    0.120992] thermal_sys: Registered thermal governor 'step_wise'
[    0.137007] OF: /gpio@03020000/gp```w interface driver usbfs
[    0.229183] usbcore: registered new interface driver hub
[    0.234807] usbcore: registered new device driver usb
[    0.243172] pps_core: LinuxPPS API ver. 1 registered
[    0.248314] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    0.257801] PTP clock support registered
[    0.262424] Ion: ion_parse_dt_heap_common: id 0 type 2 name carveout align 1000
[    0.270461] ion_carveout_heap_create, size=0x0
[    0.275173] cvi_get_rtos_ion_size, rtos ion_size get:0x0
[    0.280808] platform carveout: [ion] add heap id 0, type 2, base 0x0, size 0x0
[    0.288653] Advanced Linux Sound Architecture Driver Initialized.
[    0.296398] clocksource: Switched to clocksource riscv_clocksource
[    0.316298] NET: Registered protocol family 2
[    0.321983] tcp_listen_portaddr_hash hash table entries: 256 (order: 0, 4096 bytes, linear)
[    0.330717] TCP established hash table entries: 512 (order: 0, 4096 bytes, linear)
[    0.338523] TCP bind hash table entries: 512 (order: 0, 4096 bytes, linear)
[    0.345793] TCP: Hash tables configured (established 512 bind 512)
[    0.352493] UDP hash table entries: 256 (order: 1, 8192 bytes, linear)
[    0.359295] UDP-Lite hash table entries: 256 (order: 1, 8192 bytes, linear)
[    0.366721] NET: Registered protocol family 1
[    0.371966] RPC: Registered named UNIX socket transport module.
[    0.378121] RPC: Registered udp transport module.
[    0.382976] RPC: Registered tcp transport module.
[    0.387896] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    0.397215] Initialise system trusted keyrings
[    0.402133] workingset: timestamp_bits=62 max_order=14 bucket_order=0
[    0.418298] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    0.425642] jffs2: version 2.2. (NAND) © 2001-2006 Red Hat, Inc.
[    0.433016] Key type asymmetric registered
[    0.437239] Asymmetric key parser 'x509' registered
[    0.442397] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 249)
[    0.450035] io scheduler mq-deadline registered
[    0.454773] io scheduler kyber registered
[    0.463237] pinctrl-single 3001000.pinctrl: 1024 pins, size 4096
[    0.555695] Serial: 8250/16550 driver, 5 ports, IRQ sharing disabled
[    0.564666] printk: console [ttyS0] disabled
[    0.569204] 4140000.serial: ttyS0 at MMIO 0x4140000 (irq = 15, base_baud = 1562500) is a 16550A
[    0.578338] printk: console [ttyS0] enabled
[    0.578338] printk: console [ttyS0] enabled
[    0.586949] printk: bootconsole [sbi0] disabled
[    0.586949] printk: bootconsole [sbi0] disabled
[    0.597551] 41c0000.serial: ttyS4 at MMIO 0x41c0000 (irq = 16, base_baud = 1562500) is a 16550A
[    0.610197] cvi-spif 10000000.cvi-spif: unrecognized JEDEC id bytes: ff ff ff ff ff ff
[    0.618465] cvi-spif 10000000.cvi-spif: device scan failed
[    0.624177] cvi-spif 10000000.cvi-spif: unable to setup flash chip
[    0.637299] libphy: Fixed MDIO Bus: probed
[    0.642192] bm-dwmac 4070000.ethernet: IRQ eth_wake_irq not found
[    0.648567] bm-dwmac 4070000.ethernet: IRQ eth_lpi not found
[    0.654573] bm-dwmac 4070000.ethernet: Hash table entries set to unexpected value 0
[    0.662668] bm-dwmac 4070000.ethernet: no reset control found
[    0.668916] bm-dwmac 4070000.ethernet: User ID: 0x10, Synopsys ID: 0x37
[    0.675846] bm-dwmac 4070000.ethernet:       DWMAC1000
[    0.680758] bm-dwmac 4070000.ethernet: DMA HW capability register supported
[    0.687988] bm-dwmac 4070000.ethernet: RX Checksum Offload Engine supported
[    0.695219] bm-dwmac 4070000.ethernet: COE Type 2
[    0.700116] bm-dwmac 4070000.ethernet: TX Checksum insertion supported
[    0.706897] bm-dwmac 4070000.ethernet: Normal descriptors
[    0.712512] bm-dwmac 4070000.ethernet: Ring mode enabled
[    0.718039] bm-dwmac 4070000.ethernet: Enable RX Mitigation via HW Watchdog Timer
[    0.725808] bm-dwmac 4070000.ethernet: device MAC address be:74:33:8c:cb:c7
[    0.761231] libphy: stmmac: probed
[    0.766294] bm-dwmac 4070000.ethernet: Cannot get clk_500m_eth!
[    0.772663] bm-dwmac 4070000.ethernet: Cannot get gate_clk_axi4!
[    0.780771] dwc2 4340000.usb: axi clk installed
[    0.785542] dwc2 4340000.usb: apb clk installed
[    0.790273] dwc2 4340000.usb: 125m clk installed
[    0.795080] dwc2 4340000.usb: 33k clk installed
[    0.799805] dwc2 4340000.usb: 12m clk installed
[    0.804626] dwc2 4340000.usb: EPs: 8, dedicated fifos, 3072 entries in SPRAM
[    0.812645] dwc2 4340000.usb: DWC OTG Controller
[    0.817524] dwc2 4340000.usb: new USB bus registered, assigned bus number 1
[    0.824810] dwc2 4340000.usb: irq 36, io mem 0x04340000
[    0.831295] hub 1-0:1.0: USB hub found
[    0.835346] hub 1-0:1.0: 1 port detected
[    0.841244] usbcore: registered new interface driver usb-storage
[    0.848015] i2c /dev entries driver
[    0.853874] sdhci: Secure Digital Host Controller Interface driver
[    0.860332] sdhci: Copyright(c) Pierre Ossman
[    0.864871] sdhci-pltfm: SDHCI platform and OF driver helper
[    0.871041] cvi:sdhci_cvi_probe
[    0.920417] mmc0: SDHCI controller on 4310000.cv-sd [4310000.cv-sd] using ADMA 64-bit
[    0.928593] cvi_proc_init cvi_host 0x(____ptrval____)
[    0.940705] ledtrig-cpu: registered to indicate activity on CPUs
[    0.947651] usbcore: registered new interface driver usbhid
[    0.953575] usbhid: USB HID core driver
[    0.961268] cvitek-i2s 4100000.i2s: cvi_i2s_probe
[    0.971861] cvitek-i2s 4130000.i2s: cvi_i2s_probe
[    0.977752] cviteka-adc sound_adc: cviteka_adc_probe, dev name=sound_adc
[    0.988453] cviteka-adc sound_adc: cviteka_adc_probe start devm_snd_soc_register_card
[    0.997041] cvitekaadc 300a100.adc: cvitekaadc_probe
[    1.003159] cviteka-dac sound_dac: cviteka_dac_probe, dev name=sound_dac
[    1.010659] cvitekadac 300a000.dac: cvitekadac_probe
[    1.016121] cvitekadac_probe gpio_is_valid mute_pin_l
[    1.023036] NET: Registered protocol family 10
[    1.029898] Segment Routing with IPv6
[    1.033985] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
[    1.041292] NET: Registered protocol family 17
[    1.046419] Loading compiled-in X.509 certificates
[    1.076492] mmc0: new high speed SDHC card at address aaaa
[    1.089369] mmcblk0: mmc0:aaaa SD32G 29.7 GiB 
[    1.096764] cviteka-adc sound_adc: cviteka_adc_probe, dev name=sound_adc
[    1.103762] cviteka-adc sound_adc: cviteka_adc_probe start devm_snd_soc_register_card
[    1.118179] cviteka-dac sound_dac: cviteka_dac_probe, dev name=sound_dac
[    1.131356] cfg80211: Loading compiled-in X.509 certificates for regulatory database
[    1.142164]  mmcblk0: p1 p2
[    1.149256] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
[    1.156519] cfg80211: failed to load regulatory.db
[    1.161750] ALSA device list:
[    1.165614] dw-apb-uart 4140000.serial: forbid DMA for kernel console
[    1.198588] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
[    1.207103] VFS: Mounted root (ext4 filesystem) on device 179:2.
[    1.214218] devtmpfs: mounted
[    1.217556] Freeing unused kernel memory: 160K
[    1.222782] Run /sbin/init as init process
[    1.227087]   with arguments:
[    1.230191]     /sbin/init
[    1.233026]   with environment:
[    1.236279]     HOME=/
[    1.238752]     TERM=linux
[    1.241588] early_time_log: run_init_process: 5298482us
[    1.247069] usb 1-1: new high-speed USB device number 2 using dwc2
init started: BusyBox v1.36.1 ()
[    1.440575] dwc2 4340000.usb: Not connected
[    1.538064] bm-dwmac 4070000.ethernet eth0: PHY [stmmac-0:00] driver [Generic PHY] (irq=POLL)
[    1.559469] dwmac1000: Master AXI performs any burst length
[    1.565295] bm-dwmac 4070000.ethernet eth0: No Safety Features support found
[    1.573005] bm-dwmac 4070000.ethernet eth0: IEEE 1588-2002 Timestamp supported
[    1.581054] bm-dwmac 4070000.ethernet eth0: registered PTP clock
[    1.588077] bm-dwmac 4070000.ethernet eth0: configuring for phy/rmii link mode
[    1.656488] dwc2 4340000.usb: Not connected
[   10.839565] random: chronyd: uninitialized urandom read (3 bytes read)
[   10.846450] random: chronyd: uninitialized urandom read (1024 bytes read)
[   18.680486] random: crng init done
starting pid 150, tty '/dev/ttyS0': '/usr/sbin/ttyrun ttyS0 /sbin/getty 115200 ttyS0'

OpenEmbedded 1.0 milkv-duo /dev/ttyS0

milkv-duo login: root
                                                                                  
root@milkv-duo:~# uname -a
Linux milkv-duo 5.10.4-yocto-standard-milkv-duo #1 PREEMPT Fri Oct 6 23:47:33 UTC 2023 riscv64 GNU/Linux
root@milkv-duo:~# cat /proc/version
Linux version 5.10.4-yocto-standard-milkv-duo (oe-user@oe-host) (riscv64-oe-linux-musl-gcc (GCC) 13.3.0, GNU ld (GNU Binutils) 2.42.0.20240723) #1 PREEMPT Fri Oct 6 23:47:33 UTC 2023
root@milkv-duo:~# 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
