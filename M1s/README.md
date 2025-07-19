---
product: Sipeed M1s Dock
cpu: BL808
cpu_core: XuanTie C906 + XuanTie E907 + XuanTie E902
ram: 768KB(SRAM) + 64MB(PSRAM)

vendor: sipeed-m1s
---

# Sipeed M1s

## Test Environment

### Operating System Information

- FreeRTOS
  - Download Link:
    - SDK: https://gitee.com/Sipeed/M1s_BL808_SDK
    - Examples: https://gitee.com/Sipeed/M1s_BL808_example
  - Reference Installation Document: https://wiki.sipeed.com/hardware/zh/maix/m1s/other/start.html
  - Download Link: https://github.com/openbouffalo/buildroot_bouffalo/releases/download/v1.0.1/bl808-linux-pine64_ox64_full_defconfig.tar.gz
    - SDK: https://github.com/bouffalolab/bl_mcu_sdk
    - Flashing Tool: https://openbouffalo.org/static-assets/bldevcube/BouffaloLabDevCube-v1.8.3.zip
  - Reference Installation Document: https://wiki.postmarketos.org/wiki/Sipeed_M1s_DOCK_(sipeed-m1sdock)
- BuildRoot/postmarketOS
  - Download Link: https://github.com/openbouffalo/buildroot_bouffalo/releases/download/v1.0.1/bl808-linux-pine64_ox64_full_defconfig.tar.gz
    - SDK：https://github.com/bouffalolab/bl_mcu_sdk
    - Flashing tool: https://openbouffalo.org/static-assets/bldevcube/BouffaloLabDevCube-v1.8.3.zip
  - Reference Installation Document: https://wiki.postmarketos.org/wiki/Sipeed_M1s_DOCK_(sipeed-m1sdock)
- RT-Thread
  - Download Link: https://github.com/DongshanPI/buildroot_dongshannezhastu
  - Reference Installation Document: https://github.com/RT-Thread/rt-thread/tree/master/bsp/bouffalo_lab/bl808

### Hardware Information

- Sipeed M1s Dock

## Test Results

| Software Category    | Package Name | Test Result (Test Report) |
| -------------------- | ------------ | ------------------------- |
| BuildRoot Image Boot | N/A          | [CFH][BuildRoot]          |
| postmarketOS Boot    | N/A          | [CFH][pmOS]               |
| FreeRTOS Boot        | hello_world  | [Successful][FreeRTOS]    |
| RT-Thread Boot       | N/A          | [CFH][RT-Thread]          |

[BuildRoot]: ./BuildRoot/README.md
[RT-Thread]: ./RT-Thread/README.md
[pmOS]: ./postmarketOS/README.md
[FreeRTOS]: ./FreeRTOS/README.md
