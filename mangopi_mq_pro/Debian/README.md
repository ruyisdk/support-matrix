---
sys: debian
sys_ver: null
sys_var: null

status: basic
last_update: 2025-03-03
---

# Debian MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download Link: https://popolon.org/depots/RISC-V/D1/ovsienko/RVBoards_D1_Debian_lxde_img_linux_v0.4.1.img.zip
- Reference Installation Document: https://popolon.org/depots/RISC-V/D1/ovsienko/_index.html

### Hardware Information

- MangoPi MQ Pro
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `unzip` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
unzip /path/to/RVBoards_D1_Debian_lxde_img_linux_v0.4.1.img.zip
sudo dd if=/path/to/RVBoards_D1_Debian_lxde_img_linux_v0.4.1.img of=/dev/your_device bs=1M status=progress
```

### Logging into the System

Plug in the power via the USB-C "OTG" port (instead of "HOST") to avoid issues with faulty power supply (see https://forums.100ask.net/t/topic/876/6).

Logging into the system via the serial port.

Default username: `root`
Default password: `rvboards`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted normally and login via the onboard serial port is also successful.

An faulty, glitched (thus practically unusable) instance of LightDM / LXDE is available through the onboard miniHDMI port when connected to a monitor.

### Boot Log

```log
Welcome to Debian GNU/Linux 11 (bullseye)!

[    4.803783] systemd[1]: Set hostname to <RVBoards>.
[    6.274624] systemd[1]: /lib/systemd/system/plymouth-start.service:16: Unit configured to use KillMode=none. This is unsafe, as it disables systemd's process lifecycle management for the service. Please update your service to use a safer KillMode=, such as 'mixed' or 'control-group'. Support for KillMode=none is deprecated and will eventually be removed.
[    6.495490] systemd[1]: Queued start job for default target Graphical Interface.
[    6.506242] random: systemd: uninitialized urandom read (16 bytes read)
[    6.514170] systemd[1]: system-getty.slice: unit configures an IP firewall, but the local system does not support BPF/cgroup firewalling.
[    6.528131] systemd[1]: (This warning is only shown for the first unit using IP firewalling.)
[    6.539148] systemd[1]: Created slice system-getty.slice.
[  OK  ] Created slice system-getty.slice.
[    6.572593] random: systemd: uninitialized urandom read (16 bytes read)
[    6.581085] systemd[1]: Created slice system-modprobe.slice.
[  OK  ] Created slice system-modprobe.slice.
[    6.602339] 
[    6.602339] insmod_device_driver
[    6.602339] 
[    6.612601] random: systemd: uninitialized urandom read (16 bytes read)
[    6.621028] systemd[1]: Created slice system-serial\x2dgetty.slice.
[  OK  ] Created slice system-serial\x2dgetty.slice.
[    6.663362] systemd[1]: Created slice User and Session Slice.
[  OK  ] Created slice User and Session Slice.
[    6.703154] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[  OK  ] Started Forward Password R…uests to Wall Directory Watch.
[    6.742961] systemd[1]: Condition check resulted in Arbitrary Executable File Formats File System Automount Point being skipped.
[    6.756764] systemd[1]: Reached target Remote File Systems.
[  OK  ] Reached target Remote File Systems.
[    6.792723] systemd[1]: Reached target Slices.
[  OK  ] Reached target Slices.
[    6.822825] systemd[1]: Reached target Swap.
[  OK  ] Reached target Swap.
[    6.854731] systemd[1]: Listening on Syslog Socket.
[  OK  ] Listening on Syslog Socket.
[    6.893486] systemd[1]: Listening on fsck to fsckd communication Socket.
[  OK  ] Listening on fsck to fsckd communication Socket.
[    6.933100] systemd[1]: Listening on initctl Compatibility Named Pipe.
[  OK  ] Listening on initctl Compatibility Named Pipe.
[    6.998954] systemd[1]: Condition check resulted in Journal Audit Socket being skipped.
[    7.009153] systemd[1]: Listening on Journal Socket (/dev/log).
[  OK  ] Listening on Journal Socket (/dev/log).
[    7.043707] systemd[1]: Listening on Journal Socket.
[  OK  ] Listening on Journal Socket.
[    7.083824] systemd[1]: Listening on udev Control Socket.
[  OK  ] Listening on udev Control Socket.
[    7.123454] systemd[1]: Listening on udev Kernel Socket.
[  OK  ] Listening on udev Kernel Socket.
[    7.163336] systemd[1]: Condition check resulted in Huge Pages File System being skipped.
[    7.173259] systemd[1]: Condition check resulted in POSIX Message Queue File System being skipped.
[    7.187383] systemd[1]: Mounting Kernel Debug File System...
         Mounting Kernel Debug File System...
