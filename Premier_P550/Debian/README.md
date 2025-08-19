---
sys: debian
sys_ver: null
sys_var: null

status: CFT
last_update: 2025-04-09
---

# Debain HiFive Premier P550 Test Report

## Test Environment

### Hardware Information

- Development Board: HiFive Premier P550
- Other Hardware:
  - A MicroSD card
  - A USB Type A to C cable

### Operating System Information

- OS Version: Debian-v1.0.0-20250228 (ESWIN official support)
- Download Links: <https://github.com/eswincomputing/eic7x-images/releases/tag/Debian-v1.0.0-20250228>
- Reference Installation Document:
  - <https://www.sifive.com/document-file/hifive-premier-p550-image-update-procedure>
  - <https://github.com/eswincomputing/eic7x-images/releases/download/Yocto-v1.0.0-20241021/EIC7700_Debian_Yocto_Ubuntu_System_Burnning_Guide.pdf>
- Reference Softwave Document: <https://www.sifive.com/document-file/hifive-premier-p550-software-reference-manual>

## Installation Steps

1. Download and extract the OS image and bootloader files.

    ```bash
    wget -c https://github.com/eswincomputing/eic7x-images/releases/download/Debian-v1.0.0-20250228/EIC7x_Release_Images_20250228.zip.00*
    
    7z x EIC7x_Release_Images_20250228.zip.001
    ```

2. Mount the MicroSD card and use the `cp` command to copy the image files to the MicroSD card. (Assuming `/dev/sdX` is the MicroSD card device)

    ```bash
    sudo mount /dev/sdX /mnt/sd
    
    sudo cp ./boot-P550-20250311-170029.ext4 ./root-P550-20250311-170029.ext4 ./bootloader_P550.bin /mnt/sd

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

    - Check the GPT(GUID Partition Table).

        ```bash
        => run gpt_partition

        => mmc part
        ```

    - Flash the os image.

        ```bash
        => es_fs update mmc 1 boot-P550-20250311-170029.ext4 mmc 0:1

        => es_fs update mmc 1 root-P550-20250311-170029.ext4 mmc 0:3
        ```

5. Power cycle the board to boot with the new images.

## Expected Results

The system should boot normally and allow login via serial or other methods.

## Actual Results

CFT

### Test Conclusion

CFT
