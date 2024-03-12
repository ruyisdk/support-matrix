# StarFive VisionFive 2

## 测试环境

### 操作系统信息

- openEuler RISC-V 23.09 Preview
    - 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Visionfive2/
    - 参考安装文档：https://gitee.com/openeuler/RISC-V/blob/master/release/openEuler-23.03/Installation_Book/Visionfive2/README.md
- Debian（官方提供）
    - 下载链接：https://github.com/starfive-tech/VisionFive2/releases/
- openKylin
    - 下载链接：https://www.openkylin.top/downloads
    - 参考安装文档：https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin
- Ubuntu 23.10
    - 下载链接：https://cdimage.ubuntu.com/releases/23.10/release/
    - 参考安装文档：https://wiki.ubuntu.com/RISC-V/StarFive%20VisionFive%202
- BuildRoot (VisionFive 2 SDK)
    - 下载链接：https://github.com/starfive-tech/VisionFive2/releases
    - 参考安装文档：https://github.com/starfive-tech/VisionFive2

### 硬件开发板信息

- HiFive Unmatched

## 测试结果

| 软件分类                | 软件包名 | 测试结果（测试报告）      |
|---------------------|----------|-----------------------|
| openEuler/Base 镜像启动 | N/A      | [成功][oERVBase]        |
| openEuler/Xfce 镜像启动 | N/A      | [成功][oERVXfce]        |
| Debian 镜像启动         | N/A      | 成功（StarFive 厂商镜像） |
| openKylin 镜像启动      | N/A      | 成功（官方支持）          |
| Ubuntu 镜像启动         | N/A      | 成功（官方支持）          |
| BuildRoot 镜像启动      | N/A      | 成功（StarFive 厂商镜像） |

[oERVBase]: https://gitee.com/yunxiangluo/openEuler-RISC-V-23.09-independent/tree/master/VF2
[oERVXfce]: https://gitee.com/yunxiangluo/openEuler-RISC-V-23.09-independent/tree/master/VF2