---
vendor: jlc
product: HengShanPi D133EBS
cpu: D133EBS
cpu_core: E907
ram: 1MB SRAM + 8MB PSRAM

vendor: hengshanpi
board_variant: [generic]
cpu_arch: [
    xuantie-e907,
]
---

# HengShanPi

## Hardware Specifications

- **Processor**: D133EBS
- **Memory**: 1MB SRAM + 8MB PSRAM
- **Storage**: 16 MB QSPI Nor Flash
- **Interfaces**: RGB565, LVDS, DVP Camera, Ethernet, PWM, I2C, SPI, QSPI, UART, GPIO
- **Power**: 5 ~ 12 V

## Supported Operating Systems

- RT-Thread: 4.1.1
  - Download Link: <https://gitee.com/lcsc/luban-lite> or <https://gitee.com/artinchip/luban-lite>
  - Reference Installation Document: <https://wiki.lckfb.com/zh-hans/hspi-d133ebs>

## Test Results

| Software Category      | Package Name | Test Results (Test Report) |
|------------------------|--------------|----------------------------|
| RT-Thread Build & boot | Lunban-lite  | [Successful][RT-Thread]    |

[RT-Thread]: ./RT-Threand/README.md