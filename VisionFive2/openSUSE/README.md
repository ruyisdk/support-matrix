---
sys: opensuse
sys_ver: null
sys_var: null

status: basic
last_update: 2024-10-25
---

# openSUSE Tumbleweed VisionFive 2 Test Report

## Test Environment

### Operating System Information

- System Version: 20241024
- Download Link: https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/StarFive:/VisionFive2/images/
- Reference Installation Document: https://en.opensuse.org/HCL:VisionFive2

### Hardware Information

- StarFive VisionFive 2
- A USB Power Adapter
- A USB-A to C or C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont Wires

## Installation Steps

### Decompress and Flash the Image to the microSD Card

Assuming `/dev/sdX` is the storage card.

```bash
xzcat openSUSE-Tumbleweed-RISC-V-JeOS-starfivevisionfive2.riscv64-2024.10.14-Build1.20.raw.xz | sudo dd of=/dev/sdX iflag=fullblock status=progress bs=4M
```

### Boot Mode Selection

StarFive VisionFive 2 provides multiple boot modes, configurable through onboard dip switches before powering on; these are marked on the board itself.

To boot the openSUSE image, select the microSD card boot mode (i.e., `RGPIO_0 = 1`, `RGPIO_1 = 0`).

> Note: In this mode, there is a small chance of boot failure. If you encounter boot failure, you might see output similar to the following on the serial port:
>
>```log
>dwmci_s: Response Timeout.                                                                                            
>dwmci_s: Response Timeout.                                                                                            
>BOOT fail,Error is 0xffffffff
>```
>
> You can try repowering the board or pressing the button near the USB Type-C power interface. This usually resolves the issue.

### Logging into the System

Login to the system via the serial port.

Username: `root`
Default Password: `linux`

## Expected Results

The system should boot normally and allow login via the serial port.

## Actual Results

The system booted successfully and login via the serial port was successful.

### Boot Log

```log
Welcome to openSUSE Tumbleweed 20241024 - Kernel 6.12.0-rc4-103-default (ttyS0).

end0: 192.168.31.87 fe80::4fd8:4211:1862:b059
end1:  


localhost login: root
Password: 
Have a lot of fun...
localhost:~ # uname -a
Linux localhost.localdomain 6.12.0-rc4-103-default #1 SMP PREEMPT_DYNAMIC Wed Oct 23 21:57:24 UTC 2024 (a082c88) riscv64 riscv64 riscv64 GNU/Linux
localhost:~ # cat /etc/os-release 
NAME="openSUSE Tumbleweed"
# VERSION="20241024"
ID="opensuse-tumbleweed"
ID_LIKE="opensuse suse"
VERSION_ID="20241024"
PRETTY_NAME="openSUSE Tumbleweed"
ANSI_COLOR="0;32"
# CPE 2.3 format, boo#1217921
CPE_NAME="cpe:2.3:o:opensuse:tumbleweed:20241024:*:*:*:*:*:*:*"
#CPE 2.2 format
#CPE_NAME="cpe:/o:opensuse:tumbleweed:20241024"
BUG_REPORT_URL="https://bugzilla.opensuse.org"
SUPPORT_URL="https://bugs.opensuse.org"
HOME_URL="https://www.opensuse.org"
DOCUMENTATION_URL="https://en.opensuse.org/Portal:Tumbleweed"
LOGO="distributor-logo-Tumbleweed"
localhost:~ # 
```

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/z3xt9HGtT5iVtI7tbtQNi9rHf.svg)](https://asciinema.org/a/z3xt9HGtT5iVtI7tbtQNi9rHf)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
