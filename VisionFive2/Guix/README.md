---
sys: guix
sys_ver: null
sys_var: null

status: basic
last_update: 2025-04-11
---

# Guix System VisionFive 2 Test Report

## Test Environment

### Operating System Information

- Source code link: https://git.savannah.gnu.org/cgit/guix.git/tree/gnu/system/images/visionfive2.scm
- Download Link: https://ci.guix.gnu.org/search/latest?query=spec:images+status:success+system:x86_64-linux+visionfive2-barebones-raw-image

### Hardware Information

- StarFive VisionFive 2
- A USB-A Power Adapter
- A USB-A to C Cable
- A microSD Card
- A microSD Card Reader
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three DuPont Wires

## Installation Steps

### Flashing Image to microSD Card

Use `dd` to flash the image to the microSD card.

```bash
sudo dd if=<hash>-visionfive2-barebones-raw-image of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Log into the system via the serial port.

Username: root
No password.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted up successfully, and login via the serial port was successful.

### Boot Log

```log
[   36.862330] shepherd[1]: GNU Shepherd 1.0.3 (Guile 3.0.9, riscv64-unknown-linux-gnu)
[   36.870795] shepherd[1]: bit-count is deprecated.  Use bitvector-count, or a loop over array-ref if array support is needed.
[   36.885641] shepherd[1]: scm_bitvector_length is deprecated.  Use scm_c_bitvector_length instead.
[   36.895159] shepherd[1]: Starting service root...
[   36.903053] shepherd[1]: Service root started.
[   36.908134] shepherd[1]: Service root running with value #<<process> id: 1 command: #f>.
[   36.918309] shepherd[1]: Service root has been started.
[   36.935595] shepherd[1]: starting services...
[   36.940596] shepherd[1]: Configuration successfully loaded from '/gnu/store/97s9ywwn93zp2q0i5r892h4aqrs8zp95-shepherd.conf'.
[   37.051971] shepherd[1]: Starting service user-file-systems...
[   37.058551] shepherd[1]: Starting service root-file-system...
[   37.070429] shepherd[1]: Starting service host-name...
[   37.076385] shepherd[1]: Starting service pam...
[   37.086157] shepherd[1]: Starting service sysctl...
[   37.091864] shepherd[1]: Starting service log-rotation...
[   37.102046] shepherd[1]: Starting service loopback...
[   37.107930] shepherd[1]: Service user-file-systems started.
[   37.116275] shepherd[1]: Service root-file-system started.
[   37.122529] shepherd[1]: Service host-name started.
[   37.130024] shepherd[1]: Service pam started.
[   37.135096] shepherd[1]: Service log-rotation started.
[   37.143951] shepherd[1]: Service user-file-systems running with value #t.
[   37.151457] shepherd[1]: Service user-file-systems has been started.
[   37.161530] shepherd[1]: Service root-file-system running with value #t.
[   37.169019] shepherd[1]: Service root-file-system has been started.
[   37.179039] shepherd[1]: Service host-name running with value "visionfive2".
[   37.186839] shepherd[1]: Service host-name has been started.
[   37.195658] shepherd[1]: Service pam running with value #t.
[   37.202150] shepherd[1]: Service pam has been started.
[   37.218602] shepherd[1]: Service log-rotation running with value #<timer #<<calendar-event> seconds: (0) minutes: (0) hours: (22) days-of-month: (1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31) months: (1 2 3 4 5 6 7 8 9 10 11 12) days-of-week: (0)> #<procedure rotation ()> 3f967a48c0>.
[   37.248184] shepherd[1]: Service log-rotation has been started.
[   37.303455] shepherd[1]: Service sysctl has been started.
[   37.309964] shepherd[1]: Service sysctl started.
[   37.424748] udevd[120]: starting version 3.2.14
[   37.480184] udevd[120]: specified group 'sgx' unknown
[   37.545630] udevd[120]: starting eudev-3.2.14
[   37.818554] udevd[120]: no sender credentials received, message ignored
[   37.830806] shepherd[1]: [sysctl] fs.protected_hardlinks = 1
[   37.837502] shepherd[1]: Service sysctl running with value #t.
[   37.850167] shepherd[1]: [sysctl] fs.protected_symlinks = 1
[   37.856627] shepherd[1]: Starting service udev...
[   37.866968] shepherd[1]: could not create '/dev/mapper/control': File exists
[   37.875003] shepherd[1]: waiting for udevd...
[   37.883727] shepherd[1]: Registering new logger for udev.
[   37.890005] shepherd[1]: Service loopback has been started.
[   37.900022] shepherd[1]: [k8s4gfkih3f0icjdqzwk3jaqggp33jf6-set-up-network] Waiting for network device 'lo'...
[   37.910961] shepherd[1]: Service loopback started.
[   37.918228] shepherd[1]: Service loopback running with value #t.
[   38.338893] starfive-dphy-rx 19820000.phy: supply mipi_0p9 not found, using dummy regulator
[   40.496841] starfive-dwmac 16040000.ethernet eth0: Register MEM_TYPE_PAGE_POOL RxQ-0
[   40.506930] starfive-dwmac 16040000.ethernet eth0: PHY [stmmac-1:00] driver [Generic PHY] (irq=POLL)
[   41.521098] starfive-dwmac 16040000.ethernet: Failed to reset the dma
[   41.527605] starfive-dwmac 16040000.ethernet eth0: stmmac_hw_setup: DMA engine initialization failed
[   41.536803] starfive-dwmac 16040000.ethernet eth0: __stmmac_open: Hw setup failed
[   41.547218] starfive-dwmac 16030000.ethernet eth1: Register MEM_TYPE_PAGE_POOL RxQ-0
[   41.557443] starfive-dwmac 16030000.ethernet eth1: PHY [stmmac-0:00] driver [Generic PHY] (irq=POLL)
[   42.575157] starfive-dwmac 16030000.ethernet: Failed to reset the dma
[   42.581665] starfive-dwmac 16030000.ethernet eth1: stmmac_hw_setup: DMA engine initialization failed
[   42.590843] starfive-dwmac 16030000.ethernet eth1: __stmmac_open: Hw setup failed
[   42.826381] starfive-dwmac 16030000.ethernet eth1: Register MEM_TYPE_PAGE_POOL RxQ-0
[   42.837799] starfive-dwmac 16030000.ethernet eth1: PHY [stmmac-0:00] driver [Generic PHY] (irq=POLL)
[   42.939653] dwmac4: Master AXI performs fixed burst length
[   42.945234] starfive-dwmac 16030000.ethernet eth1: No Safety Features support found
[   42.952961] starfive-dwmac 16030000.ethernet eth1: IEEE 1588-2008 Advanced Timestamp supported
[   42.963133] starfive-dwmac 16030000.ethernet eth1: configuring for phy/rgmii-id link mode
[   42.974135] 8021q: adding VLAN 0 to HW filter on device eth1
[   42.979914] starfive-dwmac 16030000.ethernet eth1: Adding VLAN ID 0 is not supported
[   43.006705] starfive-dwmac 16040000.ethernet eth0: Register MEM_TYPE_PAGE_POOL RxQ-0
[   43.016906] starfive-dwmac 16040000.ethernet eth0: PHY [stmmac-1:00] driver [Generic PHY] (irq=POLL)


