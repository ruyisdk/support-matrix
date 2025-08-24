# Lichee Cluster 4A

## 概述

Lichee Cluster 4A (以下简称 LC4A) 是矽速科技研发的高性能 RISC-V 集群计算平台，可以用于构建多节点计算集群，而且还是学习 Kubernetes、自动化、边缘人工智能计算、本地迷你服务器，托管应用程序、容器等的优秀工具。单个 Lichee Cluster 4A 最多可装配 7 个 LM4A 核心板，每个 LM4A 核心板含有 4TOPS@int8 AI 算力的 NPU，单核心板最大支持 16GB LPDDR4X 内存和 128G eMMC 存储，整个集群有强大的灵活性和可扩展性。

Lichee Cluster 4A 板载八口千兆交换机以提供高速连接，轻松将多个节点连接起来，组成强大的计算集群，还支持 USB3.0 和 SD 卡存储扩展，能够轻松地将扩展额外存储或者增加外围设备。

Lichee Cluster 4A 还带有 BMC (带外管理)，BMC 独立连接了每个 LM4A 的系统串口和复位引脚。BMC 可以从硬件上复位单个计算节点，还可以通过串口执行命令,比如执行 ser2net 或 kermit 来管理 Slot。

## 技术规格
- **支持的核心板**: LM4A x 7
- **CPU**: RISC-V C910@1.85GHz x 4 x 7
- **GPU**: IMG™ B 系列 BXM-4-64 x 7
- **NPU**: 4TOPS@INT8 x 7
- **RAM**: 最大 16GB x 7
- **EMMC**:	最大 128GB x 7
- **BMC**: SIPEED Lichee RV
- **电源管理**: Sipeed M0 Sense
- **Ethernet**:
  - 千兆以太网1(Slot#1)
  - 千兆以太网2(交换机)
  - 百兆以太网(BMC)
- **USB**:
  - USB3.0 x 7 (LM4A)
  - USB2.0 x 1 (BMC)
- **HDMI**: HDMI x 1 (Slot 1)
- **SDCARD**:	TF x 7
- **电源支持**:	
  - 支持 DC 口直流电源供电
  - 支持 ATX 24PIN 电源
- **RTC 供电**: CR2032 纽扣电池
- **散热**: 
  - 5V PWM 风扇接口 x 7
  - 12V 4PIN PWM 风扇接口 x 1
- **尺寸**:
  - Mini ITX, 17 x 17 cm (6.7 x 6.7 inch)
  - 可选配 MINI ITX 机箱, 20 x 12 x 22 cm
