---
sys: ubuntu
sys_ver: "25.04"
sys_var: null

status: CFT
last_update: 2025-04-18
---

# Ubuntu Pine64 Star64 Test Report

## Test Environment

### Operating System Information

- System Version: Ubuntu 25.04
- Download Link: https://cdimage.ubuntu.com/releases/25.04/release/ubuntu-25.04-preinstalled-server-riscv64+jh7110.img.xz
- Reference Installation Document: https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/pine64-star64/

### Hardware Information

- Pine64 Star64
- A microSD card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires

## Installation Steps

### Decompress and Flash the Image to the microSD Card

Assume `/dev/sdc` is the storage card.

```bash
xz -d ubuntu-25.04-preinstalled-server-riscv64+jh7110.img.xz
sudo dd if=ubuntu-25.04-preinstalled-server-riscv64+jh7110.img of=/dev/sdc bs=1m status=progress
```

### Logging into the System

1. Insert the microSD card into the board

2. Set the boot source to the microSD card (see [Boot source selection](https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/pine64-star64/#boot-source-selection))

3. Connect a USB UART adapter to the UART on the GPIO header (see [UART console](https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/pine64-star64/#uart-console))

4. Power on the board

5. When “Hit any key to stop autoboot” is displayed, press Enter

6. Reset the U-Boot environment with the following commands:

```bash
env default -f -a
env save
```

7. Power cycle the board

8. Wait for an output line confirming that cloud-init has finished running; this service is responsible for generating SSH keys, and creating the default user:

```log
[   35.682018] cloud-init[909]: Cloud-init v. 24.1.3-0ubuntu3 finished at Tue, 23 Apr 2024 07:44:59 +0000. Datasource DataSourceNoCloud [seed=/var/lib/cloud/seed/nocloud-net][dsmode=net].  Up 35.65 seconds
```

9. Login with the user `ubuntu` and the default password `ubuntu`

## Expected Results

The system boots up normally, and information can be viewed through the onboard serial port.

## Actual Results

CFT

### Boot Log

Screen recording (from flashing the system to booting up):
```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
</details>
