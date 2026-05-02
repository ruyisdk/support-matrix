---
sys: freebsd
sys_ver: "15.1-BETA1"
sys_var: null

status: basic
last_update: 2026-05-02
---

# FreeBSD VisionFive 2 Test Report

## Test Environment

### System Information

- System Version: 15.1-BETA1
- Download Link: https://download.freebsd.org/releases/ISO-IMAGES/15.1/FreeBSD-15.1-BETA1-riscv-riscv64-GENERICSD.img.xz

### Hardware Information

- StarFive VisionFive 2
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing the Installation Image

Download and decompress the image

```bash
wget https://download.freebsd.org/releases/ISO-IMAGES/15.1/FreeBSD-15.1-BETA1-riscv-riscv64-GENERICSD.img.xz
unxz FreeBSD-15.1-BETA1-riscv-riscv64-GENERICSD.img.xz
```

Flash the image to the microSD card.

```bash
dd if=FreeBSD-15.1-BETA1-riscv-riscv64-GENERICSD.img of=/dev/your/device status=progress
```

### Booting the System

Insert the microSD card, connect the serial port, and use 1-bit QSPI Nor Flash mode (i.e. RGPIO_0 = 0, RGPIO_1 = 0) to boot.

Manually interrupt the u-boot process and input the boot command:

```bash
load mmc 1:3 ${fdt_addr_r} dtb/starfive/jh7110-starfive-visionfive-2-v1.3b.dtb
load mmc 1:3 ${kernel_addr_r} efi/boot/bootriscv64.efi
bootefi ${kernel_addr_r} ${fdt_addr_r}
```

Upon seeing `Hit [Enter] to boot immediately, or any other key for command prompt` in the serial console, press any key other than Enter for the FreeBSD stage 3 bootloader prompt.

