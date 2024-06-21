# Lichee Cluster 4A

## Test Environment

### System Information

- RevyOS (Sipeed Vendor Image)
    - Download link: [here](https://dl.sipeed.com/shareURL/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/bin)
    - Reference Installation Document: [here](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lc4a/lc4a.html)
- openEuler RISC-V 23.09 Preview
    - Download link: [here](https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/lpi4a/)
    - Reference Installation Document: [here](https://revyos.github.io/)
- RevyOS (w/mainline kernel)
    - Download link: [here](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4amain/20240127/)
    - Reference Installation Document: [here](https://revyos.github.io/)
- RevyOS
    - Download link: [here](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/)
    - Reference Installation Document: [here](https://docs.revyos.dev/)
- openKylin
    - Download link: [here](https://www.openkylin.top/downloads/index-cn.html)
    - Reference Installation Document: [here](https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin)
- Fedora
    - Download link: [here](https://openkoji.iscas.ac.cn/pub/dl/riscv/T-Head/th1520_light/images/)
    - Reference Installation Document: [here](https://fedoraproject.org/wiki/Architectures/RISC-V/T-Head)
- Armbian
    - Download link: [here](https://github.com/chainsx/armbian-riscv-build/tree/main)
    - Reference Installation Document: [here](https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide.md)
- OpenWRT
    - Download link: [here](https://github.com/chainsx/openwrt-th1520/releases)
    - Reference Installation Document: [here](https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide.md)

### Board Information

- Lichee Cluster 4A + 7 * LM4A 8GB RAM

## Test Results


| Software Category                | Package Name | Test Results (Test Report)                     |
| -------------------------------- | ------------ | ---------------------------------------------- |
| RevyOS (Sipeed Manufacturer Image)| N/A          | [Success][RevySipeed] (Sipeed Manufacturer Image)|
| RevyOS (LPi4a Image) Image Boot  | N/A          | [Success][RevyLPi]                             |
| RevyOS (mainline Image) Image Boot| N/A         | [Success][RevyOS] (Official Support)           |
| openEuler/Base Image Boot        | N/A          | [Success][oERV]                                |
| openEuler/Xfce Image Boot        | Xfce         | [Success][oERV]                                |
| openKylin Image Boot             | N/A          | [Success][oK]                                  |
| Fedora Desktop Image Boot        | N/A          | [Success][Fedora]                              |
| Armbian Image Boot               | N/A          | [Success][Armbian]                             |
| OpenWRT Image Boot               | N/A          | [Success][OpenWRT]                             |

[RevySipeed]: ./RevyOS/README_Sipeed.md
[RevyLPi]: ./RevyOS/README_lpi4a.md
[RevyOS]: ./RevyOS/README.md
[oERV]: ./openEuler/README.md
[oK]: ./openKylin/README.md
[Fedora]: ./Fedora/README.md
[Armbian]: ./Armbian/README.md
[OpenWRT]: ./OpenWRT/README.md
