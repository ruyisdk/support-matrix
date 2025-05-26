---
vendor: sifive
product: SiFive HiFive Premier P550
cpu: EIC7700X
cpu_core: SiFive P550
---

# SiFive HiFive Premier P550

## Overview

From the data sheet:
> The HF106 is a RISC-V platform board with carrier board + SOM, using ESWIN-developed EIC7700X SOC. The HF106 features 16GB/32GB of 64-bit LPDDR5 memory up to 6400MHz and 128GB eMMC memory. High- speed interconnect with PCIE Gen3, and external connectors with Gigabit Ethernet and USB3.2 Gen1. Supports storage expansion with SATA and Micro SD Card.

## Hardware Specifications
- **Processor**: EIC7700X
- **Memory**: 16 / 32 GB
- **Storage**: 128GB Samsung eMMC

### Technical Information

#### Internal Connections

- 1x 4-lane PCIe Connector (x16 form factor)
- 1x 4-Pin SOM Fan Header (PWM Controlled 5V Supply)
- 2x 4-Pin System Fan Header (PWM Controlled / 12V Supply)
- 1x Battery Holder for Real-Time Clock
- 1x 24-Pin ATX Power Measurement Header
- 1x 40-Pin GPIOS Header
- 1x SATA connector
- 1x 10-Pin JTAG Header
- 1x M.2 Key E Connector (Wi-Fi)
- 1x Header (Connected to Mini-DTX Case Front Panel I/O).
- 1x Header (Connected to Type-A in front panel)
- 1x Header (Connected to Audio Jacks in front panel)
- 1x Type-E Connector for Mini-DTX Case Front Panel Type-C connector Support

#### External Connections 
- 1x Micro SD Card in the rear
- 2x Gigabit Ethernet RJ45 Connectors in the rear
- 1x 10/100Mbps RJ45 Connector in the rear
- 1x HDMI Connector in the rear
- 2x USB 3.2 Gen1 Type-A Connectors in the rear
- 1x Audio Jack connector in the rear
- 1x USB Type-C (JTAG/UART over FT4232H) in the rear

#### Power
- Type 24Pin ATX Power Connector, and Optional DC12V/5A Adaptor

## Supported Operating Systems
- Deeepin - 25

## Test Results
| Software Category | Package Name | Test Results |
|-------------------|--------------|--------------|
| Deepin            | RuyiSDK      | Success      |