Use serial console instead of EFI framebuffer ([e2a08ac9ce](https://codeberg.org/FreeBSD/freebsd-src/commit/e2a08ac9ce424f543a2f03c67fb882fdabbdd32a)):

```shell
set console="comconsole"
boot
```

### Logging into the System

Log into the system via the serial port.

Username: `root`

Password: `root`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
StarFive # bootefi ${kernel_addr_r} ${fdt_addr_r}
Card did not respond to voltage select! : -110
** Unable to read file ubootefi.var **
Failed to load EFI variables
Consoles: EFI console
    Reading loader env vars from /efi/freebsd/loader.env
Setting currdev to disk0p3:
FreeBSD/riscv EFI loader, Revision 3.0

   Command line arguments: console=tty1 console=ttyS0,115200 debug rootwait earlycon=sbi
   Image base: 0xf660e000
   EFI version: 2.80
   EFI Firmware: Das U-Boot (rev 8225.4096)
   Console: ttyS0,115200 (0)
   Load Path: /efi\boot\bootriscv64.efi
   Load Device: /VenHw(e61d73b9-a384-4acc-aeab-82e828f3628b)/SD(1)/SD(1)/HD(3,GPT,6272ec00-453e-11f1-a254-0cc47ad8b808,0x4000,0x1b000)
Trying ESP: /VenHw(e61d73b9-a384-4acc-aeab-82e828f3628b)/SD(1)/SD(1)/HD(3,GPT,6272ec00-453e-11f1-a254-0cc47ad8b808,0x4000,0x1b000)
Setting currdev to disk0p3:
Trying: /VenHw(e61d73b9-a384-4acc-aeab-82e828f3628b)/SD(1)/SD(1)/HD(1,GPT,62713036-453e-11f1-a254-0cc47ad8b808,0x1000,0x1000)
Setting currdev to disk0p1:
Trying: /VenHw(e61d73b9-a384-4acc-aeab-82e828f3628b)/SD(1)/SD(1)/HD(2,GPT,6272144b-453e-11f1-a254-0cc47ad8b808,0x2000,0x2000)
Setting currdev to disk0p2:
Trying: /VenHw(e61d73b9-a384-4acc-aeab-82e828f3628b)/SD(1)/SD(1)/HD(4,GPT,6273c70d-453e-11f1-a254-0cc47ad8b808,0x1f000,0xddfb000)
Setting currdev to disk0p4:
Loading /boot/defaults/loader.conf0e000, 0x0
Loading /boot/defaults/loader.conf
Loading /boot/device.hints
Loading /boot/loader.conf
Loading /boot/loader.conf.local
Loading kernel...
/boot/kernel/kernel text=0x61e92c text=0x1687d4 data=0x118ad8 data=0xf00+0x1e6ce0 0x8+0x1283b8+0x8+0x10d3ea
Loading configured modules...
/boot/kernel/umodem.ko text=0x20c0 text=0x1290 data=0x700+0x4 0x8+0x6900+0x8+0xf04
loading required module 'ucom'
/boot/kernel/ucom.ko text=0x254c text=0x3074 data=0x948+0x858 0x8+0x120a8+0x8+0x16e8
/boot/entropy size=0x1000
/etc/hostid size=0x25

Hit [Enter] to boot immediately, or any other key for command prompt.
Booting [/boot/kernel/kernel] in 9 seconds...

Type '?' for a list of commands, 'help' for more detailed help.
OK set console="comconsole"
OK boot
Using DTB provided by EFI at 0x47f00000.
Kernel args: (null)
Loading splash ok
Loading shutdown splash ok
EFI framebuffer information:
addr, size     0xfe000000, 0x0
dimensions     0 x 0
stride         0
masks          0x00ff0000, 0x0000ff00, 0x000000ff, 0xff000000
clk u0_mipitx_dphy_clk_txesc already disabled
---<<BOOT>>---
Copyright (c) 1992-2025 The FreeBSD Project.
Copyright (c) 1979, 1980, 1983, 1986, 1988, 1989, 1991, 1992, 1993, 1994
	The Regents of the University of California. All rights reserved.
FreeBSD is a registered trademark of The FreeBSD Foundation.
FreeBSD 15.1-BETA1 releng/15.1-n283455-58777180c5b0 GENERIC riscv
FreeBSD clang version 19.1.7 (https://github.com/llvm/llvm-project.git llvmorg-19.1.7-0-gcd708029e0b2)
VT(efifb): resolution 0x0
SBI: OpenSBI v1.2
SBI Specification Version: 1.0
CPU 0  : Vendor=SiFive Core=6/7/P200/X200-Series Processor (Hart 1)
  marchid=0x8000000000000007, mimpid=0x4210427
  MMU: 0x1<Sv39>
  ISA: 0x112d<Atomic,Compressed,Double,Float,Mult/Div>
  S-mode Extensions: 0
real memory  = 4294967296 (4096 MB)
avail memory = 4171530240 (3978 MB)
FreeBSD/SMP: Multiprocessor System Detected: 4 CPUs
CPU 1  : Vendor=SiFive Core=6/7/P200/X200-Series Processor (Hart 2)
CPU 2  : Vendor=SiFive Core=6/7/P200/X200-Series Processor (Hart 3)
CPU 3  : Vendor=SiFive Core=6/7/P200/X200-Series Processor (Hart 4)
random: unblocking device.
random: entropy device external interface
kbd0 at kbdmux0
ofwbus0: <Open Firmware Device Tree>
simplebus0: <Flattened device tree simple bus> on ofwbus0
starfive_syscon0: <JH7110 STG syscon> mem 0x10240000-0x10240fff on simplebus0
starfive_syscon1: <JH7110 SYS syscon> mem 0x13030000-0x13030fff on simplebus0
jh7110_clk_pll0: <StarFive JH7110 PLL clock generator> mem 0x13030000-0x13030fff on starfive_syscon1
starfive_syscon2: <JH7110 AON syscon> mem 0x17010000-0x17010fff on simplebus0
jh7110_clk_sys0: <StarFive JH7110 SYS clock generator> mem 0x13020000-0x1302ffff on simplebus0
jh7110_aon0: <StarFive JH7110 AON clock generator> mem 0x17000000-0x1700ffff on simplebus0
jh7110_stg0: <StarFive JH7110 STG clock generator> mem 0x10230000-0x1023ffff on simplebus0
sbi0: <RISC-V Supervisor Binary Interface>
cpulist0: <Open Firmware CPU Group> on ofwbus0
cpu0: <Open Firmware CPU> on cpulist0
intc0: <RISC-V Local Interrupt Controller> on ofwbus0
sbi_ipi0: <RISC-V SBI Inter-Processor Interrupts> on sbi0
plic0: <RISC-V PLIC> mem 0xc000000-0xfffffff irq 14,15,16,17,18,19,20,21,22 on simplebus0
gpio0: <StarFive JH7110 GPIO controller> mem 0x13040000-0x1304ffff irq 44 on simplebus0
gpiobus0: <OFW GPIO bus> on gpio0
timer0: <RISC-V Timer>
Timecounter "RISC-V Timecounter" frequency 4000000 Hz quality 1000
Event timer "RISC-V Eventtimer" frequency 4000000 Hz quality 1000
rcons0: <RISC-V console>
cpufreq_dt0: <Generic cpufreq driver> on cpu0
cpufreq0: <CPU frequency control> on cpu0
cpufreq_dt1: <Generic cpufreq driver> on cpu1
cpufreq1: <CPU frequency control> on cpu1
cpufreq_dt2: <Generic cpufreq driver> on cpu2
cpufreq2: <CPU frequency control> on cpu2
cpufreq_dt3: <Generic cpufreq driver> on cpu3
cpufreq3: <CPU frequency control> on cpu3
uart0: <16550 or compatible> mem 0x10000000-0x1000ffff irq 23 on simplebus0
uart0: console (115384,n,8,1)
gpioc0: <GPIO controller> at pins 0-63 on gpiobus0
starfive_dwmmc0: <Synopsys DesignWare Mobile Storage Host Controller (StarFive)> mem 0x16010000-0x1601ffff irq 48 on simplebus0
starfive_dwmmc0: Hardware version ID is 290a
mmc0: <MMC/SD bus> on starfive_dwmmc0
starfive_dwmmc1: <Synopsys DesignWare Mobile Storage Host Controller (StarFive)> mem 0x16020000-0x1602ffff irq 49 on simplebus0
starfive_dwmmc1: Hardware version ID is 290a
mmc1: <MMC/SD bus> on starfive_dwmmc1
eqos0: <DesignWare EQOS Gigabit Ethernet for JH7110> mem 0x16030000-0x1603ffff irq 50,51,52 on simplebus0
miibus0: <MII bus> on eqos0
mcommphy0: <Motorcomm YT8531 10/100/1000 PHY> PHY 0 on miibus0
mcommphy0:  none, 10baseT, 10baseT-FDX, 100baseTX, 100baseTX-FDX, 1000baseT-FDX, 1000baseT-FDX-master, auto
mcommphy1: <Motorcomm YT8531 10/100/1000 PHY> PHY 1 on miibus0
mcommphy1:  none, 10baseT, 10baseT-FDX, 100baseTX, 100baseTX-FDX, 1000baseT-FDX, 1000baseT-FDX-master, auto
eqos0: Ethernet address: f2:00:01:57:01:f1
eqos1: <DesignWare EQOS Gigabit Ethernet for JH7110> mem 0x16040000-0x1604ffff irq 53,54,55 on simplebus0
miibus1: <MII bus> on eqos1
mcommphy2: <Motorcomm YT8531 10/100/1000 PHY> PHY 0 on miibus1
mcommphy2:  none, 10baseT, 10baseT-FDX, 100baseTX, 100baseTX-FDX, 1000baseT-FDX, 1000baseT-FDX-master, auto
mcommphy3: <Motorcomm YT8531 10/100/1000 PHY> PHY 1 on miibus1
mcommphy3:  none, 10baseT, 10baseT-FDX, 100baseTX, 100baseTX-FDX, 1000baseT-FDX, 1000baseT-FDX-master, auto
eqos1: Ethernet address: f2:00:33:a0:13:07
pcib0: <Starfive JH7110 PCIe controller> mem 0x940000000-0x940ffffff,0x2b000000-0x2b0fffff irq 63 on simplebus0
pcib0: Link up
pci0: <PCI bus> on pcib0
pcib0: route pin 1 for device 0.0 to 67
pcib1: <PCI-PCI bridge> irq 67 at device 0.0 on pci0
pci1: <PCI bus> on pcib1
pcib0: route pin 1 for device 0.0 to 68
xhci0: <XHCI (generic) USB 3.0 controller> irq 68 at device 0.0 on pci1
xhci0: 32 bytes context size, 64-bit DMA
xhci0: xECP capabilities <LEGACY,PROTO,PROTO,DEBUG>
usbus0 on xhci0
pcib2: <Starfive JH7110 PCIe controller> mem 0x9c0000000-0x9c0ffffff,0x2c000000-0x2c0fffff irq 64 on simplebus0
pcib2: Cannot establish data link
Timecounters tick every 1.000 msec
usbus0: 5.0Gbps Super Speed USB v3.0
mmc0: No compatible cards found on bus
ugen0.1: <(0x1106) XHCI root HUB> at usbus0
uhub0 on usbus0
uhub0: <(0x1106) XHCI root HUB, class 9/0, rev 3.00/1.00, addr 1> on usbus0
mmcsd0: 128GB <SDHC SR128 8.6 SN 40CC4673 MFG 12/2024 by 3 SD> at mmc1 50.0MHz/4bit/1016-block
sbi_ipi0: using for IPIs
Release APs
Trying to mount root from ufs:/dev/ufs/rootfs [rw]...
WARNING: / was not properly dismounted
Warning: no time-of-day clock registered, system time will not be set accurately
uhub0: 5 ports with 4 removable, self powered
ugen0.2: <vendor 0x2109 USB2.0 Hub> at usbus0
uhub1 on uhub0
uhub1: <vendor 0x2109 USB2.0 Hub, class 9/0, rev 2.10/4.20, addr 1> on usbus0
Waiting 30s for the root mount holders: usbus0uhub1: 4 ports with 4 removable, self powered
Setting hostuuid: 31374656-3031-3142-2d32-3331302d4430.
Setting hostid: 0x4c42e45b.
Starting file system checks:
/dev/ufs/rootfs: 28193 files, 652595 used, 27528436 free (124 frags, 3441039 blocks, 0.0% fragmentation)
Mounting local filesystems:.
Setting up harvesting: RANDOMDEV,[CALLOUT],[UMA],[FS_ATIME],SWI,INTERRUPT,NET_NG,[NET_ETHER],NET_TUN,MOUSE,KEYBOARD,ATTACH,CACHED
Feeding entropy: .
ELF ldconfig path: /lib /usr/lib /usr/lib/compat
Setting hostname: generic.
lo0: link state changed to UP
eqos0: link state changed to DOWN
eqos1: link state changed to DOWN
Starting Network: lo0 eqos0 eqos1.
lo0: flags=1008049<UP,LOOPBACK,RUNNING,MULTICAST,LOWER_UP> metric 0 mtu 16384
	options=680003<RXCSUM,TXCSUM,LINKSTATE,RXCSUM_IPV6,TXCSUM_IPV6>
	inet 127.0.0.1 netmask 0xff000000
	inet6 ::1 prefixlen 128
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x3
	groups: lo
	nd6 options=23<PERFORMNUD,ACCEPT_RTADV,AUTO_LINKLOCAL>
eqos0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500
	options=80008<VLAN_MTU,LINKSTATE>
	ether f2:00:01:57:01:f1
	inet6 fe80::f000:1ff:fe57:1f1%eqos0 prefixlen 64 scopeid 0x1
	media: Ethernet autoselect (none)
	status: no carrier
	nd6 options=23<PERFORMNUD,ACCEPT_RTADV,AUTO_LINKLOCAL>
eqos1: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500
	options=80008<VLAN_MTU,LINKSTATE>
	ether f2:00:33:a0:13:07
	inet6 fe80::f000:33ff:fea0:1307%eqos1 prefixlen 64 scopeid 0x2
	media: Ethernet autoselect (none)
	status: no carrier
	nd6 options=23<PERFORMNUD,ACCEPT_RTADV,AUTO_LINKLOCAL>
Starting devd.
Waiting 30s for the default route interface: .....(no carrier)
route: message indicates error: File exists
add host 127.0.0.1: gateway lo0 fib 0: route already in table
route: message indicates error: File exists
add host ::1: gateway lo0 fib 0: route already in table
add net fe80::: gateway ::1
add net ff02::: gateway ::1
add net ::ffff:0.0.0.0: gateway ::1
add net ::0.0.0.0: gateway ::1
Updating motd:.
Creating and/or trimming log files.
Clearing /tmp (X related).
Updating /var/run/os-release done.
Starting syslogd.
No core dumps found.
Mounting late filesystems:.
Performing sanity check on sshd configuration.
Starting sshd.
Starting cron.
Starting background file system checks in 60 seconds.

Fri May  1 09:31
FreeBSD/riscv (generic) (ttyu0)

login: root
Password:
May  1 09:31:16 generic login[2646]: ROOT LOGIN (root) ON ttyu0
Last login: Fri May  1 09:25:58 on ttyu0
FreeBSD 15.1-BETA1 (GENERIC) releng/15.1-n283455-58777180c5b0

Welcome to FreeBSD!
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
