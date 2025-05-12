
> id: linux-yp40-sdk-getting-started
>
> title:Linux YP4.0 IVI SDK-Getting Started for TCC803x
>
> typora-root-url: ./static/img/


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


=======
+------------------------------+---------------------------------------+
| **Board**                    | **Board Name/Version**                |
+:============================:+=======================================+
| CPU Sub-board                | TCC8030_CPU_LPD4321_V1.2.2            |
+------------------------------+---------------------------------------+
| Main Board                   | TCC803X_MAIN_V1.1.1                   |
+------------------------------+---------------------------------------+
| 12.3" 1920x720 LCD           | TM_WLCD_12.3LVDS_SV0.2                |
|                              |                                       |
|                              | TCC80XX_BOE_WLCD_12.3_SV1.1.1         |
|                              |                                       |
|                              | TCCXXXX_AUO_WLCD_12.3_SV0.1.0         |
+------------------------------+---------------------------------------+
| Audio and Broadcasting and   | TCC8XXX_AK4601_SILAB_ISDBT_DAB_SV1.0  |
| Radio tuner Board (ABRB)     |                                       |
+------------------------------+---------------------------------------+
| Jog Navigation Sub-board     | TCC80XX_KEY_SV0.1                     |
+------------------------------+---------------------------------------+

