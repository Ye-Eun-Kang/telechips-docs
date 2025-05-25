## Introduction

This document describes the how to useof eMMC, incoulidng interface connection, power connection, and connection method according to speed). eMMC complies with the JESD84-B51 standard published by JEDEC. \[1\]

&nbsp;

### About eMMC (embedded Multi-Media Card)

eMMC is designed for a wide range of application in mobile phones, tablet PC, navigational systems, and industrial field. eMMC is an embedded non-volatile memory system, which simplifies the application interface design and frees the host processor from low-level flash memory management.

&nbsp;

&nbsp;

## eMMC Hardware Information

### eMMC Pin Description

Table 2.1 shows information on eMMC pins conforming to the JEDEC standard.

Table 2.1 eMMC Pin Description

|  **Parameter**   | **Type** | **Description**                                              |
| :--------------: | :------: | :----------------------------------------------------------- |
|  V<sub>cc<sub/>  |  Supply  | Flash  memory I/F and Flash memory power supply              |
| V<sub>ccq <sub/> |  Supply  | Memory  controller core and MMC interface I/O power supply   |
|  V<sub>ss<sub/>  |  Supply  | Flash  memory I/F and Flash memory ground connection         |
| V<sub>ssq<sub/>  |  Supply  | Memory  controller core and MMC I/F ground connection        |
|       VDDi       |    -     | Connect  **VDDi** to ground through 0.1 µF capacitor<br>**Note:** The value presented for each manufacturer differs, so refer to the  manufacturer’s datasheet. |
|       CLK        |  Input   | Clock:  Each cycle directs a 1-bit transfer on the command and DAT lines |
|       CMD        |  Input   | Command:  A bidirectional channel used for device initialization and command transfers     Command  has two operating modes as follows:  <br>  - Open-drain for initialization <br>  - Push-pull for fast command  transfer |
|       DAT0       |   I/O    | Data  I/O0: Bidirectional channel used for data transfer     |
|       DAT1       |   I/O    | Data  I/O1: Bidirectional channel used for data transfer     |
|       DAT2       |   I/O    | Data  I/O2: Bidirectional channel used for data transfer     |
|       DAT3       |   I/O    | Data  I/O3: Bidirectional channel used for data transfer     |
|       DAT4       |   I/O    | Data  I/O4: Bidirectional channel used for data transfer     |
|       DAT5       |   I/O    | Data  I/O5: Bidirectional channel used for data transfer     |
|       DAT6       |   I/O    | Data  I/O6: Bidirectional channel used for data transfer     |
|       DAT7       |   I/O    | Data  I/O7: Bidirectional channel used for data transfer     |
|       RSTN       |  Input   | Reset  signal pin                                            |
|     DS (DQS)     |  Output  | DS:  Data Strobe (HS400 mode)                                |
|       RFU        |    -     | Reserved for  future use                                     |

&nbsp;

&nbsp;

### Hardware Specification

Table 2.2 shows information on the hardware specification of the eMMC conforming to the JEDEC standard.

Table 2.2 Capacitor and Resistor Value

<table style={{ textAlign: 'center' }}>
  <thead>
    <tr>
      <th colspan="1">Parameter</th>
      <th colspan="1">Symbol</th>
      <th colspan="1">MIN</th>
      <th colspan="1">TYP</th>
      <th colspan="1">MAX</th>
      <th colspan="1">Unit</th>
      <th colspan="1">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">CMD</td>
      <td>RCMD</td>
      <td>4.7</td>
      <td>　</td>
      <td>100</td>
      <td>kΩ</td>
      <td>Pull-up resistor&nbsp;&nbsp;&nbsp;for CMD</td>
    </tr>
    <tr>
      <td>RDAT</td>
      <td>10</td>
      <td>　</td>
      <td>100</td>
      <td>kΩ</td>
      <td>Pull-up resistor&nbsp;&nbsp;&nbsp;for DAT0 to 7</td>
    </tr>
    <tr>
      <td>DS (DQS)</td>
      <td>RDS</td>
      <td>10</td>
      <td>　</td>
      <td>100</td>
      <td>kΩ</td>
      <td>Pull-down&nbsp;&nbsp;&nbsp;resistor for DS</td>
    </tr>
    <tr>
      <td rowspan="2">VDDi</td>
      <td rowspan="2">CREG</td>
      <td>0.1</td>
      <td>　</td>
      <td>　</td>
      <td>µF</td>
      <td>To stabilize&nbsp;&nbsp;&nbsp;regulator output when target device bus speed mode is either&nbsp;&nbsp;&nbsp;backward-compatible, high speed SDR, high speed DDR, or HS200</td>
    </tr>
    <tr>
      <td>1</td>
      <td>　</td>
      <td>　</td>
      <td>µF</td>
      <td>To stabilize&nbsp;&nbsp;&nbsp;regulator output when target device bus speed mode is HS400</td>
    </tr>
  </tbody>
</table>

&nbsp;

&nbsp;

## Apply eMMC of TCC803x EVB

### Overview

TCC803x complies with the following specification. \[2\]

- SD Host Controller Specification Version 3.0

