# Lichee Pi 3A

## 总览

Lichee Pi 3A 是一款基于核心计算板 LM3A 的 RISC-V Linux 开发板，配备了 K1 RISC-V 处理器、8GB/16GB LPDDR4X 内存和 64GB/128GB eMMC 存储。
它具有多种接口，具体如下：
| 类型   | 描述                                         |
| ------ | -------------------------------------------- |
| 以太网 | 2 x 1000M 以太网（可选 POE）                 |
| USB    | 4 x USB3.2 Gen1, 2 x USB2.0                  |
| PCIe   | 1 x PCIE Gen2x1, 2 x M.2 M Key (PCIe Gen2x2) |
| 音频   | 1 x 3.5mm 音频接口, 扬声器                   |
| 显示   | 1 x HDMI 1.4, 1 x MIPI DSI 4-lan             |
| 摄像头 | 1 x MIPI CSI 2-lan, 1 x MIPI CSI 4-lan       |
| GPIO   | 标准 20-pin GPIO                             |
它可以通过标准 PD 充电器供电，也支持 DC 12v 电源供电。

## 支持的操作系统

- Bianbu v2.2-minimal
  - 下载链接：https://archive.spacemit.com/image/k1/version/bianbu/v2.2/
  - 参考安装文档：https://wiki.sipeed.com/hardware/zh/lichee/K1/lpi3a/1_intro.html
- Fedora Minimal 41 (来自 Fedora V Force)
  - 下载链接: https://mirror.iscas.ac.cn/fedora-riscv/dl/SpacemiT/K1_M1/images/latest/k1-fedora-minimal.img.gz
  - 参考安装文档: https://wiki.sipeed.com/hardware/zh/lichee/K1/lpi3a/1_intro.html
- Fedora Xfce Desktop 41 (来自 Fedora V Force)
  - 下载链接: https://mirror.iscas.ac.cn/fedora-riscv/dl/SpacemiT/K1_M1/images/latest/k1-fedora-multi-desktops.img.gz
  - 参考安装文档: https://wiki.sipeed.com/hardware/zh/lichee/K1/lpi3a/1_intro.html
- openKylin v2.0 SP1
  - 下载链接：[https://www.openkylin.top/downloads/index-cn.html](https://www.openkylin.top/downloads/index-cn.html) **选择 k1 镜像**
  - 参考安装文档：[https://docs.openkylin.top/zh/01_%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7%E6%8C%87%E5%8D%97/%E5%9C%A8riscv%E4%B8%8A%E5%AE%89%E8%A3%85/%E5%9C%A8SpacemiT_K1%E4%B8%8A%E5%AE%89%E8%A3%85openKylin](https://docs.openkylin.top/zh/01_%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7%E6%8C%87%E5%8D%97/%E5%9C%A8riscv%E4%B8%8A%E5%AE%89%E8%A3%85/%E5%9C%A8SpacemiT_K1%E4%B8%8A%E5%AE%89%E8%A3%85openKylin)


## 测试结果

| 软件类别       | 包名称                 | 测试结果 (测试报告)        |
| -------------- | ---------------------- | -------------------------- |
| Bianbu         | minimal                | [CFH][bianbu-minimal]      |
| Fedora         | fedora v force         | [Basic][fedora-fvf]        |
| Fedora desktop | fedora v force desktop | [Good][fedora-fvf_desktop] |
| openKylin      | N/A                    | [Good][openkylin]          |

[bianbu-minimal]: ./Bianbu/README_zh.md
[fedora-fvf]: ./Fedora/README_zh.md
[fedora-fvf_desktop]: ./Fedora/README_desktop_zh.md
[openkylin]: ./openKylin/README_zh.md