---
vendor: sipeed-lpi4a
product: LicheePi 4A
cpu: TH1520
cpu_core: XuanTie C910 + XuanTie C906 + XuanTie E902
ram: 8G
board_variants: [ 8g ]
---

# Lichee Pi 4A

## Testing Environment

### System Information

- openEuler 24.03 LTS SP1
    - Download Link：https://mirrors.tuna.tsinghua.edu.cn/openeuler/openEuler-24.03-LTS-SP1/embedded_img/riscv64/lpi4a/
    - Reference Installation Document：https://docs.openeuler.org/zh/docs/24.03_LTS_SP1/docs/Installation/RISC-V-LicheePi4A.html
- openEuler RISC-V 25.03
    - Download Link: https://repo.openeuler.org/openEuler-25.03/embedded_img/riscv64/lpi4a/
    - Reference Installation Document: https://docs.openeuler.org/en/docs/24.03_LTS/docs/Installation/RISC-V-LicheePi4A.html
- openKylin 2.0 SP1
    - Download Link：https://www.openkylin.top/downloads/index-cn.html
    - Reference Installation Document：https://docs.openkylin.top/zh/01_%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7%E6%8C%87%E5%8D%97/%E5%9C%A8riscv%E4%B8%8A%E5%AE%89%E8%A3%85/%E5%9C%A8LicheePi4A%E4%B8%8A%E5%AE%89%E8%A3%85openKylin
- Fedora 38
    - Download Link：https://github.com/chainsx/fedora-riscv-builder/releases
    - Reference Installation Document：https://wiki.sipeed.com/hardware/zh/lichee/th1520/lpi4a/4_burn_image.html
- OpenWRT
    - Download Link：https://github.com/chainsx/openwrt-th1520/releases
    - Reference Installation Document：https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide_ch.md
- Deepin 25-beige-preview 20250122
    - Download Link：https://deepin-community.github.io/sig-deepin-ports/images/riscv/download
    - Reference Installation Document：https://cdimage.deepin.com/RISC-V/preview-20240517-riscv64/README.md
- RevyOS 20250323
    - Download Link: https://fast-mirror.isrc.ac.cn/revyos/extra/images/lpi4a/20250323/
    - Reference Installation Document: https://revyos.github.io/docs/

### Hardware Information

- Lichee Pi 4A 8GB RAM + 32GB eMMC

## Test Results

| Software Category                 | Software Package | Test Results (Test Report)              |
|-----------------------------------|------------------|-----------------------------------------|
| openEuler/Base Image Boot         | N/A              | [Success][oERV]                         |
| openEuler/Xfce Image Boot         | Xfce             | [Success][oERV]                         |
| openEuler Innovation Image Boot   | N/A              | [Success][openEuler]                    |
| Fedora chainsx Desktop Image Boot | N/A              | [Success][Fedora]                       |
| openKylin Desktop Image Boot      | N/A              | [Success][openKylin] (Official Support) |
| OpenWRT Image Boot                | N/A              | [Success][OpenWRT]                      |
| Deepin Desktop Image Boot         | N/A              | [Success][Deepin]                       |
| RevyOS Desktop Image Boot         | N/A              | [Success][RevyOS]                       |

[oERV]: ./openEuler/README.md
[openEuler]: ./openEuler/Innovation.md
[Fedora]: ./Fedora/README_chainsx.md
[openKylin]: ./openKylin/README.md
[OpenWRT]: ./OpenWRT/README.md
[Deepin]: ./Deepin/README.md
[RevyOS]: ./RevyOS/README.md
