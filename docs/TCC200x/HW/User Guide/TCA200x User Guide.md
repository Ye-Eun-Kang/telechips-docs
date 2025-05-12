[TOC]



# 1     Introduction

This document is a hardware user guide for the TCA2000 Evaluation Board (EVB) based on the TCA2000. This document describes system installation, debugging, and detailed information on the overall design and usage of the EVB.

 

## 1.1    Terminology

This chapter lists and defines terminologies used in this user guide.

 

| **Terminology** | **Definition**                                               |
| --------------- | ------------------------------------------------------------ |
| CAN             | Flexible  Controller Area Network peripheral                 |
| Ethernet AVB    | Audio  Video Bridging over Ethernet                          |
| ETM             | Embedded  Trace Macrocell                                    |
| EVB             | Evaluation  Board                                            |
| GMSL            | Gigabit  Multimedia Serial Link                              |
| GND             | Ground                                                       |
| GPIO            | General  Purpose Input Output                                |
| I2C             | Inter-integrated  Circuit interface                          |
| ISP             | Image  Signal Processor                                      |
| JTAG            | Joint  Test Action Group                                     |
| LPDDR5          | Low Power DDR5 DRAM                                          |
| MCU             | Microcontroller  Unit                                        |
| MIPI CSI        | Mobile  Industry Processor Interface Camera Serial interface |
| PCIe            | Peripheral  Component Interconnect Express                   |
| P-SOC           | Platform  SoC                                                |
| PMIC            | Power  Management Integrated Circuit                         |
| SNOR            | Serial  NOR flash memory                                     |
| SPI             | Serial  Peripheral Interface                                 |
| STR             | Suspend  To Resume                                           |
| UART            | Universal  Asynchronous Receiver/Transmitter                 |
| UFS             | Universal  Flash Storage                                     |
| USB             | Universal  Serial Bus                                        |

 

# 2    Block Diagram

## 2.1   System Block Diagram

Figure 2.1 shows the system block diagram of the TCA2000 EVB.

​                             



 

## 2.2   Features of TCA2000 EVB

Table 2.1 describes the features of the TCA2000 EVB.

 

**Table 2.1 Features**

| **Function**                        | **Description**                                              | **Note**                                                     |             |
| ----------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ----------- |
| Application Processor               | TCA2000                                                      | Master cluster: Cortex-A76  Quad             DynamIQ Shared Unit (DSU)  Slave cluster: Cortex-A76 Quad   DynamIQ Shared Unit (DSU) |             |
| Safety Processor                    | TCA2000                                                      | Cortex-M7 Single                                             |             |
| Neural Processing Unit (NPU)        | TCA2000                                                      | Sapeon X340 core  x10   200 TOPS                             |             |
| Memory                              | LPDDR5                                                       | Maximum Clock: 3200 MHz  Density: 32 Gb x2,  64Gb x2  Vendor: Samsung   Part number: K3KL8L80QM-MHCT02V(32 Gb)   K3KL3L30DM-JHCU02V  (64 Gb) |             |
| Serial-NOR Flash                    | Density: 512 Mb  Vendor: MXIC  Part number: MX25UM51245GXDR00 |                                                              |             |
| UFS                                 | UFS3.1  Density: 128 GB  Vendor: KIOXIA  Part number: THGJFGT0T25BAB8  (128 GB) |                                                              |             |
| Video In                            | MIPI CSI                                                     | 2-channel  MIPI CSI2 4-lane                                  |             |
| Peripheral                          | CAN                                                          | Three CAN Transceivers  Vendor: Microchip  Part number: MCP2562FD-E/SN | Not mounted |
| Ethernet Audio Video Bridging (AVB) | Ethernet  AVB PHY 1000Base-T1  Vendor:  Marvell  Part  number: 88Q2220 |                                                              |             |
| Ethernet                            | Ethernet  PHY 1000Base-T  Vendor:  Realtek  Part  number: RTL8211F |                                                              |             |
| X-TAL                               | Master                                                       | 24 MHz Crystal  Oscillator                                   |             |
| Slave                               | 24 MHz Crystal  Oscillator                                   |                                                              |             |
| Connector                           | JTAG                                                         | Standard  20-pin/2.54 mm Right Angle type Pin Header Male  n System debugging |             |
| External MCU                        | Standard 28-pin/2 mm  Pin Header Male  n MCU Sub-board       | Sub-board  name:  TCC7022_25_35_45_MOD                       |             |
| External P-SOC                      | 2 mm pitch 24-pin Right angle                                |                                                              |             |
| HSSTP                               | Vendor: Samtec  Port number: ASP-130367-01  0.8mm pitch 40-pin  n ~~Debugging s~~System  debugging |                                                              |             |
| USB2.0 Device                       | n USB2.0 Type-C  20-pin  x 2                                 | One for  Master  One for Slave for Test                      |             |
| MIPI CSI                            | Vendor: Amphenol FCI  Part number: 61082-041402LF  0.8 mm pitch 40-pin  MIPI CSI Sub-board | Sub-board  name:  TCC805X_MAX96712_4TO1_SVx.x  TCC803X_MAX9286_VD_POC_SVx.x |             |
| PCIe                                | Edge Card x2                                                 |                                                              |             |
| Ethernet                            | RJ45 x4                                                      |                                                              |             |
| Ethernet AVB                        | TE B1 Connector x2                                           |                                                              |             |
| External MCU                        | Connector for  connection with external MCU  2 mm pitch 24-pin Right Angle  x2 | EVB name:  TCC7022_25_35_45_MCU~~_Vx.x.x~~                   |             |
| DC Power Jack                       | ~~ ~~Vendor: Molex  Part number: 39-30-0080  4.2mm pitch 8-pin | 13A/pin                                                      |             |
| Jack                                | Power ACC On/Off                                             | Toggle switch  ~~ ~~Part  number: SMTS-102-2C3               |             |
| Switch                              | STR mode                                                     | Toggle switch  Part  number: SMTS-102-2C3                    |             |
| Boot mode                           | Three 3-pin slide switches                                   |                                                              |             |
| Reset                               | System reset switch                                          |                                                              |             |

 

**Note:** For inquiries about the EVB, contact Telechips. [1]

# 3     EVB Overview



The TCA2000 EVB can implement the following functions depending on the combination of the interface sub-board.

- AI Accelerator
- Camera and LiDAR Sensor Fusion

 

Table 3.1 describes the default configuration of the TCA2000 EVB.

 

**Table 3.1 Default Configuration of TCA2000 EVB**

|     **Board Name**      |            **Description**             |
| :---------------------: | :------------------------------------: |
| TCA2000_LPD5_MOD_V0.1.0 | AI Accelerator module board for LPDDR5 |
| TCA2_1000_MOTHER_V0.1.0 |              Motherboard               |

 

 

Table 3.2 describes the additional boards that are provided upon request.

 

**Table 3.2 Configuration of Additional Board**

