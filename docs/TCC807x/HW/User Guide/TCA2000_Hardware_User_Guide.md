


TABLE OF CONTENTS

Contents














































Figures














































Tables


































# Introduction
This document is a hardware user guide for the TCA2000 Evaluation Board (EVB) based on the TCA2000. This document describes system installation, debugging, and detailed information on the overall design and usage of the EVB.

## Terminology
This chapter lists and defines terminologies used in this user guide.


# Block Diagram
## System Block Diagram
Figure 21 shows the system block diagram of the TCA2000 EVB.


Figure 21 System Block Diagram

## Features of TCA2000 EVB
Table 2.1 describes the features of the TCA2000 EVB.

Table 2.1 Features

Note: For inquiries about the EVB, contact Telechips. [1]
# EVB Overview
The TCA2000 EVB can implement the following functions depending on the combination of the interface sub-board.

AI Accelerator
Camera and LiDAR Sensor Fusion

Table 3.1 describes the default configuration of the TCA2000 EVB.

Table 3.1 Default Configuration of TCA2000 EVB


Table 3.2 describes the additional boards that are provided upon request.

Table 3.2 Configuration of Additional Board


Table 3.3 Chip Version


## TCA2000 LPDDR5 Module Board
Figure 3.1 and Figure 3.2 show the top view and bottom view of the TCA2000 module board.


Figure 3.1 TCA2000 Module Board (Top View)

Figure 3.2 TCA2000 Module Board (Bottom View)

Table 3.4 describes the connectors of the TCA2000 module board (bottom view).

Table 3.4 Description of CPU Board (Bottom View)


## TCA2_1000 Motherboard
Figure 3.3 shows the top view of the motherboard.


Figure 3.3 TCA2000 Motherboard (Top View)

Table 3.5 describes motherboard (top view) connectors.

Table 3.5 Description of Motherboard (Top View)


Figure 3.4 shows the bottom view of the motherboard.


Figure 3.4 TCA2000 Motherboard (Bottom View)

Table 3.6 describes the motherboard (bottom view) connectors.

Table 3.6 Description of Motherboard (Bottom View)

Note: Ethernet sub-board is not provided by Telechips.
## MIPI CSI Sub-board
The Mobile Industry Processor Interface (MIPI) CSI sub-board is an interface sub-board to connect cameras.

The MIPI CSI sub-board supports the following camera module.
MAXIM's Gigabit Multimedia Serial Link (GMSL) 50Ω Single-ended Coaxial interface

Note 1: The MIPI CSI sub-board is provided upon request.
Note 2:
GMSL1: TCC803X_MAX9286_VD_POC
GMSL2: TCC805X_MAX96712_4TO1

### Converting GMSL1 to MIPI CSI
The following MIPI CSI sub-board converts GMSL1 to MIPI CSI for MAXIM’s GMSL 50Ω Single-ended Coaxial type camera module.



Table 3.7 describes the GMLS1 to MIPI CSI sub-board connectors.

Table 3.7 Description of GMSL1 to MIPI CSI Sub-board


### Converting GMSL2 to MIPI CSI
The following MIPI CSI sub-board converts GMSL2 to MIPI CSI for MAXIM’s GMSL 50Ω Single-ended Coaxial type camera module.



Table 3.8 describes the GMLS2 to MIPI CSI sub-board connectors.

Table 3.8 Description of GMSL2 to MIPI CSI Sub-board


## External MCU Board
For description of external MCU board, refer to “TCC70xx Common Hardware-User Guide for TCC7022_25_35_45_MCU EVB”. [12]


## External MCU Module
For description of external MCU module, refer to “TCC70xx Common Hardware-User Guide for TCC7022_25_35_45_MCU MOD”. [13]
# Specifications
## LPDDR5
LPDDR5 is located on the module board and the information is as follows:

LPDDR5 for Master Die
Vendor: Samsung
Part number: K3KL8L80QM-MHCT02V
BUS width: 32 bits
Density: 4 GB

Vendor: Samsung
Part number: K3KL3L30DM-JHCU02V
BUS width: 64 bits
Density: 8 GB

LPDDR5 for Slave Die
Vendor: Samsung
Part number: K3KL8L80QM-MHCT02V
BUS width: 32 bits
Density: 4 GB

Vendor: Samsung
Part number: K3KL3L30DM-JHCU02V
BUS width: 64 bits
Density: 8 GB


## Serial NOR Flash Memory
SNOR (Octa SPI type) is located on the module board and the information is as follows:

Vendor: MXIC
Part number: MX25UM51245GXDR00
Density: 512 Mb


## UFS
The UFS memory is located on the motherboard and the information is as follows:

Vendor: KIOXIA
Part number: THGJFGT0T25BAB8
Density: 128 GB


## Power Connector (CON2)
CON2 is an 8-pin DC 12V external power supply connector with a 4.2 mm pitch plug. It is used to supply power to the TCA2000 EVB.
The power supply must provide at least 20 A of current.

Figure 4.1 shows the power connector and plug for the DC 12V power supply.


Figure 4.1 DC 12V Power Supply Connector and Plug

Caution: Compatibility problems may occur if you use an adapter other than the power adapter provided by Telechips.


Figure 4.2 shows the location of CON2 on the motherboard.


Figure 4.2 Power Connector (CON2)


## JTAG Connector (J10D761)
J10D761 is a standard 20-pin/2.54 mm right angle type Pin Header Male for JTAG emulator.
Figure 4.3 shows the location of J10D761 on the motherboard.


Figure 4.3 JTAG Connector (J10D1)


Figure 4.4 shows the schematic of JTAG connector (J10D761).


Figure 4.4 Schematic of JTAG Connector (J10D761)


Table 4.1 describes the pins of J10D761.

Table 4.1 J10D761 Pin Description


## HSSTP Connector (JH2 and JH1)
JH2 and JH1 are 40-pin/0.8 mm board-to-board connectors for Embedded Trace Macrocell (ETM).
JH2 is used for the Master die, and JH1 is used for the Slave die.
Figure 4.5 shows the locations of JH2 and JH1 on the motherboard.


Figure 4.5 HSSTP Connector (JH2 and JH1)

Figure 46 shows the schematic of HSSTP connectors (JH2 and JH1).


Figure 46 Schematic of HSSTP Connectors (JH2 and JH1)

Table 4.2 describes the pins of JH2.

Table 4.2 Description of JH2 Pins


Table 4.3 describes the pins of JH1.

Table 4.3 Description of JH1 Pins



## Boot Mode
The TCA2000 EVB has three switches for booting configuration with BM[2:0], and supports three different boot modes:
USB 2.0 Boot mode
SNOR and UFS Boot mode
UFS Boot mode

Important: BM[3] is a pin used only for a pull-down function in the circuit. Therefore, it is NC and should not be used in boot mode.

The slide switches (JSW2 to JSW4) are used to select the boot modes of the TCA2000 EVB.
For more information on the boot mode of the TCA2000 EVB, refer to “TCA2000 Chip Specification”. [2]

Figure 4.7 shows the location of slide switches on the motherboard.


Figure 4.7 Slide Switches (JSW2, JSW3, and JSW4)

Figure 4.8 shows the schematic of slide switches.


Figure 4.8 Schematic of Slide Switches for Boot Mode

Note: The R78 is located on the module board, and the R6040(NC) is located on the motherboard.

Table 4.4 describes the function of slide switches.

Table 4.4 Description of Slide Switches for Boot Mode


Figure 4.9 shows the circuit connection status based on the slide switch position.


Figure 4.9 Slide Switch Position

### USB Boot Mode
This mode is mainly for firmware update.
In this mode, you can download a program into the user-defined area by using the USB 2.0 port.

