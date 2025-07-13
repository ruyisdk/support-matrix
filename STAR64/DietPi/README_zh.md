# DietPi Star64 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://dietpi.com/downloads/images/DietPi_Star64-RISC-V-Trixie.img.xz
- 参考安装文档：https://dietpi.com/blog/?p=2629

### 硬件信息

- Pine64 Star64
- microSD 卡一张
- DC 12V5A 圆头电源适配器
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 解压并刷写镜像到 microSD 卡

```bash
xz -d https://dietpi.com/downloads/images/DietPi_Star64-RISC-V-Trixie.img.xz
dd if=https://dietpi.com/downloads/images/DietPi_Star64-RISC-V-Trixie.img.xz of=/dev/<your-device>
```

### 引导模式选择

将启动项设为 microSD 卡 (GPIO_0 = 1, GPIO_1 = 0；参见 [选择启动项](https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/pine64-star64/#boot-source-selection))。

### 登录系统

通过串口登录系统。

用户名：`root`
默认密码：`dietpi`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```log
[    6.963049] systemd[1]: systemd-tpm2-setup-early.service - Early TPM SRK Setup was skipped because of an unmet condition check (ConditionSecurity=measured-uki).
[    6.979760] systemd[1]: Starting systemd-udev-load-credentials.service - Load udev Rules from Credentials...
[    6.998487] systemd[1]: Starting systemd-udev-trigger.service - Coldplug All udev Devices...
[    7.013373] systemd[1]: Mounted dev-hugepages.mount - Huge Pages File System.
[    7.026809] systemd[1]: Mounted dev-mqueue.mount - POSIX Message Queue File System.
[    7.035331] systemd[1]: Mounted run-lock.mount - Legacy Locks Directory /run/lock.
[    7.043560] systemd[1]: Mounted sys-kernel-debug.mount - Kernel Debug File System.
[    7.053397] systemd[1]: Mounted sys-kernel-tracing.mount - Kernel Trace File System.
[    7.062447] systemd[1]: fake-hwclock-load.service: Deactivated successfully.
[    7.070022] systemd[1]: Finished fake-hwclock-load.service - Restore the current clock.
[    7.078128] systemd-journald[169]: Collecting audit messages is disabled.
[    7.093392] systemd[1]: Finished kmod-static-nodes.service - Create List of Static Device Nodes.
[    7.103390] systemd[1]: modprobe@configfs.service: Deactivated successfully.
Star64 (riscv64)





Star64 (riscv64)












┌─────────────────────────────────────────────────────────────┤ DietPi-Login ├──────────────────────────────────────────────────────────────┐
│                                                                                                                                           │
│ [FAILED] Unknown install state/First run setup failed                                                                                     │
│                                                                                                                                           │
│ An error has occurred either during first run update or installs.                                                                         │
│                                                                                                                                           │
│ First run setup will now attempt to re-apply the last step, forced as interactive run.                                                    │
│ If this repeatedly fails, please collect all terminal output and the content of /var/tmp/dietpi/logs/dietpi-firstrun-setup.log if         │
│ available and report this issue to: https://github.com/MichaIng/DietPi/issues                                                             │
│                                                                                                                                           │
│ Would you like to restart the first run setup and installation?                                                                           │
│                                                                                                                                           │
│                                          <Ok>                                              <Cancel>                                       │
│                                                                                                                                           │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘












root@DietPi:~# uname -a
Linux DietPi 6.1.97 #1 SMP Fri Jul  5 23:04:10 UTC 2024 riscv64 GNU/Linux
root@DietPi:~# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@DietPi:~# cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 1
hart            : 2
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 2
hart            : 3
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 3
hart            : 4
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

root@DietPi:~#

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
