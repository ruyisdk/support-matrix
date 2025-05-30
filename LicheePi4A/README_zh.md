# Lichee Pi 4A

## 测试环境

### 操作系统信息

- openEuler RISC-V 24.03 SP1 LTS
    - 下载链接：https://www.openeuler.org/zh/download/#openEuler%2024.03%20LTS%20SP1
    - 参考安装文档：https://docs.openeuler.org/zh/docs/24.03_LTS/docs/Installation/RISC-V-LicheePi4A.html
- openEuler 25.03
    - 下载链接：https://repo.openeuler.org/openEuler-25.03/embedded_img/riscv64/lpi4a/
    - 参考安装文档：https://docs.openeuler.org/zh/docs/24.03_LTS/docs/Installation/RISC-V-LicheePi4A.html
- RevyOS 20250323
    - 下载链接：https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/20250323/
    - 参考安装文档：https://docs.revyos.dev/
- openKylin v2.0-SP1
    - 下载链接：https://www.openkylin.top/downloads/index-cn.html
    - 参考安装文档：https://docs.openkylin.top/zh/01_%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7%E6%8C%87%E5%8D%97/%E5%9C%A8riscv%E4%B8%8A%E5%AE%89%E8%A3%85/%E5%9C%A8LicheePi4A%E4%B8%8A%E5%AE%89%E8%A3%85openKylin
- Fedora 41
    - 下载链接：https://images.fedoravforce.org/LicheePi%204A
    - 参考安装文档：https://fedoraproject.org/wiki/Architectures/RISC-V/T-Head
- Armbian (Ubuntu 22.04 LTS)
    - 下载链接：https://github.com/chainsx/armbian-riscv-build/releases
    - 参考安装文档：https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide_ch.md
- Arch Linux
    - 下载链接：https://mirror.iscas.ac.cn/archriscv/images/
    - 参考安装文档：https://wiki.archlinux.org/title/General_recommendations
- Deepin 25-beige-preview 20250122
    - 下载链接：https://deepin-community.github.io/sig-deepin-ports/images/riscv/download
    - 参考安装文档：https://cdimage.deepin.com/RISC-V/preview-20240517-riscv64/README.md
- NixOS 23.05
    - 下载链接：https://github.com/ryan4yin/nixos-licheepi4a/releases
    - 参考安装文档：https://github.com/ryan4yin/nixos-licheepi4a?tab=readme-ov-file
    
### 硬件开发板信息

- Lichee Pi 4A 16GB RAM + 128GB eMMC

## 测试结果

| 软件分类                       | 软件包名 | 测试结果（测试报告）          |
|--------------------------------|----------|-------------------------------|
| openEuler LTS 镜像启动         | N/A      | [成功][oERV]                  |
| openEuler 社区创新版本镜像启动 | N/A      | [成功][openEuler]             |
| RevyOS 桌面镜像启动            | N/A      | [成功][RevyOS]（官方支持）    |
| Fedora 桌面镜像启动            | N/A      | [成功][Fedora]（官方支持）    |
| openKylin 桌面镜像启动         | N/A      | [成功][openKylin]（官方支持） |
| Armbian (Ubuntu) 镜像启动      | N/A      | [成功][Armbian]               |
| Arch Linux 桌面镜像启动        | N/A      | [成功][ArchLinux]             |
| Deepin 桌面镜像启动            | N/A      | [成功][Deepin]                |
| NixOS 镜像启动                 | N/A      | [成功][NixOS]                 |
| irradium 镜像启动              | N/A      | [CFT][irradium]              |

[oERV]: ./openEuler/README_zh.md
[openEuler]: ./openEuler/Innovation_zh.md
[RevyOS]: ./RevyOS/README_zh.md
[Fedora]: ./Fedora/README_zh.md
[Armbian]: ./Armbian/README_zh.md
[openKylin]: ./openKylin/README_zh.md
[ArchLinux]: ./ArchLinux/README_zh.md
[Deepin]: ./Deepin/README_zh.md
[NixOS]: ./NixOS/README_zh.md
[irradium]: ./irradium/README_zh.md
