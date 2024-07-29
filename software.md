## 流行 Linux 发行版 for RISC-V 的应用支持情况

| 软件名   | 软件分类   | Arch Linux | Debian/RevyOS | Fedora | FreeBSD | Gentoo | openAnolis | OpenBSD | openCloudOS | openEuler | openKylin | openSUSE | Ubuntu | Tina-Linux | Android 13 | Armbian | BuildRoot | OpenHarmony | FreeRTOS | RT-Thread | Zephyr | OpenWRT | ThreadX | NuttX | Melis |
| -------- | ---------- | ---------- | ------------- | ------ | ------- | ------ | ---------- | ------- | ----------- | --------- | --------- | -------- | ------ | ---------- | ---------- | ------- | --------- | ----------- | -------- | --------- | ------ | ------- | ------- | ----- | ----- |
|          | 系统版本   |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| kernel   |            |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| glibc    |            |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| gcc      | Toolchain  |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| gdb      | Toolchain  |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| binutils | Toolchain  |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| cmake    | Toolchain  |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| clang    | Toolchain  |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| llvm     | Toolchain  |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| lldb     | Toolchain  |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| openJDK  | Java       |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| python   | Python     |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| Nodejs   | JavaScript |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| chromium | JavaScript |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| firefox  | JavaScript |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| rust     | RUST       |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| ocaml    | SAIL       |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| dart？   |            |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| vscode   |            |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| eclipse  |            |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
|          |            |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| Mono     |            |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| numpy？  |            |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |
| Pandas   |            |            |               |        |         |        |            |         |             |           |           |          |        |            |            |         |           |             |          |           |        |         |         |       |       |



说明：
关于软件包列表：

1. 基于当前RISC-V硬件的性能，更多的是作为运行环境，因此C、C++、Fortran、Java、Python、JavaScript、Rust、Dart、Chisel、SAIL 相关的运行环境所需的软件是ruyisdk所需要了解的。
2. ruyisdk定义了开发环境支持RISC-V，因此OS for RISC-V作为开发环境，对IDE等开发工具的支持情况也是一个需要了解的点，目前可能受限于硬件性能，可仅在部分高性能设备上验证。
3. 软件的调研列表包含不限于甲辰计划、RISC-V软件测试任务的一些指定软件包，如Mono、numpy等；
4. 上述软件包列表欢迎补充，有不合适的也可以修改/删除。

关于表格的填写：

1. OS的版本与软件包的版本是重要信息，需要在表格中进行体现。
2. 软件的支持程度/支持情况，大致的分类：
   - OS发行版软件仓库支持/第三方软件源支持 ：没有支持的向OS社区反馈需求；
   - 安装成功(包含其所需的依赖)/不成功-依赖缺失/不成功-软件bug：不成功的向OS发行版社区反馈问题；
   - 使用情况：具体软件具体分析，按需测试，发现问题则分情况向OS社区、或者软件upstream反馈问题；
3. 参考资料：https://github.com/isrc-cas/tarsier-meta/blob/main/report/info.md
