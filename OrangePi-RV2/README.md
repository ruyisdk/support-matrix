---
vendor: orangepi-rv2
product: OrangePi RV2
cpu: Ky X1
cpu_core: "null"
ram: 2G/4G/8G
---

# OrangePi RV2

## Hardware Specifications

- **Processor**: Ky X1 (8-core RISC-V AI CPU 2TOPS of converged AI power)
- **Memory**: 2G/4G/8G LPDDR4X
- **Storage**: Support external MicroSD card or eMMC module
- **Interfaces**: Wi-Fi 5.0 + Bluetooth 5.0 with BLE support, two M.2 M-Key slots
(PCIe 2.0 2-lane), USB3.0, USB2.0, MIPI DSI, MIPI CSI, Ethernet, PWM, I2C, SPI, CAN, UART, GPIO, RTC Connector
- **Power**: 5V/5A

## Supported Operating Systems

- Ubuntu 24.04.01 LTS (official support)
  - Download link: <http://www.orangepi.cn/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-Pi-RV2.html>
  - Reference Installation Document: <http://www.orangepi.cn/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-Pi-RV2.html>
- OpenWRT 24.10.0 (official suport)
  - Download link: <http://www.orangepi.cn/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-Pi-RV2.html>
  - Reference Installation Document: <http://www.orangepi.cn/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-Pi-RV2.html>
- irradium 3.8
  - Download link: <https://mirror.serverion.com/irradium/images/orange_pi_rv2/irradium-3.8-riscv64-core-orange_pi_rv2-6.14.4-build-20250503.img.zst>
  - Reference Installation Document:
    - <http://www.orangepi.cn/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-Pi-RV2.html>
    - <https://mirror.serverion.com/irradium/images/orange_pi_rv2/README.TXT>

## Test Results

| Software Category     | Package Name     | Test Results (Test Report)                        |
| --------------------- | ---------------- | ------------------------------------------------- |
| Ubuntu LTS image boot | N/A              | [Successful][Ubuntu LTS]                          |
| OpenWRT image boot    | N/A              | [Successful][OpenWRT]                             |
| irradium image boot   | N/A              | [Successful][irradium]                            |

[Ubuntu LTS]: ./Ubuntu/README_LTS.md
[OpenWRT]: ./OpenWRT/README.md
[irradium]: ./irradium/README.md