This is the GNU system.  Welcome.
visionfive2 login: [   44.029833] starfive-dwmac 16040000.ethernet: Failed to reset the dma
[   44.036347] starfive-dwmac 16040000.ethernet eth0: stmmac_hw_setup: DMA engine initialization failed
[   44.045532] starfive-dwmac 16040000.ethernet eth0: __stmmac_open: Hw setup failed

visionfive2 login: root
This is the GNU operating system, welcome!

root@visionfive2 ~# uname -a
Linux visionfive2 6.13.9-gnu #1 SMP 1 riscv64 GNU/Linux
root@visionfive2 ~# cat /etc/os-release
NAME="Guix System"
ID=guix
PRETTY_NAME="Guix System"
LOGO=guix-icon
HOME_URL="https://guix.gnu.org"
DOCUMENTATION_URL="https://guix.gnu.org/en/manual"
SUPPORT_URL="https://guix.gnu.org/en/help"
BUG_REPORT_URL="https://lists.gnu.org/mailman/listinfo/bug-guix"
root@visionfive2 ~# lscpu
Architecture:             riscv64
  Byte Order:             Little Endian
CPU(s):                   4
  On-line CPU(s) list:    0-3
NUMA:
  NUMA node(s):           1
  NUMA node0 CPU(s):      0-3
Vulnerabilities:
  Gather data sampling:   Not affected
  Itlb multihit:          Not affected
  L1tf:                   Not affected
  Mds:                    Not affected
  Meltdown:               Not affected
  Mmio stale data:        Not affected
  Reg file data sampling: Not affected
  Retbleed:               Not affected
  Spec rstack overflow:   Not affected
  Spec store bypass:      Not affected
  Spectre v1:             Not affected
  Spectre v2:             Not affected
  Srbds:                  Not affected
  Tsx async abort:        Not affected
root@visionfive2 ~# cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 1
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

root@visionfive2 ~#

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
