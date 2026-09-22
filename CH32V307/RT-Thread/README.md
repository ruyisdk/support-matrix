---
sys: rtthread
sys_ver: "5.3.1"
sys_var: null
status: basic
last_update: 2026-09-18
---

# RT-Thread CH32V307 Test Report

## Test Environment

### Operating System Information

- Source code: https://github.com/RT-Thread/rt-thread/tree/dc3da6d87fa980b5e4fe2f73a828708e69182b90
- Tested commit: `dc3da6d87fa980b5e4fe2f73a828708e69182b90` (serial banner prints 5.3.1; this is not the `v5.3.1` release tag)
- BSP: `bsp/wch/risc-v/ch32v307v-r1`
- Board README: https://github.com/RT-Thread/rt-thread/blob/dc3da6d87fa980b5e4fe2f73a828708e69182b90/bsp/wch/risc-v/ch32v307v-r1/README.md
- Toolchain: WCH RISC-V GCC 8.2.0
  - https://github.com/NanjingQinheng/sdk-toolchain-RISC-V-GCC-WCH/archive/refs/tags/V1.0.0.zip
- Build environment: RT-Thread Env v2.0.0 for Windows
  - https://github.com/RT-Thread/env-windows/releases
- Flasher: WCH-LinkUtility 3.1
  - https://www.wch.cn/downloads/WCH-LinkUtility_EXE.html
- SDK package (needed for `ch32v30x.h`): [CH32V307-SDK-for-RTT](https://github.com/kaidegit/CH32V307-SDK-for-RTT)

### Hardware Information

- CH32V307V-EVT-R1 (MCU: CH32V307VCT6)
- On-board WCH-LinkE (Type-C next to the two buttons)
- USB Type-C cable
- Optional: Ethernet cable for the on-board 10M PHY

This report was verified on Windows.

## Installation Steps

### Hardware connection

1. Plug Type-C into the on-board WCH-LinkE port (next to the two buttons). Do not use the USB connector on the opposite side.
2. Turn on the board power switch.
3. Windows Device Manager should show **WCH-LinkRV** and a COM port. Install the WCH-Link driver if they do not appear.

### Build

1. Download and extract WCH RISC-V GCC 8.2.0. `riscv-none-embed-gcc --version` should print 8.2.0.
2. Install RT-Thread Env v2.0.0.
3. Clone RT-Thread and open Env in the BSP directory:

```
git clone https://github.com/RT-Thread/rt-thread.git
cd rt-thread
git checkout dc3da6d87fa980b5e4fe2f73a828708e69182b90
cd bsp\wch\risc-v\ch32v307v-r1
```

4. `board.h` includes `ch32v30x.h`, but that header is not in the RT-Thread tree. In Env, enable the CH32V307 SDK package and run `pkgs --update`, or extract [CH32V307-SDK-for-RTT](https://github.com/kaidegit/CH32V307-SDK-for-RTT) into this BSP's `packages` directory.
5. Build:

```
scons --exec-path=YOUR_PATH\sdk-toolchain-RISC-V-GCC-WCH\bin
```

A successful build produces `rtthread.bin` in the BSP directory.

### Flash

1. Open WCH-LinkUtility. Set Target File to `rtthread.bin`.
2. Set Chip Mem to **224K ROM + 96K RAM** and click **Set**. Changing the dropdown without Set has no effect. CH32V307 flash and SRAM are configurable (288K+32K / 256K+64K / 224K+96K / 192K+128K). The board overview `ram: 64KB(SRAM)` is the 256K+64K datasheet split. This BSP's `board.h` uses 224K flash + 96K SRAM (`SRAM_SIZE 96`), so the flasher must match that split. It is not extra physical RAM, and it does not replace the board metadata.
3. Enable Erase, Program, Verify, and Reset, then download.

### Serial console

Open the WCH-Link COM port at 115200 8-N-1. Open the serial session **before** resetting the board, otherwise the banner is easy to miss.

## Expected Results

The board boots RT-Thread. The serial console shows the RT-Thread banner and an `msh >` prompt.

## Actual Results

The board booted. Serial output showed RT-Thread 5.3.1 and `msh >`. `help`, `ps`, `version`, and `free` responded.

On-board LED1/LED2 are only wired to header J3. They stay dark unless jumpered. The default `main.c` toggles PB5 (Arduino silk D5). Missing LEDs are not a boot failure.

### Boot Log

```log
 \ | /
- RT -     Thread Operating System
 / | \     5.3.1 build Sep 18 2026 19:21:26
 2006 - 2026 Copyright by RT-Thread team
msh >
```

### Optional: on-board 10M Ethernet

Default `ch32v307v-r1` leaves Ethernet off. In Env `menuconfig`: **Hardware Drivers Config → On-chip Peripheral Drivers → Enable Ethernet**. lwIP, netdev, and SAL come with that option; DHCP is on by default. Rebuild and flash with the same 224K+96K Chip Mem.

Plug the RJ45 into a LAN router (not a PC Ethernet port). After reset, `ifconfig` showed `e0` `LINK_UP` with a DHCP address, and `ping` to the gateway succeeded.

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