Table 4.5 describes the slide switch settings for USB 2.0 boot mode.

Table 4.5 Configuration of USB 2.0 Boot Mode


### SNOR and UFS Boot Mode
The TCA2000 EVB supports SNOR and UFS boot mode by using the M_GPIO_B and UFS TX/RX.
Table 4.6 describes the slide switch settings for SNOR and UFS boot mode.

Table 4.6 Configuration of SNOR and UFS Boot Mode

### UFS Boot Mode
The TCA2000 EVB supports UFS boot mode by using the UFS TX/RX
Table 4.7 describes the slide switch settings for UFS boot mode.

Table 4.7 Configuration of UFS Boot Mode


## Reset (RST) Switch
SW1 is a tact switch to reset the system. The location of the tact switch on the motherboard is shown in Figure 4.10.


Figure 4.10 Tact Switch (SW1)

If you press the RST switch (SW1), the system will be forced to reboot.





## USB Connectors
The TCA2000 EVB supports USB2.0 Device.

JC14 is located on the top side of the motherboard. Refer to Figure 4.11.


Figure 4.11 USB Type-C Connectors (JC14)


JC15 is located on the bottom side of the motherboard. Refer to Figure 4.12.


Figure 4.12 USB Type-C Connectors (JC15)


Table 4.8 describes the connector for each USB.

Table 4.8 Description of USB Connectors

### USB2.0 Connector (JC14)
USB2.0 of the TCA2000 supports USB Device function. JC14 is an USB2.0 Type-C connector for USB2.0 port.
When the TCA2000 EVB is set to USB boot mode, the USB port of the PC should be connected to JC14.


### USB2.0 Connector (JC15)
USB2.0 of the TCA2000 supports USB Device function. JC15 is an USB2.0 Type-C connector for USB2.0 port.
When the TCA2000 EVB is set to USB boot mode, the USB port of the PC should be connected to JC15.


## UART Debug Connector
The JC1 and JC2 are standard USB Type-C connectors. The JC1 and JC2 is located on the bottom side of the motherboard. Refer to Figure 4.13.



Figure 4.13 UART Debug Connectors (JC1 and JC2)


The JC1 is used to output the debug message of the TCA2000 EVB. The debug messages that can be output from EVB are as follows:
Cluster for master die
Safety core for master die
ISP core for master die
ISP core for slave die

The JC2 is used to output the debug message of the TCA2000 EVB. The debug messages that can be output from EVB are as follows:
Cluster for slave die (Optional)
Safety core for slave die (Optional)

On the TCA2000 EVB, the USB to UART bridge controllers are designed for JC1 and JC2, and you can connect JC1 and JC2 directly to PC by using the USB Type-C cable.


## Video In
The TCA2000 EVB supports MIPI-CSI2 4-lane for 2 channels

### MIPI-CSI2 Connector (JH7 and JH6)
JH7 and JH6 are connectors used to interface with the MIPI sub-board.
These connectors are located on the motherboard.
JH7 is used for the Master Die and JH6 is used for the Slave Die.

The TCA2000 EVB supports the following camera module:
MAXIM's GMSL 50Ω Single-ended Coaxial

Note: The MIPI sub-board is provided upon request (optional).

Figure 4.14 shows the location of the JH7 and JH6 on the motherboard.


Figure 4.14 MIPI-CSI2 Connector (JH7 and JH6)

Table 4.9 describes the information of MIPI-CSI2 connector (JH7 and JH6).

Table 4.9 Information of MIPI-CSI2 Connector (JH7 and JH6)
Figure 4.15 shows the schematic of MIPI-CSI2 connector (JH7 and JH6).


Figure 4.15 Schematic of MIPI-CSI2 Connector (JH7 and JH6)

Table 4.10 describes the pins of JH7.

Table 4.10 JH7 Pin Description


Table 4.11 describes the pins of JH6.

