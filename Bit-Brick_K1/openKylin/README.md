---
sys: openkylin
sys_ver: 2.0 SP2
sys_var: null
status: basic
last_update: 2025-09-18
---

# openKylin v2.0 SP2 Bit-Brick K1 Test Report

## Test Environment

### System Information

- System Version: openKylin v2.0-SP2
- Download Link: [https://www.openkylin.top/downloads/index.html](https://www.openkylin.top/downloads/index.html) **Choose k1 version**

### Hardware Information

- Bit-Brick K1
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing the Image (SD Card)

After downloading and extracting the image, use `dd` to flash the image to the microSD card.

```bash
xz -d openKylin-Embedded-V2.0-SP2-Release-spacemit-k1-riscv64.img.xz
sudo dd if=openKylin-Embedded-V2.0-SP2-Release-spacemit-k1-riscv64.img of=/dev/your-device bs=4M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default Username: `openkylin`
Default Password: `openkylin`


## Actual Results

### Boot Log

```log

openKylin 2.0 SP2 openkylin ttyS0

openkylin login: openkylin
密码：
Welcome to openKylin 2.0 SP2 (GNU/Linux 6.6.63 riscv64)

 * Support:        https://openkylin.top

The programs included with the openKylin system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

openKylin comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

You do not have any new mail.
openkylin@openkylin:~$ uname -a
Linux openkylin 6.6.63 #2.2~rc3.2 SMP PREEMPT Thu Apr  3 06:53:27 UTC 2025 riscv64 riscv64 riscv64 GNU/Linux
openkylin@openkylin:~$ cat /etc/os-release
NAME="openKylin"
FULL_NAME="openKylin"
VERSION="2.0 SP2 (nile)"
VERSION_US="2.0 SP2 (nile)"
ID=openkylin
PRETTY_NAME="openKylin 2.0 SP2"
VERSION_ID="2.0"
HOME_URL="https://www.openkylin.top/"
VERSION_CODENAME=nile
PRODUCT_FEATURES=3
openkylin@openkylin:~$ cat /proc/cpuinfo
processor       : 0
hart            : 0
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 1
hart            : 1
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 2
hart            : 2
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 3
hart            : 3
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 4
hart            : 4
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 5
hart            : 5
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 6
hart            : 6
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 7
hart            : 7
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

openkylin@openkylin:~$
```

### Desktop Environment

HDMI output is black, Kernel floods `[drm:dpu_isr] ERROR Under Run! DPU_Mclk = 0, DPU BW = 0`, spacemit_rproc/rpmsg blocks for tens of minutes during boot and only comes up very late, Likely a kernel/BSP defect.

``` log
dmesg -k | grep -iE "drm|dpu|hdmi|fbcon" | tail -n 200 | grep -iE 
[ 7840.724174] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0l -n 200
[ 7840.724236] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 7840.724251] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 7840.724264] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 7840.724277] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 7840.724289] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 7840.724300] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 7840.724312] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 7840.724324] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 7840.724336] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8689.571918] [drm] spacemit_hdmi_connector_detect() hdmi status disconnected
[ 8689.584568] [drm] spacemit_hdmi_connector_detect() hdmi status disconnected
[ 8689.590428] [drm] spacemit_hdmi_encoder_disable()
[ 8689.598915] [drm] spacemit_crtc_atomic_disable(power off)
[ 8711.613843] [drm] spacemit_hdmi_connector_detect() hdmi status connected
[ 8711.628849] [drm] spacemit_hdmi_connector_detect() hdmi status connected
[ 8711.628883] [drm] spacemit_hdmi_get_edid_block() len 128
[ 8711.651802] [drm] spacemit_hdmi_get_edid_block() len 128
[ 8711.663237] [drm] spacemit_crtc_atomic_enable(power on)
[ 8711.663327] [drm] dpu_init
[ 8711.663363] [drm] spacemit_hdmi_encoder_enable()
[ 8711.663380] [drm] spacemit_hdmi_setup() id 0xa28501, hdmi 8bpc
[ 8711.663627] [drm] DPU type 0 id 2 Start!
[ 8711.664317] dpu_isr: 9170 callbacks suppressed
[ 8711.664329] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8711.664373] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8711.664388] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8711.664401] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8711.664411] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8711.664422] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8711.664432] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8711.664442] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8711.664452] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8711.664462] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8742.235926] [drm] spacemit_hdmi_connector_detect() hdmi status disconnected
[ 8742.248828] [drm] spacemit_hdmi_connector_detect() hdmi status disconnected
[ 8742.257920] [drm] spacemit_hdmi_encoder_disable()
[ 8742.263749] [drm] spacemit_crtc_atomic_disable(power off)
[ 8757.256799] [drm] spacemit_hdmi_connector_detect() hdmi status connected
[ 8757.272020] [drm] spacemit_hdmi_connector_detect() hdmi status connected
[ 8757.272055] [drm] spacemit_hdmi_get_edid_block() len 128
[ 8757.299784] [drm] spacemit_hdmi_get_edid_block() len 128
[ 8757.310589] [drm] spacemit_crtc_atomic_enable(power on)
[ 8757.310692] [drm] dpu_init
[ 8757.310729] [drm] spacemit_hdmi_encoder_enable()
[ 8757.310750] [drm] spacemit_hdmi_setup() id 0xa28501, hdmi 8bpc
[ 8757.310997] [drm] DPU type 0 id 2 Start!
[ 8757.311878] dpu_isr: 23968 callbacks suppressed
[ 8757.311884] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8757.311934] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8757.311952] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8757.311965] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8757.311978] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8757.311990] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8757.312004] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8757.312017] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8757.312029] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8757.312041] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8762.843624] [drm] spacemit_hdmi_connector_detect() hdmi status disconnected
[ 8762.856716] [drm] spacemit_hdmi_connector_detect() hdmi status disconnected
[ 8762.864619] [drm] spacemit_hdmi_encoder_disable()
[ 8762.877784] [drm] spacemit_crtc_atomic_disable(power off)
[ 8763.098508] [drm] spacemit_hdmi_connector_detect() hdmi status connected
[ 8763.106127] [drm] spacemit_hdmi_connector_detect() hdmi status connected
[ 8763.106167] [drm] spacemit_hdmi_get_edid_block() len 128
[ 8763.127845] [drm] spacemit_hdmi_get_edid_block() len 128
[ 8763.139954] [drm] spacemit_crtc_atomic_enable(power on)
[ 8763.140073] [drm] dpu_init
[ 8763.140110] [drm] spacemit_hdmi_encoder_enable()
[ 8763.140129] [drm] spacemit_hdmi_setup() id 0xa28501, hdmi 8bpc
[ 8763.140382] [drm] DPU type 0 id 2 Start!
[ 8763.141114] dpu_isr: 160227 callbacks suppressed
[ 8763.141126] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8763.141170] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8763.141179] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8763.141187] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8763.141193] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8763.141200] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8763.141206] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8763.141213] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8763.141219] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8763.141225] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8787.726947] [drm] spacemit_hdmi_connector_detect() hdmi status disconnected
[ 8787.739897] [drm] spacemit_hdmi_connector_detect() hdmi status disconnected
[ 8787.748405] [drm] spacemit_hdmi_encoder_disable()
[ 8787.757159] [drm] spacemit_crtc_atomic_disable(power off)
[ 8787.964782] [drm] spacemit_hdmi_connector_detect() hdmi status connected
[ 8787.973212] [drm] spacemit_hdmi_connector_detect() hdmi status connected
[ 8787.973246] [drm] spacemit_hdmi_get_edid_block() len 128
[ 8787.995837] [drm] spacemit_hdmi_get_edid_block() len 128
[ 8788.007894] [drm] spacemit_crtc_atomic_enable(power on)
[ 8788.008000] [drm] dpu_init
[ 8788.008036] [drm] spacemit_hdmi_encoder_enable()
[ 8788.008053] [drm] spacemit_hdmi_setup() id 0xa28501, hdmi 8bpc
[ 8788.008306] [drm] DPU type 0 id 2 Start!
[ 8788.009616] dpu_isr: 42061 callbacks suppressed
[ 8788.009625] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8788.009672] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8788.009686] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8788.009697] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8788.009708] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8788.009718] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8788.009728] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8788.009739] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8788.009749] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8788.009760] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8819.336733] [drm] spacemit_hdmi_connector_detect() hdmi status disconnected
[ 8819.349221] [drm] spacemit_hdmi_connector_detect() hdmi status disconnected
[ 8819.358292] [drm] spacemit_hdmi_encoder_disable()
[ 8819.375097] [drm] spacemit_crtc_atomic_disable(power off)
[ 8819.569211] [drm] spacemit_hdmi_connector_detect() hdmi status connected
[ 8819.576788] [drm] spacemit_hdmi_connector_detect() hdmi status connected
[ 8819.576826] [drm] spacemit_hdmi_get_edid_block() len 128
[ 8819.599838] [drm] spacemit_hdmi_get_edid_block() len 128
[ 8819.611983] [drm] spacemit_crtc_atomic_enable(power on)
[ 8819.612098] [drm] dpu_init
[ 8819.612134] [drm] spacemit_hdmi_encoder_enable()
[ 8819.612152] [drm] spacemit_hdmi_setup() id 0xa28501, hdmi 8bpc
[ 8819.612404] [drm] DPU type 0 id 2 Start!
[ 8819.614365] dpu_isr: 111681 callbacks suppressed
[ 8819.614379] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8819.614443] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8819.614460] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8819.614473] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8819.614486] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8819.614498] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8819.614510] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8819.614521] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8819.614533] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8819.614544] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8820.625841] [drm] spacemit_hdmi_connector_detect() hdmi status disconnected
[ 8820.631309] [drm] spacemit_hdmi_connector_detect() hdmi status disconnected
[ 8820.642353] [drm] spacemit_hdmi_encoder_disable()
[ 8820.645870] [drm] spacemit_crtc_atomic_disable(power off)
[ 8835.583523] [drm] spacemit_hdmi_connector_detect() hdmi status disconnected
[ 8835.583550] [drm] spacemit_hdmi_connector_detect() hdmi status disconnected
[ 8846.975385] [drm] spacemit_hdmi_connector_detect() hdmi status connected
[ 8846.991412] [drm] spacemit_hdmi_connector_detect() hdmi status connected
[ 8846.991447] [drm] spacemit_hdmi_get_edid_block() len 128
[ 8847.011710] [drm] spacemit_hdmi_get_edid_block() len 128
[ 8847.020593] [drm] spacemit_crtc_atomic_enable(power on)
[ 8847.020697] [drm] dpu_init
[ 8847.020733] [drm] spacemit_hdmi_encoder_enable()
[ 8847.020751] [drm] spacemit_hdmi_setup() id 0xa28501, hdmi 8bpc
[ 8847.020966] [drm] DPU type 0 id 2 Start!
[ 8847.033689] dpu_isr: 85855 callbacks suppressed
[ 8847.033707] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8847.033759] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8847.033773] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8847.033787] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8847.033794] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8847.033806] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8847.033818] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8847.033830] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8847.033837] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8847.033849] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8875.633885] [drm] spacemit_hdmi_connector_detect() hdmi status disconnected
[ 8875.646475] [drm] spacemit_hdmi_connector_detect() hdmi status disconnected
[ 8875.652366] [drm] spacemit_hdmi_encoder_disable()
[ 8875.654411] [drm] spacemit_crtc_atomic_disable(power off)
[ 8904.033397] [drm] spacemit_hdmi_connector_detect() hdmi status connected
[ 8904.035525] [drm] spacemit_hdmi_connector_detect() hdmi status connected
[ 8904.040614] [drm] spacemit_hdmi_connector_detect() hdmi status connected
[ 8904.040645] [drm] spacemit_hdmi_get_edid_block() len 128
[ 8904.157212] [drm] hdmi_i2c_write wait hdmi ddc command done timeout
[ 8904.157229] [drm] spacemit_hdmi_get_edid_block() failed to read edid
[ 8904.157237] [drm] spacemit_hdmi_connector_get_modes() get edid failed
[ 8904.169514] [drm] spacemit_crtc_atomic_enable(power on)
[ 8904.169619] [drm] dpu_init
[ 8904.169654] [drm] spacemit_hdmi_encoder_enable()
[ 8904.169673] [drm] spacemit_hdmi_setup() id 0xa28501, hdmi 8bpc
[ 8904.169942] [drm] DPU type 0 id 2 Start!
[ 8904.175978] dpu_isr: 4517 callbacks suppressed
[ 8904.176003] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8904.176060] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8904.176075] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8904.176087] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8904.176098] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8904.176110] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8904.176122] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8904.176133] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8904.176144] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8904.176156] [drm:dpu_isr] *ERROR* Under Run! DPU_Mclk = 0, DPU BW = 0
[ 8905.624340] [drm] spacemit_hdmi_connector_detect() hdmi status disconnected
[ 8905.629765] [drm] spacemit_hdmi_connector_detect() hdmi status disconnected
[ 8905.638896] [drm] spacemit_hdmi_encoder_disable()
[ 8905.653401] [drm] spacemit_crtc_atomic_disable(power off)
[ 8908.684713] [drm] spacemit_hdmi_connector_detect() hdmi status disconnected
[ 8908.684744] [drm] spacemit_hdmi_connector_detect() hdmi status disconnected
[ 8908.686782] [drm] spacemit_hdmi_connector_detect() hdmi status connected
[ 8908.701615] [drm] spacemit_hdmi_connector_detect() hdmi status connected
[ 8908.701649] [drm] spacemit_hdmi_get_edid_block() len 128
[ 8908.823191] [drm] hdmi_i2c_write wait hdmi ddc command done timeout
[ 8908.823207] [drm] spacemit_hdmi_get_edid_block() failed to read edid
[ 8908.823216] [drm] spacemit_hdmi_connector_get_modes() get edid failed
[ 8908.833808] [drm] spacemit_crtc_atomic_enable(power on)
[ 8908.833909] [drm] dpu_init
[ 8908.833946] [drm] spacemit_hdmi_encoder_enable()
[ 8908.833965] [drm] spacemit_hdmi_setup() id 0xa28501, hdmi 8bpc
[ 8908.834232] [drm] DPU type 0 id 2 Start!
```

## Test Conclusion

The system boots up with long time, DRM has broken, only can login through the serial port.