|     **Board Name**     |                   **Description**                   |
| :--------------------: | :-------------------------------------------------: |
| TCC803X_MAX9286_VD_POC | MIPI camera sub-board for converting GMSL1 to MIPI  |
| TCC805X_MAX96712_4TO1  | MIPI camera sub-board for  converting GMSL2 to MIPI |
|  TCC7022_25_35_45_MCU  |                 External MCU board                  |
|  TCC7022_25_35_45_MOD  |                 External MCU module                 |

 

 

**Table 3.3 Chip Version**

| **Category** | **Making Information** |                       **Chip Marking**                       |          **Note**           |
| :----------: | :--------------------: | :----------------------------------------------------------: | :-------------------------: |
|  TCA2000 ES  |          OXX           | ![image-20250509160734576](C:\Users\jekim\AppData\Roaming\Typora\typora-user-images\image-20250509160734576.png) | Initial  version of TCA2000 |

 



 

## 3.1    TCA2000 LPDDR5 Module Board

Figure 3.1 and Figure 3.2 show the top view and bottom view of the TCA2000 module board. 

 ![image-20250509160832079](C:\Users\jekim\AppData\Roaming\Typora\typora-user-images\image-20250509160832079.png)

 **Figure 3.1 TCA2000 Module Board (Top View)**






**Figure 3.2 TCA2000 Module Board (Bottom View)**

 

Table 3.4 describes the connectors of the TCA2000 module board (bottom view).

 

**Table 3.4 Description of CPU Board (Bottom View)**

| **Number** | **Reference Number** |         **Name**         |                       **Description**                        |
| :--------: | :------------------: | :----------------------: | :----------------------------------------------------------: |
|     1      |         J11          | 120-pin B to B Connector |         Connect the module board to the  motherboard         |
|     2      |          J8          | 200-pin B to B Connector |         Connect the module board to the  motherboard         |
|     3      |         J10          | 150-pin B to B Connector | Connect the module board to the  motherboard   Only for testing purpose |

 



 

## 3.2    TCA2_1000 Motherboard

Figure 3.3 shows the top view of the motherboard.

 ![image-20250509161651436](C:\Users\jekim\AppData\Roaming\Typora\typora-user-images\image-20250509161651436.png)

  

**Figure 3.3 TCA2000 Motherboard (Top View)**

 

Table 3.5 describes motherboard (top view) connectors.

 

**Table 3.5 Description of Motherboard (Top View)**

| **Number** | **Reference Number** | **Name**                      | **Description**                                              |
| ---------- | -------------------- | ----------------------------- | ------------------------------------------------------------ |
| 1          | CON4                 | Dual D-Sub Connector          | CAN Connector for Slave Die                                  |
| 2          | CON3                 | Dual D-Sub Connector          | CAN Connector for Master Die                                 |
| 3          | JH3                  | 4-pin Header Male             | Connect to a cable for FAN  power and control signal         |
| 4          | SW4                  | Toggle Switch                 | Switch to change to Suspend To RAM(STR)  mode                |
| 5          | SW3                  | Toggle Switch                 | Switch for power enable signal                               |
| 6          | CON2                 | Power Jack                    | 12V Power Jack                                               |
| 7          | JC14                 | USB Type-C Connector          | USB device connector to  download firmware for Master Die    |
| 8          | J20                  | PCIe Edge Card                | PCIe Edge Card for Master Die                                |
| 9          | J19                  | 200-pin B to B Connector      | Connect the motherboard to the  module board                 |
| 10         | J21                  | 120-pin B to B Connector      | Connect the motherboard to the  module board                 |
| 11         | J23                  | 150-pin B to B Connector      | Connect the motherboard to the  module board                 |
| 12         | J14D1                | 28-pin Header Male            | Connect to the ~~ ~~external MCU sub-board ~~board~~         |
| 13         | CON9                 | 24-pin Right Angle Header Box | Connect to the external P-SOC  signals                       |
| 14         | SW6                  | Slide Switch                  | Select the Ethernet PHY or  Ethernet sub-board               |
| 15         | CON7, CON8           | 24-pin Right Angle Header Box | Connect to the external MCU  signals                         |
| 16         | JC19                 | RJ45 Connector                | Legacy Ethernet port for LiDAR                               |
| 17         | JC16                 | RJ45 Connector                | Legacy Ethernet port for LiDAR                               |
| 18         | JC17                 | RJ45 Connector                | Legacy Ethernet port for LiDAR                               |
| 19         | JC18                 | RJ45 Connector                | Legacy Ethernet port for LiDAR                               |
| 20         | SW1                  | Tact Switch                   | Switch for system reset  (GRESET)                            |
| 21         | JC10                 | TE B1 Connector               | Ethernet AVB port                                            |
| 22         | JC9                  | TE B1 Connector               | Ethernet AVB port                                            |
| 23         | SW8, SW7, SW10, SW9  | Slide Switch                  | Configuration for Ethernet AVB  PHY (U40 and~~,~~  U39)      |
| 24         | SW5                  | Slide Switch                  | Select the Ethernet AVB PHY or  Ethernet sub-board           |
| 25         | CON1                 | 10-pin Right Angle Header Box | Connect to remote control board’s  signals                   |
| 26         | JC21                 | PCIe Edge Card                | PCIe Edge Card for Slave Die                                 |
| 27         | J10D761              | 20-pin Right Angle Header Box | JTAG header for system debug                                 |
| 28         | JH1                  | 40-pin Mezzanine Connector    | Connect to the High-Speed  Serial Transmit Port (HSSTP) for Slave Die |
| 29         | JSW2, JSW3, JSW4     | Slide Switch                  | Select the boot mode of system                               |
| 30         | JH2                  | 40-pin Mezzanine Connector    | Connect to the High-Speed  Serial Transmit Port (HSSTP) for Master Die |

 

Table 3.6 describes the motherboard (bottom view) connectors.

 

**Table 3.6 Description of Motherboard (Bottom View)**

| **Number** | **Reference Number** | **Name**                   | **Description**                                              |
| ---------- | -------------------- | -------------------------- | ------------------------------------------------------------ |
| 1          | JH11                 | 40-pin Mezzanine Connector | Connect to Ethernet Sub board  for Master Die                |
| 2          | JH10                 | 40-pin Mezzanine Connector | Connect to Ethernet Sub board  for Slave Die                 |
| 3          | JC1                  | USB Type-C Connector       | UART debug port for Master CPU  cluster, Master SIC and ISP  |
| 4          | JC2                  | USB Type-C Connector       | UART debug port for Slave CPU  cluster and Slave SIC (Optional) |
| 5          | JH7                  | 40-pin Mezzanine Connector | Connect to the MIPI-CSI  sub-board for Master Die            |
| 6          | JH6                  | 40-pin Mezzanine Connector | Connect to the MIPI-CSI  sub-board for Slave Die             |
| 7          | JC15                 | USB Type-C Connector       | USB device connector to  download firmware for Slave Die (Optional) |

 **Note:** Ethernet sub-board is not provided by Telechips.





## 3.3    MIPI CSI Sub-board

The Mobile Industry Processor Interface (MIPI) CSI sub-board is an interface sub-board to connect cameras.

 

The MIPI CSI sub-board supports the following camera module.

