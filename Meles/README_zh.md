# Milk-V Meles

## 测试环境

### 操作系统信息

- RevyOS
    - 下载链接：https://mirror.iscas.ac.cn/revyos/extra/images/meles/20241229/
    - 参考安装文档：https://milkv.io/zh/docs/meles/getting-started/boot
- Deepin TH1520 20250122
    - 下载链接：https://ci.deepin.com/repo/deepin/deepin-ports/cdimage/20250122/riscv64/deepin-25-beige-preview-riscv64-th1520-20250122-113934.tar.xz
      - U-Boot with SPL 固件：https://cdimage.deepin.com/RISC-V/preview-20240815-riscv64/uboot-th1520-revyos.zip
      - iw-single-line 烧录工具：https://mirror.iscas.ac.cn/revyos/extra/images/meles/20240720/iw-single-line.bin
    - 参考安装文档：https://milkv.io/zh/docs/meles/getting-started/boot
### 硬件开发板信息

- Milk-V Meles 4GB/8GB/16GB
    - 文档中测试的为 16GB 版本

## 测试结果

| 软件分类        | 软件包名 | 测试结果（测试报告） |
| --------------- | -------- | -------------------- |
| RevyOS 镜像启动 | N/A      | [Good][RevyOS]       |
| Deepin 镜像启动 | N/A      | [Good][Deepin]       |

[RevyOS]: ./RevyOS/README_zh.md
[Deepin]: ./Deepin/README_zh.md