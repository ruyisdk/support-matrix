# LicheeRV / AWOL Nezha D1

## 测试环境

### 操作系统信息

- openEuler RISC-V 23.03 Preview
  - 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.03-V1-riscv64/D1/
    - 可选包含 Xfce 桌面的镜像或者仅提供命令行的 Base 镜像
  - 参考安装文档：https://gitee.com/openeuler/RISC-V/tree/master/release/openEuler-23.03/Installation_Book/D1_and_Licheerv

### 硬件开发板信息

- Sipeed Lichee RV Dock
- AWOL Nezha

两款开发板均采用了全志 D1 芯片，共享同样的系统镜像。

## 测试结果

| 软件分类      | 软件包名     | 测试结果（测试报告）                                                                                                                   |
|-----------|--------------|------------------------------------------------------------------------------------------------------------------------------------|
| Base 镜像启动 |              | [成功](https://gitee.com/yunxiangluo/ruyisdk-test/blob/master/20240130/D1-%E9%95%9C%E5%83%8F%E5%88%B7%E5%86%99%E6%B5%8B%E8%AF%95.md) |
| 桌面镜像启动  | Xfce Desktop | [成功](https://gitee.com/openeuler/RISC-V/tree/master/release/openEuler-23.03/Installation_Book/D1_and_Licheerv)                     |