Table 4.11 JH6 Pin Description


## Ethernet
The TCA2000 EVB supports six Ethernet MAC controllers.
On the TCA2000 EVB, you can use four RTL8211F transceivers for legacy Ethernet or two 88Q2220 Ethernet AVB transceivers for Ethernet AVB.
JC16, JC17, JC18, and JC19 are RJ45 connectors for 10/100/1000 Mbps Ethernet connections, and JC9 and JC10 are automotive Ethernet connectors for 100/1000 Mbps Ethernet AVB connections.

Figure 4.16 shows the location of JC9, JC10, JC16, JC17, JC18, and JC19 on the motherboard.





Figure 4.16 Automotive Ethernet Connector (JC9 and JC10) and Ethernet RJ45 Connector (JC16, JC17, JC18, and JC19)


### Slide Switch (SW5)
SW5 is used to select 100/1000 Mbps Ethernet AVB (U39) or Ethernet sub-board (JH11).
On the motherboard, U31 is an analog switch for 100/1000 Mbps Ethernet AVB PHY (U39), and U32 is an analog switch for the Ethernet sub-board (JH11).
When U31 is enabled, the Ethernet AVB PHY (U39) is selected. When U32 is enabled, the Ethernet sub-board (JH11) is selected.

The SW5 is located on the motherboard as shown in Figure 4.17.
The Ethernet sub-board (JH11) is located on the bottom side of the motherboard as shown in Figure 4.18.


Figure 4.17 Slide Switch (SW5)


Figure 4.18 Ethernet Sub board (JH11)





Figure 4.19 Schematic of Analog Switches (U31 and U32) and Slide Switch (SW5)


Table 4.12 describes the settings of SW5.

Table 4.12 SW5 Setting


### Slide Switch (SW6)
SW6 is used to select 10/100/1000 Mbps Ethernet transceiver (U82) or Ethernet sub-board (JH10).
On the motherboard, U33 is an analog switch for 10/100/1000 Mbps Ethernet Transceiver (U82), and U34 is an analog switch for the Ethernet sub-board (JH10).
When U33 is enabled, the Ethernet transceiver (U82) is selected. When U34 is enabled, the Ethernet Sub-board (JH10) is selected.

The SW6 is located on the motherboard as shown in Figure 4.20.

The Ethernet sub-board (JH10) is located on the bottom side of the motherboard as shown in Figure 4.21.


Figure 4.20 Slide Switch (SW6)



Figure 4.21 Ethernet Sub board (JH10)



Figure 4.22 shows the schematic of analog switches and a slide switch (U33, U34, and SW6)


Figure 4.22 Schematic of Analog Switches (U33 and U34) and Slide Switch (SW6)



Table 4.13 describes the settings of SW6.

Table 4.13 SW6 Setting

## PCIe Card (JC20 and JC21)
The TCA2000 supports PCIe Gen4 x4 lanes for 2 channels. An edge card is used for PCIe applications on the TCA2000 EVB.
JC20 is for the master die and JC21 for the slave die.
JC20 and JC21 are located on the motherboard as shown in Figure 4.23.


Figure 4.23 PCIe Edge Card (JC20 and JC21)


Figure 4.24 shows the schematic of JC20.


Figure 4.24 Schematic of PCIe Connector (JC20)


Table 4.14 describes the pins of JC20.

Table 4.14 JC20 Pin Description


Figure 4.25 shows the schematic of JC21.


Figure 4.25 Schematic of PCIe Connector (JC21)

Table 4.15 describes the pins of JC21.

Table 4.15 JC21 Pin Description


## CAN Connectors (CON3 and CON4)
The TCA2000 EVB supports 4-channel CAN.
CON3 is for the master die and CON4 for the slave die.

The CON3 and CON4 are located on the motherboard as shown in Figure 4.26.

.
Figure 4.26 CAN Connectors (CON3 and CON4)

