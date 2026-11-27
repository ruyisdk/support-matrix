---
sys: rtthread
sys_ver: null
sys_var: smart-only
provider: Vendor

status: basic
last_update: 2026-11-25
---

# RT-Smart Only SDK CanMV K230 Test Report

## Test Environment

### Operating System Information

- SDK build: `v0.8-50-gd8f4468`, daily build dated 2026-11-25
- Download link: https://download.kendryte.com/developer/releases/rtos_k230/daily_build/?lang=zh
- Image file: `RtSmart-K230_V1P0_P1_rtsmart_v0.8-50-gd8f4468_nncase_v2.11.0.img.gz`
- Reference Installation Document: https://www.kendryte.com/k230_rtos/zh/main/userguide/how_to_flash.html

### Hardware Information

- Development Board: Canaan Kendryte K230
- Tested hardware revision: v1.1
- A 32 GB microSD card
- USB A to C / USB C to C cable

## Installation Steps

### Flashing Image

Decompress the gzip image and write it to the microSD card. The following commands are for macOS; replace `diskN` with the actual microSD device.

```bash
gzip -dk /path/to/k230.img.gz
diskutil list external physical
diskutil unmountDisk /dev/diskN
sudo dd if=/path/to/k230.img of=/dev/rdiskN bs=4m
sync
diskutil eject /dev/diskN
```

Insert the card while the board is powered off, then connect power. On the first boot, wait for `/data` formatting to finish before restarting or removing power.

### Logging into the System

Connect to the board's first USB serial channel at 115200 baud, 8 data bits, 1 stop bit, no parity, and no flow control. For example, using `tio` on macOS:

```bash
tio -b 115200 -d 8 -s 1 -p none -f none /dev/cu.YOUR_SERIAL_PORT
```

The image starts the SmartIPC example automatically. Press `Ctrl+C` and wait for `RTSP thread exited` to access the `msh />` shell. No username or password was requested.

## Actual Results

The system booted successfully and the serial shell was usable.

Screen recording:

