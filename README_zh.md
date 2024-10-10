# RISC-V 开发板与操作系统支持矩阵

[English](./README_zh.md) | [中文](./README_zh.md)

## Linux 发行版


| CPU               | IP Core                                    | Product/Model                           | Arch Linux | Debian/RevyOS | Fedora | Gentoo | openAnolis | openCloudOS | openEuler | openKylin | openSUSE | Ubuntu | Tina-Linux | Armbian | BuildRoot | OpenWRT | Bianbu | Deepin | Yocto | Alpine |
| ----------------- | ------------------------------------------ | --------------------------------------- | ---------- | :------------ | ------ | ------ | ---------- | ----------- | --------- | --------- | -------- | ------ | ---------- | ------- | --------- | ------- | ------ | ------ | ----- | ------ |
| SG2042            | XuanTie C920                               | [Pioneer Box][Pioneer]                  | -          | Good          | Good   | -      | -          | WIP         | Good      | Good      | -        | -      | -          | -       | -         | -       | -      | Basic  | -     | -      |
| CV1800B           | XuanTie C906                               | [Milk-V Duo (64M)][Duo]                 | Basic      | Basic         | -      | -      | -          | -           | Basic     | -         | -        | -      | -          | -       | Basic     | WIP     | -      | -      | -     | -      |
| SG2002            | XuanTie C906 + ARM Cortex-A53              | [Milk-V Duo (256M)][Duo256m]            | -          | Basic         | -      | -      | -          | -           | -         | -         | -        | -      | -          | -       | Basic     | -       | -      | -      | -     | WIP    |
| TH1520            | XuanTie C910 + XuanTie C906 + XuanTie E902 | [LicheePi 4A][LPi4A]                    | Good       | Good          | Good   | -      | -          | -           | Good      | Good      | -        | Basic  | -          | Basic   | -         | Basic   | -      | Good   | -     | -      |
| JH7100            | SiFive U74 + SiFive E24                    | [VisionFive][VF1]                       | -          | -             | Good   | -      | -          | -           | Good      | Good      | Basic    | Basic  | -          | Basic   | Basic     | Basic   | -      | Basic  | -     | -      |
| JH7110            | SiFive U74 + SiFive S7 + SiFive E24        | [VisionFive 2][VF2]                     | Basic      | Good          | -      | Basic  | -          | -           | Good      | Good      | Basic    | Basic  | -          | Good    | Basic     | Basic   | -      | Basic  | -     | -      |
| K230              | XuanTie C908                               | [CanMV K230][K230]                      | -          | Basic         | Basic  | -      | -          | -           | -         | -         | -        | Basic  | -          | -       | -         | -       | -      | -      | -     | -      |
| K510              | K510 (?)                                   | [Canaan K510-CRB-V1.2 KIT][K510]        | -          | -             | -      | -      | -          | -           | -         | -         | -        | -      | -          | -       | Basic     | -       | -      | -      | -     | -      |
| D1 (D1-H)         | XuanTie C906                               | [LicheeRV/AWOL Nezha][C906]             | Basic      | Good          | Good   | -      | -          | -           | Good      | -         | Basic    | Basic  | Basic      | -       | -         | Basic   | -      | -      | -     | -      |
| D1 (D1-H)         | XuanTie C906                               | [DongshanPI-Nezha STU][DongshanPI-STU]  | CFT        | CFT           | -      | -      | -          | -           | -         | -         | -        | -      | CFT        | -       | CFT       | CFT     | -      | -      | -     | -      |
| D1 (D1-H)         | XuanTie C906                               | [MangoPi MQ Pro][mangopi_mq_pro]        | CFT        | CFT           | CFT    | -      | -          | -           | -         | -         | CFT      | CFT    | CFT        | CFT     | -         | CFT     | -      | -      | -     | -      |
| D1s               | XuanTie C906                               | [DongShanPI D1s][DongShanPI-D1s]        | -          | -             | -      | -      | -          | -           | -         | -         | -        | -      | CFT        | -       | -         | -       | -      | -      | -     | -      |
| D1s               | XuanTie C906                               | [Mangopi MQ][mangopi_mq]                | -          | -             | -      | -      | -          | -           | -         | -         | -        | -      | CFT        | -       | -         | -       | -      | -      | -     | -      |
| D1s               | XuanTie C906                               | [D1s NeZha][NeZha-D1s]                  | -          | -             | -      | -      | -          | -           | -         | -         | -        | Basic  | CFT        | -       | -         | -       | -      | -      | -     | -      |
| U740              | SiFive U74 + SiFive S7                     | [HiFive Unmatched][Unmatched]           | -          | Basic         | Basic  | -      | -          | -           | Good      | Good      | Basic    | Basic  | -          | -       | -         | Basic   | -      | CFT    | -     | -      |
| SG2000            | XuanTie C906 + ARM Cortex-A53              | [Milk-V Duo S][DuoS]                    | -          | Basic         | -      | -      | -          | -           | -         | -         | -        | -      | -          | -       | Basic     | -       | -      | -      | -     | -      |
| JH7110            | SiFive U74 + SiFive S7 + SiFive E24        | [Milk-V Mars][Mars]                     | -          | Basic         | -      | -      | -          | -           | -         | -         | -        | Basic  | -          | -       | Basic     | -       | -      | CFT    | -     | -      |
| FSL1030M          | Nuclei UX608                               | [Milk-V Vega][Vega]                     | -          | -             | -      | -      | -          | -           | -         | -         | -        | -      | -          | -       | CFH       | -       | -      | -      | -     | -      |
| TH1520            | XuanTie C910 + XuanTie C906 + XuanTie E902 | [Milk-V Meles][Meles]                   | -          | CFT           | -      | -      | -          | -           | -         | -         | -        | -      | -          | -       | -         | -       | -      | -      | -     | -      |
| TH1520            | XuanTie C910 + XuanTie C906 + XuanTie E902 | [Lichee Cluster 4A][Cluster4A]          | -          | Basic         | Basic  | -      | -          | -           | Basic     | Basic     | -        | Basic  | -          | Basic   | -         | Basic   | -      | -      | -     | -      |
| TH1520            | XuanTie C910 + XuanTie C906 + XuanTie E902 | [Lichee Console 4A][Console4A]          | -          | Good          | -      | -      | -          | -           | -         | -         | -        | -      | -          | -       | -         | -       | -      | -      | -     | -      |
| SG2002            | XuanTie C906 + ARM Cortex-A53              | [LicheeRV Nano][LicheeRVNano]           | -          | Basic         | -      | -      | -          | -           | -         | -         | -        | -      | -          | -       | Basic     | -       | -      | -      | -     | -      |
| BL808             | XuanTie C906 + XuanTie E907 + XuanTie E902 | [Sipeed M1s Dock][SipeedM1s]            | -          | -             | -      | -      | -          | -           | -         | -         | -        | -      | -          | -       | Basic     | -       | -      | -      | -     | -      |
| Keystone K1       | SpacemiT X60                               | [BananaPi BPI-F3][BPI-F3]               | -          | -             | -      | -      | -          | -           | -         | -         | -        | -      | -          | Basic   | -         | -       | Basic  | -      | -     | -      |
| Keystone K1       | SpacemiT X60                               | [Milk-V Jupiter][Jupiter]               | -          | -             | CFT    | -      | -          | -           | -         | -         | -        | CFT    | -          | -       | -         | -       | CFT    | -      | -     | -      |
| TH1520            | XuanTie C910 + XuanTie C906 + XuanTie E902 | [BeagleV-Ahead]                         | -          | -             | -      | -      | -          | -           | -         | -         | -        | CFT    | -          | -       | -         | -       | -      | -      | CFT   | -      |
| MPFS025T          | SiFive U54 + SiFive E51                    | [BeagleV-Fire]                          | -          | -             | -      | -      | -          | -           | -         | -         | -        | CFT    | -          | -       | -         | -       | -      | -      | -     | -      |
| JH7110            | SiFive U74 + SiFive S7 + SiFive E24        | [Star64]                                | CFT        | CFT           | -      | CFT    | -          | -           | CFT       | CFT       | CFT      | CFT    | -          | CFT     | CFT       | CFT     | -      | CFT    | CFT   | -      |
| MPFS250T          | SiFive U54 + SiFive E51                    | [PolarFire FPGA SoC Icicle Kit][Icicle] | CFT        | -             | -      | -      | -          | -           | -         | -         | -        | Basic  | -          | -       | Basic     | -       | -      | -      | Basic | -      |
| PIC64GX1000-V/FCS | SiFive U54 + SiFive E51                    | [PIC64GX Curiosity Kit][PIC64GX]        | -          | -             | -      | -      | -          | -           | -         | -         | -        | CFT    | -          | -       | -         | -       | -      | -      | CFT   | -      |

