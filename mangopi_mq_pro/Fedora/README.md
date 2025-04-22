---
sys: fedora
sys_ver: "33"
sys_var: null

status: basic
last_update: 2025-03-03
---

# Fedora MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download Link: https://mirror.iscas.ac.cn/fedora-riscv/old_dl/Allwinner/Nezha_D1/images-release/Fedora/fedora-riscv64-d1-developer-xfce-rawhide-Rawhide-20220117-135925.n.0-sda.raw.zst
- Reference Installation Document: https://popolon.org/depots/RISC-V/D1/ovsienko/_index.html

### Hardware Information

- MangoPi MQ Pro
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

The system booted normally and login via the onboard serial port is also successful.

### Boot Log

```log
[  OK  ] Started Load/Save RF Kill Switch Status.
[  OK  ] Started Network Manager Script Dispatcher Service.
[  134.755896] sunxi-rfkill soc@3000000:rfkill@0: set block: 1
[  134.868537] sunxi-rfkill soc@3000000:rfkill@0: bt power off success
[  135.245383] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  135.268543] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  135.465939] sunxi-rfkill soc@3000000:rfkill@0: set block: 0
[  135.563779] sunxi-rfkill soc@3000000:rfkill@0: bt power on success
[  136.083021] sunxi-rfkill soc@3000000:rfkill@0: set block: 1
[  136.147681] sunxi-rfkill soc@3000000:rfkill@0: bt power off success
[ ***  ] (2 of 2) A start job is running for Network Manager Wait Online (1min 11s / no limit)
[  136.448614] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  136.471940] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  136.748538] sunxi-rfkill soc@3000000:rfkill@0: set block: 0
[  *** ] (2 of 2) A start job is running for Network Manager Wait Online (1min 12s / no limit)
[  136.970112] libphy: 4500000.eth: probed
[  137.031617] sunxi-gmac 4500000.eth eth0: eth0: Type(8) PHY ID 0000ffff at 0 IRQ poll (4500000.eth-0:00)
[  137.092358] sunxi-gmac 4500000.eth eth0: Initialize hardware error
[  137.119899] ------------[ cut here ]------------
[  137.149065] called from state READY
[  137.175128] WARNING: CPU: 0 PID: 536 at drivers/net/phy/phy.c:839 phy_stop+0x84/0x94
[  137.205914] Modules linked in: ip_set nfnetlink ebtable_filter ebtables xradio_btlpm snd_soc_sunxi_daudio snd_soc_sunxi_dmic snd_soc_sunxi_simple_card snd_soc_sunxi_hdmi snd_soc_simple_card_utils snd_soc_sunxi snd_soc_dmic bluetooth ecdh_generic ecc zram i2c_dev libarc4 cfg80211
[  137.286964] CPU: 0 PID: 536 Comm: NetworkManager Not tainted 5.4.61 #5
[  137.314899] sepc: ffffffe00077a900 ra : ffffffe00077a900 sp : ffffffe07aef7380
[   **[  137.374847]  t1 : 0000000001806000 t2 : 0000000000000000 s0 : ffffffe07aef73b0
*] (2 of 2) A start job is running for Network Manage[  137.402735]  s1 : ffffffe078249000 a0 : 0000000000000017 a1 : ffffffe0010ced78
r Wait Online (1min 12s / no limit)
[  137.433458]  a2 : ffffffe0010eb050 a3 : 0000000000000000 a4 : 0000000000000000
[  137.458643]  a5 : 0000000000000000 a6 : 00000000000101a8 a7 : 0000000000000003
[  137.483899] sunxi-rfkill soc@3000000:rfkill@0: set block: 1
[  137.511208]  s2 : 0000000000000002 s3 : ffffffe078249000 s4 : 0000000000001000
[  137.544439] sunxi-rfkill soc@3000000:rfkill@0: bt power off success
[  137.575899]  s5 : 0000000000001000 s6 : fffffffffffff000 s7 : ffffffe07aef7640
[  137.633791]  s8 : ffffffe0786d0410 s9 : 0000000000000000 s10: 0000000000000000
[  137.657869] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  137.682714] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  137.741446]  s11: 0000000000000000 t3 : 0000000000000000 t4 : 0000000048d12000
[  137.771703]  t5 : 0000000000000003 t6 : 0000000000000001
[  137.799471] sstatus: 0000000200000120 sbadaddr: 0000000000000000 scause: 0000000000000003
[    **] (1 of 2) A start job is running for /etc/rc.d/rc.local Compatibility (1min 13s / no limit)
[  138.123493] sunxi-rfkill soc@3000000:rfkill@0: set block: 0
[     *] (1 of 2) A start job is running for /etc/rc.d/rc.local Compatibility (1min 13s / no limit)
[  138.811730] sunxi-rfkill soc@3000000:rfkill@0: set block: 1
[  138.857768] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[    **] (1 of 2) A start job is running for /etc/rc.d/rc.local Compatibility (1min 14s / no limit)
[   ***] (2 of 2) A start job is running for Network Manager Wait Online (1min 14s / no limit)
[  139.517676] sunxi-rfkill soc@3000000:rfkill@0: set block: 0
[  *** ] (2 of 2) A start job is running for Network Manager Wait Online (1min 15s / no limit)
[  140.060932] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  140.086800] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  140.133816] sunxi-rfkill soc@3000000:rfkill@0: set block: 1
[ ***  ] (2 of 2) A start job is running for Network Manager Wait Online (1min 15s / no limit)
[***   ] (1 of 2) A start job is running for /etc/rc.d/rc.local Compatibility (1min 16s / no limit)
[  140.936792] sunxi-rfkill soc@3000000:rfkill@0: bt power on success
[  141.053863] libphy: 4500000.eth: probed
[  141.123076] sunxi-gmac 4500000.eth eth0: eth0: Type(8) PHY ID 0000ffff at 0 IRQ poll (4500000.eth-0:00)
[  141.183561] sunxi-gmac 4500000.eth eth0: Initialize hardware error
[  141.233412] ------------[ cut here ]------------
[  141.268480] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  141.295030] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  141.328335] called from state READY
[**    ] (1 of 2) A start job is running for /etc/rc.d/rc.local Compatibility (1min 16s / no limit)
[  141.393525] Modules linked in: ip_set nfnetlink ebtable_filter ebtables xradio_btlpm snd_soc_sunxi_daudio snd_soc_sunxi_dmic snd_soc_sunxi_simple_card snd_soc_sunxi_hdmi snd_soc_simple_card_utils snd_soc_sunxi snd_soc_dmic bluetooth ecdh_generic ecc zram i2c_dev libarc4 cfg80211
[  141.530622] CPU: 0 PID: 536 Comm: NetworkManager Tainted: G        W         5.4.61 #5
[  141.581610] sepc: ffffffe00077a900 ra : ffffffe00077a900 sp : ffffffe07aef7380
[  141.613535]  gp : ffffffe001268958 tp : ffffffe072009c40 t0 : 0000000000000000
[  141.641304] sunxi-rfkill soc@3000000:rfkill@0: set block: 1
[  141.693465] sunxi-rfkill soc@3000000:rfkill@0: bt power off success
[  141.735301]  t1 : 0000000001806000 t2 : 0000000000000000 s0 : ffffffe07aef73b0
[  141.793811]  s1 : ffffffe07271a800 a0 : 0000000000000017 a1 : ffffffe0010ced78
[*     ] (1 of 2) A start job is running fo[  141.892475]  a5 : 0000000000000000 a6 : 0000000000010281 a7 : 0000000000020000
r /etc/rc.d/rc.local Compatibility (1min 17s / no limit)
[  141.953445]  s2 : 0000000000000002 s3 : ffffffe07271a800 s4 : 0000000000001000
[  141.992395]  s5 : 0000000000001000 s6 : fffffffffffff000 s7 : ffffffe07aef7640
[  142.053628]  s8 : ffffffe00887ae10 s9 : 0000000000000000 s10: 0000000000000000
[  142.091424]  s11: 0000000000000000 t3 : 0000000000000001 t4 : 0000000000000049
[  142.150113]  t5 : 0000000000000003 t6 : 0000000000000001
[  142.196130] sstatus: 0000000200000120 sbadaddr: 0000000000000000 scause: 0000000000000003
[  142.233495] ---[ end trace 587bb8eaea7bff61 ]---
[**    ] (2 of 2) A start job is running for Network Manager Wait Online (1min 17s / no limit)
[  142.430394] sunxi-rfkill soc@3000000:rfkill@0: bt power on success
[  142.470590] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[***   ] (2 of 2) A start job is running for Network Manager Wait Online (1min 18s / no limit)
[  142.982612] sunxi-rfkill soc@3000000:rfkill@0: set block: 1
[ ***  ] (2 of 2) A start job is running for Network Manager Wait Online (1min 18s / no limit)
[  143.655980] sunxi-rfkill soc@3000000:rfkill@0: set block: 0
[  143.681991] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  *** ] (1 of 2) A start job is running for /etc/rc.d/rc.local Compatibility (1min 19s / no limit)
[   ***] (1 of 2) A start job is running for /etc/rc.d/rc.local Compatibility (1min 19s / no limit)
[  144.489257] sunxi-rfkill soc@3000000:rfkill@0: set block: 1
[    **] (1 of 2) A start job is running for /etc/rc.d/rc.local Compatibility (1min 19s / no limit)
[  144.878871] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  OK  ] Started /etc/rc.d/rc.local Compatibility.
[  145.334361] libphy: 4500000.eth: probed
[  145.441759] sunxi-gmac 4500000.eth eth0: eth0: Type(8) PHY ID 0000ffff at 0 IRQ poll (4500000.eth-0:00)
         Starting Light Display Manager...
         Starting Hold until boot process finishes up...
[  145.704171] sunxi-gmac 4500000.eth eth0: Initialize hardware error
[  145.789886] ------------[ cut here ]------------
[  145.874678] called from state READY
[  145.950354] WARNING: CPU: 0 PID: 536 at drivers/net/phy/phy.c:839 phy_stop+0x84/0x94
[  146.023581] Modules linked in: ebtable_nat ebtable_broute ip_set nfnetlink ebtable_filter ebtables xradio_btlpm snd_soc_sunxi_daudio snd_soc_sunxi_dmic snd_soc_sunxi_simple_card snd_soc_sunxi_hdmi snd_soc_simple_card_utils snd_soc_sunxi snd_soc_dmic bluetooth ecdh_generic ecc zram i2c_dev libarc4 cfg80211
[  146.132288] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  146.542370] CPU: 0 PID: 536 Comm: NetworkManager Tainted: G        W         5.4.61 #5
[  146.643623] sepc: ffffffe00077a900 ra : ffffffe00077a900 sp : ffffffe07aef7380
[  146.748365]  gp : ffffffe001268958 tp : ffffffe072009c40 t0 : 0000000000000000
[  146.874664]  t1 : 0000000001806000 t2 : 0000000000000000 s0 : ffffffe07aef73b0
[  146.993478]  s1 : ffffffe078df9000 a0 : 0000000000000017 a1 : ffffffe0010ced78
[  147.098989]  a2 : ffffffe0010eb050 a3 : 0000000000000000 a4 : 0000000000000000
[  147.223927]  a5 : 0000000000000000 a6 : 000000000001033a a7 : ffffffe0791c6b00
[  147.243279]  s2 : 0000000000000002 s3 : ffffffe078df9000 s4 : 0000000000001000
[  147.244100]  s5 : 0000000000001000 s6 : fffffffffffff000 s7 : ffffffe07aef7640
[  147.244106]  s8 : ffffffe00887aa10 s9 : 0000000000000000 s10: 0000000000000000
[  147.244111]  s11: 0000000000000000 t3 : 0000000000000000 t4 : 0000000000000400
[  147.244115]  t5 : 0000000000000003 t6 : 0000000000000001
[  147.244121] sstatus: 0000000200000120 sbadaddr: 0000000000000000 scause: 0000000000000003
[  147.244126] ---[ end trace 587bb8eaea7bff62 ]---
[  147.282819] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  147.301992] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  149.688530] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  149.699390] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  150.533770] libphy: 4500000.eth: probed
[  150.550067] sunxi-gmac 4500000.eth eth0: eth0: Type(8) PHY ID 0000ffff at 0 IRQ poll (4500000.eth-0:00)
[  150.623395] sunxi-gmac 4500000.eth eth0: Initialize hardware error
[  150.630296] ------------[ cut here ]------------
[  150.663476] called from state READY
[  150.667443] WARNING: CPU: 0 PID: 536 at drivers/net/phy/phy.c:839 phy_stop+0x84/0x94
[  150.703409] Modules linked in: ebtable_nat ebtable_broute ip_set nfnetlink ebtable_filter ebtables xradio_btlpm snd_soc_sunxi_daudio snd_soc_sunxi_dmic snd_soc_sunxi_simple_card snd_soc_sunxi_hdmi snd_soc_simple_card_utils snd_soc_sunxi snd_soc_dmic bluetooth ecdh_generic ecc zram i2c_dev libarc4 cfg80211
[  150.793386] CPU: 0 PID: 536 Comm: NetworkManager Tainted: G        W         5.4.61 #5
[  150.802250] sepc: ffffffe00077a900 ra : ffffffe00077a900 sp : ffffffe07aef7380
[  150.843396]  gp : ffffffe001268958 tp : ffffffe072009c40 t0 : ffffffe00128fff8
[  150.851487]  t1 : 0000000000000064 t2 : 0000000000000000 s0 : ffffffe07aef73b0
[  150.889690] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  150.902110] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  150.913416]  s1 : ffffffe079f08000 a0 : 0000000000000017 a1 : 000000000000000a
[  150.921507]  a2 : 0000000000000000 a3 : 0000000000000007 a4 : 0000000000000001
[  150.953421]  a5 : 0000000000000000 a6 : 000000000000037d a7 : 0000000000000006
[  150.961481]  s2 : 0000000000000002 s3 : ffffffe079f08000 s4 : 0000000000001000
[  151.003364]  s5 : 0000000000001000 s6 : fffffffffffff000 s7 : ffffffe07aef7640
[  151.011424]  s8 : ffffffe00887aa10 s9 : 0000000000000000 s10: 0000000000000000
[  151.053400]  s11: 0000000000000000 t3 : ffffffe001273df8 t4 : 0000000000026c10
[  151.061490]  t5 : 0000000000026c10 t6 : ffffffe0012743be
[  151.093422] sstatus: 0000000200000120 sbadaddr: 0000000000000000 scause: 0000000000000003
[  151.102577] ---[ end trace 587bb8eaea7bff63 ]---
[  152.092753] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  152.104694] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  153.297576] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  153.306630] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  154.133866] libphy: 4500000.eth: probed
[  154.152622] sunxi-gmac 4500000.eth eth0: eth0: Type(8) PHY ID 0000ffff at 0 IRQ poll (4500000.eth-0:00)
[  154.243415] sunxi-gmac 4500000.eth eth0: Initialize hardware error
[  154.250345] ------------[ cut here ]------------
[  154.263438] called from state READY
[  154.274128] WARNING: CPU: 0 PID: 536 at drivers/net/phy/phy.c:839 phy_stop+0x84/0x94
[  154.303970] Modules linked in: nf_tables(+) ebtable_nat ebtable_broute ip_set nfnetlink ebtable_filter ebtables xradio_btlpm snd_soc_sunxi_daudio snd_soc_sunxi_dmic snd_soc_sunxi_simple_card snd_soc_sunxi_hdmi snd_soc_simple_card_utils snd_soc_sunxi snd_soc_dmic bluetooth ecdh_generic ecc zram i2c_dev libarc4 cfg80211
[  154.395817] CPU: 0 PID: 536 Comm: NetworkManager Tainted: G        W         5.4.61 #5
[  154.423395] sepc: ffffffe00077a900 ra : ffffffe00077a900 sp : ffffffe07aef7380
[  154.431487]  gp : ffffffe001268958 tp : ffffffe072009c40 t0 : 0000000000000000
[  154.473388]  t1 : 0000000001806000 t2 : 0000000000000000 s0 : ffffffe07aef73b0
[  154.481448]  s1 : ffffffe078d84000 a0 : 0000000000000017 a1 : ffffffe0010ced78
[  154.496833] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  154.508523] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  154.553423]  a2 : ffffffe0010eb050 a3 : 0000000000000000 a4 : 0000000000000000
[  154.561515]  a5 : 0000000000000000 a6 : 0000000000010127 a7 : 0000000000000016
[  154.601746]  s2 : 0000000000000002 s3 : ffffffe078d84000 s4 : 0000000000001000
[  154.634607]  s5 : 0000000000001000 s6 : fffffffffffff000 s7 : ffffffe07aef7640
[  154.642699]  s8 : ffffffe0735df010 s9 : 0000000000000000 s10: 0000000000000000
[  154.678445]  s11: 0000000000000000 t3 : 0000003ff2d62454 t4 : 00000000004b8e58
[  154.701756]  t5 : 0000000000000003 t6 : 0000000000000001
[  154.723546] sstatus: 0000000200000120 sbadaddr: 0000000000000000 scause: 0000000000000003
[  154.732671] ---[ end trace 587bb8eaea7bff64 ]---
[  155.698647] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  155.710723] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  156.905166] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  156.913754] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  158.106846] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  158.115802] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect

Welcome to the Fedora/RISC-V disk image
https://fedoraproject.org/wiki/Architectures/RISC-V

Build date: Tue Nov 16 19:18:13 UTC 2021

Kernel 5.4.61 on an riscv64 (ttyS0)

The root password is 'fedora_rocks!'.
root password logins are disabled in SSH starting Fedora 31.
User 'riscv' with password 'fedora_rocks!' in 'wheel' group is provided.

To install new packages use 'dnf install ...'

To upgrade disk image use 'dnf upgrade --best'

If DNS isn’t working, try editing ‘/etc/yum.repos.d/fedora-riscv.repo’.

For updates and latest information read:
https://fedoraproject.org/wiki/Architectures/RISC-V

Fedora/RISC-V
-------------
Koji:               http://fedora.riscv.rocks/koji/
SCM:                http://fedora.riscv.rocks:3000/
Distribution rep.:  http://fedora.riscv.rocks/repos-dist/
Koji internal rep.: http://fedora.riscv.rocks/repos/
fedora-riscv login: [  159.306184] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  159.318293] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  160.507760] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  160.520863] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  161.710643] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  161.723339] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  162.914269] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  162.925862] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  164.116380] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  164.128390] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  165.319639] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  165.330903] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  166.519770] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  166.533849] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  167.723491] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  167.736825] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  168.925821] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  168.939536] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  170.128350] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  170.142290] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  171.333296] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  171.345185] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  172.537704] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  172.548018] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  173.737875] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  173.750618] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  174.940879] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  174.952911] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  176.141833] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  176.155646] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  177.346021] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  177.358276] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  178.546991] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  178.560614] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  179.750731] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  179.762842] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  180.956654] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  180.965238] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  182.154670] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  182.166859] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  183.359085] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  183.369834] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  184.561563] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  184.572783] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  188.168086] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  188.181073] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  189.372591] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  189.383631] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  190.572415] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  190.586559] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  191.777962] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  191.789440] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  192.979647] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  192.992103] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  194.180414] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  194.194362] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  195.383911] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  195.396611] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  196.586019] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  196.598334] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  197.788088] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  197.801951] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  198.994425] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  199.006088] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  200.196282] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  200.210049] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  201.406484] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  201.415065] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  202.605035] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  202.618073] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
r[  203.814799] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  203.823391] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
iscv
Password: [  205.012192] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  205.026333] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect

[  207.427944] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  207.436528] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  208.624707] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  208.637641] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  209.829582] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  209.841346] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[riscv@fedora-riscv ~]$ [  211.031655] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  211.045481] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  212.237952] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  212.249511] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
unma[  213.440031] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  213.453852] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
un[  214.646559] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  214.658358] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
ame [  215.849629] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  215.862774] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
-a
-bash: ununame: command not found
[riscv@fedora-riscv ~]$ [  217.054295] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  217.067706] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
uname [  218.258678] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  218.272260] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
-a
Linux fedora-riscv 5.4.61 #5 PREEMPT Tue Dec 7 21:35:21 CST 2021 riscv64 riscv64 riscv64 GNU/Linux
[riscv@fedora-riscv ~]$ [  219.462935] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  219.476606] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
ca[  220.670122] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  220.681076] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
t /etc/[  221.878958] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  221.887536] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  223.080242] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  223.090349] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
os-lea[  224.281286] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  224.295093] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  225.485839] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  225.499534] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
cat [  226.694209] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  226.703661] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
/etc/[  227.894337] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  227.907954] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
os-re[  229.098573] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  229.112254] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
lease
-bash: cacat: command not found
[riscv@fedora-riscv ~]$ [  230.302912] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  230.316739] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
cat [  231.512156] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  231.521281] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
/etc[  232.712379] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  232.725600] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
/os[  233.924566] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  233.933143] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
-releas[  235.121550] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  235.134221] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
e
NAME=Fedora
VERSION="33 (Rawhide)"
ID=fedora
VERSION_ID=33
VERSION_CODENAME=""
PLATFORM_ID="platform:f33"
PRETTY_NAME="Fedora 33 (Rawhide)"
ANSI_COLOR="0;34"
LOGO=fedora-logo-icon
CPE_NAME="cpe:/o:fedoraproject:fedora:33"
HOME_URL="https://fedoraproject.org/"
DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora/rawhide/system-administrators-guide/"
SUPPORT_URL="https://fedoraproject.org/wiki/Communicating_and_getting_help"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=rawhide
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=rawhide
PRIVACY_POLICY_URL="https://fedoraproject.org/wiki/Legal:PrivacyPolicy"
[riscv@fedora-riscv ~]$ [  236.330303] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
[  236.338938] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device disconnect
[  237.529814] sunxi-ehci 4200000.ehci1-controller: ehci_irq: highspeed device connect
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
