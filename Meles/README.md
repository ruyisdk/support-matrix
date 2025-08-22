---
vendor: Milk-V
product: Milk-V Meles
cpu: TH1520
cpu_core: XuanTie C910 + XuanTie C906 + XuanTie E902
ram: 8G/16G
---

# Milk-V Meles

## Overview

Milk-V Meles is a credit card-sized, single-board computer (SBC) based on the TH1520. It is powered by a Quad Core RISC-V 64GCV C910, capable of running up to 1.85GHz. This SBC is packed with rich interfaces and boasts powerful computing and AI capabilities, making it an ideal RISC-V intelligent hardware platform for hobbyists, makers, engineers, teachers, and students.

## Hardware Specifications

- **Processor**: TH1520(4xC910@1.85G, RV64GCV, 4TOPS@int8 NPU, 50GFLOP GPU)
  - CPU: RISC-V 64GCV C910*4@1.85GHz
    - Each core contains 64KB I cache amd 64KB D Cache
    - 1MB of Shared L2 Cache
    - Support TEE and REE, configured during core booting
    - Support multi-core debugging framework of custom and RISC-V compatible interface
    - Independent power domain, supports DVFS
  - GPU:
    - OpenCL 1.1/1.2/2.0
    - OpenGL ES 3.0/3.1/3.2
    - Vulkan 1.1/1.2
    - Android NN HAL
  - NPU: Support 4TOPS@INT8, up to 1GHz
    - Support TensorFlow、ONNX、Caffe
    - Support CNN、RNN、DNN
  - Decode: Real-time decoder, support H.265/H.264/VP9/8/7/6/AVS/AVS+/AVS2.0/VC1/MPEG4
    - Supports H.264 BP/MP/HP@level 5.1 decoding, up to 4K resolution
    - Supports H.265/HEVC Main Profile@level 5.1 decoding, up to 4K resolution
    - Supports VP9 Profile-2 decoding, up to 4K resolution
    - Supports AVS2.0 decoding, up to 4K resolution
    - Supports VP6/7/8/AVS/AVS+/VC1/MPEG4 decoding, up to 1920x1080 resolution
    - Decoding at 4K@75fps maximum
  - Encode:
    - Supports H.264 BP/MP/HP@level4.2 encoding, up to 4K resolution
    - Supports H.265/HEVC Main Profile encoding, up to 4K resolution
    - Only supports I-frames and P-frames
    - Encoding at 4K@40fps maximum
- **Memory**: 8/16GB LPDDR4X, 4266 MT/s
- **storage**:
  - 1x eMMC Slot
  - 1x MicroSD Slot
- **Display**:
  - 1x HDMI 2.0, up to 4K@60FPS
  - 1x MIPI DSI 4-lanes, support touch screen
- **Audio**:
  - 1x HDMI 2.0 with audio output
  - 1x I2S, support audio input and output
  - 1x 3.5mm jack for audio output
- **Camera**:
  - 1x 4-lanes MIPI CSI input
  - 1x 2-lanes MIPI CSI input
- **USB**:
  - 4x USB3.0 HOST
  - 1x USB2.0 Device (Type-C)
- **Ethernet**: 10/100/1000 Mbps RJ45 Port
- **Wireless**:	AP6256 (WI-FI 5 / BT 5.2)
- **GPIO**:	40 Pin GPIO Header, up to 3xUART, 2xI2C, 1xSPI, 1xI2S,1xADC, 8xGPIO, 1xC910 debug port
- **Key**:
  - 1x Key for reset
  - 1x Key for recovery
  - 1x Key for eMMC / SPI flash bootmode swich
- **LED**:
  - 1x Power LED
  - 1x User LED
- **Power**: USB Type-C
- **Other**: 1x 2Pin for Fan