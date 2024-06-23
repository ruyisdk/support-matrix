# Armbian VisionFive 测试报告

## 测试环境

### 系统信息

- 系统版本：openKylin 0.9.5
- 下载链接：[https://www.armbian.com/vision-five/](https://www.armbian.com/vision-five/)
- 参考安装文档：[https://docs.armbian.com/User-Guide_Getting-Started/](https://docs.armbian.com/User-Guide_Getting-Started/)

### 硬件信息

- StarFive VisionFive
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `unxz` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
unxz /path/to/Armbian_community.img.xz
sudo dd if=/path/to/Armbian_community.img of=/dev/your-device bs=1M status=progress
```

### 更新/引导 boot


若 u-boot 无法引导而是进入了命令行，需要更新 u-boot（详见：（pr 31）[https://github.com/starfive-tech/u-boot/pull/31]）：

官方文档：[https://starfivetech.com/uploads/VisionFive%20Single%20Board%20Computer%20Quick%20Start%20Guide.pdf](https://starfivetech.com/uploads/VisionFive%20Single%20Board%20Computer%20Quick%20Start%20Guide.pdf)

u-boot 下载：https://github.com/starfive-tech/Fedora_on_StarFive/releases

或者，手动输入以下命令以引导系统：

```u-boot
ext4load mmc 0:1 0x84000000 /boot/Image
ext4load mmc 0:1 0x88000000 /boot/dtb/starfive/jh7100-starfive-visionfive-v1.dtb
setenv bootargs "root=/dev/mmcblk0p1 console=ttyS0,115200n8 console=tty0 earlycon=sbi rootflags=data=writeback stmmaceth=chain_mode:1 rw rw no_console_suspend consoleblank=0 fsck.fix=yes fsck.repair=yes net.ifnames=0 splash plymouth.ignore-serial-consoles"
booti 0x84000000 - 0x88000000
```

### 登录系统

通过串口登录系统。

首次登录需要强制设置账户和密码。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。
### 启动信息

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/EJJCRPhcPoMqp4OlMjUD9eOej.svg)](https://asciinema.org/a/EJJCRPhcPoMqp4OlMjUD9eOej)

```log
Welcome to Armbian_community! 

Documentation: https://docs.armbian.com | Community support: https://community.armbian.com/

IP address: 

Create root password: IP address: 

Create root password: *********
Repeat root password: 
Armbian_community 24.5.0-trunk.278 Noble hvc0 

visionfive login: ****
Rejected - passwords do not match. Try again [3].
Create root password: **********
Repeat root password: **********

WARNING!

You are using an automated build meant only for developers to provide
constructive feedback to improve build system, OS settings or UX.

If this does not apply to you, STOP NOW!  Especially don't use this 
image for production since things might not work as expected or at 
all. They may  break anytime with next update.

Shell: BASH

Creating a new user account. Press <Ctrl-C> to abort

Please provide a username (eg. your first name): armbian
Create user (armbian) password: **********
Repeat user (armbian) password: **********

Please provide your real name: Armbian

Dear Armbian, your account armbian has been created and is sudo enabled.
Please use this account for your daily work from now on.

Internet connection was not detected.

Connect via wireless? [Y/n] n
n

Detected timezone: 

Set user language based on your location? [Y/n] n
n

At your location, more locales are possible:

  1) aa_DJ.UTF-8              170) it_IT.UTF-8
  2) aa_ER                    171) iu_CA
  3) aa_ET                    172) ja_JP.UTF-8
  4) af_ZA.UTF-8              173) kab_DZ
  5) agr_PE                   174) ka_GE.UTF-8
  6) ak_GH                    175) kk_KZ.UTF-8
  7) am_ET                    176) kl_GL.UTF-8
  8) an_ES.UTF-8              177) km_KH
  9) anp_IN                   178) kn_IN
 10) ar_AE.UTF-8              179) kok_IN
 11) ar_BH.UTF-8              180) ko_KR.UTF-8
 12) ar_DZ.UTF-8              181) ko_KR.UTF-8
 13) ar_EG.UTF-8              182) ks_IN
 14) ar_IN                    183) ks_IN@devanagari
 15) ar_IQ.UTF-8              184) ks_IN@devanagari
 16) ar_JO.UTF-8              185) ku_TR.UTF-8
 17) ar_KW.UTF-8              186) kv_RU
 18) ar_LB.UTF-8              187) kw_GB.UTF-8
 19) ar_LY.UTF-8              188) ky_KG
 20) ar_MA.UTF-8              189) lb_LU
 21) ar_OM.UTF-8              190) lg_UG.UTF-8
 22) ar_QA.UTF-8              191) li_BE
 23) ar_SA.UTF-8              192) lij_IT
 24) ar_SD.UTF-8              193) li_NL
 25) ar_SS                    194) ln_CD
 26) ar_SY.UTF-8              195) lo_LA
 27) ar_TN.UTF-8              196) lt_LT.UTF-8
 28) ar_YE.UTF-8              197) lv_LV.UTF-8
 29) as_IN                    198) lzh_TW
 30) ast_ES.UTF-8             199) mag_IN
 31) ayc_PE                   200) mai_IN
 32) az_AZ                    201) mai_NP
 33) az_IR                    202) mfe_MU
 34) be_BY.UTF-8              203) mg_MG.UTF-8
 35) be_BY@latin              204) mhr_RU
 36) be_BY@latin              205) mi_NZ.UTF-8
 37) bem_ZM                   206) miq_NI
 38) ber_DZ                   207) mjw_IN
 39) ber_MA                   208) mk_MK.UTF-8
 40) bg_BG.UTF-8              209) ml_IN
 41) bhb_IN.UTF-8             210) mni_IN
 42) bho_IN                   211) mn_MN
 43) bho_NP                   212) mnw_MM
 44) bi_VU                    213) mr_IN
 45) bn_BD                    214) ms_MY.UTF-8
 46) bn_IN                    215) mt_MT.UTF-8
 47) bo_CN                    216) my_MM
 48) bo_IN                    217) nan_TW
 49) br_FR.UTF-8              218) nan_TW@latin
 50) brx_IN                   219) nan_TW@latin
 51) bs_BA.UTF-8              220) nb_NO.UTF-8
 52) byn_ER                   221) nds_DE
 53) ca_AD.UTF-8              222) nds_NL
 54) ca_ES.UTF-8              223) ne_NP
 55) ca_ES@valencia           224) nhn_MX
 56) ca_ES@valencia           225) niu_NU
 57) ca_FR.UTF-8              226) niu_NZ
 58) ca_IT.UTF-8              227) nl_AW
 59) ce_RU                    228) nl_BE.UTF-8
 60) chr_US                   229) nl_NL.UTF-8
 61) ckb_IQ                   230) nn_NO.UTF-8
 62) cmn_TW                   231) nr_ZA
 63) crh_RU                   232) nso_ZA
 64) crh_UA                   233) oc_FR.UTF-8
 65) csb_PL                   234) om_ET
 66) cs_CZ.UTF-8              235) om_KE.UTF-8
 67) cv_RU                    236) or_IN
 68) cy_GB.UTF-8              237) os_RU
 69) da_DK.UTF-8              238) pa_IN
 70) de_AT.UTF-8              239) pap_AW
 71) de_BE.UTF-8              240) pap_CW
 72) de_CH.UTF-8              241) pa_PK
 73) de_DE.UTF-8              242) pl_PL.UTF-8
 74) de_IT.UTF-8              243) ps_AF
 75) de_LI.UTF-8              244) pt_BR.UTF-8
 76) de_LU.UTF-8              245) pt_PT.UTF-8
 77) doi_IN                   246) quz_PE
 78) dsb_DE                   247) raj_IN
 79) dv_MV                    248) rif_MA
 80) dz_BT                    249) ro_RO.UTF-8
 81) el_CY.UTF-8              250) ru_RU.UTF-8
 82) el_GR.UTF-8              251) ru_UA.UTF-8
 83) en_AG                    252) rw_RW
 84) en_AU.UTF-8              253) sah_RU
 85) en_BW.UTF-8              254) sa_IN
 86) en_CA.UTF-8              255) sat_IN
 87) en_DK.UTF-8              256) sc_IT
 88) en_GB.UTF-8              257) sd_IN
 89) en_HK.UTF-8              258) sd_IN@devanagari
 90) en_IE.UTF-8              259) sd_IN@devanagari
 91) en_IL                    260) sd_PK
 92) en_IN                    261) se_NO
 93) en_NG                    262) sgs_LT
 94) en_NZ.UTF-8              263) shn_MM
 95) en_PH.UTF-8              264) shs_CA
 96) en_SC.UTF-8              265) sid_ET
 97) en_SG.UTF-8              266) si_LK
 98) en_US.UTF-8              267) sk_SK.UTF-8
 99) en_ZA.UTF-8              268) sl_SI.UTF-8
