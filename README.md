## RISCV Board and OS Supported Matrix

## 主流操作系统 for RISC-V 硬件适配情况（主流 RISC-V 开发板）

| CPU         | 产品型号                                | Arch Linux | Debian/RevyOS | Fedora | FreeBSD | Gentoo | openAnolis | OpenBSD | openCloudOS | openEuler | openKylin | openSUSE | Ubuntu | Tina-Linux | Android 13 | Armbian | BuildRoot | OpenHarmony | FreeRTOS | RT-Thread | Zephyr | OpenWRT | ThreadX | NuttX | Melis | Bianbu |
|-------------|-----------------------------------------|------------|---------------|--------|---------|--------|------------|---------|-------------|-----------|-----------|----------|--------|------------|------------|---------|-----------|-------------|----------|-----------|--------|---------|---------|-------|-------|--------|
| SG2042      | [Pioneer Box][Pioneer]                  | N/A        | Good          | Good   | N/A     | N/A    | N/A        | N/A     | WIP         | Good      | Good      | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | WIP         | N/A      | N/A       | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| CV1800B     | [Milk-V Duo (64M)][Duo]                 | Basic      | Basic         | CFH    | N/A     | N/A    | N/A        | N/A     | N/A         | Basic     | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | Basic     | N/A         | Basic    | Basic     | N/A    | WIP     | Basic   | N/A   | N/A   | N/A    |
| SG2002      | [Milk-V Duo (256M)][Duo256m]            | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | Basic     | N/A         | Basic    | Basic     | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| TH1520      | [LicheePi 4A][LPi4A]                    | Good       | Good          | Good   | N/A     | N/A    | N/A        | N/A     | N/A         | Good      | Good      | N/A      | WIP    | N/A        | N/A        | Good    | N/A       | WIP         | N/A      | N/A       | N/A    | Basic   | N/A     | N/A   | N/A   | N/A    |
| JH7100      | [VisionFive][VF1]                       | N/A        | N/A           | Good   | N/A     | N/A    | N/A        | Basic   | N/A         | Good      | Good      | Basic    | Basic  | N/A        | N/A        | Basic   | Basic     | N/A         | N/A      | N/A       | N/A    | Basic   | N/A     | N/A   | N/A   | N/A    |
| JH7110      | [VisionFive 2][VF2]                     | Basic      | Good          | N/A    | WIP     | Basic  | N/A        | Basic   | N/A         | Good      | Good      | Basic    | Basic  | N/A        | WIP        | Good    | Basic     | WIP         | N/A      | Basic     | CFH    | Basic   | N/A     | Basic | N/A   | N/A    |
| K230        | [CanMV K230][K230]                      | N/A        | Basic         | Basic  | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | Basic  | N/A        | N/A        | N/A     | N/A       | N/A         | N/A      | Basic     | N/A    | N/A     | N/A     | Basic | N/A   | N/A    |
| K510        | [Canaan K510-CRB-V1.2 KIT][K510]        | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | Basic     | N/A         | N/A      | N/A       | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| C906        | [LicheeRV/AWOL Nezha][C906]             | N/A        | Good          | Good   | WIP     | N/A    | N/A        | N/A     | N/A         | Good      | N/A       | Basic    | Basic  | Basic      | N/A        | N/A     | N/A       | N/A         | N/A      | N/A       | N/A    | Basic   | N/A     | N/A   | N/A   | N/A    |
| D1h         | [DongshanPI-哪吒 STU][DongshanPI-STU]    | N/A        | CFT           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | CFT        | N/A        | N/A     | CFT       | N/A         | N/A      | CFT       | N/A    | CFT     | N/A     | N/A   | N/A   | N/A    |
| D1h         | [MangoPi MQ Pro][mangopi_mq_pro]        | CFT        | CFT           | CFT    | CFT     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | CFT      | CFT    | CFT        | N/A        | CFT     | N/A       | N/A         | N/A      | CFT       | N/A    | CFT     | N/A     | N/A   | N/A   | N/A    |
| D1s         | [DongShanPI D1s][DongShanPI-D1s]        | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | CFT        | N/A        | N/A     | N/A       | N/A         | N/A      | N/A       | N/A    | CFT     | N/A     | N/A   | N/A   | N/A    |
| D1s         | [Mangopi MQ][mangopi_mq]                | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | CFT        | N/A        | N/A     | N/A       | N/A         | N/A      | N/A       | N/A    | CFT     | N/A     | N/A   | N/A   | N/A    |
| D1s         | [D1s NeZha][NeZha-D1s]                  | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | CFT        | N/A        | N/A     | N/A       | N/A         | N/A      | N/A       | N/A    | CFT     | N/A     | N/A   | N/A   | N/A    |
| U740        | [HiFive Unmatched][Unmatched]           | N/A        | Basic         | Good   | Basic   | N/A    | N/A        | Basic   | N/A         | Good      | Good      | Basic    | Basic  | N/A        | N/A        | CFH     | N/A       | WIP         | N/A      | N/A       | Basic  | Basic   | N/A     | N/A   | N/A   | N/A    |
| SG2000      | [Milk-V Duo S][DuoS]                    | N/A        | Basic         | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | Basic     | N/A         | Basic    | N/A       | N/A    | N/A     | N/A     | Basic | N/A   | N/A    |
| JH7110      | [Milk-V Mars][Mars]                     | N/A        | Good          | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | CFT       | N/A         | Basic    | N/A       | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| FSL1030M    | [Milk-V Vega][Vega]                     | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | CFH       | N/A         | N/A      | N/A       | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| TH1520      | [Milk-V Meles][Meles]                   | N/A        | CFT           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | N/A      | N/A       | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| K210        | [Sipeed Maix-Bit][MaixBit]              | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | Basic    | Basic     | N/A    | N/A     | N/A     | Basic | N/A   | N/A    |
| TH1520      | [Lichee Cluster 4A][Cluster4A]          | N/A        | Good          | Good   | N/A     | N/A    | N/A        | N/A     | N/A         | Good      | Good      | N/A      | N/A    | N/A        | N/A        | Good    | N/A       | N/A         | N/A      | N/A       | N/A    | Basic   | N/A     | N/A   | N/A   | N/A    |
| TH1520      | [Lichee Console 4A][Console4A]          | N/A        | Good          | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | N/A      | N/A       | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| SG2002      | [LicheeRV Nano][LicheeRVNano]           | N/A        | Basic         | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | Basic     | N/A         | Basic    | N/A       | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| AE350       | [Tang Mega 138K][TangMega138K]          | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | Basic    | Basic     | CFH    | N/A     | N/A     | N/A   | N/A   | N/A    |
| BL808       | [Sipeed M1s Dock][SipeedM1s]            | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | Basic     | N/A         | Basic    | N/A       | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| BL702       | [Sipeed M0 sense][M0sense]              | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | Basic    | N/A       | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| BL618       | [Sipeed M0P Dock][M0P]                  | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | Basic    | N/A       | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| BL616       | [Sipeed M0s Dock][M0s]                  | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | Basic    | N/A       | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| CH32V103    | [CH32V103-EVT][CH32V103]                | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | Basic    | Basic     | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| CH32V203    | [CH32V203-EVT][CH32V203]                | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | Basic    | Basic     | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| CH32V208    | [CH32V208-EVT][CH32V208]                | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | Basic    | Basic     | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| CH32V303    | [CH32V303-EVT][CH32V303]                | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | Basic    | Basic     | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| CH32V305    | [CH32V305-EVT][CH32V305]                | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | Basic    | Basic     | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| CH32V307    | [CH32V307-EVT][CH32V307]                | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | Basic    | Basic     | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| CH573F      | [CH573F-EVT][CH573F]                    | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | Basic    | Basic     | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| CH582F      | [CH582F-EVT][CH582F]                    | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | Basic    | Basic     | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| CH592X      | [CH592X-EVT][CH592X]                    | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | Basic    | Basic     | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| GD32VF103   | [Longan Nano][Longan_Nano]              | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | CFT      | CFT       | Basic  | N/A     | N/A     | N/A   | N/A   | N/A    |
| GD32VF103   | [RV-STAR][RV_STAR]                      | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | CFT      | CFT       | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| GD32VF103   | [Nuclei DDR200T][DDR200T]               | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | CFT      | CFT       | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| V853        | [全志 V853 开发板][V853]                  | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | N/A      | N/A       | N/A    | N/A     | N/A     | N/A   | CFT   | N/A    |
| V853        | [100ASK-V853-PRO][V853]                 | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | N/A      | N/A       | N/A    | N/A     | N/A     | N/A   | CFT   | N/A    |
| V851s       | [柚木 PI-蜥蜴][YouMuPI]                  | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | N/A      | N/A       | N/A    | N/A     | N/A     | N/A   | CFT   | N/A    |
| V851se      | [TinyVision][TinyVision]                | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | N/A         | N/A      | N/A       | N/A    | N/A     | N/A     | N/A   | CFT   | N/A    |
| Keystone K1 | [香蕉派 BPI-F3][BPI-F3]                  | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | Good    | N/A       | N/A         | N/A      | N/A       | N/A    | N/A     | N/A     | N/A   | N/A   | Good   |
| TH1520      | [BeagleV-Ahead][BeagleV-Ahead]          | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | CFT    | N/A        | N/A        | N/A     | N/A       | N/A         | N/A      | N/A       | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| MPFS025T    | [BeagleV-Fire][BeagleV-Fire]            | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | CFT    | N/A        | N/A        | N/A     | N/A       | N/A         | N/A      | N/A       | N/A    | N/A     | N/A     | N/A   | N/A   | N/A    |
| JH7110      | [Star64][STAR64]                        | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | CFT     | N/A       | N/A         | N/A      | N/A       | N/A    | N/A     | N/A     | CFT   | N/A   | N/A    |
| MPFS250T    | [PolarFire FPGA SoC Icicle Kit][Icicle] | CFT        | N/A           | N/A    | N/A     | N/A    | N/A        | CFT     | N/A         | N/A       | N/A       | N/A      | Basic  | N/A        | N/A        | N/A     | Basic     | N/A         | CFT      | N/A       | CFT    | N/A     | N/A     | CFT   | N/A   | N/A    |