Figure 4.27 shows the schematic of CAN connector.


Figure 4.27 Schematic of CAN Connector (CON3 and CON4)

Table 4.16 describes the pins of CON3.

Table 4.16 CON3 Pin Description

Table 4.17 describes the pins of CON4.

Table 4.17 CON4 Pin Description



## Toggle Switches (SW3 and SW4)
In general, system power is controlled by the MCU. However, the TCA2000 EVB has a power control switch that allows the EVB to operate independently of the MCU.
On the TCA2000 EVB, SW3 is used to select system power ON/OFF and SW4 is used to select STR mode.
SW3 and SW4 do not operate when an external MCU is connected.

Note: For details on how to use SW4, refer to Chapter 4.15.1.

The location of the SW3 and SW4 on the motherboard is shown in Figure 4.28.


Figure 4.28 Toggle Switches (SW3 and SW4)

Figure 4.29 shows the schematic of toggle switches (SW3 and SW4).


Figure 4.29 Schematic of Toggle Switches (SW3 and SW4)


Table 4.18 describes the settings of SW3.

Table 4.18 SW3 Setting

Table 4.19 describes the settings of SW4.

Table 4.19 SW4 Setting

### How to use SW4 Toggle Switch
As mentioned in Chapter 4.15, the SW4 toggle switch is used to select STR mode. To properly enter STR mode, the switch must be operated according to the following procedure sequence.
Entering STR Mode
Turn on SW3: Turn on system power by using the system power on/off switch, SW3. (Normal system boot)
Enter the command to enter STR mode with the UART console. (TBD)
Turn on SW4: Activate STR mode by using the STR mode switch, SW4. (STR mode ready state)
Turn off SW3: Turn off system power by using the system power on/off switch, SW3.
The system enters the STR mode.

Exiting STR Mode
Turn on SW3: Turn on system power by using the system power on/off switch, SW3.
The system exits STR mode and enters the ready state.
Turn off SW4: Deactivate STR mode by using the STR mode switch, SW4. (Normal system boot)

Caution: The STR mode switch, SW4, must be operated while SW3 is turned on. SW4 must be turned off before supplying 12V power to the power connector (CON4) described in Chapter 4.4.


## Connector for External Platform SOC
CON9 is a connector for signals from external platform SoC. CON9 is connected to the motherboard by using a 24-pin cable.
CON9 is located on the motherboard as shown in Figure 4.30.


Figure 4.30 Connector for Signals of External Platform SoC (CON9)

Figure 4.31 shows the schematic of external Platform SoC connector (CON9).


Figure 4.31 Schematic of External Platform SoC Connector (CON9)

Table 4.20 describes the pins of CON2.

Table 4.20 CON9 Pin Description


## Connector for External MCU
CON7, CON8, and J14D1 are connectors for external MCU. CON7, CON8, and J14D1 cannot be used at the same time. CON7 and CON8 are connected to the motherboard by using a 24-pin cable, and J14D1 is connected to the motherboard by using a 28-pin Header.
The MCU boards available from Telechips are as follows.
For CON7 and CON8	: TCC7022_25_35_45_MCU
For J14D1		: TCC7022_25_35_45_MOD

Note: The external MCU board is provided upon request (optional).

These connectors are located on the main board as shown in Figure 4.32 and Figure 4.33.


Figure 4.32 Connector for External MCU (CON7 and CON8)

Figure 4.33 Connector for External MCU (J14D1)


Figure 4.34 shows the schematic of external MCU connector (CON7 and CON8).


Figure 4.34 Schematic of External MCU Connector (CON7 and CON8)


Figure 4.35 shows the schematic of external MCU connector (J14D1).


Figure 4.35 Schematic of External MCU Connector (J14D1)

Table 4.21 describes the pins of CON7.

Table 4.21 CON7 Pin Description



Table 4.22 describes the pins of CON8.

Table 4.22 CON8 Pin Description


