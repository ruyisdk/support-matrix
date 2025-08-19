---
sys: openeuler
sys_ver: null
sys_var: null

status: cfh
last_update: 2025-04-05
---

# openEuler/oERV Milk-V Meles Test Report

## Test Environment

### Operating System Information

- System Version: openEuler RISC-V 20241105
  - Download Link: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/testing/20241105/v0.1/meles/
  - iw-single-line flashing tool: https://mirror.iscas.ac.cn/revyos/extra/images/meles/20240720/iw-single-line.bin
- Reference Installation Document: https://milkv.io/zh/docs/meles/getting-started/boot

> Note: This is not the official image, but the one published by the openEuler RISC-V SIG Group.

### Hardware Information

- Milk-V Meles 4GB/8GB/16GB
- eMMC module > 16GB
- A USB A to C cable
- Optional: A USB-TTL Debugger (Flash U-Boot with SPL to SPI NOR Flash)
- Optional: Keyboard, monitor, mouse (for graphical interface testing)

## Installation Steps

Milk-V Meles' Bootloader is stored inside the onboard SPI NOR Flash, which can be upgraded using `cct` tool provided by `yoctools`. This is different from Lichee Pi 4A which uses the same TH1520 SoC.

You'll need UART serial connection to flash the firmware.

> Note: please do not try to use `fastboot flash uboot` method to upgrade U-Boot firmware, which is the same as the LPi4A.
> This method will NOT flash U-Boot to SPI NOR Flash which is loaded on boot by default. Thus you must use `cct` to flash the firmware.

Known issue: some AMD boards might not pick up Meles in fastboot mode.

Workaround: try connect Meles to a external USB Hub rather than the USB ports directly provided by the motherboard/PCH.

### Use `cct` to flash Bootloader into SPI NOR Flash

`cct` is the image flashing tool provided by `yoctools`, which requires Python 3.6~3.11 and Linux.

If your distro has already upgrade to Python 3.12+, then you'll need to manually install Python 3.11, create a Python virtual environment with it.

