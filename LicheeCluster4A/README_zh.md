# Lichee Cluster 4A

## 测试环境

### 操作系统信息

- RevyOS (Sipeed 厂商镜像)
    - 下载链接：https://dl.sipeed.com/shareURL/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/bin
    - 参考安装文档：https://wiki.sipeed.com/hardware/zh/lichee/th1520/lc4a/lc4a.html
- openEuler RISC-V 23.09 Preview
    - 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/lpi4a/
    - 参考安装文档：https://revyos.github.io/
- RevyOS (w/mainline kernel)
    - 下载链接：https://mirror.iscas.ac.cn/revyos/extra/images/lpi4amain/20240127/
    - 参考安装文档：https://revyos.github.io/
- RevyOS
    - 下载链接：https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/
    - 参考安装文档：https://docs.revyos.dev/
- openKylin
    - 下载链接：https://www.openkylin.top/downloads/index-cn.html
    - 参考安装文档：https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin
- Fedora
    - 下载链接：https://openkoji.iscas.ac.cn/pub/dl/riscv/T-Head/th1520_light/images/
    - 参考安装文档：https://fedoraproject.org/wiki/Architectures/RISC-V/T-Head
- Armbian
    - 下载链接：https://github.com/chainsx/armbian-riscv-build/tree/main
    - 参考安装文档：https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide_zh.md
- OpenWRT
    - 下载链接：https://github.com/chainsx/openwrt-th1520/releases
    - 参考安装文档：https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide_zh.md

### 硬件开发板信息

- Lichee Cluster 4A + 7 * LM4A 8GB RAM

## 测试结果

| 软件分类                         | 软件包名 | 测试结果（测试报告）                  |
| -------------------------------- | -------- | ------------------------------------- |
| RevyOS(Sipeed 厂商镜像) 镜像启动 | N/A      | [成功][RevySipeed]（Sipeed 厂商镜像） |
| RevyOS(LPi4a 镜像) 镜像启动      | N/A      | [成功][RevyLPi]                       |
| RevyOS(mainline 镜像) 镜像启动   | N/A      | [成功][RevyOS]（官方支持）            |
| openEuler/Base 镜像启动          | N/A      | [成功][oERV]                          |
| openEuler/Xfce 镜像启动          | Xfce     | [成功][oERV]                          |
| openKylin 镜像启动               | N/A      | [成功][oK]                            |
| Fedora 桌面镜像启动              | N/A      | [成功][Fedora]                        |
| Armbian 镜像启动                 | N/A      | [成功][Armbian]                       |
| OpenWRT 镜像启动                 | N/A      | [成功][OpenWRT]                       |

[RevySipeed]: ./RevyOS/README_Sipeed_zh.md
[RevyLPi]: ./RevyOS/README_lpi4a_zh.md
[RevyOS]: ./RevyOS/README_zh.md
[oERV]: ./openEuler/README_zh.md
[oK]: ./openKylin/README_zh.md
[Fedora]: ./Fedora/README_zh.md
[Armbian]: ./Armbian/README_zh.md
[OpenWRT]: ./OpenWRT/README_zh.md