n MAXIM's Gigabit Multimedia Serial Link (GMSL) 50Ω Single-ended Coaxial interface

 

**Note 1:** The MIPI CSI sub-board is provided upon request.

**Note 2:** 

- GMSL1: TCC803X_MAX9286_VD_POC
- GMSL2: TCC805X_MAX96712_4TO1

 

### 3.3.1    Converting GMSL1 to MIPI CSI

The following MIPI CSI sub-board converts GMSL1 to MIPI CSI for MAXIM’s GMSL 50Ω Single-ended Coaxial type camera module.

  

Table 3.7 describes the GMLS1 to MIPI CSI sub-board connectors.



 **Table 3.7 Description of GMSL1 to MIPI CSI Sub-board**

| **Number** | **Reference**  **Number** | **Name**                   | **Description**                                              |
| ---------- | ------------------------- | -------------------------- | ------------------------------------------------------------ |
| 1          | CON1,2,3,4                | FAKRA Connector            | 4-channel input is  available for camera module.  GMSL 50Ω Single-ended  Coaxial cable |
| 2          | JP2,3,4,5                 | 4-pin Header Connector     | Connect to power supply                                      |
| 3          | JSW1,2,3,4,5,6            | Slide Switch               | Select mode                                                  |
| 4          | JH1                       | 40-pin Mezzanine Connector | Connect to the CPU board                                     |



 



 

### 3.3.2    Converting GMSL2 to MIPI CSI

Table 3.8 describes the GMLS2 to MIPI CSI sub-board connectors.

 

**Table 3.8 Description of GMSL2 to MIPI CSI Sub-board**

| **Number** | **Reference**  **Number** | **Name**                   | **Description**                                              |
| ---------- | ------------------------- | -------------------------- | ------------------------------------------------------------ |
| 1          | CON1,2,3,4                | FAKRA Connector            | 4-channel  input is available for camera module.  GMSL 50Ω Single-ended  Coaxial cable |
| 2          | JP6,7,8,9                 | 4-pin Header Connector     | Connect  to power supply                                     |
| 3          | JH1                       | 40-pin Mezzanine Connector | Connect  to the CPU board                                    |

 

 

## 3.4    External MCU Board

For description of external MCU board, refer to *“TCC70xx Common Hardware-User Guide for TCC7022_25_35_45_MCU EVB*”. [12]

 

 

## 3.5    External MCU Module

For description of external MCU module, refer to *“TCC70xx Common Hardware-User Guide for TCC7022_25_35_45_MCU MOD*”. [13]







# 4     Specifications

## 4.1    LPDDR5

LPDDR5 is located on the module board and the information is as follows:

 

LPDDR5 for Master Die

- Vendor: Samsung
- Part number: K3KL8L80QM-MHCT02V
- BUS width: 32 bits  
- Density: 4 GB

 

- Vendor: Samsung
- Part number: K3KL3L30DM-JHCU02V
- BUS width: 64 bits 
- Density: 8 GB

 

LPDDR5 for Slave Die

- Vendor: Samsung
- Part number: K3KL8L80QM-MHCT02V
- BUS width: 32 bits  
- Density: 4 GB

 

- Vendor: Samsung
- Part number: K3KL3L30DM-JHCU02V
- BUS width: 64 bits  
- Density: 8 GB

 

## 4.2    Serial NOR Flash Memory

SNOR (Octa SPI type) is located on the module board and the information is as follows:

 

- Vendor: MXIC
- Part number: MX25UM51245GXDR00 
- Density: 512 Mb



 

 

## 4.3    UFS

The UFS memory is located on the motherboard and the information is as follows:

 

- Vendor: KIOXIA
- Part number: THGJFGT0T25BAB8
- Density: 128 GB

 



 

## 4.4    Power Connector (CON2)

CON2 is an 8-pin DC 12V external power supply connector with a 4.2 mm pitch plug. It is used to supply power to the TCA2000 EVB.

The power supply must provide at least 20 A of current.



 

**Caution:** Compatibility problems may occur if you use an adapter other than the power adapter provided by Telechips.

 

 

## 4.5    JTAG Connector (J10D761)

J10D761 is a standard 20-pin/2.54 mm right angle type Pin Header Male for JTAG emulator. 

 

Table 4.1 describes the pins of J10D761.

 

**Table 4.1 J10D761 Pin Description**

| **Pin   Number**          | **Schematic   Net Name** | **DIR** | **Description**  |
| ------------------------- | ------------------------ | ------- | ---------------- |
| **Mother ◄**► **J10D761** |                          |         |                  |
| 1                         | JTAG_3P3                 | -       | Power 3.3V       |
| 2                         | JTAG_3P3                 | -       | Power 3.3V       |
| 3                         | TRSTn                    | **◄**   | Test Reset       |
| 4                         | DGND                     | -       | Ground           |
| 5                         | TDI                      | **◄**   | Test Data In     |
| 6                         | DGND                     | -       | Ground           |
| 7                         | TMS                      | **◄**   | Test Mode State  |
| 8                         | DGND                     | -       | Ground           |
| 9                         | TCK                      | **◄**   | Test Clock       |
| 10                        | DGND                     | -       | Ground           |
| 11                        | DGND                     | -       | Ground           |
| 12                        | DGND                     | -       | Ground           |
| 13                        | TDO                      | ►       | Test Data Output |
| 14                        | DGND                     | -       | Ground           |
| 15                        | JTAG_RSTn                | **◄**   | System Reset     |
| 16                        | DGND                     | -       | Ground           |
| 17                        | NC                       | -       | Not Connected    |
| 18                        | DGND                     | -       | Ground           |
| 19                        | NC                       | -       | Not Connected    |
| 20                        | DGND                     | -       | Ground           |

 



 

## 4.6    HSSTP Connector (JH2 and JH1)

JH2 and JH1 are 40-pin/0.8 mm board-to-board connectors for Embedded Trace Macrocell (ETM). JH2 is used for the Master die, and JH1 is used for the Slave die.



 

Table 4.2 describes the pins of JH2.

 

**Table 4.2 Description of JH2 Pins**

