---
product: Sipeed M0 sense
cpu: BL702
cpu_core: SiFive E24
ram: 132KB

vendor: sipeed-m0sense
---

# Sipeed M0sense

## Test Environment

### Operating System Information

- FreeRTOS Demo
    - Source Link: [https://gitee.com/Sipeed/M0sense_BL702_example](https://gitee.com/Sipeed/M0sense_BL702_example)
    - Reference Installation Document: [https://wiki.sipeed.com/hardware/zh/maixzero/sense/start.html](https://wiki.sipeed.com/hardware/zh/maixzero/sense/start.html)
- RT-Thread / RT-Thread Smart
  - Source Code Link: https://github.com/RT-Thread/rt-thread
  - Reference Installation Document: https://github.com/RT-Thread/rt-thread/blob/master/bsp/bouffalo_lab/README.md

### Hardware Information

- Sipeed Maix M0sense

## Test Results

| Software Category | Package Name          | Test Result (Test Report) |
| ----------------- | --------------------- | ------------------------- |
| FreeRTOS Demo     | single_button_control | [Successful][FreeRTOS]    |
| RT-Thread         | N/A                   | [Successful][RT-Thread]   |

[FreeRTOS]: ./FreeRTOS/README.md
[RT-Thread]: ./RT-Thread/README.md