[![asciicast](https://asciinema.org/a/K8vqPMTIgVLHBxGv.svg)](https://asciinema.org/a/K8vqPMTIgVLHBxGv)

Boot log:

```log
msh />reboot
U-Boot SPL 2022.10-00013-ga22d6316 (Nov 19 2026 - 07:19:17 +0000)

OpenSBI v0.9
heap: [0x006312c0 - 0x026312c0], size 32768 KB
page: [0x026312c8 - 0x0fffec00], size 223030 KB
lwIP-2.1.2 initialized!
[I/board.sdio] probing boot storage on SDIO1
[I/sal.skt] Socket Abstraction Layer initialize success, lwIP 2.1.2.
msh />[I/board.sdio] preparing SDIO Wi-Fi socket on host 0
[E/drv_touch] touch probe failed.
[E/drv_touch] Register default touch failed
Probe dummy af driver
find sensor(ov5647_csi0) on csi0
[I/SDIO] SD card capacity 31166976 KB.
found part[0], begin: 115343360, size: 30.0MB
found part[1], begin: 146800640, size: 1.0GB
found part[2], begin: -2147483648, size: 27.740GB
[I/SDIO] sd1: selected timing: SD HS, 4-bit, clock=50000000 Hz
Can't find sensor on csi1
Can't find sensor on csi2
SDK: v0.8-20261125-041046-gitlab-runner-6gndtoqdk-project-1631-concurrent-1-d8f4468, nncase: 2.11.0
Config parameters:
Sensor type: auto-detect
MIPI lane preference: 0
Audio capture enabled: 1
Audio sample rate: 8000
Audio channel count: 1
Video encoder type: h264
Video encoder width: 1280
Video encoder height: 720
Video encoder bitrate (kbps): 2000
Video output connector type: LCD
OSD width: 800
OSD height: 480
Video output width: 800
Video output height: 480
AI input width: 1280
AI input height: 720
AI analysis frame rate: 10
Kmodel file: /sdcard/app/examples/integrated_poc/smart_ipc/face_detection_320.kmodel
Face detection thresh[I/board.sdio] SDIO Wi-Fi socket ready on host 0
old: 0.600000
Face detection NMS threshold: 0.400000
Enable video output: 1
Enable AI analysis: 1
Enable video encoding: 1
Video encoder data source: Sensor Channel
Streaming mode: RTSP
Port: 8554

probe sensor: CSI0 type=7 name=ov5647_csi0 selected=1920x1080@30 lanes=2 requested=1920x1080@30 lane_pref=0 mirror=0 phy_freq=1 hdr_mode=4
detect sensor type: 7
phys_addr is 10000000 osd_pool_id is 0
[I/brcmf.sdio] probing SDIO 02d0:a9a6 with 2 functions on sd0
[I/brcmf.chip] chip 43430 rev 1, RAM 0x00000000+0x80000, 7 cores
[I/WLAN.dev] WLAN device sta registered as phy0-sta
[I/WLAN.dev] WLAN device ap registered as phy0-ap
[I/brcmf.sdio] bound SDIO 02d0:a9a6 as BCM43430A1 (F1 block 64, F2 block 256)
[I/board.sdio] SDIO Wi-Fi card detected on host 0
[I/brcmf.sdio] firmware started on BCM43430A1 with NVRAM nvram.txt
[I/brcmf.proto] SDIO RX glom alignment configured
[I/brcmf.proto] SDIO TX glom enabled (max 32 frames)
@@@@@@@@face detection init took 352.983 ms
kd_mpi_vicap[E/sal.skt] not find ne_set_chn_attr: chn0 adjusted buffer_size: old=0x8cc00, new=0x8d000 (width=800, height=480, format=31)
vicap chn twork interface device by protocol family(2).
[E/sal.skt] SAL socket protocol family input failed, return error -30 set attr success.
vicapaudi chn 1 seo i2s clock frequency is 512000(512000)
audio codec adc clock frequency is 20[I/brcmf.wifi] firmware channels: 13 at 2.4 GHz, 0 at 5 GHz (20 MHz)
t att4 5 GHz ([I/WLAN.dev] wlan init success
20 MHz)r success.
vicap chn 2 set attr success.
.
create rtsp server failed.unable to create stream socket: Address family not supported by protocol
RTSP initialization failed, retrying in 3000 milliseconds...
[I/WLAN.lwip] eth device init ok name:wlan0
[I/WLAN.dev] wlan init success
[I/WLAN.lwip] eth device init ok name:wlan0ap
panel st7701_480x800, pixelclock 27000 khz, resolution 480x800@59
connector init success, connector type: 605274512, width:480,height:800
vo layer init: type 605274512, layer_id 0, width 800, height 480, ratation_90 1
sample_vo_init: layer_id 0, width 800, height 480, pixel_format 31, func 2,buf_nr:2
sample_osd_init: layer_id 7, width 800, height 480, pixel_format 17, func 2, buf_nr:2
@@@@@@_init_vo_layer_osd took 138.271 ms
@@@@@@_start_vi_cap took 45.3367 ms
_venc_vb_create_pool poolid 7
MySmartIPC::start took 242.135 ms
SmartIPC started (RTSP mode, port 8554).
total test took 694.334 ms
[I/rtl8152] RTL8152 attached as eth0, MAC <REDACTED>
rtsp server init ok
with_video
with_audio
g711liveSubSession

"test" stream
Play this stream using the URL "rtsp://0.0.0.0:8554/test"
Default route has no IPv4 address, retrying (1/10)...
Default route has no IPv4 address, retrying (2/10)...
Default route has no IPv4 address, retrying (3/10)...
Default route has no IPv4 address, retrying (4/10)...
Default route has no IPv4 address, retrying (5/10)...
Default route has no IPv4 address, retrying (6/10)...
Default route has no IPv4 address, retrying (7/10)...
Default route has no IPv4 address, retrying (8/10)...
Default route has no IPv4 address, retrying (9/10)...
Default route has no IPv4 address, retrying (10/10)...
Failed to get local IP address
RTSP service started successfully: rtsp://0.0.0.0:8554/test
^Cexit_flag true
RTSP service stopped
ch 0: 512 pictures encoded. Average FrameRate = 15 Fps
ch 0: total used pages 862
vpu_exit_locked>q_wm 0
release reserved vb 281546752
release reserved vb 282701824
release reserved vb 292380672
RTSP thread exited
version
SDK: v0.8-20261125-041046-gitlab-runner-6gndtoqdk-project-1631-concurrent-1-d8f4468
msh />ps
thread               pri  status      sp     stack size max used left tick  error
-------------------- ---  ------- ---------- ----------  ------  ---------- ---
usbh_rtl8152_rx       15  suspend 0x00000588 0x00001000    42%   0x0000000a EINTRPT
usbh_hub0             14  suspend 0x000005b8 0x00002000    24%   0x00000004 EINTRPT
brcmf-tx              12  suspend 0x000007f8 0x00001000    50%   0x0000000a EINTRPT
brcmf-rx              11  suspend 0x00000558 0x00002000    27%   0x00000008 EINTRPT
sdio_irq               4  suspend 0x00000528 0x00002800    19%   0x00000013 EINTRPT
mtp                   16  suspend 0x000004e8 0x00005000    06%   0x0000000a EINTRPT
mtp_inty              16  suspend 0x00000528 0x00005000    06%   0x0000000a EINTRPT
mcm_task               1  suspend 0x000004e8 0x00002000    15%   0x00000005 EINTRPT
vb_release            12  suspend 0x000004f8 0x00002000    15%   0x0000000a OK
tshell                20  running 0x00003478 0x00014000    16%   0x00000009 OK
thermal               12  suspend 0x00000948 0x00001800    38%   0x0000000a EINTRPT
ts_sample              8  suspend 0x00000608 0x00001000    42%   0x0000000a EINTRPT
usage_thread          30  suspend 0x00000518 0x00002000    16%   0x0000000a EINTRPT
gpio_irq_to_user      16  suspend 0x000004f8 0x00005000    06%   0x0000000a OK
gpio_debounce         15  suspend 0x000004f8 0x00005000    06%   0x0000000a OK
wdt_feed1             25  suspend 0x000004d8 0x00000c00    40%   0x000000c8 EINTRPT
brcmf-init            14  suspend 0x000004f8 0x00003000    32%   0x00000003 OK
wlan                  15  suspend 0x000004f8 0x00004000    07%   0x0000000a OK
sys workq             17  suspend 0x000004f8 0x00005000    06%   0x0000000a OK
mmcsd_detect          22  suspend 0x00000548 0x00008000    08%   0x00000009 EINTRPT
tcpip                 10  suspend 0x00000588 0x00002800    14%   0x00000014 EINTRPT
etx                   12  suspend 0x00000548 0x00002800    13%   0x00000010 EINTRPT
erx                   12  suspend 0x00000558 0x00002800    13%   0x00000010 EINTRPT
tsystem               30  suspend 0x00000508 0x00004000    08%   0x0000001d EINTRPT
tidle0                31  ready   0x00000438 0x00004000    06%   0x00000016 OK
timer                  4  suspend 0x00000488 0x00004000    07%   0x00000009 OK
msh />free
memheap               pool size  max used size available size
-------------------- ---------- ------------- --------------
heap                 33554432   8558144       30385088
msh />hello
Hello RT-Thread!
msh />ls /data
Directory /data:
msh />
```

On the first boot, SDIO Wi-Fi probing failed; the driver initialized successfully after a software reboot.

First-boot `df` output:

```log
msh />df
The function is not implemented.
msh />
```

## Test Criteria

Successful: The system boots and the serial shell accepts commands.

Failed: The system fails to boot or the serial shell is unusable.

## Test Conclusion

Test successful.
