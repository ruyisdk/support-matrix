# openEuler RISC-V 24.03 LPi4A Test Report

## Test Environment

### System Information

- System Version: openEuler 24.03 RISC-V preview
- Download Link: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/testing/2403LTS-test/v1/lpi4a/
- Reference Installation Document: https://docs.openeuler.org/zh/docs/24.03_LTS/docs/Installation/RISC-V-LicheePi4A.html

### Hardware Information

- Lichee Pi 4A (8G RAM + 32G eMMC)
- USB-C Power Adapter / DC Power Supply
- A USB-UART Debugger

## Installation Steps

### Using the `ruyi` CLI to Flash Image to Onboard eMMC

Install [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, then run `ruyi device provision` and follow the prompts.

### Logging into the System

Logging into the system via serial console.

Default username: `openeuler` or `root`
Default password: `openEuler12#$`

## Expected Results

The system boots up successfully and allows login via the serial console.

If connected to a network, SSH login should be possible.

## Actual Results

The system boots up without issues, and both serial console and SSH login are successful.

### Boot Log

```log
Welcome to 6.6.0

System information as of time:  Thu Jan  1 08:00:22 AM CST 1970

System load:    2.07
Processes:      191
Memory used:    3.0%
Swap used:      0.0%
Usage On:       13%
Users online:   1

[openeuler@openeuler-riscv64 ~]$ cat /etc/os-release                                                                                                                         
NAME="openEuler"
VERSION="24.03 (LTS)"
ID="openEuler"
VERSION_ID="24.03"
PRETTY_NAME="openEuler 24.03 (LTS)"
ANSI_COLOR="0;31"
                                                                                                                                                                             
[openeuler@openeuler-riscv64 ~]$ uname -a
Linux openeuler-riscv64 6.6.0 #1 SMP Tue Apr  9 02:46:40 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux

[openeuler@openeuler-riscv64 ~]$ cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 1
hart            : 0
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 2
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 3
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0
```

Screen recording (from flashing image to logging into system):

[![asciicast](https://asciinema.org/a/oXGHqeiBmb0n5zIKHnbGnnRb2.svg)](https://asciinema.org/a/oXGHqeiBmb0n5zIKHnbGnnRb2)


## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
