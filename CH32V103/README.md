# CH32V103C

## Test Environment

### System Information

- FreeRTOS
    - Source code link: [https://www.wch.cn/downloads/CH32V103EVT_ZIP.html](https://www.wch.cn/downloads/CH32V103EVT_ZIP.html)
    - Reference Installation Document: Official documentation is located inside the compressed package
        - PlatformIO documentation: [https://github.com/Community-PIO-CH32V/platform-ch32v](https://github.com/Community-PIO-CH32V/platform-ch32v)
- RT-Thread / FreeRTOS (PlatformIO)
    - Source code link: [https://github.com/Community-PIO-CH32V/ch32-pio-projects](https://github.com/Community-PIO-CH32V/ch32-pio-projects)
    - Reference Installation Document:
        - PlatformIO Core: [https://docs.platformio.org/en/latest/core/installation/index.html](https://docs.platformio.org/en/latest/core/installation/index.html)
        - PlatformIO CH32V: [https://pio-ch32v.readthedocs.io/en/latest/installation.html](https://pio-ch32v.readthedocs.io/en/latest/installation.html)


### Hardware Information

- CH32V103C-EVT-R1-1v1

## Test Results

| Software Category | Package Name | Test Result (Test Report) |
| ----------------- | ------------ | ------------------------- |
| FreeRTOS          | N/A          | [Success][FreeRTOS]       |
| FreeRTOS          | PlatformIO   | [Success][FreeRTOS_pio]   |
| RT-Thread         | N/A          | [Success][RTThread]       |

[FreeRTOS]: ./FreeRTOS/README.md
[RTThread]: ./RT-Thread/README.md
[FreeRTOS_pio]: ./FreeRTOS/README_pio.md