- SDIO Card Specification Version 3.0

- eMMC Version 5.1 compliance

  - SD0 channel supports HS400 mode.

  - SD1 and SD2 channels support up to HS200 mode.

    &nbsp;

    


### eMMC Pin Assignment of TCC803x EVB

Table 3.1 shows the TCC803x EVB pin assignment for eMMC interface configuration.

Table 3.1 eMMC Pin Assignment of TCC803x EVB

<table style={{ textAlign: 'center' }}>
  <thead>
    <tr>
      <th colspan="1">Application</th>
      <th colspan="1">Signal Name</th>
      <th colspan="1">Ball Number</th>
      <th colspan="1">Pin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="12">eMMC</td>
      <td>eMMC_CLK</td>
      <td>AB22</td>
      <td>GPIO_SD0_00</td>
    </tr>
    <tr>
      <td>eMMC_CMD</td>
      <td>AG23</td>
      <td>GPIO_SD0_01</td>
    </tr>
    <tr>
      <td>eMMC_D0</td>
      <td>AC22</td>
      <td>GPIO_SD0_02</td>
    </tr>
    <tr>
      <td>eMMC_D1</td>
      <td>AD22</td>
      <td>GPIO_SD0_03</td>
    </tr>
    <tr>
      <td>eMMC_D2</td>
      <td>AB21</td>
      <td>GPIO_SD0_04</td>
    </tr>
    <tr>
      <td



- In the TCC803x EVB, eMMC uses the **GPIO_SD0** port.

  &nbsp;

  

### eMMC Power of TCC803x EVB

Figure 3.1 shows the power assignment of eMMC.