| **Pin Number**     | **Schematic Net Name** | **DIR** | **Description**                                  |
| ------------------ | ---------------------- | ------- | ------------------------------------------------ |
| **CPU ◄**► **JH2** |                        |         |                                                  |
| 1                  | NC                     | -       | Not  Connected                                   |
| 2                  | NC                     | -       | Not  Connected                                   |
| 3                  | NC                     | -       | Not  Connected                                   |
| 4                  | NC                     | -       | Not  Connected                                   |
| 5                  | DGND                   | -       | Ground                                           |
| 6                  | DGND                   | -       | Ground                                           |
| 7                  | NC                     | -       | Not  Connected                                   |
| 8                  | NC                     | -       | Not  Connected                                   |
| 9                  | NC                     | -       | Not  Connected                                   |
| 10                 | NC                     | -       | Not  Connected                                   |
| 11                 | DGND                   | -       | Ground                                           |
| 12                 | DGND                   | -       | Ground                                           |
| 13                 | M_HSSTP_LN0_TXP        | ►       | The  differential output data pair of Lane 0 TXP |
| 14                 | NC                     | -       | Not  Connected                                   |
| 15                 | M_HSSTP_LN0_TXM        | ►       | The  differential output data pair of Lane 0 TXM |
| 16                 | NC                     | -       | Not  Connected                                   |
| 17                 | DGND                   | -       | Ground                                           |
| 18                 | DGND                   | -       | Ground                                           |
| 19                 | NC                     | -       | Not  Connected                                   |
| 20                 | NC                     | -       | Not  Connected                                   |
| 21                 | NC                     | -       | Not  Connected                                   |
| 22                 | NC                     | -       | Not  Connected                                   |
| 23                 | DGND                   | -       | Ground                                           |
| 24                 | DGND                   | -       | Ground                                           |
| 25                 | M_HSSTP_LN1_TXP        | ►       | The  differential output data pair of Lane 1 TXP |
| 26                 | NC                     | -       | Not  Connected                                   |
| 27                 | M_HSSTP_LN1_TXM        | ►       | The differential  output data pair of Lane 1 TXM |
| 28                 | NC                     | -       | Not  Connected                                   |
| 29                 | DGND                   | -       | Ground                                           |
| 30                 | DGND                   | -       | Ground                                           |
| 31                 | NC                     | -       | Not  Connected                                   |
| 32                 | NC                     | -       | Not  Connected                                   |
| 33                 | NC                     | -       | Not  Connected                                   |
| 34                 | NC                     | -       | Not  Connected                                   |
| 35                 | DGND                   | -       | Ground                                           |
| 36                 | NC                     | -       | Not  Connected                                   |
| 37                 | NC                     | -       | Not Connected                                    |
| 38                 | NC                     | -       | Not  Connected                                   |
| 39                 | NC                     | -       | Not  Connected                                   |
| 40                 | NC                     | -       | Not  Connected                                   |

  

Table 4.3 describes the pins of JH1.

 

**Table 4.3 Description of JH1 Pins**

| **Pin Number**     | **Schematic Net Name** | **DIR** | **Description**                                  |
| ------------------ | ---------------------- | ------- | ------------------------------------------------ |
| **CPU ◄**► **JH1** |                        |         |                                                  |
| 1                  | NC                     | -       | Not Connected                                    |
| 2                  | NC                     | -       | Not  Connected                                   |
| 3                  | NC                     | -       | Not  Connected                                   |
| 4                  | NC                     | -       | Not  Connected                                   |
| 5                  | DGND                   | -       | Ground                                           |
| 6                  | DGND                   | -       | Ground                                           |
| 7                  | NC                     | -       | Not  Connected                                   |
| 8                  | NC                     | -       | Not  Connected                                   |
| 9                  | NC                     | -       | Not  Connected                                   |
| 10                 | NC                     | -       | Not  Connected                                   |
| 11                 | DGND                   | -       | Ground                                           |
| 12                 | DGND                   | -       | Ground                                           |
| 13                 | S_HSSTP_LN0_TXP        | ►       | The  differential output data pair of Lane 0 TXP |
| 14                 | NC                     | -       | Not  Connected                                   |
| 15                 | S_HSSTP_LN0_TXM        | ►       | The  differential output data pair of Lane 0 TXM |
| 16                 | NC                     | -       | Not  Connected                                   |
| 17                 | DGND                   | -       | Ground                                           |
| 18                 | DGND                   | -       | Ground                                           |
| 19                 | NC                     | -       | Not  Connected                                   |
| 20                 | NC                     | -       | Not Connected                                    |
| 21                 | NC                     | -       | Not  Connected                                   |
| 22                 | NC                     | -       | Not  Connected                                   |
| 23                 | DGND                   | -       | Ground                                           |
| 24                 | DGND                   | -       | Ground                                           |
| 25                 | S_HSSTP_LN1_TXP        | ►       | The  differential output data pair of Lane 1 TXP |
| 26                 | NC                     | -       | Not  Connected                                   |
| 27                 | S_HSSTP_LN1_TXM        | ►       | The  differential output data pair of Lane 1 TXM |
| 28                 | NC                     | -       | Not  Connected                                   |
| 29                 | DGND                   | -       | Ground                                           |
| 30                 | DGND                   | -       | Ground                                           |
| 31                 | NC                     | -       | Not  Connected                                   |
| 32                 | NC                     | -       | Not  Connected                                   |
| 33                 | NC                     | -       | Not  Connected                                   |
| 34                 | NC                     | -       | Not  Connected                                   |
| 35                 | DGND                   | -       | Ground                                           |
| 36                 | NC                     | -       | Not  Connected                                   |
| 37                 | NC                     | -       | Not  Connected                                   |
| 38                 | NC                     | -       | Not  Connected                                   |
| 39                 | NC                     | -       | Not  Connected                                   |
| 40                 | NC                     | -       | Not  Connected                                   |

 

 



 

## 4.7    Boot Mode

The TCA2000 EVB has three switches for booting configuration with BM[2:0], and supports three different boot modes:

- USB 2.0 Boot mode 
- SNOR and UFS Boot mode 
- UFS Boot mode

 

**Important:** BM[3] is a pin used only for a pull-down function in the circuit. Therefore, it is NC and should not be used in boot mode.

 

The slide switches (JSW2 to JSW4) are used to select the boot modes of the TCA2000 EVB.

For more information on the boot mode of the TCA2000 EVB, refer to “*TCA2000 Chip Specification*”. [2]

 

**Note:** The R78 is located on the module board, and the R6040(NC) is located on the motherboard.



 

Table 4.4 describes the function of slide switches.

 

**Table 4.4 Description of Slide Switches for Boot Mode**

| **Reference Number** | **Function Name** | **Description**           |
| -------------------- | ----------------- | ------------------------- |
| JSW2                 | BM2               | Boot mode bit2 of TCA2000 |
| JSW3                 | BM1               | Boot mode bit1 of TCA2000 |
| JSW4                 | BM0               | Boot mode bit0 of TCA2000 |

 

 



### 4.7.1    USB Boot Mode

This mode is mainly for firmware update. In this mode, you can download a program into the user-defined area by using the USB 2.0 port.

 Table 4.5 describes the slide switch settings for USB 2.0 boot mode.

 

**Table 4.5 Configuration of USB 2.0 Boot Mode**

| **Pin**       | **Value** | **Figure** |
| ------------- | --------- | ---------- |
| BM3 (JSW1)_NC | Low(0)    |            |
| BM2 (JSW2)    | Low(0)    |            |
| BM1 (JSW3)    | Low(0)    |            |
| BM0 (JSW4)    | Low(0)    |            |

 

 

### 4.7.2    SNOR and UFS Boot Mode

The TCA2000 EVB supports SNOR and UFS boot mode by using the M_GPIO_B and UFS TX/RX. Table 4.6 describes the slide switch settings for SNOR and UFS boot mode.

 

**Table 4.6 Configuration of SNOR and UFS Boot Mode**

