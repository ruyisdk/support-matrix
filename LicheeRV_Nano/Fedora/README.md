---
sys: fedora
sys_ver: 41
sys_var: null

status: basic
last_update: 2024-12-14
---

# Fedora 41 LicheeRV Nano Test Report

## Test Environment

### Operating System Information

- System Version: Fedora 41
- Download Link: https://mirror.iscas.ac.cn/fedora-riscv/dl/Sipeed/LicheeRV_Nano/images/latest/LicheeRV_Nano-fedora-minimal.img.gz
- Reference Installation Document: https://github.com/chainsx/fedora-riscv-builder

### Hardware Information

- LicheeRV Nano
- A USB-A to C or USB-C to C cable
- A microSD card
- A microSD card reader
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Download image

```shell
wget https://mirror.iscas.ac.cn/fedora-riscv/dl/Sipeed/LicheeRV_Nano/images/latest/LicheeRV_Nano-fedora-minimal.img.gz
gzip -d LicheeRV_Nano-fedora-minimal.img.gz
```

### Flash the image to microSD card via `dd`

```shell
sudo dd if=LicheeRV_Nano-fedora-minimal.img of=/dev/your/device bs=4M status=progress
```

### Logging into the System

Log into the system via the serial port.

Username: `root`
Password: `riscv`

## Expected Results

The system should boot normally and allow login via the serial port.

## Actual Results

The system boots up normally and login through the serial port is successful.

