---
sys: debian
sys_ver: "1.0.0-20250730"
sys_var: minimal
provider: Vendor
status: basic
last_update: 2026-09-07
---

# Debian HiFive Premier P550 Test Report

## Test Environment

### Hardware Information

- Board: HiFive Premier P550
- Other hardware:
  - A microSD card
  - A USB Type-C to Type-A cable

### Operating System Information

- System Version: Debian GNU/Linux trixie/sid (ESWIN Debian-v1.0.0-20250730)
- Download Link: <https://github.com/eswincomputing/eic7x-images/releases/tag/Debian-v1.0.0-20250730>
- Reference Installation Document:
  - <https://www.sifive.com/document-file/hifive-premier-p550-image-update-procedure>
- Software Reference Manual: <https://www.sifive.com/document-file/hifive-premier-p550-software-reference-manual>

## Installation Steps

1. Download and extract the operating system image.

    ```bash
    for i in 001 002 003 004; do
        wget -c "https://github.com/eswincomputing/eic7x-images/releases/download/Debian-v1.0.0-20250730/EIC7x_Release_Images_0730.zip.$i"
    done
    ```

    In this release, the actual archive volume order does not match the file numbering. Remap the volumes before extraction:

    ```bash
    mkdir -p fixed-split
    cd fixed-split

    ln -s ../EIC7x_Release_Images_0730.zip.002 EIC7x_Release_Images_0730.z01
    ln -s ../EIC7x_Release_Images_0730.zip.003 EIC7x_Release_Images_0730.z02
    ln -s ../EIC7x_Release_Images_0730.zip.004 EIC7x_Release_Images_0730.z03
    ln -s ../EIC7x_Release_Images_0730.zip.001 EIC7x_Release_Images_0730.zip

    7z x EIC7x_Release_Images_0730.zip
    cd EIC7x_Release_Images_0730
    ```

2. Format the microSD card as ext4 and copy the P550 minimal images. (Assume `/dev/sdb` is the microSD card device.)

    ```bash
    lsblk
    sudo umount /dev/sdb* 2>/dev/null || true
    sudo wipefs -a /dev/sdb
    sudo mkfs.ext4 -F -L P550_INSTALL /dev/sdb

    sudo mkdir -p /mnt/sd
    sudo mount /dev/sdb /mnt/sd
    ```

    Copy the boot and root images to the microSD card using short filenames:

    ```bash
    sudo cp ./dvb/bootloader_P550.bin /mnt/sd/
    sudo cp ./dvb/minimal/boot-P550-20250904-101110.ext4 /mnt/sd/b
    sudo cp ./dvb/minimal/root-P550-20250904-101110.ext4 /mnt/sd/r

    sync
    sudo umount /mnt/sd
    ```

3. Insert the microSD card, connect to the board through the serial port, power on the board, and enter U-Boot from SPI Flash.

    - Set the DIP switches to SPI Flash boot mode: `DIP_SW1[3:0] = 0100`. (ON = 0, OFF = 1)
    - When `Hit any key to stop autoboot` appears in the serial terminal, quickly press Enter to enter the U-Boot command line.
    - Confirm that the image files on the microSD card are accessible:

      ```text
      => ls mmc 1
               4751464 bootloader_P550.bin
            1048576000 r
             104857600 b
      ```

4. Create the eMMC partition table and flash the Debian images using U-Boot.

    ```text
    => run gpt_partition
    Writing GPT: success!
    ```

    Flash the boot partition:

    ```text
    => es_fs update mmc 1 b mmc 0:1
    ```

    Output:

    ```text
    Write progress: 100%:++++++++++++++++++++++++++++++++++++++++++++++++++
    mmc has been successfully writen in mmc 0:1
    ```

    Flash the root partition:

    ```text
    => es_fs update mmc 1 r mmc 0:3
    ```

    Output:

    ```text
    Write progress: 100%:++++++++++++++++++++++++++++++++++++++++++++++++++
    mmc has been successfully writen in mmc 0:3
    ```

5. Power off the board, remove the microSD card, and power it on again.

    ```text
    => poweroff
    poweroff ...
    eic770x_core_shutdown
    ```

    Log in with the following credentials after the system boots:

    ```text
    Username: eswin
    Password: eswin
    ```

## Expected Results

The system should boot normally and allow login through the serial port or other methods.

## Actual Results

The system boots normally and login through the serial port is successful.

### Boot Log

```text
[ OK ] Reached target graphical.target - Graphical Interface.
       Starting systemd-update-utmp-runle…- Record Runlevel Change in UTMP...
[ OK ] Finished systemd-update-utmp-runle…e - Record Runlevel Change in UTMP.

Debian GNU/Linux trixie/sid rockos-eswin ttyS0

rockos-eswin login: eswin
Password:

Linux rockos-eswin 6.6.92-eic7x-2025.07 #2025.09.04.09.57+ SMP Thu Sep  4 09:59:13 CST 2025 riscv64

eswin@rockos-eswin:~$ uname -a
Linux rockos-eswin 6.6.92-eic7x-2025.07 #2025.09.04.09.57+ SMP Thu Sep  4 09:59:13 CST 2025 riscv64 GNU/Linux

eswin@rockos-eswin:~$ cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"

eswin@rockos-eswin:~$
```

Screen recording (from flashing the image to logging into the system)：

[![asciicast](https://asciinema.org/a/1264770.svg)](https://asciinema.org/a/1264770)

## Test Criteria

Test success: The actual result is consistent with the expected result.

Test failure: The actual result is inconsistent with the expected result.

## Test Conclusion

Test successful.
