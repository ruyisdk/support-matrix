# Milk-V Pioneer

## 测试环境

### 操作系统信息

- openEuler RISC-V 23.09 Preview
    - 下载链接：https://www.openeuler.org/zh/download/archive/detail/?version=openEuler%2024.03%20LTS
    - 参考安装文档：https://docs.openeuler.org/zh/docs/24.03_LTS/docs/Installation/RISC-V-Pioneer1.3.html
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

| 软件分类                      | 软件包名 | 测试结果（测试报告）                |
|-----------------------------|----------|--------------------------------|
| openEuler (Image 镜像，Legacy) | N/A      | [成功][oERV]（官方支持）            |
| RevyOS 镜像启动               | N/A      | [成功][RevyOS]（官方支持）          |
| openKylin 镜像启动            | N/A      | [成功][oK]（官方支持）              |
| Fedora 镜像启动               | N/A      | [成功][Fedora]（官方支持&出厂预装） |
| Deepin 镜像启动               | N/A      | [成功][Deepin]（仅 CLI）            |

[oERV]: ./openEuler/README_zh.md
[RevyOS]: ./RevyOS/README_zh.md
[oK]: ./openKylin/README_zh.md
[Fedora]: ./Fedora/README_zh.md
[Deepin]: ./Deepin/README_zh.md