#### 说明

* Good：支持图形界面
* Basic：能启动运行
* CFH (Call for help)：官方/论坛资料表示支持，但是未跑通
* CFT (Call for testing)：镜像链接有，但是缺乏硬件设备验证
* CFI (Call for more information)：官方资料宣称有，但是找不到镜像文件等实际可用的资料
* WIP：官方宣发操作系统即将/正在对开发板进行支持，但暂未获取到可用的镜像
* N/A：暂未从官方或者其它渠道获取到开发板的支持信息

[Pioneer]: ./Pioneer/README.md
[Duo]: ./Duo/README.md
[Duo256m]: ./Duo256m/README.md
[LPi4A]: ./LicheePi4A/README.md
[VF1]: ./VisionFive/README.md
[VF2]: ./VisionFive2/README.md
[K230]: ./K230/README.md
[C906]: ./D1_LicheeRV/README.md
[Unmatched]: ./Unmatched/README.md
[DuoS]: ./Duo_S/README.md
[Mars]: ./Mars/README.md
[Vega]: ./Vega/README.md
[Meles]: ./Meles/README.md
[MaixBit]: ./Maix-I_K210/README.md
[Cluster4A]: ./LicheeCluster4A/README.md
[Console4A]: ./LicheeConsole4A/README.md
[LicheeRVNano]: ./LicheeRV_Nano/README.md
[TangMega138K]: ./Tang_Mega_138K/README.md
[K510]: ./K510/README.md
[SipeedM1s]: ./M1s/README.md
[M0sense]: ./M0sense/README.md
[M0P]: ./M0P_Dock/README.md
[M0s]: ./M0s/README.md
[CH32V103]: ./CH32V103/README.md
[CH32V203]: ./CH32V203/README.md
[CH32V208]: ./CH32V208/README.md
[CH32V303]: ./CH32V303/README.md
[CH32V305]: ./CH32V305/README.md
[CH32V307]: ./CH32V307/README.md
[CH582F]: ./CH582F/README.md
[CH592X]: ./CH592X/README.md
[Longan_Nano]: ./Longan_Nano/README.md
[RV_STAR]: ./RV_STAR/README.md
[DDR200T]: ./DDR200T/README.md
[V853]: ./V853/README.md
[100ASK]: ./100ASK/README.md
[YouMuPI]: ./YouMuPI/README.md
[TinyVision]: ./TinyVision/README.md
[CH573F]: ./CH573F/README.md
[DongshanPI-STU]: ./DongshanPI-STU/README.md
[mangopi_mq_pro]: ./mangopi_mq_pro/README.md
[DongShanPI-D1s]: ./DongShanPI-D1s/README.md
[mangopi_mq]: ./mangopi_mq/README.md
[NeZha-D1s]: ./NeZha-D1s/README.md
[BPI-F3]: ./BPI-F3/README.md
[BeagleV-Ahead]: ./BeagleV-Ahead/README.md
[BeagleV-Fire]: ./BeagleV-Fire/README.md
[STAR64]: ./STAR64/README.md
[Icicle]: ./Icicle/README.md
