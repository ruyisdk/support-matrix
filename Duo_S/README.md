---
vendor: milkv-duos
product: Milk-V Duo S
cpu: SG2000
cpu_core: XuanTie C906 + ARM Cortex-A53
ram: 256MB
---

# Milk-V Duo S

## Test Environment

### Operating System Information

- BuildRoot & FreeRTOS
  - Download Link: https://github.com/milkv-duo/duo-buildroot-sdk/releases
    - BuildRoot SDK provided by Milk-V, which also includes FreeRTOS
  - Reference Installation Document: https://github.com/milkv-duo/duo-buildroot-sdk
- Apache NuttX RTOS
  - Source Code Links
    - NuttX: https://github.com/lupyuen2/wip-nuttx: /tree/sg2000
    - NuttX Apps: https://github.com/lupyuen2/wip-nuttx-apps/tree/sg2000
  - Reference Installation Document: https://github.com/lupyuen/nuttx-sg2000
- Debian
  - Download Link: https://github.com/Fishwaldo/sophgo-sg200x-debian/releases/tag/v1.4.0
  - Reference Installation Document: https://github.com/Fishwaldo/sophgo-sg200x-debian
- Zephyr
  - Source Code Link: https://github.com/zephyrproject-rtos/zephyr/tree/main
  - Reference Installation Document:
      - https://docs.zephyrproject.org/latest/develop/getting_started/index.html
      - https://github.com/milkv-duo/duo-buildroot-sdk
- Ubuntu
  - Download Link: https://drive.google.com/file/d/1mkzLhvtjJup3GbgWKZdwL80PZMMXg7n1/view
  - Reference Installation Document: https://xyzdims.com/3d-printers/misc-hardware-notes/iot-milk-v-duo-risc-v-esbc-running-linux/
- OpenWrt
  - Download Link: https://github.com/draftbottle/Milkv-duo-openwrt/releases/download/v4.0/milkv-duos.img
  - Reference Installation Document:
	  - https://community.milkv.io/t/milk-v-duo-openwrt/2399/10
	  - https://github.com/draftbottle/VizOS

### Hardware Information

- Milk-V Duo S (512M, SG2000)

## Test Results

| Software Category           | Package Name | Test Result (Report)    |
|-----------------------------|--------------|-------------------------|
| BuildRoot Image Boot        | N/A          | [Successful][BuildRoot] |
| Debian Image Boot           | N/A          | [Successful][Debian]    |
| FreeRTOS Boot               | mailbox-test | [Successful][FreeRTOS]  |
| Apache NuttX Build and Boot | N/A          | [Successful][NuttX]     |
| Zephyr Image Build and Boot | N/A          | [Successful][Zephyr]    |
| Ubuntu Image Boot           | N/A          | [Successful][Ubuntu]    |
| OpenWrt Build and Boot      | N/A          | [Successful][OpenWrt]   |

[BuildRoot]: ./BuildRoot/README.md
[Debian]: ./Debian/README.md
[FreeRTOS]: ./FreeRTOS/README.md
[NuttX]: ./NuttX/README.md
[Zephyr]: ./Zephyr/README.md
[Ubuntu]: ./Ubuntu/README.md
[OpenWrt]: ./OpenWrt/README.md
