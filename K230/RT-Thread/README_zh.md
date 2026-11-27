# RT-Smart CanMV K230 测试报告（Linux + RT-Smart SDK）

## 测试环境

### 操作系统信息

官方预编译 SDK 已经含有了 RT-Smart。

- 下载链接：https://github.com/kendryte/k230_sdk/releases/tag/v2.0
- 镜像文件：`CanMV-K230_sdcard_v2.0_nncase_v2.10.0.img.gz`
- 参考安装文档：https://www.kendryte.com/k230/zh/v2.0/01_software/board/K230_SDK_%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E.html

### 硬件信息

- 开发板：Canaan Kendryte K230
- 本次实测硬件版本：v1.1
- 32 GB microSD 卡
- USB A to C / USB C to C 线缆

## 安装步骤

### 刷写镜像

使用 `gzip` 解压镜像。
清空你的 sd 卡。
使用 `dd` 将镜像写入 microSD 卡。

```bash
gzip -d /path/to/k230.img.gz
sudo wipefs -a /dev/your_device
sudo dd if=/path/to/k230.img of=/dev/your_device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户： `root`
无默认密码。

其中小核 tty 为 Linux，大核 tty 为 RT-Smart。

## 实际结果

启动录像：

[![asciicast](https://asciinema.org/a/K0izhLQRGIjz9IWC.svg)](https://asciinema.org/a/K0izhLQRGIjz9IWC)

```log
OpenSBI v0.9
mpp built Sep 12 2025 16:51:17
vicap_mcm_initRT-SMART Hello RISC-V.
msh />press 'q' to exit application!!
mirror mirror is 0 , sensor tpye is 24
first mode is 0
ov5647_power_rest OV5647_CAM_PIN is 0
set output err, set default format ISP_PIX_FMT_YUV420SP
[tuning] dev: 0
acq_win.width: 1920
acq_win.height: 1080
pipe_ctrl: 4261412857
sensor_fd: 11
sensor_type: 24
sensor_name: ov5647
database_name: ov5647-1920x1080
buffer_num: 0
buffer_size: 0
[tuning] chn: 0
out_win.width: 1920
out_win.height: 1080
bit_width: 0
pix_format: 5
buffer_num: 10
buffer_size: 3110912
yraw_size: 0
uv_size: 0
v_size: 0
block_type: 1
wait_time: 500
chn_enable: 1
isp_3dnr_en is 1 g_isp_dev_ctx[dev_num].dev_attr.pipe_ctrl.bits.dnr3_enable is 0
VsiCamDeviceCreate[D/lt9611] vtotal 1125 v hw:0-vt:0 active 1080 htotal_sys 400

created!
ov5647_power_rest OV5647_CAM_PIN is 0
kd_mpi_isp_set_output_chn_format, width(1920), height(1080), pix_format(5)
kd_mpi_isp_set_output_chn_format, width(1280), height(720), pix_format(16)
[dw] init, version Sep 12 2025 10:08:29
q
kd_mpi_isp_stop_stream chn enable is 1
kd_mpi_isp_stop_stream chn enable is 1
kd_mpi_isp_stop_stream chn enable is 0
release reserved vb 278734848
release reserved vb 0
ov5647_power_rest OV5647_CAM_PIN is 0
<ipcm> phys 0x180000, size 0x79000
ps
thread               pri  status      sp     stack size max used left tick  error
-------------------- ---  ------- ---------- ----------  ------  ---------- ---
tshell                20  running 0x00003428 0x00014000    16%   0x00000002 OK
sharefs_client         5  suspend 0x00000508 0x00006000    05%   0x00000005 EINTRPT
thermal_detect_threa  16  suspend 0x000004d8 0x00002800    12%   0x0000000a EINTRPT
auto_load_thread      16  suspend 0x000004c8 0x00002800    12%   0x0000000a EINTRPT
mcm_task               0  suspend 0x00000528 0x00002000    16%   0x00000005 EINTRPT
ipcm-discovery         5  suspend 0x000004f8 0x00001000    32%   0x00000002 EINTRPT
ipcm-recv              5  suspend 0x00000518 0x00001000    33%   0x00000005 EINTRPT
sys_work              23  suspend 0x00000488 0x00005000    05%   0x0000000a OK
tsystem               30  suspend 0x000004f8 0x00004000    09%   0x0000001d EINTRPT
tidle0                31  ready   0x00000448 0x00004000    06%   0x00000020 OK
timer                  4  suspend 0x00000488 0x00004000    07%   0x00000009 OK
msh />free
memheap               pool size  max used size available size
-------------------- ---------- ------------- --------------
heap                 33554432   1197184       32865152
msh />
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
