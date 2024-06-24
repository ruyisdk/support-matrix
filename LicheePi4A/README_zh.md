# Lichee Pi 4A

## 测试环境

### 操作系统信息

- openEuler RISC-V 23.09 Preview
    - 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/lpi4a/
    - 参考安装文档：https://gitee.com/yunxiangluo/openEuler-RISC-V-23.09-independent/blob/master/lpi4a/Install_ch.md
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
    - 参考安装文档：https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide_ch.md

### 硬件开发板信息

- Lichee Pi 4A 16GB RAM + 128GB eMMC
- Lichee Pi 4A 8GB RAM + 64GB eMMC

## 测试结果

| 软件分类                | 软件包名 | 测试结果（测试报告）          |
|---------------------|----------|---------------------------|
| openEuler/Base 镜像启动 | N/A      | [成功][oERV]                |
| openEuler/Xfce 镜像启动 | Xfce     | [成功][oERV]                |
| RevyOS 桌面镜像启动     | N/A      | [成功][RevyOS]（官方支持）    |
| Fedora 桌面镜像启动     | N/A      | [成功][Fedora]（官方支持）    |
| openKylin 桌面镜像启动  | N/A      | [成功][openKylin]（官方支持） |
| Armbian 镜像启动        | N/A      | [成功][Armbian]             |
| OpenWRT 镜像启动        | N/A      | [成功][OpenWRT]             |

[oERV]: ./openEuler/README_zh.md
[RevyOS]: ./RevyOS/README_zh.md
[Fedora]: ./Fedora/README_zh.md
[Armbian]: ./Armbian/README_zh.md
[openKylin]: ./openKylin/README_zh.md
[OpenWRT]: ./OpenWRT/README_zh.md