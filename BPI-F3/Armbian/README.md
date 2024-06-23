# Armbian Banana Pi BPI-F3 Test Report

## Test Environment

### System Information

- Download Links:
  - Baidu Netdisk: https://pan.baidu.com/s/1VIp3bwbDjMairyXXMZwNkQ?pwd=8888
  - Google Drive: https://drive.google.com/drive/folders/1Y5iKY55hFEO2z0sEeG_KC5EInD6nVDft?usp=sharing
- Reference Installation Document: https://docs.banana-pi.org/en/BPI-F3/GettingStarted_BPI-F3

### Hardware Information

- Banana Pi BPI-F3
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing the Image (SD Card)

After downloading and extracting the image, use `dd` to flash the image to the microSD card.

```bash
xz -kd Armbian-bpi-SpacemiT_24.5.0-trunk_Bananapif3_noble_legacy_6.1.15_xfce_desktop.img.xz
sudo dd if=/path/to/Armbian-bpi-SpacemiT_24.5.0-trunk_Bananapif3_noble_legacy_6.1.15_xfce_desktop.img of=/dev/your-device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

On the first boot, create a user.

## Expected Results

The system should boot up normally and allow login through the onboard serial port.

## Actual Results

The system booted successfully and login through the onboard serial port was also successful.

### Boot Log

Screen recording (From flashing image to system login):
[![asciicast](https://asciinema.org/a/aoWgw2BtCDRHOpxG4eYsWRPKZ.svg)](https://asciinema.org/a/aoWgw2BtCDRHOpxG4eYsWRPKZ)

```log
Welcome to Armbian-bpi-SpacemiT! 

Documentation: https://docs.armbian.com/ | Community support: https://community.armbian.com/

IP address: 

Create root password: 
Repeat root password: 

Warning: Weak password, it is WAY too short!

Support status: community support (unsupported userspace)

Choose default system command shell:

1) bash
2) zsh


Choose default system command shell:

1) bash
2) zsh
1

Shell: BASH

Creating a new user account. Press <Ctrl-C> to abort

Desktop environment will not be enabled if you abort the new user creation

Please provide a username (eg. your first name): 
Error: illegal characters in username

Creating a new user account. Press <Ctrl-C> to abort

Desktop environment will not be enabled if you abort the new user creation

Please provide a username (eg. your first name): plct
Create user (plct) password: ****
Repeat user (plct) password: ****

Warning: Weak password, it is too short!

Please provide your real name: Plct

Dear Plct, your account plct has been created and is sudo enabled.
Please use this account for your daily work from now on.

Detected timezone: 

Set user language based on your location? [Y/n] y
y

