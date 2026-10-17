---
product: RT-Thread RDC2022 Memorial Board (D1s)
cpu: D1s
cpu_core: XuanTie C906
ram: 64MB DDR2 (SiP)
vendor: RT-Thread
---

# RT-Thread RDC2022 Memorial Board (D1s)

This is the RDC2022 Memorial Board, a compact development board produced by the
RT-Thread community to commemorate the 2022 RT-Thread Developer Conference.
It is powered by the Allwinner D1s SoC, which integrates a XuanTie C906 RISC-V
core (RV64IMAFDCVU @ 1.008 GHz) with 64 MB of DDR2 memory in a SiP package.

- **Memory**: 64 MB DDR2 (SiP package)
- **Storage**: 121 MB onboard SD NAND (marked `SDN1G`, 126,877,696 bytes),
  connected via the SDC0 controller (PF0–PF5)
- **Debug**: CH340N USB-to-UART bridge accessible through the Type-C debug
  port, wired to SoC PE2/UART0_TX and PE3/UART0_RX