# CH32V103C

## 测试环境

### 操作系统信息

- FreeRTOS
    - 源码链接：https://www.wch.cn/downloads/CH32V103EVT_ZIP.html
    - 参考文档：官方文档位于压缩包内
        - PlatformIO 提供文档：https://github.com/Community-PIO-CH32V/platform-ch32v
- RT-Thread / FreeRTOS (PlatformIO)
    - 源码链接：https://github.com/Community-PIO-CH32V/ch32-pio-projects
    - 参考文档：
        - PlatformIO Core：https://docs.platformio.org/en/latest/core/installation/index.html
        - PlatformIO CH32V：https://pio-ch32v.readthedocs.io/en/latest/installation.html


### 硬件开发板信息

- CH32V103C-EVT-R1-1v1

## 测试结果

| 软件分类      | 软件包名      | 测试结果（测试报告）|
|--------------|-------------|------------------|
| FreeRTOS     | N/A         | [成功][FreeRTOS]  |
| FreeRTOS     | PlatformIO  | [成功][FreeRTOS_pio]  |
| RT-Thread    | N/A         | [成功][RTThread]  |

[FreeRTOS]: ./FreeRTOS/README_zh.md
[RTThread]: ./RT-Thread/README_zh.md
[FreeRTOS_pio]: ./FreeRTOS/README_pio_zh.md
