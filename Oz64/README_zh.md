# Pine64 Oz64

## 测试环境

### 操作系统信息

- Debian
  - 下载链接：https://github.com/scpcom/sophgo-sg200x-debian/releases/tag/v1.6.10
  - 参考安装文档：https://github.com/scpcom/sophgo-sg200x-debian/
- NuttX
  - 预编译镜像: https://github.com/lupyuen2/wip-nuttx/releases/tag/sg2000c-1
  - 工具链: xPack https://github.com/xpack-dev-tools/riscv-none-elf-gcc-xpack/releases
  - 参考安装文档: https://nuttx.apache.org/docs/latest/quickstart/install.html

### 硬件开发板信息

- Pine64 Oz64 (512MB, SG2000)

## 测试结果

| 软件分类        | 软件包名 | 测试结果（测试报告） |
| --------------- | -------- | -------------------- |
| Debian 镜像启动 | N/A      | [成功][Debian]       |
| NuttX 镜像启动  | N/A      | [成功][NuttX]        |

[Debian]: ./Debian/README_zh.md
[NuttX]: ./NuttX/README_zh.md