Table 4.23 describes the pins of J14D1.

Table 4.23 J14D1 Pin Description


# References
Contact Telechips for more details:
TCA2000 Chip Specification
TCA2000 Common Hardware-Quick Start Guide for EVB
TCA2000 Common Hardware-Assembly Manual for EVB
TCA2000_GPIO Assignment
Reference Schematic TCA2000_LPD5_MOD EVB
Reference Schematic TCA2000_MOTHER EVB
Reference Schematic TCC803X_MAX9286_VD_POC EVB
Reference Schematic TCC805X_MAX96712_4TO1 EVB
Reference Schematic TCC7022_25_35_45_MCU
Reference Schematic TCC7022_25_35_45_MOD
TCC70xx Common Hardware-User Guide for TCC7022_25_35_45_MCU EVB
TCC70xx Common Hardware-User Guide for TCC7022_25_35_45_MCU MOD

Note: Reference documents can be provided whenever available, depending on the terms of a contract. If the reference documents are unavailable, the contents directly related to your development can be guided.
# Revision History
## Rev. 0.10: 2025-03-14
Preliminary version release



DISCLAIMER

This material is being made available solely for your internal use with its products and service offerings of Telechips, Inc (“Telechips”). and/or licensors and shall not be used for any other purposes. This material may not be altered, edited, or modified in any way without Telechips’ prior written approval. Unauthorized use or disclosure of this material or the information contained herein is strictly prohibited, and you agree to indemnify Telechips and licensors for any damages or losses suffered by Telechips and/or licensors for any unauthorized uses or disclosures of this material, in whole or part. Further, Telechips, Inc. reserves the right to revise this material and to make changes to its content, at any time, without obligation to notify any person or entity of such revisions or changes.

THIS MATERIAL IS BEING PROVIDED “AS IS” WITHOUT WARRANTY OF ANY KIND, WHETHER EXPRESSED, IMPLIED, STATUTORY OR OTHERWISE. TO THE MAXIMUM EXTENT PERMITTED BY LAW, TELECHIPS AND/OR LICENSORS SPECIFICALLY DISCLAIM ALL WARRANTIES OF TITLE, MERCHANTABILITY, NON-INFRINGEMENT, FITNESS FOR A PARTICULAR PURPOSE, SATISFACTORY QUALITY, COMPLETENESS OR ACCURACY, AND ALL WARRANTIES ARISING OUT OF TRADE USAGE OR OUT OF A COURSE OF DEALING OR COURSE OF PERFORMANCE. MOREOVER, NEITHER TELECHIPS, INC. NOR LICENSORS, SHALL BE LIABLE TO YOU OR ANY THIRD PARTY FOR ANY EXPENSES, LOSSES, USE, OR ACTIONS HOWSOEVER INCURRED OR UNDERTAKEN BY YOU IN RELIANCE ON THIS MATERIAL.

THIS MATERIAL IS DESIGNED FOR GENERAL PURPOSE, AND ACCORDINGLY YOU ARE RESPONSIBLE FOR ALL OR ANY OF INTELLECTUAL PROPERTY LICENSES REQUIRED FOR ACTUAL APPLICATION. TELECHIPS, INC. DOES NOT PROVIDE ANY INDEMNIFICATION FOR ANY INTELLECTUAL PROPERTIES OWNED BY THIRD PARTY.


Copyright Statement


Copyright in this material provided by Telechips, Inc. is owned by Telechips unless otherwise noted. For reproduction or use of Telechips’ copyright material, prior written consent should be obtained from Telechips. That prior written consent, if given, will be subject to conditions that Telechips’ name should be included and interest in the material should be acknowledged when the material is reproduced or quoted, either in whole or in part. You must not copy, adapt, publish, distribute, or commercialize any contents contained in the material in any manner without the written permission of Telechips. Trademarks used in Telechips’ copyright material are the property of Telechips.
