---
sys: deepin
sys_ver: null
sys_var: null

status: basic
last_update: 2024-11-24
---

# Deepin Milk-V Mars Test Report

## Test Environment

### Operating System Information

- System Version: Deepin preview
- Download Link: https://cdimage.deepin.com/RISC-V/preview-20240613-riscv64/deepin-23-beige-preview-riscv64-milkv-mars-20240613-123442.tar.xz
- Reference Installation Document: https://milkv.io/zh/docs/mars/getting-started/boot

### Hardware Information

- Milk-V Mars
- A USB power adapter
- A USB-A to C or C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires

## Installation Steps

### Decompress and Flash Image to microSD Card

Use `tar` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
tar -xvf deepin-23-beige-preview-riscv64-milkv-mars-20240613-123442.tar.xz
sudo dd if=deepin-milkv-mars-riscv64-stable-desktop-installer.img of=/dev/sda bs=4M status=progress
```

### Logging into the System

Log into the system via the serial port.

Default username: `root`
Default password: `deepin`

## Expected Results

The system should boot up normally and allow login via the serial port.

## Actual Results

The system starts normally and the output is successfully viewed through the serial port.

### Boot Log

```log
root@deepin-riscv64-jh7110:/etc# cat /etc/os-release                            
PRETTY_NAME="Deepin 23"                                                         
NAME="Deepin"                                                                   
VERSION_ID="23"                                                                 
VERSION="23"                                                                    
ID=deepin                                                                       
HOME_URL="https://www.deepin.org/"                                              
BUG_REPORT_URL="https://bbs.deepin.org"                                         
VERSION_CODENAME=beige   
```

Screen recording (from flashing the image to system login):
[![asciinema](https://asciinema.org/a/EIM84vEQbB0JNug7ufjqykMOa)](https://asciinema.org/a/EIM84vEQbB0JNug7ufjqykMOa)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