At your location, more locales are possible:

  1) aa_DJ.UTF-8              168) is_IS.UTF-8
  2) aa_ER                    169) it_CH.UTF-8
  3) aa_ER@saaho              170) it_IT.UTF-8
  4) aa_ER@saaho              171) iu_CA
  5) aa_ET                    172) ja_JP.UTF-8
  6) af_ZA.UTF-8              173) kab_DZ
  7) agr_PE                   174) ka_GE.UTF-8
  8) ak_GH                    175) kk_KZ.UTF-8
  9) am_ET                    176) kl_GL.UTF-8
 10) an_ES.UTF-8              177) km_KH
 11) anp_IN                   178) kn_IN
 12) ar_AE.UTF-8              179) kok_IN
 13) ar_BH.UTF-8              180) ko_KR.UTF-8
 14) ar_DZ.UTF-8              181) ko_KR.UTF-8
 15) ar_EG.UTF-8              182) ks_IN
 16) ar_IN                    183) ks_IN@devanagari
 17) ar_IQ.UTF-8              184) ks_IN@devanagari
 18) ar_JO.UTF-8              185) ku_TR.UTF-8
 19) ar_KW.UTF-8              186) kw_GB.UTF-8
 20) ar_LB.UTF-8              187) ky_KG
 21) ar_LY.UTF-8              188) lb_LU
 22) ar_MA.UTF-8              189) lg_UG.UTF-8
 23) ar_OM.UTF-8              190) li_BE
 24) ar_QA.UTF-8              191) lij_IT
 25) ar_SA.UTF-8              192) li_NL
 26) ar_SD.UTF-8              193) ln_CD
 27) ar_SS                    194) lo_LA
 28) ar_SY.UTF-8              195) lt_LT.UTF-8
 29) ar_TN.UTF-8              196) lv_LV.UTF-8
 30) ar_YE.UTF-8              197) lzh_TW
 31) as_IN                    198) mag_IN
 32) ast_ES.UTF-8             199) mai_IN
 33) ayc_PE                   200) mai_NP
 34) az_AZ                    201) mfe_MU
 35) az_IR                    202) mg_MG.UTF-8
 36) be_BY.UTF-8              203) mhr_RU
 37) be_BY@latin              204) mi_NZ.UTF-8
 38) be_BY@latin              205) miq_NI
 39) bem_ZM                   206) mjw_IN
 40) ber_DZ                   207) mk_MK.UTF-8
 41) ber_MA                   208) ml_IN
 42) bg_BG.UTF-8              209) mni_IN
 43) bhb_IN.UTF-8             210) mn_MN
 44) bho_IN                   211) mnw_MM
 45) bho_NP                   212) mr_IN
 46) bi_VU                    213) ms_MY.UTF-8
 47) bn_BD                    214) mt_MT.UTF-8
 48) bn_IN                    215) my_MM
 49) bo_CN                    216) nan_TW
 50) bo_IN                    217) nan_TW@latin
 51) br_FR.UTF-8              218) nan_TW@latin
 52) brx_IN                   219) nb_NO.UTF-8
 53) bs_BA.UTF-8              220) nds_DE
 54) byn_ER                   221) nds_NL
 55) ca_AD.UTF-8              222) ne_NP
 56) ca_ES.UTF-8              223) nhn_MX
 57) ca_ES@valencia           224) niu_NU
 58) ca_ES@valencia           225) niu_NZ
 59) ca_FR.UTF-8              226) nl_AW
 60) ca_IT.UTF-8              227) nl_BE.UTF-8
 61) ce_RU                    228) nl_NL.UTF-8
 62) chr_US                   229) nn_NO.UTF-8
 63) ckb_IQ                   230) nr_ZA
 64) cmn_TW                   231) nso_ZA
 65) crh_UA                   232) oc_FR.UTF-8
 66) csb_PL                   233) om_ET
 67) cs_CZ.UTF-8              234) om_KE.UTF-8
 68) cv_RU                    235) or_IN
 69) cy_GB.UTF-8              236) os_RU
 70) da_DK.UTF-8              237) pa_IN
 71) de_AT.UTF-8              238) pap_AW
 72) de_BE.UTF-8              239) pap_CW
 73) de_CH.UTF-8              240) pa_PK
 74) de_DE.UTF-8              241) pl_PL.UTF-8
 75) de_IT.UTF-8              242) ps_AF
 76) de_LI.UTF-8              243) pt_BR.UTF-8
 77) de_LU.UTF-8              244) pt_PT.UTF-8
 78) doi_IN                   245) quz_PE
 79) dsb_DE                   246) raj_IN
 80) dv_MV                    247) rif_MA
 81) dz_BT                    248) ro_RO.UTF-8
 82) el_CY.UTF-8              249) ru_RU.UTF-8
 83) el_GR.UTF-8              250) ru_UA.UTF-8
 84) en_AG                    251) rw_RW
 85) en_AU.UTF-8              252) sah_RU
 86) en_BW.UTF-8              253) sa_IN
 87) en_CA.UTF-8              254) sat_IN
 88) en_DK.UTF-8              255) sc_IT
 89) en_GB.UTF-8              256) sd_IN
 90) en_HK.UTF-8              257) sd_IN@devanagari
 91) en_IE.UTF-8              258) sd_IN@devanagari
 92) en_IL                    259) sd_PK
 93) en_IN                    260) se_NO
 94) en_NG                    261) sgs_LT
 95) en_NZ.UTF-8              262) shn_MM
 96) en_PH.UTF-8              263) shs_CA
 97) en_SC.UTF-8              264) sid_ET
 98) en_SG.UTF-8              265) si_LK
 99) en_US.UTF-8              266) sk_SK.UTF-8
