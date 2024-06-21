# Fedora 38 Milk-V Duo Test Report

## Test Environment

### Operating System Information

- System Version: Fedora 38
- Download Link: https://github.com/chainsx/fedora-riscv-builder/releases/download/20230719-1650/Fedora-38-Minimal-MilkV-Duo-riscv64.img.xz
- Reference Installation Document: https://github.com/chainsx/fedora-riscv-builder
- Issue/CFH: https://github.com/chainsx/fedora-riscv-builder/issues/6
    - (Image fails to boot)

> Note: This image is provided by community developers and is not an official image.

### Hardware Information

- Milk-V Duo 64M
- One USB power adapter
- One USB-A to C or USB-C to C cable
- One microSD card
- One USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three DuPont wires
- The Milk-V Duo has pre-soldered pin headers required for debugging
- Optional: Milk-V Duo IOB (baseboard)

## Installation Steps

### Flashing the Image to microSD Card Using `dd`

```shell
xzcat Fedora-38-Minimal-MilkV-Duo-riscv64.img.xz | sudo dd of=/dev/sdc bs=4M iflag=fullblock status=progress 
```

### Logging into the System

Log into the system via the serial port.

Username: `root`
Password: `fedora`

## Expected Results

The system should boot normally and allow login via the serial port.

## Actual Results

The system failed to boot successfully; systemd core dumps after powering on, preventing normal login.

### Boot Log

```log
[  *** ] (2 of 7) Job systemd-update-utmp.se…ice/start running (20s / no limit)                                                     
[  182.618625] (imesyncd)[130]: unhandled signal 11 code 0x1 at 0xffffffffffffffff in libsystemd-shared-253.2-614.7.riscv64.fc38.so]
[  182.632471] CPU: 0 PID: 130 Comm: (imesyncd) Not tainted 5.10.4-tag- #1                                                          
[  182.639349] epc: 0000003fb7b5aece ra : 0000003fb7b5aece sp : 0000003fffe42320                                                    
[  182.646762]  gp : 0000002ac2e73800 tp : 0000003fb71cb260 t0 : 0000003fb7c1d9d8                                                   
[  182.654266]  t1 : 0000003fb7b1dbbc t2 : 0000000000000000 s0 : 0000003fffe423a0                                                   
[  182.661769]  s1 : 0000003fb7ce9c20 a0 : 0000000000000000 a1 : 0000002ac2f6ee80                                                   
[  182.669273]  a2 : 0000002ac2f6ee80 a3 : 0000000000000000 a4 : 0000000000000000                                                   
[  182.676778]  a5 : 0000000000000000 a6 : fefefefefefefeff a7 : 0000000000000024                                                   
[  182.684277]  s2 : 0000002ac2f6ee80 s3 : 0000003fb7ce9c30 s4 : 0000000000000000                                                   
[  182.691781]  s5 : 0000002ac2f6ee80 s6 : 0000003fffe424c8 s7 : ffffffffffffffff                                                   
[  182.699286]  s8 : 000000000000002d s9 : ffffffffffffffff s10: ffffffffffffffff                                                   
[  182.706789]  s11: 0000000000000006 t3 : 0000003fb7bfc72e t4 : 0000000000000000                                                   
[  182.714293]  t5 : 0000000000000000 t6 : 000000000000002f                                                                         
[  182.719818] status: 8000000201804020 badaddr: ffffffffffffffff cause: 000000000000000d
```

Screen recording of the boot process:

[![asciicast](https://asciinema.org/a/MxHNPZZ2MG8vPEBSmMNwTz6DY.svg)](https://asciinema.org/a/MxHNPZZ2MG8vPEBSmMNwTz6DY)

### Defect Report

https://github.com/chainsx/fedora-riscv-builder/issues/6

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test failed.
