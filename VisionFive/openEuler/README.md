# openEuler RISC-V 23.09 VisionFive Test Report

## Test Environment

### Operating System Information

- System Version: openEuler 23.09 RISC-V preview
- Download Link: [https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Visionfive/](https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Visionfive/)
- Reference Installation Document: [https://gitee.com/openeuler/RISC-V/tree/master/release/openEuler-23.03/Installation_Book/Visionfive](https://gitee.com/openeuler/RISC-V/tree/master/release/openEuler-23.03/Installation_Book/Visionfive)

### Hardware Information

- StarFive VisionFive
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flash the Image to microSD Card Using `ruyi` CLI

Install the [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the prompts.

### Logging into the System

Log into the system via the serial port.

Default Username: `openeuler`
Default Password: `openEuler12#$`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully, and login via the onboard serial port was successful.

### Boot Log

Screen recording (From flashing image to login):

[![asciicast](https://asciinema.org/a/lkduJVcErVoqb3ewZuzjl4TVi.svg)](https://asciinema.org/a/lkduJVcErVoqb3ewZuzjl4TVi)

```log
Welcome to 6.1.0-0.rc4.8.oe2309.riscv64

System information as of time:  Mon Sep 18 08:01:36 AM CST 2023

System load:    2.62
Processes:      120
Memory used:    2.4%
Swap used:      0.0%
Usage On:       4%
Users online:   1
To run a command as administrator(user "root"),use "sudo <command>".
[openeuler@openeuler-riscv64 ~]$ uname -a
Linux openeuler-riscv64 6.1.0-0.rc4.8.oe2309.riscv64 #1 SMP Fri Oct 20 08:23:28 UTC 2023 riscv64 riscv64 riscv64 GNU/Linux
[openeuler@openeuler-riscv64 ~]$ cat /etc/os-release 
NAME="openEuler"
VERSION="23.09"
ID="openEuler"
VERSION_ID="23.09"
PRETTY_NAME="openEuler 23.09"
ANSI_COLOR="0;31"

[openeuler@openeuler-riscv64 ~]$ 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

