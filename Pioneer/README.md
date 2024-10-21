---
product: Pioneer Box
cpu: SG2042
cpu_core: XuanTie C920
---


# Milk-V Pioneer

## Test Environment

### Operating System Information

- openEuler RISC-V 24.03 LTS
    - Download link: https://www.openeuler.org/en/download/archive/detail/?version=openEuler%2024.03%20LTS
    - Reference Installation Document: https://docs.openeuler.org/en/docs/24.03_LTS/docs/Installation/RISC-V-Pioneer1.3.html
- RevyOS 20240119
    - Download link: https://mirror.iscas.ac.cn/revyos/extra/images/sg2042/
    - Reference Installation Document: https://revyos.github.io/docs/
- Fedora 38
    - Download link: https://milkv.io/docs/pioneer/getting-started/download
    - Reference Installation Document: https://milkv.io/zh/docs/pioneer/getting-started/InstallOS
- openKylin 2.0 alpha RISC-V
    - Download link: https://www.openkylin.top/downloads
    - Reference Installation Document: https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin
- Deepin 23 preview-20240517
    - Download link: 
        - OS image: https://cdimage.deepin.com/RISC-V/preview-20240517-riscv64/deepin-sg2042-riscv64-stable-desktop-installer.tar.xz
        - Firmware: https://cdimage.deepin.com/RISC-V/preview-20240517-riscv64/sophgo-bootloader-multi-sg2042-dev.zip
    - Reference installation manual: https://cdimage.deepin.com/RISC-V/preview-20240517-riscv64/README.md

### Hardware Information

- Milk-V Pioneer (v1.3)

## Test Results

| Software Category              | Package Name | Test Results (Test Report)                                   |
| ------------------------------ | ------------ | ------------------------------------------------------------ |
| openEuler (Image, Legacy Boot) | N/A          | [Success][oERV] (Official support)                           |
| RevyOS Image Boot              | N/A          | [Success][RevyOS] (Official support)                         |
| openKylin Image Boot           | N/A          | [Success][oK] (Official support)                             |
| Fedora Image Boot              | N/A          | [Success][Fedora] (Official support & Factory pre-installed) |
| Deepin                         | N/A          | [Success][Deepin], CLI only                                  |

[oERV]: ./openEuler/README.md
[RevyOS]: ./RevyOS/README.md
[oK]: ./openKylin/README.md
[Fedora]: ./Fedora/README.md
[Deepin]: ./Deepin/README.md
