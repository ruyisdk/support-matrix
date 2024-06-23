# Sipeed M1s

## Test Environment

### Operating System Information

- FreeRTOS
  - Download Link:
    - SDK: https://gitee.com/Sipeed/M1s_BL808_SDK
    - Examples: https://gitee.com/Sipeed/M1s_BL808_example
  - Reference Installation Document: https://wiki.sipeed.com/hardware/zh/maix/m1s/other/start.html
- BuildRoot
  - Download Link: https://dl.sipeed.com/fileList/MAIX/M1s/M1s_Dock/7_Firmware/m1sdock_linux_20221116.zip
    - SDK: https://github.com/sipeed/M1s_BL808_Linux_SDK
    - Flashing Tool: https://dev.bouffalolab.com/download
  - Reference Installation Document: https://wiki.sipeed.com/hardware/zh/maix/m1s/other/start.html

### Hardware Information

- Sipeed M1s Dock

## Test Results

| Software Category         | Package Name | Test Result (Test Report) |
|---------------------------|--------------|---------------------------|
| BuildRoot Image Boot      | N/A          | [Successful][BuildRoot]   |
| FreeRTOS Boot             | hello_world  | [Successful][FreeRTOS]    |

[BuildRoot]: ./BuildRoot/README.md
[FreeRTOS]: ./FreeRTOS/README.md
