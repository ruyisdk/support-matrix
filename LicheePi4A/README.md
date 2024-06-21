# Lichee Pi 4A

## Testing Environment

### System Information

- openEuler RISC-V 23.09 Preview
    - Download link: [openEuler-RISC-V](https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/lpi4a/)
    - Reference Installation Document: [Installation Guide](https://gitee.com/yunxiangluo/openEuler-RISC-V-23.09-independent/blob/master/lpi4a/Install.md)
- RevyOS
    - Download link: [RevyOS Images](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/)
    - Reference Installation Document: [RevyOS Documentation](https://docs.revyos.dev/)
- openKylin
    - Download link: [OpenKylin Downloads](https://www.openkylin.top/downloads/index-cn.html)
    - Reference Installation Document: [OpenKylin Installation Guide](https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin)
- Fedora
    - Download link: [Fedora Images](https://openkoji.iscas.ac.cn/pub/dl/riscv/T-Head/th1520_light/images/)
    - Reference Installation Document: [Fedora Installation Guide](https://fedoraproject.org/wiki/Architectures/RISC-V/T-Head)
- Armbian
    - Download link: [Armbian Images](https://github.com/chainsx/armbian-riscv-build/tree/main)
    - Reference Installation Document: [Armbian Installation Guide](https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide.md)

### Hardware Information

- Lichee Pi 4A 16GB RAM + 128GB eMMC
- Lichee Pi 4A 8GB RAM + 64GB eMMC

## Test Results

| Software Category         | Software Package | Test Results (Test Report) |
|-------------------------|------------------|---------------------------|
| openEuler/Base Image Boot  | N/A              | [Success][oERV]           |
| openEuler/Xfce Image Boot  | Xfce             | [Success][oERV]           |
| RevyOS Desktop Image Boot  | N/A              | [Success][RevyOS] (Official Support)  |
| Fedora Desktop Image Boot   | N/A              | [Success][Fedora] (Official Support) |
| openKylin Desktop Image Boot| N/A              | [Success][openKylin] (Official Support) |
| Armbian Image Boot          | N/A              | [Success][Armbian]         |
| OpenWRT Image Boot          | N/A              | [Success][OpenWRT]         |

[oERV]: ./openEuler/README.md
[RevyOS]: ./RevyOS/README.md
[Fedora]: ./Fedora/README.md
[Armbian]: ./Armbian/README.md
[openKylin]: ./openKylin/README.md
[OpenWRT]: ./OpenWRT/README.md