| **Pin**       | **Value** | **Figure** |
| ------------- | --------- | ---------- |
| BM3 (JSW1)_NC | Low(0)    |            |
| BM2 (JSW2)    | Low(0)    |            |
| BM1 (JSW3)    | High(1)   |            |
| BM0 (JSW4)    | High(1)   |            |



 

### 4.7.3    UFS Boot Mode

The TCA2000 EVB supports UFS boot mode by using the UFS TX/RX. Table 4.7 describes the slide switch settings for UFS boot mode.

 

**Table 4.7 Configuration of UFS Boot Mode**

| **Pin**       | **Value** | **Figure** |
| ------------- | --------- | ---------- |
| BM3 (JSW1)_NC | Low(0)    |            |
| BM2 (JSW2)    | High(1)   |            |
| BM1 (JSW3)    | High(1)   |            |
| BM0 (JSW4)    | Low(0)    |            |

 

 



## 4.8    Reset (RST) Switch

SW1 is a tact switch to reset the system. The location of the tact switch on the motherboard is shown in Figure 4.10.

 If you press the RST switch (SW1), the system will be forced to reboot.

 

 

 

 



 

## 4.9    USB Connectors

The TCA2000 EVB supports USB2.0 Device.  JC14 is located on the top side of the motherboard. Refer to Figure 4.11.  

JC15 is located on the bottom side of the motherboard. Refer to Figure 4.12.

 Table 4.8 describes the connector for each USB.

 

**Table 4.8 Description of USB Connectors** 

| **Reference Number** | **Function**  | **Description**                         |      |
| -------------------- | ------------- | --------------------------------------- | ---- |
| JC14                 | USB2.0 Device | USB2.0 Type-C Connector  for master die |      |
| JC15                 | USB2.0 Device | USB2.0 Type-C Connector  for slave die  |      |

 

### 4.9.1    USB2.0 Connector (JC14)

USB2.0 of the TCA2000 supports USB Device function. JC14 is an USB2.0 Type-C connector for USB2.0 port.

When the TCA2000 EVB is set to USB boot mode, the USB port of the PC should be connected to JC14. 

  

### 4.9.2    USB2.0 Connector (JC15)

USB2.0 of the TCA2000 supports USB Device function. JC15 is an USB2.0 Type-C connector for USB2.0 port.

When the TCA2000 EVB is set to USB boot mode, the USB port of the PC should be connected to JC15. 



 



## 4.10  UART Debug Connector

The JC1 and JC2 are standard USB Type-C connectors. The JC1 and JC2 is located on the bottom side of the motherboard. Refer to Figure 4.13.

 

- The JC1 is used to output the debug message of the TCA2000 EVB. The debug messages that can be output from EVB are as follows:

  - Cluster for master die

  - Safety core for master die

  - ISP core for master die

  - ISP core for slave die

 

- The JC2 is used to output the debug message of the TCA2000 EVB. The debug messages that can be output from EVB are as follows:
  - Cluster for slave die (Optional)
  - Safety core for slave die (Optional)

 

- On the TCA2000 EVB, the USB to UART bridge controllers are designed for JC1 and JC2, and you can connect JC1 and JC2 directly to PC by using the USB Type-C cable.

 



 

## 4.11  Video In

The TCA2000 EVB supports MIPI-CSI2 4-lane for 2 channels

 

### 4.11.1  MIPI-CSI2 Connector (JH7 and JH6)

JH7 and JH6 are connectors used to interface with the MIPI sub-board.

 

**Table 4.9 Information of MIPI-CSI2 Connector (JH7 and JH6)** 

| **Item**                | **Description** |
| ----------------------- | --------------- |
| Vendor                  | FCI             |
| Manufacture Part Number | 61082-041402LF  |
| Connector Type          | Receptacle      |
| Mounting Type           | Surface  Mount  |
| Number of Positions     | 40              |
| Number of Rows          | 2               |
| Row Pitch               | 0.8  mm         |



| **Part Number** | **Figure** | **U33** | **U34** | **Description**                                              |                                                              |
| --------------- | ---------- | ------- | ------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| SW6             |            |         | Enable  | Disable                                                      | Default setting of TCA2000 EVB  Ethernet transceiver (U82) is selected.  Ethernet sub-board (JH10) is not selected. |
|                 |            | Disable | Enable  | Ethernet sub-board (JH10) is selected.  Ethernet transceiver (U82) is not selected. |                                                              |



 

## 3.13  PCIe Card (JC20 and JC21)

The TCA2000 supports PCIe Gen4 x4 lanes for 2 channels. An edge card is used for PCIe applications on the TCA2000 EVB.

JC20 is for the master die and JC21 for the slave die.

JC20 and JC21 are located on the motherboard as shown in Figure 4.23.

 

​     

​        JC21        

​        JC20        

​      



Figure 4.23 PCIe Edge Card (JC20 and JC21)

 

 

Figure 4.24 shows the schematic of JC20.

 

  

Figure 4.24 Schematic of PCIe Connector (JC20)

 

 

Table 4.14 describes the pins of JC20.

 

Table 4.14 JC20 Pin Description