Since Python 3.12 and [PEP 668](https://peps.python.org/pep-0668/), you can not use `pip` to install packages globally.

And `yoctools` still depends on some packages which were already deprecated/replaced in Python 3.12+, thus you must create a Python venv in order to use `yoctools`.

Take Arch Linux as an example. By the time this article was written (2025.01), the default Python is Python 3.13, directly install `yoctools` will not work. You should install Python 3.11 from [AUR](https://aur.archlinux.org/packages/python311/) and creating a virtual environment using this version in order to flash the firmware.

Prepare Python 3.11 environment:

```shell
paru python311
sudo pacman -S python-virtualenv
virtualenv -p 3.11 meles
source meles/bin/activate
pip install yoctools
cd meles/bin
```

For those distros still staying at Python 3.6~3.11, you can install `yoctools` directly with `pip`. Python venv is not required.

Download the firmware:

```shell
wget https://mirror.iscas.ac.cn/revyos/extra/images/meles/20240720/iw-single-line.bin
wget https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/testing/20241105/v0.1/meles/u-boot-with-spl-meles.bin
```

Note: choose the correct version depending on your board's RAM:

- 4GB -> u-boot-with-spl-meles-4g.bin
- 8GB -> u-boot-with-spl-meles.bin

The `iw-single-line.bin` can be used with all RAM versions.

Connect the board and your PC with UART debugger. **DO NOT** run tools like `minicom` or `tio` which will occupy the serial port.

Hold the recovery button and **THEN** power on the board.

> The recovery button is located at the edge of the board near the GPIO pins, while the eMMC boot button is on the inner side - Don't be confused!
> For details please refer to: https://milkv.io/docs/meles/hardware/meles-main-board

```shell
sudo ./cct list -u /dev/ttyUSB0
#Please change accordingly. Depending on your debugger, e.g. for CH343P it's ttyACM0 rather than ttyUSB0
sudo ./cct download -d ram0 -f iw-single-line.bin -v checksum -r
sudo ./cct download -u /dev/ttyUSB0 -d qspi0 -f ./u-boot-with-spl-meles.bin -v checksum -r -t 1200
```

Wait for the flashing progress to complete, then power off the board, hold the recovery button and reconnect it to PC.

### Flashing Image using `fastboot` onto the Development Board

Check connection status:

```shell
$ lsusb | grep T-HEAD
Bus 001 Device 045: ID 2345:7654 T-HEAD USB download gadget
```

Next, execute the following commands to download, extract and flash the images to your board's eMMC.

> If `fastboot` doesn't pick up the board or you encounter flashing issues, check the device connection and try running `fastboot` as a privileged user (i.e. `sudo`). Doing so is usually required under Linux since the default USB VID/PID is not in the default udev rules.

```shell
wget https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/testing/20241105/v0.1/meles/boot-20241105-115243.ext4.zst
wget https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/testing/20241105/v0.1/meles/root-20241105-115243.ext4.zst
zstd -T0 -dv *.ext4.zst
sudo fastboot flash ram u-boot-with-spl-meles.bin
sudo fastboot reboot
sudo fastboot flash boot boot-meles-20241229_032258.ext4
sudo fastboot flash root root-meles-20241229_032258.ext4
```

After the flashing process, reset the board and you're good to go.

## Expected Results

The system should boot normally and allow login through the onboard serial port.

## Actual Results

Boot fails with a kernel panic.

### Boot Log

```log
brom_ver 8
[APP][E] protocol_connect failed, exit.
-----------------------------------------
  _____             _  _____ _____  _  __
 |  __ \           (_)/ ____|  __ \| |/ /
 | |__) |   _ _   _ _| (___ | |  | | ' /
 |  _  / | | | | | | |\___ \| |  | |  <
 | | \ \ |_| | |_| | |____) | |__| | . \
 |_|  \_\__,_|\__, |_|_____/|_____/|_|\_\
               __/ |
              |___/
                    -- Presented by ISCAS
-----------------------------------------

U-Boot SPL 2020.01-g96627087 (May 29 2024 - 08:34:19 +0000)
FM[1] lpddr4x dualrank freq=3733 64bit dbi_off=n sdram init
found ddr boundary <0x400000000>
ddr initialized, jump to uboot
image has no header


U-Boot 2020.01-g96627087 (May 29 2024 - 08:34:19 +0000)

CPU:   rv64imafdcvsu
Model: Milk-V Meles
DRAM:  16 GiB
aon wakeup by gpio enabled
aon wakeup by rtc enabled
iic id:0 addr_mode:0 speed:2
C910 CPU FREQ: 750MHz
MMC:   sdhci@ffe7080000: 0, sd@ffe7090000: 1
Loading Environment from MMC... OK
In:    serial@ffe7014000
Out:   serial
Err:   serial
light_c910_set_gpio_output_high: trying to set gpio output high
ethaddr: 32:49:d2:24:9e:0c
eth1addr: 32:49:d2:24:9e:0d
Net:   ethernet@ffe7070000 (eth0) using MAC address - 32:49:d2:24:9e:0c
eth0: ethernet@ffe7070000
Hit any key to stop autoboot:  0
Unknown command 'usb' - try 'help'
Card did not respond to voltage select!
50248 bytes read in 1 ms (47.9 MiB/s)
pmic_dev_num:2 offset:60 addr:1099510546492
regu_num:17 offset:178 addr:1099510546610
-->pmic_dev_num:2 offset:60
-->regu_num:17 offset:178
5281216 bytes read in 17 ms (296.3 MiB/s)
86392 bytes read in 1 ms (82.4 MiB/s)
 not find hibernate sign
fixup memory region from [0x000200000 ~ 0x200000000] to [0x000200000 ~ 0x400000000]
Retrieving file: /extlinux/extlinux.conf
454 bytes read in 1 ms (443.4 KiB/s)
1:      Linux openEuler-riscv
Retrieving file: /Image
35675136 bytes read in 113 ms (301.1 MiB/s)
append: root=/dev/mmcblkXp4 console=ttyS0,115200 rootwait rw earlycon clk_ignore_unused loglevel=7 eth= rootrwoptions=rw,noatime rootrwreset=yes
Retrieving file: /dtbs/thead/th1520-milkv-meles.dtb
88452 bytes read in 2 ms (42.2 MiB/s)
   Using Device Tree in place at 0000000003800000, end 0000000003818983

Starting kernel ...

## fdt has reset_sample

OpenSBI v0.9
   ____                    _____ ____ _____
  / __ \                  / ____|  _ \_   _|
 | |  | |_ __   ___ _ __ | (___ | |_) || |
 | |  | | '_ \ / _ \ '_ \ \___ \|  _ < | |
 | |__| | |_) |  __/ | | |____) | |_) || |_
  \____/| .__/ \___|_| |_|_____/|____/_____|
        | |
        |_|

Platform Name             : Milk-V Meles
Platform Features         : mfdeleg
Platform HART Count       : 4
Platform IPI Device       : clint
Platform Timer Device     : clint
Platform Console Device   : uart8250
Platform HSM Device       : ---
Platform SysReset Device  : thead_reset
Firmware Base             : 0x0
Firmware Size             : 140 KB
Runtime SBI Version       : 0.3

Domain0 Name              : root
Domain0 Boot HART         : 0
Domain0 HARTs             : 0*,1*,2*,3*
Domain0 Region00          : 0x000000ffdc000000-0x000000ffdc00ffff (I)
Domain0 Region01          : 0x0000000000000000-0x000000000003ffff ()
Domain0 Region02          : 0x0000000000000000-0xffffffffffffffff (R,W,X)
Domain0 Next Address      : 0x0000000000200000
Domain0 Next Arg1         : 0x0000000003800000
Domain0 Next Mode         : S-mode
Domain0 SysReset          : yes

core:0 light_final_init: line:241 enter. cold_boot:1
Boot HART ID              : 0
Boot HART Domain          : root
Boot HART ISA             : rv64imafdcvsux
Boot HART Features        : scounteren,mcounteren,time
Boot HART PMP Count       : 0
Boot HART PMP Granularity : 0
Boot HART PMP Address Bits: 0
Boot HART MHPM Count      : 16
Boot HART MHPM Count      : 16
Boot HART MIDELEG         : 0x0000000000000222
Boot HART MEDELEG         : 0x000000000000b109
[    0.000000] Linux version 5.10.113-7.oe2403.riscv64 (abuild@openeuler-riscv64) (gcc_old (GCC) 12.3.1 (openEuler 12.3.1-31.oe2403), GNU ld (GNU Binutils) 2.41) #1 SMP PREEMPT Tue Jul 23 12:45:59 UTC 2024
[    0.000000] earlycon: uart0 at MMIO32 0x000000ffe7014000 (options '115200n8')
[    0.000000] printk: bootconsole [uart0] enabled
[    0.000000] efi: UEFI not found.
[    0.000000] Reserved memory: created CMA memory pool at 0x00000000d8000000, size 512 MiB
[    0.000000] OF: reserved mem: initialized node linux,cma, compatible id shared-dma-pool
[    0.000000] Zone ranges:
[    0.000000]   DMA32    [mem 0x0000000000200000-0x00000000ffffffff]
[    0.000000]   Normal   [mem 0x0000000100000000-0x00000001ffffffff]
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000000200000-0x000000000fffffff]
[    0.000000]   node   0: [mem 0x0000000010000000-0x00000000166fffff]
[    0.000000]   node   0: [mem 0x0000000016700000-0x000000001bffffff]
[    0.000000]   node   0: [mem 0x000000001c000000-0x000000001dffffff]
[    0.000000]   node   0: [mem 0x000000001e000000-0x00000000383fffff]
[    0.000000]   node   0: [mem 0x0000000038400000-0x000000003a1fffff]
[    0.000000]   node   0: [mem 0x000000003a200000-0x00000001ffffffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000000200000-0x00000001ffffffff]
[    0.000000] software IO TLB: mapped [mem 0x00000000fbfff000-0x00000000fffff000] (64MB)
[    0.000000] SBI specification v0.3 detected
[    0.000000] SBI implementation ID=0x1 Version=0x9
[    0.000000] SBI v0.2 TIME extension detected
[    0.000000] SBI v0.2 IPI extension detected
[    0.000000] SBI v0.2 RFENCE extension detected
[    0.000000] SBI v0.2 HSM extension detected
[    0.000000] riscv: ISA extensions acdfimsuv
[    0.000000] riscv: ELF capabilities acdfimv
[    0.000000] percpu: Embedded 28 pages/cpu s74392 r8192 d32104 u114688
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 2063880
[    0.000000] Kernel command line: root=/dev/mmcblkXp4 console=ttyS0,115200 rootwait rw earlycon clk_ignore_unused loglevel=7 eth= rootrwoptions=rw,noatime rootrwreset=yes
[    0.000000] Dentry cache hash table entries: 1048576 (order: 11, 8388608 bytes, linear)
[    0.000000] Inode-cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
[    0.000000] Sorting __ex_table...
[    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
[    0.000000] Memory: 7381924K/8386560K available (12979K kernel code, 4975K rwdata, 14336K rodata, 368K init, 509K bss, 480348K reserved, 524288K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
[    0.000000] ftrace: allocating 47712 entries in 187 pages
[    0.000000] ftrace: allocated 187 pages with 6 groups
[    0.000000] rcu: Preemptible hierarchical RCU implementation.
[    0.000000] rcu:     RCU restricting CPUs from NR_CPUS=8 to nr_cpu_ids=4.
[    0.000000]  Trampoline variant of Tasks RCU enabled.
[    0.000000]  Rude variant of Tasks RCU enabled.
[    0.000000]  Tracing variant of Tasks RCU enabled.
[    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
[    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
[    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
[    0.000000] riscv-intc: 64 local interrupts mapped
[    0.000000] plic: interrupt-controller@ffd8000000: mapped 240 interrupts with 4 handlers for 8 contexts.
[    0.000000] random: get_random_bytes called from 0xffffffe000002cf8 with crng_init=0
[    0.000000] riscv_timer_init_dt: Registering clocksource cpuid [0] hartid [0]
[    0.000000] clocksource: riscv_clocksource: mask: 0xffffffffffffffff max_cycles: 0x1623fa770, max_idle_ns: 881590404476 ns
[    0.000008] sched_clock: 64 bits at 3000kHz, resolution 333ns, wraps every 4398046511097ns
[    0.008783] Console: colour dummy device 80x25
[    0.013373] Calibrating delay loop (skipped), value calculated using timer frequency.. 6.00 BogoMIPS (lpj=12000)
[    0.023654] pid_max: default: 32768 minimum: 301
[    0.028524] LSM: Security Framework initializing
[    0.033348] Mount-cache hash table entries: 16384 (order: 5, 131072 bytes, linear)
[    0.041049] Mountpoint-cache hash table entries: 16384 (order: 5, 131072 bytes, linear)
[    0.052048] ASID allocator initialised with 65536 entries
[    0.057718] rcu: Hierarchical SRCU implementation.
[    0.063857] EFI services will not be available.
[    0.069040] smp: Bringing up secondary CPUs ...
core:0 light_hart_start: line:196 enter
core:1 light_final_init: line:241 enter. cold_boot:0
core:0 light_hart_start: line:203 exit
core:0 light_hart_start: line:196 enter
core:2 light_final_init: line:241 enter. cold_boot:0
core:0 light_hart_start: line:203 exit
core:0 light_hart_start: line:196 enter
core:3 light_final_init: line:241 enter. cold_boot:0
core:0 light_hart_start: line:203 exit
[    0.111519] smp: Brought up 1 node, 4 CPUs
[    0.117924] devtmpfs: initialized
[    0.153493] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.163419] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
[    0.186039] pinctrl core: initialized pinctrl subsystem
[    0.192867] NET: Registered protocol family 16
[    0.222062] DMA: preallocated 1024 KiB GFP_KERNEL pool for atomic allocations
[    0.230630] DMA: preallocated 1024 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
[    0.238891] audit: initializing netlink subsys (disabled)
[    0.244731] audit: type=2000 audit(0.152:1): state=initialized audit_enabled=0 res=1
[    0.245551] thermal_sys: Registered thermal governor 'step_wise'
[    0.252605] thermal_sys: Registered thermal governor 'power_allocator'
[    0.259803] cpuidle: using governor ladder
[    0.270665] cpuidle: using governor menu
[    0.317975] light-iopmp iopmp: invalid iopmp tap:-22
[    0.323059] light-iopmp iopmp: invalid iopmp tap:-22
[    0.406239] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
[    0.413104] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
[    0.433329] vdd_1v8: supplied by vdd_5v
[    0.438623] vgaarb: loaded
[    0.441980] SCSI subsystem initialized
[    0.446206] usbcore: registered new interface driver usbfs
[    0.451907] usbcore: registered new interface driver hub
[    0.457414] usbcore: registered new device driver usb
[    0.463150] mc: Linux media interface: v0.10
[    0.467547] videodev: Linux video capture interface: v2.00
[    0.474068] Advanced Linux Sound Architecture Driver Initialized.
[    0.481143] Bluetooth: Core ver 2.22
[    0.484852] NET: Registered protocol family 31
[    0.489382] Bluetooth: HCI device and connection manager initialized
[    0.495842] Bluetooth: HCI socket layer initialized
[    0.500813] Bluetooth: L2CAP socket layer initialized
[    0.505962] Bluetooth: SCO socket layer initialized
[    0.511752] clocksource: Switched to clocksource riscv_clocksource
[    1.469634] NET: Registered protocol family 2
[    1.474531] IP idents hash table entries: 131072 (order: 8, 1048576 bytes, linear)
[    1.489219] tcp_listen_portaddr_hash hash table entries: 4096 (order: 4, 65536 bytes, linear)
[    1.498047] TCP established hash table entries: 65536 (order: 7, 524288 bytes, linear)
[    1.506462] TCP bind hash table entries: 65536 (order: 8, 1048576 bytes, linear)
[    1.514912] TCP: Hash tables configured (established 65536 bind 65536)
[    1.521786] UDP hash table entries: 4096 (order: 5, 131072 bytes, linear)
[    1.528806] UDP-Lite hash table entries: 4096 (order: 5, 131072 bytes, linear)
[    1.536480] NET: Registered protocol family 1
[    1.542066] RPC: Registered named UNIX socket transport module.
[    1.548093] RPC: Registered udp transport module.
[    1.552881] RPC: Registered tcp transport module.
[    1.557646] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    1.565176] PCI: CLS 0 bytes, default 64
[    1.570580] khv_probe, 164, irq: 40.
[    1.576470] Initialise system trusted keyrings
[    1.581349] workingset: timestamp_bits=46 max_order=21 bucket_order=0
[    1.606390] NFS: Registering the id_resolver key type
[    1.611627] Key type id_resolver registered
[    1.615896] Key type id_legacy registered
[    1.620187] nfs4filelayout_init: NFSv4 File Layout Driver Registering...
[    1.626998] nfs4flexfilelayout_init: NFSv4 Flexfile Layout Driver Registering...
[    1.634538] jffs2: version 2.2. (NAND) © 2001-2006 Red Hat, Inc.
[    1.641519] fuse: init (API version 7.32)
[    1.646455] 9p: Installing v9fs 9p2000 file system support
[    1.739689] NET: Registered protocol family 38
[    1.744238] Key type asymmetric registered
[    1.748404] Asymmetric key parser 'x509' registered
[    1.753416] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 247)
[    1.761133] io scheduler mq-deadline registered
[    1.765813] io scheduler kyber registered
[    1.772062] light-pinctrl fffff4a000.padctrl-aosys: initialized light pinctrl driver
[    1.780406] light-pinctrl ffcb01d000.padctrl-audiosys: initialized light pinctrl driver
[    1.813432] light-fm-clk ffef010000.clock-controller: succeed to register light fullmask clock driver
[    1.833244] visys-clk-gate-provider soc:visys-clk-gate: succeed to register visys gate clock provider
[    1.847358] vpsys-clk-gate-provider ffecc30000.vpsys-clk-gate: succeed to register vpsys gate clock provider
[    1.867844] vosys-clk-gate-provider ffef528000.vosys-clk-gate: succeed to register vosys gate clock provider
[    1.878472] dspsys-clk-gate-provider soc:dspsys-clk-gate: cannot find regmap for tee dsp system register
[    1.894381] dspsys-clk-gate-provider soc:dspsys-clk-gate: succeed to register dspsys gate clock provider
[    1.904573] light_audiosys_clk_probe audiosys_regmap=0xffffffe100935800
[    1.920417] audiosys-clk-gate-provider soc:audiosys-clk-gate: succeed to register audiosys gate clock provider
[    1.939378] miscsys-clk-gate-provider soc:miscsys-clk-gate: succeed to register miscsys gate clock provider
[    1.950431] dw_axi_dmac_platform ffefc00000.dmac: DesignWare AXI DMA Controller, 4 channels
[    1.961387] dw_axi_dmac_platform ffc8000000.audio_dmac: DesignWare AXI DMA Controller, 16 channels
[    1.973010] no vdmabuf_reserved_memory node
[    1.977272] virtio-vdmabuf: carveout buf not setup -22
[    2.074075] Serial: 8250/16550 driver, 6 ports, IRQ sharing disabled
[    2.092279] vs-dc ffef600000.dc8200: dpu0pll_on:0 dpu1pll_on:1
[    2.117698] loop: module loaded
[    2.125968] tun: Universal TUN/TAP device driver, 1.6
[    2.133909] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    2.140204] ohci-pci: OHCI PCI platform driver
[    2.145763] usbcore: registered new interface driver usb-storage
[    2.151916] usbcore: registered new interface driver ums-sddr09
[    2.157960] usbcore: registered new interface driver ums-sddr55
[    2.164457] mousedev: PS/2 mouse device common for all mice
[    2.171982] xgene-rtc fffff40000.rtc: registered as rtc0
[    2.177478] xgene-rtc fffff40000.rtc: setting system clock to 1970-01-01T00:00:00 UTC (0)
[    2.186051] i2c /dev entries driver
[    2.192649] light_reset_deassert id:0
[    2.196419] dw_wdt ffefc30000.watchdog: No valid TOPs array specified
[    2.203938] light_reset_deassert id:1
[    2.207656] dw_wdt ffefc31000.watchdog: No valid TOPs array specified
[    2.215590] Watchdog module: light-wdt loaded
[    2.220717] device-mapper: ioctl: 4.44.0-ioctl (2021-02-01) initialised: dm-devel@redhat.com
[    2.229871] Bluetooth: HCI UART driver ver 2.2.0c90be4.20211102-175223
[    2.236547] Bluetooth: HCI H4 protocol initialized
[    2.241426] Bluetooth: HCI Realtek H5 protocol initialized
[    2.247020] rtk_btcoex: rtk_btcoex_init: version: 1.2
[    2.252185] rtk_btcoex: create workqueue
[    2.256470] rtk_btcoex: alloc buffers 1792, 2432 for ev and l2
[    2.264500] sdhci: Secure Digital Host Controller Interface driver
[    2.270808] sdhci: Copyright(c) Pierre Ossman
[    2.275237] sdhci-pltfm: SDHCI platform and OF driver helper
[    2.286298] ledtrig-cpu: registered to indicate activity on CPUs
[    2.294049] usbcore: registered new interface driver usbhid
[    2.299842] usbhid: USB HID core driver
[    2.305056] misc vhost-vdmabuf: no vdmabuf_reserved_memory node
[    2.311092] misc vhost-vdmabuf: vhost-vdmabuf: carveout buf not setup -22
[    2.318013] mmc0: SDHCI controller on ffe7080000.sdhci [ffe7080000.sdhci] using ADMA 64-bit
[    2.326569] misc vhost-vdmabuf: vhost-vdmabuf: init successfully
[    2.334343] thead,light-mbox-client mbox_910t_client2: Successfully registered
[    2.342995] light-adc fffff51000.adc: Thead light adc registered.
thead_vendor_ext_provider: extid:9000001 funcid:0
thead_vendor_ext_provider: extid:9000001 funcid:0
thead_vendor_ext_provider: extid:9000001 funcid:0
thead_vendor_ext_provider: extid:9000001 funcid:0
[    2.368361] [perf] T-HEAD C900 PMU v1 probed
[    2.373628] light_efuse ffff210000.efuse: succeed to register light efuse driver
[    2.389382] IPVS: Registered protocols (TCP, UDP, SCTP, AH, ESP)
[    2.395991] IPVS: Connection hash table configured (size=4096, memory=64Kbytes)
[    2.403629] IPVS: ipvs loaded.
[    2.406787] IPVS: [rr] scheduler registered.
[    2.411320] IPv4 over IPsec tunneling driver
[    2.418095] NET: Registered protocol family 10
[    2.421251] mmc0: new HS400 MMC card at address 0001
[    2.424460] Segment Routing with IPv6
[    2.428900] mmcblk0: mmc0:0001 A3A562 115 GiB
[    2.431872] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
[    2.436433] mmcblk0boot0: mmc0:0001 A3A562 partition 1 4.00 MiB
[    2.443067] NET: Registered protocol family 17
[    2.448521] mmcblk0boot1: mmc0:0001 A3A562 partition 2 4.00 MiB
[    2.452698] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
[    2.472099] mmcblk0rpmb: mmc0:0001 A3A562 partition 3 16.0 MiB, chardev (245:0)
[    2.472160] Bluetooth: RFCOMM TTY layer initialized
[    2.484685] Bluetooth: RFCOMM socket layer initialized
[    2.489966] Bluetooth: RFCOMM ver 1.11
[    2.492744]  mmcblk0: p1 p2 p3 p4
[    2.493896] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
[    2.502702] Bluetooth: BNEP socket layer initialized
[    2.507815] Bluetooth: HIDP (Human Interface Emulation) ver 1.2
[    2.513835] Bluetooth: HIDP socket layer initialized
[    2.518939] 8021q: 802.1Q VLAN Support v1.8
[    2.523228] [WLAN_RFKILL]: Enter rfkill_wlan_init
[    2.528453] [BT_RFKILL]: Enter rfkill_rk_init
[    2.533420] 9pnet: Installing 9P2000 support
[    2.537843] Key type dns_resolver registered
[    2.542501] NET: Registered protocol family 40
[    2.547898] registered taskstats version 1
[    2.552077] Loading compiled-in X.509 certificates
[    2.559109]
[    2.560687] ********************************************************************
[    2.568174] **     NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE           **
[    2.575659] **                                                                **
[    2.583142] **  WRITEABLE clk DebugFS SUPPORT HAS BEEN ENABLED IN THIS KERNEL **
[    2.590623] **                                                                **
[    2.598095] ** This means that this kernel is built to expose clk operations  **
[    2.605557] ** such as parent or rate setting, enabling, disabling, etc.      **
[    2.613036] ** to userspace, which may compromise security on your system.    **
[    2.620517] **                                                                **
[    2.627987] ** If you see this message and you are not debugging the          **
[    2.635494] ** kernel, report this immediately to your vendor!                **
[    2.642988] **                                                                **
[    2.650482] **     NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE           **
[    2.657999] ********************************************************************
[    2.738329] i2c_designware ffcb01a000.i2c: going to probe light i2c driver
[    2.746661] es8156 5-0009: supply AVDD not found, using dummy regulator
[    2.753689] es8156 5-0009: supply DVDD not found, using dummy regulator
[    2.760514] es8156 5-0009: supply PVDD not found, using dummy regulator
[    2.768159] light-pinctrl ffe7f3c000.padctrl1-apsys: initialized light pinctrl driver
[    2.776623] light-pinctrl ffec007000.padctrl0-apsys: initialized light pinctrl driver
[    2.789507] pwm-light ffec01c000.pwm: succeed to add a pwm chip
[    2.796114] spi-flash@0 enforce active low on chipselect handle
[    2.802170] get gpio succes 4
[    2.806249] spi-nor spi1.0: w25q64jwm (8192 Kbytes)
[    2.812117] 1 fixed-partitions partitions found on MTD device spi1.0
[    2.818580] Creating 1 MTD partitions on "spi1.0":
[    2.823471] 0x000000000000-0x000000800000 : "loader"
[    2.835859] fff7f08000.serial: ttyS4 at MMIO 0xfff7f08000 (irq = 6, base_baud = 6250000) is a 16550A
[    2.847117] ffe7014000.serial: ttyS0 at MMIO 0xffe7014000 (irq = 4, base_baud = 6250000) is a 16550A
[    2.856761] printk: console [ttyS0] enabled
[    2.856761] printk: console [ttyS0] enabled
[    2.865296] printk: bootconsole [uart0] disabled
[    2.865296] printk: bootconsole [uart0] disabled
[    2.875630] light_dwmac_eth ffe7070000.ethernet: IRQ eth_wake_irq not found
[    2.882665] light_dwmac_eth ffe7070000.ethernet: IRQ eth_lpi not found
[    2.889458] light_dwmac_eth ffe7070000.ethernet: Cannot get CSR clock
[    2.895998] light_dwmac_eth ffe7070000.ethernet: PTP uses main clock
[    2.902409] light_dwmac_eth ffe7070000.ethernet: no reset control found
[    2.909137] light_dwmac_eth ffe7070000.ethernet: get_rate gmac_pll_clk_freq 500000000
[    2.917102] light_dwmac_eth ffe7070000.ethernet: id: 0
[    2.922282] light_dwmac_eth ffe7070000.ethernet: phy interface: 9
[    2.928479] light_dwmac_eth ffe7070000.ethernet: set phy_if_reg val 0x1
[    2.935228] RX clk delay: 0x0
[    2.938234] TX clk delay: 0x0
[    2.941654] light_dwmac_eth ffe7070000.ethernet: User ID: 0x10, Synopsys ID: 0x37
[    2.949202] light_dwmac_eth ffe7070000.ethernet:     DWMAC1000
[    2.954818] light_dwmac_eth ffe7070000.ethernet: DMA HW capability register supported
[    2.962686] light_dwmac_eth ffe7070000.ethernet: RX Checksum Offload Engine supported
[    2.970551] light_dwmac_eth ffe7070000.ethernet: COE Type 2
[    2.976174] light_dwmac_eth ffe7070000.ethernet: TX Checksum insertion supported
[    2.983604] light_dwmac_eth ffe7070000.ethernet: Enhanced/Alternate descriptors
[    2.990951] light_dwmac_eth ffe7070000.ethernet: Enabled extended descriptors
[    2.998119] light_dwmac_eth ffe7070000.ethernet: Ring mode enabled
[    3.004333] light_dwmac_eth ffe7070000.ethernet: Enable RX Mitigation via HW Watchdog Timer
[    3.012740] light_dwmac_eth ffe7070000.ethernet: Using 0 bits DMA width,skb alloc dma32 flag 4
[    3.032649] vs-drm display-subsystem: bound ffef600000.dc8200 (ops dc_component_ops)
[    3.040764] dwhdmi-light ffef540000.dw-hdmi-tx: Detected HDMI TX controller v2.14a with HDCP (DWC HDMI 2.0 TX PHY)
[    3.052380] dwhdmi-light ffef540000.dw-hdmi-tx: registered DesignWare HDMI I2C bus driver
[    3.060536] mmc1: SDHCI controller on ffe7090000.sd [ffe7090000.sd] using ADMA 64-bit
[    3.061188] vs-drm display-subsystem: bound ffef540000.dw-hdmi-tx (ops dw_hdmi_light_ops)
[    3.078124] [drm] Initialized vs-drm 1.0.0 20191101 for display-subsystem on minor 0
[    3.086149] vs-drm display-subsystem: [drm] Cannot find any crtc or sizes
[    3.097998] light_aon_probe:virtual_log_mem=0x(____ptrval____), phy base=0x33600000,size:2097152
[    3.108075] succeed to create power domain debugfs direntry
[    3.115526] get regual dual rail---->
[    3.141918] cpu cpu0: EM: created perf domain
[    3.148120] cpufreq: cpufreq_online: CPU0: Running at unlisted initial frequency: 750000 KHz, changing to: 800000 KHz
[    3.159244] cpu cpu0: finish to register cpufreq driver
[    3.165543] thead,light-aon-test aon:light-aon-test: Successfully registered
[    3.190529] random: fast init done
[    3.197817] Get audio text phy mem:0x00032000000, size:14680064
[    3.198214] sdhci-dwcmshc ffe70a0000.sd: allocated mmc-pwrseq
[    3.203832] PM: hibernation: Registered nosave memory: [mem 0x32000000-0x32dfffff]
[    3.203846] light-pm soc:aon_suspend_ctrl: Light power management control sys successfully registered
[    3.209675] light-event soc:light-event: magicnum:0x5a5a5a5a mode:0x22
[    3.209685] light-event soc:light-event: light-event driver init successfully
[    3.240687] light_regdump_probe got mem start 0x38400000 size 0x1e00000
[    3.247915] [light_wdt_probe,346] register power off callback
[    3.253721] succeed to register light pmic watchdog
[    3.260382] light rpmsg: Ready for cross core communication!
[    3.266075] light rpmsg: rproc_name = m4
[    3.271249] virtio_rpmsg_bus virtio0: rpmsg host is online
[    3.280838] light_rpmsg_probe:virtual_log_mem=0x(____ptrval____), phy base=0x33400000,size:2097152
[    3.289859] virtio_rpmsg_bus virtio0: creating channel rpmsg-virtual-char-channel-1 addr 0xee
[    3.289989] light rpmsg: driver is registered.
[    3.302959] cfg80211: Loading compiled-in X.509 certificates for regulatory database
[    3.312227] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
[    3.318884] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
[    3.319770] clk: Not disabling unused clocks
[    3.327553] cfg80211: failed to load regulatory.db
[    3.331871] ALSA device list:
[    3.339687]   #0: Light-Sound-Card
[    3.343465] dw-apb-uart ffe7014000.serial: forbid DMA for kernel console
[    3.359773] mmc2: SDHCI controller on ffe70a0000.sd [ffe70a0000.sd] using ADMA 64-bit
[    3.399811] mmc2: queuing unknown CIS tuple 0x80 (2 bytes)
[    3.407031] mmc2: queuing unknown CIS tuple 0x80 (3 bytes)
[    3.414262] mmc2: queuing unknown CIS tuple 0x80 (3 bytes)
[    3.414898] List of all partitions:
[    3.422810] mmc2: queuing unknown CIS tuple 0x80 (7 bytes)
[    3.423411] b300       120832000 mmcblk0
[    3.428840]  driver: mmcblk
[    3.432382] mmc2: queuing unknown CIS tuple 0x81 (9 bytes)
[    3.432871]   b301            2031 mmcblk0p1 f29e63b4-9bf4-4e30-bce5-d91126520f44
[    3.441161]
[    3.450175]   b302          512000 mmcblk0p2 76655d00-86dc-4bcc-9d9e-e94f049ba2a6
[    3.450179]
[    3.459162]   b303         4194304 mmcblk0p3 5ebcaaf0-e098-43b9-beef-1f8deedd135f
[    3.459165]
[    3.468177]   b304       116123631 mmcblk0p4 80a5a8e9-c744-491a-93c1-4f4194fd690b
[    3.468182]
[    3.477174] 1f00            8192 mtdblock0
[    3.477177]  (driver?)
[    3.483740] No filesystem could mount root, tried:
[    3.483744]  ext3
[    3.488630]  ext2
[    3.490557]  ext4
[    3.492492]  vfat
[    3.494422]  msdos
[    3.494825] mmc2: new ultra high speed SDR104 SDIO card at address 0001
[    3.496367]  iso9660
[    3.496370]  fuseblk
[    3.496372]
[    3.496384] light-event soc:light-event: set rebootmode:0x22
[    3.516603] Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(179,4)
[    3.525044] SMP: stopping secondary CPUs
[    3.528989] enter panic_cpufreq_notifier_call
[    3.533521] finish to execute cpufreq notifier callback on panic
[    3.539603] ---[ end Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(179,4) ]---
```
## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test failed.
