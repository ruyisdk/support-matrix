---
product: Lichee Pi 4A
cpu: TH1520
cpu_core: XuanTie C910 + XuanTie C906 + XuanTie E902
ram: 8G/16G

vendor: sipeed-lpi4a
board_variant: [8g, 16g]
cpu_arch: [
    xuantie-c910,
    xuantie-c906,
    xuantie-e902,
]
---

# Lichee Pi 4A

## Testing Environment

### System Information

- openEuler RISC-V 24.03 SP1 LTS
    - Download Link: https://www.openeuler.org/en/download/#openEuler%2024.03%20LTS%20SP1
    - Reference Installation Document: https://docs.openeuler.org/en/docs/24.03_LTS/docs/Installation/RISC-V-LicheePi4A.html
- openEuler RISC-V 25.03
    - Download Link: https://repo.openeuler.org/openEuler-25.03/embedded_img/riscv64/lpi4a/
    - Reference Installation Document: https://docs.openeuler.org/en/docs/24.03_LTS/docs/Installation/RISC-V-LicheePi4A.html
- RevyOS 20250526
    - Download link: [RevyOS Images](https://fast-mirror.isrc.ac.cn/revyos/extra/images/lpi4a/20250526/)
    - Reference Installation Document: [RevyOS Documentation](https://docs.revyos.dev/)
- openKylin 2.0 SP1
    - Download link: https://www.openkylin.top/downloads/index-cn.html
    - Desktop Environment: UKUI
    - Reference Installation Document: https://docs.openkylin.top/zh/01_%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7%E6%8C%87%E5%8D%97/%E5%9C%A8riscv%E4%B8%8A%E5%AE%89%E8%A3%85/%E5%9C%A8LicheePi4A%E4%B8%8A%E5%AE%89%E8%A3%85openKylin
- Fedora 41
  - Download Link: https://images.fedoravforce.org/LicheePi%204A
  - Reference Installation Document: https://fedoraproject.org/wiki/Architectures/RISC-V/T-Head
- Armbian (Ubuntu 22.04 LTS)
    - Download link: https://github.com/chainsx/armbian-riscv-build/releases
    - Reference Installation Document: ttps://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide.md
- Arch Linux
    - Download link: https://mirror.iscas.ac.cn/archriscv/images/
    - Reference Installation Document: https://wiki.archlinux.org/title/General_recommendations
- Deepin 25-beige-preview 20250122
    - Download Link: https://ci.deepin.com/repo/deepin/deepin-ports/cdimage/20250122/riscv64/deepin-25-beige-preview-riscv64-th1520-20250122-113934.tar.xz
    - Reference Installation Document: https://cdimage.deepin.com/RISC-V/preview-20240517-riscv64/README.md
- NixOS 23.05
    - Download Link：https://github.com/ryan4yin/nixos-licheepi4a/releases
    - Reference Installation Document：https://github.com/ryan4yin/nixos-licheepi4a?tab=readme-ov-file
- OpenWRT
    - Download Link：https://github.com/chainsx/openwrt-th1520/releases
    - Reference Installation Document：https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide_ch.md
- Slackware
    - Download link: http://dl.slarm64.org/slackware/images/lichee_pi_4a/
    - Reference Installation Document: http://dl.slarm64.org/slackware/images/lichee_pi_4a/README.TXT
### Hardware Information

- Lichee Pi 4A 8/16GB RAM + 32/128GB eMMC


## Test Results

| Software Category               | Software Package | Test Results (Test Report)              |
|---------------------------------|------------------|-----------------------------------------|
| openEuler LTS Image Boot        | N/A              | [Success][oERV]                         |
| openEuler Innovation Image Boot | N/A              | [Success][openEuler]                    |
| RevyOS Desktop Image Boot       | N/A              | [Success][RevyOS] (Official Support)    |
| Fedora Desktop Image Boot       | N/A              | [Success][Fedora] (Official Support)    |
| openKylin Desktop Image Boot    | N/A              | [Success][openKylin] (Official Support) |
| Armbian (Ubuntu) Image Boot     | N/A              | [Success][Armbian]                      |
| Arch Linux Desktop Image Boot   | N/A              | [Success][ArchLinux]                    |
| Deepin Desktop Image Boot       | N/A              | [Success][Deepin]                       |
| NixOS Image Boot                | N/A              | [Success][NixOS]                        |
| irradium Image Boot             | N/A              | [CFT][irradium]                         |
| Slackware Image Boot            | N/A              | [Success][Slackware]                    |
| OpenWRT Image Boot              | N/A              | [Success][OpenWRT]                      |

[oERV]: ./openEuler/README.md
[openEuler]: ./openEuler/Innovation.md
[RevyOS]: ./RevyOS/README.md
[Fedora]: ./Fedora/README.md
[Armbian]: ./Armbian/README.md
[openKylin]: ./openKylin/README.md
[ArchLinux]: ./ArchLinux/README.md
[Deepin]: ./Deepin/README.md
[NixOS]: ./NixOS/README.md
[irradium]: ./irradium/README.md
[Slackware]: ./Slackware/README.md
[OpenWRT]: ./OpenWRT/README.md
