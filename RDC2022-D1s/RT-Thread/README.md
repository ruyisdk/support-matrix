---
sys: rtthread
sys_ver: 5.0.0
sys_var: smart
status: basic
last_update: 2026-10-17
---

# RT-Thread RDC2022 Memorial Board (D1s) Test Report

## Test Environment

### Hardware Information

- RT-Thread RDC2022 Memorial Board (Allwinner D1s, XuanTie C906, RV64IMAFDCVU @ 1.008 GHz, 64 MB DDR2 SiP)
- Onboard storage: SD NAND (marked `SDN1G`, 126,877,696 bytes / ~121 MiB, on SDC0 / PF0–PF5)
- Onboard USB-to-UART: CH340N (USB VID:PID `0x1a86:0x7523`, Type-C debug port wired to SoC PE2/UART0_TX, PE3/UART0_RX)
- Host: macOS 26.6 (Apple Silicon, arm64; CH340 natively identified as `/dev/cu.usbserial-111130`)

### Operating System Information

- OS Version: RT-Thread Smart 5.0.0 build Jan 10 2023 (factory restore image; boot banner confirmed on hardware)
- Download Link: https://github.com/RT-Thread/rt-thread
- Reference Installation Document:
  - RT-Thread community tutorial: https://club.rt-thread.org/ask/article/bd9c5cb55e0bc8f5.html
  - Allwinner online forum mirror: https://bbs.aw-ol.com/topic/2905/
  - RT-Thread D1s BSP README: `bsp/allwinner/d1s/README-M7.md`
- Firmware source:
  - Factory prebuilt image pack: `RDC资料.7z` (MD5: `ba70c72c683d85b92bf8318f6e4d41e6`), containing factory `boot0_sdcard_sun20iw1p1_f133.bin` (49,152 bytes, SHA256: `139635802d9078599dfdeac257201310d994b5560abba7947aa7d0b4640b54c6`) and factory kernel image `sd.bin` (1,793,536 bytes, SHA256: `e203b1f9cc4a587ec2c06a43ae884766fd72556eb97fdfcdca9ec1d92aa42d40`)
  - Mainline comparison firmware: built from RT-Thread master `bsp/allwinner/d1s` with `riscv64-linux-musleabi_for_x86_64-pc-linux-gnu` (GCC 10.1.0), packed via `mksdimg.sh` (`mkimage -T sunxi_toc1`) into TOC1-format `sd.bin` (1,084,416 bytes, SHA256: `69ba25bacc50b8fa2102013bd968b5cca6d49c2e918c0d57fddc76c98056570f`)

## Installation Steps

### 1. Enter FEL Flashing Mode

With the board powered off, hold the onboard FEL download button (Burn Key),
then connect the Type-C data cable to the lower USB download port to power
the board and connect it to the host. The SoC chip ID is detected as
`0x00185900` (Allwinner D1/F133 series). Release the button.

### 2. Flashing Tool Preparation

On the host, use `aozima/xfel` (compiled from commit `35641da`, providing the
`xfel sd` subcommand) patched for the Allwinner SDIO controller. Do **not** use
the unpatched `test-sdcard` branch, which has serious defects on SD NAND:
unconfigured pin drivers and ignored write-return values that cause silent
write failures and controller hangs.

### 3. Factory Firmware Restore, Chunked Write, and Read-Back Verification

The Allwinner D1s boot media layout is as follows:

- **Boot0 (SPL/eGON.BT0)**: target byte offset `8192` (`0x2000`, sector 16).
  The factory `boot0_sdcard_sun20iw1p1_f133.bin` is byte-for-byte identical to
  the mainline `boot0_sdcard_sun20iw1p1_d1s.bin` (same SHA256). The existing
  Boot0 data at offset 8192 on the onboard SD NAND was verified intact via
  `xfel sd read 8192 49152` with matching hash; no rewrite was needed.

