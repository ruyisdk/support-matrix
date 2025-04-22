---
sys: ubuntu
sys_ver: "25.04"
sys_var: null

status: CFT
last_update: 2025-04-18
---

# Ubuntu D1s NeZha Test Report

## Test Environment

### Operating System Information

- System Version: Ubuntu 25.04
- Download Link: https://cdimage.ubuntu.com/releases/25.04/release/ubuntu-25.04-preinstalled-server-riscv64+nezha.img.xz
- Reference Installation Document: https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/allwinner-nezha-d1/

### Hardware Information

- D1s NeZha
- A USB-A to C or C to C cable
- A microSD card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires

## Installation Steps

### Decompress and Flash the Image to the microSD Card

Assume `/dev/sdc` is the storage card.

```bash
xz -d ubuntu-25.04-preinstalled-server-riscv64+nezha.img.xz
sudo dd if=ubuntu-25.04-preinstalled-server-riscv64+nezha.img of=/dev/sdc bs=1m status=progress
```

### Logging into the System

Log into the system via the serial port.

Default username: `ubuntu`
Default password: `ubuntu`

Upon the first login, you will be prompted to change the default password.

## Expected Results

The system should boot normally and allow login via the serial port.

## Actual Results
<details>
<summary>result is outdated(24.04)</summary>
The system boots up normally, and login via the serial port is successful.

### Boot Log

Screen recording (from compilation to startup):
[![asciicast](https://asciinema.org/a/gPmHuofP650Kl9mTp8xLk1tod.svg)](https://asciinema.org/a/gPmHuofP650Kl9mTp8xLk1tod)

```log
ubuntu@ubuntu:~$ cat /proc/cpuinfo                                              processor       : 0                                                             hart            : 0                                                             isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm                        mmu             : sv39                                                          uarch           : thead,c906                                                    mvendorid       : 0x5b7                                                         marchid         : 0x0                                                           mimpid          : 0x0                                                           hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
</details>
