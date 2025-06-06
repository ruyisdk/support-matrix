---
sys: bianbu
sys_ver: "2.2"
sys_var: minimal

status: cfh
last_update: 2025-06-04
---

# Bianbu Lichee Pi 3A Test Report

## Test Environment

### System Information

- System version: v2.2-minimal
- Download Links: https://archive.spacemit.com/image/k1/version/bianbu/v2.2/
- Reference Installation Document: https://wiki.sipeed.com/hardware/en/lichee/K1/lpi3a/1_intro.html

### Hardware Information

- Lichee Pi 3A
- Power Adapter
- A USB to UART Debugger
- A microSD Card (If flash to SD card)
- A type-C cable for fastboot flash

## Installation Steps

### Flashing the Image (SD Card)

**Please make sure to choose the file ending with `.img.zip`**
After downloading and extracting the image, use `dd` to flash the image to the microSD card.

```bash
unzip bianbu-24.04-minimal-k1-v2.2-release-20250430181626.img.zip
sudo dd if=/path/to/bianbu-24.04-minimal-k1-v2.2-release-20250430181626.img of=/dev/your-device bs=1M status=progress
```

### Flashing the Image (eMMC)

**Please make sure to choose the file ending without `img`**
After downloading and extracting the image, use `fastboot` to flash the image to the eMMC.

```bash
unzip bianbu-24.04-minimal-k1-v2.2-release-20250430181626.zip
```

Hold the BOOT button while powering on/RST, to enter the fastboot mode. You shall see the dfu-device in your system:

```log
❯ sudo fastboot devices
dfu-device       DFU download
```

```bash
sudo fastboot stage factory/FSBL.bin
sudo fastboot continue
# Wait for 1 sec
sudo fastboot stage u-boot.itb
sudo fastboot continue
# Wait for 1 sec
sudo fastboot flash gpt partition_universal.json
sudo fastboot flash bootinfo factory/bootinfo_emmc.bin
sudo fastboot flash fsbl factory/FSBL.bin
sudo fastboot flash env env.bin
sudo fastboot flash opensbi fw_dynamic.itb
sudo fastboot flash uboot u-boot.itb
sudo fastboot flash bootfs bootfs.ext4
sudo fastboot flash rootfs rootfs.ext4
```

### Logging into the System

Logging into the system via the serial port.

Default Username: `root`
Default Password: `bianbu`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

A Kernel Panic occurred during the boot process. See the boot log below for details.

### Boot Log

A KP occurred during the boot process, in `spacemit_snd_sspa_pdev_probe`.

Screen recording:
[![asciicast](https://asciinema.org/a/eIS9n4XCZmeghruBB8QaX1Iew.svg)](https://asciinema.org/a/eIS9n4XCZmeghruBB8QaX1Iew)

```log
[    6.213704] enter spacemit_snd_sspa_pdev_probe
[    6.233687] Unable to handle kernel NULL pointer dereference at virtual address 0000000000000090
[    6.242577] Oops [#1]
[    6.244866] Modules linked in:
[    6.247957] CPU: 7 PID: 1 Comm: swapper/0 Not tainted 6.6.63 #2.2.0.2
[    6.254464] Hardware name: SiPEED LPi3A Board (DT)
[    6.259289] epc : spacemit_snd_pcm_new+0x19a/0x280
[    6.264118]  ra : spacemit_snd_pcm_new+0x186/0x280
[    6.268947] epc : ffffffff80c5b814 ra : ffffffff80c5b800 sp : ffffffc800073900
[    6.276217]  gp : ffffffff820fac50 tp : ffffffd900388000 t0 : ffffffff81a84738
[    6.283498]  t1 : 0000000000000004 t2 : 0000000000000000 s0 : ffffffc800073990
[    6.290768]  s1 : 0000000000000000 a0 : 0000000000000000 a1 : 000000000000011b
[    6.298058]  a2 : 0000000000000000 a3 : 0000000000000000 a4 : ffffffd900388000
[    6.305317]  a5 : 0000000000000000 a6 : 0000000000000002 a7 : 00000000000001e7
[    6.312597]  s2 : 0000000000000002 s3 : fffffffffffff000 s4 : 0000000000000800
[    6.319867]  s5 : 0000000000000400 s6 : ffffffff815c0888 s7 : ffffffd903908e40
[    6.327116]  s8 : ffffffd9038b2040 s9 : ffffffd9038cb400 s10: 0000000000000002
[    6.334396]  s11: ffffffd903908ec0 t3 : ffffffffffffffff t4 : 3e00000000ffffff
[    6.341666]  t5 : fffffffff0000080 t6 : ffffffd90386128d
[    6.347012] status: 0000000200000120 badaddr: 0000000000000090 cause: 000000000000000d
[    6.355000] [<ffffffff80c5b814>] spacemit_snd_pcm_new+0x19a/0x280
[    6.361148] [<ffffffff80c46df8>] snd_soc_pcm_component_new+0x26/0xa0
[    6.367546] [<ffffffff80c4c588>] soc_new_pcm+0x436/0x5be
[    6.372919] [<ffffffff80c3cefe>] snd_soc_bind_card+0x8b2/0xa30
[    6.378804] [<ffffffff80c3d162>] snd_soc_register_card+0xe6/0xf8
[    6.384850] [<ffffffff80c4c884>] devm_snd_soc_register_card+0x40/0x86
[    6.391326] [<ffffffff80c5cb1a>] asoc_simple_card_probe+0x180/0x25e
[    6.397637] [<ffffffff80831f86>] platform_probe+0x52/0xaa
[    6.403085] [<ffffffff8082f5cc>] really_probe+0x8c/0x326
[    6.408434] [<ffffffff8082f8c8>] __driver_probe_device+0x62/0x110
[    6.414571] [<ffffffff8082f9ac>] driver_probe_device+0x36/0xba
[    6.420452] [<ffffffff8082fbbc>] __driver_attach+0xbc/0x19e
[    6.426078] [<ffffffff8082d774>] bus_for_each_dev+0x58/0xa6
[    6.431704] [<ffffffff8082f05a>] driver_attach+0x1a/0x22
[    6.437046] [<ffffffff8082e842>] bus_add_driver+0xf6/0x1fe
[    6.442559] [<ffffffff80830a48>] driver_register+0x3e/0xd8
[    6.448062] [<ffffffff80831c82>] __platform_driver_register+0x1e/0x26
[    6.454557] [<ffffffff80c5c69a>] spacemit_snd_card_init+0x1a/0x22
[    6.460703] [<ffffffff800027aa>] do_one_initcall+0x36/0x218
[    6.466323] [<ffffffff81001452>] kernel_init_freeable+0x22c/0x296
[    6.472434] [<ffffffff80fded84>] kernel_init+0x26/0x116
[    6.477724] [<ffffffff80fe7816>] ret_from_fork+0xe/0x18
[    6.482987] Code: b783 0d0c 6bdc cb89 4789 4481 13e3 f8f9 b783 108c (6bdc) ffb5 
[    6.490590] ---[ end trace 0000000000000000 ]---
[    6.495262] Kernel panic - not syncing: Attempted to kill init! exitcode=0x0000000b
[    6.502964] SMP: stopping secondary CPUs
[    6.506930] ---[ end Kernel panic - not syncing: Attempted to kill init! exitcode=0x0000000b ]---
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test failed.
