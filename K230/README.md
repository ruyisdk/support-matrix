# CanMV K230

## Test Environment

### Operating System Information

- Canaan Kendryte K230 Official CanMV Debian SDK
  - Download Link: https://kendryte-download.canaan-creative.com/developer/k230/canmv_debian_sdcard_sdk_1.3.img.gz
  - Reference Installation Document: https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month08/Week3/CanMV-K230.md
- Canaan Kendryte K230 Official CanMV Ubuntu SDK
  - Download Link: https://kendryte-download.canaan-creative.com/developer/k230/canmv_ubuntu_sdcard_1.3.img.gz
  - Reference Installation Document: https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month08/Week3/CanMV-K230.md
- Fedora 38
  - Download Link: https://github.com/ruyisdk/mkimg-k230-rv64ilp32/releases
  - Reference Installation Document: https://developer.canaan-creative.com/k230/dev/zh/CanMV_K230_%E6%95%99%E7%A8%8B.html
- RT-Thread
  - Download Link: https://github.com/kendryte/k230_sdk/releases/tag/v1.4
  - Reference Installation Document: https://github.com/kendryte/k230_docs/blob/main/zh/01_software/board/K230_SDK_%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E.md

### Hardware Information

- Canaan Kendryte K230

## Test Results

| Software Category              | Package Name | Test Results (Test Report)                |
| ------------------------------ | ------------ | ----------------------------------------- |
| Debian Image Boot              | N/A          | [Successful][K230Debian] (Official Image) |
| Ubuntu Image Boot              | N/A          | [Successful][K230Ubuntu] (Official Image) |
| Fedora Image Boot              | N/A          | [Successful][Fedora]                      |
| RT-Thread Image Build and Boot | N/A          | [Successful][RT-Thread] (Official Image)  |
| NuttX Image Build and Boot     | N/A          | [Successful][NuttX]                       |

[K230Debian]: ./Debian/README.md
[K230Ubuntu]: ./Ubuntu/README.md
[Fedora]: ./Fedora/README.md
[RT-Thread]: ./RT-Thread/README.md
[NuttX]: ./NuttX/README.md
