---
sys: NixOS
sys_ver: null
sys_var: null

status: basic
last_update: 2024-12-22
---

# NixOS VisionFive 2 Test Report

## Test Environment

### Operating System Information

- System version: 25.05.20241121
- Source code link: https://github.com/NickCao/nixos-riscv
- Reference Installation Document: https://github.com/NickCao/nixos-riscv/README.md

### Hardware Information

- StarFive VisionFive 2
- A USB-A Power Adapter
- A USB-A to C Cable
- A microSD Card
- A microSD Card Reader
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three DuPont Wires

## Installation Steps

### Compiling Image

Run `nix build ".#hydraJobs.visionfive2"` if you happen to be using NixOS on your host.

It is not recommended to install and use the `nix` package manager on other distributions. Try using e.g. the official Docker image instead:
```shell
docker run -ti -v $(pwd):/work ghcr.io/nixos/nix
```

Inside the Docker container:

```shell
echo "max-jobs = auto" >> /etc/nix/nix.conf # Enable multi-threaded compilation
echo "substituters = https://mirrors.tuna.tsinghua.edu.cn/nix-channels/store https://cache.nixos.org/" >> /etc/nix/nix.conf # Switch to another mirror
cd /work
nix build ".#hydraJobs.visionfive2" --extra-experimental-features nix-command --extra-experimental-features flakes
```

The resulting image will reside at `./result/sd-image/`, with a filename similar to `nixos-sd-image-25.05.20241121.0039986-riscv64-linux-starfive-visionfive2.img.zst`。

### Flashing Image to microSD Card

Use `dd` to flash the image to the microSD card.

### Logging into the System

Logging into the system via the serial port.

No password are set and will automatically login by default.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
<<< Welcome to NixOS 25.05.20241121.0039986 (riscv64) - ttyS0 >>>
The "nixos" and "root" accounts have empty passwords.

To log in over ssh you must set a password for either "nixos" or "root"
with `passwd` (prefix with `sudo` for "root"), or add your public key to
/home/nixos/.ssh/authorized_keys or /root/.ssh/authorized_keys.

If you need a wireless connection, type
`sudo systemctl start wpa_supplicant` and configure a
network using `wpa_cli`. See the NixOS manual for details.


Run 'nixos-help' for the NixOS manual.

nixos login: nixos (automatic login)


[nixos@nixos:~]$ uname -a
Linux nixos 6.12.0 #1-NixOS SMP Sun Nov 17 22:15:08 UTC 2024 riscv64 GNU/Linux

[nixos@nixos:~]$ cat /etc/os-release 
ANSI_COLOR="1;34"
BUG_REPORT_URL="https://github.com/NixOS/nixpkgs/issues"
BUILD_ID="25.05.20241121.0039986"
CPE_NAME="cpe:/o:nixos:nixos:25.05"
DEFAULT_HOSTNAME=nixos
DOCUMENTATION_URL="https://nixos.org/learn.html"
HOME_URL="https://nixos.org/"
ID=nixos
ID_LIKE=""
IMAGE_ID=""
IMAGE_VERSION=""
LOGO="nix-snowflake"
NAME=NixOS
PRETTY_NAME="NixOS 25.05 (Warbler)"
SUPPORT_END="2025-06-30"
SUPPORT_URL="https://nixos.org/community.html"
VARIANT=""
VARIANT_ID=installer
VENDOR_NAME=NixOS
VENDOR_URL="https://nixos.org/"
VERSION="25.05 (Warbler)"
VERSION_CODENAME=warbler
VERSION_ID="25.05"

[nixos@nixos:~]$ cat /proc/cpuinfo
processor       : 0
hart            : 2
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

[nixos@nixos:~]$
```

USB driver also works, despite what is written in the original README:

```log
[nixos@nixos:~]$ [  681.045954] usb 2-4: new SuperSpeed USB device number 2 using xhci_hcd
[  681.068527] usb-storage 2-4:1.0: USB Mass Storage device detected
[  681.079456] scsi host0: usb-storage 2-4:1.0
[  682.110860] scsi 0:0:0:0: Direct-Access      USB      SanDisk 3.2Gen1 1.00 PQ: 0 ANSI: 6
[  682.124874] sd 0:0:0:0: [sda] 60088320 512-byte logical blocks: (30.8 GB/28.7 GiB)
[  682.133356] sd 0:0:0:0: [sda] Write Protect is off
[  682.138907] sd 0:0:0:0: [sda] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
[  682.182460]  sda: sda1
[  682.185238] sd 0:0:0:0: [sda] Attached SCSI removable disk
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
