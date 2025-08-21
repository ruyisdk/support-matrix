# Lichee Pi 4A

## 概述

Lichee Pi 4A（简称 LPi4A）是一款基于平头哥 TH1520 处理器的单板计算机。它包含一个四核 RISC-V 64GCV 指令集架构的 C910 处理器，主频为 1.85GHz；支持 4TOPS@INT8 的NPU；支持 4K@30fps 的显示输出及多种音视频编解码；配备双千兆以太网和 USB3.0 接口；并使用单核 C906 实现音频处理功能。

## 硬件规格
- **处理器**：TH1520（4×C910@1.85GHz，RV64GCV，4TOPS@INT8 NPU，50GFLOP GPU）
  - **CPU**：RISC-V 64GCV C910 × 4 @ 1.85GHz
    - 每个核心包含 64KB I-Cache 和 64KB D-Cache
    - 共享 1MB L2 缓存
    - 支持 TEE（可信执行环境）和 REE（富执行环境），在核心启动时配置
    - 支持自定义及 RISC-V 兼容的多核调试框架
    - 独立电源域，支持动态电压频率调节（DVFS）
  - **GPU**：
    - 支持 OpenCL 1.1/1.2/2.0
    - 支持 OpenGL ES 3.0/3.1/3.2
    - 支持 Vulkan 1.1/1.2
    - 支持 Android NN HAL
  - **NPU**：支持 4TOPS@INT8，最高频率 1GHz
    - 支持 TensorFlow、ONNX、Caffe 等框架
    - 支持 CNN、RNN、DNN 等神经网络模型
  - **视频解码**：实时解码器，支持 H.265/H.264/VP9/VP8/VP7/VP6/AVS/AVS+/AVS2.0/VC1/MPEG4
    - 支持 H.264 BP/MP/HP@Level 5.1 解码，最高分辨率 4K
    - 支持 H.265/HEVC Main Profile@Level 5.1 解码，最高分辨率 4K
    - 支持 VP9 Profile-2 解码，最高分辨率 4K
    - 支持 AVS2.0 解码，最高分辨率 4K
    - 支持 VP6/VP7/VP8/AVS/AVS+/VC1/MPEG4 解码，最高分辨率 1920×1080
    - 最大解码能力为 4K@75fps
  - **视频编码**：
    - 支持 H.264 BP/MP/HP@Level 4.2 编码，最高分辨率 4K
    - 支持 H.265/HEVC Main Profile 编码，最高分辨率 4K
    - 仅支持 I 帧和 P 帧
    - 最大编码能力为 4K@40fps
- **内存**：8/16GB 64bits LPDDR4X-3733
- **存储**：
  - eMMC（可选）：无、8GB、32GB、128GB
  - 支持 TF 卡扩展
- **网络接口**：
  - 双千兆以太网接口，支持可选 PoE 供电
- **Wi-Fi / 蓝牙**：RTL8723DS，支持 802.11b/g/n，1x1 MIMO，蓝牙 4.2
- **USB 接口**：
  - 4 个 USB 3.0 Type-A 接口
  - 1 个 USB 2.0 Type-C 接口（用于供电或刷写系统）
- **音频**：
  - 1 个 3.5mm 立体声接口
  - 1 个音频接口
  - 板载两个麦克风
- **显示输出**：
  - 1 个 HDMI 2.0 接口
  - 1 个 4通道 MIPI DSI 接口
- **摄像头接口**：
  - 2 个 2通道 MIPI CSI 接口
  - 1 个 4通道 MIPI CSI 接口
- **GPIO 引脚**：2×10 针 GPIO 接口
  - 包含 3 个 UART、1 个 I2C、1 个 SPI
  - 提供 1 个 5V、1 个 3.3V、2 个 GND 引脚
  - 其他扩展引脚
- **供电方式**：DC 5.5mm 接口、USB-C 接口、PoE（外部供电）
- **尺寸**：99 × 84.5 mm