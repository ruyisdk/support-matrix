# eweOS Milk-V Mars 测试报告

## 测试环境

### 操作系统信息

- 系统版本：eweOS
- 下载链接：<https://github.com/panglars/eweos-vf2-mainline>
- 参考安装文档：<https://github.com/panglars/eweos-vf2-mainline/blob/main/README.md>
- eweOS官网: <https://os.ewe.moe/>

### 硬件信息

- Milk-V Mars (V1.21)
- USB 电源适配器一个
- USB-A to C 或 C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

## 安装步骤

### 构建镜像

- 根据本地RISC-V工具链前缀更改 `build.sh` 中的 `CROSS_COMPILE`

- 修改 `build.sh` 中eweOS的镜像链接 `${WGET} https://os-repo-lu.ewe.moe/eweos-images/eweos-riscv64-tarball.tar.xz`为 `${WGET} https://os-repo-auto.ewe.moe/eweos-images/eweos-riscv64-tarball.tar.xz` (链接出处：<https://os-wiki.ewe.moe/guides/qemu-boot-isoimage>)

``` bash
chmod +x ./build.sh
sudo ./build.sh
```

构建出的镜像为 `ewe-vf2.img`

> [!Note]
> 构建的流程中会挂载镜像并执行 `chroot` 操作，且会联网下载软件包，故只有在一台能联网的RISC-V架构的HOST机器上才能成功自动构建镜像。

### 刷写镜像到 microSD 卡

```bash
sudo dd if=ewe-vf2.img of=/dev/<your-device> bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名：`ewe`

默认密码：`ewe`

Root 帐户密码:`ewe`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
eweOS 6.13.8 (/dev/ttyS0)


eweos-diskimage login: ewe
Password:

Welcome to eweOS!

 * Mainpage: https://os.ewe.moe
 * Wiki:     https://os-wiki.ewe.moe
 * Packages: https://os.ewe.moe/pkglist

[ewe@eweos-diskimage ~]$ cat /etc/os-release
NAME="eweOS"
ID=ewe
PRETTY_NAME="eweOS"
BUILD_ID=rolling
ANSI_COLOR="0;36"
HOME_URL="https://os.ewe.moe"
SUPPORT_URL="https://os.ewe.moe"
BUG_REPORT_URL="https://os.ewe.moe"
LOGO=eweos-logo
[ewe@eweos-diskimage ~]$ uname -a
Linux eweos-diskimage 6.13.8 #1 SMP Wed Mar 26 17:04:22 UTC 2025 riscv64 GNU/Linux
[ewe@eweos-diskimage ~]$ cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 1
hart            : 2
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
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
