---
sys: fedora
sys_ver: "44"
sys_var: server
status: basic
last_update: 2026-09-12
---

# Fedora 44 Server HiFive Premier P550 Test Report

## Test Environment

### Hardware Information

- Development board: HiFive Premier P550
- Additional hardware:
  - One MicroSD card
  - One USB Type-C cable

### Operating System Information

- OS version: Fedora Linux 44 (Server Edition) (`Fedora-Server-Host-Omni-44-20260731.0.riscv64.raw.xz`)
- Bootchain: `2026.08.00-HFP550`
- Download link:
  - <https://dl.fedoraproject.org/pub/alt/risc-v/release/44/Server/riscv64/images/Fedora-Server-Host-Omni-44-20260731.0.riscv64.raw.xz>
- Bootchain:
  - <https://github.com/sifiveinc/freedom-u-sdk/releases/tag/2026.08.00-HFP550>
- Reference installation documents:
  - <https://fedoraproject.org/wiki/Architectures/RISC-V/SiFive/HiFivePremierP550>
  - <https://www.sifive.com/document-file/hifive-premier-p550-image-update-procedure>
- Software reference document:
  - <https://www.sifive.com/document-file/hifive-premier-p550-software-reference-manual>

## Installation Steps

1. Download the Fedora image, checksum file, and P550 bootchain:

   ```bash
   wget -c https://dl.fedoraproject.org/pub/alt/risc-v/release/44/Server/riscv64/images/Fedora-Server-Host-Omni-44-20260731.0.riscv64.raw.xz
   wget -c https://dl.fedoraproject.org/pub/alt/risc-v/release/44/Server/riscv64/images/Fedora-Server-Host-Omni-44-20260731.0.riscv64.raw.xz.sha256
   wget -c https://github.com/sifiveinc/freedom-u-sdk/releases/download/2026.08.00-HFP550/bootloader_ddr5_secboot.bin
   ```

   Verify the Fedora image:

   ```bash
   sha256sum -c Fedora-Server-Host-Omni-44-20260731.0.riscv64.raw.xz.sha256
   ```

   Decompress the image:

   ```bash
   unxz Fedora-Server-Host-Omni-44-20260731.0.riscv64.raw.xz
   ```

2. Prepare an ext4-formatted MicroSD card and copy the Fedora image and bootloader to it.

   > The following commands assume that the MicroSD card is `/dev/sdX`. Use `lsblk` to confirm the actual device before proceeding.

   ```bash
   sudo umount /dev/sdX* 2>/dev/null
   sudo wipefs -a /dev/sdX
   sudo mkfs.ext4 -F -L P550_INSTALL /dev/sdX

   sudo mkdir -p /mnt/p550
   sudo mount /dev/sdX /mnt/p550

   sudo cp Fedora-Server-Host-Omni-44-20260731.0.riscv64.raw /mnt/p550/
   sudo cp bootloader_ddr5_secboot.bin /mnt/p550/

   sync
   sudo umount /mnt/p550
   ```

3. Insert the MicroSD card into the board, connect the serial console, and power on the P550.

   Serial settings:

   ```text
   Baud rate: 115200
   Data bits: 8
   Parity: None
   Stop bits: 1
   Flow control: None
   ```

   Set the board to boot from SPI Flash. When the following prompt appears:

   ```text
   Hit any key to stop autoboot
   ```

   press any key to enter U-Boot.

4. In U-Boot, verify the MicroSD card and files:

   ```text
   => mmc list
   => ls mmc 1
   ```

   The following files should be visible:

   ```text
   bootloader_ddr5_secboot.bin
   Fedora-Server-Host-Omni-44-20260731.0.riscv64.raw
   ```

5. Update the P550 bootchain:

   ```text
   => ext4load mmc 1 0x90000000 bootloader_ddr5_secboot.bin
   => es_burn write 0x90000000 flash
   ```

   Wait for the write operation to complete, then reboot the board.

6. Write the complete Fedora disk image to the onboard eMMC:

   ```text
   => es_fs write mmc 1 Fedora-Server-Host-Omni-44-20260731.0.riscv64.raw mmc 0
   ```

   After the write operation completes, power off the board and remove the MicroSD card.

7. Configure Fedora to boot automatically from the onboard eMMC.

   Power on the board again and enter U-Boot:

   ```text
   => env default -af
   => env set bootdev 'mmc 0'
   => env set bootcmd 'load ${bootdev}:2 ${fdt_addr_r} dtb/${fdtfile}; load ${bootdev}:1 ${kernel_addr_r} EFI/fedora/shimriscv64.efi; bootefi ${kernel_addr_r} ${fdt_addr_r};'
   => env set stdin serial
   => env set stdout serial
   => env set stderr serial
   => env save
   => reset
   ```

   The system will then boot Fedora automatically from the eMMC.

8. After the system boots, log in with the following credentials:

   ```text
   Username: fedora
   Password: linux
   ```

## Expected Results

The system should boot normally and allow login through the serial console or other methods.

## Actual Results

The system boots normally, and login through the serial console is successful.

### Boot Log

```text
[  OK  ] Reached target multi-user.target - Multi-User System.
[  OK  ] Finished cockpit-issue.service - Cockpit issue updater service.

Fedora Linux 44 (Server Edition)
Kernel 7.1.5-201.0.riscv64.omni.fc44.riscv64 on riscv64 (ttyS0)

Web console: https://localhost:9090/

localhost login: fedora
Password:

[fedora@localhost ~]$ uname -a
Linux localhost.localdomain 7.1.5-201.0.riscv64.omni.fc44.riscv64 #1 SMP PREEMPT_DYNAMIC Wed Jul 29 22:12:49 EDT 2026 riscv64 GNU/Linux
[fedora@localhost ~]$ cat /etc/os-release
NAME="Fedora Linux"
VERSION="44 (Server Edition)"
RELEASE_TYPE=stable
ID=fedora
VERSION_ID=44
PRETTY_NAME="Fedora Linux 44 (Server Edition)"
VARIANT="Server Edition"
VARIANT_ID=server
[fedora@localhost ~]$
```

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/1264802.svg)](https://asciinema.org/a/1264802)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
