---
sys: rtthread
sys_ver: "5.3.1"
sys_var: null
status: basic
last_update: 2026-09-29
---

# RT-Thread CH32V003 Test Report

## Test Environment

### Operating System Information

- Source code: https://github.com/RT-Thread/rt-thread/tree/6f99d7bf97911c47a19ce9c52ccdc74d6b31cab4
- Tested commit: `6f99d7bf97911c47a19ce9c52ccdc74d6b31cab4` (serial banner prints 5.3.1; this is not the `v5.3.1` release tag)
- BSP: `bsp/wch/risc-v/ch32v003f4p6-evt`, added by [RT-Thread/rt-thread#11838](https://github.com/RT-Thread/rt-thread/pull/11838), merged by Rbb666 on 2026-09-28
- Board README: https://github.com/RT-Thread/rt-thread/blob/6f99d7bf97911c47a19ce9c52ccdc74d6b31cab4/bsp/wch/risc-v/ch32v003f4p6-evt/README.md
- Toolchain: WCH RISC-V GCC 8.2.0
  - https://github.com/NanjingQinheng/sdk-toolchain-RISC-V-GCC-WCH
- Build environment: RT-Thread Env v2.0.0 for Windows
  - https://github.com/RT-Thread/env-windows/releases
- Flasher: WCH-LinkUtility 3.1
  - https://www.wch.cn/downloads/WCH-LinkUtility_EXE.html

The chip vendor SDK sources this BSP builds against (`libraries/ch32v00x`) are inside the BSP directory, so no extra SDK package has to be downloaded.

### Hardware Information

- CH32V003F4P6-EVT (MCU: CH32V003F4P6, TSSOP20, up to 48 MHz, 16 KB flash + 2 KB SRAM)
- External WCH-LinkE. This board has no on-board debugger.
- Dupont wires for the debug line and for the serial pair
- USB Type-C cable. The Type-C on this board only supplies power.

This report was verified on Windows.

## Installation Steps

### Hardware connection

1. Connect the WCH-LinkE to the board with dupont wires: 3V3 to the board's VCC silkscreen, GND to GND, SWDIO to PD1. SWCLK is not connected. Do not power the board from the LinkE 5V pin.
2. The serial pins are separate and must be crossed: LinkE TX to board PD6, LinkE RX to board PD5. The console is USART1 (TX PD5, RX PD6).
3. Windows Device Manager should show **WCH-LinkRV** and a COM port (COM11 on this machine). Install the WCH-Link driver if they do not appear.

### Build

1. Download and extract WCH RISC-V GCC 8.2.0. `riscv-none-embed-gcc --version` should print 8.2.0.
2. Install RT-Thread Env v2.0.0.
3. Clone RT-Thread and open Env in the BSP directory:

```
git clone https://github.com/RT-Thread/rt-thread.git
cd rt-thread
git checkout 6f99d7bf97911c47a19ce9c52ccdc74d6b31cab4
cd bsp\wch\risc-v\ch32v003f4p6-evt
```

4. Build:

```
scons --exec-path=YOUR_PATH\sdk-toolchain-RISC-V-GCC-WCH\bin
```

A successful build produces `rtthread.bin` in the BSP directory. The default image opens UART1 only. This chip has 16 KB of flash and 2 KB of SRAM, so nothing else is enabled.

### Flash

1. Open WCH-LinkUtility. Set Series to **CH32V003** (not CH32V20X) and Target File to `rtthread.bin`.
2. Do not tick **Erase All**. Do not click **Set** on the Chip Mem dropdown: this part has 16 KB flash + 2 KB SRAM.
3. If the chip is running, a direct download fails (the tool reports 10002). Hold the board in reset first, then download.

### Serial console

Open the WCH-Link COM port at 115200 8-N-1. Open the serial session **before** resetting the board, otherwise the banner is easy to miss.

## Expected Results

The board boots RT-Thread. The serial console shows the RT-Thread banner and an `msh >` prompt.

## Actual Results

The board booted. On COM11 the serial output showed the RT-Thread 5.3.1 banner, the `MCU: CH32V003F4P6` line printed by the BSP and an `msh >` prompt. The image that was run on the board occupied 15680 bytes of the 16 KB flash.

Only the serial console was exercised on this board. GPIO, ADC and SPI were not run here and stay **to be supported**; I2C and TIM were not run either.

### Boot Log

```log
 \ | /
- RT -     Thread Operating System
 / | \     5.3.1 build Sep 25 2026 20:46:44
 2006 - 2026 Copyright by RT-Thread team
MCU: CH32V003F4P6
msh >
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
