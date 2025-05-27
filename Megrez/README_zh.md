# Milk-V Megrez

## 测试环境

### 操作系统信息

- RockOS
    - 项目链接：https://github.com/rockos-riscv
    - 镜像链接：https://fast-mirror.isrc.ac.cn/rockos/images/generic/latest/
    - 参考安装文档
        - https://milkv.io/zh/docs/megrez/getting-started/boot
        - https://rockos-riscv.github.io/rockos-docs/docs/installation
- Fedora 41
    - 镜像链接：https://images.fedoravforce.org/Megrez
    - 参考安装文档：https://milkv.io/zh/docs/megrez/getting-started/boot
- Guix System
    - 镜像链接: https://github.com/Z572/guix-riscv-channel/releases
    - 参考安装文档: https://github.com/Z572/guix-riscv-channel#megrez
- Deepin
    - 镜像链接: https://deepin-community.github.io/sig-deepin-ports/images/riscv/download
    - 参考安装文档: https://milkv.io/zh/docs/megrez/getting-started/boot

### 硬件开发板信息

- Milk-V Megrez

## 测试结果

| 软件分类                | 软件包名 | 测试结果（测试报告）             |
|-------------------------|----------|----------------------------------|
| RockOS 镜像启动         | N/A      | [Good][RockOS]                   |
| Fedora 镜像启动         | N/A      | [CFT][Fedora]                    |
| Guix System 镜像启动    | N/A      | [CFT][Guix]                      |
| Deepin 镜像启动         | N/A      | [Good][Deepin]                   |

[RockOS]: ./RockOS/README.md
[Fedora]: ./Fedora/README.md
[Guix]: ./Guix/README.md
[Deepin]: ./Deepin/README.md
