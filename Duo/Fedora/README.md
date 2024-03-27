# Fedora 38 Milk-V Duo 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Fedora 38
- 下载链接：https://github.com/chainsx/fedora-riscv-builder/releases/download/20230719-1650/Fedora-38-Minimal-MilkV-Duo-riscv64.img.xz
- 参考安装文档：https://github.com/chainsx/fedora-riscv-builder
- Issue/CFH: https://github.com/chainsx/fedora-riscv-builder/issues/6
    - （镜像无法启动）

> Note: 此镜像为社区开发者提供，非官方镜像。

### 硬件信息

- Milk-V Duo 64M
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根
- Milk-V Duo 本体上预先焊接好调试所需的排针
- 可选：Milk-V Duo IOB（底板）

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
xzcat Fedora-38-Minimal-MilkV-Duo-riscv64.img.xz | sudo dd of=/dev/sdc bs=4M iflag=fullblock status=progress 
```

### 登录系统

通过串口登录系统。

用户名：`root`
密码：`fedora`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统未能成功启动，上电后 systemd 会 coredump，无法正常登录。

### 启动信息

```log
[  *** ] (2 of 7) Job systemd-update-utmp.se…ice/start running (20s / no limit)                                                     
[  182.618625] (imesyncd)[130]: unhandled signal 11 code 0x1 at 0xffffffffffffffff in libsystemd-shared-253.2-614.7.riscv64.fc38.so]
[  182.632471] CPU: 0 PID: 130 Comm: (imesyncd) Not tainted 5.10.4-tag- #1                                                          
[  182.639349] epc: 0000003fb7b5aece ra : 0000003fb7b5aece sp : 0000003fffe42320                                                    
[  182.646762]  gp : 0000002ac2e73800 tp : 0000003fb71cb260 t0 : 0000003fb7c1d9d8                                                   
[  182.654266]  t1 : 0000003fb7b1dbbc t2 : 0000000000000000 s0 : 0000003fffe423a0                                                   
[  182.661769]  s1 : 0000003fb7ce9c20 a0 : 0000000000000000 a1 : 0000002ac2f6ee80                                                   
[  182.669273]  a2 : 0000002ac2f6ee80 a3 : 0000000000000000 a4 : 0000000000000000                                                   
[  182.676778]  a5 : 0000000000000000 a6 : fefefefefefefeff a7 : 0000000000000024                                                   
[  182.684277]  s2 : 0000002ac2f6ee80 s3 : 0000003fb7ce9c30 s4 : 0000000000000000                                                   
[  182.691781]  s5 : 0000002ac2f6ee80 s6 : 0000003fffe424c8 s7 : ffffffffffffffff                                                   
[  182.699286]  s8 : 000000000000002d s9 : ffffffffffffffff s10: ffffffffffffffff                                                   
[  182.706789]  s11: 0000000000000006 t3 : 0000003fb7bfc72e t4 : 0000000000000000                                                   
[  182.714293]  t5 : 0000000000000000 t6 : 000000000000002f                                                                         
[  182.719818] status: 8000000201804020 badaddr: ffffffffffffffff cause: 000000000000000d
```

启动流程屏幕录像：

[![asciicast](https://asciinema.org/a/MxHNPZZ2MG8vPEBSmMNwTz6DY.svg)](https://asciinema.org/a/MxHNPZZ2MG8vPEBSmMNwTz6DY)

### 缺陷报告

https://github.com/chainsx/fedora-riscv-builder/issues/6

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试失败。