> Note: In the event of broken `dnf` that yields `Illegal instruction`, consider replacing `/boot/fip.bin` with the one from [here](https://github.com/Pairman/LicheeRV-Nano-Build/releases/download/20250408/fip.bin); See https://github.com/ruyisdk/support-matrix/issues/215

### Boot Log

```log
Welcome to Fedora Linux 41 (Rawhide Prerelease)!

[  OK  ] Created slice system-getty.slice - Slice /system/getty.
[  OK  ] Created slice system-modprobe.slice - Slice /system/modprobe.
[  OK  ] Created slice system-serial\x2dget…slice - Slice /system/serial-getty.
[  OK  ] Created slice system-sshd\x2dkeygen.slice - Slice /system/sshd-keygen.
[  OK  ] Created slice system-systemd\x2dzr…- Slice /system/systemd-zram-setup.
[  OK  ] Created slice user.slice - User and Session Slice.
[  OK  ] Started systemd-ask-password-wall.…d Requests to Wall Directory Watch.
         Expecting device dev-disk-by\x2duu…ce - /dev/disk/by-uuid/84D7-9B43...
         Expecting device dev-ttyS0.device - /dev/ttyS0...
         Expecting device dev-zram0.device - /dev/zram0...
[  OK  ] Reached target integritysetup.targ… Local Integrity Protected Volumes.
[  OK  ] Reached target remote-cryptsetup.target - Remote Encrypted Volumes.
[  OK  ] Reached target remote-fs.target - Remote File Systems.
[  OK  ] Reached target slices.target - Slice Units.
[  OK  ] Reached target veritysetup.target - Local Verity Protected Volumes.
[  OK  ] Listening on systemd-coredump.socket - Process Core Dump Socket.
[  OK  ] Listening on systemd-creds.socket - Credential Encryption/Decryption.
[  OK  ] Listening on systemd-initctl.socke…- initctl Compatibility Named Pipe.
[  OK  ] Listening on systemd-journald-audit.socket - Journal Audit Socket.
[  OK  ] Listening on systemd-journald-dev-…socket - Journal Socket (/dev/log).
[  OK  ] Listening on systemd-journald.socket - Journal Sockets.
[  OK  ] Listening on systemd-mountfsd.socket - DDI File System Mounter Socket.
[  OK  ] Listening on systemd-nsresourced.s… Namespace Resource Manager Socket.
[  OK  ] Listening on systemd-udevd-control.socket - udev Control Socket.
[  OK  ] Listening on systemd-udevd-kernel.socket - udev Kernel Socket.
[  OK  ] Listening on systemd-userdbd.socket - User Database Manager Socket.
         Mounting dev-mqueue.mount - POSIX Message Queue File System...
         Mounting sys-kernel-debug.mount - Kernel Debug File System...
         Starting modprobe@configfs.service - Load Kernel Module configfs...
         Starting modprobe@dm_mod.service - Load Kernel Module dm_mod...
         Starting modprobe@drm.service - Load Kernel Module drm...
         Starting modprobe@efi_pstore.servi… - Load Kernel Module efi_pstore...
         Starting modprobe@fuse.service - Load Kernel Module fuse...
         Starting modprobe@loop.service - Load Kernel Module loop...
         Starting systemd-journald.service - Journal Service...
         Starting systemd-network-generator…k units from Kernel command line...
         Starting systemd-remount-fs.servic…unt Root and Kernel File Systems...
         Starting systemd-sysctl.service - Apply Kernel Variables...
         Starting systemd-tmpfiles-setup-de… Device Nodes in /dev gracefully...
         Starting systemd-udev-load-credent…Load udev Rules from Credentials...
         Starting systemd-udev-trigger.service - Coldplug All udev Devices...
         Starting systemd-vconsole-setup.service - Virtual Console Setup...
[  OK  ] Mounted dev-mqueue.mount - POSIX Message Queue File System.
[  OK  ] Mounted sys-kernel-debug.mount - Kernel Debug File System.
[  OK  ] Finished modprobe@configfs.service - Load Kernel Module configfs.
[  OK  ] Finished modprobe@dm_mod.service - Load Kernel Module dm_mod.
[  OK  ] Finished modprobe@drm.service - Load Kernel Module drm.
[  OK  ] Finished modprobe@efi_pstore.service - Load Kernel Module efi_pstore.
[  OK  ] Finished modprobe@fuse.service - Load Kernel Module fuse.
[  OK  ] Finished modprobe@loop.service - Load Kernel Module loop.
[  OK  ] Finished systemd-network-generator…ork units from Kernel command line.
[FAILED] Failed to start systemd-sysctl.service - Apply Kernel Variables.
See 'systemctl status systemd-sysctl.service' for details.
[  OK  ] Finished systemd-udev-load-credent…- Load udev Rules from Credentials.
[  OK  ] Finished systemd-remount-fs.servic…mount Root and Kernel File Systems.
         Starting systemd-nsresourced.service - Namespace Resource Manager...
         Starting systemd-random-seed.service - Load/Save OS Random Seed...
         Starting systemd-userdbd.service - User Database Manager...
         Mounting sys-kernel-config.mount - Kernel Configuration File System...
[  OK  ] Finished systemd-random-seed.service - Load/Save OS Random Seed.
[  OK  ] Mounted sys-kernel-config.mount - Kernel Configuration File System.
[  OK  ] Started systemd-journald.service - Journal Service.
         Starting systemd-journal-flush.ser…sh Journal to Persistent Storage...
[  OK  ] Started systemd-nsresourced.service - Namespace Resource Manager.
[  OK  ] Finished systemd-journal-flush.ser…lush Journal to Persistent Storage.
[  OK  ] Started systemd-userdbd.service - User Database Manager.
[  OK  ] Finished systemd-vconsole-setup.service - Virtual Console Setup.
[  OK  ] Finished systemd-tmpfiles-setup-de…ic Device Nodes in /dev gracefully.
         Starting systemd-tmpfiles-setup-de…eate Static Device Nodes in /dev...
[  OK  ] Finished systemd-tmpfiles-setup-de…Create Static Device Nodes in /dev.
[  OK  ] Reached target local-fs-pre.target…Preparation for Local File Systems.
         Starting systemd-udevd.service - R…ager for Device Events and Files...
[  OK  ] Finished systemd-udev-trigger.service - Coldplug All udev Devices.
[  OK  ] Started systemd-udevd.service - Ru…anager for Device Events and Files.
         Starting plymouth-start.service - Show Plymouth Boot Screen...
[  OK  ] Found device dev-ttyS0.device - /dev/ttyS0.
[  OK  ] Started plymouth-start.service - Show Plymouth Boot Screen.
[  OK  ] Found device dev-disk-by\x2duuid-8…vice - /dev/disk/by-uuid/84D7-9B43.
[  OK  ] Started systemd-ask-password-plymo…quests to Plymouth Directory Watch.
[  OK  ] Reached target cryptsetup.target - Local Encrypted Volumes.
[  OK  ] Reached target paths.target - Path Units.
[  OK  ] Reached target sound.target - Sound Card.
[  OK  ] Reached target usb-gadget.target - Hardware activated USB gadget.
[  OK  ] Listening on systemd-rfkill.socket…ll Switch Status /dev/rfkill Watch.
         Mounting boot.mount - /boot...
[  OK  ] Stopped systemd-vconsole-setup.service - Virtual Console Setup.
         Stopping systemd-vconsole-setup.service - Virtual Console Setup...
         Starting systemd-vconsole-setup.service - Virtual Console Setup...
[  OK  ] Mounted boot.mount - /boot.
[  OK  ] Finished systemd-vconsole-setup.service - Virtual Console Setup.
[ TIME ] Timed out waiting for device dev-zram0.device - /dev/zram0.
[DEPEND] Dependency failed for dev-zram0.swap - Compressed Swap on /dev/zram0.
[DEPEND] Dependency failed for systemd-zram…ervice - Create swap on /dev/zram0.
[  OK  ] Reached target swap.target - Swaps.
         Mounting tmp.mount - Temporary Directory /tmp...
[  OK  ] Mounted tmp.mount - Temporary Directory /tmp.
[  OK  ] Reached target local-fs.target - Local File Systems.
[  OK  ] Listening on systemd-bootctl.socket - Boot Entries Service Socket.
[  OK  ] Listening on systemd-sysext.socket… System Extension Image Management.
         Starting plymouth-read-write.servi…ymouth To Write Out Runtime Data...
         Starting systemd-tmpfiles-setup.se…e Volatile Files and Directories...
[  OK  ] Finished plymouth-read-write.servi…Plymouth To Write Out Runtime Data.
[  OK  ] Finished systemd-tmpfiles-setup.se…ate Volatile Files and Directories.
         Starting audit-rules.service - Load Audit Rules...
         Starting systemd-resolved.service - Network Name Resolution...
[  OK  ] Finished audit-rules.service - Load Audit Rules.
         Starting auditd.service - Security Audit Logging Service...
[  OK  ] Started auditd.service - Security Audit Logging Service.
         Starting systemd-update-utmp.servi…ord System Boot/Shutdown in UTMP...
[  OK  ] Finished systemd-update-utmp.servi…ecord System Boot/Shutdown in UTMP.
[  OK  ] Started systemd-resolved.service - Network Name Resolution.
[  OK  ] Reached target nss-lookup.target - Host and Network Name Lookups.
[  OK  ] Reached target sysinit.target - System Initialization.
[  OK  ] Started fstrim.timer - Discard unused filesystem blocks once a week.
[  OK  ] Started raid-check.timer - Weekly RAID setup health check.
[  OK  ] Started systemd-tmpfiles-clean.tim…y Cleanup of Temporary Directories.
[  OK  ] Started unbound-anchor.timer - dai…f the root trust anchor for DNSSEC.
[  OK  ] Reached target timers.target - Timer Units.
[  OK  ] Listening on avahi-daemon.socket -…DNS/DNS-SD Stack Activation Socket.
[  OK  ] Listening on dbus.socket - D-Bus System Message Bus Socket.
[  OK  ] Listening on pcscd.socket - PC/SC Smart Card Daemon Activation Socket.
[  OK  ] Listening on sshd-unix-local.socke…temd-ssh-generator, AF_UNIX Local).
[  OK  ] Listening on sssd-kcm.socket - SSS…ros Cache Manager responder socket.
[  OK  ] Listening on systemd-hostnamed.socket - Hostname Service Socket.
[  OK  ] Reached target sockets.target - Socket Units.
         Starting dbus-broker.service - D-Bus System Message Bus...
[  OK  ] Started dbus-broker.service - D-Bus System Message Bus.
[  OK  ] Reached target basic.target - Basic System.
         Starting avahi-daemon.service - Avahi mDNS/DNS-SD Stack...
         Starting chronyd.service - NTP client/server...
         Starting dracut-shutdown.service -…store /run/initramfs on shutdown...
         Starting firewalld.service - firewalld - dynamic firewall daemon...
[  OK  ] Reached target sshd-keygen.target.
[  OK  ] Reached target nss-user-lookup.target - User and Group Name Lookups.
         Starting systemd-homed.service - Home Area Manager...
         Starting systemd-logind.service - User Login Management...
[  OK  ] Finished dracut-shutdown.service - Restore /run/initramfs on shutdown.
[  OK  ] Started avahi-daemon.service - Avahi mDNS/DNS-SD Stack.
[  OK  ] Started systemd-homed.service - Home Area Manager.
[  OK  ] Finished systemd-homed-activate.service - Home Area Activation.
[  OK  ] Started chronyd.service - NTP client/server.
[  OK  ] Started systemd-logind.service - User Login Management.
[  OK  ] Started firewalld.service - firewalld - dynamic firewall daemon.
[  OK  ] Reached target network-pre.target - Preparation for Network.
         Starting NetworkManager.service - Network Manager...
         Expecting device dev-zram0.device - /dev/zram0...
         Starting systemd-hostnamed.service - Hostname Service...
[  OK  ] Started systemd-hostnamed.service - Hostname Service.
         Starting NetworkManager-dispatcher…anager Script Dispatcher Service...
[  OK  ] Started NetworkManager.service - Network Manager.
[  OK  ] Reached target network.target - Network.
         Starting sshd.service - OpenSSH server daemon...
         Starting systemd-user-sessions.service - Permit User Sessions...
[  OK  ] Started NetworkManager-dispatcher.… Manager Script Dispatcher Service.
[  OK  ] Finished systemd-user-sessions.service - Permit User Sessions.
         Starting plymouth-quit-wait.servic…d until boot process finishes up...
         Starting plymouth-quit.service - Terminate Plymouth Boot Screen...

Welcome to the Fedora RISC-V disk image
https://openkoji.iscas.ac.cn/koji/

Build date: Mon Jul  1 03:20:03 UTC 2024

Kernel 5.10.4-tag- on an riscv64 (ttyS0)

The root password is 'riscv'.
root password logins are disabled in SSH starting Fedora.

If DNS isn’t working, try editing ‘/etc/yum.repos.d/fedora-riscv.repo’.

For updates and latest information read:
https://fedoraproject.org/wiki/Architectures/RISC-V

Fedora RISC-V
-------------
fedora-riscv login: root
Password:
[root@fedora-riscv ~]# uname -a
Linux fedora-riscv 5.10.4-tag- #1 PREEMPT Tue Jul 9 20:03:10 CST 2024 riscv64 GNU/Linux
[root@fedora-riscv ~]# cat /etc/os-release
NAME="Fedora Linux"
VERSION="41 (Rawhide Prerelease)"
ID=fedora
VERSION_ID=41
VERSION_CODENAME=""
PLATFORM_ID="platform:f41"
PRETTY_NAME="Fedora Linux 41 (Rawhide Prerelease)"
ANSI_COLOR="0;38;2;60;110;180"
LOGO=fedora-logo-icon
CPE_NAME="cpe:/o:fedoraproject:fedora:41"
DEFAULT_HOSTNAME="fedora"
HOME_URL="https://fedoraproject.org/"
DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora/rawhide/system-administrators-guide/"
SUPPORT_URL="https://ask.fedoraproject.org/"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=rawhide
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=rawhide
SUPPORT_END=2025-05-13
[root@fedora-riscv ~]#

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
