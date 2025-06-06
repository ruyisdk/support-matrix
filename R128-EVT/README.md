---
product: R128-EVT
cpu: R128-S2
cpu_core: XuanTie C906
ram: 1MB(SRAM) + 16MB(PSRAM)

vendor: awol-r128
board_variant: [
    generic,
]
cpu_arch: [
    xuantie-c906,
]
---

# R128 EVT Development Kit

## Test Environment

### Operating System Information

- FreeRTOS
    - SDK Link:
        - https://r128.docs.aw-ol.com/r128/get_sdk/
    - Test Precompiled Firmware: https://www.aw-ol.com/downloads/resources/126
    - Reference Installation Document:
        - https://r128.docs.aw-ol.com/devkit/r128_evt/

### Hardware Information

- R128 EVT Development Kit

## Test Results

| Software Category | Package Name  | Test Result (Test Report) |
|-------------------|---------------|---------------------------|
| FreeRTOS          | N/A           | [CFT][FreeRTOS]           |

[FreeRTOS]: ./FreeRTOS/README.md