| **Pin Number**              | **JC20**               |                |                 |                             |
| --------------------------- | ---------------------- | -------------- | --------------- | --------------------------- |
| **TCA2000**   **Port Name** | **Schematic Net Name** | **DIR**        | **Description** |                             |
| **Mother ◄**► **JC20**      |                        |                |                 |                             |
| A1                          | M_GPIO_E08             | M_PCIe_DETn    | ►               | PCIe Card Detection         |
| A2                          | -                      | M_PCIe_12P0    | -               | Power 12V                   |
| A3                          | -                      | M_PCIe_12P0    | -               | Power 12V                   |
| A4                          | -                      | DGND           | -               | Ground                      |
| A5                          | -                      | NC             | -               | Not Connected               |
| A6                          | -                      | NC             | -               | Not Connected               |
| 7                           | -                      | NC             | -               | Not Connected               |
| A8                          | -                      | NC             | -               | Not Connected               |
| A9                          | -                      | M_PCIe_3P3     | -               | Power 3.3V                  |
| A10                         | -                      | M_PCIe_3P3     | -               | Power 3.3V                  |
| A11                         | M_GPIO_E09             | M_PCIe_RSTn    | **◄**           | PCIe Reset                  |
| A12                         | -                      | DGND           | -               | Ground                      |
| A13                         | MST_PCIE_REFCLK_P      | M_PCIe_CLK_P   | **◄**           | PCIe Positive Clock         |
| A14                         | MST_PCIE_REFCLK_M      | M_PCIe_CLK_N   | **◄**           | PCIe Negative Clock         |
| A15                         | -                      | DGND           | -               | Ground                      |
| A16                         | MST_PCIE_TXP0          | M_PCIe_TXP0    | ►               | PCIe Transmit Positive Data |
| A17                         | MST_PCIE_TXN0          | M_PCIe_TXN0    | ►               | PCIe Transmit Negative Data |
| A18                         | -                      | DGND           | -               | Ground                      |
| A19                         | -                      | NC             | -               | Not Connected               |
| A20                         | -                      | DGND           | -               | Ground                      |
| A21                         | MST_PCIE_TXP1          | M_PCIe_TXP1    | ►               | PCIe Transmit Positive Data |
| A22                         | MST_PCIE_TXN1          | M_PCIe_TXN1    | ►               | PCIe Transmit Negative Data |
| A23                         | -                      | DGND           | -               | Ground                      |
| A24                         | -                      | DGND           | -               | Ground                      |
| A25                         | MST_PCIE_TXP2          | M_PCIe_TXP2    | ►               | PCIe Transmit Positive Data |
| A26                         | MST_PCIE_TXN2          | M_PCIe_TXN2    | ►               | PCIe Transmit Negative Data |
| A27                         | -                      | DGND           | -               | Ground                      |
| A28                         | -                      | DGND           | -               | Ground                      |
| A29                         | MST_PCIE_TXP3          | M_PCIe_TXP3    | ►               | PCIe Transmit Positive Data |
| A30                         | MST_PCIE_TXN3          | M_PCIe_TXN3    | ►               | PCIe Transmit Negative Data |
| A31                         | -                      | DGND           | -               | Ground                      |
| A32                         | -                      | NC             | -               | Not Connected               |
| B1                          | -                      | M_PCIe_12P0    | -               | Power 12V                   |
| B2                          | -                      | M_PCIe_12P0    | -               | Power 12V                   |
| B3                          | -                      | M_PCIe_12P0    | -               | Power 12V                   |
| B4                          | -                      | DGND           | -               | Ground                      |
| B5                          | -                      | NC             | -               | Not Connected               |
| B6                          | -                      | NC             | -               | Not Connected               |
| B7                          | -                      | DGND           | -               | Ground                      |
| B8                          | -                      | M_PCIe_3P3     | -               | Power 3.3V                  |
| B9                          | -                      | NC             |                 | Not Connected               |
| B10                         | -                      | M_PCIe_AUX_3P3 |                 | AUX Power 3.3V              |
| B11                         | M_GPIO_E06             | M_PCIe_WAKEn   | **◄**           | PCIe Wake                   |
| B12                         | M_GPIO_E08             | M_PCIe_CLKREQn | ►               | PCIe Clock Request          |
| B13                         | -                      | DGND           | -               | Ground                      |
| B14                         | MST_PCIE_RXP0          | M_PCIe_RXP0    | **◄**           | PCIe Receive Positive Data  |
| B15                         | MST_PCIE_RXN0          | M_PCIe_RXN0    | **◄**           | PCIe Receive Negative Data  |
| B16                         | -                      | DGND           | -               | Ground                      |
| B17                         | M_GPIO_E08             | M_PCIe_DETn    | ►               | PCIe Card Detection         |
| B18                         | -                      | DGND           | -               | Ground                      |
| B19                         | MST_PCIE_RXP1          | M_PCIe_RXP1    | **◄**           | PCIe Receive Positive Data  |
| B20                         | MST_PCIE_RXN1          | M_PCIe_RXN1    | **◄**           | PCIe Receive Negative Data  |
| B21                         | -                      | DGND           | -               | Ground                      |
| B22                         | -                      | DGND           | -               | Ground                      |
| B23                         | MST_PCIE_RXP2          | M_PCIe_RXP2    | **◄**           | PCIe Receive Positive Data  |
| B24                         | MST_PCIE_RXN2          | M_PCIe_RXN2    | **◄**           | PCIe Receive Negative Data  |
| B25                         | -                      | DGND           | -               | Ground                      |
| B26                         | -                      | DGND           | -               | Ground                      |
| B27                         | MST_PCIE_RXP3          | M_PCIe_RXP3    | **◄**           | PCIe Receive Positive Data  |
| B28                         | MST_PCIE_RXN3          | M_PCIe_RXN3    | **◄**           | PCIe Receive Negative Data  |
| B29                         | -                      | DGND           | -               | Ground                      |
| B30                         | -                      | NC             | -               | Not Connected               |
| B31                         | M_GPIO_E08             | M_PCIe_DETn    | ►               | PCIe Card Detection         |
| B32                         | -                      | DGND           | -               | Ground                      |

 



 

Figure 4.25 shows the schematic of JC21.

 

  

Figure 4.25 Schematic of PCIe Connector (JC21)

 

Table 4.15 describes the pins of JC21.

 

Table 4.15 JC21 Pin Description

