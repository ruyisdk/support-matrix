# BuildRoot Milk-V Duo 256M 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Duo 256M v2.0.0
- 下载链接：https://github.com/milkv-duo/duo-buildroot-sdk-v2/releases
- 参考安装文档：https://github.com/milkv-duo/duo-buildroot-sdk-v2

### 硬件信息

- Milk-V Duo 256M
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

## 安装步骤

### 下载 Duo 256m 的镜像

```bash
wget https://github.com/milkv-duo/duo-buildroot-sdk-v2/releases/download/v2.0.0/milkv-duo256m-musl-riscv64-sd_v2.0.0.img.zip
unzip milkv-duo256m-musl-riscv64-sd_v2.0.0.img.zip
```

### 刷写镜像

用 dd 刷写镜像到 sd 卡：
```shell
sudo dd if=milkv-duo256m-musl-riscv64-sd_v2.0.0.img  of=/path/to/your/device bs=4M status=progress
```

### 登录系统

通过串口或 ssh 登录系统。

shell 会自动以 root 登录，无需用户名和密码。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
[    2.955329] vi_core_probe:206(): irq(29) for isp get from platform driver.
[    2.964050] sync_task_init:177(): sync_task_init vi_pipe 0
[    2.969787] sync_task_init:177(): sync_task_init vi_pipe 1
[    2.975960] sync_task_init:177(): sync_task_init vi_pipe 2
[    2.981935] sync_task_init:177(): sync_task_init vi_pipe 3
[    2.987940] sync_task_init:177(): sync_task_init vi_pipe 4
[    2.994496] vi_core_probe:242(): isp registered as cvi-vi
[    3.056104] vpss_start_handler:5134(): handler for dev(0) started
[    3.056305] vpss_start_handler:5134(): handler for dev(1) started
[    3.089343] cvi-mipi-tx mipi_tx: IRQ index 0 not found
[    3.101222] cvi-mipi-tx mipi_tx: vbat irq(-6)
[    3.106349] cvi-mipi-tx mipi_tx: reset gpio pin(495) active(0)
[    3.112718] cvi-mipi-tx mipi_tx: power ctrl gpio pin(499) active(1)
[    3.119504] cvi-mipi-tx mipi_tx: pwm gpio pin(498) active(1)
[    3.152127] cv181x-cooling cv181x_cooling: elems of dev-freqs=6
[    3.158359] cv181x-cooling cv181x_cooling: dev_freqs[0]: 850000000 500000000
[    3.166143] cv181x-cooling cv181x_cooling: dev_freqs[1]: 425000000 375000000
[    3.173798] cv181x-cooling cv181x_cooling: dev_freqs[2]: 425000000 300000000
[    3.181520] cv181x-cooling cv181x_cooling: Cooling device registered: cv181x_cooling
[    3.213990] [INFO] Register SBM IRQ ###################################
[    3.214017] [INFO] pvctx->s_sbm_irq = 35
[    3.231513] jpu ctrl reg pa = 0xb030000, va = (____ptrval____), size = 256
[    3.243330] end jpu_init result = 0x0
[    3.342841] cvi_vc_drv_init result = 0x0
[    3.416924] sh (163): drop_caches: 3
Starting app...

[root@milkv-duo]~# uname -a
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Mon Dec 9 10:13:49 CST 2024 riscv64 GNU/Linux
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

成功