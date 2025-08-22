# BeagleV-Ahead

## 概述

BeagleV Ahead 围绕平头哥 TH1520 RISC-V SoC 构建，配备四核玄铁 C910 处理器，主频 1.85GHz，内置 4 TOPS NPU，支持 64 位 DDR，以及使用单核 C906 进行音频处理。

## 硬件规格

- **处理器**：平头哥 TH1520（四核玄铁 C910 处理器）
- **内存**：4GB LPDDR4
- **存储**：16GB eMMC
- **WiFi/蓝牙**：
  - PHY：AP6203BM
  - 天线：2.4GHz 和 5GHz
- **以太网**：
  - PHY: Realtek RTL8211F-VD-CG Gigabit Ethernet phy
  - 接口：集成变压器 RJ-45
- **microUSB 3.0**
  - 连接性：USB OTG，支持闪存
  - 电源：输入：5V，输出：5V
- **HDMI**：
  - 发送器：TH1520 视频输出系统
  - 接口：Mini HDMI

- **其他接口**：
  - microSD
  - mikroBUS 扩展板接口（I2C/UART/SPI/ADC/PWM/GPIO）
  - 2 个 CSI 接口，兼容 BeagleBone AI-64、Raspberry Pi Zero/CM4（22 针）
  - DSI 接口