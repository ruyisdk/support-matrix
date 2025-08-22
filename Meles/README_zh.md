# Milk-V Meles

## 概述

Milk-V Meles 是一款基于 TH1520 的信用卡大小的单板计算机（SBC）。它拥有四个 RISC-V 64GCV C910 核心，最高可运行频率1.85GHz。Meles 包含了丰富的接口和强大的计算和人工智能能力，是爱好者、工业制造商、工程师、教师和学生的理想 RISC-V 智能硬件平台。

## 硬件规格

- **处理器**：TH1520（4xC910@1.85G，RV64GCV，4TOPS@int8 NPU，50GFLOP GPU）  
  - **CPU**：RISC-V 64GCV C910 × 4 @ 1.85GHz  
    - 每个核心包含 64KB I Cache 和 64KB D Cache
    - 1MB 共享 L2 缓存  
    - 支持 TEE 和 REE，在核心启动时进行配置  
    - 支持自定义及 RISC-V 兼容接口的多核调试框架  
    - 独立电源域，支持动态电压频率调节（DVFS）  
  - **GPU**：  
    - OpenCL 1.1/1.2/2.0  
    - OpenGL ES 3.0/3.1/3.2  
    - Vulkan 1.1/1.2  
    - Android NN HAL  
  - **NPU**：支持 4TOPS@INT8，最高频率 1GHz  
    - 支持 TensorFlow、ONNX、Caffe  
    - 支持 CNN、RNN、DNN  
  - **视频解码**：实时解码器，支持 H.265/H.264/VP9/8/7/6/AVS/AVS+/AVS2.0/VC1/MPEG4  
    - 支持 H.264 BP/MP/HP@level 5.1 解码，最高支持 4K 分辨率  
    - 支持 H.265/HEVC Main Profile@level 5.1 解码，最高支持 4K 分辨率  
    - 支持 VP9 Profile-2 解码，最高支持 4K 分辨率  
    - 支持 AVS2.0 解码，最高支持 4K 分辨率  
    - 支持 VP6/7/8/AVS/AVS+/VC1/MPEG4 解码，最高支持 1920x1080 分辨率  
    - 最高支持 4K@75fps 解码  
  - **视频编码**：  
    - 支持 H.264 BP/MP/HP@level4.2 编码，最高支持 4K 分辨率  
    - 支持 H.265/HEVC Main Profile 编码，最高支持 4K 分辨率  
    - 仅支持 I-frames and P-frames 
    - 最高支持 4K@40fps 编码  
- **内存**：8GB / 16GB LPDDR4X，4266 MT/s  
- **存储**：  
  - 1x eMMC 插槽  
  - 1x MicroSD 插槽  
- **显示**：  
  - 1x HDMI 2.0，支持最高 4K@60FPS  
  - 1x MIPI DSI 4-lanes,，支持触摸屏  
- **音频**：  
  - 1x HDMI 2.0 带音频输出
  - 1x I2S 接口，支持音频输入和输出  
  - 1x 3.5mm 音频输出接口  
- **摄像头**：  
  - 1x 4-lanes MIPI CSI 输入
  - 1x 2-lanes MIPI CSI 输入
- **USB**：  
  - 4x 主机 USB3.0 接口  
  - 1x 从机 USB2.0（Type-C）接口  
- **以太网**：10/100/1000 Mbps RJ45 端口  
- **无线**：AP6256（WI-FI 5 / BT 5.2）  
- **GPIO**：40 针 GPIO 接头，最多支持 3x UART、2x I2C、1x SPI、1x I2S、1x ADC、8x GPIO、1x C910 调试端口  
- **按键**：
  - 1x 复位按键 (Reset)
  - 1x 恢复按键 (Recovery)
  - 1x eMMC / SPI 启动模式切换按键
- **LED**：  
  - 1x 电源 LED
  - 1x 用户 LED
- **电源**：USB Type-C  
- **其他**：1x 2Pin 风扇接口