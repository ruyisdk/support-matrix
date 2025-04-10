# HiFive Premier P550

## 概述

HiFive Premier P550 是一款由 ESWIN EIC7700X SoC 驱动的 Mini-DTX 规格的高性能 RISC-V 单板计算机，配备运行频率为 1.4 GHz 的 SiFive 四核 P550 64 位 RISC-V 处理器和集成的 Imagination AXM-8-256 GPU以及 ~20 TOPS 的硬件加速 AI NPU。其具有完备的 PC IO 并预装 Ubuntu 24.04 操作系统。

## 硬件规格

- **处理器**: ESWIN EIC7700X (四核 SiFive P550)
- **内存**: 16GB/32GB LPDDR5
- **存储**: 128GB eMMC
- **接口**:
  - 2 个 10/100/1000 Ethernet RJ45 接口
  - 1 个用于远程板卡管理的 Ethernet RJ45 接口（通过专用 MCU 实现）
  - 1 个 M.2 Key E 接口，用于 Wi-Fi / Bluetooth 模块（通过 SDIO / UART 接口连接）
  - 1 个 PCI Express Gen 3 x4（通过 PCIe x16 插槽）
  - 2 个 USB 3.2 Gen 1 Type-A 接口
  - 1 个 USB 19-pin 公连接器，支持前面板 2 个 USB 3.2 Gen 1 接口
  - 1 个 USB Type-E 接口，支持前面板 1 个 USB 3.2 Gen 1 Type-C 接口
  - 1 个 JTAG 接口
  - 1 个 SATA 3 接口（6Gb/s）
  - 1 个 microSD 卡接口
  - 1 个 USB Type-C 接口（仅支持 USB2），通过 FT4232H 提供调试 UART/JTAG 支持
  - 1 个 HDMI 2.0 接口
  - 符合 Mini-ITX 机箱标准的前面板接口
  - 1 个 CR1220 电池座，用于实时时钟
  - 3 个风扇接口
  - 1 个音频接口（前面板立体声输出和输入/麦克风信号）
  - 1 个后面板立体声插孔，带麦克风输入
  - 1 个 40-pin 外设 I/O 接口
- **电源**: 标准 ATX 电源

## 支持的操作系统

- Ubuntu - 2025.02.00 (基于Ubuntu 24.04.01 LTS) (SiFive 官方支持)
  - 下载链接：<https://github.com/sifiveinc/hifive-premier-p550-ubuntu/releases/tag/2025.02.00>
  - 参考安装文档：<https://www.sifive.com/document-file/hifive-premier-p550-image-update-procedure>
- Debian - Debian-v1.0.0-20250228 (ESWIN 官方支持)
  - 下载链接：<https://github.com/eswincomputing/eic7x-images/releases/tag/Debian-v1.0.0-20250228>
  - 参考安装文档：<https://github.com/eswincomputing/eic7x-images/releases/download/Yocto-v1.0.0-20241021/EIC7700_Debian_Yocto_Ubuntu_System_Burnning_Guide.pdf>
- Yocto - 2024.11.00-HFP550 (SiFive 官方支持)
  - 下载链接：<https://github.com/sifiveinc/freedom-u-sdk/releases/tag/2024.11.00-HFP550>
  - 参考安装文档：<https://www.sifive.com/document-file/hifive-premier-p550-image-update-procedure>

## 测试结果

| 软件类别             | 包名称       | 测试结果 (测试报告)    |
|---------------------|--------------|----------------------|
| Ubuntu LTS 镜像启动  | N/A          | [CFT][Ubuntu LTS]    |
| Debian 镜像启动      | N/A          | [CFT][Debian]        |
| Yocto 镜像启动       | N/A          | [CFT][Yocto]         |

[Ubuntu LTS]: ./Ubuntu/README_LTS_zh.md
[Debian]: ./Debian/README_zh.md
[Yocto]: ./Yocto/README_zh.md
