---
product: CH32V203-EVT
cpu: CH32V203
cpu_core: QingKe V4B
ram: 20KB(SRAM)

vendor: wch-ch32v203-evb
board_variant: [
    c6t6,
    c8t6,
    c8u6.
    f8p6,
    f8u6,
    g6u6,
    g8r6,
    k6t6,
    k8t6,
    rbt6,
]
cpu_arch: [
    wch-v4,
]
---


# CH32V203

## Test Environment

### Operating System Information

- RT-Thread / FreeRTOS
    - Source Code Link: [GitHub Repository](https://github.com/Community-PIO-CH32V/ch32-pio-projects)
    - Reference Installation Document:
        - PlatformIO Core: [Installation Guide](https://docs.platformio.org/en/latest/core/installation/index.html)
        - PlatformIO CH32V: [Installation Guide](https://pio-ch32v.readthedocs.io/en/latest/installation.html)


### Hardware Information

- CH32V203G6U6-EVT-R0-1v0
- CH32V203C8T6-EVT-R0-1v0

## Test Results


| Software Category | Package Name | Test Results (Test Report) |
| ----------------- | ------------ | -------------------------- |
| FreeRTOS          | N/A          | [Success][FreeRTOS]        |
| RT-Thread         | N/A          | [Success][RTThread]        |

[FreeRTOS]: ./FreeRTOS/README.md
[RTThread]: ./RT-Thread/README.md
