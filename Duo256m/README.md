# Milk-V Duo 256M

## Test Environment

### Operating System Information

- BuildRoot & FreeRTOS
  - Download link: [https://github.com/milkv-duo/duo-buildroot-sdk/releases](https://github.com/milkv-duo/duo-buildroot-sdk/releases)
    - Official Milk-V provided BuildRoot SDK, which also includes FreeRTOS.
  - Reference Installation Document: [https://github.com/milkv-duo/duo-buildroot-sdk](https://github.com/milkv-duo/duo-buildroot-sdk)
- Debian
  - Download link: [https://github.com/Fishwaldo/sophgo-sg200x-debian](https://github.com/Fishwaldo/sophgo-sg200x-debian)
  - Reference Installation Document: [https://github.com/Fishwaldo/sophgo-sg200x-debian](https://github.com/Fishwaldo/sophgo-sg200x-debian)
- RT-Thread
  - Source code link: [https://github.com/RT-Thread/rt-thread](https://github.com/RT-Thread/rt-thread)
  - Reference Installation Document: [https://github.com/RT-Thread/rt-thread/blob/6101f1fd29374ac69c107e3cfeadfa06b0c901f9/bsp/cvitek/cv18xx_risc-v/README.md](https://github.com/RT-Thread/rt-thread/blob/6101f1fd29374ac69c107e3cfeadfa06b0c901f9/bsp/cvitek/cv18xx_risc-v/README.md)

### Hardware Information

- Milk-V Duo (256M, SG2002)

## Test Results

| Software Category         | Package Name | Test Result (Report)                         |
|---------------------------|--------------|---------------------------------------------|
| BuildRoot Image Boot      | N/A          | [Success][BuildRoot]                     |
| FreeRTOS Boot             | N/A          | [Success][FreeRTOS] (Included in BuildRoot image) |
| Debian Image Boot         | N/A          | [Success][Debian]                        |
| RT-Thread Image Build & Boot | N/A        | [Success][RT-Thread]                     |
| Zephyr Image Build & Boot | N/A          | [Success][Zephyr]                        |
  
[BuildRoot]: ./BuildRoot/README.md
[Debian]: ./Debian/README.md
[RT-Thread]: ./RT-Thread/README.md
[FreeRTOS]: ./FreeRTOS/README.md
[Zephyr]: ./Zephyr/README.md
