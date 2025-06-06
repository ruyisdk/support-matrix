---
product: Lichee Pi 3A
cpu: Key Stone K1
cpu_core: SpacemiT X60
ram: LPDDR4X 8G/16G

vendor: spacemit-lpi3a
board_variant: [
    generic
]
cpu_arch: [
    spacemit-x60,
]
---

# Lichee Pi 3A

## Overview

Lichee Pi 3A is a RISC-V Linux development board based on core compute board LM3A, which is equipped with a K1 RISC-V processor, 8GB/16GB LPDDR4X memory, and 64GB/128GB eMMC storage. 

It has a variety of interfaces as follows:

| Type     | Description                                  |
| -------- | -------------------------------------------- |
| Ethernet | 2 x 1000M Ethernet (POE Optional)            |
| USB      | 4 x USB3.2 Gen1, 2 x USB2.0                  |
| PCIe     | 1 x PCIE Gen2x1, 2 x M.2 M Key (PCIe Gen2x2) |
| Audio    | 1 x 3.5mm Audio Jack, Speaker                |
| Display  | 1 x HDMI 1.4, 1 x MIPI DSI 4-lan             |
| Camera   | 1 x MIPI CSI 2-lan, 1 x MIPI CSI 4-lan       |
| GPIO     | standard 20-pin GPIO                         |

It can be powered by a standard PD charger, or a DC power supply is also supported.

## Supported Operating Systems

- Bianbu v2.2-minimal
  - Download Links: https://archive.spacemit.com/image/k1/version/bianbu/v2.2/
  - Reference Installation Document: https://wiki.sipeed.com/hardware/en/lichee/K1/lpi3a/1_intro.html
- Fedora Minimal 41 (From Fedora V Force)
  - Download Links: https://mirror.iscas.ac.cn/fedora-riscv/dl/SpacemiT/K1_M1/images/latest/k1-fedora-minimal.img.gz
  - Reference Installation Document: https://wiki.sipeed.com/hardware/en/lichee/K1/lpi3a/1_intro.html
- Fedora Xfce Desktop 41 (From Fedora V Force)
  - Download Links: https://mirror.iscas.ac.cn/fedora-riscv/dl/SpacemiT/K1_M1/images/latest/k1-fedora-multi-desktops.img.gz
  - Reference Installation Document: https://wiki.sipeed.com/hardware/en/lichee/K1/lpi3a/1_intro.html
- openKylin v2.0 SP1
  - Download Link: [https://www.openkylin.top/downloads/index.html](https://www.openkylin.top/downloads/index.html) **Choose k1 version**
  - Reference Installation Document: [https://docs.openkylin.top/en/01_%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7%E6%8C%87%E5%8D%97/%E5%9C%A8riscv%E4%B8%8A%E5%AE%89%E8%A3%85/%E5%9C%A8SpacemiT_K1%E4%B8%8A%E5%AE%89%E8%A3%85openKylin](https://docs.openkylin.top/en/01_%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7%E6%8C%87%E5%8D%97/%E5%9C%A8riscv%E4%B8%8A%E5%AE%89%E8%A3%85/%E5%9C%A8SpacemiT_K1%E4%B8%8A%E5%AE%89%E8%A3%85openKylin)

## Test Results

| Software Category | Package Name           | Test Results (Test Report) |
| ----------------- | ---------------------- | -------------------------- |
| Bianbu            | minimal                | [CFH][bianbu-minimal]      |
| Fedora minimal    | fedora v force         | [Basic][fedora-fvf]        |
| Fedora desktop    | fedora v force desktop | [Good][fedora-fvf_desktop] |
| openKylin         | N/A                    | [Good][openkylin]          |

[bianbu-minimal]: ./Bianbu/README.md
[fedora-fvf]: ./Fedora/README.md
[fedora-fvf_desktop]: ./Fedora/README_desktop.md
[openkylin]: ./openKylin/README.md