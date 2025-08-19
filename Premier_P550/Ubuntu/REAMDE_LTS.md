---
sys: ubuntu
sys_ver: 24.04.01
sys_var: LTS

status: CFT
last_update: 2025-04-09
---

# Ubuntu 24.04.01 LTS HiFive Premier P550 Test Report

## Test Environment

### Hardware Information

- Development Board: HiFive Premier P550
- Other Hardware:
  - A MicroSD card
  - A USB Type A to C cable

### Operating System Information

- OS Version: Ubuntu 2025.02.00 (Based on Ubuntu 24.04.01 LTS) (SiFive official support)
- Download Links: <https://github.com/sifiveinc/hifive-premier-p550-ubuntu/releases/tag/2025.02.00>
- Reference Installation Document: <https://www.sifive.com/document-file/hifive-premier-p550-image-update-procedure>
- Reference Softwave Document: <https://www.sifive.com/document-file/hifive-premier-p550-software-reference-manual>

## Installation Steps

1. Download and extract the OS image and bootloader files.

    ```bash
    wget https://github.com/sifiveinc/hifive-premier-p550-ubuntu/releases/download/2025.02.00/ubuntu-24.04-preinstalled-server-riscv64.img.xz

    wget https://github.com/sifiveinc/freedom-u-sdk/releases/download/2024.11.00-HFP550/bootloader_ddr5_secboot.bin

    unxz -d ubuntu-24.04-preinstalled-server-riscv64.img.xz
    ```

2. Mount the MicroSD card and use the `cp` command to copy the image files to the MicroSD card. (Assuming `/dev/sdX` is the MicroSD card device)

    ```bash
    sudo mount /dev/sdX /mnt/sd
    
    sudo cp ./ubuntu-24.04-preinstalled-server-riscv64.img ./bootloader_ddr5_secboot.bin /mnt/sd

    sync

    sudo umount /mnt/sd
    ```

3. Insert the MicroSD card, connect the serial port on the development board, boot the development board, and enter the U-Boot in the SPI Flash.
    - Ensure that the DIP switch is the SPI Flash startup mode: `DIP_SW1[3:0] = 0100`. (SW's ON = 0, OFF = 1)
    - Quickly press Enter when `Hit any key to stop autoboot` appears on the serial terminal to enter the U-Boot command line interface.

4. Burn the image using the custom U-Boot command.
    - Check that the images on the MMC card are readable.

        ```bash
        => ls mmc 1
        ```

    - Flash the new bootloader if necessary.

        ```bash
        => ext4load mmc 1 0x90000000 bootloader_ddr5_secboot.bin

        => es_burn write 0x90000000 flash
        ```

    - Flash the os image.

        ```bash
        => es_fs write mmc 1 ubuntu-24.04-preinstalled-server-riscv64.img mmc 0
        ```

5. Power cycle the board to boot with the new images.

## Expected Results

The system should boot normally and allow login via serial or other methods.

## Actual Results

CFT

### Test Conclusion

CFT