---

## *BSD


| CPU      | IP Core                             | Product/Model                           | FreeBSD | OpenBSD | NetBSD |
|----------|-------------------------------------|-----------------------------------------|---------|---------|--------|
| JH7100   | SiFive U74 + SiFive E24             | [VisionFive][VF1]                       | -       | Basic   | -      |
| JH7110   | SiFive U74 + SiFive S7 + SiFive E24 | [VisionFive 2][VF2]                     | WIP     | Basic   | Basic  |
| U740     | SiFive U74 + SiFive S7              | [HiFive Unmatched][Unmatched]           | Basic   | Basic   | -      |
| D1-H     | XuanTie C906                        | [DongshanPI-Nezha STU][DongshanPI-STU]  | CFT     | -       | -      |
| D1-H     | XuanTie C906                        | [MangoPi MQ Pro][mangopi_mq_pro]        | CFT     | -       | CFT    |
| MPFS250T | SiFive U54 + SiFive E51             | [PolarFire FPGA SoC Icicle Kit][Icicle] | -       | CFT     | -      |

---

## RTOS / 实时操作系统

![RTOS](assets/rtos.svg)

---

## 其它

![Others](assets/others.svg)

---

#### 说明

* Good：支持图形界面
* Basic：能启动运行
* CFH (Call for help)：官方/论坛资料表示支持，但是未跑通
* CFT (Call for testing)：镜像链接有，但是缺乏硬件设备验证
* CFI (Call for more information)：官方资料宣称有，但是找不到镜像文件等实际可用的资料
* WIP：官方宣发操作系统即将/正在对开发板进行支持，但暂未获取到可用的镜像
* -：暂未从官方或者其它渠道获取到开发板的支持信息

