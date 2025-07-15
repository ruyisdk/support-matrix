---
sys: dietpi
sys_ver: null
sys_var: null

status: basic
last_update: 2025-07-13
---

# DietPi Star64 Test Report

## Test Environment

### Operating System Information

- Download Link: https://dietpi.com/downloads/images/DietPi_Star64-RISC-V-Trixie.img.xz
- Reference Installation Document: https://dietpi.com/blog/?p=2629

### Hardware Information

- Pine64 Star64
- A microSD card
- DC 12V5A Barrel power adapter
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires

## Installation Steps

### Decompress and Flash Image to microSD Card

```bash
xz -d DietPi_Star64-RISC-V-Trixie.img.xz
dd if=DietPi_Star64-RISC-V-Trixie.img.xzg of=/dev/<your-device>
```

### Boot Mode Selection

Set the boot option to microSD (GPIO_0 = 1, GPIO_1 = 0; See [Boot Source Selection](https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/pine64-star64/#boot-source-selection) for details).

### Logging into the System

Logging into the system via the serial port.

Username: `root`
Default Password: `dietpi`

## Expected Results

The system boots normally and allows login via the serial port.

## Actual Results

The system booted normally and login via the serial port was successful.

### Boot Log

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

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
