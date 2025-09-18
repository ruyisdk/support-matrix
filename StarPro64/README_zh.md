# StarPro64

参考文档：https://pine64.org/documentation/StarPro64/

## 概述

StarPro64是PINE64制造的RISC-V架构的单板计算机，拥有1.8GHz的EIC7700X SoC以及19.95 TOPS的NPU性能。它保持了和model-A相同的形态，与Star64相似，拥有两个有线网口、HDMI输出、USB2.0和3.0接口、全功能GPIO和4x PCIE插槽。

## 硬件规格
- **处理器**: ESWIN EIC7700X
- **内存**: 8GB / 16GB / 32GB LPDDR5
- **存储**: 
  - 板载 128Mbit (16MByte) XSPI NOR 闪存 - 可启动
  - microSD - 可启动, 支持 SDHC 和 SDXC ，支持最大存储 256GB
  - eMMC - 可启动 (可选的 eMMC 模块)
- **接口**: 
  - 4通道 PCIe Gen3
  - 2×20 针脚 “Pi2” GPIO 接头
  - 4通道 MiPi DSI 接口，为 LCD 显示器设计
  - 4通道 MiPi CSI 接口，为相机模块设计
  - 2个 USB3.0 专用主机连接埠
  - 2个 USB2.0 共享主机连接埠
- **电源**: 12V DC

## 支持的操作系统
- deepin - 25

## 测试结果
| 软件类别         | 包名称       | 测试结果 (测试报告) |
|------------------|--------------|---------------------|
| deepin 镜像启动  | N/A          | 成功                |
