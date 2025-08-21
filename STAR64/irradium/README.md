---
sys: irradium
sys_ver: "3.8"
sys_var: null

status: basic
last_update: 2025-07-13
---

# irradium Star64 Test Report

## Test Environment

### Operating System Information

- Download Link: https://dl.irradium.org/irradium/images/star64/irradium-3.8-riscv64-xfce-star64-6.12.33-build-20250613.img.zst
- Reference Installation Document: https://dl.irradium.org/irradium/images/star64/

### Hardware Information

- Pine64 Star64
- A microSD card
- DC 12V5A Barrel power adapter
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires

## Installation Steps

### Decompress and Flash the Image to the microSD Card

Assume `/dev/sdc` is the storage card.

```bash
zstd -d https://dl.irradium.org/irradium/images/star64/irradium-3.8-riscv64-xfce-star64-6.12.33-build-20250613.img.zst
sudo dd if=https://dl.irradium.org/irradium/images/star64/irradium-3.8-riscv64-xfce-star64-6.12.33-build-20250613.img of=/dev/sdX bs=1m status=progress
```

### Logging into the System

Set the boot option to microSD (GPIO_0 = 1, GPIO_1 = 0; See [Boot Source Selection](https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/pine64-star64/#boot-source-selection) for details).

Username: `root`

Password: (set at first login)

## Expected Results

The system boots up normally, and login via the serial port is successful.

## Actual Results

The system boots up normally, and login via the serial port is successful.

### Boot Log

```log
U-Boot SPL 2025.04-jh7110 (Jun 13 2025 - 03:16:36 +0000)
DDR version: dc2e84f0.
Trying to boot from MMC2

OpenSBI v1.6
   ____                    _____ ____ _____
  / __ \                  / ____|  _ \_   _|
 | |  | |_ __   ___ _ __ | (___ | |_) || |
 | |  | | '_ \ / _ \ '_ \ \___ \|  _ < | |
 | |__| | |_) |  __/ | | |____) | |_) || |_
  \____/| .__/ \___|_| |_|_____/|____/_____|
        | |
        |_|

Platform Name               : Pine64 Star64
Platform Features           : medeleg
Platform HART Count         : 5
Platform IPI Device         : aclint-mswi
Platform Timer Device       : aclint-mtimer @ 4000000Hz
Platform Console Device     : uart8250
Platform HSM Device         : ---
Platform PMU Device         : ---
Platform Reboot Device      : pm-reset
Platform Shutdown Device    : pm-reset
Platform Suspend Device     : ---
Platform CPPC Device        : ---
Firmware Base               : 0x40000000
Firmware Size               : 373 KB
Firmware RW Offset          : 0x40000
Firmware RW Size            : 117 KB
Firmware Heap Offset        : 0x50000
Firmware Heap Size          : 53 KB (total), 3 KB (reserved), 13 KB (used), 36 KB (free)
Firmware Scratch Size       : 4096 B (total), 440 B (used), 3656 B (free)
Runtime SBI Version         : 2.0
Standard SBI Extensions     : time,rfnc,ipi,base,hsm,srst,pmu,dbcn,legacy
Experimental SBI Extensions : fwft,dbtr,sse

Domain0 Name                : root
Domain0 Boot HART           : 4
Domain0 HARTs               : 0*,1*,2*,3*,4*
Domain0 Region00            : 0x0000000010000000-0x0000000010000fff M: (I,R,W) S/U: (R,W)
Domain0 Region01            : 0x0000000002000000-0x000000000200ffff M: (I,R,W) S/U: ()
Domain0 Region02            : 0x0000000040040000-0x000000004005ffff M: (R,W) S/U: ()
Domain0 Region03            : 0x0000000040000000-0x000000004003ffff M: (R,X) S/U: ()
Domain0 Region04            : 0x000000000c000000-0x000000000fffffff M: (I,R,W) S/U: (R,W)
Domain0 Region05            : 0x0000000000000000-0xffffffffffffffff M: () S/U: (R,W,X)
Domain0 Next Address        : 0x0000000040200000
Domain0 Next Arg1           : 0x0000000040400000
Domain0 Next Mode           : S-mode
Domain0 SysReset            : yes
Domain0 SysSuspend          : yes

Boot HART ID                : 4
Boot HART Domain            : root
Boot HART Priv Version      : v1.11
Boot HART Base ISA          : rv64imafdcbx
Boot HART ISA Extensions    : zihpm,sdtrig
Boot HART PMP Count         : 8
Boot HART PMP Granularity   : 12 bits
Boot HART PMP Address Bits  : 34
Boot HART MHPM Info         : 2 (0x00000018)
Boot HART Debug Triggers    : 8 triggers
Boot HART MIDELEG           : 0x0000000000000222
Boot HART MEDELEG           : 0x000000000000b109


U-Boot 2025.04-jh7110 (Jun 13 2025 - 03:16:36 +0000)

CPU:   sifive,u74-mc
Model: Pine64 Star64
DRAM:  8 GiB
Core:  153 devices, 26 uclasses, devicetree: board
WDT:   Not starting watchdog@13070000
MMC:   mmc@16010000: 0, mmc@16020000: 1
Loading Environment from SPIFlash... SF: Detected gd25lq128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB
OK
StarFive EEPROM format v2

--------EEPROM INFO--------
Vendor : PINE64
Product full SN: STAR64V1-2310-D008E000-00000005
data version: 0x2
PCB revision: 0xc1
BOM revision: A
Ethernet MAC0 address: 6c:cf:39:00:75:61
Ethernet MAC1 address: 6c:cf:39:00:75:62
--------EEPROM INFO--------

starfive_7110_pcie pcie@9c0000000: Starfive PCIe bus probed.
In:    serial@10000000
Out:   serial@10000000
Err:   serial@10000000
Net:   eth0: ethernet@16030000, eth1: ethernet@16040000
starting USB...
No USB controllers found
Working FDT set to ff71fa20
Hit any key to stop autoboot:  0
Card did not respond to voltage select! : -110
** File not found ubootefi.var **
Failed to load EFI variables
** Unable to write file ubootefi.var **
Failed to persist EFI variables
** Unable to write file ubootefi.var **
Failed to persist EFI variables
** Unable to write file ubootefi.var **
Failed to persist EFI variables
** Booting bootflow '<NULL>' with efi_mgr
Loading Boot0000 'mmc 1' failed
EFI boot manager: Cannot load any image
Boot failed (err=-14)
Card did not respond to voltage select! : -110
** File not found /boot.bmp **
** Booting bootflow 'mmc@16020000.bootdev.part_3' with script
Boot script loaded from mmc 1:3
141 bytes read in 2 ms (68.4 KiB/s)
41319 bytes read in 8 ms (4.9 MiB/s)
28450816 bytes read in 877 ms (30.9 MiB/s)
Working FDT set to 46000000
Failed to load '/dtb/starfive/overlay/starfive-fixup.scr'
7890780 bytes read in 361 ms (20.8 MiB/s)
## Loading init Ramdisk from Legacy Image at 46100000 ...
   Image Name:   uInitrd
   Image Type:   RISC-V Linux RAMDisk Image (gzip compressed)
   Data Size:    7890716 Bytes = 7.5 MiB
   Load Address: 00000000
   Entry Point:  00000000
   Verifying Checksum ... OK
## Flattened Device Tree blob at 46000000
   Booting using the fdt blob at 0x46000000
Working FDT set to 46000000
   Loading Ramdisk to fdf5f000, end fe6e571c ... OK
   Loading Device Tree to 00000000fdeec000, end 00000000fdf5efff ... OK
Working FDT set to fdeec000

Starting kernel ...

�[    0.703376] Error: Driver 'imx219' is already registered, aborting...
[    0.706249] cpufreq: Unable to obtain ARMCLK: -2
[    0.816484] CCACHE: DataError @ 0x00000000.08024DE0
[    0.816529] CCACHE: DataFail @ 0x00000000.08024DFC
[    0.819359] debugfs: Directory '16008000.dma-controller' with parent 'dmaengine' already present!
[    2.770281] udevd[138]: failed to execute '/usr/sbin/nfsrahead' '/usr/sbin/nfsrahead 179:0': No such file or directory
[    7.710605] udevd[175]: specified group 'netdev' unknown


irradium  (star64) (ttyS0)

star64 login: root
You are required to change your password immediately (administrator enforced).
New password:
Retype new password:
 _                   _  _
|_| ___  ___  ___  _| ||_| _ _  _____
| ||  _||  _|| .'|| . || || | ||     |
|_||_|  |_|  |__,||___||_||___||_|_|_|
      _              ___  ___
 ___ | |_  ___  ___ |  _|| | |
|_ -||  _|| .'||  _|| . ||_  |
|___||_|  |__,||_|  |___|  |_|

# uname -a
Linux star64 6.12.33 #1 SMP PREEMPT Thu Jun 12 18:14:58 UTC 2025 riscv64 GNU/Linux
# cat /etc/os-release
NAME=irradium
VERSION_ID="3.8"
ID=irradium
PRETTY_NAME="irradium"
HOME_URL="https://irradium.org"
DOCUMENTATION_URL="https://irradium.org/Main/Handbook3-8"
BUG_REPORT_URL="https://irradium.org/bugs"
# cat /proc/cpuinfo
processor       : 0
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 2
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 3
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

#

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.