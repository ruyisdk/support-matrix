---
sys: fedora
sys_ver: 33
sys_var: null

status: cfh
last_update: 2025-03-18
---

# Fedora DongshanPI-Nezha STU Test Report

## Test Environment

### Operating System Information

- Download Link: https://mirror.iscas.ac.cn/fedora-riscv/old_dl/Allwinner/Nezha_D1/images-release/Fedora/fedora-riscv64-d1-developer-xfce-rawhide-Rawhide-20220117-135925.n.0-sda.raw.zst
- Reference Installation Document: https://popolon.org/depots/RISC-V/D1/ovsienko/_index.html

### Hardware Information

- DongshanPI-Nezha STU
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `zstd` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
zstd -kd fedora-riscv64-d1-developer-xfce-rawhide-Rawhide-20220117-135925.n.0-sda.raw.zst
sudo dd if=/path/to/fedora-riscv64-d1-developer-xfce-rawhide-Rawhide-20220104-012902.n.0-sda.raw of=/dev/your_device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default Username: `root`
Default Password: `riscv`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system is unbootable with faulty systemd daemons, unloaded kernel modules and frequent core dumps.

See the boot log below for more details.

### Boot Log

```log
[  129.355648] sstatus: 8000000201804020 sbadaddr: 0000000000000000 scause: 0000000000000002
[  129.355889] Process 582(systemd-coredum) has RLIMIT_CORE set to 1
[  129.355893] Aborting core
[  129.356418] systemd-coredum[583]: unhandled signal 4 code 0x1 at 0x0000003fb8b162c4 in ld-2.32.so[3fb8b11000+1b000]
[  129.356456] CPU: 0 PID: 583 Comm: systemd-coredum Not tainted 5.4.61 #5
[  129.356462] sepc: 0000003fb8b162c4 ra : 0000003fb8b1aa00 sp : 0000003fff9444e0
[  129.356468]  gp : ffffffe001268958 tp : 0000000000000000 t0 : 000000006ffffeff
[  129.356473]  t1 : ffffffffeffffef5 t2 : 000000000000000a s0 : 0000003fff944a70
[  129.356478]  s1 : 0000003fff944520 a0 : 0000002ab6ffebf0 a1 : 0000000000000005
[  129.356482]  a2 : 0000000000000003 a3 : 0000003fff9444e0 a4 : 0000000000000001
[  129.356487]  a5 : 0000002ab6ffe238 a6 : 0000000000000001 a7 : 0000000000000039
[  129.356492]  s2 : 0000002ab6ffebf0 s3 : 0000002ab7008dd0 s4 : 0000003fb8b2f1b0
[  129.356497]  s5 : 0000003fb8b2f1b0 s6 : 0000000000000000 s7 : 0000000000000000
[  129.356502]  s8 : 0000000000000000 s9 : 0000003fff944ae0 s10: 0000003fff9445b0
[  129.356507]  s11: 0000003fff9445c8 t3 : fffffffffffffffc t4 : 0000000000000032
[  129.356511]  t5 : 000000000000000b t6 : 000000006ffffdff
[  129.356516] sstatus: 8000000201804020 sbadaddr: 0000000000000000 scause: 0000000000000002
[  129.356788] Process 583(systemd-coredum) has RLIMIT_CORE set to 1
[  129.356792] Aborting core
[  129.367180] sepc: 0000003fcce0fcb6 ra : 0000003fcce0fc46 sp : 0000003fffd4d380
[  129.367186]  gp : 0000002ab5b46800 tp : 0000003fccb921b0 t0 : 0000000000000005
[  129.367192]  t1 : 0000003fbf4c96a0 t2 : 00000000ffffffff s0 : 0000003fbeb590e0
[  129.367198]  s1 : 0000003fbe43ccf0 a0 : 0000003fbeb97cc0 a1 : 0000000000000000
[  129.367203]  a2 : 0000000000000001 a3 : 00000007fffffff8 a4 : 000000000000001c
[  129.367208]  a5 : 0000003fbce01540 a6 : 0000003fbf4c9690 a7 : 0000000000000003
[  129.367214]  s2 : 0000002abece5180 s3 : 0000000000000002 s4 : 00000047be43ce50
[  129.367219]  s5 : 0000003fbce01580 s6 : 0000000000000001 s7 : 0000003fbe43ce58
[  129.367225]  s8 : ffffffffffffffff s9 : 0000000000000002 s10: 0000000000000028
[  129.367230]  s11: 0000003fbe43ce58 t3 : 0000000000000007 t4 : 0000003fbe43ce80
[  129.367234]  t5 : 0000000000000006 t6 : 0000000000000010
[  129.367240] sstatus: 8000000201804020 sbadaddr: 00000047be43ce50 scause: 000000000000000d
[  129.379951] Process 584(systemd-coredum) has RLIMIT_CORE set to 1
[  129.379957] Aborting core
[  129.386912] Process 586(systemd-coredum) has RLIMIT_CORE set to 1
[  129.386918] Aborting core
[  129.392731] Process 590(systemd-coredum) has RLIMIT_CORE set to 1
[  129.392735] Aborting core
[  129.397320] Process 592(systemd-coredum) has RLIMIT_CORE set to 1
[  129.397325] Aborting core

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test failed.