: []{#_Ref167786678 .anchor}Table 2.1 EVB Version

**Note:** For more details, refer to the following document. \[8\]

- "*TCC803x Common Hardware-Assembly Manual for EVB*"

  **Important**: The default LCD setting of Linux_YP4.0_IVI SDK is
  fitted with "TCCXXXX_AUO_WLCD_12.3".

  To use a different LCD, modify the build configuration as described in
  Chapter 4.6.3.4.3.
>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b

### CPU Sub-board

Figure 2.1 shows the top view of TCC803x CPU sub-board.
![image-20250512112558246](../../../../../../YE/15. web-base documentation/Github/telechips-docs/static/img/Linux YP4.0 IVI SDK-Getting Started for TCC803x/image-20250512112558246.png)

[]{#_Ref157148846 .anchor}Figure 2.1 CPU Sub-board (Top View)

Table 2.2 describes the TCC803x CPU sub-board (top view) connectors.

+----+--------+------------------+------------------------------------+
| ** | **Ref  | **Name**         | **Description**                    |
| Nu | erence |                  |                                    |
| mb | Nu     |                  |                                    |
| er | mber** |                  |                                    |
| ** |        |                  |                                    |
+:==:+:======:+:================:+====================================+
| 1  | JR4    | > 26-pin LVDS    | > Connect to the LCD module for    |
|    |        | > Connector      | > single-channel LVDS signal       |
+----+--------+------------------+------------------------------------+
| 2  | JR2    | > 26-pin LVDS    | > Connect to the LCD module for    |
|    |        | > Connector      | > dual-channel LVDS signal         |
+----+--------+------------------+------------------------------------+
| 3  | JR1    | > 26-pin LVDS    | > Connect to the LCD module for    |
|    |        | > Connector      | > dual-channel LVDS signal         |
+----+--------+------------------+------------------------------------+
| 4  | J      | > Slide Switch   | > Select the path of bus switch    |
|    | SW7,10 |                  |                                    |
+----+--------+------------------+------------------------------------+
| 5  | JSW1   | > Slide Switch   | > Select the boot mode of the      |
|    | ,2,3,4 |                  | > system                           |
+----+--------+------------------+------------------------------------+
| 6  | SW3    | > Tact Switch    | > PMIC ON Key: Only for Test       |
+----+--------+------------------+------------------------------------+
| 7  | S1     | > Tact Switch    | > System K_RESET: Initialize the   |
|    |        |                  | > power management block of        |
|    |        |                  | > TCC803x                          |
+----+--------+------------------+------------------------------------+
| 8  | SW2    | > Tact Switch    | > System P_RESET: Initialize the   |
|    |        |                  | > system of TCC803x                |
+----+--------+------------------+------------------------------------+
| 9  | JC4    | > USB Type-A     | > USB2.0 High speed Host connector |
|    |        | > Connector      |                                    |
+----+--------+------------------+------------------------------------+
| 10 | JC2    | > USB Type-A     | > USB2.0 High speed Host and       |
|    |        | > Connector      | > Device connector                 |
+----+--------+------------------+------------------------------------+
| 11 | JC1    | > USB3.0 Type-A  | > USB3.0 Super speed connector     |
|    |        | > Connector      |                                    |
+----+--------+------------------+------------------------------------+
| 12 | JM1    | > MicroSD Socket | > MicroSD memory card socket       |
+----+--------+------------------+------------------------------------+
| 13 | JC7    | > RJ45 Connector | > Legacy Ethernet port             |
+----+--------+------------------+------------------------------------+
| 14 | U26    | > \-             | > NC (Ethernet AVB port)           |
+----+--------+------------------+------------------------------------+
| 15 | JR3    | > 24-pin Right   | > Connect to the Open-LDI LCD      |
|    |        | > Angle Pin      | > module for dual-channel control  |
|    |        | > Header Box     | > signals                          |
+----+--------+------------------+------------------------------------+
| 16 | JR5    | > 24-pin Right   | > Connect to the LCD module for    |
|    |        | > Angle Pin      | > HDMI control signals             |
|    |        | > Header Box     |                                    |
+----+--------+------------------+------------------------------------+
| 17 | JR6    | > 24-pin Right   | > Connect to the Open-LDI LCD      |
|    |        | > Angle Pin      | > module for single-channel        |
|    |        | > Header Box     | > control signals                  |
+----+--------+------------------+------------------------------------+
| 18 | JH3    | > 40-pin         | > Connect to the Bluetooth and     |
|    |        | > Mezzanine      | > Wi-Fi sub-board                  |
|    |        | > Connector      |                                    |
+----+--------+------------------+------------------------------------+
| 19 | JH2    | > 40-pin         | > Connect to the PCIe sub-board    |
|    |        | > Mezzanine      |                                    |
|    |        | > Connector      |                                    |
+----+--------+------------------+------------------------------------+
| 20 | JC5    | > HDMI Connector | > Connect to the HDMI TFT LCD      |
|    |        |                  | > module                           |
+----+--------+------------------+------------------------------------+
| 21 | JH1    | > 40-pin         | > Connect to the MIPI sub-board    |
|    |        | > Mezzanine      |                                    |
|    |        | > Connector      |                                    |
+----+--------+------------------+------------------------------------+
| 22 | J10D1  | > 20-pin Right   | > JTAG connector for system        |
|    |        | > Angle Pin      | > debugging                        |
|    |        | > Header Male    |                                    |
+----+--------+------------------+------------------------------------+

: []{#_Ref164840123 .anchor}Table 2.2 Description of CPU Sub-board (Top
View)

Figure 2.2 shows the bottom view of TCC803x CPU sub-board.

![](media/image3.png){width="6.458333333333333in" height="4.53125in"}

[]{#_Ref27727596 .anchor}Figure 2.2 CPU Sub-board (Bottom View)

Table 2.3 describes TCC803x CPU sub-board (bottom view) connectors.

+----+-------+------------------+------------------------------------+
| ** | *     | **Name**         | **Description**                    |
| Nu | *Refe |                  |                                    |
| mb | rence |                  |                                    |
| er | Num   |                  |                                    |
| ** | ber** |                  |                                    |
+:==:+:=====:+:================:+====================================+
| 1  | JHB2  | 180-pin B to B   | > Connect CPU board to the main    |
|    |       | Connector        | > board                            |
+----+-------+------------------+------------------------------------+
| 2  | JHB1  | 180-pin B to B   | > Connect CPU board to the main    |
|    |       | Connector        | > board                            |
+----+-------+------------------+------------------------------------+
| 3  | JC3   | Micro type USB   | > USB device connector for         |
|    |       | AB Connector     | > downloading firmware             |
+----+-------+------------------+------------------------------------+

: []{#_Ref36478714 .anchor}Table 2.3 Description of CPU Sub-board
(Bottom View)

### Main Board

Figure 2.3 shows the top view of the main board.

![](media/image4.jpeg){width="6.854166666666667in" height="3.59375in"}

[]{#_Ref157148849 .anchor}Figure 2.3 Main Board (Top View)

Table 2.4 describes the main board (top view) connectors.

+----+-------+------------------+------------------------------------+
| ** | *     | **Name**         | **Description**                    |
| Nu | *Refe |                  |                                    |
| mb | rence |                  |                                    |
| er | Num   |                  |                                    |
| ** | ber** |                  |                                    |
+:==:+:=====:+:================:+:===================================+
| 1  | JHB4  | 180-pin B to B   | > Connect the main board to the    |
|    |       | Connector        | > CPU sub-board                    |
+----+-------+------------------+------------------------------------+
| 2  | JHB3  | 180-pin B to B   | > Connect the main board to the    |
|    |       | Connector        | > CPU sub-board                    |
+----+-------+------------------+------------------------------------+
| 3  | JP7   | 4-pin Pin Header | > Connect the main board to the    |
|    |       | Female           | > External MIC                     |
+----+-------+------------------+------------------------------------+
| 4  | JP8   | 4-pin Pin Header | > Connect the main board to the    |
|    |       | Female           | > External MIC                     |
+----+-------+------------------+------------------------------------+
| 5  | JC4   | Phone Jack       | > Jack for sound output from the   |
|    |       |                  | > rear seat                        |
+----+-------+------------------+------------------------------------+
| 6  | JC2   | Phone Jack       | > Jack for sound output from the   |
|    |       |                  | > front seat                       |
+----+-------+------------------+------------------------------------+
| 7  | JC1   | Phone Jack       | > Jack for sound input to the AUX  |
+----+-------+------------------+------------------------------------+

: []{#_Ref164840175 .anchor}Table 2.4 Description of Main Board (Top
View)

Figure 2.4 shows the bottom view of the main board.

![](media/image5.jpeg){width="5.982609361329834in"
height="3.652485783027122in"}

[]{#_Ref157148850 .anchor}Figure 2.4 Main Board (Bottom View)

Table 2.5 describes the main board (bottom view) connectors.

+----+-------+----------------+--------------------------------------+
| ** | *     | **Name**       | **Description**                      |
| Nu | *Refe |                |                                      |
| mb | rence |                |                                      |
| er | Num   |                |                                      |
| ** | ber** |                |                                      |
+:==:+:=====:+:==============:+:=====================================+
| 1  | J7    | Power Jack     | > 12V Power Jack                     |
+----+-------+----------------+--------------------------------------+
| 2  | SW2   | Toggle Switch  | > Test for ACC signal                |
+----+-------+----------------+--------------------------------------+
| 3  | SW1   | Toggle Switch  | > Test for EarlyCamera and           |
|    |       |                | > RearCamera                         |
+----+-------+----------------+--------------------------------------+
| 4  | JH1   | 14-pin Pin     | > Connect the main board to the iPod |
|    |       | Header Male    | > sub-board                          |
+----+-------+----------------+--------------------------------------+
| 5  | JH7   | 20-pin Pin     | > Connect the main board to the UART |
|    |       | Header Male    | > Test sub-board                     |
+----+-------+----------------+--------------------------------------+
| 6  | JH9   | 20-pin Pin     | > Connect the main board to the key  |
|    |       | Header Male    | > sub-board                          |
+----+-------+----------------+--------------------------------------+
| 7  | CON1  | D-sub 9-pin    | > UART debug port for Main Core      |
|    |       | Connector      | > (Cortex-A53)                       |
+----+-------+----------------+--------------------------------------+
| 8  | CON2  | D-sub 9-pin    | > UART debug port for MCU            |
|    |       | Connector      | > (Cortex-R5)                        |
+----+-------+----------------+--------------------------------------+
| 9  | JP11  | 4-pin Pin      | > UART debug port for Sub-core       |
|    |       | Header Male    | > (Cortex-A7)                        |
+----+-------+----------------+--------------------------------------+
| 10 | JP14  | 12-pin Pin     | > Audio Power header for connecting  |
|    |       | Header Male    | > main board with ABRB               |
+----+-------+----------------+--------------------------------------+
| 11 | JP15  | 12-pin Pin     | > DXB Power header for connecting    |
|    |       | Header Male    | > main board with ABRB               |
+----+-------+----------------+--------------------------------------+
| 12 | JP1   | 12-pin Pin     | > Radio Tuner Power header for       |
|    |       | Header Male    | > connecting main board with ABRB    |
+----+-------+----------------+--------------------------------------+
| 13 | JP5   | 38-pin Pin     | > Radio Tuner signal Header for      |
|    |       | Header Male    | > connecting main board with ABRB    |
+----+-------+----------------+--------------------------------------+
| 14 | JH2   | 44-pin Pin     | > Connect the main board to the      |
|    |       | Header Male    | > Camera test sub-board              |
+----+-------+----------------+--------------------------------------+
| 15 | JP12  | 38-pin Pin     | > DXB signal header for connecting   |
|    |       | Header Male    | > main board with ABRB               |
+----+-------+----------------+--------------------------------------+
| 16 | JC9   | RCA Jack       | > Input of CVBS or Audio             |
+----+-------+----------------+--------------------------------------+
| 17 | JP13  | 50-pin Pin     | > Audio Codec or DSP signal header   |
|    |       | Header Male    | > for connecting main board with     |
|    |       |                | > ABRB                               |
+----+-------+----------------+--------------------------------------+
| 18 | CON3  | D-sub 9-pin    | > CAN and LIN                        |
|    |       | Connector      |                                      |
+----+-------+----------------+--------------------------------------+
| 19 | JP6   | 14-pin Pin     | > Select the output channel for CAN  |
|    |       | Header Male    | > and LIN                            |
+----+-------+----------------+--------------------------------------+
| 20 | JC7   | Fiber optical  | > Output of S/PDIF                   |
|    |       | Jack           |                                      |
+----+-------+----------------+--------------------------------------+
| 21 | JC5   | Fiber optical  | > Input of S/PDIF                    |
|    |       | Jack           |                                      |
+----+-------+----------------+--------------------------------------+
| 22 | U19   | Power AMP      | > 45W Power AMP **\                  |
|    |       |                | > **                                 |
|    |       |                | >                                    |
|    |       |                | > **Note:** Not mounted on the board |
+----+-------+----------------+--------------------------------------+
| 23 | JP4   | Test Point     | > Connect the main board to the      |
|    |       |                | > speaker                            |
+----+-------+----------------+--------------------------------------+
| 24 | JH8   | 30-pin Pin     | > Connector for Vehicle signal input |
|    |       | Header Box     |                                      |
+----+-------+----------------+--------------------------------------+

: []{#_Ref112313501 .anchor}Table 2.5 Description of Main Board (Bottom
View)

**Note:** Test sub-board and camera test sub-board are not provided by
Telechips.

###  LCD Sub-board for Default EVB Configuration

Three types of LCD boards are supported for EVB configurations. Choose
the appropriate one based on your LCD type.

**Note:** Linux_YP4.0_IVI SDK's default setting of LCD is fitted with
"TCCXXXX_AUO_WLCD_12.3".

#### TCC80XX_BOE_WLCD_12.3" LCD Sub-board

Figure 2.5 shows the top view of TCC80XX_BOE_WLCD_12.3" LCD sub-board.

![](media/image6.png){width="7.4474234470691165in"
height="3.1742880577427823in"}

[]{#_Ref156838684 .anchor}Figure 2.5 TCC80XX_BOE_WLCD_12.3" LCD
Sub-board (Top View)

Table 2.6 describes TCC80XX_BOE_WLCD_12.3" LCD sub-board (top view)
connectors.

+----+-------+------------------+------------------------------------+
| ** | *     | **Name**         | **Description**                    |
| Nu | *Refe |                  |                                    |
| mb | rence |                  |                                    |
| er | Num   |                  |                                    |
| ** | ber** |                  |                                    |
+:==:+:=====:+:================:+====================================+
| 1  | J13   | 26-pin LVDS      | > Connect to even channel LVDS     |
|    |       | Connector        |                                    |
+----+-------+------------------+------------------------------------+
| 2  | J12   | 26-pin LVDS      | > Connect to odd channel LVDS      |
|    |       | Connector        |                                    |
+----+-------+------------------+------------------------------------+
| 3  | CON1  | 24-pin Right     | > Receive power and control        |
|    |       | Angle Header Box | > signals for touch                |
+----+-------+------------------+------------------------------------+
| 4  | CON2  | 24-pin Right     | > Receive power and control        |
|    |       | Angle Header Box | > signals for touch                |
+----+-------+------------------+------------------------------------+
| 5  | CON3  | 24-pin Right     | > Receive power and control        |
|    |       | Angle Header Box | > signals                          |
+----+-------+------------------+------------------------------------+
| 6  | CON4  | 24-pin Right     | > Receive power and control        |
|    |       | Angle Header Box | > signals                          |
+----+-------+------------------+------------------------------------+

: []{#_Ref156838685 .anchor}Table 2.6 Description of
TCC80XX_BOE_WLCD_12.3" LCD Sub-board (Top View)

Figure 2.6 shows the bottom view of TCC80XX_BOE_WLCD_12.3" LCD
sub-board.

![](media/image7.png){width="7.276388888888889in" height="4.1125in"}

[]{#_Ref156838686 .anchor}Figure 2.6 TCC80XX_BOE_WLCD_12.3" LCD
Sub-board (Bottom View)

Table 2.7 describes TCC80XX_BOE_WLCD_12.3" LCD sub-board (bottom view)
connectors.

+----+---------+-------------+----------------------------------------+
| ** | **Re    | **Name**    | **Description**                        |
| Nu | ference |             |                                        |
| mb | N       |             |                                        |
| er | umber** |             |                                        |
| ** |         |             |                                        |
+:==:+:=======:+:===========:+========================================+
| 1  | CON6    | 10-pin      | > Optional power output connector for  |
|    |         | Power       | > connecting additional LCD sub-board  |
|    |         | Connector   | > in DP daisy chain mode               |
+----+---------+-------------+----------------------------------------+
| 2  | CON5    | 10-pin      | > Optional power input connector for   |
|    |         | Power       | > connecting additional LCD sub-board  |
|    |         | Connector   | > in DP daisy chain mode               |
+----+---------+-------------+----------------------------------------+
| 3  | J11     | Phone Jack  | > Audio codec output                   |
+----+---------+-------------+----------------------------------------+
| 4  | J10     | FPC         | > Connect to touch interface of BOE    |
|    |         | Connector   | > LCD                                  |
+----+---------+-------------+----------------------------------------+
| 5  | J9      | FPC         | > Connect to backlight and open-LDI    |
|    |         | Connector   | > interface of BOE LCD                 |
+----+---------+-------------+----------------------------------------+
| 6  | J4      | DP          | > Connect the BOE LCD sub-board to the |
|    |         | Connector   | > TCC805x CPU board                    |
+----+---------+-------------+----------------------------------------+
| 7  | J1      | HDMI        | > Connect the BOE LCD sub-board to the |
|    |         | Connector   | > TCC803x CPU board                    |
+----+---------+-------------+----------------------------------------+
| 8  | J2      | FAKRA       | > Connect to HDMI for data output in   |
|    |         | Connector   | > GMSL                                 |
+----+---------+-------------+----------------------------------------+
| 9  | J6      | FAKRA       | > Connect to DP_A for data output in   |
|    |         | Connector   | > GMSL                                 |
+----+---------+-------------+----------------------------------------+
| 10 | > J5    | > FAKRA     | > Connect to DP_B for data output in   |
|    |         | > Connector | > GMSL                                 |
+----+---------+-------------+----------------------------------------+
| 11 | J7      | FAKRA       | > Connect to DP in daisy chain mode    |
|    |         | Connector   | > for data output in GMSL              |
+----+---------+-------------+----------------------------------------+
| 12 | J8      | FAKRA       | > Connect to DP or HDMI for data       |
|    |         | Connector   | > output in GMSL                       |
+----+---------+-------------+----------------------------------------+
| 13 | SW5     | DIP Switch  | > Select the display mode of           |
|    |         |             | > deserializer CFG1                    |
+----+---------+-------------+----------------------------------------+
| 14 | SW3,4   | DIP Switch  | > Select the display mode of           |
|    |         |             | > deserializer CFG0                    |
+----+---------+-------------+----------------------------------------+
| 15 | SW6     | Slide       | > Select the LVDS source of BOE LCD    |
|    |         | Switch      |                                        |
+----+---------+-------------+----------------------------------------+
| 16 | SW2     | Slide       | > Select the GPIOs to control HDMI or  |
|    |         | Switch      | > DP interface                         |
+----+---------+-------------+----------------------------------------+
| 17 | SW1     | Slide       | > Select the GPIOs to control LVDS or  |
|    |         | Switch      | > SerDes interface                     |
+----+---------+-------------+----------------------------------------+

: []{#_Ref156838687 .anchor}Table 2.7 Description of
TCC80XX_BOE_WLCD_12.3" LCD Sub-board (Bottom View)

**Note**: Parts related to DisplayPort (DP) (1, 2, 6, 9, 10, and 11) are
not used in TCC803x EVB.

#### 12.3\" 1920x720 TFT LCD Sub-board

Figure 2.7 shows the top view of 12.3\" 1920x720 TFT LCD sub-board.

![](media/image8.jpeg){width="4.565217629046369in"
height="2.217884951881015in"}

[]{#_Ref35614058 .anchor}Figure 2.7 12.3\" 1920x720 TFT LCD Sub-board
(Top View)

Table 2.8 describes 12.3\" 1920x720 TFT LCD sub-board (top view)
connectors.

+----+-------+------------------+------------------------------------+
| ** | *     | **Name**         | **Description**                    |
| Nu | *Refe |                  |                                    |
| mb | rence |                  |                                    |
| er | Num   |                  |                                    |
| ** | ber** |                  |                                    |
+:==:+:=====:+:================:+====================================+
| 1  | JR2   | 26-pin LVDS      | > Connect to odd channel LVDS      |
|    |       | Connector        |                                    |
+----+-------+------------------+------------------------------------+
| 2  | JR1   | 26-pin LVDS      | > Connect to even channel LVDS     |
|    |       | Connector        |                                    |
+----+-------+------------------+------------------------------------+
| 3  | JR3   | 24-pin Right     | > Receive power and control        |
|    |       | Angle Header Box | > signals                          |
+----+-------+------------------+------------------------------------+
| 4  | CN1   | FPC Connector    | > Connect the TFT LCD sub-board to |
|    |       |                  | > the TFT LCD panel                |
+----+-------+------------------+------------------------------------+
| 5  | CN4   | FPC Connector    | > Connector for backlight power of |
|    |       |                  | > TFT LCD panel                    |
+----+-------+------------------+------------------------------------+

: []{#_Ref35614094 .anchor}Table 2.8 Description of 12.3\" 1920x720 TFT
LCD Sub-board (Top View)

Figure 2.8 shows the bottom view of 12.3\" 1920x720 TFT LCD sub-board.

![](media/image9.jpeg){width="4.408696412948381in"
height="2.296580271216098in"}

[]{#_Ref35615836 .anchor}Figure 2.8 12.3" 1920x720 TFT LCD Sub-board
(Bottom View)

Table 2.9 describes 12.3\" 1920x720 TFT LCD sub-board (bottom view)
connectors.

+----+--------+-----------------+-------------------------------------+
| ** | **Ref  | **Name**        | **Description**                     |
| Nu | erence |                 |                                     |
| mb | Nu     |                 |                                     |
| er | mber** |                 |                                     |
| ** |        |                 |                                     |
+:==:+:======:+:===============:+=====================================+
| 1  | CN2    | FPC Connector   | > Connect the TFT LCD sub-board to  |
|    |        |                 | > the TFT LCD panel                 |
+----+--------+-----------------+-------------------------------------+
| 2  | JC1    | HDMI Connector  | > Connect the TFT LCD sub-board to  |
|    |        |                 | > the CPU sub-board                 |
+----+--------+-----------------+-------------------------------------+
| 3  | JSW1   | Slide Switch    | > Select HDMI or LVDS input         |
+----+--------+-----------------+-------------------------------------+
| 4  | CN3    | FPC Connector   | > Connector for backlight power of  |
|    |        |                 | > TFT LCD panel                     |
+----+--------+-----------------+-------------------------------------+

: []{#_Ref35614946 .anchor}Table 2.9 Description of 12.3\" 1920x720 TFT
LCD Sub-board (Bottom View)

#### TCCXXXX_AUO_WLCD_12.3\" LCD Sub-board

![](media/image10.png){width="7.276388888888889in"
height="5.6819444444444445in"}

[]{#_Toc167786527 .anchor}Figure 2.9 TCCXXXX_AUO_WLCD_12.3\" LCD
Sub-board

### ABRB

<<<<<<< HEAD
[Figure]: 

shows the top view of ABRB. The ABRB is connected to the
=======
Figure 2.10 shows the top view of ABRB. The ABRB is connected to the
>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
main board.

<figure>
<img src="media/image11.jpeg" style="width:5.576in;height:4.12183in" />
<figcaption><p><span id="_Ref167786570" class="anchor"></span>Figure
2.10 ABRB (Top View)</p></figcaption>
</figure>

<<<<<<< HEAD
=======

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
Table 2.10 describes ABRB (top view) connectors.

+----+--------+------------------+-----------------------------------+
| ** | **Ref  | **Name**         | **Description**                   |
| Nu | erence |                  |                                   |
| mb | Nu     |                  |                                   |
| er | mber** |                  |                                   |
| ** |        |                  |                                   |
+:==:+:======:+:================:+===================================+
| 1  | CON6   | SMA Connectors   | > Broadcasting tuner antenna --   |
|    | ,7,8,9 |                  | > ISDBT and CMMB                  |
+----+--------+------------------+-----------------------------------+
| 2  | CON4,5 | SMA Connectors   | > Broadcasting tuner antenna --   |
|    |        |                  | > DAB, DMB                        |
+----+--------+------------------+-----------------------------------+
| 3  | JC1    | Phone Jack       | > Audio codec output              |
+----+--------+------------------+-----------------------------------+
| 4  | JP8    | 12-pin Pin       | > Power for external turner       |
|    |        | Header Male      | > sub-board                       |
+----+--------+------------------+-----------------------------------+
| 5  | CO     | SMA Connectors   | > Radio tuner antenna (Band3_A/B) |
|    | N10,11 |                  |                                   |
+----+--------+------------------+-----------------------------------+
| 6  | CON1,2 | SMA Connectors   | > Radio tuner antenna             |
|    |        |                  | > (FMA/FMB/AMI)                   |
+----+--------+------------------+-----------------------------------+
| 7  | JP9    | 38-pin Pin       | > Pin Header Male for external    |
|    |        | Header Male      | > Radio tuner sub-board           |
+----+--------+------------------+-----------------------------------+
| 8  | JSW2   | Slide Switch     | > Select for Basic tuner or tuner |
|    |        |                  | > sub-board                       |
+----+--------+------------------+-----------------------------------+
| 9  | JSW1   | Slide Switch     | > Select for DXB tuner            |
+----+--------+------------------+-----------------------------------+
| 10 | JSW4   | Slide Switch     | > Select for DAC                  |
+----+--------+------------------+-----------------------------------+
| 11 | JSW3   | Slide Switch     | > Select for Codec (AK4601 or     |
|    |        |                  | > TCC7604)                        |
+----+--------+------------------+-----------------------------------+

: []{#_Ref35616185 .anchor}Table 2.10 Description of ABRB (Top View)

Figure 2.11 shows the bottom view of ABRB.

![](media/image12.jpeg){width="4.714116360454943in"
height="3.5679997812773405in"}

[]{#_Ref35616639 .anchor}Figure 2.11 ABRB (Bottom View)

Table 2.11 describes ABRB (bottom view) connectors.

+----+------------+------------------+---------------------------------+
| ** | **R        | **Name**         | **Description**                 |
| Nu | eference** |                  |                                 |
| mb |            |                  |                                 |
| er | **Number** |                  |                                 |
| ** |            |                  |                                 |
+:==:+:==========:+:================:+=================================+
| 1  | JP1        | 12-pin Pin       | > Radio Tuner Power             |
|    |            | Header Box       |                                 |
+----+------------+------------------+---------------------------------+
| 2  | JP3        | 12-pin Pin       | > DXB power                     |
|    |            | Header Box       |                                 |
+----+------------+------------------+---------------------------------+
| 3  | JP2        | 12-pin Pin       | > Audio power                   |
|    |            | Header Box       |                                 |
+----+------------+------------------+---------------------------------+
| 4  | JP5        | 50-pin Pin       | > Audio signals                 |
|    |            | Header Box       |                                 |
+----+------------+------------------+---------------------------------+
| 5  | JP6        | 36-pin Pin       | > DXB signals                   |
|    |            | Header Box       |                                 |
+----+------------+------------------+---------------------------------+
| 6  | JP4        | 38-pin Pin       | > Radio Tuner signals           |
|    |            | Header Box       |                                 |
+----+------------+------------------+---------------------------------+

: []{#_Ref35616687 .anchor}Table 2.11 Description of ABRB (Bottom View)

###  Jog Navigation Sub-board

On the TCC803x EVB, the key functions are provided by three tact
switches and two rotary encoder switches, corresponding to each function
as shown in Figure 2.12.

![](media/image13.png){width="4.179172134733158in"
height="1.7059514435695537in"}

[]{#_Ref143235592 .anchor}Figure 2.12 Jog Navigation Sub-board

### Chip Version

Only the BX version is supported. If you are using a different version,
you must replace it to the BX version.

The version information is marked on the chip.

- OXX-i: Engineering Sample (ES)

- OAX-i: Customer Sample (CS)-AX

- OBX-i: Customer Sample (CS)-BX

+------------+-----------------+-----------------------+---------------+
| **         | **Marking       | **Chip Marking**      | **Note**      |
| Category** | Information**   |                       |               |
+:==========:+:===============:+:=====================:+:=============:+
| TCC803x CS | > OAX           | > ![](media           | First         |
|            |                 | /image14.png){width=" | Customer      |
|            |                 | 1.2333333333333334in" | Sample        |
|            |                 | > height="            |               |
|            |                 | 1.179861111111111in"} |               |
+------------+-----------------+-----------------------+---------------+
|            | > OBX           | > ![](media           | Second        |
|            |                 | /image15.png){width=" | Customer      |
|            |                 | 1.2260837707786527in" | Sample        |
|            |                 | > height="            |               |
|            |                 | 1.235482283464567in"} |               |
+------------+-----------------+-----------------------+---------------+

## Boot Mode

### USB Boot Mode

+------------+-----------------+---------------------------------------+
| **         | **USB Boot Mode | **FWDN Port**                         |
| Category** | Switch**        |                                       |
+:==========:+:===============:+:=====================================:+
| TCC803x    | > ![](med       | > ![](media/image17.png)              |
|            | ia/image16.png) |                                       |
+------------+-----------------+---------------------------------------+

: []{#_Toc136422982 .anchor}Table 2.12 Set to USB Boot Mode

### SNOR Boot Mode

+------------+-----------------+-----------------------+---------------+
| **         | **SNOR Boot     | **Reset Switch**      | **Note**      |
| Category** | Mode Switch**   |                       |               |
+:==========:+:===============:+:=====================:+:==============+
| TCC803x    | > ![](med       | > ![](media           | > The reset   |
|            | ia/image18.png) | /image19.png){width=" | > button is   |
|            |                 | 1.4150940507436571in" | > on the      |
|            |                 | > height="            | > bottom left |
|            |                 | 1.477755905511811in"} | > corner of   |
|            |                 |                       | > the board.  |
+------------+-----------------+-----------------------+---------------+

: []{#_Toc519268645 .anchor}Table 2.13 Set to SNOR Boot Mode

### eMMC Boot Mode

+------------+-----------------+-----------------------+---------------+
| **         | **eMMC Boot     | **Reset Switch**      | **Note**      |
| Category** | Mode Switch**   |                       |               |
+:==========:+:===============:+:=====================:+:==============+
| TCC803x    | > ![](me        | > ![](media           | > The reset   |
|            | dia/image20.png | /image19.png){width=" | > button is   |
|            | ){width="0.8065 | 1.4150940507436571in" | > on the      |
|            | 999562554681in" | > height="            | > bottom left |
|            | >               | 1.477755905511811in"} | > corner of   |
|            |  height="1.2732 |                       | > the board.  |
|            | 28346456693in"} |                       |               |
+------------+-----------------+-----------------------+---------------+

: []{#_Ref30664774 .anchor}Table 2.14 Set to eMMC Boot Mode

### Function Switch

+------------+-----------------+---------------------------------------+
| Category   | Function Switch | Description                           |
+:==========:+:===============:+=======================================+
| Camera     | > ![](me        | > Use external camera port.           |
|            | dia/image21.png |                                       |
|            | ){width="0.9645 |                                       |
|            | 669291338582in" |                                       |
|            | >               |                                       |
|            | height="0.81889 |                                       |
|            | 76377952756in"} |                                       |
+------------+-----------------+---------------------------------------+
|            | > ![](me        | > Use internal camera port.           |
|            | dia/image22.png |                                       |
|            | ){width="0.7716 |                                       |
|            | 535433070866in" |                                       |
|            | >               |                                       |
|            | height="0.81889 |                                       |
|            | 76377952756in"} |                                       |
+------------+-----------------+---------------------------------------+
| Tuner/USB  | > ![](m         | > Use Tuner B (Broadcasting control). |
|            | edia/image23.pn |                                       |
|            | g){width="1.047 |                                       |
|            | 244094488189in" |                                       |
|            | >               |                                       |
|            | height="0.66535 |                                       |
|            | 43307086615in"} |                                       |
+------------+-----------------+---------------------------------------+
|            | > ![](me        | > Use USB (Enable USB power control). |
|            | dia/image24.png |                                       |
|            | ){width="0.8976 |                                       |
|            | 377952755905in" |                                       |
|            | >               |                                       |
|            | height="0.66535 |                                       |
|            | 43307086615in"} |                                       |
+------------+-----------------+---------------------------------------+
| Network    | > ![](me        | > Use e-AVB port.                     |
|            | dia/image25.png |                                       |
|            | ){width="0.8267 |                                       |
|            | 716535433071in" |                                       |
|            | >               |                                       |
|            | height="0.81496 |                                       |
|            | 06299212598in"} |                                       |
+------------+-----------------+---------------------------------------+
|            | > ![](me        | > Use Ethernet port.                  |
|            | dia/image26.png |                                       |
|            | ){width="0.7716 |                                       |
|            | 535433070866in" |                                       |
|            | >               |                                       |
|            | height="0.81496 |                                       |
|            | 06299212598in"} |                                       |
+------------+-----------------+---------------------------------------+

: []{#_Toc136422985 .anchor}Table 2.15 Set Function Switch

**Note:** For more details, refer to the following documents. \[11\]

- "*TCC803x Common Hardware-User Guide for EVB*"

- "*TCC803x Common Hardware-Quick Start Guide for EVB*"

# Board Assembly Guide

## Components of Kit

Table 3.1 describes the configuration for single display system of
TCC803x EVB.

+----------------------------+-----------------------------------+-----+
| **Figure**                 | **Name/Specification**            | **Q |
|                            |                                   | uan |
|                            |                                   | tit |
|                            |                                   | y** |
+:==========================:+:=================================:+:===:+
| ![](media/image27.png){wi  | TCC8030_CPU_LPD4321               | 1   |
| dth="1.0833333333333333in" |                                   |     |
| heig                       |                                   |     |
| ht="0.6893930446194225in"} |                                   |     |
+----------------------------+-----------------------------------+-----+
| ![](media/image28.jpeg){wi | TCC803X_MAIN                      | 1   |
| dth="1.1181102362204725in" |                                   |     |
| hei                        |                                   |     |
| ght="0.594488188976378in"} |                                   |     |
+----------------------------+-----------------------------------+-----+
| ![](media/image29.jpeg){wi | TCC8XXX_AK4601_SILAB_ISDBT_DAB    | 1   |
| dth="0.7009055118110237in" |                                   |     |
| heigh                      |                                   |     |
| t="0.46313976377952754in"} |                                   |     |
+----------------------------+-----------------------------------+-----+
| ![](media/image30.png){wi  | BOE_WLCD_12.3\" LCD or            | 1   |
| dth="1.2086953193350831in" | AUO_WLCD_12.3\" LCD (left)        |     |
| height="0.54059164         |                                   |     |
| 47944007in"}![](media/imag | or                                |     |
| e31.png){width="1.15625in" |                                   |     |
| heig                       | TM_WLCD_12.3LVDS (right)          |     |
| ht="0.5527843394575678in"} |                                   |     |
+----------------------------+-----------------------------------+-----+
| ![](media/image32.png){wi  | TCC80XX_KEY                       | 1   |
| dth="0.8985214348206474in" |                                   |     |
| heig                       |                                   |     |
| ht="0.3250831146106737in"} |                                   |     |
+----------------------------+-----------------------------------+-----+
| ![](media/image33.jpeg){wi | LVDS Cable                        | 2   |
| dth="0.6979166666666666in" |                                   |     |
| heig                       |                                   |     |
| ht="0.4097080052493438in"} |                                   |     |
+----------------------------+-----------------------------------+-----+
| ![](media/image34.jpeg){w  | 24-pin Flat Cable                 | 1   |
| idth="0.705498687664042in" |                                   |     |
| height="0.59375in"}        |                                   |     |
+----------------------------+-----------------------------------+-----+
| ![](media/image35.jpeg){w  | 20-pin Flat Cable                 | 1   |
| idth="0.874349300087489in" |                                   |     |
| height="0.53125in"}        |                                   |     |
+----------------------------+-----------------------------------+-----+
| ![](media/image            | Screw nut                         | 8   |
| 36.jpeg){width="0.46875in" |                                   |     |
| height="0.46875in"}        |                                   |     |
+----------------------------+-----------------------------------+-----+
| ![](media/image37.png){wi  | DC 12V Power Adapter              | 1   |
| dth="0.4722222222222222in" |                                   |     |
| heigh                      | (5A or more required)             |     |
| t="0.46070319335083115in"} |                                   |     |
+----------------------------+-----------------------------------+-----+
| ![](media/image38.png){wi  | Micro Type USB Cable              | 1   |
| dth="0.5729166666666666in" |                                   |     |
| heig                       |                                   |     |
| ht="0.5559667541557305in"} |                                   |     |
+----------------------------+-----------------------------------+-----+
| ![](media/image39.jpeg){wi | 110/220V Power Cable              | 1   |
| dth="0.4961122047244094in" |                                   |     |
| height="0.4375in"}         |                                   |     |
+----------------------------+-----------------------------------+-----+

: []{#_Ref143236920 .anchor}Table 3.1 Configuration for Single Display
System of TCC803x EVB

**Caution:** Compatibility problems may occur if you use cables other
than the basic components for display and Power Adapter provided by
Telechips.

## Display System Assembly

### Display System Assembly with BOE or AUO

**Step 1:** Set the switches on the WLCD_12.3" LCD sub-board.

For Dual LVDS, set the slide switches (SW1, SW2, and SW6) and DIP
switches (SW3, SW4, and SW5) as shown in the following Table 3.2 and
Figure 3.1.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
<<<<<<< HEAD
   **Display**                         **SW1**                                               **SW2**                                               **SW6**                                **SW4**                  **SW3**                  **SW5**
------------- ----------------------------------------------------- ----------------------------------------------------- ----------------------------------------------------- ------------------------ ------------------------ ------------------------
=======

   **Display**                         **SW1**                                               **SW2**                                               **SW6**                                **SW4**                  **SW3**                  **SW5**

------------- ----------------------------------------------------- ----------------------------------------------------- ----------------------------------------------------- ------------------------ ------------------------ ------------------------

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
    Dual LVDS    ![](media/image40.png){width="0.6654286964129483in"   ![](media/image41.png){width="0.6737773403324584in"   ![](media/image41.png){width="0.6737773403324584in"   ![](media/image42.emf)   ![](media/image42.emf)   ![](media/image43.emf)
                           height="0.3779527559055118in"}                        height="0.3834503499562555in"}                        height="0.3834503499562555in"}                                                               

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : []{#_Ref112158737 .anchor}Table 3.2 Configuration of LCD Sub-board
  Switch for Dual LVDS in Single Display System

![](media/image44.png){width="7.276388888888889in"
height="1.4326388888888888in"}

[]{#_Ref112168702 .anchor}Figure 3.1 Configuration of LCD Sub-board
Switch for Dual LVDS in Single Display System

**\
<<<<<<< HEAD
=======

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
**

**Step 2:** Check the LED indicator on the WLCD_12.3" LCD sub-board for
Single display system.

![](media/image45.jpeg){width="6.663888888888889in"
height="1.8479538495188101in"}

[]{#_Ref112231391 .anchor}Figure 3.2 LED Indicator of LCD Sub-board
Switch for Dual LVDS in Single Display System

**Step 3:** Connect LVDS cables and a flat cable as follows:

![](media/image46.png){width="6.299212598425197in"
height="2.8117410323709535in"}

[]{#_Ref112231392 .anchor}Figure 3.3 Cable Assembly

**Step 4:** As shown in Figure 3.4, assemble the WLCD_12.3" LCD
sub-board by aligning PCB supports with the hole, and connect each cable
to the sub-board.

![](media/image47.png){width="6.299212598425197in"
height="2.772062554680665in"}

[]{#_Ref112158805 .anchor}Figure 3.4 BOE/AUO LCD Assembly

**Step 5:** Tighten the screw nut to the WLCD_12.3" LCD sub-board.

![](media/image48.png){width="4.573109142607174in"
height="1.6794542869641296in"}

[]{#_Ref112231395 .anchor}Figure 3.5 Screw Engagement

![](media/image49.png){width="5.760661636045494in"
height="3.077703412073491in"}

[]{#_Ref112231396 .anchor}Figure 3.6 Position of Screw Engagement

**Step 6:** Connect the Jog Navigation sub-board to the main board by
using the flat cable for Jog Navigation sub-board as follows. Connect
the cable correctly based on the position of pin 1.

![](media/image50.png){width="3.7604166666666665in" height="2.75in"}

[]{#_Ref112231398 .anchor}Figure 3.7 Connect Jog Navigation Sub-Board to
Main Board

Figure 3.8 shows the completely assembled single display system of
TCC803x EVB.

![](media/image51.png){width="5.100896762904637in"
height="2.420589457567804in"}

[]{#_Ref112161012 .anchor}Figure 3.8 Assembled Single Display (for
Cluster) System of TCC803x EVB

### Display System Assembly with TFT LCD

**Step 1:** Connect LVDS cables and a flat cable as follows:

![](media/image46.png){width="6.299212598425197in"
height="2.8117410323709535in"}

[]{#_Ref27728059 .anchor}Figure 3.9 Cable Assembly

**Step 2:** As shown in Figure 3.10, assemble the 12.3\" 1920x720 TFT
LCD sub-board by aligning PCB supports with the hole, and connect each
cable to the sub-board.

![](media/image52.png){width="6.299212598425197in"
height="3.262609361329834in"}

[]{#_Ref27660331 .anchor}Figure 3.10 TFT LCD Assembly

**Step 3:** Tighten the screw nut to the 12.3" 1920x720 TFT LCD
sub-board.

![](media/image53.jpeg){width="4.724409448818897in"
height="0.8887904636920385in"}

[]{#_Toc124147915 .anchor}Figure 3.11 Screw Engagement

![](media/image54.jpeg){width="4.724409448818897in"
height="2.7971916010498687in"}

[]{#_Toc124147916 .anchor}Figure 3.12 Position of Screw Engagement

**Step 4:** Connect the Jog Navigation sub-board to the main board by a
flat cable as follows. Connect the cable correctly based on the position
of pin 1.

![](media/image55.png){width="6.299212598425197in"
height="3.124456474190726in"}

[]{#_Toc124147917 .anchor}Figure 3.13 Connect Jog Navigation Sub-board

Figure 3.14 shows the completely assembled single display system of
TCC803x EVB.

![](media/image56.png){width="5.088392388451443in"
height="2.812555774278215in"}

[]{#_Ref112161493 .anchor}Figure 3.14 Assembled Single Display System of
TCC803x EVB

# Build Guide

## SDK Build Preparation 

Linux_YP4.0_IVI is based on the Yocto Project 4.0 Kirkstone. Therefore,
the Yocto Project environment must be set on the host PC to use the
Linux_YP4.0_IVI. To download SDK, source-mirror, and tools, you must
install utilities.

## Yocto Project

The Yocto Project is an open source project that focuses on embedded
Linux development.

It uses a combination of Open Embedded project, which is Poky, and
***bitbake*** as the build system to make Linux images.

By using Yocto Project, you can simultaneously build the bootloader,
kernel, and rootfs.

## Task Process

Figure 4.1 shows the task process of Yocto Project. You can download the
source from the upstream based on the metadata and build it. When the
build is completed, package, image, and SDK are provided as results.

![](media/image57.wmf){width="6.876388888888889in"
height="3.370138888888889in"}

[]{#_Ref40969045 .anchor}Figure 4.1 Yocto Project Development Process

## Yocto Project Installation

### Linux Distribution Versions Supported by Yocto Project

The following Linux distribution versions are supported. Other
distribution versions have [not]{.underline} passed the verification
process in Yocto project.

For details, refer to the following Yocto Project website:

- <https://docs.yoctoproject.org/kirkstone/ref-manual/system-requirements.html#supported-linux-distributions>

<!-- -->

- Ubuntu 20.04 (LTS)

- Ubuntu 22.04 (LTS)

- Fedora 38

- Debian GNU/Linux 11.x (Bullseye)

- AlmaLinux 8

### List of Packages Required for Host Development System to use Yocto Project

The mandatory packages must be installed on Host System (individual
computer or development server) to use Yocto Project.

For details, refer to the following Yocto Project website:

- 
- 

[https://docs.yoctoproject.org/kirkstone/ref-manual/system-requirements.html#required-packages-for-the-build-host](https://docs.yoctoproject.org/kirkstone/ref-manual/system-requirements.html#required-packages-for-the-build-host )

## Install Utilities

### repo

You can download the Linux_YP4.0_IVI through Android ***repo***.

To install the ***repo,*** refer to the following website:
<https://gerrit.googlesource.com/git-repo/>.

If ***repo*** is already installed, you can use it without
re-installation.

### NcFTP

***NcFTP*** is a browser program for the File Transfer Protocol. It is
required to download tools from Telechips' FTP server.

For details on ***NcFTP***, refer to the following website:
<http://www.NcFTP.com/ncftp>.

## Linux_YP4.0_IVI

Use ***autolinux*** to download and build the Linux_YP4.0_IVI SDK.

- ***autolinux*** (python script to automatically download and build the
  SDK)

### Composition of Linux_YP4.0_IVI

Once the download is completed, you can check the following items.

+---+----------+----------+-------------------------------------------+
| * |          |          | **Description**                           |
| * |          |          |                                           |
| I |          |          |                                           |
| t |          |          |                                           |
| e |          |          |                                           |
| m |          |          |                                           |
| * |          |          |                                           |
| * |          |          |                                           |
+:=:+:========:+:========:+===========================================+
| p | meta     |          | > Yocto Project 4.0 Kirkstone build       |
| o |          |          | > system                                  |
| k |          |          |                                           |
| y |          |          |                                           |
+---+----------+----------+-------------------------------------------+
|   | m        |          |                                           |
|   | eta-poky |          |                                           |
+---+----------+----------+-------------------------------------------+
|   | meta-y   |          |                                           |
|   | octo-bsp |          |                                           |
+---+----------+----------+-------------------------------------------+
|   | meta-arm |          | > Supports Arm toolchain Layer            |
+---+----------+----------+-------------------------------------------+
|   | meta-qt5 |          | > Supports Qt5 5.6.3 Layer                |
+---+----------+----------+-------------------------------------------+
|   | me       |          | > Supports packages to avoid GPLv3        |
|   | ta-gplv2 |          | > license                                 |
+---+----------+----------+-------------------------------------------+
|   | me       |          | > Supports Telechips BSP Layer            |
|   | ta-telec |          |                                           |
|   | hips-bsp |          |                                           |
+---+----------+----------+-------------------------------------------+
|   | meta-t   | m        | > Recipes that require modification from  |
|   | elechips | eta-core | > Open Source Software (OSS) used by      |
|   |          |          | > Telechips Linux_YP4.0_IVI or recipes    |
|   |          |          | > that are not in Yocto Project 4.0       |
+---+----------+----------+-------------------------------------------+
|   |          | me       | > OSS Layer that is added by Telechips    |
|   |          | ta-extra |                                           |
+---+----------+----------+-------------------------------------------+
|   |          | meta-qt5 | > Supports Qt5 to support Telechips GUI   |
|   |          |          | > application                             |
+---+----------+----------+-------------------------------------------+
|   |          | meta-ivi | > Configuration package and example       |
|   |          |          | > programs of In-vehicle Infotainment     |
|   |          |          | > (IVI)                                   |
+---+----------+----------+-------------------------------------------+
|   |          | meta     | > Configuration package and example       |
|   |          | -subcore | > programs on sub-core                    |
+---+----------+----------+-------------------------------------------+
|   | dow      |          | > Script for downloading source-mirror    |
|   | nload.sh |          | > and tools                               |
+---+----------+----------+-------------------------------------------+
| s |          |          | > Local repository for building the basic |
| o |          |          | > class of Linux_YP4.0_IVI                |
| u |          |          |                                           |
| r |          |          |                                           |
| c |          |          |                                           |
<<<<<<< HEAD
| e |          |          |                                           |
| - |          |          |                                           |
| m |          |          |                                           |
| i |          |          |                                           |
| r |          |          |                                           |
| r |          |          |                                           |
| o |          |          |                                           |
| r |          |          |                                           |
+---+----------+----------+-------------------------------------------+
| f |          |          | > FWDN execute file                       |
| w |          |          | >                                         |
| d |          |          | > VTC driver                              |
| n |          |          | >                                         |
| _ |          |          | > Source code                             |
| v |          |          |                                           |
| 8 |          |          |                                           |
+---+----------+----------+-------------------------------------------+
| m |          |          | > mktcimg execute file                    |
| k |          |          | >                                         |
| t |          |          | > Source code                             |
| c |          |          |                                           |
| i |          |          |                                           |
| m |          |          |                                           |
| g |          |          |                                           |
+---+----------+----------+-------------------------------------------+
| b |          |          | > Boot-firmware files                     |
| o |          |          | >                                         |
| o |          |          | > Tools to make images for boot-firmware  |
| t |          |          |                                           |
| - |          |          |                                           |
| f |          |          |                                           |
| i |          |          |                                           |
| r |          |          |                                           |
| m |          |          |                                           |
| w |          |          |                                           |
| a |          |          |                                           |
| r |          |          |                                           |
| e |          |          |                                           |
| _ |          |          |                                           |
| t |          |          |                                           |
| c |          |          |                                           |
| c |          |          |                                           |
| 8 |          |          |                                           |
| 0 |          |          |                                           |
| 3 |          |          |                                           |
| x |          |          |                                           |
+---+----------+----------+-------------------------------------------+
| T |          |          | > Yocto Project 4.0 Kirkstone             |
| o |          |          | > *buildtools*                            |
| o |          |          |                                           |
| l |          |          | - x86_                                    |
| s |          |          | 64-buildtools-nativesdk-standalone-4.0.sh |
|   |          |          |                                           |
|   |          |          | - x86_64-buildt                           |
|   |          |          | ools-extended-nativesdk-standalone-4.0.sh |
+---+----------+----------+-------------------------------------------+
=======

| e                                                            |      |      |                                           |
| ------------------------------------------------------------ | ---- | ---- | ----------------------------------------- |
| m                                                            |      |      |                                           |
| i                                                            |      |      |                                           |
| r                                                            |      |      |                                           |
| r                                                            |      |      |                                           |
| o                                                            |      |      |                                           |
| r                                                            |      |      |                                           |
| +---+----------+----------+-------------------------------------------+ |      |      |                                           |
| f                                                            |      |      | > FWDN execute file                       |
| w                                                            |      |      | >                                         |
| d                                                            |      |      | > VTC driver                              |
| n                                                            |      |      | >                                         |
| _                                                            |      |      | > Source code                             |
| v                                                            |      |      |                                           |
| 8                                                            |      |      |                                           |
| +---+----------+----------+-------------------------------------------+ |      |      |                                           |
| m                                                            |      |      | > mktcimg execute file                    |
| k                                                            |      |      | >                                         |
| t                                                            |      |      | > Source code                             |
| c                                                            |      |      |                                           |
| i                                                            |      |      |                                           |
| m                                                            |      |      |                                           |
| g                                                            |      |      |                                           |
| +---+----------+----------+-------------------------------------------+ |      |      |                                           |
| b                                                            |      |      | > Boot-firmware files                     |
| o                                                            |      |      | >                                         |
| o                                                            |      |      | > Tools to make images for boot-firmware  |
| t                                                            |      |      |                                           |
| -                                                            |      |      |                                           |
| f                                                            |      |      |                                           |
| i                                                            |      |      |                                           |
| r                                                            |      |      |                                           |
| m                                                            |      |      |                                           |
| w                                                            |      |      |                                           |
| a                                                            |      |      |                                           |
| r                                                            |      |      |                                           |
| e                                                            |      |      |                                           |
| _                                                            |      |      |                                           |
| t                                                            |      |      |                                           |
| c                                                            |      |      |                                           |
| c                                                            |      |      |                                           |
| 8                                                            |      |      |                                           |
| 0                                                            |      |      |                                           |
| 3                                                            |      |      |                                           |
| x                                                            |      |      |                                           |
| +---+----------+----------+-------------------------------------------+ |      |      |                                           |
| T                                                            |      |      | > Yocto Project 4.0 Kirkstone             |
| o                                                            |      |      | > *buildtools*                            |
| o                                                            |      |      |                                           |
| l                                                            |      |      | - x86_                                    |
| s                                                            |      |      | 64-buildtools-nativesdk-standalone-4.0.sh |
|                                                              |      |      |                                           |
|                                                              |      |      | - x86_64-buildt                           |
|                                                              |      |      | ools-extended-nativesdk-standalone-4.0.sh |
| +---+----------+----------+-------------------------------------------+ |      |      |                                           |
>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b

### Autolinux

***autolinux*** was developed by Telechips to make it easier for you to
download and build the SDK.

It does not provide all settings and functions, so you should refer to
Chapter 4.6.3 for detailed configurations.

#### Download Autolinux

You can download the ***autolinux*** script from git repository.

+-----------------------------------------------------------------------+
| **\~/release\$ git clone                                              |
| ssh://git.telechips.com/linux_ivi/script/build-autolinux\             |
| \~/release\$ cd build-autolinux\                                      |
| \~/release/build-autolinux\$ git checkout linux_yp4.0_ivi_1.0.0\      |
| \~/release/build-autolinux\$ tree**                                   |
|                                                                       |
| > .                                                                   |
| >                                                                     |
| > ├── autolinux                                                       |
| >                                                                     |
| > ├── classes                                                         |
| >                                                                     |
| > │   ├── feature.py                                                  |
| >                                                                     |
| > │   └── features                                                    |
| >                                                                     |
| > │   ├── cluster.py                                                  |
| >                                                                     |
| > │   ├── common.py                                                   |
| >                                                                     |
| > │   └── ivi.py                                                      |
| >                                                                     |
| > ├── doc                                                             |
| >                                                                     |
| > │   └── variable.txt                                                |
| >                                                                     |
| > ├── README                                                          |
| >                                                                     |
| > ├── script                                                          |
| >                                                                     |
| > │   ├── bitbake-layers.sh                                           |
| >                                                                     |
| > │   ├── build_configure.sh                                          |
| >                                                                     |
| > │   ├── build_image.sh                                              |
| >                                                                     |
| > │   └── devtool.sh                                                  |
| >                                                                     |
| > └── template                                                        |
| >                                                                     |
| > ├── linux_ivi.py                                                    |
| >                                                                     |
| > ├── sdk.py                                                          |
| >                                                                     |
| > ├── tcc803x_linux_cluster.py                                        |
| >                                                                     |
| > ├── tcc803x_linux_ivi_jvckenwood.py                                 |
| >                                                                     |
| > ├── tcc803x_linux_ivi_litbig.py                                     |
| >                                                                     |
| > ├── tcc803x_linux_ivi.py                                            |
| >                                                                     |
| > ├── tcc805x_linux_cluster.py                                        |
| >                                                                     |
| > ├── tcc805x_linux_ivi.py                                            |
| >                                                                     |
| > ├── tcc807x_linux_ivi_pre_release.py                                |
| >                                                                     |
| > ├── tcc807x_linux_ivi.py                                            |
| >                                                                     |
| > └── tcc897x_linux_cluster.py                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

#### Composition of Autolinux

+------+-------+--------+--------------------------------------------+
| **Fi |       |        | **Description**                            |
| le** |       |        |                                            |
+:====:+:=====:+:======:+============================================+
| a    |       |        | Python script to automatically download    |
| utol |       |        | and build the SDK                          |
| inux |       |        |                                            |
+------+-------+--------+--------------------------------------------+
| cla  | featu |        | Python class for SDK features              |
| sses | re.py |        |                                            |
+------+-------+--------+--------------------------------------------+
|      | fea   | clus   | File that defines supported cluster        |
|      | tures | ter.py | features                                   |
+------+-------+--------+--------------------------------------------+
|      |       | com    | File that defines supported common         |
|      |       | mon.py | features                                   |
+------+-------+--------+--------------------------------------------+
|      |       | ivi.py | File that defines supported IVI features   |
+------+-------+--------+--------------------------------------------+
| doc  | va    |        | Document that describes the variables used |
|      | riabl |        | in ***autolinux***                         |
|      | e.txt |        |                                            |
+------+-------+--------+--------------------------------------------+
| RE   |       |        | Document that describes ***autolinux***    |
| ADME |       |        |                                            |
+------+-------+--------+--------------------------------------------+
| sc   | bi    |        | Shell script to execute                    |
| ript | tbake |        | ***bitbake-layers*** in ***autolinux***    |
|      | -laye |        |                                            |
|      | rs.sh |        |                                            |
+------+-------+--------+--------------------------------------------+
|      | bui   |        | Shell script to execute ***configure*** in |
|      | ld_co |        | ***autolinux***                            |
|      | nfigu |        |                                            |
|      | re.sh |        |                                            |
+------+-------+--------+--------------------------------------------+
|      | buil  |        | Shell script to execute ***bitbake*** in   |
|      | d_ima |        | ***autolinux***                            |
|      | ge.sh |        |                                            |
+------+-------+--------+--------------------------------------------+
|      | devto |        | Shell script to execute ***devtool*** in   |
|      | ol.sh |        | ***autolinux***                            |
+------+-------+--------+--------------------------------------------+
| temp | li    |        | File that defines supported machines and   |
| late | nux_i |        | manifests for Linux_YP4.0_IVI SDK          |
|      | vi.py |        |                                            |
+------+-------+--------+--------------------------------------------+
|      | s     |        | File that defines supported SDKs, source   |
|      | dk.py |        | mirror, and build tool paths               |
+------+-------+--------+--------------------------------------------+
|      | Other |        | File that defines supported machines and   |
|      | files |        | manifests for other SDKs                   |
|      |       |        |                                            |
|      |       |        | These files are used by other SDKs         |
+------+-------+--------+--------------------------------------------+

#### Autolinux Usage

+-----------------------------------------------------------------------+
| **\~/release/build-autolinux\$ ./autolinux \--help**                  |
|                                                                       |
| **usage: autolinux \[-h\] -c COMMAND \[COMMAND \...\] \[-V\] \[-s     |
| SDK\] \[-m MACHINE\]\                                                 |
| \[-x MANIFEST\] \[-f FEATURES \[FEATURES \...\]\]\                    |
| \[-sf SUBFEATURES \[SUBFEATURES \...\]\] \[\--skip-ftp\]**            |
|                                                                       |
| Linux SDK Configurations                                              |
|                                                                       |
| **optional arguments:\                                                |
| ** **-h**, **\--help** show this help message and exit                |
|                                                                       |
| **General Command:**                                                  |
|                                                                       |
| **-c** COMMAND \[COMMAND \...\], **\--command** COMMAND \[COMMAND     |
| \...\]\                                                               |
| General Command to use autolinux(required option)\                    |
| -commands-\                                                           |
| **update**: sync to recipes matched manifest.xml, Be careful local    |
| changes will be lost\                                                 |
| **configure** \[option\] \[name\]: setup the newer build environment\ |
| conf_opt arg : addtionally set configuration options\                 |
| refers to 'Configuration Options'\                                    |
| Ex) autolinux -c configure -m tcc8050-main\                           |
| save \[name\] : save autolinux.config file to .config/\               |
| load \[name\] : load configure file from .config/\                    |
| **clean** \[option\]: move current built files to recycle directory.  |
| Recycle dir:build/delete\                                             |
| old : delete current built files and recycle directory.\              |
| all : delete total build directory\                                   |
| **build** \[option\]: build SDK Image, choose the name of the image   |
| to build\                                                             |
| \'args\' : extra command strings\                                     |
| Ex) autolinux -c build \"linux-telechips -C compile\"**\              |
| ** sub \'args\' : building on sub-core, available only when the       |
| with-subcore option is enabled\                                       |
| Ex) autolinux -c build sub \"linux-telechips -C compile\"\            |
| **devtool** \[option\] : devtool package to develop easily**\         |
| ** \'args\' : extra command strings\                                  |
| Ex) autolinux -c devtool \'modify linux-telechips\                    |
| sub \'args\' : devtool on sub-core\                                   |
| Ex) autolinux -c sub devtool \'modify linux-telechips\'\              |
| **layers** \[option\] : bitbake-layers command\                       |
| \'args\' : extra command strings\                                     |
| Ex) autolinux -c layers add-layer \'poky/meta-telechips/meta-ivi\'\   |
| sub \'args\' : building on sub-core, available only when the          |
| with-subcore option is enabled\                                       |
| Ex) autolinux -c sub layers add-layer                                 |
| \'poky/meta-telechips/meta-ivi/meta-ivi-subcore\'\                    |
| **make_fai** : make SDdata.fai for fwdn\                              |
| **make_updatedir** \[option\] : make update directory for update\     |
| main : make only on the main core\                                    |
| sub : make only on the sub core\                                      |
| **chk_security** : make csv file for whether or not memory protection |
| technology\                                                           |
| **info** : show information of current configuration\                 |
| **modify** option: modify specific configure at current set-up\       |
| feature : modify features\                                            |
| sub-feature : modify subcore features\                                |
| image : modify image                                                  |
|                                                                       |
| **-V**, **\--version** print version and exit                         |
|                                                                       |
| **Configuration Options:**                                            |
|                                                                       |
| -s SDK, \--sdk SDK enter the sdk to download\                         |
| sdk lists\                                                            |
| ivi :\[\'linux_ivi\', \'tcc803x_linux_ivi\', \'tcc805x_linux_ivi\',   |
| \'tcc807x_linux_ivi\'\]                                               |
|                                                                       |
| cluster :\[\'tcc897x_linux_cluster\', \'tcc803x_linux_cluster\',      |
| \'tcc805x_linux_cluster\'\]\                                          |
| -m MACHINE, \--machine MACHINE\                                       |
| enter the machine to build\                                           |
| -x MANIFEST, \--manifest MANIFEST\                                    |
| enter the manifest to build\                                          |
| -f FEATURES \[FEATURES \...\], \--features FEATURES \[FEATURES        |
| \...\]\                                                               |
| enter the feature list\                                               |
| Ex) -f with-subcore gpu-vz meta-update\                               |
| -sf SUBFEATURES \[SUBFEATURES \...\], \--sub-features SUBFEATURES     |
| \[SUBFEATURES \...\]\                                                 |
| enter the subfeature list\                                            |
| Ex) -sf rvc gpu-vz meta-update                                        |
|                                                                       |
| **Environment Options:**                                              |
|                                                                       |
| **\--skip-ftp** Skip to download from Telechips FTP Server            |
+=======================================================================+
+-----------------------------------------------------------------------+

#### Download and Configure SDK

Linux_YP4.0_IVI is downloaded during the initial configuration.

You can set up the initial configuration by using a configure command.
If you execute the configure command, the initial configuration is
progressed as the following four steps.

**Note:** Each step is activated only when there is at least one
selectable option.

1.  **Choose the Platform** and **SDK**.

2.  **Choose the manifest** **to repo**.

    - This step is not activated in the current version of Linux
      YP4.0_IVI because there is no selection option

3.  **Choose a Machine to build**.

4.  **Choose the features** to build.

When the configuration is completed, the set-up is saved as an
"autolinux.config".

The following is an example of TCC8030.

+-----------------------------------------------------------------------+
| **\~/release/build-autolinux\$ ./autolinux -c configure**             |
|                                                                       |
| **The command is configure or Add configuration                       |
| options(sdk,machine,manifest)**                                       |
|                                                                       |
| **Configure Start**                                                   |
|                                                                       |
| **Choose the Platform**                                               |
|                                                                       |
| 1.cluster                                                             |
|                                                                       |
| 2.ivi                                                                 |
|                                                                       |
| Select SDK(1-2): 2\                                                   |
| **Choose the SDK to download**                                        |
|                                                                       |
| 1.linux_ivi                                                           |
|                                                                       |
| 2.tcc803x_linux_ivi                                                   |
|                                                                       |
| 3.tcc805x_linux_ivi                                                   |
|                                                                       |
| 4.tcc807x_linux_ivi                                                   |
|                                                                       |
| Select SDK(1-4): 1                                                    |
|                                                                       |
| **Choose a Machine to build**                                         |
|                                                                       |
| 1.tcc8030-main                                                        |
|                                                                       |
| 2.tcc8050-main                                                        |
|                                                                       |
| 3.tcc8053-main                                                        |
|                                                                       |
| 4.tcc8059-main                                                        |
|                                                                       |
| 5.tcc8070-main                                                        |
|                                                                       |
| 6.tcc8030-sub                                                         |
|                                                                       |
| 7.tcc8050-sub                                                         |
|                                                                       |
| 8.tcc8053-sub                                                         |
|                                                                       |
| 9.tcc8059-sub                                                         |
|                                                                       |
| 10.tcc8070-sub                                                        |
|                                                                       |
| Choose Machine(1-10): 1                                               |
|                                                                       |
| **Choose the Features at tcc8030-main // \"\*\" means selected        |
| feature**                                                             |
|                                                                       |
| 1\. bootchart Install bootchart                                       |
|                                                                       |
| 2\. network Install network packages                                  |
|                                                                       |
| 3\. optee Using OPTEE                                                 |
|                                                                       |
| \* 4. with-subcore Booting with sub-core                              |
|                                                                       |
| \* 5. support-4k-video Support 4k Video Contents                      |
|                                                                       |
| 6\. booting-animation Enable Booting Animation                        |
|                                                                       |
| \* 7. meta-update Enable Update                                       |
|                                                                       |
| \* 8. meta-micom Enable Micom                                         |
|                                                                       |
| 0.Exit                                                                |
|                                                                       |
| Choose Features enable/disable (1-8): 0                               |
|                                                                       |
| **Choose the Features at tcc8030-sub**                                |
|                                                                       |
| **// In case \"with-subcore\" enabled in features, sub-core\'s        |
| feature select step activated.**                                      |
|                                                                       |
| 1\. network Install network packages                                  |
|                                                                       |
| \* 2. rvc Enable Rear Camera                                          |
|                                                                       |
| \* 3. meta-update Enable Update                                       |
|                                                                       |
| \* 4. meta-micom Enable Micom                                         |
|                                                                       |
| 0.Exit                                                                |
|                                                                       |
| Choose Features enable/disable (1-4): 0                               |
|                                                                       |
| \...                                                                  |
|                                                                       |
| \...                                                                  |
|                                                                       |
| tools/x86_64-buildtools-extended-nativesdk-standalone-4.0.sh          |
|                                                                       |
| tools/x86_64-buildtools-nativesdk-standalone-4.0.sh                   |
|                                                                       |
| **Do you want to build tools installer version 4.0? (y/n):** y        |
|                                                                       |
| Extended Build tools installer version 4.0                            |
|                                                                       |
| ==========================================                            |
|                                                                       |
| **You are about to install the SDK to                                 |
| \"/home/release/build-autolinux/buildtools/4.0\". Proceed \[Y/n\]?**  |
| Y                                                                     |
|                                                                       |
| Extracting SDK\...\...\...\...\...\...done                            |
|                                                                       |
| Setting it up\...done                                                 |
|                                                                       |
| SDK has been successfully set up and is ready to be used.             |
|                                                                       |
| Each time you wish to use the SDK in a new shell session, you need to |
| source the environment setup script e.g.                              |
|                                                                       |
| \$ .                                                                  |
| /home/release/                                                        |
| build-autolinux/buildtools/4.0/environment-setup-x86_64-pokysdk-linux |
|                                                                       |
| Enabled with-subcore, The autolinux script makes new configuration    |
| files of Sub-core automatically                                       |
|                                                                       |
| ===========                                                           |
| ===================================================================== |
|                                                                       |
| **SDK=linux_ivi**                                                     |
|                                                                       |
| **MANIFEST=linux_yp4.0_ivi_1.0.0.xml**                                |
|                                                                       |
| **DATE=2024/05/31**                                                   |
|                                                                       |
| **MACHINE=tcc8030-main**                                              |
|                                                                       |
| **VERSION=release**                                                   |
|                                                                       |
| **FEATURES=with-subcore,support-4k-video,meta-micom,meta-update**     |
|                                                                       |
| **SUBFEATURES=rvc,meta-micom,meta-update**                            |
|                                                                       |
| ===========                                                           |
| ===================================================================== |
|                                                                       |
| **\~/release/build-autolinux\$ ls**                                   |
|                                                                       |
| autolinux\* boot-firmware_tcc803x/ build/ classes/ fwdn_v8/ poky/     |
| release-info/ source-mirror/ tools/ autolinux.config                  |
| boot-firmware_tcc805x/ boot-firmware_tcc807x/ buildtools/ doc/        |
| mktcimg/ README script/ template/                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

##### Configure Command with Extra Options

The configure command can be used with the following three extra
options.

- **Configuration Options**

+-----------------------------------------------------------------------+
| **\~/release/build-autolinux\$ ./autolinux \--help**                  |
|                                                                       |
| \...                                                                  |
|                                                                       |
| **Configuration Options:**\                                           |
| -s SDK, \--sdk SDK enter the sdk to download\                         |
| sdk lists\                                                            |
| ivi :\[\'linux_ivi\', \'tcc803x_linux_ivi\', \'tcc805x_linux_ivi\',   |
| \'tcc807x_linux_ivi\'\]\                                              |
| cluster :\[\'tcc897x_linux_cluster\', \'tcc803x_linux_cluster\',      |
| \'tcc805x_linux_cluster\'\]\                                          |
| -m MACHINE, \--machine MACHINE\                                       |
| enter the machine to build\                                           |
| -x MANIFEST, \--manifest MANIFEST\                                    |
| enter the manifest to build\                                          |
| -f FEATURES \[FEATURES \...\], \--features FEATURES \[FEATURES        |
| \...\]\                                                               |
| enter the feature list\                                               |
| ex) -f with-subcore gpu-vz meta-update\                               |
| -sf SUBFEATURES \[SUBFEATURES \...\], \--sub-features SUBFEATURES     |
| \[SUBFEATURES \...\]\                                                 |
| enter the subfeature list\                                            |
| ex) -sf rvc gpu-vz meta-update                                        |
|                                                                       |
| > \...                                                                |
+=======================================================================+
+-----------------------------------------------------------------------+

- **save:** Saves the "autolinux.config" to read the next configuration.

> If you append **save**, "autolinux.config" is saved as machine name in
> the .config path.

+-----------------------------------------------------------------------+
| **\~/release/build-autolinux\$ ./autolinux -c configure save**        |
|                                                                       |
| > \...                                                                |
| >                                                                     |
| > tcc8030-main.config save successful                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

- **load:** Loads the configuration files saved as **save** in the
  .config path.

  If you append **load**, the **Choose a configure to load** menu is
  activated.

+-----------------------------------------------------------------------+
| **\~/release/build-autolinux\$ ./autolinux -c configure load**        |
|                                                                       |
| **Choose a configure to load**                                        |
|                                                                       |
| 1.  tcc8030-main.config                                               |
|                                                                       |
| Select Config(1-1): 1                                                 |
|                                                                       |
| > tcc8030-main.config load successful                                 |
| >                                                                     |
| > \...                                                                |
+=======================================================================+
+-----------------------------------------------------------------------+

#### Build Linux_YP4.0_IVI 

Enter **build** command to start building the SDK. The menu is activated
only when there are at least two images to be built. The way the
**build** command works is the same as ***bitbake***.

-----------------------------------------------------------------------
<<<<<<< HEAD
=======

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
  **\~/release/build-autolinux\$ ./autolinux -c build\
  **Read configuration from autolinux.config\
  **\
  Choose an Image to build**\
  1.telechips-ivi-image-minimal\
  2.telechips-ivi-image-multimedia\
  3.telechips-ivi-image\
  4.automotive-linux-platform-image\
<<<<<<< HEAD
=======

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
  Choose Image (1-4):4
  
  -----------------------------------------------------------------------

-----------------------------------------------------------------------

##### Result of Building SDK

The following is an example of TCC8030.

+-----------------------------------------------------------------------+
| Enabled with-subcore, The autolinux script build Sub-core Image       |
| automatically in background                                           |
|                                                                       |
| NOTE: Your conf/bblayers.conf has been automatically updated.         |
|                                                                       |
| Parsing recipes: 100%                                                 |
| \|#######################################################\| Time:     |
| 0:00:40                                                               |
|                                                                       |
| Parsing of 1090 .bb files complete (0 cached, 1090 parsed). 1739      |
| targets, 266 skipped, 0 masked, 0 errors.                             |
|                                                                       |
| NOTE: Resolving any missing task queue dependencies                   |
|                                                                       |
| Build Configuration:                                                  |
|                                                                       |
| BB_VERSION = \"2.0.0\"                                                |
|                                                                       |
| BUILD_SYS = \"x86_64-linux\"                                          |
|                                                                       |
| NATIVELSBSTRING = \"universal\"                                       |
|                                                                       |
| TARGET_SYS = \"aarch64-telechips-linux\"                              |
|                                                                       |
| MACHINE = \"tcc8030-main\"                                            |
|                                                                       |
| DISTRO = \"poky-telechips-systemd\"                                   |
|                                                                       |
| DISTRO_VERSION = \"4.0.17\"                                           |
|                                                                       |
| TUNE_FEATURES = \"aarch64 armv8a crc cortexa53\"                      |
|                                                                       |
| TARGET_FPU = \"\"                                                     |
|                                                                       |
| LINUX_VERSION = \"5.10.205\"                                          |
|                                                                       |
| KBUILD_DEFCONFIG = \"tcc803x_ivi_defconfig\"                          |
|                                                                       |
| IMAGE_FEATURES = \" debug-tweaks read-only-rootfs\"                   |
|                                                                       |
| GCCVERSION = \"arm-11.2\"                                             |
|                                                                       |
| GLIBCVERSION = \"2.35%\"                                              |
|                                                                       |
| INVITE_PLATFORM = \" with-subcore multimedia support-4k-video         |
| qt5/wayland micom fw-update genivi\"                                  |
|                                                                       |
| meta                                                                  |
|                                                                       |
| meta-poky                                                             |
|                                                                       |
| \...                                                                  |
|                                                                       |
| \...                                                                  |
|                                                                       |
| \...                                                                  |
|                                                                       |
| Summary: There was 1 WARNING message shown.                           |
|                                                                       |
| ===========                                                           |
| ===================================================================== |
|                                                                       |
| **Built Images Path :                                                 |
| /home/releas                                                          |
| e/build-autolinux/build/tcc8030-main/tmp/deploy/images/tcc8030-main** |
|                                                                       |
| **Built Images Path :                                                 |
| /home/rele                                                            |
| ase/build-autolinux/build/tcc8030-sub/tmp/deploy/images/tcc8030-sub** |
|                                                                       |
| ===========                                                           |
| ===================================================================== |
+=======================================================================+
+-----------------------------------------------------------------------+

##### Build Command with Additional Arguments (Optional)

The **build** command can be used with additional arguments (string
argument).

- String argument

> The **build** command supports a string argument for building the
> specific packages. The specific packages are built based on the
> machine stored in "autolinux.config".

-----------------------------------------------------------------------
<<<<<<< HEAD
  **\~/release/build-autolinux\$ ./autolinux -c build \"linux-telechips
=======

  **\~/release/build-autolinux\$ ./autolinux -c build \"linux-telechips

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
  -c compile\"**
  
  -----------------------------------------------------------------------

-----------------------------------------------------------------------

- Sub + string argument

> The **build** command supports a string argument for building the
> specific packages on the sub-machine. This **build** command requires
> **with-subcore** feature enabled.

-----------------------------------------------------------------------
<<<<<<< HEAD
  **\~/release/build-autolinux\$ ./autolinux -c build sub
=======

  **\~/release/build-autolinux\$ ./autolinux -c build sub

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
  \"linux-telechips -c compile\"**
  
  -----------------------------------------------------------------------

-----------------------------------------------------------------------

#### Make "SD_Data.fai" to download Firmware

Enter **make_fai** command to make "SD_Data.fai". The **make_fai**
command is based on the image defined in "autolinux.config".

+-----------------------------------------------------------------------+
| **\~/release/build-autolinux\$ ./autolinux -c make_fai**              |
|                                                                       |
| \...                                                                  |
|                                                                       |
| ===========                                                           |
| ===================================================================== |
|                                                                       |
| **FWDN Path :                                                         |
| /home/release/build-autolinux/build/tcc8030-main/tmp/deploy/fwdn**    |
|                                                                       |
| ===========                                                           |
| ===================================================================== |
|                                                                       |
| **\~/release/build-autolinux\$ ls                                     |
| build/tcc8030-main/tmp/deploy/fwdn**                                  |
|                                                                       |
| boot-firmware partition.list SD_Data.fai SD_Data.gpt SD_Data.gpt.back |
| SD_Data.gpt.prim                                                      |
+=======================================================================+
+-----------------------------------------------------------------------+

**Note: make_fai** command is described in Chapter 5.2.2.

#### Other Commands and Options

##### Clean

The **clean** command is related to removing build history.

- **clean:** Moves the currently built files to the recycle directory.
  The recycle directory path is as follows: "build/delete/#"

+-----------------------------------------------------------------------+
| **\~/release/build-autolinux\$ ./autolinux -c clean**                 |
|                                                                       |
| Read configuration from autolinux.config                              |
|                                                                       |
| deleted target :                                                      |
|                                                                       |
| > /home/release/build-autolinux/build/tcc8030-main/                   |
|                                                                       |
| /home/release/build-autolinux/build/tcc8030-sub/                      |
|                                                                       |
| move current built files. recycle dir:build/delete/0                  |
+=======================================================================+
+-----------------------------------------------------------------------+

- **clean old:** Deletes the recycle directory.

+-----------------------------------------------------------------------+
| **\~/release/build-autolinux\$ ./autolinux -c clean old**             |
|                                                                       |
| delete recycle directory in background.                               |
+=======================================================================+
+-----------------------------------------------------------------------+

- **clean all:** Deletes the entire build directory including build
  history. Therefore, when you rebuild the SDK after executing the
  **clean all** command, the build time takes a long time.

> **Note**: After **clean all**, you must **configure** again.

+-----------------------------------------------------------------------+
| **\~/release/build-autolinux\$ ./autolinux -c clean all**             |
|                                                                       |
| All build directories will be deleted. Are you sure you want to       |
| delete it? (y/n): y                                                   |
|                                                                       |
| delete total build directory. It takes a long time in background!!    |
|                                                                       |
| **\~/release/build-autolinux\$ ./autolinux -c configure**             |
+=======================================================================+
+-----------------------------------------------------------------------+

##### Modify

The **modify** command modifies the already configured
"autolinux.config".

- **modify feature:** Modifies the feature.

> If the **with-subcore** feature is disabled, only the main core
> feature is modified.

+-----------------------------------------------------------------------+
| **\~/release/build-autolinux\$ ./autolinux -c modify feature**        |
|                                                                       |
| Read configuration from autolinux.config                              |
|                                                                       |
| **Choose the Features at tcc8030-main**                               |
|                                                                       |
| 1\. bootchart Install bootchart                                       |
|                                                                       |
| 2\. network Install network packages                                  |
|                                                                       |
| 3\. optee Using OPTEE                                                 |
|                                                                       |
| \* 4. with-subcore Booting with sub-core                              |
|                                                                       |
| \* 5. support-4k-video Support 4k Video Contents                      |
|                                                                       |
| 6\. booting-animation Enable Booting Animation                        |
|                                                                       |
| \* 7. meta-update Enable Update                                       |
|                                                                       |
| \* 8. meta-micom Enable Micom                                         |
|                                                                       |
| 0.Exit                                                                |
|                                                                       |
| Choose Features enable/disable (1-8): 0                               |
|                                                                       |
| **Choose the Features at tcc8030-sub**                                |
|                                                                       |
| 1\. network Install network packages                                  |
|                                                                       |
| \* 2. rvc Enable Rear Camera                                          |
|                                                                       |
| \* 3. meta-update Enable Update                                       |
|                                                                       |
| \* 4. meta-micom Enable Micom                                         |
|                                                                       |
| 0.Exit                                                                |
|                                                                       |
| Choose Features enable/disable (1-4): 0                               |
|                                                                       |
| ===========                                                           |
| ===================================================================== |
|                                                                       |
| **\...**                                                              |
|                                                                       |
| **FEATURES=with-subcore,support-4k-video,meta-micom,meta-update**     |
|                                                                       |
| **SUBFEATURES=rvc,meta-micom,meta-update**                            |
|                                                                       |
| **\...**                                                              |
|                                                                       |
| ===========                                                           |
| ===================================================================== |
|                                                                       |
| Modify feature Successful                                             |
+=======================================================================+
+-----------------------------------------------------------------------+

- **modify sub-feature**: Modifies the sub-feature. To modify the
  sub-feature, the feature must include **with-subcore**.

+-----------------------------------------------------------------------+
| **\~/release/build-autolinux\$ ./autolinux -c modify sub-feature**    |
|                                                                       |
| Read configuration from autolinux.config                              |
|                                                                       |
| **Choose the Features at tcc8030-sub**                                |
|                                                                       |
| \* 1. rvc Enable Rear Camera                                          |
|                                                                       |
| \* 2. meta-update Enable Update                                       |
|                                                                       |
| \* 3. meta-micom Enable Micom                                         |
|                                                                       |
| 0.Exit                                                                |
|                                                                       |
| Choose Features enable/disable (1-3): 0                               |
|                                                                       |
| ===========                                                           |
| ===================================================================== |
|                                                                       |
| **\...**                                                              |
|                                                                       |
| **SUBFEATURES=rvc,meta-micom,meta-update**                            |
|                                                                       |
| **\...**                                                              |
|                                                                       |
| ===========                                                           |
| ===================================================================== |
|                                                                       |
| Modify sub-feature Successful                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

- **modify image**: Modifies an image. The menu is activated only when
  there are at least two images to be built.

+-----------------------------------------------------------------------+
| **\~/release/build-autolinux\$ ./autolinux -c modify image**          |
|                                                                       |
| Read configuration from autolinux.config                              |
|                                                                       |
| **Choose an Image to build**                                          |
|                                                                       |
| > 1.telechips-ivi-image-minimal                                       |
| >                                                                     |
| > 2.telechips-ivi-image-multimedia                                    |
|                                                                       |
| 3.telechips-ivi-image                                                 |
|                                                                       |
| 4.automotive-linux-platform-image                                     |
|                                                                       |
| Choose Image (1-4): 4                                                 |
|                                                                       |
| > ===                                                                 |
| ===================================================================== |
|                                                                       |
| **\...**                                                              |
|                                                                       |
| **IMAGE=automotive-linux-platform-image**                             |
|                                                                       |
| > ===                                                                 |
| ===================================================================== |
|                                                                       |
| Modify image Successful                                               |
+=======================================================================+
+-----------------------------------------------------------------------+

##### Devtool

***devtool*** is available in ***autolinux*** through **devtool**
command. For a detailed description of ***devtool***, see Chapter 4.7.3.

+-----------------------------------------------------------------------+
| **\~/release/build-autolinux\$ ./autolinux -c devtool \"modify        |
| linux-telechips\"**                                                   |
|                                                                       |
| Read configuration from autolinux.config                              |
|                                                                       |
| NOTE: Starting bitbake server\...                                     |
|                                                                       |
| \...                                                                  |
|                                                                       |
| \...                                                                  |
|                                                                       |
| INFO: Copying kernel config to workspace                              |
|                                                                       |
| INFO: Recipe linux-telechips now set up to build from                 |
| /home/release                                                         |
| /build-autolinux/build/tcc8030-main/workspace/sources/linux-telechips |
|                                                                       |
| **\~/release/build-autolinux\$**                                      |
+=======================================================================+
+-----------------------------------------------------------------------+

##### Update

The **update** command executes **repo sync** by using "manifest.xml"
that is set in "autolinux.config". (Any local changes are removed.)

+-----------------------------------------------------------------------+
| **\~/release/build-autolinux\$ ./autolinux -c update**                |
|                                                                       |
| Read configuration from autolinux.config                              |
|                                                                       |
| \...                                                                  |
|                                                                       |
| Sync Update Completed.                                                |
+=======================================================================+
+-----------------------------------------------------------------------+

### Detailed Configuration

This chapter explains how to change settings before building the SDK. It
also includes features provided by ***autolinux***.

> Set "local.conf" as follows according to the target board.
>
> For main core, local.conf file is located at
> ../build-autolinux/build/tcc8030-main/conf.

+:---------------:+:---------------:+:-------------------------------:+
| **Name of       | **Default       | **Description**                 |
| Variable**      | Value**         |                                 |
+-----------------+-----------------+---------------------------------+
| BB              | 8               | > Maximum number of tasks that  |
| _NUMBER_THREADS |                 | > can be run simultaneously     |
+-----------------+-----------------+---------------------------------+
| PARALLEL_MAKE   | -j 16           | > Option for make               |
+-----------------+-----------------+---------------------------------+
| MACHINE         | N/A             | > Select target board.          |
|                 |                 |                                 |
|                 |                 | - tcc8030-main                  |
+-----------------+-----------------+---------------------------------+
| EXTRA           | debug-tweaks    | > Image property selected       |
| _IMAGE_FEATURES |                 | > additionally                  |
|                 | r               | >                               |
|                 | ead-only-rootfs | > For detailed options, refer   |
|                 |                 | > to "local.conf".              |
+-----------------+-----------------+---------------------------------+
| CORE_IMAG       | NULL            | > Name of package to be         |
| E_EXTRA_INSTALL |                 | > installed additionally on     |
|                 |                 | > image                         |
+-----------------+-----------------+---------------------------------+
| DISTRO          | poky-te         | > Select SDK type.              |
|                 | lechips-systemd |                                 |
|                 |                 | - poky-telechips (sysvinit)     |
|                 |                 |                                 |
|                 |                 | - poky-telechips-systemd        |
|                 |                 |   (systemd)                     |
+-----------------+-----------------+---------------------------------+

> For sub-core, local.conf file is located at
> ../build-autolinux/build/tcc8030-sub/conf.

+:---------------:+:---------------:+:-------------------------------:+
| **Name of       | **Default       | **Description**                 |
| Variable**      | Value**         |                                 |
+-----------------+-----------------+---------------------------------+
| BB              | 8               | > Maximum number of tasks that  |
| _NUMBER_THREADS |                 | > can be run simultaneously     |
+-----------------+-----------------+---------------------------------+
| PARALLEL_MAKE   | -j 16           | > Option for make               |
+-----------------+-----------------+---------------------------------+
| MACHINE         | N/A             | > Select target board.          |
|                 |                 |                                 |
|                 |                 | - tcc8030-sub                   |
+-----------------+-----------------+---------------------------------+
| EXTRA           | debug-tweaks    | > Image property selected       |
| _IMAGE_FEATURES |                 | > additionally                  |
|                 | r               | >                               |
|                 | ead-only-rootfs | > For detailed options, refer   |
|                 |                 | > to "local.conf".              |
+-----------------+-----------------+---------------------------------+
| CORE_IMAG       | NULL            | > Name of package to be         |
| E_EXTRA_INSTALL |                 | > installed additionally on     |
|                 |                 | > image                         |
+-----------------+-----------------+---------------------------------+
| DISTRO          | poky-telechips  | > Select SDK type.              |
|                 |                 |                                 |
|                 |                 | - poky-telechips (sysvinit)     |
|                 |                 |                                 |
|                 |                 | - poky-telechips-systemd        |
|                 |                 |   (systemd)                     |
+-----------------+-----------------+---------------------------------+

#### Enable Main Core Functions

Use the **INVITE_PLATFORM** variable in the main core's "local.conf" to
set the supporting functions.

+:-------------------:+:----------------------------------------------:+
| **Feature**         | **Configuration**                              |
+---------------------+------------------------------------------------+
| Support 4K Video    | > INVITE_PLATFORM += \"support-4k-video\"      |
+---------------------+------------------------------------------------+
| Booting Animation   | > INVITE_PLATFORM += \"booting-animation\"     |
+---------------------+------------------------------------------------+

#### Enable Sub-core

To use the sub-core, you should enable the **INVITE_PLATFORM** variable
in the main core's "local.conf".

-----------------------------------------------------------------------
<<<<<<< HEAD
       **Feature**      **Configuration**
--------------------- -------------------------------------------------
=======

       **Feature**      **Configuration**

--------------------- -------------------------------------------------

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
     Enable sub-core    INVITE_PLATFORM += \"with-subcore\"

-----------------------------------------------------------------------

#### Set Up Sub-core Application

> Use **SUBCORE_APPS** variable in the sub-core's "local.conf" to set up
> the sub-core application for Rear View Camera (RVC).
>
> The RVC is enabled by default.

--------------------- -------------------------------------------------
<<<<<<< HEAD
       **Feature**                      **Configuration**
    
           RVC                       SUBCORE_APPS += \"rvc\"
=======

       **Feature**                      **Configuration**
    
           RVC                       SUBCORE_APPS += \"rvc\"

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
--------------------- -------------------------------------------------

#### Additional Setting

##### Set Up Graphics System

Use **DISTRO_FEATURES:remove = \"wayland\"** variable in the main core's
"local.conf" to set the Linux graphics system.

The default value is Wayland.

--------------------- -------------------------------------------------
<<<<<<< HEAD
=======

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
   **Graphics System**                  **Configuration**

         Wayland                             Default
    
          FBDEV               DISTRO_FEATURES:remove = \"wayland\"
<<<<<<< HEAD
=======

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
--------------------- -------------------------------------------------

##### Enable PulseAudio

To use PulseAudio as the Sound Server, **DISTRO_FEATURES:append = \"**
**pulseaudio\"** variable in the main core's "local.conf" should be
enabled.

**Note:** **\" pulseaudio\"** is enabled by default.

--------------------- -------------------------------------------------
<<<<<<< HEAD
    **Sound Server**                    **Configuration**
    
       PulseAudio           DISTRO_FEATURES:append = \" pulseaudio\"
=======

    **Sound Server**                    **Configuration**
    
       PulseAudio           DISTRO_FEATURES:append = \" pulseaudio\"

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
--------------------- -------------------------------------------------

##### Setting by changing LCD Panel AUO to BOE

The default LCD panel in the SDK is AUO. If you want to use BOE, remove
the **\#** (uncomment) from the **#LCD_PANEL_TYPE** in the "local.conf"
in each core.

--------------------- -------------------------------------------------
<<<<<<< HEAD
=======

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
        **Core**                         **local.conf**

        Main Core                   #LCD_PANEL_TYPE = \"BOE\"
    
        Sub-core                    #LCD_PANEL_TYPE = \"BOE\"
<<<<<<< HEAD
=======

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
--------------------- -------------------------------------------------

**Note:** For more details, refer to "*TCCxxxx Common SDK-User Guide for
AUO and BOE touch"*. \[12\]

## FAQs on Build

This chapter describes the frequently asked questions in the Yocto
Project environment.

### Q1. How to rebuild Package

If you want to rebuild the package, you should clean and then build the
package. Follow one of the three clean task types described in Chapter
4.7.1.1 to Chapter 4.7.1.3.

#### clean and build

Clear all output. However, shared state cache data is not cleared.

+-----------------------------------------------------------------------+
| \~/\.../build-autolinux\$ ./autolinux -c build \"alsa-lib -c clean\"  |
|                                                                       |
| \~/\.../build-autolinux\$ ./autolinux -c build \"alsa-lib\"           |
+-----------------------------------------------------------------------+

#### cleanall and build

Clear all data including all results, shared state cache data, and
downloaded source code.

+-----------------------------------------------------------------------+
| \~/\.../build-autolinux\$ ./autolinux -c build \"alsa-lib -c          |
| cleanall\"                                                            |
|                                                                       |
| \~/\.../build-autolinux\$ ./autolinux -c build \"alsa-lib\"           |
+-----------------------------------------------------------------------+

#### cleansstate and build

Clear all output and shared state cache data.

+-----------------------------------------------------------------------+
| \~/\.../build-autolinux\$ ./autolinux -c build \"alsa-lib -c          |
| cleansstate\"                                                         |
|                                                                       |
| \~/\.../build-autolinux\$ ./autolinux -c build \"alsa-lib\"           |
+-----------------------------------------------------------------------+

### Q2. How to rebuild All Packages

The Yocto project provides a single build type per recipe, so there is
no full rebuild functionality. To rebuild all packages,

you need to clean up each package and build the image.

If you want to rebuild the packages used by the image, you can use the
following command.

+-----------------------------------------------------------------------+
| > \~/\.../build-autolinux\$ ./autolinux -c build                      |
| > \"automotive-linux-platform-image \--runall=cleanall\"              |
| >                                                                     |
| > \~/\.../build-autolinux\$ ./autolinux -c build                      |
+-----------------------------------------------------------------------+

### Q3. How to modify Source Code -- Use Devtool

Yocto project provides ***devtool***, which has features to help you
build, test, and package software.

**Note:** ***devtool*** creates workspace directory and recipes in your
build directory and adds workspace to your "conf/bblayers.conf" after
you execute **devtool** command. Therefore, you can modify your source
code and recipes in the workspace directory.

#### Add Source Code

If you want to add your source code that has no recipe in the SDK, you
can use **devtool add** command. It assists in adding new software to be
built to the SDK. The **devtool add** command generates a new recipe
based on the existing source code.

You can add source code from a remote repository and a local directory
to the SDK:

- **devtool add {recipe name} {fetch url or source tree}**

+:----------------------------------------------------------------------+
| > \~/\.../build-autolinux\$ ./autolinux -c devtool add new-recipe     |
| > ssh://git.telechips.com/linux_ivi/bsp/kernel-5.10.git               |
| >                                                                     |
| > \~/\.../build-autolinux\$ ./autolinux -c devtool add new-recipe2    |
| > ./workspace/sources/new-recipe/                                     |
+-----------------------------------------------------------------------+

Then, the **devtool add** command generates **new-recipe** or
**new-recipe2** in workspace/recipes/new-recipe or new-recipe2. And the
source code is downloaded or copied in workspace/sources/new-recipe or
new-recipes2 directory. You can modify your recipes in the workspace.

You can see more information by using the following command: **devtool
add \--help**

#### Modify Source Code

The ***devtool*** sets up an environment to enable you to modify the
existing source code in the SDK. You can modify your recipes and source
code by the following command:

- **devtool modify {recipe name}**

+-----------------------------------------------------------------------+
| > \~/\.../build-autolinux\$ ./autolinux -c devtool modify sdk-recipe  |
+-----------------------------------------------------------------------+

Then, the **devtool modify** command generates a ".bbappend" file in
workspace/appends/sdk-recipe.bbappend. The source code is downloaded in
workspace/sources/sdk-recipe. You can modify your source code and
".bbappend".

You can also apply the external source code to your recipe.

+:----------------------------------------------------------------------+
| > \~/\.../build-autolinux\$ git clone                                 |
| > ssh://git.telechips.com/linux_ivi/bsp/kernel-5.10.git               |
| >                                                                     |
| > \~/\.../build-autolinux\$ ./autolinux -c devtool modify sdk-recipe  |
+-----------------------------------------------------------------------+

You can find more information by using the following command: **devtool
modify \--help**

#### Update Recipe

You can update the existing recipe to build the recipe for an updated
set of source files by using the following command:

- **devtool upgrade -V {version} {recipe name}**

+:----------------------------------------------------------------------+
| > \~/\.../build-autolinux\$ ./autolinux -c devtool upgrade -V 1.0.1   |
| > -S 7aa51ebda4a4512375bf12ca356afb7277e6826e sdk-recipe              |
+-----------------------------------------------------------------------+

The command above updates the SRCREV of recipe. In your workspace,
"sdk-recipe_1.0.1.bb" is generated in workspace/recipes directory, and
"sdk-recipe_1.0.1.bbappend" is generated in workspace/appends directory.

You can find more information by using the following command: **devtool
upgrade \--help**

#### After Setting Environment

If you want to build your source code or recipe, you can build it by
using the following command:

- **bitbake {recipe name} or devtool build {recipe name}**

+:----------------------------------------------------------------------+
| > \~/\.../build-autolinux\$ ./autolinux -c build \"new-recipe\"       |
| >                                                                     |
| > \~/\.../build-autolinux\$ ./autolinux -c devtool build new-recipe   |
+-----------------------------------------------------------------------+

You can install your outputs to your target by using the following
command:

- **devtool deploy-target {recipe name} {target}**

+-----------------------------------------------------------------------+
| > \~/\.../build-autolinux\$ ./autolinux -c devtool deploy-target      |
| > new-recipe root@192.168.1.1                                         |
+-----------------------------------------------------------------------+

After you finish editing recipes and source code, you can apply your
recipes to Yocto layer by using the following command:

- **devtool finish {recipe name} {layer name}**

+-----------------------------------------------------------------------+
| > \~/\.../build-autolinux\$ ./autolinux -c devtool finish new-recipe  |
| > meta-telechips                                                      |
| >                                                                     |
| > \~/\.../build-autolinux\$ ./autolinux -c devtool finish new-recipe2 |
| > meta-telechips                                                      |
+-----------------------------------------------------------------------+

The ***devtool*** makes the devtool branch in your workspace.

If you commit your patch to devtool branch and finish executing
***devtool***, the **devtool finish** command generates the patches and
adds the patches to the recipe.

If you want to remove your local outputs, reset the recipe by using the
following command:

- **devtool reset {recipe name} or devtool reset \--all**

+-----------------------------------------------------------------------+
| > \~/\.../build-autolinux\$ ./autolinux -c devtool reset recipe       |
| >                                                                     |
| > \~/\.../build-autolinux\$ ./autolinux -c devtool reset \--all       |
+-----------------------------------------------------------------------+

### Q4. How to add Extra Package to Image

If you want to install additional packages to the image that you are
currently building, you can set up the **CORE_IMAGE_EXTRA_INSTALL**
variable in "conf/local.conf" as follows:

-----------------------------------------------------------------------
<<<<<<< HEAD
=======

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
  CORE_IMAGE_EXTRA_INSTALL += \"openssh\"
  
  -----------------------------------------------------------------------

-----------------------------------------------------------------------

### Q5. How to modify rootfs Image Without Modifying Recipes

If you temporarily modify **rootfs** and create an image, run
**do_image** with the force option as follows:

+-----------------------------------------------------------------------+
| > \~/\.../build/tcc8030-main\$ pushd                                  |
| > tmp/work/tcc803                                                     |
| 0_main-telechips-linux/automotive-linux-platform-image/1.0-r0/rootfs/ |
| >                                                                     |
| > //modify rootfs                                                     |
| >                                                                     |
| > \~/\.../build/tcc8030-main/tmp/work/tcc8030                         |
| _main-telechips-linux/automotive-linux-platform-image/1.0-r0/rootfs\$ |
| > popd                                                                |
| >                                                                     |
| > \~/\.../build-autolinux\$ ./autolinux -c build                      |
| > \"automotive-linux-platform-image -C image\"                        |
| >                                                                     |
| > \~/\.../build-autolinux\$ ./autolinux -c make_fai                   |
+-----------------------------------------------------------------------+

### Q6. How to change Default Setting from Read-only to Writable rootfs

The default setting of the SDK **rootfs** is read-only. If you want to
use writable **rootfs**, you should change the **EXTRA_IMAGE_FEATURES**
in "conf/local.conf".

- read-only : **EXTRA_IMAGE_FEATURES = \"debug-tweaks
  read-only-rootfs\"**

- writeable : **EXTRA_IMAGE_FEATURES = \"debug-tweaks\"**

### Q7. How to enable Network Environment

To use network in the SDK, enable **network** feature in ***autolinux***
script.

### Q8. How to enable SSH Environment

The SDK supports SSH server based on openSSH.

**Note:** IP address, MAC address, and Gateway address must be set
according to your environment.

To use network in the SDK, enable **ssh-server-openssh** feature in
***autolinux*** script.

Select **network** feature first, then select **ssh-server-openssh**
feature.

The following is an example of TCC8030.

+-----------------------------------------------------------------------+
| **\~/release/build-autolinux\$ ./autolinux -c modify feature**        |
|                                                                       |
| Read configuration from autolinux.config                              |
|                                                                       |
| Choose the Features at tcc8030-main                                   |
|                                                                       |
| 1\. bootchart Install bootchart                                       |
|                                                                       |
| 2\. **network** Install network packages                              |
|                                                                       |
| 3\. optee Using OPTEE                                                 |
|                                                                       |
| \...                                                                  |
|                                                                       |
| 0.Exit                                                                |
|                                                                       |
| Choose Features enable/disable (1-8): 2                               |
|                                                                       |
| Choose the Features at tcc8030-main                                   |
|                                                                       |
| 1\. bootchart Install bootchart                                       |
|                                                                       |
| \* 2. **network** Install network packages                            |
|                                                                       |
| 3\. ssh-server-openssh Install openssh with network packages          |
|                                                                       |
| 4\. optee Using OPTEE                                                 |
|                                                                       |
| \...                                                                  |
|                                                                       |
| 0.Exit                                                                |
|                                                                       |
| Choose Features enable/disable (1-9): 3                               |
|                                                                       |
| Choose the Features at tcc8030-main                                   |
|                                                                       |
| 1\. bootchart Install bootchart                                       |
|                                                                       |
| \* 2. **network** Install network packages                            |
|                                                                       |
| \* 3. **ssh-server-openssh** Install openssh with network packages    |
|                                                                       |
| 4\. optee Using OPTEE                                                 |
|                                                                       |
| \...                                                                  |
|                                                                       |
| 0.Exit                                                                |
|                                                                       |
| Choose Features enable/disable (1-9): 0                               |
|                                                                       |
| \...                                                                  |
|                                                                       |
| ============                                                          |
| ===================================================================== |
|                                                                       |
| \...                                                                  |
|                                                                       |
| **FEATURES=\...network,ssh-server-openssh**                           |
|                                                                       |
| \...                                                                  |
|                                                                       |
| ============                                                          |
| ===================================================================== |
|                                                                       |
| Modify feature Successful                                             |
+=======================================================================+
+-----------------------------------------------------------------------+

### Q9. How to build Multi-machine from One Kernel or U-Boot Source

To build multi-machine from one external source (kernel or U-Boot),
enable variables related to **externalsrc** in the "conf/local.conf" for
each machine as follows:

+-----------------------------------------------------------------------+
| INHERIT += \"externalsrc\"                                            |
|                                                                       |
| //set kernel external source path                                     |
|                                                                       |
| EXTERNALSRC:pn-linux-telechips = \"\${HOME}/xxx\"                     |
|                                                                       |
| //set u-boot external source                                          |
|                                                                       |
| EXTERNALSRC:pn-u-boot-tcc = \"\${HOME}/xxx\"                          |
|                                                                       |
| EXTERNALSRC_BUILD:pn-u-boot-tcc = \"\${EXTERNALSRC:pn-u-boot-tcc}\"   |
+=======================================================================+
+-----------------------------------------------------------------------+

Each build path is limited to multi-machine build from one kernel or
U-Boot source through Yocto.

+-----------------------------------------------------------------------+
| //u-boot build path                                                   |
|                                                                       |
| \${EXTERNALSRC:pn-u-boot-tcc}/\${MACHINE}                             |
|                                                                       |
| //kernel build path                                                   |
|                                                                       |
| \${WORKDIR}/\${BPN}-\${PV}                                            |
+=======================================================================+
+-----------------------------------------------------------------------+

**Important:** The configuration files ("local.conf" and
"bblayers.conf") are reset if you enter the **configure** command in
***autolinux*** again.

When using **externalsrc**, Yocto does not execute the **do_patch**
task.

For details on **externalsrc**, refer to the following Yocto Project
website:

- <https://docs.yoctoproject.org/ref-manual/classes.html#externalsrc>

### Q10. How to disable initramfs

To disable initramfs, reset the related variables in "conf/local.conf"
for each machine as follows:

+-----------------------------------------------------------------------+
| INITRAMFS_IMAGE = \"\"                                                |
|                                                                       |
| INITRAMFS_TASK = \"\"                                                 |
|                                                                       |
| INITRAMFS_IMAGE_BUNDLE = \"0\"                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

And disable Kernel config, **CONFIG_BLK_INITRD**, in defconfig.

**Important:** The configuration files ("local.conf" and "bblayer.conf")
are reset if you enter **configure** command in ***autolinux*** again.

## Build Application 

### Using Application Development Toolkit (ADT)

The ADT provided by Telechips supports Cross Compile environment based
on **sysroot**, and it is based on the toolchain (**ARM GCC 11.2**) used
in the Yocto build.

The ADT uses various environment variables to support the environment
based on **sysroot**.

Major environment variables include **CC**, **LD**, and
**CONFIGURE_FLAGS**.

Environment variables that are already defined in ADT should not be
redefined in Makefile.

To build application, you should get familiar with the following
information.

#### Build ADT

[Autolinux Configuration]{.underline}

Execute ***autolinux*** build environment in the Yocto project
environment as described in Chapter 4.6.2.4. If this step is already
done, you can skip this chapter and go to Chapter 4.8.1.2.

[ADT Type Provided by Linux_YP4.0_IVI]{.underline}

Linux_YP4.0_IVI supports four types of ADTs as follows:

- **meta-toolchain-telechips (ADT)\
  <<<<<<< HEAD
  =======
  
>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
  **You can install basic packages for building Linux_YP4.0_IVI-based
  programs by using **meta-toolchain-telechips**.\
  \
  For detailed installation packages, refer to the following file:

<!-- -->

- poky/meta-telechips/meta-core/recipes-core/packagegroups/packagegroup-telechips-toolchain-target.bb

<!-- -->

- **meta-toolchain-telechips-ivi (ADT including GStreamer)**

  GStreamer and Linux_YP4.0_IVI demo applications are additionally
  installed in the **meta-toolchain-telechips**.

  For detailed installation packages, refer to the following file:

<!-- -->

- poky/meta-telechips/meta-ivi/recipes-telechips-ivi/packagegroups/packagegroup-als-ivi-toolchain-target.bb

<!-- -->

- **meta-toolchain-telechips-qt5 (ADT including GStreamer and Qt5)**

  Qt5 packages are additionally installed in
  **meta-toolchain-telechips-ivi**.

  For detailed installation packages, refer to the following files:

<!-- -->

- poky/meta-qt5/recipes-qt/packagegroups/packagegroup-qt5-toolchain-target.bb

- poky/meta-telechips/meta-ivi/recipes-qt/packagegroups/packagegroup-qt5-toolchain-target.bbappend

<!-- -->

- **meta-toolchain-telechips-subcore (ADT)**

  You can install basic packages for building Linux_YP4.0_IVI-based
  programs by using **meta-toolchain-telechips-subcore**.

  For detailed installation packages, refer to the following file:

<!-- -->

- poky/meta-telechips/meta-subcore/recipes-telechips-subcore/packagegroups/packagegroup-telechips-subcore-toolchain-target.bb

[Build ADT]{.underline}

To build the ADT for Main core, use the ***autolinux*** as follows:

- Build ADT for the main core

+-----------------------------------------------------------------------+
| > **\~/ release/build-autolinux\$ ./autolinux -c build**              |
| > \"**meta-toolchain-telechips-qt5**\"                                |
| >                                                                     |
| > Loading cache: 100%                                                 |
| > ##                                                                  |
| ###################################################################\| |
| > Time: 0:00:00                                                       |
| >                                                                     |
| > Loaded 1663 entries from dependency cache.                          |
| >                                                                     |
| > Parsing recipes: 100%                                               |
| >                                                                     |
| ###################################################################\| |
| > Time: 0:00:00                                                       |
| >                                                                     |
| > Parsing of 1046 .bb files complete (1045 cached, 1 parsed). 1664    |
| > targets, 260 skipped, 0 masked, 0 errors.                           |
| >                                                                     |
| > NOTE: Resolving any missing task queue dependencies                 |
| >                                                                     |
| > Build Configuration:                                                |
| >                                                                     |
| > BB_VERSION = \"2.0.0\"                                              |
| >                                                                     |
| > BUILD_SYS = \"x86_64-linux\"                                        |
| >                                                                     |
| > NATIVELSBSTRING = \"universal\"                                     |
| >                                                                     |
| > TARGET_SYS = \"aarch64-telechips-linux\"                            |
| >                                                                     |
| > MACHINE = \"tcc8030-main\"                                          |
| >                                                                     |
| > DISTRO = \"poky-telechips-systemd\"                                 |
| >                                                                     |
| > DISTRO_VERSION = \"4.0.17\"                                         |
| >                                                                     |
| > TUNE_FEATURES = \"aarch64 armv8a crc cortexa53\"                    |
| >                                                                     |
| > TARGET_FPU = \"\"                                                   |
| >                                                                     |
| > LINUX_VERSION = \"5.10.205\"                                        |
| >                                                                     |
| > KBUILD_DEFCONFIG = \"tcc803x_ivi_defconfig\"                        |
| >                                                                     |
| > IMAGE_FEATURES = \" debug-tweaks read-only-rootfs\"                 |
| >                                                                     |
| > GCCVERSION = \"arm-11.2\"                                           |
| >                                                                     |
| > GLIBCVERSION = \"2.35%\"                                            |
| >                                                                     |
| > INVITE_PLATFORM = \" with-subcore multimedia support-4k-video       |
| > qt5/wayland micom fw-update genivi\"                                |
| >                                                                     |
| > meta                                                                |
| >                                                                     |
| > meta-poky                                                           |
| >                                                                     |
| > \...                                                                |
| >                                                                     |
| > \...                                                                |
| >                                                                     |
| > Initialising tasks: 100%                                            |
| > \|###############################################################\| |
| > Time: 0:00:05                                                       |
| >                                                                     |
| > Sstate summary: Wanted 863 Found 266 Missed 597 Current 848 (30%    |
| > match, 65% complete)                                                |
| >                                                                     |
| > NOTE: Executing Tasks                                               |
| >                                                                     |
| > NOTE: Tasks Summary: Attempted 5442 tasks of which 3600 didn\'t     |
| > need to be rerun and all succeeded.                                 |
| >                                                                     |
| > NOTE: Writing buildhistory                                          |
| >                                                                     |
| > NOTE: Writing buildhistory took: 4 seconds                          |
+-----------------------------------------------------------------------+

When the build is successfully completed, the results come out in the
following location.

+-----------------------------------------------------------------------+
| > **\~/release/build-autolinux\$ ls -1                                |
| > build/tcc8030-main/tmp/deploy/sdk/**                                |
| >                                                                     |
| > LINUX_YP4.0_IVI_1.0.0-tcc803x-too                                   |
| lchain-cortexa53-opengl-wayland-qt5-x86_64-gcc-arm-11.2.host.manifest |
| >                                                                     |
| > LINUX_YP4.0_IVI_1.0.0-tc                                            |
| c803x-toolchain-cortexa53-opengl-wayland-qt5-x86_64-gcc-arm-11.2.sh\* |
| >                                                                     |
| > LINUX_YP4.0_IVI_1.0.0-tcc803x-toolc                                 |
| hain-cortexa53-opengl-wayland-qt5-x86_64-gcc-arm-11.2.target.manifest |
| >                                                                     |
| > LINUX_YP4.0_IVI_1.0.0-tcc803x-too                                   |
| lchain-cortexa53-opengl-wayland-qt5-x86_64-gcc-arm-11.2.testdata.json |
+-----------------------------------------------------------------------+

- Build ADT for the sub-core

+-----------------------------------------------------------------------+
| > **\~/ release/build-autolinux\$ ./autolinux -c build sub            |
| > \"meta-toolchain-telechips-subcore\"**                              |
| >                                                                     |
| > Loading cache: 100%                                                 |
| > ##                                                                  |
| ###################################################################\| |
| > Time: 0:00:00                                                       |
| >                                                                     |
| > Loaded 2052 entries from dependency cache.                          |
| >                                                                     |
| > NOTE: Resolving any missing task queue dependencies                 |
| >                                                                     |
| > Build Configuration:                                                |
| >                                                                     |
| > BB_VERSION = \"2.0.0\"                                              |
| >                                                                     |
| > BUILD_SYS = \"x86_64-linux\"                                        |
| >                                                                     |
| > NATIVELSBSTRING = \"universal\"                                     |
| >                                                                     |
| > TARGET_SYS = \"arm-telechips-linux-gnueabi\"                        |
| >                                                                     |
| > MACHINE = \"tcc8030-sub\"                                           |
| >                                                                     |
| > DISTRO = \"poky-telechips\"                                         |
| >                                                                     |
| > DISTRO_VERSION = \"4.0.17\"                                         |
| >                                                                     |
| > TUNE_FEATURES = \"arm vfp cortexa7 neon thumb callconvention-hard\" |
| >                                                                     |
| > TARGET_FPU = \"hard\"                                               |
| >                                                                     |
| > LINUX_VERSION = \"5.10.205\"                                        |
| >                                                                     |
| > KBUILD_DEFCONFIG = \"tcc803x_ivi_subcore_defconfig\"                |
| >                                                                     |
| > IMAGE_FEATURES = \" debug-tweaks read-only-rootfs\"                 |
| >                                                                     |
| > GCCVERSION = \"arm-11.2\"                                           |
| >                                                                     |
| > GLIBCVERSION = \"2.35%\"                                            |
| >                                                                     |
| > INVITE_PLATFORM = \" qt5/eglfs micom fw-update\"                    |
| >                                                                     |
| > SUBCORE_APPS = \" rvc\"                                             |
| >                                                                     |
| > meta                                                                |
| >                                                                     |
| > meta-poky                                                           |
| >                                                                     |
| > \...                                                                |
| >                                                                     |
| > \...                                                                |
| >                                                                     |
| > Initialising tasks: 100%                                            |
| > \|###############################################################\| |
| > Time: 0:00:05                                                       |
| >                                                                     |
| > Sstate summary: Wanted 308 Local 257 Mirrors 0 Missed 51 Current    |
| > 1224 (83% match, 96% complete)                                      |
| >                                                                     |
| > Removing 19 stale sstate objects for arch tcc8050_sub: 100%         |
| > \|#############################\| Time: 0:00:01                     |
| >                                                                     |
| > Removing 24 stale sstate objects for arch cortexa53: 100%           |
| > \|###############################\| Time: 0:00:00                   |
| >                                                                     |
| > NOTE: Executing Tasks                                               |
| >                                                                     |
| > NOTE: Tasks Summary: Attempted 3882 tasks of which 3743 didn\'t     |
| > need to be rerun and all succeeded.                                 |
| >                                                                     |
| > NOTE: Writing buildhistory                                          |
| >                                                                     |
| > NOTE: Writing buildhistory took: 5 seconds                          |
+-----------------------------------------------------------------------+

When the build is successfully completed, the results come out in the
following location.

+-----------------------------------------------------------------------+
| > **\~/release/build-autolinux\$ ls -1                                |
| > build/tcc8030-sub/tmp/deploy/sdk/**                                 |
| >                                                                     |
| > LINUX_YP4.0_IVI_1.0.0-tcc803x-toolchai                              |
| n-cortexa7t2hf-opengl-fbdev-subcore-x86_64-gcc-arm-11.2.host.manifest |
| >                                                                     |
| > LINUX_YP4.0_IVI_1.0.0-tcc803x                                       |
| -toolchain-cortexa7t2hf-opengl-fbdev-subcore-x86_64-gcc-arm-11.2.sh\* |
| >                                                                     |
| > LINUX_YP4.0_IVI_1.0.0-tcc803x-toolchain-                            |
| cortexa7t2hf-opengl-fbdev-subcore-x86_64-gcc-arm-11.2.target.manifest |
| >                                                                     |
| > LINUX_YP4.0_IVI_1.0.0-tcc803x-toolchai                              |
| n-cortexa7t2hf-opengl-fbdev-subcore-x86_64-gcc-arm-11.2.testdata.json |
+-----------------------------------------------------------------------+

#### Install ADT

Run the script to install ADT as follows.

**Note:** For building ADT, refer to Chapter 4.8.1.1.

+-----------------------------------------------------------------------+
| > **\~/release\$                                                      |
| > ./build                                                             |
| -autolinux/build/tcc8030-main/tmp/deploy/sdk/LINUX_YP4.0_IVI_1.0.0-tc |
| c803x-toolchain-cortexa53-opengl-wayland-qt5-x86_64-gcc-arm-11.2.sh** |
| >                                                                     |
| > Telechips Baseline (Poky/meta-telechips/meta-core) SDK installer    |
| > version nodistro.0                                                  |
| >                                                                     |
| > ==============                                                      |
| ===================================================================== |
| >                                                                     |
| > Enter target directory for SDK (default: /usr/local/oecore-x86_64): |
| > ./adt                                                               |
| >                                                                     |
| > You are about to install the SDK to \"/home/release/adt\". Proceed  |
| > \[Y/n\]? Y                                                          |
| >                                                                     |
| > Extracting                                                          |
| > SDK...\...\...\...\...\...\...\...\...\...\...\...\...\...\....done |
| >                                                                     |
| > Setting it up\...done                                               |
| >                                                                     |
| > SDK has been successfully set up and is ready to be used.           |
| >                                                                     |
| > Each time you wish to use the SDK in a new shell session, you need  |
| > to source the environment setup script e.g.                         |
| >                                                                     |
| > \$ . /home/release/adt/environment-setup-cortexa53-telechips-linux  |
| >                                                                     |
| > \~/release\$                                                        |
+-----------------------------------------------------------------------+

#### ADT Setting

Set to ADT build environment.

You can use **echo \$CC** to check whether your current environment is
ADT.

+-----------------------------------------------------------------------+
| > **\~/release\$ source                                               |
| > adt/environment-setup-cortexa53-telechips-linux**                   |
| >                                                                     |
| > **\~/release\$ echo \$CC**                                          |
| >                                                                     |
| > aarch64-telechips-linux-gcc -mcpu=cortex-a53 -march=armv8-a+crc     |
| > -mbranch-protection=standard -mcpu=cortex-a53 -mtune=cortex-a53     |
| > -fstack-protector-strong -fPIE -pie -O2 -D_FORTIFY_SOURCE=2         |
| > -Wformat -Wformat-security -Werror=format-security -fPIC            |
| > \--sysroot=/home/release/adt/sysroots/cortexa53-telechips-linux     |
+-----------------------------------------------------------------------+

#### Conduct Cross Compile by using ADT

You can use ADT to easily conduct cross complication as follows:

- Single File Exercise\
  If the project source is in one file, conduct cross complication by
  using **\$CC** as follows:

+-----------------------------------------------------------------------+
| > **\~/release\$ \$CC -o hello hello.c**                              |
+-----------------------------------------------------------------------+

- Exercise based on Makefile

  If the project is based on a Makefile, do not define the **AR**,
  **CC**, **CXX**, and **LD** variables in the Makefile.

  Environment variables that are already defined in ADT should not be
  redefined in Makefile.

- Exercise based on ***Autotools***

  If project is based on ***Autotools***, use **\$CONFIGURE_FLAGS** as
  follows:

+-----------------------------------------------------------------------+
| > **\~/release\$ aclocal**                                            |
| >                                                                     |
| > **\~/release\$ autoheader**                                         |
| >                                                                     |
| > **\~/release\$ autoconf**                                           |
| >                                                                     |
| > **\~/release\$ automake -a**                                        |
| >                                                                     |
| > **\~/release\$ ./configure \$CONFIGURE_FLAGS**                      |
| >                                                                     |
| > **\~/release\$ make**                                               |
+-----------------------------------------------------------------------+

### Use Extensible SDK (eSDK)

The eSDK provided by Telechips supports the Cross Compile environment
based on **sysroot**, recipes, ***devtool***, built images, and build
information.

#### Build eSDK

Yocto Project supports extensible SDK (eSDK), which allows the
followings:

- Adding new applications and libraries to an image easily

- Modifying the source code of an existing component

- Testing changes on the target hardware

**Important:** To use eSDK, the host GCC version must be 7.5 or higher.

[Autolinux Configuration]{.underline}

Execute ***autolinux*** build environment in the Yocto project
environment as described in Chapter 4.6.2.4.

**Note:** If this step is already done, you can skip this chapter.

[Build eSDK]{.underline}

To build the eSDK, use the ***autolinux*** as follows:

+-----------------------------------------------------------------------+
| > **\~/release/build-autolinux\$ ./autolinux -c build                 |
| > \"automotive-linux-platform-image -c populate_sdk_ext\"**           |
| >                                                                     |
| > Loading cache: 100%                                                 |
| > ##                                                                  |
| ###################################################################\| |
| > Time: 0:00:00                                                       |
| >                                                                     |
| > Loaded 1663 entries from dependency cache.                          |
| >                                                                     |
| > Parsing recipes: 100%                                               |
| >                                                                     |
| ###################################################################\| |
| > Time: 0:00:00                                                       |
| >                                                                     |
| > Parsing of 1046 .bb files complete (1045 cached, 1 parsed). 1664    |
| > targets, 260 skipped, 0 masked, 0 errors.                           |
| >                                                                     |
| > NOTE: Resolving any missing task queue dependencies                 |
| >                                                                     |
| > Build Configuration:                                                |
| >                                                                     |
| > BB_VERSION = \"2.0.0\"                                              |
| >                                                                     |
| > BUILD_SYS = \"x86_64-linux\"                                        |
| >                                                                     |
| > NATIVELSBSTRING = \"universal\"                                     |
| >                                                                     |
| > TARGET_SYS = \"aarch64-telechips-linux\"                            |
| >                                                                     |
| > MACHINE = \"tcc8030-main\"                                          |
| >                                                                     |
| > DISTRO = \"poky-telechips-systemd\"                                 |
| >                                                                     |
| > DISTRO_VERSION = \"4.0.17\"                                         |
| >                                                                     |
| > TUNE_FEATURES = \"aarch64 armv8a crc cortexa53\"                    |
| >                                                                     |
| > TARGET_FPU = \"\"                                                   |
| >                                                                     |
| > LINUX_VERSION = \"5.10.205\"                                        |
| >                                                                     |
| > KBUILD_DEFCONFIG = \"tcc803x_ivi_defconfig\"                        |
| >                                                                     |
| > IMAGE_FEATURES = \" debug-tweaks read-only-rootfs\"                 |
| >                                                                     |
| > GCCVERSION = \"arm-11.2\"                                           |
| >                                                                     |
| > GLIBCVERSION = \"2.35%\"                                            |
| >                                                                     |
| > INVITE_PLATFORM = \" with-subcore multimedia support-4k-video       |
| > qt5/wayland micom fw-update genivi\"                                |
| >                                                                     |
| > meta                                                                |
| >                                                                     |
| > meta-poky                                                           |
| >                                                                     |
| > \...                                                                |
| >                                                                     |
| > \...                                                                |
| >                                                                     |
| > Initialising tasks: 100%                                            |
| > \|###############################################################\| |
| > Time: 0:00:05                                                       |
| >                                                                     |
| > Sstate summary: Wanted 863 Found 266 Missed 597 Current 848 (30%    |
| > match, 65% complete)                                                |
| >                                                                     |
| > NOTE: Executing Tasks                                               |
| >                                                                     |
| > NOTE: Tasks Summary: Attempted 5442 tasks of which 3600 didn\'t     |
| > need to be rerun and all succeeded.                                 |
| >                                                                     |
| > NOTE: Writing buildhistory                                          |
| >                                                                     |
| > NOTE: Writing buildhistory took: 4 seconds                          |
+-----------------------------------------------------------------------+

When the build is successfully completed, the results come out in the
following location.

+-----------------------------------------------------------------------+
| > **\~/release/build-autolinux\$ ls -1                                |
| > build/tcc8030-main/tmp/deploy/sdk/**                                |
| >                                                                     |
| > poky-telechips-systemd-glibc-x86_64-automotive-                     |
| linux-platform-image-cortexa53-toolchain-ext-nodistro.0.host.manifest |
| >                                                                     |
| > poky-telechips-systemd-glibc-x86_64-                                |
| automotive-linux-platform-image-cortexa53-toolchain-ext-nodistro.0.sh |
| >                                                                     |
| > poky-telechips-systemd-glibc-x86_64-automotive-li                   |
| nux-platform-image-cortexa53-toolchain-ext-nodistro.0.target.manifest |
| >                                                                     |
| > poky-telechips-systemd-glibc-x86_64-automotive-                     |
| linux-platform-image-cortexa53-toolchain-ext-nodistro.0.testdata.json |
| >                                                                     |
| > x86_64-buildtools-nativesdk-standalone-4.0.17.host.manifest         |
| >                                                                     |
| > x86_64-buildtools-nativesdk-standalone-4.0.17.sh                    |
| >                                                                     |
| > x86_64-buildtools-nativesdk-standalone-4.0.17.target.manifest       |
| >                                                                     |
| > x86_64-buildtools-nativesdk-standalone-4.0.17.testdata.json         |
+-----------------------------------------------------------------------+

#### Install eSDK

Execute the following script to install eSDK. For building eSDK, refer
to Chapter 4.8.2.1.

+-----------------------------------------------------------------------+
| > **\~/eSDK\$                                                         |
| > ./poky-telechips-systemd-glibc-x86_64-au                            |
| tomotive-linux-platform-image-cortexa53-toolchain-ext-nodistro.0.sh** |
| >                                                                     |
| > Telechips Baseline (Poky/meta-telechips/meta-core) Extensible SDK   |
| > installer version nodistro.0                                        |
| >                                                                     |
| > =========================                                           |
| ===================================================================== |
| >                                                                     |
| > Enter target directory for SDK (default:                            |
| > \~/poky-telechips-systemd_sdk): ./maincore                          |
| >                                                                     |
| > You are about to install the SDK to \"/home/eSDK/maincore\".        |
| > Proceed \[Y/n\]? Y                                                  |
| >                                                                     |
| > Extracting                                                          |
| > SDK\...\...\...\...\...\...\...\...\...\...\...\...\...             |
| \...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\....done |
| >                                                                     |
| > Setting it up\...                                                   |
| >                                                                     |
| > Extracting buildtools\...                                           |
| >                                                                     |
| > Preparing build system\...                                          |
| >                                                                     |
| > \~/eSDK\$ ls -1 maincore/                                           |
| >                                                                     |
| > bitbake-cookerdaemon.log                                            |
| >                                                                     |
| > buildtools/                                                         |
| >                                                                     |
| > cache/                                                              |
| >                                                                     |
| > conf/                                                               |
| >                                                                     |
| > downloads/                                                          |
| >                                                                     |
| > environment-setup-cortexa53-telechips-linux                         |
| >                                                                     |
| > layers/                                                             |
| >                                                                     |
| > preparing_build_system.log                                          |
| >                                                                     |
| > site-config-cortexa53-telechips-linux                               |
| >                                                                     |
| > sstate-cache/                                                       |
| >                                                                     |
| > sysroots/                                                           |
| >                                                                     |
| > tmp/                                                                |
| >                                                                     |
| > version-cortexa53-telechips-linux                                   |
| >                                                                     |
| > workspace/                                                          |
+-----------------------------------------------------------------------+

The important directories and files included in the eSDK are as follows:

- **buildtools:** Tools to configure the build environment of Yocto
  Project for the Linux_YP4.0_IVI

- **conf:** Directory that contains user configuration files such as
  "local.conf" and "bblayers.conf"

- **downloads:** Directory that contains the downloaded files

- **environment-setup-cortexa53-telechips-linux:** Script file to set
  eSDK environment

- **layers:** Directory that contains recipes, patches, configuration
  files, and so on that are required for building the eSDK

- **sstate-cache:** Directory that contains prebuilt cache

- **workspace:** Directory that contains recipes and source code in
  working

#### Build Application

Yocto project supports ***devtool*** that provides the several features
for developer. Refer to Chapter 4.7.3 to modify source code.

### Copy Application File to Board via USB

**{Storage_Path}** depends on the number of connected storages.

Check and use the path set when connecting storage. (Example:
/run/media/sda1)

1.  Connect USB storage to USB3.0 Host or USB2.0 terminal.

<!-- -->

5.  When copying the application file to root folder, run the following
    **copy** command:

    - **root@telechips-MACHINE:\~# cp {Storage_Path}/user_file .**

6.  If the copied path has authority of read-only, you need to run the
    following **remount** and **copy** commands.

    - **root@telechips-MACHINE:\~# mount -o remount,rw** **/**

    - **root@telechips-MACHINE:\~# cp {Storage_Path}/user_file .**

# Firmware Downloader (FWDN) Guide

This chapter describes how to download the Linux_YP4.0_IVI to TCC803x
Evaluation Board (EVB) and to log in the Linux console.

For more information on how to use the tools for ***Firmware
Downloader***, refer to the following documents.

- **FWDN V8**: "*TCCxxxx Common-User Guide for Firmware Downloader V8*"
  \[9\]

- **mktcimg**: "*TC Common-User Guide for mktcimg*" \[10\]

The ***FWDN V8*** is a PC tool for downloading firmware in Windows 10
64-bit and Linux environments.

This chapter describes the case of downloading in Windows environment.
For Linux, refer to \"*TCCxxxx Common-User Guide for Firmware Downloader
V8*". \[9\]

## System Requirement

### Software Requirement

+---------+---------------------------+-----------+-------------------+
| **Cat   | **Description**           | **Path**  | **Note**          |
| egory** |                           |           |                   |
+:=======:+===========================+:=========:+===================+
| VTC     | > Driver for Windows PC   | fwdn_v8/o | > V5.0.0.14 or    |
| Driver  | > that is used to         | ut/vtcdrv | > higher is       |
|         | > download                | v5.0      | > strongly        |
|         | > Linux_YP4.0_IVI         | .0.14.zip | > recommended.    |
|         | > firmware.               |           | >                 |
|         | >                         |           | > Refer to VTC    |
|         | > VTC driver              |           | > Driver          |
|         | > corresponding to the    |           | > information     |
|         | > Windows version must be |           | > path:           |
|         | > installed.              |           |                   |
|         | >                         |           | - \"ReadMe.txt\"  |
|         | > It is installed only    |           |   in vtcdrv       |
|         | > once on your PC.        |           |   v5.0.0.14.zip   |
+---------+---------------------------+-----------+-------------------+
| FWDN    | > Tools for downloading   | fwdn_v8   | > You must use    |
|         | > Linux_YP4.0_IVI         | /out/fwdn | > ***FWDN V8***.  |
|         | > firmware                |           |                   |
|         |                           | or        |                   |
|         |                           |           |                   |
|         |                           | fw        |                   |
|         |                           | dn_v8/out |                   |
|         |                           | /fwdn.exe |                   |
+---------+---------------------------+-----------+-------------------+

: []{#_Ref143248365 .anchor}Table 5.1 Software Requirement

### Hardware Requirement

+---------+---------------------------+--------------------------------+
| **Cat   | **Description**           | **Note**                       |
| egory** |                           |                                |
+:=======:+===========================+:==============================:+
| Demo    | > Supported chipsets are  | > \-                           |
| Board   | > TCC803x.                |                                |
+---------+---------------------------+--------------------------------+
| Power   | > 12V power adapter is    | > Recommend using the power    |
| Adapter | > used to supply power to | > adapter (12V) provided by    |
|         | > the board and LCD.      | > Telechips.                   |
+---------+---------------------------+--------------------------------+
| USB     | > It is used to connect a | > Refer to Chapter 2.2.1 for   |
| Cable   | > demo board to PC.       | > USB cable connection.        |
+---------+---------------------------+--------------------------------+

: []{#_Ref143248373 .anchor}Table 5.2 Hardware Requirement

## Linux_YP4.0_IVI Firmware Construction

Note: If you have already built the SDK following Chapter 4.6.2.5 and
have created \"SD_Data.fai\", you can skip this chapter.

+-------------+--------------------------------------------------------+
| **Image     | **Description**                                        |
| Type**      |                                                        |
+:===========:+:=======================================================+
| U-Boot\     | > Image to initialize the system hardware and put the  |
| boot loader | > Linux kernel image into memory for execution         |
| Image       | >                                                      |
|             | > Refer to the following example for the U-Boot image  |
| (\*.rom)    | > names used in each core.                             |
|             | >                                                      |
|             | > u-boot-tcc8030-main.rom                              |
+-------------+--------------------------------------------------------+
| Kernel      | > A boot image file in which the Linux kernel is       |
| Image       | > compressed                                           |
|             | >                                                      |
| (\*.img)    | > Refer to the following example for the Kernel image  |
|             | > names used in each board.                            |
|             | >                                                      |
|             | > **Example:**                                         |
|             | >                                                      |
|             | > Main core: tc-boot-\[MACHINE\].img                   |
|             | >                                                      |
|             | > Sub-core: Image-\[MACHINE\].bin                      |
+-------------+--------------------------------------------------------+
| Root File   | > An image that is served as the root file system for  |
| System      | > Linux system                                         |
| Image       | >                                                      |
|             | > Refer to the following example for the root file     |
| (\*.ext4)   | > system image names used in each machine.             |
|             | >                                                      |
|             | > The default generated Root File System Image is      |
|             | > read-only.                                           |
|             | >                                                      |
|             | > **Example:**\                                        |
|             | > Main core:                                           |
|             | > automotive-linux-platform-image-tcc8030-main.ext4    |
|             | >                                                      |
|             | > Sub-core:                                            |
|             | > telechips-ivi-subcore-image-tcc8030-sub.cpio         |
+-------------+--------------------------------------------------------+
| RW          | > It is used to store the RW data of the database and  |
| Partition   | > application used in Media Player as the RW area      |
| Image       | > required by Linux_YP4.0_IVI.                         |
|             | >                                                      |
| (Home       | > **Example:** home-directory.ext4                     |
| directory)  |                                                        |
|             |                                                        |
| (\*.ext4)   |                                                        |
+-------------+--------------------------------------------------------+
| Device Tree | > An image that contains driver information on the     |
| Binary      | > hardware devices of each board                       |
| (DTB)       | >                                                      |
| Image\      | > Refer to the following example for the dtb image     |
| (\*.dtb)    | > names used in each core.                             |
|             | >                                                      |
|             | > **Example:**                                         |
|             | >                                                      |
|             | > Main core: tcc8030-ivi-lpd4321.dtb                   |
|             |                                                        |
|             | Sub-core: tcc8030-ivi-subcore-lpd4321.dtb              |
+-------------+--------------------------------------------------------+
| SNOR Image  | > This image contains SNOR firmware image.             |
|             | >                                                      |
| (\*.rom)    | > SNOR image uses prebuilt image. Refer to the         |
|             | > following example for the SNOR image.                |
|             | >                                                      |
|             | > **Example:** tcc803x_snor_boot.rom                   |
+-------------+--------------------------------------------------------+
| bconf.bin   | > This is the configuration information for the        |
|             | > chipboot code and the boot firmware such as BL1/2    |
|             | > and SC F/W.                                          |
+-------------+--------------------------------------------------------+
| dram        | > This is the DRAM parameter information data used     |
| _params.bin | > during DRAM initialization.                          |
+-------------+--------------------------------------------------------+
| fwdn.rom    | > This is an image of firmware running in CR5 (MICOM)  |
|             | > to use FWDN.                                         |
+-------------+--------------------------------------------------------+
| hsm.bin     | > This is an image of firmware running in Hardware     |
|             | > Security Module (HSM).                               |
+-------------+--------------------------------------------------------+
| optee.rom   | > This is an image of Trusted Environment Execution    |
|             | > (TEE) OS for CA53.                                   |
+-------------+--------------------------------------------------------+
| mi          | > This is an image to initialize the system hardware   |
| com-bl1.rom | > and execute the main firmware of CR5 (MICOM) image   |
+-------------+--------------------------------------------------------+
| m           | > This is a main firmware image of CR5 (MICOM)         |
| icom.cs.bin |                                                        |
+-------------+--------------------------------------------------------+
| r5          | > This is a sub-firmware image of CR5 (MICOM). This    |
| _sub_fw.bin | > image is used when updating the main firmware.       |
+-------------+--------------------------------------------------------+
| ap.rom      | > This is an image of trusted-firmware BL31 for CA7.   |
+-------------+--------------------------------------------------------+
| bl2-2.rom   | > This is an image of trusted-firmware BL31.           |
+-------------+--------------------------------------------------------+
| keyp        | > This is an image where the keys for Secure Boot are  |
| ackages.bin | > stored.                                              |
+-------------+--------------------------------------------------------+

: []{#_Ref143248405 .anchor}Table 5.3 Linux_YP4.0_IVI Firmware
Construction

**Note:** Use Linux **dd** command to create RW file system for home
directory image:

- **\$ dd if=/dev/zero of=home-directory.ext4 bs=1K count=512000**

- **\$ mkfs.ext4 home-directory.ext4**

### Boot-firmware

Linux_YP4.0_IVI requires "fwdn.rom", HSM, trusted firmware-A, and
storage core firmware. These files are included in the boot-firmware.
You can get the boot-firmware from SDK.

+-----------------------------------------------------------------------+
| > \$ ls boot-firmware_tcc803x/prebuilt/                               |
| >                                                                     |
| > ap.rom bconf.bin bl2-2.rom dram_params.bin fwdn.rom hsm.bin         |
| > keypackages.bin micom-bl1.rom micom.cs.bin micom.xpe.bin optee.rom  |
| > r5_sub_fw.bin tcc803xpe_snor_boot.rom tcc803x_snor_boot.rom         |
+-----------------------------------------------------------------------+

### Make SD Data using make_fai

#### Check eMMC Device Information

Before creating the fai file, it must be created according to the
customer\'s eMMC capacity.

1.  Connect ***FWDN V8*** to the board.

<!-- -->

7.  Check User Capacity in eMMC Info.

**Note:** To connect ***FWDN V8*** to the board, refer to Chapter 5.4.3.

+-----------------------------------------------------------------------+
| fwdn\> [f                                                             |
| wdn.exe](https://wiki.telechips.com:8443/display/A2/fwdn.exe) \--fwdn |
| \...\\boot-firmware\\fwdn.json                                        |
|                                                                       |
| \...                                                                  |
|                                                                       |
| \...                                                                  |
|                                                                       |
| fwdn\> fwdn.exe \--device-info                                        |
|                                                                       |
| \[main:30\] FWDN V8 v1.4.12 - 2023.6.22 11:23:58                      |
|                                                                       |
| \[FWDN_V8::GetFWDNRomVersion:1588\] fwdn.rom version : 23.2.20        |
|                                                                       |
| \[FWDN_V8::PrintDeviceInfo:1201\] \-\-\-\-\-\-\-\-\-\-\-\-\--Device   |
| info\-\-\-\-\-\-\-\-\-\-\-\--                                         |
|                                                                       |
| \[FWDN_V8::PrintDeviceInfo:1202\]                                     |
|                                                                       |
| \-\-\-\-- Detail of Storages \-\-\-\--                                |
|                                                                       |
| \#### eMMC Info \####                                                 |
|                                                                       |
| Manufacture ID: 0x90                                                  |
|                                                                       |
| OEM: 0x14a                                                            |
|                                                                       |
| Name: H8G4a                                                           |
|                                                                       |
| User Capacity: 7.3 GiB (7818182656 Byte)                              |
|                                                                       |
| Boot Capacity: 8 MiB (8388608 Byte)                                   |
|                                                                       |
| RPMB Capacity: 4 MiB (4194304 Byte)                                   |
|                                                                       |
| Speed Mode: HS200                                                     |
|                                                                       |
| \#### SNOR Info \####                                                 |
|                                                                       |
| Manufacture ID: 0xc2                                                  |
|                                                                       |
| Device ID: 0x2019                                                     |
|                                                                       |
| Name: MXIC-MX25L25645G                                                |
|                                                                       |
| Sector Size: 4 KiB (4096 Byte)                                        |
|                                                                       |
| Total Capacity: 32 MiB (33554432 Byte)                                |
|                                                                       |
| 4Byte Address Mode: Supported                                         |
|                                                                       |
| \-\-\-\-- Summary of Storages \-\-\-\--                               |
|                                                                       |
| eMMC : O                                                              |
|                                                                       |
| SNOR : O                                                              |
|                                                                       |
| \-\-\-\-- Summary of DRAM Init \-\-\-\--                              |
|                                                                       |
| DRAM Init : Success (Result 0x0 )                                     |
|                                                                       |
| DRAM Size : 4096MB                                                    |
|                                                                       |
| \[FWDN_V8::PrintDeviceInfo:1203\]                                     |
| \-\-\-                                                                |
| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- |
|                                                                       |
| \[main:156\] Complete FWDN                                            |
+=======================================================================+
+-----------------------------------------------------------------------+

#### Create SD Data with eMMC Size

Add the User Capacity confirmed in eMMC Info to **STORAGE_SIZE** in
local.conf.

+-----------------------------------------------------------------------+
| > \~/release/build-autolinux\$ vi build/tcc8030-main/conf/local.conf  |
| >                                                                     |
| > // modify *local.conf* file                                         |
| >                                                                     |
| > \# Storage Size                                                     |
| >                                                                     |
| > \# Set STORAGE_SIZE variable according to the storage size you are  |
| > using                                                               |
| >                                                                     |
| > STORAGE_SIZE = \"7818182656\"                                       |
+-----------------------------------------------------------------------+

-----------------------------------------------------------------------
<<<<<<< HEAD
=======

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
  \~/release/build-autolinux\$ ./autolinux -c build

-----------------------------------------------------------------------

After adding eMMC size, make SD Data and "partition.list" based on the
contents of "make_fai.bbclass".

**Note:** Class files are used to abstract common functionality and
share it amongst multiple recipe (.bb) files. To use a class file, the
recipe should inherit the class.

-----------------------------------------------------------------------
<<<<<<< HEAD
=======

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
  \~/release/build-autolinux\$ ./autolinux -c make_fai

-----------------------------------------------------------------------

#### Partition Information of SD Data

**Type 1**: With meta-update (default)

+-------+-------+--------+--------+-----------------+----------------+
| **    | **    | *      | *      | **Description** | **File Name**  |
| FWDN\ | Size\ | *Label | *Block |                 |                |
| P     | (     | Name** | De     |                 |                |
| artit | KB)** |        | vice** |                 |                |
| ion** |       |        |        |                 |                |
|       |       |        | **(e   |                 |                |
|       |       |        | MMC)** |                 |                |
+:=====:+:=====:+:======:+:======:+=================+:==============:+
| Part  | 2048  | bl3_   | mmc    | Main Core Boot  | u-boot-\       |
| ition |       | ca53_a | blk0p1 | Loader A        | [MACHINE\].rom |
| 1     |       |        |        |                 |                |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 2048  | bl3_   | mmc    | Main Core Boot  | u-boot-\       |
| ition |       | ca53_b | blk0p2 | Loader B        | [MACHINE\].rom |
| 2     |       |        |        |                 |                |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 30720 | boot_a | mmc    | Kernel image A  | tc-boot-\      |
| ition |       |        | blk0p3 |                 | [MACHINE\].img |
| 3     |       |        |        |                 |                |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 30720 | boot_b | mmc    | Kernel image B  | tc-boot-\      |
| ition |       |        | blk0p4 |                 | [MACHINE\].img |
| 4     |       |        |        |                 |                |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | c     | sy     | mmc    | Root file       | automo         |
| ition | ustom | stem_a | blk0p5 | system A        | tive-linux-pla |
| 5     |       |        |        |                 | tform-image-\[ |
|       |       |        |        |                 | MACHINE\].ext4 |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | c     | sy     | mmc    | Root file       | automo         |
| ition | ustom | stem_b | blk0p6 | system B        | tive-linux-pla |
| 6     |       |        |        |                 | tform-image-\[ |
|       |       |        |        |                 | MACHINE\].ext4 |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 200   | dtb_a  | mmc    | Device tree A   | \[chip_n       |
| ition |       |        | blk0p7 |                 | ame\]-ivi-\[bo |
| 7     |       |        |        |                 | ard_name\].dtb |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 200   | dtb_b  | mmc    | Device tree B   | \[chip_n       |
| ition |       |        | blk0p8 |                 | ame\]-ivi-\[bo |
| 8     |       |        |        |                 | ard_name\].dtb |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 1024  | env    | mmc    | Environment     | \-             |
| ition |       |        | blk0p9 |                 |                |
| 9     |       |        |        |                 |                |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 1024  | misc   | mmcb   | Miscellaneous   | \-             |
| ition |       |        | lk0p10 |                 |                |
| 10    |       |        |        |                 |                |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 40960 | splash | mmcb   | Splash          | splash_1       |
| ition |       |        | lk0p11 |                 | 920x720x32.img |
| 11    |       |        |        |                 |                |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 5     | home   | mmcb   | RW file system\ | home-          |
| ition | 12000 |        | lk0p12 | for home        | directory.ext4 |
| 12    |       |        |        | directory       |                |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 30720 | a7s_   | mmcb   | Sub-core Kernel | Image-\        |
| ition |       | boot_a | lk0p13 | Image           | [MACHINE\].bin |
| 13    |       |        |        |                 |                |
|       |       |        |        | (optional)      |                |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 30720 | a7s_   | mmcb   | Sub-core Kernel | Image-\        |
| ition |       | boot_b | lk0p14 | Image           | [MACHINE\].bin |
| 14    |       |        |        |                 |                |
|       |       |        |        | (optional)      |                |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 200   | a7s    | mmcb   | Sub-core Device | \[             |
| ition |       | _dtb_a | lk0p15 | tree            | chip_name\]-iv |
| 15    |       |        |        |                 | i-subcore-\[bo |
|       |       |        |        | (optional)      | ard_name\].dtb |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 200   | a7s    | mmcb   | Sub-core Device | \[             |
| ition |       | _dtb_a | lk0p16 | tree            | chip_name\]-iv |
| 16    |       |        |        |                 | i-subcore-\[bo |
|       |       |        |        | (optional)      | ard_name\].dtb |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | c     | a7s_   | mmcb   | Sub-core root   | te             |
| ition | ustom | root_a | lk0p17 | file system     | lechips-ivi-su |
| 17    |       |        |        |                 | bcore-image-\[ |
|       |       |        |        | (optional)      | MACHINE\].cpio |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | c     | a7s_   | mmcb   | Sub-core root   | te             |
| ition | ustom | root_b | lk0p18 | file system     | lechips-ivi-su |
| 18    |       |        |        |                 | bcore-image-\[ |
|       |       |        |        | (optional)      | MACHINE\].cpio |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 10    | Data   | mmcb   | User storage    | \-             |
| ition | 48576 |        | lk0p19 |                 |                |
| 19    |       |        |        |                 |                |
+-------+-------+--------+--------+-----------------+----------------+

**Type 2**: Without meta-update

+-------+-------+--------+--------+-----------------+----------------+
| **    | **    | *      | *      | **Description** | **File Name**  |
| FWDN\ | Size\ | *Label | *Block |                 |                |
| P     | (     | Name** | De     |                 |                |
| artit | KB)** |        | vice** |                 |                |
| ion** |       |        |        |                 |                |
|       |       |        | **(e   |                 |                |
|       |       |        | MMC)** |                 |                |
+:=====:+:=====:+:======:+:======:+=================+:==============:+
| Part  | 2048  | bl3_   | mmc    | Main Core Boot  | u-boot-\       |
| ition |       | ca53_a | blk0p1 | Loader A        | [MACHINE\].rom |
| 1     |       |        |        |                 |                |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 2048  | bl3_   | mmc    | Main Core Boot  | u-boot-\       |
| ition |       | ca53_b | blk0p2 | Loader B        | [MACHINE\].rom |
| 2     |       |        |        |                 |                |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 30720 | boot   | mmc    | Kernel image    | tc-boot-\      |
| ition |       |        | blk0p3 |                 | [MACHINE\].img |
| 3     |       |        |        |                 |                |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | c     | system | mmc    | Root file       | automo         |
| ition | ustom |        | blk0p4 | system          | tive-linux-pla |
| 4     |       |        |        |                 | tform-image-\[ |
|       |       |        |        |                 | MACHINE\].ext4 |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 200   | dtb    | mmc    | Device tree     | \[chip_n       |
| ition |       |        | blk0p5 |                 | ame\]-ivi-\[bo |
| 5     |       |        |        |                 | ard_name\].dtb |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 1024  | env    | mmc    | Environment     | \-             |
| ition |       |        | blk0p6 |                 |                |
| 6     |       |        |        |                 |                |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 1024  | misc   | mmc    | Miscellaneous   | \-             |
| ition |       |        | blk0p7 |                 |                |
| 7     |       |        |        |                 |                |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 40960 | splash | mmc    | Splash          | splash_1       |
| ition |       |        | blk0p8 |                 | 920x720x32.img |
| 8     |       |        |        |                 |                |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 5     | home   | mmc    | RW file system\ | home-          |
| ition | 12000 |        | blk0p9 | for home        | directory.ext4 |
| 9     |       |        |        | directory       |                |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 30720 | a7     | mmcb   | Sub-core Kernel | Image-\        |
| ition |       | s_boot | lk0p10 | Image           | [MACHINE\].bin |
| 10    |       |        |        |                 |                |
|       |       |        |        | (optional)      |                |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 200   | a      | mmcb   | Sub-core Device | \[             |
| ition |       | 7s_dtb | lk0p11 | tree            | chip_name\]-iv |
| 11    |       |        |        |                 | i-subcore-\[bo |
|       |       |        |        | (optional)      | ard_name\].dtb |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | c     | a7     | mmcb   | Sub-core root   | te             |
| ition | ustom | s_root | lk0p12 | file system     | lechips-ivi-su |
| 12    |       |        |        |                 | bcore-image-\[ |
|       |       |        |        | (optional)      | MACHINE\].cpio |
+-------+-------+--------+--------+-----------------+----------------+
| Part  | 10    | Data   | mmcb   | User storage    | \-             |
| ition | 48576 |        | lk0p13 |                 |                |
| 13    |       |        |        |                 |                |
+-------+-------+--------+--------+-----------------+----------------+

If you want to add or redefine a partition, follow the steps below and
re-make SD Data.

- Add Partition

The following example shows how to add a partition.

-----------------------------------------------------------------------
<<<<<<< HEAD
=======

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
  \~/release/build-autolinux\$ vi
  poky/meta-telechips/meta-core/classes/make_fai_customer.bbclass

-----------------------------------------------------------------------

+-----------------------------------------------------------------------+
| inherit make_fai                                                      |
|                                                                       |
| make_plist_tcc803x:append() {                                         |
|                                                                       |
| **echo \"example:100M@\" \>\> \${DEPLOY_DIR}/fwdn/partition.list\$1** |
|                                                                       |
| }                                                                     |
+-----------------------------------------------------------------------+

-----------------------------------------------------------------------
<<<<<<< HEAD
=======

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
  \~/release/build-autolinux\$ vi
  poky/meta-telechips/meta-core/classes/tcc-base-image.bbclass

-----------------------------------------------------------------------

+-----------------------------------------------------------------------+
| \#                                                                    |
|                                                                       |
| \# Copyright (C) Telechips Inc.                                       |
|                                                                       |
| \#                                                                    |
|                                                                       |
| inherit core-image extrausers make_fai chk_security                   |
| **make_fai_customer**                                                 |
|                                                                       |
| IMAGE_FSTYPES = \"squashfs ext4\"                                     |
|                                                                       |
| \...                                                                  |
+-----------------------------------------------------------------------+

- Redefine Partition

This example renames an existing partition to **rom_a** and **rom_b**.

-----------------------------------------------------------------------
<<<<<<< HEAD
=======

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
  \~/release/build-autolinux\$ vi
  poky/meta-telechips/meta-core/classes/make_fai_customer.bbclass

-----------------------------------------------------------------------

+-----------------------------------------------------------------------+
| inherit make_fai                                                      |
|                                                                       |
| MAKE_PLIST = \"make_plist_customer\"                                  |
|                                                                       |
| make_plist_customer() {                                               |
|                                                                       |
| **echo \"rom_a:2M@\${DEPLOY_DIR}/images/\${MACHINE}/u-boot.rom\$1\"   |
| \>\> \${DEPLOY_DIR}/fwdn/partition.list\$1**                          |
|                                                                       |
| **echo \"rom_b:2M@\${DEPLOY_DIR}/images/\${MACHINE}/u-boot.rom\$1\"   |
| \>\> \${DEPLOY_DIR}/fwdn/partition.list\$1**                          |
|                                                                       |
| }                                                                     |
+-----------------------------------------------------------------------+

-----------------------------------------------------------------------
<<<<<<< HEAD
=======

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
  \~/release/build-autolinux\$ vi
  poky/meta-telechips/meta-core/classes/tcc-base-image.bbclass

-----------------------------------------------------------------------

+-----------------------------------------------------------------------+
| \#                                                                    |
|                                                                       |
| \# Copyright (C) Telechips Inc.                                       |
|                                                                       |
| \#                                                                    |
|                                                                       |
| inherit core-image extrausers make_fai chk_security                   |
| **make_fai_customer**                                                 |
|                                                                       |
| IMAGE_FSTYPES = \"squashfs ext4\"                                     |
|                                                                       |
| \...                                                                  |
+-----------------------------------------------------------------------+

### Make SNOR ROM Image

Pre-built images are in the following path:

- \"tcc803x_snor_boot.rom\" in boot-firmware_tcc803x/prebuilt

If you need to change the binary stored in the SNOR ROM, you must make a
new SNOR ROM image.

To make SNOR ROM image, use **d3s_snor_mkimage** in boot-firmware as
follows:

+-----------------------------------------------------------------------+
| \$ cd boot-firmware_tcc803x/tools/d3s_snor_mkimage/                   |
|                                                                       |
| \$ ./tcc803x-snor-mkimage-tools -c tcc803x.cfg -o                     |
| ../../tcc803x_snor_boot.rom                                           |
+-----------------------------------------------------------------------+

#### tcc803x.cfg

The \"tcc803x.cfg\" is a list of parameters input to the
**d3s_snor_mkimage**.

**Example:**

+-----------------------------------------------------------------------+
| \# REVISION 1:CS, 2:ES                                                |
|                                                                       |
| REVISION=1                                                            |
|                                                                       |
| \# UART Port configuration                                            |
|                                                                       |
| UART_DEBUG_CFG=35                                                     |
|                                                                       |
| \# SNOR Flash memory size(MByte)                                      |
|                                                                       |
| SNOR_SIZE=4                                                           |
|                                                                       |
| \# Input files                                                        |
|                                                                       |
| BL1_BIN=../../prebuilt/micom-bl1.rom                                  |
|                                                                       |
| MICOM_BIN=../../prebuilt/micom.cs.bin                                 |
|                                                                       |
| UPDATER_BIN=../../prebuilt/r5_sub_fw.bin                              |
|                                                                       |
| HSM_ROM=../../prebuilt/hsm.bin                                        |
|                                                                       |
| KEYPACKAGES_BIN=../../prebuilt/keypackages.bin                        |
+-----------------------------------------------------------------------+

**\
<<<<<<< HEAD
=======

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
**

## Install VTC Driver

Install USB driver (VTC Driver V5.0.0.14) for ***FWDN*** on your Windows
PC. You only need to install this driver once.

![](media/image59.png){width="4.765216535433071in"
height="3.706279527559055in"}

[]{#_Toc167786546 .anchor}Figure 5.1 VTC Driver Installation Screen

Use the VTC driver V5.0.0.14 or higher. If you use a previous version,
install the latest version.

To check the version, confirm the device manager in Windows environment.

The VTC driver installation file (vtcdrv v5.0.0.14.zip) is included in
***fwdn_v8/out*** in the SDK.

## Linux_YP4.0_IVI Firmware Download Sequence

The downloading sequence of ***FWDN*** is as follows:

1.  Set the boot mode switch to USB boot mode.

<!-- -->

1.  Connect 12V power adapter to board.

2.  Open Windows prompt or Linux console and test ***FWDN V8***.

3.  Connect ***FWDN V8*** to board.

4.  Execute the **\--low-format** command by using ***FWDN V8***.

5.  Download pre-built boot F/W image.

6.  Download images to SNOR for CR5 (MICOM).

7.  Download ".fai" file.

8.  Set the boot mode switch to SNOR boot mode or eMMC boot mode and
    reset.

**Note 1:** ***FWDN V8*** runs in Windows 10 or Linux environment.

**Note 2:** Use ***FWDN V8*** v1.4.11 or higher.

### Set Board to USB Boot Mode

Refer to Chapter 2.2.1 and Figure 5.2.

-------------------------------------------------------------------------------------------------------
<<<<<<< HEAD
     **USB Boot Mode**                      **eMMC Boot Mode**                      **SNOR Boot Mode**
------------------------ ----------------------------------------------------- ------------------------
=======

     **USB Boot Mode**                      **eMMC Boot Mode**                      **SNOR Boot Mode**

------------------------ ----------------------------------------------------- ------------------------

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
   ![](media/image16.png)   ![](media/image20.png){width="0.9565212160979878in"   ![](media/image18.png)
                                      height="1.5098807961504812in"}             

-------------------------------------------------------------------------------------------------------

[]{#_Ref156837939 .anchor}Figure 5.2 Boot Mode Switch

### Open Windows Prompt or Linux Console and Test FWDN V8

+-----------------------------------------------------------------------+
| fwdn\> [f                                                             |
| wdn.exe](https://wiki.telechips.com:8443/display/A2/fwdn.exe) \--help |
|                                                                       |
| \[main:30\] FWDN V8 v1.4.12 - 2023.6.22 11:23:58                      |
|                                                                       |
| Usage : fwdn \<command\> \<options\>                                  |
|                                                                       |
| Example:                                                              |
|                                                                       |
| Start to fwdn(load FWDN F/W) :                                        |
|                                                                       |
| fwdn \--fwdn tcc805x_fwdn.json                                        |
|                                                                       |
| Download files written to a config file :                             |
|                                                                       |
| fwdn \--write tcc805x_boot.json                                       |
|                                                                       |
| Download file :                                                       |
|                                                                       |
| fwdn -w \[file name\] -m emmc \--area boot0                           |
|                                                                       |
| fwdn -w \[file name\] -m emmc \--area boot1 -s 512                    |
|                                                                       |
| Download file at GPT partition:                                       |
|                                                                       |
| fwdn -w \[file name\] -m emmc \--area user \--part boot               |
|                                                                       |
| fwdn -w \[file name\] -m ufs \--area user \--part boot \--sector-size |
| 4096                                                                  |
|                                                                       |
| Read dump :                                                           |
|                                                                       |
| fwdn -r \[file name\] -m emmc \--area boot1 \--size 0x100 \--addr     |
| 0x123456                                                              |
|                                                                       |
| fwdn -r \[file name\] -m emmc \--area boot1 \--size 0x100             |
|                                                                       |
| \...                                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

### Connect FWDN V8 to Board

--------------------------------------------------------------------------------
<<<<<<< HEAD
  fwdn\> [fwdn.exe](https://wiki.telechips.com:8443/display/A2/fwdn.exe) \--fwdn
=======

  fwdn\> [fwdn.exe](https://wiki.telechips.com:8443/display/A2/fwdn.exe) \--fwdn

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
  \...\\boot-firmware\\fwdn.json
  
  --------------------------------------------------------------------------------

--------------------------------------------------------------------------------

### Execute \--low-format Command by Using FWDN V8 (Optional)

-----------------------------------------------------------------------------------
<<<<<<< HEAD
  fwdn\> [fwdn.exe](https://wiki.telechips.com:8443/display/A2/fwdn.exe) \--storage
=======

  fwdn\> [fwdn.exe](https://wiki.telechips.com:8443/display/A2/fwdn.exe) \--storage

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
  emmc \--low-format
  
  -----------------------------------------------------------------------------------

-----------------------------------------------------------------------------------

**Note:** This task is optional. If this task is not required, you can
skip this chapter.

### Download Pre-built F/W Image

---------------------------------------------------------------------------
<<<<<<< HEAD
  fwdn\> [fwdn.exe](https://wiki.telechips.com:8443/display/A2/fwdn.exe) -w
=======

  fwdn\> [fwdn.exe](https://wiki.telechips.com:8443/display/A2/fwdn.exe) -w

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
  \...\\boot-firmware\\boot.json
  
  ---------------------------------------------------------------------------

---------------------------------------------------------------------------

### Download Images to SNOR for CR5 (MICOM)

-----------------------------------------------------------------------
<<<<<<< HEAD
  fwdn\> fwdn.exe \--write \...\\prebuilt\\tcc803x_snor_boot.rom \--area
=======

  fwdn\> fwdn.exe \--write \...\\prebuilt\\tcc803x_snor_boot.rom \--area

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
  die1 \--storage snor
  
  -----------------------------------------------------------------------

-----------------------------------------------------------------------

### Download ".FAI" File

---------------------------------------------------------------------------
<<<<<<< HEAD
  fwdn\> [fwdn.exe](https://wiki.telechips.com:8443/display/A2/fwdn.exe) -w
=======

  fwdn\> [fwdn.exe](https://wiki.telechips.com:8443/display/A2/fwdn.exe) -w

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
  \...\\SD_Data.fai \--storage emmc \--area user
  
  ---------------------------------------------------------------------------

---------------------------------------------------------------------------

### Download Images to GPT Partition

If you want to download only a specific partition, follow the example
below: Download "boot.img" to eMMC's boot partition.

Depending on the storage, you should use different option as follows:

---------------------------------------------------------------------------
<<<<<<< HEAD
  fwdn\> [fwdn.exe](https://wiki.telechips.com:8443/display/A2/fwdn.exe) -w
=======

  fwdn\> [fwdn.exe](https://wiki.telechips.com:8443/display/A2/fwdn.exe) -w

>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b
  \...\\boot.img \--storage emmc \--area user \--part boot_a
  
  ---------------------------------------------------------------------------

---------------------------------------------------------------------------

### Complete FWDN and Reset Board

Set the boot mode switch to the desired boot mode and reset the board.

# Booting Guide

This chapter describes booting guide for TCC803x EVB.

## Booting Guide for Board

### Booting Screen

After power is supplied to board for normal booting, U-Boot screen is
shown as follows:

![](media/image61.png){width="2.8319444444444444in"
height="1.0722222222222222in"}

[]{#_Toc40947383 .anchor}Figure 6.1 U-Boot Screen

### Linux Console Login

After firmware writing is completed, you can see the log message on the
Linux console as shown in Figure 6.2.

**Caution:** When resetting the EVB, you must remove USB cable from
USB2.0 DRD port to protect board and host PC.

Connect UART serial cable to PC, to check console message.

- UART configuration is as follows:

<!-- -->

- Baud rate : 115200 bps

- Data bits : 8

- Stop bits : 1

- Parity : None

<!-- -->

- Login ID and Password are **root**.

![](media/image62.png){width="7.276388888888889in"
height="5.388888888888889in"}

[]{#_Ref143248749 .anchor}Figure 6.2 Console Login

# References

1.  Contact Telechips for more details: <sales@telechips.com>

2.  Yocto Project Quick Build:
    <https://docs.yoctoproject.org/dev-manual/start.html>

3.  Yocto Project Wiki: <https://wiki.yoctoproject.org/wiki/Main_Page>

4.  Yocto Project Development Tasks Manual:
    <https://docs.yoctoproject.org/kernel-dev/index.html>

5.  Yocto Project Reference Manual:
    <https://docs.yoctoproject.org/ref-manual/index.html>

6.  Yocto Project Application Development and the Extensible Software
    Development Kit (eSDK):
    <https://docs.yoctoproject.org/sdk-manual/index.html>

7.  BitBake User Manual: <https://docs.yoctoproject.org/bitbake.html>

8.  TCC803x Common Hardware-Assembly Manual for EVB

9.  TCCxxxx Common-User Guide for Firmware Downloader V8

<<<<<<< HEAD
10. TC Common-User Guide for mktcimg

11. TCC803x Common Hardware-User Guide for EVB\
    TCC803x Common Hardware-Quick Start Guide for EVB

12. TCCxxxx Common SDK-User Guide for AUO and BOE touch IC
=======
10.  TC Common-User Guide for mktcimg

11.  TCC803x Common Hardware-User Guide for EVB\
     TCC803x Common Hardware-Quick Start Guide for EVB

12.  TCCxxxx Common SDK-User Guide for AUO and BOE touch IC
>>>>>>> e677cfe877719359b3d25fe6995e71bda3a2127b

**Note**: Reference documents can be provided whenever available,
depending on the terms of a contract. If the reference documents are
unavailable, the contents directly related to your development can be
guided.

# Revision History

## Rev. 1.20: 2024-10-22

- Updated

<!-- -->

- Chapter 2.1: **Important** (modified description)

- Chapter 4.5.1: Website address of repo

- Chapter 4.6.3.4.3: Added **Note**

- Chapter 7: Added \[12\]

<!-- -->

- Deleted

<!-- -->

- Chapter 4.7.7.1: Use Network with Static IP

## Rev. 1.10: 2024-05-31

- Updated

<!-- -->

- Chapter [2.1](#board-description): Table 2.1

- Chapter
  [4.4.1](#linux-distribution-versions-supported-by-yocto-project):
  Website address of Yocto Project

- Chapter 4.4.2: Website address of Yocto Project

- Chapter 4.6.2.1: Source code (deleted pre2 from SDK name)

- Chapter 4.6.2.4:

<!-- -->

- Added description for step 2 (**Choose the manifest to repo**)

- Source code

<!-- -->

- Chapter 4.6.2.7.2: Source code of **modify feature** and **modify
  sub-feature**

- Chapter [4.6.3](#detailed-configuration): Overall description of order
  of sub-chapters

- Chapter
  [4.7.10](#q9.-how-to-build-multi-machine-from-one-kernel-or-u-boot-source):
  Website address of Yocto Project

- Chapter 4.8.1.1: Source code (deleted PRE2 from SDK name)

- Chapter 4.8.1.2: Source code (deleted PRE2 from SDK name)

- Chapter [6.1.2](#linux-console-login): Figure 6.2

- Chapter [7](#references): Website address of Yocto Project (from \[2\]
  to \[7\])

## Rev. 1.00: 2024-04-30

- Updated

<!-- -->

- Chapter 2:

<!-- -->

- Added TCCXXXX_AUO_WLCD_12.3_SV0.1.0

- Added Important

<!-- -->

- Chapter 2.1.3: Added **Note**

- Chapter 3.2.1: Title, Description

- Chapter 4.4.1: Website address of Yocto Project

- Chapter 4.4.2:

<!-- -->

- Website address of Yocto Project

- Deleted Table 4.1 Packages Required for Host Development System to Use
  Yocto Project

<!-- -->

- Chapter 4.6.2.4: Description and Source code

- Chapter 4.6.2.5.1: Source code

- Chapter 4.6.2.5.2: Source code

- Chapter 4.6.2.7.1

<!-- -->

- Added **Note** to **clean all**

- Source code of **clean all**

<!-- -->

- Chapter 4.6.2.7.2: Source code

- Chapter 4.6.3:

<!-- -->

- Deleted manual script build

- Changed title to "Detailed Configuration"

<!-- -->

- Chapter 4.8.1: Description and Source code

- Chapter 4.8.2: Description and Source code

- Chapter 5.4: Deleted Source Code

<!-- -->

- Added

<!-- -->

- Chapter 2.1.3.3 TCCXXXX_AUO_WLCD_12.3\" LCD Sub-board

- Chapter 5.2.2.1 Check eMMC Device Information

- Chapter 5.2.2.2 Create SD Data with eMMC Size

## Rev. 0.90: 2024-01-26

- Preliminary version release

DISCLAIMER

All information and data contained in this material are without any
commitment, are not to be considered as an offer for conclusion of a
contract, nor shall they be construed as to create any liability. Any
new issue of this material invalidates previous issues. Product
availability and delivery are exclusively subject to our respective
order confirmation form; the same applies to orders based on development
samples delivered. By this publication, Telechips, Inc. does not assume
responsibility for patent infringements or other rights of third parties
that may result from its use.

Further, Telechips, Inc. reserves the right to revise this publication
and to make changes to its content, at any time, without obligation to
notify any person or entity of such revisions or changes.

No part of this publication may be reproduced, photocopied, stored on a
retrieval system, or transmitted without the express written consent of
Telechips, Inc.

This product is designed for general purpose, and accordingly customer
be responsible for all or any of intellectual property licenses required
for actual application. Telechips, Inc. does not provide any
indemnification for any intellectual properties owned by third party.

Telechips, Inc. cannot ensure that this application is the proper and
sufficient one for any other purposes but the one explicitly expressed
herein. Telechips, Inc. is not responsible for any special, indirect,
incidental, or consequential damage or loss whatsoever resulting from
the use of this application for other purposes.

Copyright Statement

Copyright in the material provided by Telechips, Inc. is owned by
Telechips unless otherwise noted.

For reproduction or use of Telechips' copyright material, permission
should be sought from Telechips. That permission, if given, will be
subject to conditions that Telechips' name should be included and
interest in the material should be acknowledged when the material is
reproduced or quoted, either in whole or in part. You must not copy,
adapt, publish, distribute, or commercialize any contents contained in
the material in any manner without the written permission of Telechips.
Trademarks used in Telechips' copyright material are the property of
Telechips.

**Important Notice**

This material may include technology owned by the 3rd party licensor and
the technology may be subject to its associated licenses. It is solely
customer\'s responsibility to identify and comply with such licenses. No
other licenses are granted or implied by Telechips with making available
this material.

**[For customers who use licensed Codec ICs and/or licensed codec
firmware of mp3:]{.underline}**

"Supply of this product does not convey a license nor imply any right to
distribute content created with this product in revenue-generating
broadcast systems (terrestrial. Satellite, cable and/or other
distribution channels), streaming applications (via internet, intranets
and/or other networks), other content distribution systems (pay-audio or
audio-on-demand applications and the like) or on physical media (compact
discs, digital versatile discs, semiconductor chips, hard drives, memory
cards and the like). An independent license for such use is required.
For details, please visit <http://mp3licensing.com>".

**[For customers who use other firmware of mp3:]{.underline}**

"Supply of this product does not convey a license under the relevant
intellectual property of Thomson and/or Fraunhofer Gesellschaft nor
imply any right to use this product in any finished end user or
ready-to-use final product. An independent license for such use is
required. For details, please visit <http://mp3licensing.com>".

**[For customers who use Digital Wave DRA solution:]{.underline}**

"Supply of this implementation of DRA technology does not convey a
license nor imply any right to this implementation in any finished
end-user or ready-to-use terminal product. An independent license for
such use is required."

**[For customers who use DTS technology:]{.underline}**

 \"This product made under license to certain U.S. patents and/or
foreign counterparts.\"

 \"© 1996 -- 2011 DTS, Inc. All rights reserved.\"  

**[For customers who use Dolby technology:]{.underline}**

\"Supply of this Implementation of Dolby technology does not convey a
license nor imply a right under any patent, or any other industrial or
intellectual property right of Dolby Laboratories, to use this
Implementation in any finished end-user or ready-to-use final product.
It is hereby notified that a license for such use is required from Dolby
Laboratories.\"

**[For customers who use Google technology:]{.underline}**

 \"Copyright © 2013 Google Inc. All rights reserved."

**[For customers who use MS technology:]{.underline}**

\"This product is subject to certain intellectual property rights of
Microsoft and cannot be used or distributed further without the
appropriate license(s) from Microsoft.\"
