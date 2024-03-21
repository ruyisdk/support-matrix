## RISCV Board and OS Supported Matrix

## 主流操作系统 for RISC-V 硬件适配情况（主流 RISC-V 开发板）

| CPU      | 产品型号                      | Arch Linux | Debian/RevyOS | Fedora | FreeBSD | Gentoo | openAnolis | OpenBSD | openCloudOS | openEuler | openKylin | openSUSE | Ubuntu | Tina-Linux | Android 13 | Armbian | BuildRoot | OpenHarmony | FreeRTOS | RT-Thread | Zephyr | OpenWRT | ThreadX |
| -------- | ----------------------------- | ---------- | ------------- | ------ | ------- | ------ | ---------- | ------- | ----------- | --------- | --------- | -------- | ------ | ---------- | ---------- | ------- | --------- | ----------- | -------- | --------- | ------ | ------- | ------- |
| SG2042   | [Pioneer Box][Pioneer]        | CFT        | Good          | Good   | N/A     | CFT    | N/A        | N/A     | WIP         | Good      | Good      | N/A      | N/A    | N/A        | N/A        | N/A     | N/A       | WIP         | N/A      | N/A       | N/A    | N/A     | N/A     |
| CV1800B  | [Milk-V Duo][Duo]             | CFT        | CFT           | CFT    | N/A     | CFT    | N/A        | N/A     | N/A         | CFT       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | Basic     | N/A         | CFT      | CFT       | N/A    | WIP     | N/A     |
| TH1520   | [LicheePi 4A][LPi4A]          | Good       | Good          | Good   | N/A     | CFT    | CFT        | N/A     | N/A         | Good      | Good      | N/A      | WIP    | N/A        | N/A        | Good    | N/A       | WIP         | N/A      | N/A       | N/A    | CFT     | N/A     |
| JH7100   | [VisionFive 1][VF1]          | CFT        | CFT          | Good   | CFT     | CFT    | CFT        | CFT     | N/A         | Good     | Good     | CFT      | Good  | N/A        | N/A        | CFT     | CFT     | CFT         | N/A      | CFT       | N/A    | CFT     | N/A     |
| JH7110   | [VisionFive 2][VF2]           | CFT        | Good          | CFT    | CFT     | CFT    | CFT        | CFT     | N/A         | Good      | Good      | CFT      | Good   | N/A        | WIP        | CFT     | Basic     | WIP         | N/A      | CFT       | N/A    | CFT     | N/A     |
| K230     | [CanMV K230][K230]            | CFT        | Basic         | N/A    | N/A     | CFT    | CFT        | CFT     | CFT         | CFT       | N/A       | N/A      | Basic  | N/A        | N/A        | N/A     | N/A       | N/A         | N/A      | CFT       | N/A    | CFT     | N/A     |
| C906     | [LicheeRV/AWOL Nezha][C906]   | CFT        | Good          | Good   | N/A     | CFT    | CFT        | N/A     | N/A         | Good      | N/A       | N/A      | Good   | Basic      | N/A        | N/A     | N/A       | N/A         | N/A      | N/A       | N/A    | Basic   | N/A     |
| U740     | [HiFive Unmatched][Unmatched] | CFT        | Basic         | Good   | Basic   | CFT    | N/A        | Basic   | N/A         | Good      | Good      | CFT      | Good   | N/A        | N/A        | CFH     | N/A       | WIP         | N/A      | N/A       | Basic  | Basic   | N/A     |
| SG2000   | [Milk-V Duo S][DuoS]          | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | Basic     | N/A         | CFT      | N/A       | N/A    | N/A     | N/A     |
| JH7110   | [Milk-V Mars][Mars]           | CFT        | Good          | CFT    | CFT     | CFT    | CFT        | CFT     | N/A         | Good      | Good      | CFT      | Good   | N/A        | WIP        | CFT     | Basic     | WIP         | N/A      | CFT       | N/A    | CFT     | N/A     |
| FSL1030M | [Milk-V Vega][Vega]           | N/A        | N/A           | N/A    | N/A     | N/A    | N/A        | N/A     | N/A         | N/A       | N/A       | N/A      | N/A    | N/A        | N/A        | N/A     | CFH       | N/A         | N/A      | N/A       | N/A    | N/A     | N/A     |

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
[LPi4A]: ./LicheePi4A/README.md
[VF1]: ./VisionFive1/README.md
[VF2]: ./VisionFive2/README.md
[K230]: ./K230/README.md
[C906]: ./D1_LicheeRV/README.md
[Unmatched]: ./Unmatched/README.md
[DuoS]: ./Duo_S/README.md
[Mars]: ./Mars/README.md
[Vega]: ./Vega/README.md