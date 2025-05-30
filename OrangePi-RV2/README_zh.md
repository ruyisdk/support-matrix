# OrangePi RV2

## 硬件规格

- **处理器**: Ky X1 (8核 RISC-V AI CPU, 提供2TOPS CPU融合的通用算力)
- **内存**: 2G/4G/8G LPDDR4X
- **存储**: 支持外部 MicroSD 卡或 eMMC 模块
- **接口**: Wi-Fi 5.0 + Bluetooth 5.0 with BLE support, 2个 M.2 M-Key 插槽
(PCIe 2.0 2-lane), USB3.0, USB2.0, MIPI DSI, MIPI CSI, Ethernet, PWM, I2C, SPI, CAN, UART, GPIO, RTC 连接器
- **电源**: 5V/5A

## 支持的操作系统

- Ubuntu 24.04.01 LTS (官方支持)
  - 下载链接: <http://www.orangepi.cn/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-Pi-RV2.html>
  - 参考安装文档: <http://www.orangepi.cn/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-Pi-RV2.html>
- OpenWRT 24.10.0 (官方支持)
  - 下载链接: <http://www.orangepi.cn/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-Pi-RV2.html>
  - 参考安装文档: <http://www.orangepi.cn/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-Pi-RV2.html>
- irradium 3.8
  - 下载链接：<https://mirror.serverion.com/irradium/images/orange_pi_rv2/irradium-3.8-riscv64-core-orange_pi_rv2-6.14.4-build-20250503.img.zst>
  - 参考安装文档：
    - <http://www.orangepi.cn/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-Pi-RV2.html>
    - <https://mirror.serverion.com/irradium/images/orange_pi_rv2/README.TXT>

## 测试结果

| 软件类别               | 报名称            | 测试结果 (测试报告)                             |
| --------------------- | ---------------- | ---------------------------------------------- |
| Ubuntu LTS 镜像启动    | N/A              | [Successful][Ubuntu LTS]                       |
| OpenWRT 镜像启动       | N/A              | [Successful][OpenWRT]                          |
| irradium 镜像启动      | N/A              | [Successful][irradium]                         |

[Ubuntu LTS]: ./Ubuntu/README_LTS_zh.md
[OpenWRT]: ./OpenWRT/README_zh.md
[irradium]: ./irradium/README_zh.md
