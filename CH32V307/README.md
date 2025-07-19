---
product: CH32V307-EVT
cpu: CH32V307
cpu_core: QingKe V4F
ram: 64KB(SRAM)

vendor: wch-ch32v307-evb
---


# CH32V307

## Test Environment

### Operating System Information

- RT-Thread / FreeRTOS / LiteOS
    - Source Code Link: https://github.com/Community-PIO-CH32V/ch32-pio-projects
    - Reference Installation Document:
        - PlatformIO Core: https://docs.platformio.org/en/latest/core/installation/index.html
        - PlatformIO CH32V: https://pio-ch32v.readthedocs.io/en/latest/installation.html

### Hardware Information

- CH32V307V-EVT-R2-1v1

## Test Results

| Software Category | Package Name | Test Results (Test Report) |
| ----------------- | ------------ | -------------------------- |
| FreeRTOS          | N/A          | [Success][FreeRTOS]        |
| RT-Thread         | N/A          | [Success][RTThread]        |
| LiteOS            | PlatformIO   | [Success][LiteOS]          |

[FreeRTOS]: ./FreeRTOS/README.md
[RTThread]: ./RT-Thread/README.md
[LiteOS]: ./LiteOS/README.md