[    7.233368] systemd[1]: Condition check resulted in Kernel Trace File System being skipped.
[    7.246056] systemd[1]: Condition check resulted in Create list of static device nodes for the current kernel being skipped.
[    7.263965] systemd[1]: Starting Load Kernel Module configfs...
         Starting Load Kernel Module configfs...
[    7.306904] systemd[1]: Starting Load Kernel Module drm...
         Starting Load Kernel Module drm...
[    7.356860] systemd[1]: Starting Load Kernel Module fuse...
         Starting Load Kernel Module fuse...
[    7.405367] systemd[1]: Condition check resulted in Set Up Additional Binary Formats being skipped.
[    7.419691] systemd[1]: Starting File System Check on Root Device...
         Starting File System Check on Root Device...
[    7.446874] systemd[1]: Starting Journal Service...
         Starting Journal Service...
[    7.513299] systemd[1]: Starting Load Kernel Modules...
         Starting Load Kernel Modules...
[    7.556719] systemd[1]: Starting Coldplug All udev Devices...
         Starting Coldplug All udev Devices...
[    7.654192] systemd[1]: Mounted Kernel Debug File System.
[  OK  ] Mounted Kernel Debug File System.
[    7.700124] systemd[1]: modprobe@configfs.service: Succeeded.
[    7.755664] systemd[1]: Finished Load Kernel Module configfs.
[  OK  ] Finished Load Kernel Module configfs.
[    7.814371] systemd[1]: modprobe@drm.service: Succeeded.
[    7.856714] systemd[1]: Finished Load Kernel Module drm.
[  OK  ] Finished Load Kernel Module drm.
[    7.915678] systemd[1]: modprobe@fuse.service: Succeeded.
[    7.943690] systemd[1]: Finished Load Kernel Module fuse.
[  OK  ] Finished Load Kernel Module fuse.
[    7.974834] systemd[1]: Finished File System Check on Root Device.
[  OK  ] Finished File System Check on Root Device.
[    8.004868] systemd[1]: Finished Load Kernel Modules.
[  OK  ] Finished Load Kernel Modules.
[    8.044856] systemd[1]: Condition check resulted in FUSE Control File System being skipped.
[    8.086382] systemd[1]: Mounting Kernel Configuration File System...
         Mounting Kernel Configuration File System...
[    8.156481] systemd[1]: Started File System Check Daemon to report status.
[  OK  ] Started File System Check Daemon to report status.
[    8.186763] systemd[1]: Starting Remount Root and Kernel File Systems...
         Starting Remount Root and Kernel File Systems...
[    8.246333] systemd[1]: Starting Apply Kernel Variables...
         Starting Apply Kernel Variables...
[    8.318484] systemd[1]: Started Journal Service.
[  OK  ] Started Journal Service.
[  OK  ] Mounted Kernel Configuration File System.
[    8.450809] EXT4-fs (mmcblk0p5): re-mounted. Opts: (null)
[  OK  ] Finished Remount Root and Kernel File Systems.
         Starting Flush Journal to Persistent Storage...
         Starting Load/Save Random Seed...
         Starting Create System Users...
[  OK  ] Finished Apply Kernel Variables.
[    8.803143] systemd-journald[98]: Received client request to flush runtime journal.
[    8.831851] systemd-journald[98]: File /var/log/journal/a08b1f8fb88040d7bd4028b1be2c5583/system.journal corrupted or uncleanly shut down, renaming and replacing.
[  OK  ] Finished Create System Users.
         Starting Create Static Device Nodes in /dev...
