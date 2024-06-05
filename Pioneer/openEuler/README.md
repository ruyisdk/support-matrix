# openEuler RISC-V 23.09 Pioneer  Test Report

## Test Environment

### Operating System Information

- System Version: openEuler 23.09 RISC-V preview
- Download Link: [openEuler-23.09-V1-riscv64](https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/SG2042/)
- Installation Guide: [README.sg2042.txt](https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Unmatched/README.sg2042.txt)

### Hardware Information

- Milk-V Pioneer Box v1.3
- One microSD card (or NVMe SSD + NVMe SSD to USB hard drive enclosure)
- One USB Type-C cable (used to connect the onboard serial port)

## Installation Steps

### Flashing Image to Onboard eMMC using `ruyi` CLI

Install the [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the instructions.

### Logging into the System

Logging into the system via SSH.

Default username: `openeuler` or `root`
Default password: `openEuler12#$`

## Expected Results

The system starts up properly and can be accessed via SSH.

## Actual Results

The system starts up correctly and SSH login is successful.

### Boot Log

```log
System load:    1.61
Processes:      710
Memory used:    .6%
Swap used:      0.0%
Usage On:       11%
IP address:     10.0.0.12
Users online:   1
To run a command as administrator(user "root"),use "sudo <command>".
[openeuler@openeuler-riscv64 ~]$ uname -a
Linux openeuler-riscv64 6.1.61-4.oe2309.riscv64 #1 SMP Thu Dec 28 18:01:00 UTC 2023 riscv64 riscv64 riscv64 GNU/Linux
[openeuler@openeuler-riscv64 ~]$ cat /etc/os-release 
NAME="openEuler"
VERSION="23.09"
ID="openEuler"
VERSION_ID="23.09"
PRETTY_NAME="openEuler 23.09"
ANSI_COLOR="0;31"
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

