---
sys: rtthread
sys_ver: "5.3.1"
sys_var: null
status: basic
last_update: 2026-09-22
---

# RT-Thread ESP32-C3 Test Report

## Test Environment

### Operating System Information

- Source code: https://github.com/RT-Thread/rt-thread/tree/dc3da6d87fa980b5e4fe2f73a828708e69182b90
- Tested commit: `dc3da6d87fa980b5e4fe2f73a828708e69182b90` (serial banner prints 5.3.1; this is not the `v5.3.1` release tag)
- BSP: `bsp/ESP/ESP32_C3`
- Board README: https://github.com/RT-Thread/rt-thread/blob/dc3da6d87fa980b5e4fe2f73a828708e69182b90/bsp/ESP/ESP32_C3/README.md
- Toolchain: Espressif RISC-V GCC 11.2.0 (crosstool-NG esp-2022r1)
  - https://github.com/espressif/crosstool-NG/releases/download/esp-2022r1/riscv32-esp-elf-gcc11_2_0-esp-2022r1-win64.zip
- Build environment: RT-Thread Env v2.0.0 for Windows
  - https://github.com/RT-Thread/env-windows/releases
- Flasher: esptool 4.8.1 shipped with Env

`pkgs --update` pulls `ESP-IDF-latest` and `FreeRTOS-Wrapper-latest` into `packages/`. That directory is gitignored. The BSP `packages/SConscript` in the tree is empty, so the build does not see those packages until it includes them:

```python
import os
from building import *

cwd = GetCurrentDir()
objs = []

for d in ['ESP-IDF-latest', 'FreeRTOS-Wrapper-latest']:
    if os.path.isfile(os.path.join(cwd, d, 'SConscript')):
        objs = objs + SConscript(os.path.join(d, 'SConscript'))

Return('objs')
```

This DevKitM-1 is ESP32-C3 AZ revision v1.1. The default image header says `min_rev=3` and esptool refuses it. In `SConstruct`, before `elf2image` runs, set `image.min_rev = 0` and, when the attribute exists, `image.min_rev_full = 0`. `builtin_imgs/bootloader.bin` was not rebuilt. From the BSP directory, this script sets its `min_rev` to 0 and writes a separate file:

```python
from esptool.bin_image import LoadFirmwareImage

bl = LoadFirmwareImage("esp32c3", "builtin_imgs/bootloader.bin")
print("bootloader min_rev before", bl.min_rev)
bl.min_rev = 0
bl.save("bootloader-min_rev0.bin")
```

Run it with Env's Python: `python patch_bootloader_min_rev.py`. Flash `bootloader-min_rev0.bin` at `0x0` instead of the original `builtin_imgs/bootloader.bin`. This change is local to the board revision. It is not part of [RT-Thread/rt-thread#11816](https://github.com/RT-Thread/rt-thread/pull/11816).

On Windows, GNU ld records object paths with backslashes, so slash-only globs in `idf_port/ld/sections.ld` miss IRAM code and the boot dies with an illegal instruction. The separator-tolerant globs are in that pull request, commit `144e141e4de792cb8ebaca14ba4caaba18dc5e31`. On 2026-09-22 that commit was rebuilt and flashed to this board; COM10 still reached `msh >`. The command transcript below is from the image built on 2026-09-20 16:49:51.

### Hardware Information

- ESP32-C3-DevKitM-1 (Micro-USB, on-board CP2102N)
- This PC enumerated it as Silicon Labs CP210x COM10
- Chip: ESP32-C3 AZ (QFN32) revision v1.1, 4MB XMC flash, MAC `90:70:69:d7:46:70`

This report was verified on Windows.

## Installation Steps

### Hardware connection

1. Plug Micro-USB into the DevKitM-1.
2. If no COM port appears, install the Silicon Labs CP210x VCP driver and replug the board.

### Build

1. Unpack Espressif RISC-V GCC 11.2.0. `riscv32-esp-elf-gcc --version` should print 11.2.0.
2. Install RT-Thread Env v2.0.0.
3. Clone RT-Thread and enter the BSP:

```
git clone https://github.com/RT-Thread/rt-thread.git
cd rt-thread
git checkout dc3da6d87fa980b5e4fe2f73a828708e69182b90
cd bsp/ESP/ESP32_C3
```

4. In Env, run `pkgs --update`, then use the `packages/SConscript` shown above.
5. On Windows, apply the `sections.ld` change from pull request 11816. On this rev v1.1 board, also run the script above so `builtin_imgs/bootloader.bin` is saved with `min_rev` 0.
6. Build:

```
scons --exec-path=path\to\riscv32-esp-elf\bin
```

The BSP directory then contains `rtthread.bin`.

### Flash

From the BSP directory, with the three images at these offsets:

```
esptool.py -p COM10 -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size detect --flash_freq 80m 0x0 bootloader-min_rev0.bin 0x8000 partition-table.bin 0x10000 rtthread.bin
```

Replace `COM10` with the CP210x port on your machine.

### Serial console

Open that COM port at 115200 8-N-1. Open the serial session before resetting the board, otherwise the banner is easy to miss.

## Expected Results

The board boots RT-Thread. The serial console shows the RT-Thread banner and an `msh >` prompt.

## Actual Results

The board booted. Serial output showed RT-Thread 5.3.1, `Hello!RT-THREAD!`, and `msh >`. `help`, `ps`, `version`, and `free` responded.

Wi-Fi and BLE were not enabled. The default board target is LUATOS. The boot log enables GPIO12 as an output. This DevKitM-1's RGB LED is GPIO8, and that pin was not checked.

### Boot Log

```log
 \ | /
- RT -     Thread Operating System
 / | \     5.3.1 build Sep 20 2026 16:49:51
 2006 - 2026 Copyright by RT-Thread team
Hello!RT-THREAD!
msh >
```

```log
msh >help
RT-Thread shell commands:
pin              - pin [option]
list             - list objects
console          - console setting
version          - show RT-Thread version information
clear            - clear the terminal screen
free             - Show the memory usage in the system
ps               - List threads in the system
help             - RT-Thread shell help

msh >ps
thread       pri  status      sp     stack size max used left tick   error  tcb addr   usage
------------ ---  ------- ---------- ----------  ------  ---------- ------- ---------- -----
tshell        20  running 0x00000120 0x00001000     13%   0x00000009 OK      0x3fca34e0  N/A
sys workq     23  suspend 0x00000120 0x00000800     14%   0x0000000a OK      0x3fca2988  N/A
tidle0        31  ready   0x000000c0 0x00000100     75%   0x00000003 OK      0x3fcb5200  N/A
timer          4  suspend 0x00000100 0x00000200     50%   0x00000009 EINTRPT 0x3fcb5808  N/A
main          10  suspend 0x00000130 0x00000800     83%   0x00000009 EINTRPT 0x3fca2068  N/A

msh >version
RT-Thread 5.3.1 build Sep 20 2026 16:49:51

msh >free
total    : 76704
used     : 10144
maximum  : 10144
available: 66560
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful. Wi-Fi, BLE, and the GPIO8 LED were outside this run.
