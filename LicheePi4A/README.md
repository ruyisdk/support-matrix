---
product: Lichee Pi 4A
cpu: TH1520
cpu_core: XuanTie C910 + XuanTie C906 + XuanTie E902
ram: 8G/16G
vendor: Sipeed
---

# Lichee Pi 4A

## Overview

The Lichee Pi 4 A (LPi4A) is a single board computer powered by the Pinto TH1520 processor. It includes a quad-core RISC-V 64GCV instruction set architecture C910@1.85GHz; NPU support of 4TOPS@INT8 algorith; display output support of
4K@30fps resolution and multiple simultaneous audio and video encoding and decoding; dual Gigabit Ethernet and USB3.0 support; and audio processing using a single core C906.

## Hardware Specifications

- **Processor**: TH1520(4xC910@1.85G, RV64GCV, 4TOPS@int8 NPU, 50GFLOP GPU)
  - **CPU**: RISC-V 64GCV C910*4@1.85GHz
    - Each core contains 64KB I cache amd 64KB D Cache
    - 1MB of Shared L2 Cache
    - Support TEE and REE, configured during core booting
    - Support multi-core debugging framework of custom and RISC-V compatible interface
    - Independent power domain, supports DVFS
  - **GPU**:
    - OpenCL 1.1/1.2/2.0
    - OpenGL ES 3.0/3.1/3.2
    - Vulkan 1.1/1.2
    - Android NN HAL
  - **NPU**: Support 4TOPS@INT8, up to 1GHz
    - Support TensorFlow、ONNX、Caffe
    - Support CNN、RNN、DNN
  - **Decode**: Real-time decoder, support H.265/H.264/VP9/8/7/6/AVS/AVS+/AVS2.0/VC1/MPEG4
    - Supports H.264 BP/MP/HP@level 5.1 decoding, up to 4K resolution
    - Supports H.265/HEVC Main Profile@level 5.1 decoding, up to 4K resolution
    - Supports VP9 Profile-2 decoding, up to 4K resolution
    - Supports AVS2.0 decoding, up to 4K resolution
    - Supports VP6/7/8/AVS/AVS+/VC1/MPEG4 decoding, up to 1920x1080 resolution
    - Decoding at 4K@75fps maximum
  - **Encode**:
    - Supports H.264 BP/MP/HP@level4.2 encoding, up to 4K resolution
    - Supports H.265/HEVC Main Profile encoding, up to 4K resolution
    - Only supports I-frames and P-frames
    - Encoding at 4K@40fps maximum
- **Memory**: 8/16GB 64bits LPDDR4X-3733
- **storage**:
  - eMMC(Optional): None, 8G, 32G, 128G
  - Support TF card
- **Ethernet**: 2 x Gigabit Ethernet interfaces, Optional POE
- **Wi-Fi/Bluetooth**: RTL8723DS, 802.11b/g/n, 1x1 MIMO, BT4.2
- **USB**: 
  - 4 x USB Type-A 3.0
  - 1 x USB Type-C 2.0(For power supply or flashing OS)
- **Audio**: 
  - 1 x 3.5mm stereo interface
  - One audio interface
  - Two onboard microphones
- **Display**:
  - 1 x HDMI2.0
  - 1 x 4-lane MIPI DSI
- **Camera**:
  - 2 x 2-lane MIPI CSI
  - 1 x 4-lane MIPI CSI
- **GPIO**: 2x10 Pin GPIO
  - 3 x UART, 1 x IIC, 1 x SPI
  - 1 x 5V, 1 x 3.3V, 2 x GND
  - Others
- **Power**: DC5.5, USB-C, PoE(external)
- **Size**: 99 x 84.5 mm