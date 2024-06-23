# Microchip Polarfire SoC FPGA Icicle Kit

## Test Environment

### Operating System Information

- Ubuntu 24.04
    - Download Link: https://cdimage.ubuntu.com/releases/24.04/release/
    - Reference Installation Document: https://wiki.ubuntu.com/RISC-V/PolarFire%20SoC%20FPGA%20Icicle%20Kit
- BuildRoot 24.02.2
    - Source Code Download Link: https://buildroot.org/downloads/buildroot-2024.02.2.tar.gz
    - Reference Installation Document: https://gitlab.com/buildroot.org/buildroot/-/tree/master/board/microchip/mpfs_icicle?ref_type=heads
- OpenEmbedded / Yocto
    - Download Link: https://github.com/polarfire-soc/meta-polarfire-soc-yocto-bsp
    - Reference Installation Document: https://github.com/polarfire-soc/meta-polarfire-soc-yocto-bsp
- Arch Linux
    - Download Link: https://archriscv.felixc.at/
    - Reference Installation Document: https://felixc.at/2022/06/newbies-polarfire-soc-icicle-kit-first-experience
- OpenBSD
  - Download Link: https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/
  - Reference Installation Document: https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64
- FreeRTOS
    - Reference Installation Document: https://github.com/polarfire-soc/polarfire-soc-documentation/blob/master/applications-and-demos/asymmetric-multiprocessing/amp.md#building-the-linux--freertos--bm-demo
- Zephyr
    - Reference Installation Document: https://docs.zephyrproject.org/latest/boards/microchip/mpfs_icicle/doc/index.html
- NuttX
    - Reference Installation Document: https://nuttx.apache.org/docs/latest/platforms/risc-v/mpfs/index.html

### Hardware Information

- Microchip Polarfire SoC FPGA Icicle Kit

## Test Results

| Software Category        | Package Name | Test Results (Test Report) |
|----------------------|--------------|---------------------------|
| Ubuntu Image Boot    | N/A          | [Basic][Ubuntu] (Official Support) |
| Yocto Image Build and Boot | N/A      | [Basic][Yocto]            |
| BuildRoot Image Boot | N/A          | [Basic][BuildRoot]        |
| Arch Linux Boot      | N/A          | [CFT][Arch]               |
| OpenBSD Image Boot   | N/A          | [CFT][OpenBSD]            |
| FreeRTOS Image Build and Boot | N/A  | [CFT][FreeRTOS]           |
| Zephyr Image Build and Boot | N/A    | [CFT][Zephyr]             |
| NuttX Image Build and Boot | N/A     | [CFT][NuttX]              |


[Ubuntu]: ./Ubuntu/README.md
[BuildRoot]: ./BuildRoot/README.md
[Yocto]: ./Yocto/README.md
[Arch]: ./ArchLinux/README.md
[OpenBSD]: ./OpenBSD/README.md
[FreeRTOS]: ./FreeRTOS/README.md
[Zephyr]: ./Zephyr/README.md
[NuttX]: ./NuttX/README.md