| **Pin Number**              | **JC21**               |                |                 |                             |
| --------------------------- | ---------------------- | -------------- | --------------- | --------------------------- |
| **TCA2000**   **Port Name** | **Schematic Net Name** | **DIR**        | **Description** |                             |
| **CPU ◄**► **JC21**         |                        |                |                 |                             |
| A1                          | S_GPIO_E08             | S_PCIe_DETn    | ►               | PCIe Card Detection         |
| A2                          | -                      | S_PCIe_12P0    | -               | Power 12V                   |
| A3                          | -                      | S_PCIe_12P0    | -               | Power 12V                   |
| A4                          | -                      | DGND           | -               | Ground                      |
| A5                          | -                      | NC             | -               | Not Connected               |
| A6                          | -                      | NC             | -               | Not Connected               |
| 7                           | -                      | NC             | -               | Not Connected               |
| A8                          | -                      | NC             | -               | Not Connected               |
| A9                          | -                      | S_PCIe_3P3     | -               | Power 3.3V                  |
| A10                         | -                      | S_PCIe_3P3     | -               | Power 3.3V                  |
| A11                         | S_GPIO_E09             | S_PCIe_RSTn    | **◄**           | PCIe Reset                  |
| A12                         | -                      | DGND           | -               | Ground                      |
| A13                         | SLV_PCIE_REFCLK_P      | S_PCIe_CLK_P   | **◄**           | PCIe Positive Clock         |
| A14                         | SLV _PCIE_REFCLK_M     | S_PCIe_CLK_N   | **◄**           | PCIe Negative Clock         |
| A15                         | -                      | DGND           | -               | Ground                      |
| A16                         | SLV _PCIE_TXP0         | S_PCIe_TXP0    | ►               | PCIe Transmit Positive Data |
| A17                         | SLV _PCIE_TXN0         | S_PCIe_TXN0    | ►               | PCIe Transmit Negative Data |
| A18                         | -                      | DGND           | -               | Ground                      |
| A19                         | -                      | NC             | -               | Not Connected               |
| A20                         | -                      | DGND           | -               | Ground                      |
| A21                         | SLV _PCIE_TXP1         | S_PCIe_TXP1    | ►               | PCIe Transmit Positive Data |
| A22                         | SLV _PCIE_TXN1         | S_PCIe_TXN1    | ►               | PCIe Transmit Negative Data |
| A23                         | -                      | DGND           | -               | Ground                      |
| A24                         | -                      | DGND           | -               | Ground                      |
| A25                         | SLV _PCIE_TXP2         | S_PCIe_TXP2    | ►               | PCIe Transmit Positive Data |
| A26                         | SLV _PCIE_TXN2         | S_PCIe_TXN2    | ►               | PCIe Transmit Negative Data |
| A27                         | -                      | DGND           | -               | Ground                      |
| A28                         | -                      | DGND           | -               | Ground                      |
| A29                         | SLV _PCIE_TXP3         | S_PCIe_TXP3    | ►               | PCIe Transmit Positive Data |
| A30                         | SLV _PCIE_TXN3         | S_PCIe_TXN3    | ►               | PCIe Transmit Negative Data |
| A31                         | -                      | DGND           | -               | Ground                      |
| A32                         | -                      | NC             | -               | Not Connected               |
| B1                          | -                      | S_PCIe_12P0    | -               | Power 12V                   |
| B2                          | -                      | S_PCIe_12P0    | -               | Power 12V                   |
| B3                          | -                      | S_PCIe_12P0    | -               | Power 12V                   |
| B4                          | -                      | DGND           | -               | Ground                      |
| B5                          | -                      | NC             | -               | Not Connected               |
| B6                          | -                      | NC             | -               | Not Connected               |
| B7                          | -                      | DGND           | -               | Ground                      |
| B8                          | -                      | S_PCIe_3P3     | -               | Power 3.3V                  |
| B9                          | -                      | NC             |                 | Not Connected               |
| B10                         | -                      | S_PCIe_AUX_3P3 |                 | AUX Power 3.3V              |
| B11                         | S_GPIO_E06             | S_PCIe_WAKEn   | **◄**           | PCIe Wake                   |
| B12                         | S_GPIO_E08             | S_PCIe_CLKREQn | ►               | PCIe Clock Request          |
| B13                         | -                      | DGND           | -               | Ground                      |
| B14                         | SLV _PCIE_RXP0         | S_PCIe_RXP0    | **◄**           | PCIe Receive Positive Data  |
| B15                         | SLV _PCIE_RXN0         | S_PCIe_RXN0    | **◄**           | PCIe Receive Negative Data  |
| B16                         | -                      | DGND           | -               | Ground                      |
| B17                         | S_GPIO_E08             | S_PCIe_DETn    | ►               | PCIe Card Detection         |
| B18                         | -                      | DGND           | -               | Ground                      |
| B19                         | SLV _PCIE_RXP1         | S_PCIe_RXP1    | **◄**           | PCIe Receive Positive Data  |
| B20                         | SLV _PCIE_RXN1         | S_PCIe_RXN1    | **◄**           | PCIe Receive Negative Data  |
| B21                         | -                      | DGND           | -               | Ground                      |
| B22                         | -                      | DGND           | -               | Ground                      |
| B23                         | SLV _PCIE_RXP2         | S_PCIe_RXP2    | **◄**           | PCIe Receive Positive Data  |
| B24                         | SLV _PCIE_RXN2         | S_PCIe_RXN2    | **◄**           | PCIe Receive Negative Data  |
| B25                         | -                      | DGND           | -               | Ground                      |
| B26                         | -                      | DGND           | -               | Ground                      |
| B27                         | SLV _PCIE_RXP3         | S_PCIe_RXP3    | **◄**           | PCIe Receive Positive Data  |
| B28                         | SLV _PCIE_RXN3         | S_PCIe_RXN3    | **◄**           | PCIe Receive Negative Data  |
| B29                         | -                      | DGND           | -               | Ground                      |
| B30                         | -                      | NC             | -               | Not Connected               |
| B31                         | S_GPIO_E08             | S_PCIe_DETn    | ►               | PCIe Card Detection         |
| B32                         | -                      | DGND           | -               | Ground                      |

 



 

## 3.14  CAN Connectors (CON3 and CON4)

The TCA2000 EVB supports 4-channel CAN.

CON3 is for the master die and CON4 for the slave die. 

 

The CON3 and CON4 are located on the motherboard as shown in Figure 4.26.

​     

​        CON3        

​        CON4        

 



   .

Figure 4.26 CAN Connectors (CON3 and CON4)

 

Figure 4.27 shows the schematic of CAN connector.

 

  

Figure 4.27 Schematic of CAN Connector (CON3 and CON4)

 

Table 4.16 describes the pins of CON3.

 

Table 4.16 CON3 Pin Description

| **Pin Number**         | **CON3** |                 |                            |
| ---------------------- | -------- | --------------- | -------------------------- |
| **Schematic Net Name** | **DIR**  | **Description** |                            |
| **Mother ◄**► **CON3** |          |                 |                            |
| 1                      | NC       | -               | Not  Connected             |
| 2                      | CAN0_L   | **◄**►          | CAN Low-level voltage I/O  |
| 3                      | DGND     | -               | Ground                     |
| 4                      | NC       | -               | Not  Connected             |
| 5                      | NC       | -               | Not  Connected             |
| 6                      | DGND     | -               | Ground                     |
| 7                      | CAN0_H   | **◄**►          | CAN High-level voltage I/O |
| 8                      | NC       | -               | Not  Connected             |
| 9                      | CAN_5P0  | -               | Power 5V                   |
| 10                     | DGND     | -               | Ground                     |
| 11                     | NC       | -               | Not  Connected             |
| 12                     | CAN1_L   | **◄**►          | CAN Low-level voltage I/O  |
| 13                     | DGND     | -               | Ground                     |
| 14                     | NC       | -               | Not  Connected             |
| 15                     | NC       | -               | Not  Connected             |
| 16                     | DGND     | -               | Ground                     |
| 17                     | CAN1_H   | **◄**►          | CAN High-level voltage I/O |
| 18                     | NC       | -               | Not  Connected             |
| 19                     | CAN_5P0  | -               | Power 5V                   |
| 20                     | DGND     | -               | Ground                     |
| 21                     | DGND     | -               | Ground                     |
| 22                     | DGND     | -               | Ground                     |

 

Table 4.17 describes the pins of CON4.

 

Table 4.17 CON4 Pin Description

| **Pin Number**         | **CON4** |                 |                            |      |
| ---------------------- | -------- | --------------- | -------------------------- | ---- |
| **Schematic Net Name** | **DIR**  | **Description** |                            |      |
| **Mother ◄**► **CON4** |          |                 |                            |      |
| 1                      | NC       | -               | Not  Connected             |      |
| 2                      | CAN2_L   | **◄**►          | CAN Low-level voltage I/O  |      |
| 3                      | DGND     | -               | Ground                     |      |
| 4                      | NC       | -               | Not  Connected             |      |
| 5                      | NC       | -               | Not  Connected             |      |
| 6                      | DGND     | -               | Ground                     |      |
| 7                      | CAN2_H   | **◄**►          | CAN High-level voltage I/O |      |
| 8                      | NC       | -               | Not  Connected             |      |
| 9                      | CAN_5P0  | -               | Power 5V                   |      |
| 10                     | DGND     | -               | Ground                     |      |
| 11                     | NC       | -               | Not  Connected             |      |
| 12                     | CAN3_L   | **◄**►          | CAN Low-level voltage I/O  |      |
| 13                     | DGND     | -               | Ground                     |      |
| 14                     | NC       | -               | Not  Connected             |      |
| 15                     | NC       | -               | Not  Connected             |      |
| 16                     | DGND     | -               | Ground                     |      |
| 17                     | CAN3_H   | **◄**►          | CAN High-level voltage I/O |      |
| 18                     | NC       | -               | Not  Connected             |      |
| 19                     | CAN_5P0  | -               | Power 5V                   |      |
| 20                     | DGND     | -               | Ground                     |      |
| 21                     | DGND     | -               | Ground                     |      |
| 22                     | DGND     | -               | Ground                     |      |

 

 



 

