---
product: Longan Nano
cpu: GD32VF103
cpu_core: Nuclei Bumblebee
ram: 32KB(SRAM)

vendor: longan-nano
board_variant: [
    generic,
]
cpu_arch: [
    nuclei-bumblebee,
]
---

# Longan Nano

## Test Environment

### Operating System Information

- FreeRTOS/RT-Thread/ThreadX/μCOS-II
    - Source Code: https://github.com/Nuclei-Software/nuclei-sdk
    - Reference Installation Document: https://doc.nucleisys.com/nuclei_sdk/quickstart.html#build-run-and-debug-sample-application
        - https://doc.nucleisys.com/nuclei_sdk/design/board/gd32vf103c_longan_nano.html
- Zephyr
    - Source Code: https://github.com/zephyrproject-rtos/zephyr/tree/main
    - Reference Installation Document: https://docs.zephyrproject.org/latest/boards/sipeed/longan_nano/doc/index.html

### Hardware Information

- Longan Nano (GD32VF103CBT6)

## Test Results

| Software Category | Package Name | Test Results (Test Report) |
| ----------------- | ------------ | -------------------------- |
| FreeRTOS          | N/A          | [Success][FreeRTOS]        |
| RT-Thread         | N/A          | [Success][RT-Thread]       |
| Zephyr            | N/A          | [Success][Zephyr]          |
| ThreadX           | N/A          | [Success][ThreadX]         |
| μC/OS-II          | N/A          | [Success][uCOSII]          |

[FreeRTOS]: ./FreeRTOS/README.md
[RT-Thread]: ./RT-Thread/README.md
[ThreadX]: ./ThreadX/README.md
[Zephyr]: ./Zephyr/README.md
[uCOSII]: ./uCOSII/README.md
