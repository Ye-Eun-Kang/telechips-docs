# Linux YP4.0 IVI SDK-Getting Started

# 1 Introduction

This document describes Linux_YP4.0_IVI usage as follows:

- Board Description for TCC803x EVB

- Board Assembly Guide for TCC803x EVB

- Build Guide for Linux_YP4.0_IVI

- FWDN Guide for TCC803x in Linux_YP4.0_IVI

- Booting Guide for TCC803x EVB


# 2 Board Description

## 2.1 EVB Version


<div style="text-align: center;">
<strong>Table 2.1 EVB Version</strong>
</div>

| **Board**                                           | **Board Name/Version**                                       |
| :---------------------------------------------------: | :------------------------------------------------------------: |
| CPU Sub-board                                       | TCC8030_CPU_LPD4321_V1.2.2                                   |
| Main Board                                          | TCC803X_MAIN_V1.1.1                                          |
| 12.3” 1920x720 LCD                                  | TM_WLCD_12.3LVDS_SV0.2  TCC80XX_BOE_WLCD_12.3_SV1.1.1    TCCXXXX_AUO_WLCD_12.3_SV0.1.0 |
| Audio and Broadcasting and Radio tuner Board (ABRB) | TCC8XXX_AK4601_SILAB_ISDBT_DAB_SV1.0                         |
| Jog Navigation Sub-board                            | TCC80XX_KEY_SV0.1                                            |

:::note
<strong>Note:</strong> For more details, refer to the following document \[8\]:  
*TCC803x Common Hardware-Assembly Manual for EVB*
:::


:::important
<span style="color: blue;"><strong>Important:</strong> The default LCD setting of Linux_YP4.0_IVI SDK is fitted with "TCCXXXX_AUO_WLCD_12.3".\
To use a different LCD, modify the build configuration as described in Chapter 4.6.3.4.3.</span>
:::





### 2.1.1 CPU Sub-board

Figure 2.1 shows the top view of TCC803x CPU sub-board.

![Figure 2.1 CPU Sub-board](/803x/linux-yp4.0-getting-started/figure-2.1-cpu-sub-board.png)


​                               

Figure 2.1 CPU Sub-board (Top View)

 

Table 2.2 describes the TCC803x CPU sub-board (top view) connectors.

 

Table 2.2 Description of CPU Sub-board (Top View)

| **Number** | **Reference Number** | **Name**                            | **Description**                                              |
| :----------: | :--------------------: | :-----------------------------------: | ------------------------------------------------------------ |
| 1          | JR4                  | 26-pin LVDS Connector               | Connect to the LCD module for single-channel  LVDS signal    |
| 2          | JR2                  | 26-pin LVDS Connector               | Connect to the LCD module for dual-channel  LVDS signal      |
| 3          | JR1                  | 26-pin LVDS Connector               | Connect to the LCD module for dual-channel  LVDS signal      |
| 4          | JSW7,10              | Slide Switch                        | Select the path of bus switch                                |
| 5          | JSW1,2,3,4           | Slide Switch                        | Select the boot mode of the  system                          |
| 6          | SW3                  | Tact Switch                         | PMIC ON Key: Only for Test                                   |
| 7          | S1                   | Tact Switch                         | System K_RESET: Initialize the  power management block of TCC803x |
| 8          | SW2                  | Tact Switch                         | System P_RESET: Initialize the  system of TCC803x            |
| 9          | JC4                  | USB Type-A Connector                | USB2.0 High speed Host  connector                            |
| 10         | JC2                  | USB Type-A Connector                | USB2.0 High speed Host and  Device connector                 |
| 11         | JC1                  | USB3.0 Type-A Connector             | USB3.0 Super speed connector                                 |
| 12         | JM1                  | MicroSD Socket                      | MicroSD memory card socket                                   |
| 13         | JC7                  | RJ45 Connector                      | Legacy Ethernet port                                         |
| 14         | U26                  | -                                   | NC (Ethernet AVB port)                                       |
| 15         | JR3                  | 24-pin Right Angle Pin Header  Box  | Connect to the Open-LDI LCD  module for dual-channel control signals |
| 16         | JR5                  | 24-pin Right Angle Pin Header  Box  | Connect to the LCD module for HDMI  control signals          |
| 17         | JR6                  | 24-pin Right Angle Pin Header  Box  | Connect to the Open-LDI LCD  module for single-channel control signals |
| 18         | JH3                  | 40-pin Mezzanine Connector          | Connect to the Bluetooth and Wi-Fi  sub-board                |
| 19         | JH2                  | 40-pin Mezzanine Connector          | Connect to the PCIe sub-board                                |
| 20         | JC5                  | HDMI Connector                      | Connect to the HDMI TFT LCD  module                          |
| 21         | JH1                  | 40-pin Mezzanine Connector          | Connect to the MIPI sub-board                                |
| 22         | J10D1                | 20-pin Right Angle Pin Header  Male | JTAG connector for system debugging                          |


