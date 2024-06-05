# Milk-V Pioneer

## 测试环境

### 操作系统信息

- openEuler RISC-V 23.09 Preview
    - 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/SG2042/
    - 参考安装文档：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/SG2042/README.sg2042.txt
- RevyOS
    - 下载链接：https://mirror.iscas.ac.cn/revyos/extra/images/sg2042/
    - 参考安装文档：https://revyos.github.io/docs/
- Fedora
    - 下载链接：https://milkv.io/docs/pioneer/getting-started/download
    - 参考安装文档：https://milkv.io/zh/docs/pioneer/getting-started/InstallOS
- openKylin
    - 下载链接：https://www.openkylin.top/downloads
    - 参考安装文档：https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin

### 硬件开发板信息

- Milk-V Pioneer (v1.3)

## 测试结果

| 软件分类                | 软件包名 | 测试结果（测试报告）                 |
|---------------------|----------|------------------------------|
| openEuler/Base 镜像启动 | N/A      | [成功][oERV]（使用 `ruyi` CLI 刷写） |
| openEuler/Xfce 镜像启动 | N/A      | [成功][oERV]（使用 `ruyi` CLI 刷写） |
| RevyOS 镜像启动         | N/A      | [成功][RevyOS]（官方支持）           |
| openKylin 镜像启动      | N/A      | [成功][oK]（官方支持）               |
| Fedora 镜像启动         | N/A      | [成功][Fedora]（官方支持&出厂预装）  |

[oERV]: ./openEuler/README_zh.md
[RevyOS]: https://docs.revyos.dev/
[oK]: https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin
[Fedora]: https://milkv.io/zh/docs/pioneer/getting-started/InstallOS