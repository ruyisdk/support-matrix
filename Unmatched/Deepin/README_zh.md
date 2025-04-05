# Deepin HiFive Unmatched 测试报告

## 测试环境

### 系统信息

- 系统版本：Deepin
- 下载链接：https://cdimage.deepin.com/RISC-V/Unmatched-image/deepin-sifive.7z
- 参考安装文档：https://cdimage.deepin.com/RISC-V/Unmatched-image/README.txt

> [!Warning]
> Deepin 已结束对 HiFive Unmatched 的支持。本次版本的最新版本来自 2022.11.11，可能会有潜在安全问题，不建议用于生产环境。

### 硬件信息

- HiFive Unmatched Rev A
- microUSB 线缆一条（随 HiFive Unmatched 附赠）
- ATX 电源一个
- PCI-E 显卡一张（本次使用 Radeon R5 230）
- NVME 硬盘

## 安装步骤

### 刷写镜像

**该镜像并不适用于 SD 卡，需要 NVME 硬盘**

使用 `7z` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
7z e deepin-sifive.7z
sudo dd if=deepin-sifive.img of=/dev/your/device bs=1M status=progress
```

### 登录系统

通过图形界面登录系统。

串口/桌面用户信息如下：

默认用户名： `root`
默认密码： `Riscv2022#`

默认用户名： `deepin`
默认密码： `deepin`

## 预期结果

系统正常启动，能够通过板载串口或图形界面登录。

## 实际结果

系统正常启动，成功通过板载串口或图形界面登录。

```log
Verification successful
Linux deepin-riscv 6.0.0-4-riscv64 #1 SMP Debian 6.0.8-1 (2022-11-11) riscv64
Welcome to Deepin 23 GNU/Linux

    * Homepage:https://www.deepin.org/

    * Bugreport:https://bbs.deepin.org/


Last login: Fri Jan 24 19:09:43 2025
deepin@deepin-riscv:~$ cat /etc/os-release
PRETTY_NAME="Deepin 23"
NAME="Deepin"
VERSION_ID="23"
VERSION="23"
ID=Deepin
HOME_URL="https://www.deepin.org/"
BUG_REPORT_URL="https://bbs.deepin.org"
VERSION_CODENAME=beige
deepin@deepin-riscv:~$ cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,bullet0

processor       : 1
hart            : 2
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,bullet0

processor       : 2
hart            : 3
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,bullet0

processor       : 3
hart            : 4
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,bullet0

deepin@deepin-riscv:~$ uname -a
Linux deepin-riscv 6.0.0-4-riscv64 #1 SMP Debian 6.0.8-1 (2022-11-11) riscv64 GNU/Linux
deepin@deepin-riscv:~$
```


![](image/2025-01-25-03-15-31.png)

![](image/2025-01-25-03-14-53.png)

详细桌面体验测试报告见 https://github.com/QA-Team-lo/oscompare/blob/main/Deepin/Unmatched/README.md

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。