Figure 2.2 shows the bottom view of TCC803x CPU sub-board.

Figure 2.2 CPU Sub-board (Bottom View)
![Figure 2.3 Main Board Top View](/803x/linux-yp4.0-getting-started/figure-2.3-main-board-top-view.png)

Table 2.3 describes TCC803x CPU sub-board (bottom view) connectors.

Table 2.3 Description of CPU Sub-board (Bottom View)

|**Number**|**Reference Number**|**Name**|**Description**|
|:---:|:---:|:---:|:---:|
|1|JHB2|180-pin B to B Connector|Connect CPU board to the main board|
|2|JHB1|180-pin B to B Connector|Connect CPU board to the main board|
|3|JC3|Micro type USB AB Connector|USB device connector for downloading firmware|

### 2.1.2   Main Board

Figure 2.3 shows the top view of the main board.

Figure 2.3 Main Board (Top View)

Table 2.4 describes the main board (top view) connectors.

Table 2.4 Description of Main Board (Top View)

|**Number**|**Reference Number**|**Name**|**Description**|
|---|---|---|---|
|1|JHB4|180-pin B to B Connector|Connect the main board to the CPU sub-board|
|2|JHB3|180-pin B to B Connector|Connect the main board to the CPU sub-board|
|3|JP7|4-pin Pin Header Female|Connect the main board to the External MIC|
|4|JP8|4-pin Pin Header Female|Connect the main board to the External MIC|
|5|JC4|Phone Jack|Jack for sound output from the rear seat|
|6|JC2|Phone Jack|Jack for sound output from the front seat|
|7|JC1|Phone Jack|Jack for sound input to the AUX|


Figure 2.4 shows the bottom view of the main board.
![Figure 2.4 Main Board Bottom View](/803x/linux-yp4.0-getting-started/figure-2.4-main-board-bottom-view.png)

Figure 2.4 Main Board (Bottom View)

Table 2.5 describes the main board (bottom view) connectors.

Table 2.5 Description of Main Board (Bottom View)

|**Number**|**Reference Number**|**Name**|**Description**|
|---|---|---|---|
|1|J7|Power Jack|12V Power Jack|
|2|SW2|Toggle Switch|Test for ACC signal|
|3|SW1|Toggle Switch|Test for EarlyCamera and RearCamera|
|4|JH1|14-pin Pin Header Male|Connect the main board to the iPod sub-board|
|5|JH7|20-pin Pin Header Male|Connect the main board to the UART Test sub-board|
|6|JH9|20-pin Pin Header Male|Connect the main board to the key sub-board|
|7|CON1|D-sub 9-pin Connector|UART debug port for Main Core (Cortex-A53)|
|8|CON2|D-sub 9-pin Connector|UART debug port for MCU (Cortex-R5)|
|9|JP11|4-pin Pin Header Male|UART debug port for Sub-core (Cortex-A7)|
|10|JP14|12-pin Pin Header Male|Audio Power header for connecting main board with ABRB|
|11|JP15|12-pin Pin Header Male|DXB Power header for connecting main board with ABRB|
|12|JP1|12-pin Pin Header Male|Radio Tuner Power header for connecting main board with ABRB|
|13|JP5|38-pin Pin Header Male|Radio Tuner signal Header for connecting main board with ABRB|
|14|JH2|44-pin Pin Header Male|Connect the main board to the Camera test sub-board|
|15|JP12|38-pin Pin Header Male|DXB signal header for connecting main board with ABRB|
|16|JC9|RCA Jack|Input of CVBS or Audio|
|17|JP13|50-pin Pin Header Male|Audio Codec or DSP signal header for connecting main board with ABRB|
|18|CON3|D-sub 9-pin Connector|CAN and LIN|
|19|JP6|14-pin Pin Header Male|Select the output channel for CAN and LIN|
|20|JC7|Fiber optical Jack|Output of S/PDIF|
|21|JC5|Fiber optical Jack|Input of S/PDIF|
|22|U19|Power AMP|45W Power AMP<br><br>**Note:** Not mounted on the board|
|23|JP4|Test Point|Connect the main board to the speaker|
|24|JH8|30-pin Pin Header Box|Connector for Vehicle signal input|

**Note:** Test sub-board and camera test sub-board are not provided by Telechips.