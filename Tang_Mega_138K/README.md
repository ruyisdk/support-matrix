# Tang Mega 138K Pro

## Test Environment

### Operating System Information

- RT-Thread
    - Source Code Link: https://cdn.gowinsemi.com.cn/RiscV_AE350_SOC_V1.1.zip
    - Reference Installation Document: https://cdn.gowinsemi.com.cn/MUG1029-1.1_Gowin_RiscV_AE350_SOC%E8%BD%AF%E4%BB%B6%E7%BC%96%E7%A8%8B%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf
    - Reference Design Document: https://cdn.gowinsemi.com.cn/MUG1031-1.1_Gowin_RiscV_AE350_SOC%E7%A1%AC%E4%BB%B6%E8%AE%BE%E8%AE%A1%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf
    - Toolchain:
        - Gowin Cloud Source Software: http://www.gowinsemi.com.cn/faq.aspx
        - RiscV AE350 SOC RDS Software: https://cdn.gowinsemi.com.cn/RiscV_AE350_SOC_RDS_V1.1_win.zip
        - Andes-Development-Kit: https://github.com/andestech/Andes-Development-Kit
- Zephyr
    - Source Code Link: https://cdn.gowinsemi.com.cn/RiscV_AE350_SOC_V1.1.zip
    - Reference Installation Document: https://cdn.gowinsemi.com.cn/MUG1029-1.1_Gowin_RiscV_AE350_SOC%E8%BD%AF%E4%BB%B6%E7%BC%96%E7%A8%8B%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf
    - Reference Design Document: https://cdn.gowinsemi.com.cn/MUG1031-1.1_Gowin_RiscV_AE350_SOC%E7%A1%AC%E4%BB%B6%E8%AE%BE%E8%AE%A1%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf
    - Toolchain:
        - Gowin Cloud Source Software: http://www.gowinsemi.com.cn/faq.aspx
        - RiscV AE350 SOC RDS Software: https://cdn.gowinsemi.com.cn/RiscV_AE350_SOC_RDS_V1.1_win.zip
        - Andes-Development-Kit: https://github.com/andestech/Andes-Development-Kit
- FreeRTOS
    - Source Code Link: https://cdn.gowinsemi.com.cn/RiscV_AE350_SOC_V1.1.zip
    - Reference Installation Document: https://cdn.gowinsemi.com.cn/MUG1029-1.1_Gowin_RiscV_AE350_SOC%E8%BD%AF%E4%BB%B6%E7%BC%96%E7%A8%8B%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf
    - Reference Design Document: https://cdn.gowinsemi.com.cn/MUG1031-1.1_Gowin_RiscV_AE350_SOC%E7%A1%AC%E4%BB%B6%E8%AE%BE%E8%AE%A1%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf
    - Toolchain:
        - Gowin Cloud Source Software: http://www.gowinsemi.com.cn/faq.aspx
        - RiscV AE350 SOC RDS Software: https://cdn.gowinsemi.com.cn/RiscV_AE350_SOC_RDS_V1.1_win.zip
        - Andes-Development-Kit: https://github.com/andestech/Andes-Development-Kit

### Hardware Information

- Tang Mega 138K Pro Dock

## Test Results

| Software Category               | Package Name | Test Results (Test Report)   |
| ------------------------------- | ------------ | --------------------------- |
| FreeRTOS Image Build and Boot   | N/A          | [Basic][FreeRTOS]           |
| RT-Thread nano Image Build and Boot | N/A      | [Basic][RT-Thread-nano]     |
| RT-Thread std Image Build and Boot | N/A       | [Basic][RT-Thread-std]      |
| Zephyr Image Build and Boot     | N/A          | [CFH][Zephyr]               |

[FreeRTOS]: ./FreeRTOS/README.md
[RT-Thread-std]: ./RT-Thread/README.md
[RT-Thread-nano]: ./RT-Thread/README.md
[Zephyr]: ./Zephyr/README.md