![](https://ye-eun-kang.github.io/documentimage/images/TCC803x/HW/Application%20Note/TCC803x%20Common%20Hardware-Application%20Note%20for%20eMMC/image-20250526072616693.png)

Figure 3.1 Power Block of eMMC

- The output voltage of power supply is 1.8V that is applied to GPSD0 block power.

- The eMMC requires a voltage of 3.3V and 1.8V.

  - 3.3V is used for flash memory I/F and flash memory power supply.


  - 1.8V is used for memory controller core and eMMC interface I/O power supply.

    &nbsp;

    &nbsp;


## eMMC Bus Speed Mode

### eMMC Bus Speed Mode

eMMC defines several bus speed modes. Table 4.1 shows bus speed modes of eMMC.

Table 4.1 Bus Speed Mode of eMMC

|                **Mode Name**                 | **Data Rate** | **I/O Voltage**   **(V)** | **Bus Width**   **(Bit)** | **Frequency**   **(MHz)** | **Maximum Data Transfer (MB/s)**   **(implies x8 bus width)** |
| :------------------------------------------: | :-----------: | :-----------------------: | :-----------------------: | :-----------------------: | :----------------------------------------------------------: |
| Backwards Compatibility with legacy MMC card |    Single     |         3/1.8/1.2         |        1, 4, or 8         |          0 to 26          |                              26                              |
|                High Speed SDR                |    Single     |         3/1.8/1.2         |        1, 4, or 8         |          0 to 52          |                              52                              |
|                High Speed DDR                |     Dual      |         3/1.8/1.2         |          4 or 8           |          0 to 52          |                             104                              |
|                    HS200                     |    Single     |          1.8/1.2          |          4 or 8           |         0 to 200          |                             200                              |
|                    HS400                     |     Dual      |          1.8/1.2          |             8             |         0 to 200          |                             400                              |

&nbsp;

**Note 1:** Data is provided by JEDEC as eMMC standard.

**Note 2:** When using HS400 mode, the maximum operating frequency may vary slightly depending on the vendor of MMC device.

&nbsp;

&nbsp;

### HS200 Mode

eMMC CLK is up to 200 MHz, and high-speed interface timing mode is supported up to 200 MB/s. TCC803x is controlled by 1.8V I/O level. The SD0, SD1, and SD2 channels of the TCC803x support HS200 mode.

&nbsp;

#### Connection Guide

![](https://ye-eun-kang.github.io/documentimage/images/TCC803x/HW/Application%20Note/TCC803x%20Common%20Hardware-Application%20Note%20for%20eMMC/image-20250526074336247.png)

Figure 4.1 HS200 Mode Connection of eMMC

- HS200 mode connects hardware interfaces except DS pin.

- See Table 2.2 for the values of resistors and capacitors.

  &nbsp;

  &nbsp;

### HS400 Mode

eMMC CLK is up to 170 MHz, and high-speed interface timing mode is supported up to 340 MB/s. TCC803x is controlled by 1.8V I/O level. Only SD0 channel of the TCC803x supports HS400 mode.

&nbsp;

#### Connection Guide

![](https://ye-eun-kang.github.io/documentimage/images/TCC803x/HW/Application%20Note/TCC803x%20Common%20Hardware-Application%20Note%20for%20eMMC/image-20250526074343955.png)

Figure 4.2 HS400 Mode Connection of eMMC

- HS400 mode connects hardware interfaces including DS Pin.

- DS signal should be connected to a pull-down resistor by default.

- See Table 2.2 for the values of resistors and capacitors.

  &nbsp;

  &nbsp;

#### DS (DQS) Pin Setting of HS400

The DS (DQS) pin of the eMMC is in a pull-down state based on the JEDEC standard. However, the resistance state[^1] of DS (DQS) pin of eMMC is different for each manufacturer. You should refer to the datasheet of eMMC provided by each manufacturer. Design the pull-down resistor as the default and use it as an option according to the application.

Resistance RDS value is referred in Table 2.2. The value presented for each manufacturer differs, so refer to the manufacturer’s datasheet.

&nbsp;

**Note:** The TCC803x EVB uses SK Hynix’s eMMC. In this case, no external pull-down resistor is needed because the pull-down resistor is embedded with the DS pin.

&nbsp;

&nbsp;

## References

1.  Contact Telechips for more details: <sales@telechips.com>

2.  TCC803x Full Specification.

**Note:** Reference documents can be provided whenever available, depending on the terms of a contract. If the reference documents are unavailable, the contents directly related to your development can be guided.

&nbsp;

&nbsp;

## Revision History

### Rev. 1.00: 2024-05-21

- Updated
  - Chapter 5: added **Note**


&nbsp;

- Changed
  - Title changed from “TCC803x ~~Automotive~~ Common Hardware-Application Note for eMMC”


&nbsp;

### Rev. 0.01: 2020-03-20

- Preliminary version release

&nbsp;

&nbsp;

DISCLAIMER

All information and data contained in this material are without any commitment, are not to be considered as an offer for conclusion of a contract, nor shall they be construed as to create any liability. Any new issue of this material invalidates previous issues. Product availability and delivery are exclusively subject to our respective order confirmation form; the same applies to orders based on development samples delivered. By this publication, Telechips, Inc. does not assume responsibility for patent infringements or other rights of third parties that may result from its use.

Further, Telechips, Inc. reserves the right to revise this publication and to make changes to its content, at any time, without obligation to notify any person or entity of such revisions or changes.

No part of this publication may be reproduced, photocopied, stored on a retrieval system, or transmitted without the express written consent of Telechips, Inc.

This product is designed for general purpose, and accordingly customer be responsible for all or any of intellectual property licenses required for actual application. Telechips, Inc. does not provide any indemnification for any intellectual properties owned by third party.

Telechips, Inc. cannot ensure that this application is the proper and sufficient one for any other purposes but the one explicitly expressed herein. Telechips, Inc. is not responsible for any special, indirect, incidental, or consequential damage or loss whatsoever resulting from the use of this application for other purposes.

Copyright Statement

Copyright in the material provided by Telechips, Inc. is owned by Telechips unless otherwise noted.

For reproduction or use of Telechips’ copyright material, permission should be sought from Telechips. That permission, if given, will be subject to conditions that Telechips’ name should be included and interest in the material should be acknowledged when the material is reproduced or quoted, either in whole or in part. You must not copy, adapt, publish, distribute, or commercialize any contents contained in the material in any manner without the written permission of Telechips. Trademarks used in Telechips’ copyright material are the property of Telechips.

**Important Notice**

This material may include technology owned by the 3rd party licensor and the technology may be subject to its associated licenses. It is solely customer's responsibility to identify and comply with such licenses. No other licenses are granted or implied by Telechips with making available this material.

***For customers who use licensed Codec ICs and/or licensed codec firmware of mp3:***

“Supply of this product does not convey a license nor imply any right to distribute content created with this product in revenue-generating broadcast systems (terrestrial. Satellite, cable and/or other distribution channels), streaming applications (via internet, intranets and/or other networks), other content distribution systems (pay-audio or audio-on-demand applications and the like) or on physical media (compact discs, digital versatile discs, semiconductor chips, hard drives, memory cards and the like). An independent license for such use is required. For details, please visit <http://mp3licensing.com>”.

***For customers who use other firmware of mp3:***

“Supply of this product does not convey a license under the relevant intellectual property of Thomson and/or Fraunhofer Gesellschaft nor imply any right to use this product in any finished end user or ready-to-use final product. An independent license for such use is required. For details, please visit <http://mp3licensing.com>”.

***For customers who use Digital Wave DRA solution:***

“Supply of this implementation of DRA technology does not convey a license nor imply any right to this implementation in any finished end-user or ready-to-use terminal product. An independent license for such use is required.”

***For customers who use DTS technology:***

 "This product made under license to certain U.S. patents and/or foreign counterparts."

 "© 1996 – 2011 DTS, Inc. All rights reserved."  

***For customers who use Dolby technology:***

"Supply of this Implementation of Dolby technology does not convey a license nor imply a right under any patent, or any other industrial or intellectual property right of Dolby Laboratories, to use this Implementation in any finished end-user or ready-to-use final product. It is hereby notified that a license for such use is required from Dolby Laboratories."

***For customers who use Google technology:***

 "Copyright © 2013 Google Inc. All rights reserved.”

***For customers who use MS technology:***

"This product is subject to certain intellectual property rights of Microsoft and cannot be used or distributed further without the appropriate license(s) from Microsoft."

[^1]: Resistance state means Pull-up, Pull-down, or NC.
