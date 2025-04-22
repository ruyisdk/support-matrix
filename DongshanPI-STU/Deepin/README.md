---
sys: deepin
sys_ver: 23
sys_var: null

status: basic
last_update: 2025-04-22
---

# Deepin DongshanPI-Nezha STU Test Report

## Test Environment

### System Information

- System Version: Deepin 23 beige 20221209
- Download Link: https://github.com/deepin-community/deepin-riscv-board/releases/download/v20221209/deepin-d1-20221208175445.img.zst.0
- Reference Installation Document: https://github.com/deepin-community/deepin-riscv-board/

### Hardware Information

- DongshanPI-Nezha STU
- Power Adapter
- A microSD card

## Installation Steps

### Logging into the System

Login to the system via serial port or GUI.

Default username for serial: `root`
Password: `Riscv2022#`

Default username for GUI: `deepin`
Password: `deepin`

## Expected Results

The system should boot successfully, allowing login via the onboard serial console.

## Actual Results

The system boots up successfully, and login via onboard serial port is successful.

Video output works as well, but the desktop environment takes quite a few minutes to login and is practically unusable due to the immense lag.

### Boot Log

```log
Deepin GNU/Linux
Deepin GNU/Linux 23 deepin-riscv  23 deepin-riscv ttyS0

deepin-riscv login: hvc0

deepin-riscv login: root
Password:
Verification successful
Linux deepin-riscv 6.1.0-rc3+ #1 PREEMPT Thu Dec  8 17:52:42 UTC 2022 riscv64
Welcome to Deepin 23 GNU/Linux

    * Homepage:https://www.deepin.org/

    * Bugreport:https://bbs.deepin.org/


root@deepin-riscv:~# [  190.417842] fbcon: Deferring console take-over
[  190.422420] sun4i-drm display-engine: [drm] fb0: sun4i-drmdrmfb frame buffer device
[  191.959682] enter sun20i_d1_hdmi_phy_config
[  191.970283] enter sun20i_d1_hdmi_phy_enable
[  191.982312] [sun20i_d1_hdmi_phy_enable]:phy_rcalend2d_status
[  191.994318] [sun20i_d1_hdmi_phy_enable]:pll_lock_status
[  192.006308] [sun20i_d1_hdmi_phy_enable]:tx_ready_status

root@deepin-riscv:~# uname -a
Linux deepin-riscv 6.1.0-rc3+ #1 PREEMPT Thu Dec  8 17:52:42 UTC 2022 riscv64 GNU/Linux
root@deepin-riscv:~# cat /etc/os-release
PRETTY_NAME="Deepin 23"
NAME="Deepin"
VERSION_ID="23"
VERSION="23"
ID=Deepin
HOME_URL="https://www.deepin.org/"
BUG_REPORT_URL="https://bbs.deepin.org"
VERSION_CODENAME=beige
root@deepin-riscv:~#

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
