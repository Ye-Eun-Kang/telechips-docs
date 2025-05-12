

# Introduction

This document describes Linux_YP4.0_IVI usage as follows:

- Board Description for TCC803x EVB

- Board Assembly Guide for TCC803x EVB

- Build Guide for Linux_YP4.0_IVI

- FWDN Guide for TCC803x in Linux_YP4.0_IVI

- Booting Guide for TCC803x EVB

# Board Description

## EVB Version


Table 2.1 EVB Version

| **Board**                                           | **Board Name/Version**                                       |
| --------------------------------------------------- | ------------------------------------------------------------ |
| CPU Sub-board                                       | TCC8030_CPU_LPD4321_V1.2.2                                   |
| Main Board                                          | TCC803X_MAIN_V1.1.1                                          |
| 12.3” 1920x720 LCD                                  | TM_WLCD_12.3LVDS_SV0.2  TCC80XX_BOE_WLCD_12.3_SV1.1.1    TCCXXXX_AUO_WLCD_12.3_SV0.1.0 |
| Audio and Broadcasting and Radio tuner Board (ABRB) | TCC8XXX_AK4601_SILAB_ISDBT_DAB_SV1.0                         |
| Jog Navigation Sub-board                            | TCC80XX_KEY_SV0.1                                            |

 **Note:** For more details, refer to the following document. \[8\]

- "*TCC803x Common Hardware-Assembly Manual for EVB*"



**Important**: The default LCD setting of Linux_YP4.0_IVI SDK is fitted with "TCCXXXX_AUO_WLCD_12.3".

To use a different LCD, modify the build configuration as described in Chapter 4.6.3.4.3.



### 1.1.1  CPU Sub-board

Figure 2.1 shows the top view of TCC803x CPU sub-board.

![Figure 2.1 CPU Sub-board](/803x/linux-yp4.0-getting-started/figure-2.1-cpu-sub-board.png)


​                               

Figure 2.1 CPU Sub-board (Top View)

 

Table 2.2 describes the TCC803x CPU sub-board (top view) connectors.

 

Table 2.2 Description of CPU Sub-board (Top View)

| **Number** | **Reference Number** | **Name**                            | **Description**                                              |
| ---------- | -------------------- | ----------------------------------- | ------------------------------------------------------------ |
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
