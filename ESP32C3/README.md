---
product: LUATOS ESP32-C3
cpu: ESP32-C3
cpu_core: null
ram: 400K SRAM
---

# ESP32-C3

## Test Environment

### Operating System Information

- FreeRTOS(ESP-IDF)
    - Source Code: https://github.com/espressif/esp-idf
    - Reference Installation Document: https://docs.espressif.com/projects/esp-idf/zh_CN/v5.4.1/esp32c3/get-started/index.html
- Zephyr
    - Source Code: https://github.com/zephyrproject-rtos/zephyr/tree/main
    - Reference Installation Document: 
        - https://docs.zephyrproject.org/latest/develop/getting_started/index.html
        - https://docs.zephyrproject.org/latest/boards/luatos/esp32c3_luatos_core/doc/index.html

### Hardware Information

- LUATOS ESP32-C3

## Test Results

| Software Category     | Software Package | Test Results (Test Report)                        |
| --------------------- | ---------------- | ------------------------------------------------- |
| FreeRTOS  | N/A              | [Successful][FreeRTOS]                                |
| Zephyr  | N/A             | [Successful][Zephyr]                                |
                             |

[FreeRTOS]: ./FreeRTOS/README.md
[Zephyr]: ./Zephyr/README.md
