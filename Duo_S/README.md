# Milk-V Duo S

## Test Environment

### Operating System Information

- BuildRoot & FreeRTOS
  - Download Link: https://github.com/milkv-duo/duo-buildroot-sdk/releases
    - BuildRoot SDK provided by Milk-V, which also includes FreeRTOS
  - Reference Installation Document: https://github.com/milkv-duo/duo-buildroot-sdk
- Apache NuttX RTOS
  - Source Code Links
    - NuttX: https://github.com/lupyuen2/wip-nuttx/tree/sg2000
    - NuttX Apps: https://github.com/lupyuen2/wip-nuttx-apps/tree/sg2000
  - Reference Installation Document: https://github.com/lupyuen/nuttx-sg2000

### Hardware Information

- Milk-V Duo S (512M, SG2000)

## Test Results

| Software Category           | Package Name | Test Result (Report)     |
| --------------------------- | ------------ | ------------------------ |
| BuildRoot Image Boot        | N/A          | [Successful][BuildRoot]  |
| FreeRTOS Boot               | mailbox-test | [Successful][FreeRTOS]   |
| Apache NuttX Build and Boot | N/A          | [Successful, WIP][NuttX] |
| Zephyr Image Build and Boot | N/A          | [Successful][Zephyr]     |

[BuildRoot]: ./BuildRoot/README.md
[FreeRTOS]: ./FreeRTOS/README.md
[NuttX]: ./NuttX/README.md
[Zephyr]: ./Zephyr/README.md
