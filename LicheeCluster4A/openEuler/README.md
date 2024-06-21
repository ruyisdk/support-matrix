# openEuler Lichee Cluster 4A Test Report

## Test Environment

### System Information

- System Version: openEuler 23.09 RISC-V preview
- Download Link: [Here](https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/lpi4a/)
- Reference Installation Documentation: [Here](https://revyos.github.io/)

### Hardware Information

- Lichee Cluster 4A 8G / 16G
- DC 12V Power Supply
- USB-A to A
    - or LPi4A baseboard
- Network and Ethernet Cable (ensure connection to BMC instead of switch)

## Installation Steps

*Using the example of flashing to the first board in the cluster*

### Connect the Corresponding SOM

Use an A to A cable to connect the SOM.

### Use the `ruyi` CLI to Flash the Image to the Onboard eMMC

Install the [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the prompts.

Choose the image accordingly for LPi4A.

### Logging into the System

Logging into the system via SOL (Serial Over LAN).

BMC default username: `root`

BMC default password: `0penBmc` **Note: it's `0` not `O`**

Connect using `ssh -p 2301 root@lichee-rv.local`

Default username: `openeuler` or `root`
Default password: `openEuler12#$`

### Common Issues

If USB is not working, it may be due to needing to patch the Linux device tree. [Download the patch here](https://dl.sipeed.com/fileList/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/src/linux/0001-arch-riscv-boot-dts-lpi4a-disable-i2c-io-expander-fo.patch)

If you prefer not to compile the dtb manually, you can extract the dtb (light-lpi4a.dtb) from the [precompiled image](https://dl.sipeed.com/shareURL/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/bin) and replace the corresponding file in the boot directory.

## Expected Results

The system boots up successfully and allows login via SOL (Serial Over LAN).

## Actual Results

The system boots up successfully and allows login via SOL (Serial Over LAN).

### Boot Log

Screen recording (from flashing the system to startup up):

[![asciicast](https://asciinema.org/a/PtLMh7Dm2RX3C4RPoTajplYbj.svg)](https://asciinema.org/a/PtLMh7Dm2RX3C4RPoTajplYbj)

```log
Authorized users only. All activities may be monitored and reported.
openeuler-riscv64 login: openeuler
Password: 
Last login: Tue Apr  2 10:35:06 on ttyS0

Authorized users only. All activities may be monitored and reported.


Welcome to 5.10.113

System information as of time:  Tue Apr  2 10:35:58 AM CST 2024

System load:    0.84
Processes:      144
Memory used:    2.2%
Swap used:      0.0%
Usage On:       13%
IP address:     192.168.36.10
Users online:   1
To run a command as administrator(user "root"),use "sudo <command>".
[openeuler@openeuler-riscv64 ~]$ uname -a
Linux openeuler-riscv64 5.10.113 #1 SMP PREEMPT Wed Nov 22 16:04:58 UTC 2023 riscv64 riscv64 riscv64 GNU/Linux
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
