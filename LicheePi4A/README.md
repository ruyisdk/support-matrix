# Lichee Pi 4A

## 测试环境

### 操作系统信息

- openEuler RISC-V 23.09 Preview
    - 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/lpi4a/
    - 参考安装文档：https://gitee.com/yunxiangluo/openEuler-RISC-V-23.09-independent/blob/master/lpi4a/Install.md
- RevyOS
    - 下载链接：https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/
    - 参考安装文档：https://docs.revyos.dev/
- Fedora
    - 下载链接：https://openkoji.iscas.ac.cn/pub/dl/riscv/T-Head/th1520_light/images/
    - 参考安装文档：https://fedoraproject.org/wiki/Architectures/RISC-V/T-Head

### 硬件开发板信息

- Lichee Pi 4A 16GB RAM + 128GB eMMC

## 测试结果

| 软件分类                | 软件包名 | 测试结果（测试报告） |
|---------------------|----------|------------------|
| openEuler/Base 镜像启动 | N/A      | [成功][oERV]       |
| openEuler/Xfce 镜像启动 | N/A      | [成功][oERV]       |
| RevyOS 桌面镜像启动     | N/A      | 成功（官方支持）     |
| Fedora 桌面镜像启动     | N/A      | 成功（官方支持）     |

[oERV]: https://gitee.com/yunxiangluo/openEuler-RISC-V-23.09-independent/tree/master/lpi4a