[  OK  ] Finished Flush Journal to Persistent Storage.
[  OK  ] Finished Create Static Device Nodes in /dev.
[  OK  ] Reached target Local File Systems (Pre).
[  OK  ] Reached target Local File Systems.
         Starting Tell Plymouth To Write Out Runtime Data...
         Starting Create Volatile Files and Directories...
         Starting Rule-based Manage…for Device Events and Files...
[  OK  ] Finished Tell Plymouth To Write Out Runtime Data.
[  OK  ] Finished Create Volatile Files and Directories.
         Starting Network Time Synchronization...
         Starting Update UTMP about System Boot/Shutdown...
[   10.064650] proc: Bad value for 'hidepid'
[  OK  ] Finished Coldplug All udev Devices.
         Starting Helper to synchronize boot up for ifupdown...
[  OK  ] Finished Update UTMP about System Boot/Shutdown.
[  OK  ] Started Rule-based Manager for Device Events and Files.
         Starting Show Plymouth Boot Screen...
[  OK  ] Started Show Plymouth Boot Screen.
[  OK  ] Started Forward Password R…s to Plymouth Directory Watch.
[  OK  ] Reached target Local Encrypted Volumes.
[  OK  ] Reached target Paths.
[  OK  ] Started Network Time Synchronization.
[  OK  ] Reached target System Initialization.
[  OK  ] Started Daily Cleanup of Temporary Directories.
[  OK  ] Reached target System Time Set.
[  OK  ] Reached target System Time Synchronized.
[  OK  ] Started Trigger anacron every hour.
[  OK  ] Started Daily apt download activities.
[  OK  ] Started Daily apt upgrade and clean activities.
[  OK  ] Started Periodic ext4 Onli…ata Check for All Filesystems.
[  OK  ] Started Daily exim4-base housekeeping.
[  OK  ] Started Discard unused blocks once a week.
[  OK  ] Started Daily rotation of log files.
[  OK  ] Started Daily man-db regeneration.
[  OK  ] Reached target Timers.
[  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
[  OK  ] Listening on D-Bus System Message Bus Socket.
[  OK  ] Reached target Sockets.
[  OK  ] Reached target Basic System.
[  OK  ] Started Run anacron jobs.
         Starting Avahi mDNS/DNS-SD Stack...
[  OK  ] Started Regular background program processing daemon.
[  OK  ] Started D-Bus System Message Bus.
         Starting Connection service...
         Starting DUN service...
         Starting Remove Stale Onli…t4 Metadata Check Snapshots...
         Starting Telephony service...
         Starting Authorization Manager...
         Starting System Logging Service...
         Starting User Login Management...
         Starting Disk Manager...
         Starting WPA supplicant...
[   14.015124] proc: Bad value for 'hidepid'
[  OK  ] Started System Logging Service.
[  OK  ] Found device /dev/ttyS0.
[  OK  ] Started Telephony service.
[  OK  ] Started Avahi mDNS/DNS-SD Stack.
[  OK  ] Started DUN service.
[  OK  ] Started WPA supplicant.
[  OK  ] Started Authorization Manager.
[  OK  ] Started Connection service.
[  OK  ] Started User Login Management.
[  OK  ] Started Disk Manager.
[  OK  ] Reached target Hardware activated USB gadget.
[  OK  ] Listening on Load/Save RF …itch Status /dev/rfkill Watch.
         Starting Modem Manager...
         Starting Save/Restore Sound Card State...
         Starting Wait for network to be configured by ConnMan...
         Starting Load/Save RF Kill Switch Status...
[   19.227608] sunxi-rfkill soc@3000000:rfkill@0: set block: 0
[   19.266550] sunxi-rfkill soc@3000000:rfkill@0: bt power on success
[  OK  ] Finished Save/Restore Sound Card State.
[  OK  ] Reached target Sound Card.
[  OK  ] Started Load/Save RF Kill Switch Status.
[  OK  ] Started Modem Manager.
         Starting Hostname Service...
[  OK  ] Found device /sys/subsystem/net/devices/eth0.
[  OK  ] Finished Helper to synchronize boot up for ifupdown.
[  OK  ] Started ifup for eth0.
         Starting Raise network interfaces...
[   21.449224] libphy: 4500000.eth: probed
[   21.461532] sunxi-gmac 4500000.eth eth0: eth0: Type(8) PHY ID 0000ffff at 0 IRQ poll (4500000.eth-0:00)
[   21.490055] sunxi-gmac 4500000.eth eth0: Initialize hardware error
[   21.497123] ------------[ cut here ]------------
[   21.502274] called from state READY
[   21.509231] WARNING: CPU: 0 PID: 148 at drivers/net/phy/phy.c:839 phy_stop+0x72/0x82
[   21.518749] Modules linked in:
[   21.522202] CPU: 0 PID: 148 Comm: connmand Tainted: G        W         5.4.61 #12
[   21.531906] sepc: ffffffe000360f5c ra : ffffffe000360f5c sp : ffffffe0391b7b20
[   21.540947]  gp : ffffffe0008ddafc tp : ffffffe039114200 t0 : ffffffe0008ebf78
[   21.549902]  t1 : 0000000000000064 t2 : 0000000000000000 s0 : ffffffe0391b7b50
[   21.558988]  s1 : ffffffe03c267000 a0 : 0000000000000017 a1 : ffffffe000848ed0
[   21.567938]  a2 : ffffffe000852230 a3 : 0000000000000000 a4 : 0000000000000000
[   21.576955]  a5 : 0000000000000000 a6 : 00000000000001b7 a7 : 0000000000000000
[   21.586069]  s2 : 0000000000000002 s3 : 0000000000001000 s4 : 0000000000000001
[   21.595042]  s5 : 0000000000001000 s6 : fffffffffffff000 s7 : ffffffe03c267000
[   21.604044]  s8 : ffffffe03b2dd000 s9 : 0000000000000000 s10: 0000002ae4a89850
[   21.612100]  s11: 0000003fc7d65830 t3 : ffffffe0008e7b00 t4 : 0000000000002950
[   21.621489]  t5 : 0000000000002950 t6 : ffffffe0008e807e
[   21.628314] sstatus: 0000000200000120 sbadaddr: 0000000000000000 scause: 0000000000000003
[   21.638449] ---[ end trace f2c8aec3bb60bcbe ]---
[   21.875080] proc: Bad value for 'hidepid'
[  OK  ] Started Hostname Service.
[   22.982736] libphy: 4500000.eth: probed
[   22.995943] sunxi-gmac 4500000.eth eth0: eth0: Type(8) PHY ID 0000ffff at 0 IRQ poll (4500000.eth-0:00)
[   23.021677] sunxi-gmac 4500000.eth eth0: Initialize hardware error
[   23.028776] ------------[ cut here ]------------
[   23.036583] called from state READY
[   23.040526] WARNING: CPU: 0 PID: 148 at drivers/net/phy/phy.c:839 phy_stop+0x72/0x82
[   23.050591] Modules linked in:
[   23.054990] CPU: 0 PID: 148 Comm: connmand Tainted: G        W         5.4.61 #12
[   23.064281] sepc: ffffffe000360f5c ra : ffffffe000360f5c sp : ffffffe0391b7b20
[   23.073212]  gp : ffffffe0008ddafc tp : ffffffe039114200 t0 : ffffffe0008ec670
[   23.081298]  t1 : 0000000000000064 t2 : 0000000000000000 s0 : ffffffe0391b7b50
[   23.090601]  s1 : ffffffe03c267000 a0 : 0000000000000017 a1 : 000000000000000a
[   23.099628]  a2 : 0000000000000109 a3 : 0000000000000007 a4 : 0000000000000001
[   23.108582]  a5 : 0000000000000000 a6 : 00000000000001cd a7 : 0000000000000000
[   23.117598]  s2 : 0000000000000002 s3 : 0000000000001000 s4 : 0000000000000001
[   23.126663]  s5 : 0000000000001000 s6 : fffffffffffff000 s7 : ffffffe03c267000
[   23.135679]  s8 : ffffffe03b2dd000 s9 : 0000000000000000 s10: 0000002ae4a89850
[   23.144615]  s11: 0000003fc7d65830 t3 : ffffffe0008e7b00 t4 : 0000000000002258
[   23.153637]  t5 : 0000000000002258 t6 : ffffffe0008e807e
[   23.159562] sstatus: 0000000200000120 sbadaddr: 0000000000000000 scause: 0000000000000003
[   23.170097] ---[ end trace f2c8aec3bb60bcbf ]---
[   24.204585] libphy: 4500000.eth: probed
[   24.217795] sunxi-gmac 4500000.eth eth0: eth0: Type(8) PHY ID 0000ffff at 0 IRQ poll (4500000.eth-0:00)
[   24.244657] sunxi-gmac 4500000.eth eth0: Initialize hardware error
[   24.251584] ------------[ cut here ]------------
[   24.259524] called from state READY
[   24.264430] WARNING: CPU: 0 PID: 302 at drivers/net/phy/phy.c:839 phy_stop+0x72/0x82
[   24.274089] Modules linked in:
[   24.277510] CPU: 0 PID: 302 Comm: ip Tainted: G        W         5.4.61 #12
[   24.286565] sepc: ffffffe000360f5c ra : ffffffe000360f5c sp : ffffffe0352bf3e0
[   24.295599]  gp : ffffffe0008ddafc tp : ffffffe038ee9600 t0 : 0000000000000000
[   24.304604]  t1 : 0000000001806000 t2 : 0000000000000000 s0 : ffffffe0352bf410
[   24.313558]  s1 : ffffffe03c267000 a0 : 0000000000000017 a1 : ffffffe000848ed0
[   24.321643]  a2 : ffffffe000852230 a3 : 0000000000000000 a4 : 0000000000000000
[   24.343999]  a5 : 0000000000000000 a6 : 000000000001007e a7 : ffffffe038ea3cb8
[   24.352086]  s2 : 0000000000000002 s3 : 0000000000001000 s4 : 0000000000000001
[   24.375395]  s5 : 0000000000001000 s6 : fffffffffffff000 s7 : ffffffe039099410
[   24.384493]  s8 : ffffffe0352bf850 s9 : 0000000000000000 s10: 0000000000000000
[   24.393757]  s11: 0000000000000000 t3 : 0000000000000001 t4 : 0000000000000000
[   24.401843]  t5 : 0000000000000001 t6 : 0000000000000000
[   24.409079] sstatus: 0000000200000120 sbadaddr: 0000000000000000 scause: 0000000000000003
[   24.419351] ---[ end trace f2c8aec3bb60bcc0 ]---
[  OK  ] Finished Remove Stale Onli…ext4 Metadata Check Snapshots.
[   32.062354] random: crng init done
[   32.066169] random: 7 urandom warning(s) missed due to ratelimiting
[  OK  ] Finished Load/Save Random Seed.
[   33.122345] usb1-vbus: disabling
[  OK  ] Finished Raise network interfaces.
[  OK  ] Reached target Network.
         Starting OpenBSD Secure Shell server...
         Starting Permit User Sessions...
[  OK  ] Finished Permit User Sessions.
         Starting Light Display Manager...
[  113.216494] [SNDCODEC][sunxi_card_hw_params][620]:stream_flag: 1
[  113.276053] [SNDCODEC][sunxi_card_hw_params][620]:stream_flag: 1
[  113.286180] [SNDCODEC][sunxi_card_hw_params][620]:stream_flag: 1
[  113.305940] [SNDCODEC][sunxi_card_hw_params][620]:stream_flag: 0
[  113.333601] [SNDCODEC][sunxi_card_hw_params][620]:stream_flag: 0
[  113.345243] [SNDCODEC][sunxi_card_hw_params][620]:stream_flag: 0
[  113.355956] [SNDCODEC][sunxi_card_hw_params][620]:stream_flag: 0
[  113.365112] [SNDCODEC][sunxi_card_hw_params][620]:stream_flag: 1
[  113.385019] [SNDCODEC][sunxi_card_hw_params][620]:stream_flag: 1
[  113.395754] [SNDCODEC][sunxi_card_hw_params][620]:stream_flag: 1
[  113.405748] [SNDCODEC][sunxi_card_hw_params][620]:stream_flag: 0
[  113.416107] [SNDCODEC][sunxi_card_hw_params][620]:stream_flag: 1
[  113.426753] [SNDCODEC][sunxi_card_hw_params][620]:stream_flag: 1
[  113.437490] [SNDCODEC][sunxi_card_hw_params][620]:stream_flag: 1
[  113.448536] [SNDCODEC][sunxi_card_hw_params][620]:stream_flag: 0
[  113.458671] [SNDCODEC][sunxi_card_hw_params][620]:stream_flag: 1
[  113.469422] [SNDCODEC][sunxi_card_hw_params][620]:stream_flag: 1
[  113.480100] [SNDCODEC][sunxi_card_hw_params][620]:stream_flag: 1
[  113.517530] [SNDCODEC][sunxi_card_hw_params][620]:stream_flag: 0
[  113.590316] [SNDCODEC][sunxi_card_hw_params][620]:stream_flag: 1
[  115.016470] raw_flag value is 0
[  115.020023] sunxi->update_param:1
[  115.025241] WARN:audio is not on
[  115.028845] HDMI Audio Enable Successfully
[  115.064306] raw_flag value is 0
[  115.067856] sunxi->update_param:1
[  115.071556] WARN:audio is not on
[  115.076848] HDMI Audio Enable Successfully
[  115.094181] raw_flag value is 0
[  115.097986] sunxi->update_param:1
[  115.101691] WARN:audio is not on
[  115.107218] HDMI Audio Enable Successfully
[  115.115537] raw_flag value is 0
[  115.143905] raw_flag value is 0
[  115.147455] sunxi->update_param:1
[  115.151156] WARN:audio is not on
[  115.156470] HDMI Audio Enable Successfully
[  115.175361] raw_flag value is 0
[  115.178910] sunxi->update_param:1
[  115.183977] WARN:audio is not on
[  115.187609] HDMI Audio Enable Successfully
[  115.205054] raw_flag value is 0
[  115.208602] sunxi->update_param:1
[  115.222384] WARN:audio is not on
[  115.225986] HDMI Audio Enable Successfully
[  115.244347] raw_flag value is 0
[  115.250215] raw_flag value is 0
[  115.255148] sunxi->update_param:1
[  115.258851] WARN:audio is not on
[  115.263812] HDMI Audio Enable Successfully
[  115.270808] raw_flag value is 0
[  115.275952] sunxi->update_param:1
[  115.279657] WARN:audio is not on
[  115.291164] HDMI Audio Enable Successfully
[  115.299236] raw_flag value is 0
[  115.303728] sunxi->update_param:1
[  115.307432] WARN:audio is not on
[  115.311025] HDMI Audio Enable Successfully
[  115.329731] raw_flag value is 0
[  115.333500] sunxi->update_param:1
[  115.337206] WARN:audio is not on
[  115.340800] HDMI Audio Enable Successfully
[  115.354733] raw_flag value is 0
[  115.358280] sunxi->update_param:1
[  115.361980] WARN:audio is not on
[  115.367444] HDMI Audio Enable Successfully
[  115.375273] raw_flag value is 0
[  115.378823] sunxi->update_param:1
[  115.383975] WARN:audio is not on
[  115.387579] HDMI Audio Enable Successfully
[  115.396081] raw_flag value is 0
[  115.399664] sunxi->update_param:1
[  115.412387] WARN:audio is not on
[  115.416019] HDMI Audio Enable Successfully
[  115.433940] raw_flag value is 0
[  115.437490] sunxi->update_param:1
[  115.441190] WARN:audio is not on
[  115.446555] HDMI Audio Enable Successfully
[  115.454543] raw_flag value is 0
[  115.458092] sunxi->update_param:1
[  115.461792] WARN:audio is not on
[  115.467336] HDMI Audio Enable Successfully
[  115.475248] raw_flag value is 0
[  115.478794] sunxi->update_param:1
[  115.483816] WARN:audio is not on
[  115.487420] HDMI Audio Enable Successfully
[  115.507771] raw_flag value is 0
[  115.588486] raw_flag value is 0
[FAILED] Failed to start Wait for n…k to be configured by ConnMan.
[  139.156996] rc.local[456]: led
[  144.205370] rc.local[711]: resize2fs 1.46.2 (28-Feb-2021)
[  144.242548] rc.local[711]: The filesystem is already 1048576 (4k) blocks long.  Nothing to do!
[  145.578959] ======== XRADIO WIFI OPEN ========
[  145.584702] [XRADIO] Driver Label:XR_V02.16.84_P2P_HT40_01.31   
[  145.591484] [XRADIO] Allocated hw_priv @ 000000002508eb6b
[  145.605906] sunxi-rfkill soc@3000000:rfkill@0: bus_index: 1
[  145.623944] sunxi-rfkill soc@3000000:rfkill@0: wlan power on success
[  145.832793] [XRADIO] Detect SDIO card 1
[  147.922434] sunxi-rfkill soc@3000000:rfkill@0: wlan power off success
[  148.034261] [XRADIO] Remove SDIO card 1
[  148.049234] [SBUS_ERR] sdio probe timeout!
[  148.053924] [XRADIO_ERR] sbus_sdio_init failed
[  148.061794] xradio_core_init failed (-110)!
[  148.152435] rc.local[712]: insmod: ERROR: could not insert module /lib/modules/5.4.61/xr829.ko: Connection timed out
[  148.248022] usbcore: registered new interface driver uvcvideo
[  148.259704] USB Video Class driver (1.1.1)
[  148.311535] rc.local[721]: Successfully initialized wpa_supplicant
[  148.380408] rc.local[721]: Could not read interface wlan0 flags: No such device
[  148.410884] rc.local[721]: nl80211: Driver d[  148.416965] disp 0, type 4, mode5
oes not support authentication/association or connect commands
[  148.450698] rc.local[721]: nl80211: deinit ifname=wlan0 disabled_11b_rates=0
[  148.481626] rc.local[721]: Could not read interface wlan0 flags: No such device
[  148.511015] rc.local[721]: wlan0: Failed to initialize driver interface
[  148.542156] rc.local[456]: hdmi init start
[  149.432360] [HDMI receive params]: tv mode: 0x5 format:0x1 data bits:0x0 eotf:0x4 cs:0x101 dvi_hdmi:2 range:2 scan:0 aspect_ratio:8
[  149.445591] [HDMI2 error]: sink do not support this mode:4
[  150.482386] disp_al_manager_apply ouput_type:0
[  150.488064] disp_al_hdmi_cfg
[  150.602523] HDMI Audio Enable Successfully
[  150.607099] [DISP] disp_device_attached_and_enable,line:233:
[  150.607104] attached ok, mgr0<-->dev0
[  150.619105] [DISP] disp_device_attached_and_enable,line:236:
[  150.619117] type:4,mode:5,fmt:yuv444,bits:8bits,eotf:4,cs:257 dvi_hdmi:2, range:2 scan:0 ratio:8
[  150.638061] rc.local[456]: hdmi init end

Debian GNU/Linux 11 RVBoards ttyS0

RVBoards login: root
Password: 
Linux RVBoards 5.4.61 #12 PREEMPT Thu Jun 3 08:39:01 UTC 2021 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed May 19 18:39:03 CST 2021 on ttyS0
root@RVBoards:~# uname -a
Linux RVBoards 5.4.61 #12 PREEMPT Thu Jun 3 08:39:01 UTC 2021 riscv64 GNU/Linux
root@RVBoards:~# cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 11 (bullseye)"
NAME="Debian GNU/Linux"
VERSION_ID="11"
VERSION="11 (bullseye)"
VERSION_CODENAME=bullseye
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@RVBoards:~# 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.