100) en_ZM                    269) sm_WS
101) en_ZW.UTF-8              270) so_DJ.UTF-8
102) eo_US.UTF-8              271) so_ET
103) es_AR.UTF-8              272) so_KE.UTF-8
104) es_BO.UTF-8              273) so_SO.UTF-8
105) es_CL.UTF-8              274) sq_AL.UTF-8
106) es_CO.UTF-8              275) sq_MK
107) es_CR.UTF-8              276) sr_ME
108) es_CU                    277) sr_RS
109) es_DO.UTF-8              278) sr_RS@latin
110) es_EC.UTF-8              279) sr_RS@latin
111) es_ES.UTF-8              280) ssy_ER
112) es_GT.UTF-8              281) ss_ZA
113) es_HN.UTF-8              282) st_ZA.UTF-8
114) es_MX.UTF-8              283) su_ID
115) es_NI.UTF-8              284) sv_FI.UTF-8
116) es_PA.UTF-8              285) sv_SE.UTF-8
117) es_PE.UTF-8              286) sw_KE
118) es_PR.UTF-8              287) sw_TZ
119) es_PY.UTF-8              288) szl_PL
120) es_SV.UTF-8              289) ta_IN
121) es_US.UTF-8              290) ta_LK
122) es_UY.UTF-8              291) tcy_IN.UTF-8
123) es_VE.UTF-8              292) te_IN
124) et_EE.UTF-8              293) tg_TJ.UTF-8
125) et_EE.UTF-8              294) the_NP
126) eu_ES.UTF-8              295) th_TH.UTF-8
127) eu_FR.UTF-8              296) ti_ER
128) fa_IR                    297) ti_ET
129) ff_SN                    298) tig_ER
130) fi_FI.UTF-8              299) tk_TM
131) fil_PH                   300) tl_PH.UTF-8
132) fo_FO.UTF-8              301) tn_ZA
133) fr_BE.UTF-8              302) to_TO
134) fr_CA.UTF-8              303) tpi_PG
135) fr_CH.UTF-8              304) tr_CY.UTF-8
136) fr_FR.UTF-8              305) tr_TR.UTF-8
137) fr_LU.UTF-8              306) ts_ZA
138) fur_IT                   307) tt_RU
139) fy_DE                    308) tt_RU@iqtelif
140) fy_NL                    309) tt_RU@iqtelif
141) ga_IE.UTF-8              310) ug_CN
142) gbm_IN                   311) ug_CN@latin
143) gd_GB.UTF-8              312) ug_CN@latin
144) gez_ER                   313) uk_UA.UTF-8
145) gez_ER@abegede           314) unm_US
146) gez_ER@abegede           315) ur_IN
147) gez_ET                   316) ur_PK
148) gez_ET@abegede           317) uz_UZ.UTF-8
149) gez_ET@abegede           318) uz_UZ@cyrillic
150) gl_ES.UTF-8              319) uz_UZ@cyrillic
151) gu_IN                    320) ve_ZA
152) gv_GB.UTF-8              321) vi_VN
153) hak_TW                   322) wa_BE.UTF-8
154) ha_NG                    323) wae_CH
155) he_IL.UTF-8              324) wal_ET
156) hif_FJ                   325) wo_SN
157) hi_IN                    326) xh_ZA.UTF-8
158) hne_IN                   327) yi_US.UTF-8
159) hr_HR.UTF-8              328) yo_NG
160) hsb_DE.UTF-8             329) yue_HK
161) ht_HT                    330) yuw_PG
162) hu_HU.UTF-8              331) zgh_MA
163) hy_AM                    332) zh_CN.UTF-8
164) ia_FR                    333) zh_HK.UTF-8
165) id_ID.UTF-8              334) zh_SG.UTF-8
166) ig_NG                    335) lzh_TW
167) ik_CA                    336) zh_TW.UTF-8
168) is_IS.UTF-8              337) zu_ZA.UTF-8
169) it_CH.UTF-8              338) Skip generating locales
Please enter your choice:338
root@visionfive:~# uname -a
Linux visionfive 6.1.82-edge-starfive #2 SMP Fri Mar 15 18:27:50 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux
root@visionfive:~# cat /etc/os-release 
PRETTY_NAME="Armbian_community 24.5.0-trunk.278 noble"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04 (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://github.com/armbian/build"
SUPPORT_URL="https://community.armbian.com/"
BUG_REPORT_URL="https://github.com/armbian/community/issues"
PRIVACY_POLICY_URL="https://duckduckgo.com/"
UBUNTU_CODENAME=noble
LOGO="armbian-logo"
ARMBIAN_PRETTY_NAME="Armbian_community 24.5.0-trunk.278 noble"
root@visionfive:~# 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试部分成功。