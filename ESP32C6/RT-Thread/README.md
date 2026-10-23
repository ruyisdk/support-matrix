---
sys: rtthread
sys_ver: "5.3.1"
sys_var: null
status: basic
last_update: 2026-09-28
---

# RT-Thread ESP32-C6 Test Report

## Test Environment

### Operating System Information

- Source code: https://github.com/RT-Thread/rt-thread/tree/65d666e5bb1e6b6b555e565755ac0aabb4e9a02a
- Tested commit: `65d666e5bb1e6b6b555e565755ac0aabb4e9a02a` (serial banner prints 5.3.1; this is not the `v5.3.1` release tag)
- Merged by [RT-Thread/rt-thread#11836](https://github.com/RT-Thread/rt-thread/pull/11836)
- BSP: `bsp/ESP/ESP32_C6`
- Toolchain: Espressif RISC-V GCC 11.2.0 (`riscv32-esp-elf-gcc`)
- Official `RT-Thread-packages/esp-idf` had no C6 sources at the time of this test. The build used https://github.com/cms19859230182-lang/esp-idf/tree/4fa003074a73774369d38123749fe64b7b4acbd3 , cloned to `packages/ESP-IDF-latest`. The commit is pinned because the `bsp/esp32c6-scons` branch it came from can move. That change was proposed in [RT-Thread-packages/esp-idf#17](https://github.com/RT-Thread-packages/esp-idf/pull/17) and was not merged.

### Hardware Information

- ESP32-C6-DevKitC-1
- Module: ESP32-C6-WROOM-1, RISC-V, revision v0.2, 8MB flash
- UART0 is GPIO16 / GPIO17 on the board's UART USB port (CP210x), 115200 8-N-1
- Flash settings used for the test: DIO, 8MB, 80MHz, application at `0x10000`

The default image enables GPIO, UART0, and ADC. I2C, SPI, PWM, Wi-Fi, BLE, and GDBStub stay off.

## Installation Steps

### Build

```
git clone https://github.com/RT-Thread/rt-thread.git
cd rt-thread
git checkout 65d666e5bb1e6b6b555e565755ac0aabb4e9a02a
cd bsp/ESP/ESP32_C6
```

Pin the esp-idf fork to the commit this report was tested against:

```
git clone https://github.com/cms19859230182-lang/esp-idf.git packages/ESP-IDF-latest
git -C packages/ESP-IDF-latest checkout 4fa003074a73774369d38123749fe64b7b4acbd3
git -C packages/ESP-IDF-latest rev-parse HEAD
```

`rev-parse HEAD` must print `4fa003074a73774369d38123749fe64b7b4acbd3`. Stop if it prints anything else. Otherwise run `scons` with `riscv32-esp-elf-gcc` 11.2.0 on `PATH`.

### Flash

`builtin_imgs/bootloader.bin` is an ESP32-C6 bootloader. Do not reuse the ESP32-C3 bootloader. Write the bootloader at `0x0`, the partition table at `0x8000`, and `rtthread.bin` at `0x10000`.

## Expected Results

The board boots RT-Thread. The serial console shows the RT-Thread 5.3.1 banner and an `msh >` prompt. `help` and `version` answer.

## Actual Results

The default image reached `msh`. `help` and `version` answered. `version` printed 5.3.1. `list timer` showed `current tick` increasing. `free` reported total 76704 and used heap about 68904.

GPIO1 read high on 3.3V and low on GND. ADC1 channel 1, on GPIO1, read 2167 on GND and 4095 on 3.3V. There is no calibration, so ground is not 0.

SPI2 loopback, with GPIO7 shorted to GPIO2, sent `0xA5` and read `0xA5000000`. That is not a single-byte match, so SPI stays unsupported. That test was not in the default image.

With `BSP_ENABLE_GDBSTUB` on, a store to address 4 printed `Entering gdb stub now.` GDB stopped in `main` at PC `0x42001c8c`, the same value as MEPC. The default image leaves this switch off.

The raw serial transcript was not kept. The numbers above are the ones recorded in the merged pull request.

Wi-Fi and BLE were not enabled.

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful for the default image: serial shell, GPIO1, and ADC1. SPI, Wi-Fi, and BLE were outside that image.
