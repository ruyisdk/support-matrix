---
product: Lichee Cluster 4A
cpu: TH1520
cpu_core: XuanTie C910 + XuanTie C906 + XuanTie E902
ram: 8G/16G
vendor: Sipeed
---

# Lichee Cluster 4A

## Overview

Lichee Cluster 4A (hereinafter referred to as LC4A) is a high-performance RISC-V cluster computing platform developed by SiliconSpeed Technology. It can be used to build multi-node computing clusters, and can also learn Kubernetes, automation, edge artificial intelligence computing, local mini servers, and hosted applications. Excellent tool for programs, containers, etc. A single Lichee Cluster 4A can be equipped with up to 7 LM4A core boards. Each LM4A core board contains an NPU with 4TOPS@int8 AI computing power. A single core board supports up to 16GB LPDDR4X memory and 128G eMMC storage. The entire cluster has strong flexibility and reliability. Scalability.

Lichee Cluster 4A has an onboard eight-port Gigabit switch to provide high-speed connections and easily connect multiple nodes to form a powerful computing cluster. It also supports USB3.0 and SD card storage expansion, making it easy to expand additional storage or add peripherals. equipment.

Lichee Cluster 4A also comes with BMC (out-of-band management), which independently connects the system serial port and reset pin of each LM4A. BMC can reset a single computing node from the hardware, and can also execute commands through the serial port, such as executing ser2net or kermit to manage slots.

## Technical specifications

- **Supported core boards**: LM4A x 7
- **CPU**: RISC-V C910@1.85GHz x 4 x 7
- **GPU**: IMG™ B Series BXM-4-64 x 7
- **NPU**: 4TOPS@INT8 x 7
- **RAM**: Max 16GB x 7
- **EMMC**: Max 128GB x 7
- **BMC**: SIPEED Lichee RV
- **Power**: management	Sipeed M0 Sense
- **Ethernet**:
  - Gigabit Ethernet 1 (Slot#1)
  - Gigabit Ethernet 2 (Switch)
  - 100 Mbit Ethernet (BMC)
- **USB**: 
  - USB3.0 x 7 (LM4A)
  - USB2.0 x 1 (BMC)
- **HDMI**: HDMI x 1 (Slot 1)
- **SDCARD**: TF x 7
- **Power support**:
  - Supports DC port DC power supply
  - Supports ATX 24PIN power supply
- **RTC power supply**: CR2032 button battery
- **Heat dissipation**: 
  - 5V PWM fan interface x 7
  - 12V 4PIN PWM fan interface x 1
- **Dimensions**:
  - Mini ITX, 17 x 17 cm (6.7 x 6.7 inch)
  - Optional MINI ITX chassis, 20 x 12 x 22 cm