---
sys: deepin
sys_ver: "23"
sys_var: null

status: basic
last_update: 2025-07-13
---

# Deepin Star64 Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/deepin-community/deepin-riscv-board/releases/download/v20221209/deepin-visionfive-2-20221208180420.img.zst.0
- Reference Installation Document: https://cdimage.deepin.com/RISC-V/VisionFive-v2-image/README.txt

### Hardware Information

- Pine64 Star64
- A microSD card
- DC 12V5A Barrel power adapter
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires

## Installation Steps

### Decompress and Flash Image to microSD Card

```bash
zstd -d https://github.com/deepin-community/deepin-riscv-board/releases/download/v20221209/deepin-visionfive-2-20221208180420.img.zst.0
sudo dd if=https://github.com/deepin-community/deepin-riscv-board/releases/download/v20221209/deepin-visionfive-2-20221208180420.img of=/dev/your/device bs=1M status=progress
```

### Boot Mode Selection

Pine64 Star64 offers multiple boot modes, configurable via onboard DIP switches before powering on. The board itself also has silk-screen labels. See [Boot Mode Selection]((https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/pine64-star64/#boot-source-selection)) for details.

To boot the image, select the SPI Flash mode (i.e., `GPIO_0 = 0`, `GPIO_1 = 0`). Note that this mode may require updating the firmware in the Flash beforehand. If the boot is unsuccessful, please refer to the official documentation for firmware upgrade details: [Updating SPL and U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)

If not updating the firmware, choose the microSD card boot mode (i.e., `GPIO_0 = 1`, `GPIO_1 = 0`).

> Note: There is a slight chance that the system may fail to boot in this mode. If boot failure occurs, the serial output might resemble the following:
>
>```log
>dwmci_s: Response Timeout.
>dwmci_s: Response Timeout.
>BOOT fail,Error is 0xffffffff
>```
>
> You can try repowering the development board or pressing the button near the USB Type-C power port. This usually resolves the boot issue.

### Logging into the System

Log into the system via the serial port.

Default username: `root`
Default password: `deepin`

## Expected Results

The system should boot up normally and allow login via the serial port.

## Actual Results

The system booted up successfully, and login via the serial port was successful.

### Boot Log

```log
Deepin GNU/Linux 23 deepin-riscv hvc0

deepin-riscv login: Deepin GNU/Linux 23 deepin-riscv ttyS0

deepin-riscv login: [   35.717007] mipi_0p9: disabling

deepin-riscv login: root
Password:
Password verification failed, 4 chances left

Login incorrect
deepin-riscv login: root
Password:
Verification successful
Linux deepin-riscv 5.15.0+ #1 SMP Thu Dec 8 17:49:21 UTC 2022 riscv64
Welcome to Deepin 23 GNU/Linux

    * Homepage:https://www.deepin.org/

    * Bugreport:https://bbs.deepin.org/


root@deepin-riscv:~# uname -a
Linux deepin-riscv 5.15.0+ #1 SMP Thu Dec 8 17:49:21 UTC 2022 riscv64 GNU/Linux
root@deepin-riscv:~# cat /etc/os-release
PRETTY_NAME="Deepin 23"
NAME="Deepin"
VERSION_ID="23"
VERSION="23"
ID=Deepin
HOME_URL="https://www.deepin.org/"
BUG_REPORT_URL="https://bbs.deepin.org"
VERSION_CODENAME=beige
root@deepin-riscv:~# cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc

processor       : 1
hart            : 2
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc

processor       : 2
hart            : 3
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc

processor       : 3
hart            : 4
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc

root@deepin-riscv:~#

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