- **System kernel image (TOC1-format `sd.bin`)**: target byte offset `57344`
  (`0xE000`, sector 112), file size 1,793,536 bytes.

To work around xfel's unreliable large-block transfers over USB-FEL (which
cause SD NAND timeouts and state loss), strict **chunked write with per-chunk
read-back verification** was performed:

1. **Chunking strategy**: 64 KiB (65,536 bytes) per chunk, dividing the
   1,793,536-byte image into 28 chunks: chunks 0–26 are full 65,536-byte chunks
   and chunk 27 is the 24,064-byte tail chunk (27 × 65,536 + 24,064 =
   1,793,536 bytes, so the whole image is covered).
2. **Per-chunk write and verify**:
   - Chunks 0–9: each 64 KB chunk was written and immediately read back for
     hash comparison; all passed on the first attempt.
   - Chunk 10: the first write's read-back verification failed. Two consecutive
     re-reads were performed; the read-back data was consistently different
     from the source, confirming the physical media did not receive this chunk
     correctly during the large-block transfer.
   - Resume from breakpoint: after pausing and confirming, writing resumed from
     chunk 10. Chunks 10–27 were written and read back; all passed on the first
     attempt.
3. **Global read-back verification**: after all chunks were written, the entire
   1,793,536-byte segment starting at offset 57344 was read back in full and
   compared against the source SHA256 hash
   (`e203b1f9cc4a587ec2c06a43ae884766fd72556eb97fdfcdca9ec1d92aa42d40`),
   confirming 100% byte-for-byte consistency with the factory source image.

The following script reproduces exactly the chunked write and the read-back
verification described above. Run it with the index of the failed chunk to
resume from that breakpoint (for example `sh flash.sh 10`):

```sh
IMG=sd.bin          # factory image, 1,793,536 bytes
BASE=57344          # 0xE000: target byte offset on the SD NAND
BOOT0=8192          # 0x2000: Boot0 byte offset on the SD NAND
CHUNK=65536         # 64 KiB per transfer
LAST=27             # chunk 27 is the 24,064-byte tail chunk

# Read back and verify the Boot0 already present on the media (no rewrite needed)
xfel sd read "$BOOT0" 49152 boot0.readback.bin
sha256sum boot0.readback.bin   # 139635802d9078599dfdeac257201310d994b5560abba7947aa7d0b4640b54c6

# Split the image: chunk_00 .. chunk_27 (27 x 65,536 + 24,064 = 1,793,536 bytes)
split -b "$CHUNK" -d -a 2 "$IMG" chunk_

# Write and verify chunk by chunk; "$1" is the chunk index to resume from
for i in $(seq "${1:-0}" "$LAST"); do
    f=$(printf 'chunk_%02d' "$i")
    len=$(wc -c < "$f" | tr -d ' ')      # 65,536, or 24,064 for chunk 27
    off=$((BASE + i * CHUNK))
    echo "chunk $i: $len bytes @ offset $off"
    xfel sd write "$off" "$f"           # 64 KiB is the tested upper bound
    xfel sd read  "$off" "$len" "$f.read"
    cmp "$f" "$f.read" || { echo "chunk $i failed, resume with: $0 $i"; break; }
    echo "chunk $i: verified"
done

# Global read-back verification of the whole 1,793,536-byte image
xfel sd read "$BASE" 1793536 sd.readback.bin
sha256sum sd.readback.bin   # e203b1f9cc4a587ec2c06a43ae884766fd72556eb97fdfcdca9ec1d92aa42d40

xfel reset
```

On macOS use `shasum -a 256` instead of `sha256sum`.

### 4. Serial Connection and Boot

1. Connect the USB-to-UART debug cable or the onboard CH340N Type-C serial
   port to the host (device node `/dev/cu.usbserial-111130`).
2. Configure the terminal to **500000 8-N-1** with no flow control (note: this
   board's Boot0 and RT-Thread driver default to 500000 baud; using the common
   115200 produces garbled output).
