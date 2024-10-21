---
sys: ubuntu
sys_ver: 24.04.1
sys_var: null

status: cft
last_update: 2024-06-21
---

# Ubuntu on Microchip PIC64GX Curiosity Kit

## Test environment

### Hardware information

- Microchip PIC64GX Curiosity Kit
- USB Type-C to Type-C Cable (comes with the kit)
- SanDisk Ultra microSD UHS-I Card 32GB (comes with the kit)

### OS info

- Ubuntu 24.04.1
    - Link: https://cdimage.ubuntu.com/releases/24.04.1/release/ubuntu-24.04.1-preinstalled-server-riscv64+pic64gx.img.xz
    - Docs: https://wiki.ubuntu.com/RISC-V/Microchip%20PIC64GX1000%20Curiosity%20Kit

### Other info

- PIC64GX Hart Software Services
    - Repo: https://github.com/pic64gx/pic64gx-hart-software-services
- Board reference document: https://www.microchip.com/en-us/development-tool/curiosity-pic64gx1000-kit-es
    - PDF: https://ww1.microchip.com/downloads/aemDocuments/documents/MPU64/ProductDocuments/SupportingCollateral/PIC64GX_Curiosity_Kit_User_Guide.pdf
- QuickStart Card: https://onlinedocs.microchip.com/oxy/GUID-6C67D962-A70D-4AD9-94B5-2AFDB8EFFD59-en-US-2/GUID-453EE85E-64C1-483D-9619-5CADA8E3FD8B.html

## (Optional) Update Hart Software Services (HSS)

According to Ubuntu Wiki, Ubuntu depends on HSS v2024.06 or later.

If your board comes with a version older than this, you'll need to upgrade HSS manually.

You can obtain the latest HSS source code from MicroChip's official repo: https://github.com/pic64gx/pic64gx-hart-software-services

## Write image to microSD

Use Rufus/Win32DiskImager/dd or any thing you like to write the image to microSD card.

```shell
xzcat ubuntu-24.04.1-preinstalled-server-riscv64+pic64gx.img.xz | sudo dd bs=1M conv=fsync status=progress of=/dev/sdX
```

## Powering up the board

Use the stock USB Type-C to Type-C cable, connect the board to your PC.

The board should power on automatically, and the onboard USB-UART chip should also connect to your PC, which provides 3 serial ports.

On Windows there will be 3 COM ports, while on Linux you should get `/dev/ttyUSB{0,1,2}`

| Serial Port Function   | Windows             | Linux          |
|------------------------|---------------------|----------------|
| HSS Console            | The first COM port  | `/dev/ttyUSB0` |
| U-Boot & Linux Console | The second COM port | `/dev/ttyUSB1` |
| AMP Console            | The third COM port  | `/dev/ttyUSB2` |

Use any tool you like, connect to the serial port and check boot logs.

> On the first boot, Ubuntu will invoke `cloud-init`. Limited by the performance of the development board, startup may take several minutes, which is expected.

Username: `ubuntu`

Password: `ubuntu`

You will be prompted to change the password upon first login, follow the instructions.

## Expected Results

The system should boot normally and allow login through the serial console.

## Actual Results

CFT

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT