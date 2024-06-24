## RISC-V Board and OS Support Matrix 

#### [English](./README.md) | [中文](./README_zh.md)

| CPU         | IP Core                                    | Product/Model                           | Arch Linux | Debian/RevyOS | Fedora | FreeBSD | Gentoo | openAnolis | OpenBSD | openCloudOS | openEuler | openKylin | openSUSE | Ubuntu | Tina-Linux | Android 13 | Armbian | BuildRoot | OpenHarmony | FreeRTOS | RT-Thread | Zephyr | OpenWRT | ThreadX | NuttX | Melis | Bianbu |
|-------------|--------------------------------------------|-----------------------------------------|------------|---------------|--------|---------|--------|------------|---------|-------------|-----------|-----------|----------|--------|------------|------------|---------|-----------|-------------|----------|-----------|--------|---------|---------|-------|-------|--------|
| SG2042      | XuanTie C920                               | [Pioneer Box][Pioneer]                  | -          | Good          | Good   | -       | -      | -          | -       | WIP         | Good      | Good      | -        | -      | -          | -          | -       | -         | WIP         | -        | -         | -      | -       | -       | -     | -     | -      |
| CV1800B     | XuanTie C906                               | [Milk-V Duo (64M)][Duo]                 | Basic      | Basic         | -      | -       | -      | -          | -       | -           | Basic     | -         | -        | -      | -          | -          | -       | Basic     | -           | Basic    | Basic     | Basic  | WIP     | Basic   | -     | -     | -      |
| SG2002      | XuanTie C906 + ARM Cortex-A53              | [Milk-V Duo (256M)][Duo256m]            | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | Basic     | -           | Basic    | Basic     | Basic  | -       | -       | -     | -     | -      |
| TH1520      | XuanTie C910 + XuanTie C906 + XuanTie E902 | [LicheePi 4A][LPi4A]                    | Good       | Good          | Good   | -       | -      | -          | -       | -           | Good      | Good      | -        | WIP    | -          | -          | Good    | -         | WIP         | -        | -         | -      | Basic   | -       | -     | -     | -      |
| JH7100      | SiFive U74 + SiFive E24                    | [VisionFive][VF1]                       | -          | -             | Good   | -       | -      | -          | Basic   | -           | Good      | Good      | Basic    | Basic  | -          | -          | Basic   | Basic     | -           | -        | -         | -      | Basic   | -       | -     | -     | -      |
| JH7110      | SiFive U74 + SiFive S7 + SiFive E24        | [VisionFive 2][VF2]                     | Basic      | Good          | -      | WIP     | Basic  | -          | Basic   | -           | Good      | Good      | Basic    | Basic  | -          | WIP        | Good    | Basic     | WIP         | -        | Basic     | CFH    | Basic   | -       | Basic | -     | -      |
| K230        | XuanTie C908                               | [CanMV K230][K230]                      | -          | Basic         | Basic  | -       | -      | -          | -       | -           | -         | -         | -        | Basic  | -          | -          | -       | -         | -           | -        | Basic     | -      | -       | -       | Basic | -     | -      |
| K510        | K510 (?)                                   | [Canaan K510-CRB-V1.2 KIT][K510]        | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | Basic     | -           | -        | -         | -      | -       | -       | -     | -     | -      |
| D1          | XuanTie C906                               | [LicheeRV/AWOL Nezha][C906]             | Basic      | Good          | Good   | WIP     | -      | -          | -       | -           | Good      | -         | Basic    | Basic  | Basic      | -          | -       | -         | -           | -        | -         | -      | Basic   | -       | -     | -     | -      |
| D1h         | XuanTie C906                               | [DongshanPI-Nezha STU][DongshanPI-STU]  | CFT        | CFT           | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | CFT        | -          | -       | CFT       | -           | -        | CFT       | -      | CFT     | -       | -     | -     | -      |
| D1h         | XuanTie C906                               | [MangoPi MQ Pro][mangopi_mq_pro]        | CFT        | CFT           | CFT    | CFT     | -      | -          | -       | -           | -         | -         | CFT      | CFT    | CFT        | -          | CFT     | -         | -           | -        | CFT       | -      | CFT     | -       | -     | -     | -      |
| D1s         | XuanTie C906                               | [DongShanPI D1s][DongShanPI-D1s]        | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | CFT        | -          | -       | -         | -           | -        | -         | -      | CFT     | -       | -     | -     | -      |
| D1s         | XuanTie C906                               | [Mangopi MQ][mangopi_mq]                | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | CFT        | -          | -       | -         | -           | -        | -         | -      | CFT     | -       | -     | -     | -      |
| D1s         | XuanTie C906                               | [D1s NeZha][NeZha-D1s]                  | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | CFT        | -          | -       | -         | -           | -        | -         | -      | CFT     | -       | -     | -     | -      |
| U740        | SiFive U74 + SiFive S7                     | [HiFive Unmatched][Unmatched]           | -          | Basic         | Good   | Basic   | -      | -          | Basic   | -           | Good      | Good      | Basic    | Basic  | -          | -          | CFH     | -         | WIP         | -        | -         | Basic  | Basic   | -       | -     | -     | -      |
| SG2000      | XuanTie C906 + ARM Cortex-A53              | [Milk-V Duo S][DuoS]                    | -          | Basic         | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | Basic     | -           | Basic    | -         | Basic  | -       | -       | Basic | -     | -      |
| JH7110      | SiFive U74 + SiFive S7 + SiFive E24        | [Milk-V Mars][Mars]                     | -          | Good          | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | Basic     | -           | Basic    | -         | -      | -       | -       | -     | -     | -      |
| FSL1030M    | Nuclei UX608                               | [Milk-V Vega][Vega]                     | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | CFH       | -           | -        | -         | -      | -       | -       | -     | -     | -      |
| TH1520      | XuanTie C910 + XuanTie C906 + XuanTie E902 | [Milk-V Meles][Meles]                   | -          | CFT           | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | -        | -         | -      | -       | -       | -     | -     | -      |
| K210        | K210 (?)                                   | [Sipeed Maix-Bit][MaixBit]              | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | Basic    | Basic     | -      | -       | -       | Basic | -     | -      |
| TH1520      | XuanTie C910 + XuanTie C906 + XuanTie E902 | [Lichee Cluster 4A][Cluster4A]          | -          | Good          | Good   | -       | -      | -          | -       | -           | Good      | Good      | -        | -      | -          | -          | Good    | -         | -           | -        | -         | -      | Basic   | -       | -     | -     | -      |
| TH1520      | XuanTie C910 + XuanTie C906 + XuanTie E902 | [Lichee Console 4A][Console4A]          | -          | Good          | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | -        | -         | -      | -       | -       | -     | -     | -      |
| SG2002      | XuanTie C906 + ARM Cortex-A53              | [LicheeRV Nano][LicheeRVNano]           | -          | Basic         | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | Basic     | -           | Basic    | -         | -      | -       | -       | -     | -     | -      |
| AE350       | AndesCore AX45MP                           | [Tang Mega 138K][TangMega138K]          | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | Basic    | Basic     | CFH    | -       | -       | -     | -     | -      |
| BL808       | XuanTie C906 + XuanTie E907 + XuanTie E902 | [Sipeed M1s Dock][SipeedM1s]            | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | Basic     | -           | Basic    | -         | -      | -       | -       | -     | -     | -      |
| BL702       | SiFive E24                                 | [Sipeed M0 sense][M0sense]              | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | Basic    | -         | -      | -       | -       | -     | -     | -      |
| BL618       | XuanTie E907                               | [Sipeed M0P Dock][M0P]                  | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | Basic    | -         | -      | -       | -       | -     | -     | -      |
| BL616       | XuanTie E907                               | [Sipeed M0s Dock][M0s]                  | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | Basic    | -         | -      | -       | -       | -     | -     | -      |
| CH32V103    | QingKe V3A                                 | [CH32V103-EVT][CH32V103]                | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | Basic    | Basic     | -      | -       | -       | -     | -     | -      |
| CH32V203    | QingKe V4B                                 | [CH32V203-EVT][CH32V203]                | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | Basic    | Basic     | -      | -       | -       | -     | -     | -      |
| CH32V208    | QingKe V4C                                 | [CH32V208-EVT][CH32V208]                | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | Basic    | Basic     | -      | -       | -       | -     | -     | -      |
| CH32V303    | QingKe V4F                                 | [CH32V303-EVT][CH32V303]                | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | Basic    | Basic     | -      | -       | -       | -     | -     | -      |
| CH32V305    | QingKe V4F                                 | [CH32V305-EVT][CH32V305]                | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | Basic    | Basic     | -      | -       | -       | -     | -     | -      |
| CH32V307    | QingKe V4F                                 | [CH32V307-EVT][CH32V307]                | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | Basic    | Basic     | -      | -       | -       | -     | -     | -      |
| CH573F      | QingKe V3A                                 | [CH573F-EVT][CH573F]                    | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | Basic    | Basic     | -      | -       | -       | -     | -     | -      |
| CH582F      | QingKe V4A                                 | [CH582F-EVT][CH582F]                    | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | Basic    | Basic     | -      | -       | -       | -     | -     | -      |
| CH592X      | QingKe V4C                                 | [CH592X-EVT][CH592X]                    | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | Basic    | Basic     | -      | -       | -       | -     | -     | -      |
| GD32VF103   | Nuclei Bumblebee                           | [Longan Nano][Longan_Nano]              | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | CFT      | CFT       | Basic  | -       | -       | -     | -     | -      |
| GD32VF103   | Nuclei Bumblebee                           | [RV-STAR][RV_STAR]                      | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | CFT      | CFT       | -      | -       | -       | -     | -     | -      |
| GD32VF103   | Nuclei Bumblebee                           | [Nuclei DDR200T][DDR200T]               | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | CFT      | CFT       | -      | -       | -       | -     | -     | -      |
| V853        | XuanTie E907 + ARM Cortex-A7               | [AllWinner V853][V853]                  | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | -        | -         | -      | -       | -       | -     | CFT   | -      |
| V853        | XuanTie E907 + ARM Cortex-A7               | [100ASK-V853-PRO][V853]                 | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | -        | -         | -      | -       | -       | -     | CFT   | -      |
| V851s       | XuanTie E907 + ARM Cortex-A7               | [YuzukiHD-Lizard][YouMuPI]              | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | -        | -         | -      | -       | -       | -     | CFT   | -      |
| V851se      | XuanTie E907 + ARM Cortex-A7               | [TinyVision][TinyVision]                | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | -       | -         | -           | -        | -         | -      | -       | -       | -     | CFT   | -      |
| Keystone K1 | SpacemiT X60                               | [BananaPi BPI-F3][BPI-F3]               | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | Good    | -         | -           | -        | -         | -      | -       | -       | -     | -     | Good   |
| TH1520      | XuanTie C910 + XuanTie C906 + XuanTie E902 | [BeagleV-Ahead][BeagleV-Ahead]          | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | CFT    | -          | -          | -       | -         | -           | -        | -         | -      | -       | -       | -     | -     | -      |
| MPFS025T    | SiFive U54 + SiFive E51                    | [BeagleV-Fire][BeagleV-Fire]            | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | CFT    | -          | -          | -       | -         | -           | -        | -         | -      | -       | -       | -     | -     | -      |
| JH7110      | SiFive U74 + SiFive S7 + SiFive E24        | [Star64][STAR64]                        | -          | -             | -      | -       | -      | -          | -       | -           | -         | -         | -        | -      | -          | -          | CFT     | -         | -           | -        | -         | -      | -       | -       | CFT   | -     | -      |
| MPFS250T    | SiFive U54 + SiFive E51                    | [PolarFire FPGA SoC Icicle Kit][Icicle] | CFT        | -             | -      | -       | -      | -          | CFT     | -           | -         | -         | -        | Basic  | -          | -          | -       | Basic     | -           | CFT      | -         | CFT    | -       | -       | CFT   | -     | -      |

#### Notes

* Good: Supports GUI
* Basic: Can boot up and run
* CFH (Call for help): Official documentations/community forums show this OS is supported on this board, but failed to boot up
* CFT (Call for testing): An OS image is avaliable, need further verification on real hardware
* CFI (Call for more information):  Official documentations claims there is support for this OS, but no OS image avaliable yet
* WIP: Official announcements say there will be/is support for this OS/board, but no image or other resources (e.g. source code) avaliable yet
* -: No support for this OS/board combo, either from official or other sources

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

