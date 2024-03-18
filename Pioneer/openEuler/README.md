# openEuler RISC-V 23.09 Pioneer 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：openEuler 23.09 RISC-V preview
- 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/SG2042/
- 参考安装文档：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Unmatched/README.sg2042.txt

### 硬件信息

- Milk-V Pioneer Box v1.3
- microSD 卡一张（或 NVMe SSD + NVMe SSD 转 USB 硬盘盒）
- USB Type-C 线缆一条（用来连接板载串口）

## 安装步骤

### 使用 `ruyi` CLI 刷写镜像到板载 eMMC

安装 [`ruyi`](https://github.com/ruyisdk/ruyi) 包管理器，运行 `ruyi device provision` 并按提示操作。

### 登录系统

通过 SSH 登录系统。

默认用户名：`openeuler` 或 `root`
默认密码：`openEuler12#$`

## 预期结果

系统正常启动，可通过 SSH 登录。

## 实际结果

系统正常启动，成功通过 SSH 登录。

### 启动信息

```log
System load:    1.61
Processes:      710
Memory used:    .6%
Swap used:      0.0%
Usage On:       11%
IP address:     10.0.0.12
Users online:   1
To run a command as administrator(user "root"),use "sudo <command>".
[openeuler@openeuler-riscv64 ~]$ uname -a
Linux openeuler-riscv64 6.1.61-4.oe2309.riscv64 #1 SMP Thu Dec 28 18:01:00 UTC 2023 riscv64 riscv64 riscv64 GNU/Linux
[openeuler@openeuler-riscv64 ~]$ cat /etc/os-release 
NAME="openEuler"
VERSION="23.09"
ID="openEuler"
VERSION_ID="23.09"
PRETTY_NAME="openEuler 23.09"
ANSI_COLOR="0;31"

[openeuler@openeuler-riscv64 ~]$ cat /proc/cpuinfo 
processor       : 0
hart            : 1
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 1
hart            : 0
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 2
hart            : 2
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 3
hart            : 3
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 4
hart            : 4
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 5
hart            : 5
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 6
hart            : 6
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 7
hart            : 7
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 8
hart            : 8
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 9
hart            : 9
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 10
hart            : 10
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 11
hart            : 11
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 12
hart            : 12
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 13
hart            : 13
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 14
hart            : 14
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 15
hart            : 15
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 16
hart            : 16
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 17
hart            : 17
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 18
hart            : 18
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 19
hart            : 19
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 20
hart            : 20
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 21
hart            : 21
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 22
hart            : 22
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 23
hart            : 23
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 24
hart            : 24
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 25
hart            : 25
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 26
hart            : 26
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 27
hart            : 27
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 28
hart            : 28
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 29
hart            : 29
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 30
hart            : 30
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 31
hart            : 31
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 32
hart            : 32
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 33
hart            : 33
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 34
hart            : 34
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 35
hart            : 35
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 36
hart            : 36
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 37
hart            : 37
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 38
hart            : 38
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 39
hart            : 39
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 40
hart            : 40
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 41
hart            : 41
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 42
hart            : 42
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 43
hart            : 43
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 44
hart            : 44
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 45
hart            : 45
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 46
hart            : 46
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 47
hart            : 47
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 48
hart            : 48
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 49
hart            : 49
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 50
hart            : 50
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 51
hart            : 51
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 52
hart            : 52
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 53
hart            : 53
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 54
hart            : 54
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 55
hart            : 55
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 56
hart            : 56
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 57
hart            : 57
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 58
hart            : 58
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 59
hart            : 59
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 60
hart            : 60
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 61
hart            : 61
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 62
hart            : 62
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 63
hart            : 63
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

[openeuler@openeuler-riscv64 ~]$ 
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。