[Pioneer]: ./Pioneer/README_zh.md
[Duo]: ./Duo/README_zh.md
[Duo256m]: ./Duo256m/README_zh.md
[LPi4A]: ./LicheePi4A/README_zh.md
[VF1]: ./VisionFive/README_zh.md
[VF2]: ./VisionFive2/README_zh.md
[K230]: ./K230/README_zh.md
[C906]: ./D1_LicheeRV/README_zh.md
[Unmatched]: ./Unmatched/README_zh.md
[DuoS]: ./Duo_S/README_zh.md
[Mars]: ./Mars/README_zh.md
[Vega]: ./Vega/README_zh.md
[Meles]: ./Meles/README_zh.md
[MaixBit]: ./Maix-I_K210/README_zh.md
[Cluster4A]: ./LicheeCluster4A/README_zh.md
[Console4A]: ./LicheeConsole4A/README_zh.md
[LicheeRVNano]: ./LicheeRV_Nano/README_zh.md
[TangMega138K]: ./Tang_Mega_138K/README_zh.md
[K510]: ./K510/README_zh.md
[SipeedM1s]: ./M1s/README_zh.md
[M0sense]: ./M0sense/README_zh.md
[M0P]: ./M0P_Dock/README_zh.md
[M0s]: ./M0s/README_zh.md
[CH32V103]: ./CH32V103/README_zh.md
[CH32V203]: ./CH32V203/README_zh.md
[CH32V208]: ./CH32V208/README_zh.md
[CH32V303]: ./CH32V303/README_zh.md
[CH32V305]: ./CH32V305/README_zh.md
[CH32V307]: ./CH32V307/README_zh.md
[CH582F]: ./CH582F/README_zh.md
[CH592X]: ./CH592X/README_zh.md
[Longan_Nano]: ./Longan_Nano/README_zh.md
[RV_STAR]: ./RV_STAR/README_zh.md
[DDR200T]: ./DDR200T/README_zh.md
[V853]: ./V853/README_zh.md
[100ASK]: ./100ASK/README_zh.md
[YouMuPI]: ./YouMuPI/README_zh.md
[TinyVision]: ./TinyVision/README_zh.md
[CH573F]: ./CH573F/README_zh.md
[DongshanPI-STU]: ./DongshanPI-STU/README_zh.md
[mangopi_mq_pro]: ./mangopi_mq_pro/README_zh.md
[DongShanPI-D1s]: ./DongShanPI-D1s/README_zh.md
[mangopi_mq]: ./mangopi_mq/README_zh.md
[NeZha-D1s]: ./NeZha-D1s/README_zh.md
[BPI-F3]: ./BPI-F3/README_zh.md
[Jupiter]: ./Jupiter/README_zh.md
[BeagleV-Ahead]: ./BeagleV-Ahead/README_zh.md
[BeagleV-Fire]: ./BeagleV-Fire/README_zh.md
[STAR64]: ./STAR64/README_zh.md
[Icicle]: ./Icicle/README_zh.md
[PIC64GX]: ./PIC64GX/README_zh.md
[CM32M433R]: ./CM32M433R/README_zh.md
[R128-EVT]: ./R128-EVT/README_zh.md
