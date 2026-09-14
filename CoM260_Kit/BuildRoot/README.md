---
sys: buildroot
sys_ver: "1.0.7"
sys_var: null

status: good
last_update: 2026-09-14
---

# Buildroot CoM260 Kit Test Report

## Test Environment

### System Information

- System Version: SpacemiT Buildroot K3 v1.0.7
- Download Link: [Here](https://archive.spacemit.com/image/k3/version/buildroot/v1.0.7/Buildroot-K3-v1.0.7-20260819142006.zip)
- Reference Installation Documentation: [Here](https://www.spacemit.com/community/document/info?lang=zh&nodepath=hardware/eco/k3_com260/com260_user_guide.md)

### Hardware Information

- CoM260 Kit, 16GB RAM / 128GB Storage
- DC Input (chassis rating): 19V / 2.37A or 12V / 5A
- USB Type-C Data Cable
- USB-to-TTL Serial Adapter and Jumper Wires
- 1 female-to-female jumper wire (for entering flashing mode)
- Network and Ethernet Cable

## Installation Steps

*The following steps use TITANTOOLS on Ubuntu (x86_64) to flash the image over USB.*

### Download the Flashing Tool

Download [TITANTOOLS FOR LINUX X64 (64-BIT) (APPIMAGE)](https://cloud.spacemit.com/prod-api/release/download/tools?token=titantools_for_linux_64BIT_APPIMAGE) as described in the [Flashing Tool User Manual](https://www.spacemit.com/community/document/info?lang=zh&nodepath=tools/user_guide/flasher_user_guide.md). In the download directory, make it executable and launch it:

```bash
chmod +x titantools_for_linux-2.2.0-Rc.AppImage
./titantools_for_linux-2.2.0-Rc.AppImage
```

### Enter Flashing Mode

Prepare 1 female-to-female jumper wire. Orient the board as shown below, with the USB and Ethernet ports at the bottom and the button header at the top. Count positions from the left end of the header toward the right in this orientation.

![CoM260 Kit button header](./boot-pins.png)

| Positions counted from the left | Signals to short | Purpose |
| --- | --- | --- |
| 3rd and 4th pins | `FC_REC` ↔ `GND` | Select flashing mode |

To short a pair of pins, connect one end of the same female-to-female jumper wire to each pin.

- **Device not powered**, with the board turned off:

    1. Disconnect DC power from CoM260.
    2. Disconnect the Type-C cable as well.
    3. Connect one end of the jumper wire to the 3rd pin, `FC_REC`, and the other end to the 4th pin, `GND`. Keep it connected.
    4. Connect DC power to power on CoM260.
    5. Wait 1–2 seconds.
    6. Remove the jumper wire from the header to release the short between the 3rd and 4th pins.
    7. Connect CoM260 to the Ubuntu host using a Type-C cable that supports data transfer.

### Flash the Image

1. Download the image above. In TITANTOOLS, select the single-device flashing option under the development tools.
2. Scan for devices and select the device corresponding to CoM260.
3. Select a local file, load `Buildroot-K3-v1.0.7-20260819142006.zip`, and wait for extraction to complete.

   ![Select a local image in TITANTOOLS](./titantools-select-image.png)

4. Start flashing. Wait for completion, then power-cycle the board.

   ![TITANTOOLS flashing firmware](./titantools-flashing.png)

### Logging into the System

Orient the board as shown in the pin diagram above, with the USB and Ethernet ports at the bottom and the header at the top. Count positions from the left end of the header toward the right, and connect the USB-to-TTL adapter using 3 jumper wires:

| Position counted from the left | CoM260 signal | USB-to-TTL adapter |
| --- | --- | --- |
| 6th | `GND` | `GND` |
| 9th | `UART_TXD` | `RXD` |
| 10th | `UART_RXD` | `TXD` |

Confirm that the UART signal voltage levels match before connecting. With the board powered off, connect the wires according to the adapter's pin labels. Leave the adapter's `VCC` disconnected, power the board through DC, and connect the adapter's USB end to the Mac or Linux host.

**Mac host:**

After installing [Homebrew](https://brew.sh/), install `tio` with:

```bash
brew install tio
```

Find serial devices in the Mac terminal:

```bash
find /dev -maxdepth 1 -name 'cu.*'
```

If multiple devices appear, compare the output before and after plugging in the USB-to-TTL adapter to identify the new device. The following command uses `/dev/cu.usbserial-1140` as an example serial device name; replace it with the device name found on your system:

```bash
tio -b 115200 /dev/cu.usbserial-1140
```

**Linux host:**

Install `tio` on Ubuntu / Debian:

```bash
sudo apt update
sudo apt install tio
```

For other Linux distributions, install `tio` using the appropriate package manager.

Find serial devices in the Linux terminal:

```bash
find /dev -maxdepth 1 \( -name 'ttyUSB*' -o -name 'ttyACM*' \)
```

If multiple devices appear, compare the output before and after plugging in the USB-to-TTL adapter to identify the new device. The following command uses `/dev/ttyUSB0` as an example serial device name; replace it with the device name found on your system:

```bash
sudo tio -b 115200 /dev/ttyUSB0
```

`tio` defaults to `8N1` with flow control disabled.

After connecting the serial terminal, power on the board once flashing is complete, monitor the boot output, and log in.

Default username: `root`

Default password: `bianbu`

### Common Issues

The Type-C port handles data transfer and flashing, but does not power the board. Connect the power supply through DCIN.

## Expected Results

The system boots up successfully and allows login through the serial port.

## Actual Results

The system boots up successfully and allows login through the serial port.

### Boot Log

Version note: The image filename indicates v1.0.7, while `VERSION` in `/etc/os-release` on the board reports `k3-br-v1.0.6`.

Screen recording (from power-on to serial login and system information checks):

[![asciicast](https://asciinema.org/a/x6K7vTDLs4InCYxb.svg)](https://asciinema.org/a/x6K7vTDLs4InCYxb)

```log
# uname -a
Linux K3-Buildroot 6.18.3 #1 SMP PREEMPT_DYNAMIC Wed Aug 19 06:28:14 UTC 2026 riscv64 GNU/Linux
# cat /etc/os-release
NAME=Buildroot
VERSION=k3-br-v1.0.6
ID=buildroot
VERSION_ID=2025.02.6
PRETTY_NAME="Buildroot 2025.02.6"
# cat /proc/cpuinfo
processor	: 0
hart		: 0
model name	: Spacemit(R) X100
isa		: rv64imafdcvh_zicbom_zicbop_zicboz_zicntr_zicond_zicsr_zifencei_zihintntl_zihintpause_zihpm_zimop_zaamo_zalrsc_zawrs_zfa_zfbfmin_zfh_zfhmin_zca_zcb_zcd_zcmop_zba_zbb_zbc_zbs_zkt_zvbb_zvbc_zve32f_zve32x_zve64d_zve64f_zve64x_zvfbfmin_zvfbfwma_zvfh_zvfhmin_zvkb_zvkg_zvkned_zvknha_zvknhb_zvksed_zvksh_zvkt_smaia_smstateen_ssaia_sscofpmf_ssnpm_sstc_svade_svinval_svnapot_svpbmt_sdtrig
mmu		: sv39
uarch		: spacemit,x100
mvendorid	: 0x710
marchid		: 0x8000000058000002
mimpid		: 0x33d8a600
hart isa	: rv64imafdcvh_zicbom_zicbop_zicboz_zicntr_zicond_zicsr_zifencei_zihintntl_zihintpause_zihpm_zimop_zaamo_zalrsc_zawrs_zfa_zfbfmin_zfh_zfhmin_zca_zcb_zcd_zcmop_zba_zbb_zbc_zbs_zkt_zvbb_zvbc_zve32f_zve32x_zve64d_zve64f_zve64x_zvfbfmin_zvfbfwma_zvfh_zvfhmin_zvkb_zvkg_zvkned_zvknha_zvknhb_zvksed_zvksh_zvkt_smaia_smstateen_ssaia_sscofpmf_ssnpm_sstc_svade_svinval_svnapot_svpbmt_sdtrig
```

Desktop screenshot:

![Buildroot Weston desktop](./weston-desktop.png)

If the Weston desktop does not start automatically, run the following command in the board's serial terminal:

```bash
/etc/init.d/S30weston-setup.sh start
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
