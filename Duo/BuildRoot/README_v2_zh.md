# BuildRoot (v2) Milk-V Duo 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Duo-V2.0.0
- 下载链接：https://github.com/milkv-duo/duo-buildroot-sdk-v2/releases
- 参考安装文档：https://github.com/milkv-duo/duo-buildroot-sdk-v2

### 硬件信息

- Milk-V Duo 64M
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
sudo dd if=milkv-duo-musl-riscv64-sd_v2.0.0.img  of=/path/to/your/device bs=4M status=progress
```

### 登录系统

通过串口或 ssh 登录系统。默认以 root 无密码登录。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
[    2.892411] vi_core_probe:206(): irq(33) for isp get from platform driver.
[    2.901240] sync_task_init:177(): sync_task_init vi_pipe 0
[    2.906979] sync_task_init:177(): sync_task_init vi_pipe 1
[    2.913081] sync_task_init:177(): sync_task_init vi_pipe 2
[    2.919041] sync_task_init:177(): sync_task_init vi_pipe 3
[    2.924997] sync_task_init:177(): sync_task_init vi_pipe 4
[    2.931494] vi_core_probe:242(): isp registered as cvi-vi
[    2.986778] vpss_start_handler:5134(): handler for dev(0) started
[    2.986970] vpss_start_handler:5134(): handler for dev(1) started
[    3.027421] cv180x-cooling cv180x_cooling: elems of dev-freqs=6
[    3.040112] cv180x-cooling cv180x_cooling: dev_freqs[0]: 850000000 500000000
[    3.048032] cv180x-cooling cv180x_cooling: dev_freqs[1]: 425000000 375000000
[    3.055656] cv180x-cooling cv180x_cooling: dev_freqs[2]: 425000000 300000000
[    3.063401] cv180x-cooling cv180x_cooling: Cooling device registered: cv180x_cooling
[    3.093205] [INFO] Register SBM IRQ ###################################
[    3.093235] [INFO] pvctx->s_sbm_irq = 38
[    3.108700] jpu ctrl reg pa = 0xb030000, va = (____ptrval____), size = 256
[    3.121295] end jpu_init result = 0x0
[    3.206886] cvi_vc_drv_init result = 0x0
[    3.220299] sh (163): drop_caches: 3
Starting app...

[root@milkv-duo]~# uname -a
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Mon Dec 9 10:07:12 CST 2024 riscv64 GNU/Linux
[root@milkv-duo]~# cat /etc/os-release
NAME=Buildroot
VERSION=-g2b4e5fdbc
ID=buildroot
VERSION_ID=2024.02.3
PRETTY_NAME="Buildroot 2024.02.3"
[root@milkv-duo]~#
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。