100) en_ZA.UTF-8              267) sl_SI.UTF-8
101) en_ZM                    268) sm_WS
102) en_ZW.UTF-8              269) so_DJ.UTF-8
103) eo_US.UTF-8              270) so_ET
104) es_AR.UTF-8              271) so_KE.UTF-8
105) es_BO.UTF-8              272) so_SO.UTF-8
106) es_CL.UTF-8              273) sq_AL.UTF-8
107) es_CO.UTF-8              274) sq_MK
108) es_CR.UTF-8              275) sr_ME
109) es_CU                    276) sr_RS
110) es_DO.UTF-8              277) sr_RS@latin
111) es_EC.UTF-8              278) sr_RS@latin
112) es_ES.UTF-8              279) ss_ZA
113) es_GT.UTF-8              280) st_ZA.UTF-8
114) es_HN.UTF-8              281) sv_FI.UTF-8
115) es_MX.UTF-8              282) sv_SE.UTF-8
116) es_NI.UTF-8              283) sw_KE
117) es_PA.UTF-8              284) sw_TZ
118) es_PE.UTF-8              285) szl_PL
119) es_PR.UTF-8              286) ta_IN
120) es_PY.UTF-8              287) ta_LK
121) es_SV.UTF-8              288) tcy_IN.UTF-8
122) es_US.UTF-8              289) te_IN
123) es_UY.UTF-8              290) tg_TJ.UTF-8
124) es_VE.UTF-8              291) the_NP
125) et_EE.UTF-8              292) th_TH.UTF-8
126) et_EE.UTF-8              293) ti_ER
127) eu_ES.UTF-8              294) ti_ET
128) eu_FR.UTF-8              295) tig_ER
129) fa_IR                    296) tk_TM
130) ff_SN                    297) tl_PH.UTF-8
131) fi_FI.UTF-8              298) tn_ZA
132) fil_PH                   299) to_TO
133) fo_FO.UTF-8              300) tpi_PG
134) fr_BE.UTF-8              301) tr_CY.UTF-8
135) fr_CA.UTF-8              302) tr_TR.UTF-8
136) fr_CH.UTF-8              303) ts_ZA
137) fr_FR.UTF-8              304) tt_RU
138) fr_LU.UTF-8              305) tt_RU@iqtelif
139) fur_IT                   306) tt_RU@iqtelif
140) fy_DE                    307) ug_CN
141) fy_NL                    308) ug_CN@latin
142) ga_IE.UTF-8              309) ug_CN@latin
143) gd_GB.UTF-8              310) uk_UA.UTF-8
144) gez_ER                   311) unm_US
145) gez_ER@abegede           312) ur_IN
146) gez_ER@abegede           313) ur_PK
147) gez_ET                   314) uz_UZ.UTF-8
148) gez_ET@abegede           315) uz_UZ@cyrillic
149) gez_ET@abegede           316) uz_UZ@cyrillic
150) gl_ES.UTF-8              317) ve_ZA
151) gu_IN                    318) vi_VN
152) gv_GB.UTF-8              319) wa_BE.UTF-8
153) hak_TW                   320) wae_CH
154) ha_NG                    321) wal_ET
155) he_IL.UTF-8              322) wo_SN
156) hif_FJ                   323) xh_ZA.UTF-8
157) hi_IN                    324) yi_US.UTF-8
158) hne_IN                   325) yo_NG
159) hr_HR.UTF-8              326) yue_HK
160) hsb_DE.UTF-8             327) yuw_PG
161) ht_HT                    328) zh_CN.UTF-8
162) hu_HU.UTF-8              329) zh_HK.UTF-8
163) hy_AM                    330) zh_SG.UTF-8
164) ia_FR                    331) lzh_TW
165) id_ID.UTF-8              332) zh_TW.UTF-8
166) ig_NG                    333) zu_ZA.UTF-8
167) ik_CA                    334) Skip generating locales
Please enter your choice:328
Please identify a location so that time zone rules can be set correctly.
Please select a continent, ocean, "coord", or "TZ".
 1) Africa
 2) Americas
 3) Antarctica
 4) Asia
 5) Atlantic Ocean
 6) Australia
 7) Europe
 8) Indian Ocean
 9) Pacific Ocean
10) coord - I want to use geographical coordinates.
11) TZ - I want to specify the timezone using the Posix TZ format.
#? 4
Please select a country or a region whose clocks agree with yours.
 1) Afghanistan              29) Kyrgyzstan
 2) Antarctica               30) Laos
 3) Armenia                  31) Lebanon
 4) Azerbaijan               32) Macau
 5) Bahrain                  33) Malaysia
 6) Bangladesh               34) Mongolia
 7) Bhutan                   35) Myanmar (Burma)
 8) Brunei                   36) Nepal
 9) Cambodia                 37) Oman
10) China                    38) Pakistan
11) Christmas Island         39) Palestine
12) Cocos (Keeling) Islands  40) Philippines
13) Cyprus                   41) Qatar
14) East Timor               42) Réunion
15) French S. Terr.          43) Russia
16) Georgia                  44) Saudi Arabia
17) Hong Kong                45) Seychelles
18) India                    46) Singapore
19) Indonesia                47) Sri Lanka
20) Iran                     48) Syria
21) Iraq                     49) Taiwan
22) Israel                   50) Tajikistan
23) Japan                    51) Thailand
24) Jordan                   52) Turkmenistan
25) Kazakhstan               53) United Arab Emirates
26) Korea (North)            54) Uzbekistan
27) Korea (South)            55) Vietnam
28) Kuwait                   56) Yemen
#? 10
Please select one of the following timezones.
1) Beijing Time
2) Xinjiang Time
#? 1

The following information has been given:

        China
        Beijing Time

Therefore TZ='Asia/Shanghai' will be used.
Selected time is now:   Wed May  1 23:18:08 CST 2024.
Universal Time is now:  Wed May  1 15:18:08 UTC 2024.
Is the above information OK?
1) Yes
2) No
#? 1

Generating locales: zh_CN.UTF-8

Now starting desktop environment...

root@bananapif3:~# uname -a
Linux bananapif3 6.1.15-legacy-k1 #2 SMP PREEMPT Wed May  1 14:17:59 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux
root@bananapif3:~# cat /etc/os-release 
PRETTY_NAME="Armbian-bpi-SpacemiT 24.5.0-trunk mantic"
NAME="Ubuntu"
VERSION_ID="23.10"
VERSION="23.10 (Mantic Minotaur)"
VERSION_CODENAME=mantic
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://github.com/armbian/build"
SUPPORT_URL="https://community.armbian.com/"
BUG_REPORT_URL="https://github.com/armbian/community/issues"
PRIVACY_POLICY_URL="https://duckduckgo.com/"
UBUNTU_CODENAME=mantic
LOGO="armbian-logo"
ARMBIAN_PRETTY_NAME="Armbian-bpi-SpacemiT 24.5.0-trunk mantic"
root@bananapif3:~# 
 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