## 4.15  Toggle Switches (SW3 and SW4)

In general, system power is controlled by the MCU. However, the TCA2000 EVB has a power control switch that allows the EVB to operate independently of the MCU.

On the TCA2000 EVB, SW3 is used to select system power ON/OFF and SW4 is used to select STR mode.

SW3 and SW4 do not operate when an external MCU is connected.

 

**Note:** For details on how to use SW4, refer to Chapter 4.15.1.





 

Table 4.18 describes the settings of SW3.

 

Table 4.18 SW3 Setting

| **Part Number**            | **Function**                  | **Figure** | **Value**            | **Description** |                     |
| -------------------------- | ----------------------------- | ---------- | -------------------- | --------------- | ------------------- |
| **Switch**  **(Top View)** | **Switch**  **(Bottom View)** |            |                      |                 |                     |
| SW3                        | System Power                  |            |                      | 3.3V            | Power is turned on. |
|                            |                               | 0V         | Power is turned off. |                 |                     |

 

Table 4.19 describes the settings of SW4.

 

Table 4.19 SW4 Setting

| **Part Number**            | **Function**                  | **Figure** | **Value**               | **Description** |                        |
| -------------------------- | ----------------------------- | ---------- | ----------------------- | --------------- | ---------------------- |
| **Switch**  **(Top View)** | **Switch**  **(Bottom View)** |            |                         |                 |                        |
| SW4                        | STR mode                      |            |                         | 3.3V            | STR mode is turned on. |
|                            |                               | 0V         | STR mode is turned off. |                 |                        |

 

### 4.15.1  How to use SW4 Toggle Switch

As mentioned in Chapter 4.15, the SW4 toggle switch is used to select STR mode. To properly enter STR mode, the switch must be operated according to the following procedure sequence.

n Entering STR Mode

1. Turn on SW3: Turn on system power by using the system power on/off switch, SW3. (Normal system boot)
2. Enter the command to enter STR mode with the UART console. (TBD)
3. Turn on SW4: Activate STR mode by using the STR mode switch, SW4. (STR mode ready state)
4. Turn off SW3: Turn off system power by using the system power on/off switch, SW3.

The system enters the STR mode.

 

n Exiting STR Mode

1. Turn on SW3: Turn on system power by using the system power on/off switch, SW3. 

The system exits STR mode and enters the ready state.

2. Turn off SW4: Deactivate STR mode by using the STR mode switch, SW4. (Normal system boot)

 

**Caution:** The STR mode switch, SW4, must be operated while SW3 is turned on. SW4 must be turned off before supplying 12V power to the power connector (CON4) described in Chapter 4.4.

 

 



# 5     References

[1]  Contact Telechips for more details: [sales@telechips.com](mailto:sales@telechips.com)

[2]  TCA2000 Chip Specification

[3]  TCA2000 Common Hardware-Quick Start Guide for EVB 

[4]  TCA2000 Common Hardware-Assembly Manual for EVB

[5]  TCA2000_GPIO Assignment

[6]  Reference Schematic TCA2000_LPD5_MOD EVB

[7]  Reference Schematic TCA2000_MOTHER EVB

[8]  Reference Schematic TCC803X_MAX9286_VD_POC EVB

[9]  Reference Schematic TCC805X_MAX96712_4TO1 EVB

[10] Reference Schematic TCC7022_25_35_45_MCU

[11] Reference Schematic TCC7022_25_35_45_MOD

[12] TCC70xx Common Hardware-User Guide for TCC7022_25_35_45_MCU EVB

[13] TCC70xx Common Hardware-User Guide for TCC7022_25_35_45_MCU MOD

 

**Note**: Reference documents can be provided whenever available, depending on the terms of a contract. If the reference documents are unavailable, the contents directly related to your development can be guided.





# 6     Revision History



## Rev. 0.10: 2025-03-14

n Preliminary version release

 

 



DISCLAIMER

​            

This material is being made available solely for your internal use with its products and service offerings of Telechips, Inc (“Telechips”). and/or licensors and shall not be used for any other purposes. This material may not be altered, edited, or modified in any way without Telechips’ prior written approval. Unauthorized use or disclosure of this material or the information contained herein is strictly prohibited, and you agree to indemnify Telechips and licensors for any damages or losses suffered by Telechips and/or licensors for any unauthorized uses or disclosures of this material, in whole or part. Further, Telechips, Inc. reserves the right to revise this material and to make changes to its content, at any time, without obligation to notify any person or entity of such revisions or changes.

 

THIS MATERIAL IS BEING PROVIDED “AS IS” WITHOUT WARRANTY OF ANY KIND, WHETHER EXPRESSED, IMPLIED, STATUTORY OR OTHERWISE. TO THE MAXIMUM EXTENT PERMITTED BY LAW, TELECHIPS AND/OR LICENSORS SPECIFICALLY DISCLAIM ALL WARRANTIES OF TITLE, MERCHANTABILITY, NON-INFRINGEMENT, FITNESS FOR A PARTICULAR PURPOSE, SATISFACTORY QUALITY, COMPLETENESS OR ACCURACY, AND ALL WARRANTIES ARISING OUT OF TRADE USAGE OR OUT OF A COURSE OF DEALING OR COURSE OF PERFORMANCE. MOREOVER, NEITHER TELECHIPS, INC. NOR LICENSORS, SHALL BE LIABLE TO YOU OR ANY THIRD PARTY FOR ANY EXPENSES, LOSSES, USE, OR ACTIONS HOWSOEVER INCURRED OR UNDERTAKEN BY YOU IN RELIANCE ON THIS MATERIAL.

 

THIS MATERIAL IS DESIGNED FOR GENERAL PURPOSE, AND ACCORDINGLY YOU ARE RESPONSIBLE FOR ALL OR ANY OF INTELLECTUAL PROPERTY LICENSES REQUIRED FOR ACTUAL APPLICATION. TELECHIPS, INC. DOES NOT PROVIDE ANY INDEMNIFICATION FOR ANY INTELLECTUAL PROPERTIES OWNED BY THIRD PARTY.

 

 

Copyright Statement

 

 

Copyright in this material provided by Telechips, Inc. is owned by Telechips unless otherwise noted. For reproduction or use of Telechips’ copyright material, prior written consent should be obtained from Telechips. That prior written consent, if given, will be subject to conditions that Telechips’ name should be included and interest in the material should be acknowledged when the material is reproduced or quoted, either in whole or in part. You must not copy, adapt, publish, distribute, or commercialize any contents contained in the material in any manner without the written permission of Telechips. Trademarks used in Telechips’ copyright material are the property of Telechips.

 

------