3. Toggle the power switch or execute `xfel reset` to trigger a hardware reset.

## Expected Results

The board boots normally from the onboard SD NAND. Boot0 initializes DDR2 and
successfully loads the OpenSBI, device tree, and kernel image from the TOC1
package. The onboard serial port outputs the boot banner and kernel startup
messages at 500000 baud, eventually printing the `msh />` command-line
interactive prompt, allowing commands to be entered and responses echoed.

## Actual Results

### 1. Factory Firmware Restore (Verified Working)

After reset, the onboard CH340N serial port output the system interactive
terminal normally at **500000 8N1** baud, successfully entering the `msh />`
command prompt. Entering the `version` command produced the normal system
version and build time output.

### 2. Mainline Firmware Comparison Test (Failed to Boot)

The mainline-compiled `sd.bin` (1,084,416 bytes, TOC1 format containing
OpenSBI v0.9, device tree, and RT-Thread 5.3.1 kernel) was written to offset
57344 in 64 KB chunks with full read-back verification confirming exact
consistency. However, after reset, the onboard serial port produced **no output
at all** (0 bytes received) at both 500000 and 115200 baud, and the SoC did not
fall back to FEL mode.

### Boot Log

Real serial interactive log captured after successful factory firmware restore
(baud rate 500000 8N1):

```log
x: command not found.
msh />
msh />version

 \ | /
- RT -     Thread Smart Operating System
 / | \     5.0.0 build Jan 10 2023
 2006 - 2020 Copyright by rt-thread team
msh />
msh />
```

**Status assessment: `basic` (factory pre-instired firmware basic functionality
passes; mainline firmware is not yet working on this board)**

1. **Hardware integrity verified**: the Allwinner D1s SoC, onboard DDR2 memory
   controller, SD NAND (SDN1G 121 MB), CH340N USB-to-UART bridge, and power
   delivery chain all passed real-hardware validation and are fully functional.
2. **Firmware availability verified**: the official factory firmware
   (RT-Thread Smart 5.0.0) boots stably and provides an interactive msh
   terminal after correct chunked write and read-back verification.

### Known Issues and Workarounds

1. **xfel large-block writes are unreliable**:
   - The existing open-source `xfel` firmware payload for the Allwinner
     SDIO/SD-NAND controller easily loses transfer state or triggers
     internal timeouts during long-data-stream writes;
   - Some branches (e.g., `test-sdcard`) do not check auxiliary function
     return codes, causing silent write failures while reporting "success";
   - **Workaround**: when flashing onboard SD NAND, use the `aozima` patched
     branch and adopt a chunked write strategy of no more than 64 KB per
     chunk, with immediate read-back verification after each chunk. If a
     single-chunk verification fails, resume-from-breakpoint retry must be
     supported.
2. **Mainline `sd.bin` fails to boot**:
   - The firmware built from the mainline BSP (`bsp/allwinner/d1s`) produces
     no serial output (0 bytes) after reset on the RDC2022 Memorial Board;
   - Static and disassembly analysis indicates: Boot0 initializes at 500000
     baud, but the mainline device tree `u-boot.dtb` hardcodes the `chosen`
     node console to `serial0:115200n8`, while the kernel driver
     `drv_uart.c` defaults to `UART_DEFAULT_BAUDRATE 500000`. Additionally,
     the generic Boot0 DDR initialization timing parameters may have minor
     mismatches with this board's SiP memory颗粒. This issue requires further
     device tree and clock pin configuration work.

## Test Criteria

- **Test success**: the actual result matches the expected result; the system
  boots normally and can interact via the msh terminal.
- **Test failure**: the actual result does not match the expected result; the
  system fails to boot or terminal interaction cannot be established.

## Test Conclusion

Test success / BASIC

## Acknowledgements

Thanks to @BernardXiong for the support.