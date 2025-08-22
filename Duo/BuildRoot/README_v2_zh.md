# Buildroot (v2) Milk-V Duo 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Duo Buildroot V2.0.1
- 下载链接：<https://github.com/milkv-duo/duo-buildroot-sdk-v2/releases/download/v2.0.1/milkv-duo-musl-riscv64-sd_v2.0.1.img.zip>
- 参考安装文档：<https://github.com/milkv-duo/duo-buildroot-sdk-v2>

### 硬件信息

- Milk-V Duo 64M
- USB 转 UART 调试器
- microSD 卡

## 安装步骤

### 下载并解压镜像
从[下载链接](https://github.com/milkv-duo/duo-buildroot-sdk-v2/releases/download/v2.0.1/milkv-duo-musl-riscv64-sd_v2.0.1.img.zip)下载你所需镜像。
**解压相关文件**
```shell
unzip milkv-duo-musl-riscv64-sd_v2.0.1.img.zip
```

### 向 microSD 卡烧录系统镜像
可使用 `dd` 命令
```shell
sudo dd if=milkv-duo-musl-riscv64-sd_v2.0.1.img of=/dev/mmcblkX bs=1M
```

Log:
```log
输入了 896+1 块记录
输出了 896+1 块记录
939524608 字节 (940 MB, 896 MiB) 已复制，31.3784 s，29.9 MB/s
```

### 登录系统
将 microSD 卡插入 Milk-V Duo，重启。
通过串口登录系统，例如 `minicom` 工具。
```bash
minicom -D /dev/ttyACM0 -c on
```

默认用户名：`root`
默认密码：`milkv`

## 预期结果
系统正常启动，能够通过板载串口登录。
若 USB NET 已连接，可通过 SSH 登录。

## 实际结果
系统正常启动，成功通过板载串口登录。

### 启动信息
```log
[    2.777741] sync_task_init:177(): sync_task_init vi_pipe 2
[    2.783716] sync_task_init:177(): sync_task_init vi_pipe 3
[    2.789690] sync_task_init:177(): sync_task_init vi_pipe 4
[    2.796187] vi_core_probe:242(): isp registered as cvi-vi
[    2.854730] vpss_start_handler:5143(): handler for dev(0) started
[    2.854911] vpss_start_handler:5143(): handler for dev(1) started
[    2.905199] cv180x-cooling cv180x_cooling: elems of dev-freqs=6
[    2.917803] cv180x-cooling cv180x_cooling: dev_freqs[0]: 850000000 500000000
[    2.925703] cv180x-cooling cv180x_cooling: dev_freqs[1]: 425000000 375000000
[    2.933317] cv180x-cooling cv180x_cooling: dev_freqs[2]: 425000000 300000000
[    2.941032] cv180x-cooling cv180x_cooling: Cooling device registered: cv180x_cooling
[    2.975689] [INFO] Register SBM IRQ ###################################
[    2.975718] [INFO] pvctx->s_sbm_irq = 38
[    2.996176] jpu ctrl reg pa = 0xb030000, va = (____ptrval____), size = 256
[    3.007900] end jpu_init result = 0x0
[    3.101127] cvi_vc_drv_init result = 0x0
[    3.115999] sh (167): drop_caches: 3
Starting app...

[root@milkv-duo]~# uname -a
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Fri May 30 14:51:52 CST 2025 riscv64 GNU/Linux
[root@milkv-duo]~# cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

[root@milkv-duo]~# cat /etc/os-release
NAME=Buildroot
VERSION=-g6b03c2762-dirty
ID=buildroot
VERSION_ID=2025.02
PRETTY_NAME="Buildroot 2025.02"
[root@milkv-duo]~#
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。