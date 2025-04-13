# Guix Milk-V Mars 测试报告

## 测试环境

### 硬件信息

- 开发板：Milk-V Mars (8GB RAM)
- 其他硬件：
  - USB 电源适配器和USB-A to C 或 C to C 线缆一条
  - microSD 卡一张
  - USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

### 操作系统信息

- 操作系统版本：Guix (Build ID: 9893288, 8 April 2025)
- 下载链接：<https://ci.guix.gnu.org/search/latest?query=spec:images+status:success+system:x86_64-linux+visionfive2-barebones-raw-image>
- 参考安装文档：<https://milkv.iso/zh/docs/mars/getting-started/boot>

## 安装步骤

### 刷写镜像

使用 `dd` 命令或 `balenaEtcher` 软件将镜像写入 microSD 卡。

其中，`/dev/sdc` 为存储卡对应设备。

```bash
sudo dd if=0rvywqxwkfn0rk18q71fv5b55bc16ax8-visionfive2-barebones-raw-image of=/dev/sdc bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名： `root`

默认无密码

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过串口查看输出。

### 启动信息

```log
This is the GNU system.  Welcome.
visionfive2 login: root
This is the GNU operating system, welcome!

root@visionfive2 ~# uname -a
Linux visionfive2 6.13.9-gnu #1 SMP 1 riscv64 GNU/Linux

root@visionfive2 ~# cat /etc/os-release
NAME="Guix System"
ID=guix
PRETTY_NAME="Guix System"
LOGO=guix-icon
HOME_URL="https://guix.gnu.org"
DOCUMENTATION_URL="https://guix.gnu.org/en/manual"
SUPPORT_URL="https://guix.gnu.org/en/help"
BUG_REPORT_URL="https://lists.gnu.org/mailman/listinfo/bug-guix"
root@visionfive2 ~# cat /proc/cpuinfo
processor       : 0
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

root@visionfive2 ~#
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功
