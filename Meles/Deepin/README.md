---
sys: deepin
sys_ver: "20250122"
sys_var: null

status: good
last_update: 2025-04-05
---

# RevyOS Meles Version Test Report

## Test Environment

### Operating System Information

- System Version: Deepin TH1520 20250122
- Download Link: https://ci.deepin.com/repo/deepin/deepin-ports/cdimage/20250122/riscv64/deepin-25-beige-preview-riscv64-th1520-20250122-113934.tar.xz
    - iw-single-line binary: https://mirror.iscas.ac.cn/revyos/extra/images/meles/20240720/iw-single-line.bin
    - U-Boot with SPL firmware: https://cdimage.deepin.com/RISC-V/preview-20240815-riscv64/uboot-th1520-revyos.zip
- Reference Installation Document: https://milkv.io/zh/docs/meles/getting-started/boot

> [!WARNING]
> This image is not officially compatible with the Milk-V Meles; manual modification of the dtb environment variable is required as in the steps below.
>
> HDMI audio is not working.
>

### Hardware Information

- Milk-V Meles 4GB/8GB/16GB
- eMMC module > 16GB
- A USB A to C cable
- Optional: A USB-TTL Debugger (Flash U-Boot with SPL to SPI NOR Flash)
- Optional: Keyboard, monitor, mouse (for graphical interface testing)

## Installation Steps

Milk-V Meles' Bootloader is stored inside the onboard SPI NOR Flash, which can be upgraded using `cct` tool provided by `yoctools`. This is different from Lichee Pi 4A which uses the same TH1520 SoC.

You'll need UART serial connection to flash the firmware.

> Note: please do not try to use `fastboot flash uboot` method to upgrade U-Boot firmware, which is the same as the LPi4A.
> This method will NOT flash U-Boot to SPI NOR Flash which is loaded on boot by default. Thus you must use `cct` to flash the firmware.

Known issue: some AMD boards might not pick up Meles in fastboot mode.

Workaround: try connect Meles to a external USB Hub rather than the USB ports directly provided by the motherboard/PCH.

### Use `cct` to flash Bootloader into SPI NOR Flash

`cct` is the image flashing tool provided by `yoctools`, which requires Python 3.6~3.11 and Linux.

If your distro has already upgrade to Python 3.12+, then you'll need to manually install Python 3.11, create a Python virtual environment with it.

Since Python 3.12 and [PEP 668](https://peps.python.org/pep-0668/), you can not use `pip` to install packages globally.

And `yoctools` still depends on some packages which were already deprecated/replaced in Python 3.12+, thus you must create a Python venv in order to use `yoctools`.

Take Arch Linux as an example. By the time this article was written (2025.01), the default Python is Python 3.13, directly install `yoctools` will not work. You should install Python 3.11 from [AUR](https://aur.archlinux.org/packages/python311/) and creating a virtual environment using this version in order to flash the firmware.

Prepare Python 3.11 environment:

```shell
paru python311
sudo pacman -S python-virtualenv
virtualenv -p 3.11 meles
source meles/bin/activate
pip install yoctools
cd meles/bin
```

For those distros still staying at Python 3.6~3.11, you can install `yoctools` directly with `pip`. Python venv is not required.

Download the firmware:

```shell
wget https://mirror.iscas.ac.cn/revyos/extra/images/meles/20240720/iw-single-line.bin
wget https://cdimage.deepin.com/RISC-V/preview-20240815-riscv64/uboot-th1520-revyos.zip
unzip uboot-th1520-revyos.zip
```

Note: choose the correct version depending on your board's RAM:

- 4GB -> uboot-th1520-revyos/light_milkv_meles_singlerank/u-boot-with-spl.bin
- 8GB -> uboot-th1520-revyos/light_milkv_meles_dualrank/u-boot-with-spl.bin
- 16GB -> uboot-th1520-revyos/light_milkv_meles_16g/u-boot-with-spl.bin

The `iw-single-line.bin` can be used with all RAM versions.

Connect the board and your PC with UART debugger. **DO NOT** run tools like `minicom` or `tio` which will occupy the serial port.

Hold the recovery button and **THEN** power on the board.

> The recovery button is located at the edge of the board near the GPIO pins, while the eMMC boot button is on the inner side - Don't be confused!
> For details please refer to: https://milkv.io/docs/meles/hardware/meles-main-board

```shell
sudo ./cct list
sudo ./cct download -d ram0 -f iw-single-line.bin -v checksum -r
sudo ./cct download -d qspi0 -f uboot-th1520-revyos/light_milkv_meles_16g/u-boot-with-spl.bin -v checksum -r -t 1200
```

Wait for the flashing progress to complete, then power off the board, hold the recovery button and reconnect it to PC.

### Flashing Image using `fastboot` onto the Development Board

Check connection status:

```shell
$ lsusb | grep T-HEAD
Bus 001 Device 045: ID 2345:7654 T-HEAD USB download gadget
```

Next, execute the following commands to download, extract and flash the images to your board's eMMC.

> If `fastboot` doesn't pick up the board or you encounter flashing issues, check the device connection and try running `fastboot` as a privileged user (i.e. `sudo`). Doing so is usually required under Linux since the default USB VID/PID is not in the default udev rules.

```shell
wget https://ci.deepin.com/repo/deepin/deepin-ports/cdimage/20250122/riscv64/deepin-25-beige-preview-riscv64-th1520-20250122-113934.tar.xz
tar xvf deepin-25-beige-preview-riscv64-th1520-20250122-113934.tar.xz
sudo fastboot flash ram uboot-th1520-revyos/light_milkv_meles_16g/u-boot-with-spl.bin
sudo fastboot reboot; sleep 3
sudo fastboot flash boot deepin-th1520-riscv64-25-desktop-installer.boot.ext4
sudo fastboot flash root deepin-th1520-riscv64-25-desktop-installer.root.ext4
```

After the flashing process, reset the board and you're good to go.

> ![WARNING]
> The following steps is REQUIRED for successful login via GUI with this image.

Interrupt the booting process at `Hit any key to stop autoboot`, and run the following in the U-Boot console:

```shell
env set fdtfile thead/th1520-milkv-meles-16g.dtb; env save; reset
```

### Logging into the System

Logging into the system via serial port or graphical interface.

Complete the OOBE as guided, and login with the set user and password after a couple of minutes.

## Expected Results

The system should boot up normally and allow login through the serial port.

HDMI output works and the user can login to the desktop environment.

## Actual Results

The system should boot up normally and allow login through the serial port.

HDMI output works (except audio) and the user can login to the desktop environment.

### Boot Log

See https://github.com/QA-Team-lo/oscompare/blob/main/Deepin/Meles/README.md for our report on its desktop experience.

![](image/2025-01-24-01-07-27.png)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
