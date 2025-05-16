# 1         Introduction

This document describes Linux_YP4.0_IVI usage as follows:

n  Board Description for TCC807x EVB

n  Board Assembly Guide for TCC807x EVB

n  Build Guide for Linux_YP4.0_IVI

n  FWDN Guide for TCC807x in Linux_YP4.0_IVI

n  Booting Guide for TCC807x EVB

# 2         Board Description

## 2.1    EVB Version

Table 2.1 EVB Version

|**Board**|**Board Name/Version**|
|---|---|
|CPU board for LPDDR4/4X|TCC807X_LPD4_4X322_V1.0.0|
|CPU board for LPDDR5|TCC8070_LPD5322_V1.0.0|
|Main Board|TCC807X_MAIN_V1.0.0|
|UART Sub-board|TCC80XX_UART_CP2102_SV0.1.0|
|12.3” 1920x720 LCD|TCC80XX_BOE_WLCD_12.3_SV1.1.1<br><br>TCCXXXX_AUO_WLCD_12.3_SV0.1.0|

**Note:** For more details, refer to “_TCC807x Common Hardware-Assembly Manual for EVB”_. [8]

**Important:** The default LCD setting of Linux_YP4.0_IVI is fitted with “TCCXXXX_AUO_WLCD_12.3”.

To use “TCC80XX_BOE_WLCD_12.3”, modify the build configuration as described in Chapter 4.6.3.5.5.

  

### 2.1.1   CPU Board

Figure 2.1 shows the top view of the TCC807x CPU board.

Figure 2.1 TCC807x CPU Board (Top View)

Table 2.2 describes TCC807x CPU board (top view) connectors.

Table 2.2 Description of CPU Board (Top View)

|**Number**|**Reference Number**|**Name**|**Description**|
|---|---|---|---|
|1|JM1|SD Socket|SD memory card socket|
|2|J10D1|20-pin Right Angle Header|JTAG header for system debug|
|3|JH3|40-pin Mezzanine Connector|Connect to MIPI1 sub-board|
|4|JH6|40-pin Mezzanine Connector|Connect to PCIe1 sub-board|
|5|JC4|USB Type-A Connector|USB2.0 High speed Host connector|
|6|JC1|USB Type-A Connector|USB2.0 High speed Host and Device connector|
|7|JC3|USB 3.0 Type-A Connector|USB3.0 Super speed Host and Device connector|
|8|JC7|RJ45 Connector|Legacy Ethernet port|
|9|JC6|TE B1 Connector|Ethernet AVB port|
|10|SW8,9|Slide Switch|Select the mode of Ethernet AVB|
|11|SW10|Slide Switch|Select enable or disable of Safety Watchdog Timer (SWDT) function|
|12|CON5|10-pin Right Angle Header Box|Header for MIPI DSI LCD module’s power|
|13|SW1|Tact Switch|Switch for system reset (GRESET)|
|14|JSW2,3,4,5|Slide Switch|Select the boot mode of system|
|15|CON2|24-pin Right Angle Header Box|Connect to LCD module’s control signals for DP|
|16|SW3,4,5|Tact Switch|Switch for test|
|17|CON3|24-pin Right Angle Header Box|Header for LCD module’s control signals for DP|
|18|SW2|Slide Switch|Select the path of bus|
|19|CON4|24-pin Right Angle Header Box|LCD module’s control signals for DP|
|20|CON2|10-pin Right Angle Header Box|Header for the remote control board’s signal|
|21|J8D1|16-pin Header|Header for audio test of Time Division Multiplexing (TDM)|
|22|JH1|40-pin Mezzanine Connector|Connect to High Speed Serial Transmit Port (HSSTP)|
|23|JH7|40-pin Mezzanine Connector|Connect to Bluetooth and Wi-Fi sub-board|
|24|JH5|40-pin Mezzanine Connector|Connect to PCIe0 sub-board|
|25|J1|DP Connector|Connect to DP-channel LCD module|
|26|JH2|60-pin Mezzanine Connector|Connect to MIPI DSI sub-board|
|27|JH4|40-pin Mezzanine Connector|Connect to MIPI0 sub-board|

### 2.1.2   Main Board

Figure 2.2 shows the top view of the main board.

Figure 2.2 TCC807x Main Board (Top View)

Table 2.3 describes the main board (top view) connectors.

Table 2.3 Description of Main Board (Top View)

|**Number**|**Reference Number**|**Name**|**Description**|
|---|---|---|---|
|1|J1|180-pin B to B Connector|Connect the main board to the CPU board|
|2|J2|180-pin B to B Connector|Connect the main board to the CPU board|
|3|CON2,3|24-pin Right Angle Header Box|Header to connect the external MCU signals|
|4|MIC2,4|MIC|Internal MIC|
|5|MIC1,3|MIC|Internal MIC|
|6|J4|Phone Jack|Jack for front seat sound output|
|7|J7|Phone Jack|Jack for rear seat sound output|
|8|J8|Phone Jack|Jack for rear line sound output|
|9|J10|Phone Jack|Jack for AUX sound input|
|10|J9|Phone Jack|Jack for line sound input|

  

Figure 2.3 shows the bottom view of the main board.

Figure 2.3 TCC807x Main Board (Bottom View)

Table 2.4 describes the main board (bottom view) connectors.

Table 2.4 Description of Main Board (Bottom View)

|**Number**|**Reference Number**|**Name**|**Description**|
|---|---|---|---|
|1|J11|Power Jack|12V Power Jack|
|2|SW9|Toggle Switch|Power On/Off switch|
|3|SW7|Toggle Switch|Select the Suspend To RAM (STR) mode|
|4|SW8|Toggle Switch|Switch to enable rear camera|
|5|SW6|Slide Switch|Select audio codec control host:<br><br>TCC807x or external MCU|
|6|J7D1|14-pin Header|Connect the main board to the iPod sub-board|
|7|J4S1|4-pin Header|Connect the main board to the external MIC|
|8|J10D2|20-pin Header|Connect the main board to the general test sub-board|
|9|JC1|USB Type-C Connector|UART debug port|
|10|J7D2|14-pin Header|Connect the main board to the debug UART sub-board|
|11|J4S2|4-pin Header|Connect the main board to the external MIC|
|12|J6D1|12-pin Header|Power for external Software Define Radio (SDR) sub-board|
|13|J19D1|38-pin Header|Header for external Software Define Radio (SDR) sub-board|
|14|J14D1|14-pin Header|Connect the main board to the external MCU sub-board|
|15|J6D2|12-pin Header|Power for external DXB sub-board|
|16|SW10|Slide Switch|Select the Software Define Radio (SDR) power control signal|
|17|J17D1|34-pin Header|Header for external DXB sub-board|
|18|J7D3|14-pin Header|Select the output channel for CAN|
|19|J6|Fiber Optical Jack|Output of S/PDIF 1|
|20|J3|Fiber Optical Jack|Input of S/PDIF|
|21|J5|Fiber Optical Jack|Output of S/PDIF 0|
|22|CON1|Test Point|Test point for connecting main board with speaker|
|23|J10D1|20-pin Header|Connect the main board to the Motor and HUD LCD|

**Note:** The test sub-board and camera test sub-board are not provided by Telechips.

### 2.1.3   12.3” 1920x720 LCD Sub-board

**Note:** Linux_YP4.0_IVI SDK’s default setting of LCD is fitted with “TCCXXXX_AUO_WLCD_12.3”.

#### 2.1.3.1    TCC80XX_BOE_WLCD_12.3” LCD

Figure 2.4 shows the top view of the TCC80XX_BOE_WLCD_12.3” LCD sub-board.

Figure 2.4 TCC80XX_BOE_WLCD_12.3” LCD Sub-board (Top View)

Table 2.5 describes TCC80XX_BOE_WLCD_12.3” LCD sub-board (top view) connectors.

Table 2.5 Description of TCC80XX_BOE_WLCD_12.3” LCD Sub-board (Top View)

|   |   |   |   |
|---|---|---|---|
|**Number**|**Reference Number**|**Name**|**Description**|
|1|J13|26-pin LVDS Connector|Connect to even channel LVDS|
|2|J12|26-pin LVDS Connector|Connect to odd channel LVDS|
|3|CON1|24-pin Right Angle Pin Header Box|Receive power and control signals for touch|
|4|CON2|24-pin Right Angle Pin Header Box|Receive power and control signals for touch|
|5|CON3|24-pin Right Angle Pin Header Box|Receive power and control signals|
|6|CON4|24-pin Right Angle Pin Header Box|Receive power and control signals|

  

Figure 2.5 shows the bottom view of the TCC80XX_BOE_WLCD_12.3” LCD sub-board.

Figure 2.5 TCC80XX_BOE_WLCD_12.3” LCD Sub-board (Bottom View)

Table 2.6 describes TCC80XX_BOE_WLCD_12.3” LCD sub-board (bottom view) connectors.

Table 2.6 Description of TCC80XX_BOE_WLCD_12.3” LCD Sub-board (Bottom View)

|**Number**|**Reference Number**|**Name**|**Description**|
|---|---|---|---|
|1|CON6|10-pin Power Connector|Optional output power connector: Connect to the additional LCD sub-board in DP daisy-chain mode|
|2|CON5|10-pin Power Connector|Optional input power connector: Connect to the additional LCD sub-board in DP daisy-chain mode|
|3|J11|Phone Jack|Jack for audio codec output|
|4|J10|FPC Connector|Connect to touch interface of BOE LCD|
|5|J9|FPC Connector|Connect to backlight and open-LDI interface of BOE LCD|
|6|J4|DP Connector|Connect to DP interface|
|7|J1|HDMI Connector|Connect to HDMI interface (not used)|
|8|J2|FAKRA Connector|Connect HDMI to data output in GMSL|
|9|J6|FAKRA Connector|Connect to DP_A for data output in GMSL|
|10|J5|FAKRA Connector|Connect to DP_B for data output in GMSL|
|11|J7|FAKRA Connector|Connect to DP in daisy-chain mode for data output in GMSL|
|12|J8|FAKRA Connector|Connect to DP or HDMI for data output in GMSL (not used)|
|13|SW5|DIP Switch|Select the display mode of deserializer CFG1|
|14|SW3,4|DIP Switch|Select the display mode of deserializer CFG0|
|15|SW6|Slide Switch|Select the LVDS source of BOE LCD|
|16|SW2|Slide Switch|Select the GPIOs to control the HDMI or DP interface|
|17|SW1|Slide Switch|Select the GPIOs to control the LVDS or SER/DES interface|

#### 2.1.3.2    TCCXXXX_AUO_WLCD_12.3” LCD

Figure 2.6 TCCXXXX_AUO_WLCD_12.3” LCD Sub-board

  

### 2.1.4   UART Sub-board

The UART sub-board is a USB to UART bridge board that provides RS232 to USB 2.0 Full-Speed interface.

The EVB's UART interface will be provided on the main board or sub-board depending on the manufacturer’s parts supply and demand situation.

Figure 2.7 TCC80XX_UART_CP2102_SV0.1.0 (Top View)

Figure 2.8 TCC80XX_UART_CP2102_SV0.1.0 (Bottom View)

Table 2.7 describes the UART sub-board connectors.

Table 2.7 Description of UART Sub-board

|   |   |   |   |
|---|---|---|---|
|**Number**|**Reference Number**|**Name**|**Description**|
|1|JC1,2,3,4|USB Type-C Connector|USB to UART debug port|
|2|JH1|14-pin Header|Connect to main board|

  

## 2.2    Boot Mode

### 2.2.1   USB Boot Mode

Table 2.8 Set to USB 2.0 Boot Mode

|   |   |
|---|---|
|**USB 2.0 Boot Mode Switch**|**FWDN Port**|
|||

Table 2.9 Set to USB 3.0 Boot Mode

|   |   |
|---|---|
|**USB 3.0 Boot Mode Switch**|**USB3.0 Port**|
|||

 

  

### 2.2.2   eMMC Boot Mode

Table 2.10 Set to eMMC Boot Mode

|**eMMC Boot Mode Switch**|**Reset Switch**|**Note**|
|---|---|---|
|||The reset button is on the bottom right corner of the board.|

### 2.2.3   SNOR/eMMC Boot Mode

Table 2.11 Set to SNOR/eMMC Boot Mode

|   |   |   |
|---|---|---|
|**SNOR/eMMC Boot Mode Switch**|**Reset Switch**|**Note**|
|||The reset button is on the bottom right corner of the board.|

  

### 2.2.4   UFS Boot Mode

Table 2.12 Set to UFS Boot Mode

|   |   |   |
|---|---|---|
|**UFS Boot Mode Switch**|**Reset Switch**|**Note**|
|||The reset button is on the bottom right corner of the board.|

### 2.2.5   SNOR/UFS Boot Mode

Table 2.13 Set to SNOR/UFS Boot Mode

|   |   |   |
|---|---|---|
|**SNOR/UFS Boot Mode Switch**|**Reset Switch**|**Note**|
|||The reset button is on the bottom right corner of the board.|

**Note:** For more details, refer to “_TCC807x Common Hardware-User Guide for EVB_”. [12]

# 3         Board Assembly Guide

## 3.1    Configuration

Table 3.1 shows the configuration for single display system of the TCC807x EVB.

Table 3.1 Configuration for Single Display System of TCC807x EVB

|   |   |   |
|---|---|---|
|**Figure**|**Name/Specification**|**Quantity**|
||TCC807X_LPD4_4X322<br><br>TCC8070_LPD5322|1|
||TCC807X_MAIN|1|
||TCC80XX_BOE_WLCD_12.3<br><br>or<br><br>TCCXXXX_AUO_WLCD_12.3|1|
||DisplayPort Cable|1|
||FAKRA Cable|1|
||24-pin Flat Cable|1|
||Screw nut|7|
||DC 12V Power Adapter<br><br>(10A or more required)|1|
||USB Micro Type Cable|1|
||110/220V Power Cable|1|

**Caution:** Compatibility problems may occur if you use cables other than the basic components provided by Telechips for the display and the Power Adapter.

  

## 3.2    Assembly

For TCC807x EVB environment, the Linux_YP4.0_IVI SDK supports DP and MIPI DSI as an interface to WLCD_12.3’’ LCD.

This chapter describes how to configure the switches on the LCD sub-board to use DisplayPort (DP).

**Note 1:** For multi display system (DP or MIPI DSI), refer to “_TCC807x Common Hardware-Assembly Manual for EVB”_. [8]

**Note 2:** TCC807x does not support HDMI.

**Step 1:** Select the switch of the WLCD_12.3” LCD sub-board.

For DP, set the slide switches (SW1, SW2, and SW6) and DIP switches (SW3, SW4, and SW5) as shown in Table 3.2 and Figure 3.1.

Table 3.2 Configuration of LCD Sub-board Switch for DisplayPort in Single Display System

|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|**Display**|**SW1**|**SW2**|**SW6**|**SW4**|**SW3**|**SW5**|
|DisplayPort|||**_Don’t care_**||||

Figure 3.1 Configuration of LCD Sub-board Switch for DisplayPort in Single Display System

**Step 2:** Check the status of the LED indicator for the single display system of the WLCD_12.3” LCD sub-board.

Figure 3.2 LED Status of LCD Sub-board Switch for DisplayPort in Single Display System

**Step 3:** Connect the DisplayPort cable and 24-pin flat cable as follows.

Figure 3.3 Connecting CPU board to LCD

**Step 4:** Connect the LCD to the CPU board by using a DisplayPort cable and a 24-pin flat cable as follows.

n  Figure 3.4 shows the completely assembled single display system of the TCC807x EVB.

Figure 3.4 Assembled Single Display System of TCC807x EVB

## 3.3    VCP Module Connect

Connect a 24-pin flat cable as follows.

Figure 3.5 Connecting CPU Board to VCP Module

**Important 1:** The VCP module is not a default component for TCC807x EVB. To use the VCP module, contact Telechips. [1]

**Important 2:** To use the VCP module, you must download the firmware to the VCP module. Refer to “_TCC70xx Common-User Guide for Firmware Downloader_VCP_”. [13]

  

# 4         Build Guide

## 4.1    SDK Build Preparation

Linux_YP4.0_IVI is based on the Yocto Project 4.0 Kirkstone. Therefore, the Yocto Project environment must be set on the host PC to use the Linux_YP4.0_IVI. To download SDK, source-mirror, and tools, you must install utilities.

## 4.2    Yocto Project

The Yocto Project is an open source project focuses on embedded Linux development.

It uses a combination of Open Embedded project, which is Poky, and **_bitbake_** as the build system to make Linux images.

By using Yocto Project, you can simultaneously build the bootloader, kernel, and rootfs.

## 4.3    Task Process

Figure 4.1 shows the task process of Yocto Project. You can download the source from the upstream based on the metadata and build it. When the build is completed, package, image, and SDK are provided as results.

Figure 4.1 Yocto Project Development Process

  

## 4.4    Yocto Project Installation

### 4.4.1   Linux Distribution Versions Supported by Yocto Project

The following Linux distribution versions are supported. Other distribution versions have not passed the verification process in Yocto project.

For details, refer to the following Yocto Project website:

n  [https://docs.yoctoproject.org/kirkstone/ref-manual/system-requirements.html#supported-linux-distributions](https://docs.yoctoproject.org/kirkstone/ref-manual/system-requirements.html#supported-linux-distributions)

l  Ubuntu 20.04 (LTS)

l  Ubuntu 22.04 (LTS)

l  Fedora 38

l  Debian GNU/Linux 11.x (Bullseye)

l  AlmaLinux 8

### 4.4.2   List of Packages Required for Host Development System to use Yocto Project

The mandatory packages must be installed on Host System (individual computer or development server) to use Yocto Project.

For details, refer to the following Yocto Project website:

n  [https://docs.yoctoproject.org/kirkstone/ref-manual/system-requirements.html#required-packages-for-the-build-host](https://docs.yoctoproject.org/kirkstone/ref-manual/system-requirements.html#required-packages-for-the-build-host)

## 4.5    Install Utilities

### 4.5.1   repo

You can download the Linux_YP4.0_IVI through Android **_repo_**.

To install the **_repo,_** refer to the following website: [https://gerrit.googlesource.com/git-repo/](https://gerrit.googlesource.com/git-repo/).

If **_repo_** is already installed, you can use it without re-installation.

### 4.5.2   NcFTP

**_NcFTP_** is a browser program for the File Transfer Protocol. It is required to download tools from Telechips’ FTP server.

For details on **_NcFTP_**, refer to the following website: [http://www.NcFTP.com/ncftp](http://www.NcFTP.com/ncftp)

  

## 4.6    Linux_YP4.0_IVI

Use **_autolinux_** to download and build the Linux_YP4.0_IVI SDK.

n  **_autolinux_** (python script to automatically download and build the SDK)

### 4.6.1   Composition of Linux_YP4.0_IVI

After the download is completed, you can check the following items.

|**Item**|   |   |**Description**|
|---|---|---|---|
|poky|meta|   |Yocto Project 4.0 Kirkstone build system|
|meta-poky|   |
|meta-yocto-bsp|   |
|meta-arm|   |Supports Arm toolchain Layer|
|meta-qt5|   |Supports Qt5 5.6.3 Layer|
|meta-gplv2|   |Supports packages to avoid GPLv3 license|
|meta-telechips-bsp[[김(K4]](#_msocom_4) [[신(HS5]](#_msocom_5)|   |Supports Telechips BSP Layer|
|meta-telechips[[김(K6]](#_msocom_6) [[신(HS7]](#_msocom_7)|meta-core|Recipes that require modification from Open Source Software (OSS) used by Telechips Linux_YP4.0_IVI or recipes that are not in Yocto Project 4.0|
|meta-extra|OSS Layer that is added by Telechips|
|meta-qt5|Supports Qt5 to support Telechips GUI application|
|meta-ivi|Configuration package and example programs of In-vehicle Infotainment (IVI)|
|meta-subcore|Configuration package and example programs on sub-core|
|download.sh|   |Script for downloading source-mirror and tools|
|source-mirror|   |   |Local repository for building the basic class of Linux_YP4.0_IVI|
|fwdn_v8|   |   |FWDN execute file<br><br>VTC driver<br><br>Source code|
|mktcimg|   |   |mktcimg execute file<br><br>Source code|
|boot-firmware|   |   |Boot-firmware files<br><br>Tools to make images for boot-firmware|
|Tools[[김(K8]](#_msocom_8) [[신(HS9]](#_msocom_9)|   |   |Yocto Project 4.0 Kirkstone **_buildtools_**<br><br>n  x86_64-buildtools-nativesdk-standalone-4.0.sh<br><br>n  x86_64-buildtools-extended-nativesdk-standalone-4.0.sh|

  

### 4.6.2   Autolinux

**_autolinux_** was developed by Telechips to make it easier for you to download and build the SDK.

It does not provide all settings and functions, so you should refer to Chapter 4.6.3 for detailed configurations.

#### 4.6.2.1    Download Autolinux

You can download the **_autolinux_** script from git repository.

|   |
|---|
|**~/release$ git clone ssh://git.telechips.com/linux_ivi/script/build-autolinux  <br>~/release$ cd build-autolinux  <br>~/release/build-autolinux$ git checkout linux_yp4.0_ivi_1.0.0  <br>~/release/build-autolinux$ tree**<br><br>.<br><br>├── autolinux<br><br>├── classes<br><br>│   ├── feature.py<br><br>│   └── features<br><br>│       ├── cluster.py<br><br>│       ├── common.py<br><br>│       └── ivi.py<br><br>├── doc<br><br>│   └── variable.txt<br><br>├── README<br><br>├── script<br><br>│   ├── bitbake-layers.sh<br><br>│   ├── build_configure.sh<br><br>│   ├── build_image.sh<br><br>│   └── devtool.sh<br><br>└── template<br><br>    ├── linux_ivi.py<br><br>├── sdk.py<br><br>    ├── tcc803x_linux_cluster.py<br><br>    ├── tcc803x_linux_ivi_jvckenwood.py<br><br>    ├── tcc803x_linux_ivi_litbig.py<br><br>    ├── tcc803x_linux_ivi.py<br><br>    ├── tcc805x_linux_cluster.py<br><br>    ├── tcc805x_linux_ivi.py<br><br>    ├── tcc807x_linux_ivi_pre_release.py[[강(K10]](#_msocom_10) [[H김11]](#_msocom_11) <br><br>    ├── tcc807x_linux_ivi.py<br><br>    └── tcc897x_linux_cluster.py|

#### 4.6.2.2    Composition of Autolinux

|   |   |   |   |
|---|---|---|---|
|**File**|   |   |**Description**|
|autolinux|   |   |Python script to automatically download and build the SDK|
|classes|feature.py|   |Python class for SDK features|
|features|cluster.py|File that defines supported cluster features|
|common.py|File that defines supported common features|
|ivi.py|File that defines supported IVI features|
|doc|variable.txt|   |Document that describes the variables used in **_autolinux_**|
|README|   |   |Document that describes **_autolinux_**|
|script|bitbake-layers.sh|   |Shell script to execute **_bitbake-layers_** in **_autolinux_**|
|build_configure.sh|   |Shell script to execute **_configure_** in **_autolinux_**|
|build_image.sh|   |Shell script to execute **_bitbake_** in **_autolinux_**|
|devtool.sh|   |Shell script to execute **_devtool_** in **_autolinux_**|
|template|linux_ivi.py|   |File that defines supported machines and manifests for Linux_YP4.0_IVI SDK|
|sdk.py|   |File that defines supported SDKs, source mirror, and build tool paths|
|Other files|   |File that defines supported machines and manifests for other SDKs<br><br>These files are used by other SDKs|

#### 4.6.2.3    Autolinux Usage

|   |
|---|
|**~/release/build-autolinux$ ./autolinux --help**<br><br>**usage: autolinux [-h] -c COMMAND [COMMAND ...] [-V] [-s SDK] [-m MACHINE]  <br>                  [-x MANIFEST] [-f FEATURES [FEATURES ...]]  <br>                  [-sf SUBFEATURES [SUBFEATURES ...]] [--skip-ftp]**<br><br>Linux SDK Configurations<br><br>**optional arguments:  <br>**  **-h**, **--help**            show this help message and exit<br><br>**General Command:**<br><br>  **-c** COMMAND [COMMAND ...], **--command** COMMAND [COMMAND ...]  <br>General Command to use autolinux(required option)  <br>-commands-**update**: sync to recipes matched manifest.xml, Be careful local changes will be lost  <br>**configure** [option] [name]: setup the newer build environment  <br>    conf_opt arg : addtionally set configuration options  <br>                     refers to 'Configuration Options'  <br>                     Ex) autolinux -c configure -m tcc8050-main  <br>    save [name] : save autolinux.config file to .config/  <br>    load [name] : load configure file from .config/**clean** [option]: move current built files to recycle directory. Recycle dir:build/delete  <br>    old : delete current built files and recycle directory.  <br>    all : delete total build directory**build** [option]: build SDK Image, choose the name of the image to build  <br>    'args'     : extra command strings  <br>                 Ex) autolinux -c build "linux-telechips -C compile"    sub 'args' : building on sub-core, available only when the with-subcore option is enabled  <br>                 Ex) autolinux -c build sub "linux-telechips -C compile"**devtool** [option] : devtool package to develop easily    'args'     : extra command strings  <br>                 Ex) autolinux -c devtool 'modify linux-telechips  <br>    sub 'args' : devtool on sub-core  <br>                 Ex) autolinux -c sub devtool 'modify linux-telechips'**layers** [option] : bitbake-layers command  <br>    'args'     : extra command strings  <br>                 Ex) autolinux -c layers add-layer 'poky/meta-telechips/meta-ivi'  <br>    sub 'args' : building on sub-core, available only when the with-subcore option is enabled  <br>                 Ex) autolinux -c sub layers add-layer 'poky/meta-telechips/meta-ivi/meta-ivi-subcore'**make_fai** : make SDdata.fai for fwdn**make_updatedir** [option] : make update directory for update  <br>    main : make only on the main core  <br>    sub  : make only on the sub core**chk_security**  : make csv file for whether or not memory protection technology**info** : show information of current configuration**modify** option: modify specific configure at current set-up  <br>    feature     : modify features  <br>    sub-feature : modify subcore features  <br>    image       : modify image<br><br>**-V**, **--version**         print version and exit<br><br>**Configuration Options:**<br><br>  -s SDK, --sdk SDK enter the sdk to download  <br>               sdk lists  <br>               ivi     :['linux_ivi', 'tcc803x_linux_ivi', 'tcc805x_linux_ivi', 'tcc807x_linux_ivi']<br><br>               cluster :['tcc897x_linux_cluster', 'tcc803x_linux_cluster', 'tcc805x_linux_cluster']  <br>  -m MACHINE, --machine MACHINE  <br>               enter the machine to build  <br>  -x MANIFEST, --manifest MANIFEST  <br>               enter the manifest to build  <br>  -f FEATURES [FEATURES ...], --features FEATURES [FEATURES ...]  <br>               enter the feature list  <br>               Ex) -f with-subcore gpu-vz meta-update  <br>  -sf SUBFEATURES [SUBFEATURES ...], --sub-features SUBFEATURES [SUBFEATURES ...]  <br>               enter the subfeature list  <br>               Ex) -sf rvc gpu-vz meta-update<br><br>**Environment Options:**<br><br>  **--skip-ftp**            Skip to download from Telechips FTP Server|

#### 4.6.2.4    Download and Configure SDK

Linux_YP4.0_IVI is downloaded during the initial configuration.

Linux_YP4.0_IVI SDK’s default display is DisplayPort (DP) and default storage is eMMC.

You can set up the initial configuration by using a configure command. If you execute the configure command, the initial configuration is progressed as the following four steps.

**Note:** Each step is activated only when there is at least one selectable option.

1.       **Choose the Platform** and **SDK**.

2.       **Choose the manifest** **to repo**.

n  This step is not activated in the current version of Linux YP4.0_IV[[J김12]](#_msocom_12) [[H김13]](#_msocom_13) I (1.0.0) because there is no selection option.

3.       **Choose a Machine to build**.

4.       **Choose the features** to build.

When the configuration is completed, the set-up is saved as an “autolinux.config”.

The following is an example of TCC8070.

|   |
|---|
|**~/release/build-autolinux$ ./autolinux -c configure**<br><br>**The command is configure or Add configuration options(sdk,machine,manifest)**<br><br>**Configure Start**<br><br>**Choose the Platform**<br><br>1.cluster<br><br>2.ivi<br><br>Select SDK(1-2): 2  <br>**Choose the SDK to download**<br><br>1.linux_ivi<br><br>  2.tcc803x_linux_ivi<br><br>  3.tcc805x_linux_ivi<br><br>  4.tcc807x_linux_ivi<br><br>Select SDK(1-4): 1<br><br>**Choose a Machine to build**<br><br>  1.tcc8030-main<br><br>  2.tcc8050-main<br><br>  3.tcc8053-main<br><br>  4.tcc8059-main<br><br>  5.tcc8070-main<br><br>  6.tcc8030-sub<br><br>  7.tcc8050-sub<br><br>  8.tcc8053-sub<br><br>  9.tcc8059-sub<br><br>  10.tcc8070-sub<br><br>Choose Machine(1-10): 5<br><br>**Choose the Features at tcc8070-main** **// "*" means selected feature**<br><br>  1.  ufs                 Changed Boot Storage to UFS(supported : tcc8050, tcc8053, tcc8070)<br><br>  2.  bootchart           Install bootchart<br><br>  3.  network             Install network packages<br><br>  4.  optee               Using OPTEE<br><br>  5.  str                 Enable Suspend To Ram<br><br>* 6.  with-subcore        Booting with sub-core<br><br>  7.  gpu-vz              GPU Virtualization<br><br>  8.  screen-share        Screen Sharing<br><br>  9.  hud-display         Enable display for HUD<br><br>* 10. support-4k-video    Support 4k Video Contents<br><br>  11. booting-animation   Enable Booting Animation<br><br>* 12. meta-update         Enable Update<br><br>* 13. meta-micom          Enable Micom<br><br>  0.Exit<br><br>Choose Features enable/disable (1-13): 0<br><br>**Choose the Features at tcc8070-sub**<br><br>**// In case "with-subcore" enabled in features, sub-core's feature select step activated.**<br><br>1.  ufs                 Changed Boot Storage to UFS(supported : tcc8050, tcc8053, tcc8070)<br><br>2.  bootchart           Install bootchart[[W김14]](#_msocom_14) <br><br>  3.  network             Install network packages<br><br>  4.  str                 Enable Suspend To Ram<br><br>* 5.  rvc                 Enable Rear Camera<br><br>  6.  screen-share        Screen Sharing<br><br>  7.  cluster             Enable Cluster<br><br>  8.  booting-animation   Enable Booting Animation<br><br>* 9.  meta-update         Enable Update<br><br>* 10. meta-micom          Enable Micom<br><br>  0.Exit<br><br>Choose Features enable/disable (1-10[[강(K15]](#_msocom_15) [[H김16]](#_msocom_16) ): 0<br><br>...<br><br>...<br><br>tools/x86_64-buildtools-extended-nativesdk-standalone-4.0.sh<br><br>tools/x86_64-buildtools-nativesdk-standalone-4.0.sh<br><br>**Do you want to build tools installer version 4.0? (y/n):** y<br><br>Extended Build tools installer version 4.0<br><br>==========================================<br><br>**You are about to install the SDK to "/home/release/build-autolinux/buildtools/4.0". Proceed [Y/n]?** Y<br><br>Extracting SDK..................done<br><br>Setting it up...done<br><br>SDK has been successfully set up and is ready to be used.<br><br>Each time you wish to use the SDK in a new shell session, you need to source the environment setup script e.g.<br><br> $ . /home/release/build-autolinux/buildtools/4.0/environment-setup-x86_64-pokysdk-linux<br><br>Enabled with-subcore, The autolinux script makes new configuration files of Sub-core automatically<br><br>================================================================================<br><br>**SDK=linux_ivi**<br><br>**MANIFEST=linux_yp4.0_ivi_1.0.0.xml**<br><br>**DATE=2024/05/31**<br><br>**MACHINE=tcc8070-main**<br><br>**VERSION=release**<br><br>**FEATURES=with-subcore,support-4k-video,meta-micom,meta-update**<br><br>**SUBFEATURES=rvc,meta-micom,meta-update**<br><br>================================================================================<br><br>**~/release/build-autolinux$ ls**<br><br>autolinux* boot-firmware_tcc803x/ build/ classes/ fwdn_v8/ poky/ release-info/ source-mirror/ tools/ autolinux.config boot-firmware_tcc805x/ boot-firmware_tcc807x/ buildtools/ doc/ mktcimg/ README  script/ template/[[H김17]](#_msocom_17)|

  

##### 4.6.2.4.1         Configure Command with Extra Options

The configure command can be used with the following three extra options.

n   **Configuration Options**

|   |
|---|
|**~/release/build-autolinux$ ./autolinux --help**<br><br>...<br><br>**Configuration Options:**  <br>  -s SDK, --sdk SDK     enter the sdk to download  <br>                        sdk lists  <br>                        ivi     :['linux_ivi', 'tcc803x_linux_ivi', 'tcc805x_linux_ivi', 'tcc807x_linux_ivi']  <br>                        cluster :['tcc897x_linux_cluster', 'tcc803x_linux_cluster', 'tcc805x_linux_cluster']  <br>  -m MACHINE, --machine MACHINE  <br>                        enter the machine to build  <br>  -x MANIFEST, --manifest MANIFEST  <br>                        enter the manifest to build  <br>  -f FEATURES [FEATURES ...], --features FEATURES [FEATURES ...]  <br>                        enter the feature list  <br>                        ex) -f with-subcore gpu-vz meta-update  <br>  -sf SUBFEATURES [SUBFEATURES ...], --sub-features SUBFEATURES [SUBFEATURES ...]  <br>                        enter the subfeature list  <br>                        ex) -sf rvc gpu-vz meta-update<br><br>...|

n  **save:** Saves the “autolinux.config” to read the next configuration.

If you append **save**, “autolinux.config” is saved as machine name in the .config path.

|   |
|---|
|**~/release/build-autolinux$ ./autolinux -c configure save**<br><br>...<br><br>tcc8070-main.config save successful|

n  **load:** Loads the configuration files saved as **save** in the .config path.

If you append **load**, the **Choose a configure to load** menu is activated.

|   |
|---|
|**~/release/build-autolinux$ ./autolinux -c configure load**<br><br>**Choose a configure to load**<br><br>1.  tcc8070-main.config<br><br>Select Config(1-1): 1<br><br>tcc8070-main.config load successful<br><br>...|

  

#### 4.6.2.5    Build Linux_YP4.0_IVI

Enter **build** command to start building the SDK. The menu is activated only when there are at least two images to be built. The way the **build** command works is the same as **_bitbake_**.

|   |
|---|
|**~/release/build-autolinux$ ./autolinux -c build  <br>**Read configuration from autolinux.config  <br>**  <br>Choose an Image to build**  <br>  1.telechips-ivi-image-minimal  <br>  2.telechips-ivi-image-multimedia  <br>  3.telechips-ivi-image  <br>  4.automotive-linux-platform-image  <br>Choose Image (1-4):4|

##### 4.6.2.5.1         Result of Building SDK

The following is an example of TCC8070.

|   |
|---|
|Enabled with-subcore, The autolinux script build Sub-core Image automatically in background<br><br>NOTE: Your conf/bblayers.conf has been automatically updated.<br><br>Parsing recipes: 100% \|#######################################################\| Time: 0:00:40<br><br>Parsing of 1090 .bb files complete (0 cached, 1090 parsed). 1739 targets, 266 skipped, 0 masked, 0 errors.<br><br>NOTE: Resolving any missing task queue dependencies<br><br>Build Configuration:<br><br>BB_VERSION           = "2.0.0"<br><br>BUILD_SYS            = "x86_64-linux"<br><br>NATIVELSBSTRING      = "universal"<br><br>TARGET_SYS           = "aarch64-telechips-linux"<br><br>MACHINE              = "tcc8070-main"<br><br>DISTRO               = "poky-telechips-systemd"<br><br>DISTRO_VERSION       = "4.0.17"<br><br>TUNE_FEATURES        = "aarch64 armv8-2a cortexa76-cortexa55"<br><br>TARGET_FPU           = ""<br><br>LINUX_VERSION        = "5.10.205"<br><br>KBUILD_DEFCONFIG     = "tcc807x_ivi_defconfig"<br><br>IMAGE_FEATURES       = " debug-tweaks read-only-rootfs"<br><br>GCCVERSION           = "arm-11.2"<br><br>GLIBCVERSION         = "2.35%"<br><br>INVITE_PLATFORM      = " with-subcore multimedia support-4k-video qt5/wayland micom fw-update genivi"<br><br>meta<br><br>meta-poky<br><br>...<br><br>...<br><br>...<br><br>Summary: There was 1 WARNING message shown.[[김김18]](#_msocom_18) [[김김19]](#_msocom_19) [[H김20]](#_msocom_20) <br><br>================================================================================<br><br>**Built Images Path : /home/release/build-autolinux/build/tcc8070-main/tmp/deploy/images/tcc8070-main**<br><br>**Built Images Path : /home/release/build-autolinux/build/tcc8070-sub/tmp/deploy/images/tcc8070-sub**<br><br>================================================================================|

 

##### 4.6.2.5.2         Build Command with Additional Arguments (Optional)

The **build** command can be used with additional arguments (string argument).

n  String argument

The **build** command supports a string argument for building the specific packages. The specific packages are built based on the machine stored in “autolinux.config”.

|   |
|---|
|**~/release/build-autolinux$ ./autolinux -c build "linux-telechips -c compile"**|

n  Sub + string argument

The **build** command supports a string argument for building the specific packages on the sub-machine. This **build** command requires **with-subcore** feature enabled.

|   |
|---|
|**~/release/build-autolinux$ ./autolinux -c build sub "linux-telechips -c compile"**|

#### 4.6.2.6    Make “SD_Data.fai” to download Firmware

Enter **make_fai** command to make “SD_Data.fai”. The **make_fai** command is based on the image defined in “autolinux.config”.

|   |
|---|
|**~/release/build-autolinux$ ./autolinux -c make_fai**<br><br>...<br><br>================================================================================<br><br>**FWDN Path : /home/release/build-autolinux/build/tcc8070-main/tmp/deploy/fwdn**<br><br>================================================================================<br><br>**~/release/build-autolinux$ ls build/tcc8070-main/tmp/deploy/fwdn**<br><br>boot-firmware  partition.list  SD_Data.fai  SD_Data.gpt  SD_Data.gpt.back  SD_Data.gpt.prim|

**Note:** **make_fai** command is described in Chapter 5.2.2.

 

#### 4.6.2.7    Other Commands and Options

##### 4.6.2.7.1         Clean

The **clean** command is related to removing build history.

n  **clean:** Moves the currently built files to the recycle directory. The recycle directory path is as follows: “build/delete/#”

|   |
|---|
|**~/release/build-autolinux$ ./autolinux -c clean**<br><br>Read configuration from autolinux.config<br><br>deleted target :<br><br>/home/release/build-autolinux/build/tcc8070-main/<br><br>    /home/release/build-autolinux/build/tcc8070-sub/<br><br>move current built files. recycle dir:build/delete/0|

n  **clean old:** Deletes the recycle directory.

|   |
|---|
|**~/release/build-autolinux$ ./autolinux -c clean old**<br><br>delete recycle directory in background.|

n  **clean all:** Deletes the entire build directory including build history. Therefore, when you rebuild the SDK after executing the **clean all** command, the build time takes a long time.

**Note**: After **clean all**, you must **configure** again.

|   |
|---|
|**~/release/build-autolinux$ ./autolinux -c clean all**<br><br>All build directories will be deleted. Are you sure you want to delete it? (y/n): y<br><br>delete total build directory. It takes a long time in background!!<br><br>**~/release/build-autolinux$ ./autolinux -c configure**|

 

  

##### 4.6.2.7.2         Modify

The **modify** command modifies the already configured “autolinux.config”.

n  **modify feature:** Modifies the feature.

If the **with-subcore** feature is disabled, only the main core feature is modified.

|   |
|---|
|**~/release/build-autolinux$ ./autolinux -c modify feature**<br><br>Read configuration from autolinux.config<br><br>**Choose the Features at tcc8070-main**<br><br>  1.  ufs                 Changed Boot Storage to UFS(supported : tcc8050, tcc8053, tcc8070)<br><br>  2.  bootchart           Install bootchart<br><br>  3.  network             Install network packages<br><br>  4.  optee               Using OPTEE<br><br>  5.  str                 Enable Suspend To Ram<br><br>* 6.  with-subcore        Booting with sub-core<br><br>  7.  gpu-vz              GPU Virtualization<br><br>  8.  screen-share        Screen Sharing<br><br>  9.  hud-display         Enable display for HUD<br><br>* 10. support-4k-video    Support 4k Video Contents<br><br>  11. booting-animation   Enable Booting Animation<br><br>* 12. meta-update         Enable Update<br><br>* 13. meta-micom          Enable Micom<br><br>  0.Exit<br><br>Choose Features enable/disable (1-13): 0<br><br>**Choose the Features at tcc8070-sub**<br><br>1.  ufs                 Changed Boot Storage to UFS(supported : tcc8050, tcc8053, tcc8070)<br><br>2.  bootchart           Install bootchart[[W김21]](#_msocom_21) <br><br>  3.  network             Install network packages<br><br>  4.  str                 Enable Suspend To Ram<br><br>* 5.  rvc                 Enable Rear Camera<br><br>  6.  screen-share        Screen Sharing<br><br>  7.  cluster             Enable Cluster<br><br>  8.  booting-animation   Enable Booting Animation<br><br>* 9.  meta-update         Enable Update<br><br>* 10. meta-micom          Enable Micom<br><br>  0.Exit<br><br>Choose Features enable/disable (1-10[[강(K22]](#_msocom_22) [[H김23]](#_msocom_23) ): 0<br><br>================================================================================<br><br>**...**<br><br>**FEATURES=with-subcore,support-4k-video,meta-micom,meta-update**<br><br>**SUBFEATURES=rvc,meta-micom,meta-update**<br><br>**...**<br><br>================================================================================<br><br>Modify feature Successful|

n  **modify sub-feature**: Modifies the sub-feature. To modify the sub-feature, the feature must include **with-subcore**.

|   |
|---|
|**~/release/build-autolinux$ ./autolinux -c modify sub-feature**<br><br>Read configuration from autolinux.config<br><br>**Choose the Features at tcc8070-sub**<br><br>1.  ufs                 Changed Boot Storage to UFS(supported : tcc8050, tcc8053, tcc8070)<br><br>2.  bootchart           Install bootchart[[W김24]](#_msocom_24) <br><br>  3.  network             Install network packages<br><br>  4.  str                 Enable Suspend To Ram<br><br>* 5.  rvc                 Enable Rear Camera<br><br>  6.  screen-share        Screen Sharing<br><br>  7.  cluster             Enable Cluster<br><br>  8.  booting-animation   Enable Booting Animation<br><br>* 9.  meta-update         Enable Update<br><br>* 10. meta-micom          Enable Micom<br><br>  0.Exit<br><br>Choose Features enable/disable (1-10[[강(K25]](#_msocom_25) [[H김26]](#_msocom_26) ): 0<br><br>================================================================================<br><br>...<br><br>**SUBFEATURES=rvc,meta-micom,meta-update**<br><br>================================================================================<br><br>Modify sub-feature Successful[[신(HS27]](#_msocom_27) [[김김28]](#_msocom_28)|

n  **modify image**: Modifies an image. The menu is activated only when there are at least two images to be built.

|   |
|---|
|**~/release/build-autolinux$ ./autolinux -c modify image**<br><br>Read configuration from autolinux.config<br><br>**Choose an Image to build**<br><br>1.telechips-ivi-image-minimal<br><br>2.telechips-ivi-image-multimedia<br><br>  3.telechips-ivi-image<br><br>  4.automotive-linux-platform-image<br><br>Choose Image (1-4): 4<br><br>========================================================================<br><br>**...**<br><br>**IMAGE=automotive-linux-platform-image**<br><br>========================================================================<br><br>Modify image Successful|

##### 4.6.2.7.3         Devtool

**_devtool_** is available in **_autolinux_** through **devtool** command. For a detailed description of **_devtool_**, see Chapter 0.

|   |
|---|
|**~/release/build-autolinux$ ./autolinux -c devtool "modify linux-telechips"**<br><br>Read configuration from autolinux.config<br><br>NOTE: Starting bitbake server...<br><br>...<br><br>...<br><br>INFO: Copying kernel config to workspace<br><br>INFO: Recipe linux-telechips now set up to build from /home/release/build-autolinux/build/tcc8070-main/workspace/sources/linux-telechips<br><br>**~/release/build-autolinux$**|

##### 4.6.2.7.4         Update

The **update** command executes **repo sync** by using “manifest.xml” that is set in “autolinux.config”. (Any local changes are removed.)

|   |
|---|
|**~/release/build-autolinux$ ./autolinux -c update**<br><br>Read configuration from autolinux.config<br><br>...<br><br>Sync Update Completed.|

  

### 4.6.3   Detailed Configuration

This chapter explains how to change settings before building the SDK. It also includes features provided by **_autolinux_**.

Set “local.conf” as follows according to the target board.

For the main core, the “local.conf” file is located at “../build-autolinux/build/tcc8070-main/conf”.

|   |   |   |
|---|---|---|
|**Name of Variable**|**Default Value**|**Description**|
|BB_NUMBER_THREADS|8|Maximum number of tasks that can be run simultaneously|
|PARALLEL_MAKE|-j 16|Option for make|
|MACHINE|N/A|Target board setting<br><br>n  tcc8070-main|
|EXTRA_IMAGE_FEATURES|debug-tweaks<br><br>read-only-rootfs|Image property selected additionally<br><br>For detailed options, refer to “local.conf”.|
|CORE_IMAGE_EXTRA_INSTALL|NULL|Name of package to be installed additionally on image|
|DISTRO|poky-telechips-systemd|Select SDK type.<br><br>n  poky-telechips (sysvinit)<br><br>n  poky-telechips-systemd (systemd)|

For the sub-core, the “local.conf” file is located at “../build-autolinux/build/tcc8070-sub/conf”.

|   |   |   |
|---|---|---|
|**Name of Variable**|**Default Value**|**Description**|
|BB_NUMBER_THREADS|8|Maximum number of tasks that can be run simultaneously|
|PARALLEL_MAKE|-j 16|Option for make|
|MACHINE|N/A|Target board setting<br><br>n  tcc8070-sub|
|EXTRA_IMAGE_FEATURES|debug-tweaks<br><br>read-only-rootfs|Image property selected additionally<br><br>For detailed options, refer to “local.conf”.|
|CORE_IMAGE_EXTRA_INSTALL|NULL|Name of package to be installed additionally on image|
|DISTRO|poky-telechips-systemd|Select SDK type.<br><br>n  poky-telechips (sysvinit)  <br>poky-telechips-systemd (systemd)|

 

#### 4.6.3.1    Enable Main Core Functions

Use the **INVITE_PLATFORM** variable in the main core’s “local.conf” to set the supporting functions.

|   |   |
|---|---|
|**Feature**|**Configuration**|
|Support 4K Video|INVITE_PLATFORM += "support-4k-video"|
|HUD Display|INVITE_PLATFORM += "hud-display"|
|Booting Animation|INVITE_PLATFORM += "booting-animation"|

**Important:** The **booting-animation** feature must be configured[[J김29]](#_msocom_29) [[H김30]](#_msocom_30)  either in the main core or the sub-core. Therefore, if you have enabled the feature in the sub-core, do not enable it in the main core, and vice versa.

**Note:** When enabling the **hud-display** feature, you need to connect an LCD to the HUD to ensure the HUD functions properly. For details, refer to “_TCC807x Common Hardware-Assembly Manual for EVB”_. [8]

#### 4.6.3.2    Enable Sub-core

To use the sub-core or cluster in the sub-core, you should enable the **INVITE_PLATFORM** variable in the main core’s “local.conf”.

##### 4.6.3.2.1         Enable Variables for GPU Virtualization

To use GPU in the sub-core, you should enable the variables for GPU virtualization in the main core’s “local.conf”.

|**Feature**|**Configuration**|
|---|---|
|Enable sub-core|INVITE_PLATFORM += "with-subcore"|
|Enable GPU virtualization|INVITE_PLATFORM += "gpu-vz"|

#### 4.6.3.3    Set Up Sub-core Application

Use **SUBCORE_APPS** variable in the sub-core’s “local.conf” i to set up the sub-core application for Rear View Camera (RVC) and cluster.

The RVC is enabled by default.

|   |   |
|---|---|
|**Feature**|**Configuration**|
|RVC|SUBCORE_APPS += "rvc"|
|Cluster|SUBCORE_APPS += "cluster[[김31]](#_msocom_31) "|
|Booting Animation|INVITE_PLATFORM += "booting-animation"|

**Important 1:** The **booting-animation** feature must be configured either in the main core or the sub-core. Therefore, if you have enabled the feature in the sub-core, do not enable it in the main core, and vice versa.

**Important 2:** To use the **Cluster** feature on the sub-core, you must enable “gpu-vz” on the main core. Refer to Chapter [4.6.3.2.1](#_Enable_Variables_for).[[김32]](#_msocom_32) 

**Important 3:** The cluster application is developed by Altia, and you must use this application only for SDK validation. If you want to use it for other purposes, contact Altia.[[W김33]](#_msocom_33) 

#### 4.6.3.4    Enable STR

Use the **INVITE_PLATFORM** variable in the “local.conf” of the main core and the sub-core.

|   |   |
|---|---|
|**Core**|**local.conf**|
|Main Core|INVITE_PLATFORM += "str"|
|Sub-core|INVITE_PLATFORM += "str"|

**Important**: To use the **STR** feature, an external MCU, VCP[[J김34]](#_msocom_34) [[H김35]](#_msocom_35) , is required. For more information, refer to Chapter 3.3.

#### 4.6.3.5    Additional Setting

##### 4.6.3.5.1         Enable PulseAudio

To use PulseAudio as the Sound Server, **DISTRO_FEATURES:append = " [[김(K36]](#_msocom_36) pulseaudio"** variable in the main core’s “local.conf” should be enabled.

**Note:**  **"** **pulseaudio"** is enabled by default.

|   |   |
|---|---|
|**Sound Server**|**Configuration**|
|PulseAudio|DISTRO_FEATURES:append = " pulseaudio"|

##### 4.6.3.5.2         Set Up Graphics System

Use **DISTRO_FEATURES:remove = "wayland"** variable in the main core’s “local.conf” to set the Linux graphics system.

The default value is Wayland.

|   |   |
|---|---|
|**Graphics System**|**Configuration**|
|Wayland|Default|
|FBDEV|DISTRO_FEATURES:remove = "wayland"|

##### 4.6.3.5.3         Enable Vulkan

To use Vulkan, you should add vulkan to the “local.conf” of the main core and the sub-core.

|   |   |
|---|---|
|**Core**|**local.conf**|
|Main Core|DISTRO_FEATURES:append = " vulkan"<br><br>CORE_IMAGE_EXTRA_INSTALL:append = " libvulkan-telechips"|
|Sub-core|DISTRO_FEATURES:append = " vulkan"<br><br>CORE_IMAGE_EXTRA_INSTALL:append = " libvulkan-telechips"|

**Important:** Vulkan is only supported on the Wayland graphics system. To use Vulkan in sub-core, you must switch to Wayland.

##### 4.6.3.5.4         Enable OpenCL

Use **TCC_BSP_FEATURES = " opencl"** variable in the main core and sub-core’s “local.conf” to set the OpenCL.

|   |   |
|---|---|
|**Core**|**local.conf**|
|Main Core|TCC_BSP_FEATURES:append = " opencl"<br><br>CORE_IMAGE_EXTRA_INSTALL:append = " libopencl-telechips"|
|Sub-core|TCC_BSP_FEATURES:append = " opencl"<br><br>CORE_IMAGE_EXTRA_INSTALL:append = " libopencl-telechips"|

##### 4.6.3.5.5         How to change LCD Panel AUO to BOE[[W김37]](#_msocom_37) 

The default LCD panel in the SDK is AUO. If you want to use BOE, remove the **#** (uncomment) from the **#LCD_PANEL_TYPE** [[강(K38]](#_msocom_38) [[H김39]](#_msocom_39) [[H김40]](#_msocom_40) in the “local.conf” in each core.[[강(K41]](#_msocom_41) [[H김42]](#_msocom_42) 

|   |   |
|---|---|
|**Core**|**local.conf**|
|Main Core|#LCD_PANEL_TYPE = "BOE"|
|Sub-core|#LCD_PANEL_TYPE = "BOE"|

**Note:** For more details, refer to “_TCCxxxx Common SDK-User Guide for AUO and BOE touch”_. [14]

##### 4.6.3.5.6         How to change Sub-core 64-bit Memory Size[[W김43]](#_msocom_43) 

The default value of the 64-bit memory size for a sub-core is 512 MB. To modify this value, you must change the value of the variable for each core in the “local.conf” file.

|   |   |
|---|---|
|**Core**|**local.conf**|
|Main Core|SUBCORE_64BIT_MEMORY_SIZE = "0x20000000"|
|Sub-core|64BIT_MEMORY_SIZE = "0x20000000"|

**Important 1:** The value of variables [[Y강44]](#_msocom_44) [[H김45]](#_msocom_45) [[H김46]](#_msocom_46) must be set as a hexadecimal value, such as 0x20000000.

**Important 2:** The values of **SUBCORE_64BIT_MEMORY_SIZE** and **64BIT_MEMORY_SIZE** must match each other.

 

## 4.7    FAQs on Build

This chapter describes the frequently asked questions in the Yocto Project environment.

### 4.7.1   Q1. How to rebuild Package

If you want to rebuild the package, you should clean and then build the package. Follow one of the three clean task types described in Chapter 4.7.1.1 to Chapter 4.7.1.3.

#### 4.7.1.1    clean and build

Clear all output. However, shared state cache data is not cleared.

|   |
|---|
|~/.../build-autolinux$ ./autolinux -c build "alsa-lib -c clean"<br><br>~/.../build-autolinux$ ./autolinux -c build "alsa-lib"|

#### 4.7.1.2    cleanall and build

Clear all data including all results, shared state cache data, and downloaded source code.

|   |
|---|
|~/.../build-autolinux$ ./autolinux -c build "alsa-lib -c cleanall"<br><br>~/.../build-autolinux$ ./autolinux -c build "alsa-lib "|

#### 4.7.1.3    cleansstate and build

Clear all output and shared state cache data.

|   |
|---|
|~/.../build-autolinux$ ./autolinux -c build "alsa-lib -c cleansstate"<br><br>~/.../build-autolinux$ ./autolinux -c build "alsa-lib"|

### 4.7.2   Q2. How to rebuild All Packages

The Yocto project provides a single build type per recipe, so there is no full rebuild functionality. To rebuild all packages,

you need to clean up each package and build the image.

If you want to rebuild the packages used by the image, you can use the following command.

|   |
|---|
|~/.../build-autolinux$ ./autolinux -c build "automotive-linux-platform-image --runall=cleanall"<br><br>~/.../build-autolinux$ ./autolinux -c build|

  

 

### 4.7.3   Q3. How to modify Source Code – Use Devtool

Yocto project provides **_devtool_**, which has features to help you build, test, and package software.

**Note:** **_devtool_** creates workspace directory and recipes in your build directory and adds workspace to your “conf/bblayers.conf” after you execute **devtool** command. Therefore, you can modify your source code and recipes in the workspace directory.

#### 4.7.3.1    Add Source Code

If you want to add your source code that has no recipe in the SDK, you can use **devtool add** command. It assists in adding new software to be built to the SDK. The **devtool add** command generates a new recipe based on the existing source code.

You can add source code from a remote repository and a local directory to the SDK:

n  **devtool add {recipe name} {fetch url or source tree}**

|   |
|---|
|~/.../build-autolinux$ ./autolinux -c devtool add new-recipe ssh://git.telechips.com/linux_ivi/bsp/kernel-5.10.git<br><br>~/.../build-autolinux$ ./autolinux -c devtool add new-recipe2 ./workspace/sources/new-recipe/|

Then, the **devtool add** command generates **new-recipe** or **new-recipe2** in workspace/recipes/new-recipe or new-recipe2. And the source code is downloaded or copied in workspace/sources/new-recipe or new-recipes2 directory. You can modify your recipes in the workspace.

You can find more information by using the following command: **devtool add --help**

#### 4.7.3.2    Modify Source Code

The **_devtool_** sets up an environment to enable you to modify the existing source code in the SDK. You can modify your recipes and source code by the following command:

n  **devtool modify {recipe name}**

|   |
|---|
|~/.../build-autolinux$ ./autolinux -c devtool modify sdk-recipe|

Then, the **devtool modify** command generates a “.bbappend” file in workspace/appends/sdk-recipe.bbappend. The source code is downloaded in workspace/sources/sdk-recipe. You can modify your source code and “.bbappend”.

You can also apply the external source code to your recipe.

|   |
|---|
|~/.../build-autolinux$ git clone ssh://git.telechips.com/linux_ivi/bsp/kernel-5.10.git<br><br>~/.../build-autolinux$ ./autolinux -c devtool modify sdk-recipe|

You can find more information by using the following command: **devtool modify --help**

#### 4.7.3.3    Update Recipe

You can update the existing recipe to build the recipe for an updated set of source files by using the following command:

n  **devtool upgrade -V {version} {recipe name}**

|   |
|---|
|~/.../build-autolinux$ ./autolinux -c devtool upgrade -V 1.0.1 -S 7aa51ebda4a4512375bf12ca356afb7277e6826e sdk-recipe|

The command above updates the SRCREV of recipe. In your workspace, “sdk-recipe_1.0.1.bb” is generated in workspace/recipes directory, and “sdk-recipe_1.0.1.bbappend” is generated in workspace/appends directory.

You can find more information by using the following command: **devtool upgrade --help**

#### 4.7.3.4    After Setting Environment

If you want to build your source code or recipe, you can build it by using the following command:

n  **bitbake {recipe name} or devtool build {recipe name}**

|   |
|---|
|~/.../build-autolinux$ ./autolinux -c build "new-recipe"<br><br>~/.../build-autolinux$ ./autolinux -c devtool build new-recipe|

You can install your outputs to your target by using the following command:

n  **devtool deploy-target {recipe name} {target}**

|   |
|---|
|~/.../build-autolinux$ ./autolinux -c devtool deploy-target new-recipe root@192.168.1.1|

After you finish editing recipes and source code, you can apply your recipes to Yocto layer by using the following command:

n  **devtool finish {recipe name} {layer name}**

|   |
|---|
|~/.../build-autolinux$ ./autolinux -c devtool finish new-recipe meta-telechips<br><br>~/.../build-autolinux$ ./autolinux -c devtool finish new-recipe2 meta-telechips|

The **_devtool_** makes the devtool branch in your workspace.

If you commit your patch to devtool branch and finish executing **_devtool_**, the **devtool finish** command generates the patches and adds the patches to the recipe.

If you want to remove your local outputs, reset the recipe by using the following command:

n  **devtool reset {recipe name} or devtool reset --all**

|   |
|---|
|~/.../build-autolinux$ ./autolinux -c devtool reset recipe<br><br>~/.../build-autolinux$ ./autolinux -c devtool reset --all|

### 4.7.4   Q4. How to add Extra Package to Image

If you want to install additional packages to the image that you are currently building, you can set up the **CORE_IMAGE_EXTRA_INSTALL** variable in “conf/[[강(K47]](#_msocom_47) [[H김48]](#_msocom_48) local.conf” as follows:

|   |
|---|
|CORE_IMAGE_EXTRA_INSTALL += "openssh"|

  

 

### 4.7.5   Q5. How to modify rootfs Image without Modifying Recipes

If you temporarily modify **rootfs** and create an image, run **do_image** with the force option as follows:

|   |
|---|
|~/.../build/tcc8070-main$ pushd tmp/work/tcc8070_main-telechips-linux/automotive-linux-platform-image/1.0-r0/rootfs/<br><br>//modify rootfs<br><br>~/.../build/tcc8070-main/tmp/work/tcc8070_main-telechips-linux/automotive-linux-platform-image/1.0-r0/rootfs$ popd<br><br>~/.../build-autolinux$ ./autolinux -c build "automotive-linux-platform-image -C image"<br><br>~/.../build-autolinux$ ./autolinux -c make_fai|

### 4.7.6   Q6. How to change Default Setting from Read-only to Writable rootfs

The default setting of the SDK **rootfs** is read-only. If you want to use writable **rootfs**, you should change the **EXTRA_IMAGE_FEATURES** in “conf/l[[강(K49]](#_msocom_49) [[H김50]](#_msocom_50) ocal.conf”.

n  read-only : **EXTRA_IMAGE_FEATURES = "debug-tweaks read-only-rootfs"**

n  writeable : **EXTRA_IMAGE_FEATURES = "debug-tweaks"**

### 4.7.7   Q7. How to enable Network Environment

To use network in the SDK, enable **network** feature in **_autolinux_** script.

  

 

### 4.7.8   Q8. How to enable SSH Environment

The SDK supports SSH server based on openSSH.

**Note:** IP address, MAC address, and Gateway address must be set according to your environment.

 

To use network in the SDK, enable **ssh-server-openssh** feature in **_autolinux_** script.

Select **network** feature first, then select **ssh-server-openssh** feature.

The following is an example of TCC8070.

|   |
|---|
|**~/release/build-autolinux$ ./autolinux -c modify feature**<br><br>Read configuration from autolinux.config<br><br>Choose the Features at tcc8070-main<br><br>  1.  ufs                 Changed Boot Storage to UFS(supported : tcc8050, tcc8053, tcc8070)<br><br>  2.  bootchart           Install bootchart<br><br>  3.  **network**             Install network packages<br><br>  4.  optee               Using OPTEE<br><br>...<br><br>  0.Exit<br><br>Choose Features enable/disable (1-13): 3<br><br>Choose the Features at tcc8070-main<br><br>  1.  ufs                 Changed Boot Storage to UFS(supported : tcc8050, tcc8053, tcc8070)<br><br>  2.  bootchart           Install bootchart<br><br>* 3.  **network**             Install network packages<br><br>  4.  ssh-server-openssh  Install openssh with network packages<br><br>  5.  optee               Using OPTEE<br><br>...<br><br>  0.Exit<br><br>Choose Features enable/disable (1-14): 4<br><br>Choose the Features at tcc8070-main<br><br>  1.  ufs                 Changed Boot Storage to UFS(supported : tcc8050, tcc8053, tcc8070)<br><br>  2.  bootchart           Install bootchart<br><br>* 3.  **network**             Install network packages<br><br>* 4.  **ssh-server-openssh**  Install openssh with network packages<br><br>  5.  optee               Using OPTEE<br><br>...<br><br>  0.Exit<br><br>Choose Features enable/disable (1-14):0<br><br>...<br><br>=================================================================================<br><br>...<br><br>**FEATURES=...network,ssh-server-openssh**<br><br>...<br><br>=================================================================================<br><br>Modify feature Successful|

 

  

 

### 4.7.9   Q9. How to enable Touch Screen Driver for Multiple LCD Sub-boards

For software configuration, refer to _“TCCxxxx Common SDK-Application Note for Touch Screen Driver_”. [11]

For hardware configuration, refer to _“TCC807x Common Hardware-User Guide for EVB_”. [12]

### 4.7.10      Q10. How to build Multi-machine from One Kernel or U-Boot Source

To build multi-machine from one external source (kernel or U-Boot), enable variables related to **externalsrc** in the “conf/lo[[강(K51]](#_msocom_51) [[H김52]](#_msocom_52) cal.conf” for each machine as follows:

|   |
|---|
|INHERIT += "externalsrc"<br><br>//set kernel external source path<br><br>EXTERNALSRC:pn-linux-telechips = "${HOME}/xxx"<br><br>//set u-boot external source<br><br>EXTERNALSRC:pn-u-boot-tcc = "${HOME}/xxx"<br><br>EXTERNALSRC_BUILD:pn-u-boot-tcc = "${EXTERNALSRC:pn-u-boot-tcc}"|

Each build path is limited to multi-machine build from one kernel or U-Boot source through Yocto.

|   |
|---|
|//u-boot build path<br><br>${EXTERNALSRC:pn-u-boot-tcc}/${MACHINE}<br><br>//kernel build path<br><br>${WORKDIR}/${BPN}-${PV}|

**Important:** The configuration files (“local.conf” and “bblayers.conf”) are reset if you enter the **configure** command in **_autolinux_** again.

When using **externalsrc**, Yocto does not execute the **do_patch** task.

For details on **externalsrc**, refer to the following Yocto Project website:

n  [https://docs.yoctoproject.org/ref-manual/classes.html#externalsrc](https://docs.yoctoproject.org/ref-manual/classes.html#externalsrc)  

## 4.8    Build Application

### 4.8.1   Using Application Development Toolkit (ADT)

The ADT provided by Telechips supports Cross Compile environment based on **sysroot**, and it is based on the toolchain (**ARM GCC 11.2**) used in the Yocto build.

The ADT uses various environment variables to support the environment based on **sysroot**.

Major environment variables include **CC**, **LD**, and **CONFIGURE_FLAGS**.

Environment variables that are already defined in ADT should not be redefined in Makefile.

To build application, you should get familiar with the following information.

#### 4.8.1.1    Build ADT

Autolinux Configuration

Execute **_autolinux_** build environment in the Yocto project environment as described in Chapter 4.6.2.4. If this step is already done, you can skip this chapter and go to Chapter 4.8.1.2.

 

ADT Type Provided by Linux_YP4.0_IVI

Linux_YP4.0_IVI supports four types of ADTs as follows:

n  **meta-toolchain-telechips (ADT)**

You can install basic packages for building Linux_YP4.0_IVI-based programs by using **meta-toolchain-telechips**.

For detailed installation packages, refer to the following file:

l  poky/meta-telechips/meta-core/recipes-core/packagegroups/packagegroup-telechips-toolchain-target.bb

n  **meta-toolchain-telechips-ivi (ADT including GStreamer)**

GStreamer and Linux_YP4.0_IVI demo applications are additionally installed in the **meta-toolchain-telechips**.

For detailed installation packages, refer to the following file:

l  poky/meta-telechips/meta-ivi/recipes-telechips-ivi/packagegroups/packagegroup-als-ivi-toolchain-target.bb

n  **meta-toolchain-telechips-qt5 (ADT including GStreamer and Qt5)**

Qt5 packages are additionally installed in **meta-toolchain-telechips-ivi**.

For detailed installation packages, refer to the following files:

l  poky/meta-qt5/recipes-qt/packagegroups/packagegroup-qt5-toolchain-target.bb

l  poky/meta-telechips/meta-ivi/recipes-qt/packagegroups/packagegroup-qt5-toolchain-target.bbappend

n  **meta-toolchain-telechips-subcore (ADT)**

You can install basic packages for building Linux_YP4.0_IVI-based programs by using **meta-toolchain-telechips-subcore**.

For detailed installation packages, refer to the following file:

l  poky/meta-telechips/meta-subcore/recipes-telechips-subcore/packagegroups/packagegroup-telechips-subcore-toolchain-target.bb

  

Build ADT

To build the ADT for Main core, use the **_autolinux_** as follows:

 

n  Build ADT for the main core

|   |
|---|
|**~/release/build-autolinux$ ./autolinux -c build** "**meta-toolchain-telechips-qt5**"<br><br>Loading cache: 100% #####################################################################\| Time: 0:00:00<br><br>Loaded 1663 entries from dependency cache.<br><br>Parsing recipes: 100% ###################################################################\| Time: 0:00:00<br><br>Parsing of 1046 .bb files complete (1045 cached, 1 parsed). 1664 targets, 260 skipped, 0 masked, 0 errors.<br><br>NOTE: Resolving any missing task queue dependencies<br><br>Build Configuration:<br><br>BB_VERSION           = "2.0.0"<br><br>BUILD_SYS            = "x86_64-linux"<br><br>NATIVELSBSTRING      = "universal"<br><br>TARGET_SYS           = "aarch64-telechips-linux"<br><br>MACHINE              = "tcc8070-main"<br><br>DISTRO               = "poky-telechips-systemd"<br><br>DISTRO_VERSION       = "4.0.17"<br><br>TUNE_FEATURES        = "aarch64 armv8-2a cortexa76-cortexa55"<br><br>TARGET_FPU           = ""<br><br>LINUX_VERSION        = "5.10.205"<br><br>KBUILD_DEFCONFIG     = "tcc807x_ivi_defconfig"<br><br>IMAGE_FEATURES       = " debug-tweaks read-only-rootfs"<br><br>GCCVERSION           = "arm-11.2"<br><br>GLIBCVERSION         = "2.35%"<br><br>INVITE_PLATFORM      = " with-subcore multimedia support-4k-video qt5/wayland micom fw-update genivi"<br><br>meta<br><br>meta-poky<br><br>...<br><br>...<br><br>Initialising tasks: 100% \|###############################################################\| Time: 0:00:05<br><br>Sstate summary: Wanted 863 Found 266 Missed 597 Current 848 (30% match, 65% complete)<br><br>NOTE: Executing Tasks<br><br>NOTE: Tasks Summary: Attempted 5442 tasks of which 3600 didn't need to be rerun and all succeeded.<br><br>NOTE: Writing buildhistory<br><br>NOTE: Writing buildhistory took: 4 seconds|

When the build is successfully completed, the results come out in the following location.

|   |
|---|
|**~/release/build-autolinux$ ls -1 build/tcc8070-main/tmp/deploy/sdk/**<br><br>LINUX_YP4.0_IVI_1.0.0-tcc807x-toolchain-cortexa76-cortexa55-opengl-wayland-qt5-x86_64-gcc-arm-11.2.host.manifest<br><br>LINUX_YP4.0_IVI_1.0.0-tcc807x-toolchain-cortexa76-cortexa55-opengl-wayland-qt5-x86_64-gcc-arm-11.2.sh<br><br>LINUX_YP4.0_IVI_1.0.0-tcc807x-toolchain-cortexa76-cortexa55-opengl-wayland-qt5-x86_64-gcc-arm-11.2.target.manifest<br><br>LINUX_YP4.0_IVI_1.0.0-tcc807x-toolchain-cortexa76-cortexa55-opengl-wayland-qt5-x86_64-gcc-arm-11.2.testdata.json|

  

n  Build ADT for the sub-core

|   |
|---|
|**~/release/build-autolinux$ ./autolinux -c build sub** "**meta-toolchain-telechips-subcore**"<br><br>Loading cache: 100% #####################################################################\| Time: 0:00:00<br><br>Loaded 2052 entries from dependency cache.<br><br>NOTE: Resolving any missing task queue dependencies<br><br>Build Configuration:<br><br>BB_VERSION           = "2.0.0"<br><br>BUILD_SYS            = "x86_64-linux"<br><br>NATIVELSBSTRING      = "universal"<br><br>TARGET_SYS           = "aarch64-telechips-linux"<br><br>MACHINE              = "tcc8070-sub"<br><br>DISTRO               = "poky-telechips-systemd"<br><br>DISTRO_VERSION       = "4.0.17"<br><br>TUNE_FEATURES        = "aarch64 armv8-2a crypto cortexa55"<br><br>TARGET_FPU           = ""<br><br>LINUX_VERSION        = "5.10.205"<br><br>KBUILD_DEFCONFIG     = "tcc807x_ivi_subcore_defconfig"<br><br>IMAGE_FEATURES       = " debug-tweaks read-only-rootfs"<br><br>GCCVERSION           = "arm-11.2"<br><br>GLIBCVERSION         = "2.35%"<br><br>INVITE_PLATFORM      = " qt5/eglfs micom fw-update"<br><br>SUBCORE_APPS         = " rvc"<br><br>meta<br><br>meta-poky<br><br>...<br><br>...<br><br>Initialising tasks: 100% \|###############################################################\| Time: 0:00:05<br><br>Sstate summary: Wanted 308 Local 257 Mirrors 0 Missed 51 Current 1224 (83% match, 96% complete)<br><br>Removing 19 stale sstate objects for arch tcc8050_sub: 100% \|#############################\| Time: 0:00:01<br><br>Removing 24 stale sstate objects for arch cortexa53: 100% \|###############################\| Time: 0:00:00<br><br>NOTE: Executing Tasks<br><br>NOTE: Tasks Summary: Attempted 3882 tasks of which 3743 didn't need to be rerun and all succeeded.<br><br>NOTE: Writing buildhistory<br><br>NOTE: Writing buildhistory took: 5 seconds|

When the build is successfully completed, the results come out in the following location.

|   |
|---|
|**~/release/build-autolinux$ ls -1 build/tcc8070-sub/tmp/deploy/sdk/**<br><br>LINUX_YP4.0_IVI_1.0.0-tcc807x-toolchain-cortexa55-opengl-fbdev-subcore-x86_64-gcc-arm-11.2.host.manifest<br><br>LINUX_YP4.0_IVI_1.0.0-tcc807x-toolchain-cortexa55-opengl-fbdev-subcore-x86_64-gcc-arm-11.2.sh<br><br>LINUX_YP4.0_IVI_1.0.0-tcc807x-toolchain-cortexa55-opengl-fbdev-subcore-x86_64-gcc-arm-11.2.target.manifest<br><br>LINUX_YP4.0_IVI_1.0.0-tcc807x-toolchain-cortexa55-opengl-fbdev-subcore-x86_64-gcc-arm-11.2.testdata.json|

  

#### 4.8.1.2    Install ADT

Run the script to install ADT as follows.

**Note:** For building ADT, refer to Chapter 4.8.1.1.

|   |
|---|
|**~/release$** **./****build-autolinux/build/tcc8070-main/tmp/deploy/sdk/LINUX_YP4.0_IVI_1.0.0-tcc807x-toolchain-cortexa76-cortexa55-opengl-wayland-qt5-x86_64-gcc-arm-11.2.sh**<br><br>Telechips Baseline (Poky/meta-telechips/meta-core) SDK installer version nodistro.0<br><br>===================================================================================<br><br>Enter target directory for SDK (default: /usr/local/oecore-x86_64): ./adt<br><br>You are about to install the SDK to "/home/release/adt". Proceed [Y/n]? Y<br><br>Extracting SDK..............................................done<br><br>Setting it up...done<br><br>SDK has been successfully set up and is ready to be used.<br><br>Each time you wish to use the SDK in a new shell session, you need to source the environment setup script e.g.<br><br>$ . /home/release/adt/environment-setup-cortexa76-cortexa55-telechips-linux<br><br>~/release$|

#### 4.8.1.3    ADT Setting

Set to ADT build environment.

You can use **echo $CC** to check whether your current environment is ADT.

|   |
|---|
|**~/release$ source adt/environment-setup-cortexa76-cortexa55-telechips-linux**<br><br>**~/release$ echo $CC**<br><br>aarch64-telechips-linux-gcc -mcpu=cortex-a76.cortex-a55 -march=armv8.2-a -fstack-protector-strong -fPIE -pie -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security -fPIC --sysroot=/home/release/adt/sysroots/cortexa76-cortexa55-telechips-linux|

#### 4.8.1.4    Conduct Cross Compile by using ADT

You can use ADT to easily conduct cross complication as follows:

n  Single File Exercise

If the project source is in one file, conduct cross complication by using **$CC** as follows:

|   |
|---|
|**~/release$ $CC -o hello hello.c**|

n  Exercise based on Makefile

If the project is based on a Makefile, do not define the **AR**, **CC**, **CXX**, and **LD** variables in the Makefile.

[[김김53]](#_msocom_53) Environment variables that are already defined in ADT should not be redefined in Makefile.

n  Exercise based on **_Autotools_**

If project is based on **_Autotools_**, use **$CONFIGURE_FLAGS** as follows:

|   |
|---|
|**~/release$ aclocal**<br><br>**~/release$ autoheader**<br><br>**~/release$ autoconf**<br><br>**~/release$ automake -a**<br><br>**~/release$ ./configure $CONFIGURE_FLAGS**<br><br>**~/release$ make**|

  

 

### 4.8.2   Use Extensible SDK (eSDK)

The eSDK provided by Telechips supports the Cross Compile environment based on **sysroot**, recipes, **_devtool_**, built images, and build information.

#### 4.8.2.1    Build eSDK

Yocto Project supports extensible SDK (eSDK), which allows the followings:

n  Adding new applications and libraries to an image easily

n  Modifying the source code of an existing component

n  Testing changes on the target hardware

**Important:** To use eSDK, the host GCC version must be 7.5 or higher.

Autolinux Configuration

Execute **_autolinux_** build environment in the Yocto project environment as described in Chapter 4.6.2.4.

**Note:** If this step is already done, you can skip this chapter.

Build eSDK

To build the eSDK, use the **_autolinux_** as follows:

|   |
|---|
|**~/release/build-autolinux$ ./autolinux -c build "automotive-linux-platform-image -c populate_sdk_ext"**<br><br>Loading cache: 100% #####################################################################\| Time: 0:00:00<br><br>Loaded 1663 entries from dependency cache.<br><br>Parsing recipes: 100% ###################################################################\| Time: 0:00:00<br><br>Parsing of 1046 .bb files complete (1045 cached, 1 parsed). 1664 targets, 260 skipped, 0 masked, 0 errors.<br><br>NOTE: Resolving any missing task queue dependencies<br><br>Build Configuration:<br><br>BB_VERSION           = "2.0.0"<br><br>BUILD_SYS            = "x86_64-linux"<br><br>NATIVELSBSTRING      = "universal"<br><br>TARGET_SYS           = "aarch64-telechips-linux"<br><br>MACHINE              = "tcc8070-main"<br><br>DISTRO               = "poky-telechips-systemd"<br><br>DISTRO_VERSION       = "4.0.17"<br><br>TUNE_FEATURES        = "aarch64 armv8-2a cortexa76-cortexa55"<br><br>TARGET_FPU           = ""<br><br>LINUX_VERSION        = "5.10.205"<br><br>KBUILD_DEFCONFIG     = "tcc807x_ivi_defconfig"<br><br>IMAGE_FEATURES       = " debug-tweaks read-only-rootfs"<br><br>GCCVERSION           = "arm-11.2"<br><br>GLIBCVERSION         = "2.35%"<br><br>INVITE_PLATFORM      = " with-subcore multimedia support-4k-video qt5/wayland micom fw-update genivi"<br><br>meta<br><br>meta-poky<br><br>...<br><br>...<br><br>Initialising tasks: 100% \|###############################################################\| Time: 0:00:05<br><br>Sstate summary: Wanted 863 Found 266 Missed 597 Current 848 (30% match, 65% complete)<br><br>NOTE: Executing Tasks<br><br>NOTE: Tasks Summary: Attempted 5442 tasks of which 3600 didn't need to be rerun and all succeeded.<br><br>NOTE: Writing buildhistory<br><br>NOTE: Writing buildhistory took: 4 seconds|

When the build is successfully completed, the results come out in the following location.

|   |
|---|
|**~/release/build-autolinux$ ls -1 build/tcc8070-main/tmp/deploy/sdk/**<br><br>poky-telechips-systemd-glibc-x86_64-automotive-linux-platform-image-cortexa76-cortexa55-toolchain-ext-nodistro.0.host.manifest<br><br>poky-telechips-systemd-glibc-x86_64-automotive-linux-platform-image-cortexa76-cortexa55-toolchain-ext-nodistro.0.sh<br><br>poky-telechips-systemd-glibc-x86_64-automotive-linux-platform-image-cortexa76-cortexa55-toolchain-ext-nodistro.0.target.manifest<br><br>poky-telechips-systemd-glibc-x86_64-automotive-linux-platform-image-cortexa76-cortexa55-toolchain-ext-nodistro.0.testdata.json<br><br>x86_64-buildtools-nativesdk-standalone-4.0.17.host.manifest<br><br>x86_64-buildtools-nativesdk-standalone-4.0.17.sh<br><br>x86_64-buildtools-nativesdk-standalone-4.0.17.target.manifest<br><br>x86_64-buildtools-nativesdk-standalone-4.0.17.testdata.json|

#### 4.8.2.2    Install eSDK

Execute the following script to install eSDK. For building eSDK, refer to Chapter 4.8.2.1.

|   |
|---|
|**~/eSDK$ ./poky-telechips-systemd-glibc-x86_64-automotive-linux-platform-image-cortexa76-cortexa55-toolchain-ext-nodistro.0.sh**<br><br>Telechips Baseline (Poky/meta-telechips/meta-core) Extensible SDK installer version nodistro.0<br><br>==============================================================================================<br><br>Enter target directory for SDK (default: ~/poky-telechips-systemd_sdk): ./maincore<br><br>You are about to install the SDK to "/home/eSDK/maincore". Proceed [Y/n]? Y<br><br>Extracting SDK........................................................................................done<br><br>Setting it up...<br><br>Extracting buildtools...<br><br>Preparing build system...<br><br>~/eSDK$ ls maincore/<br><br>bitbake-cookerdaemon.log<br><br>buildtools/<br><br>cache/<br><br>conf/<br><br>downloads/<br><br>environment-setup-cortexa76-cortexa55-telechips-linux<br><br>layers/<br><br>preparing_build_system.log<br><br>site-config-cortexa76-cortexa55-telechips-linux<br><br>sstate-cache/<br><br>sysroots/<br><br>tmp/<br><br>version-cortexa76-cortexa55-telechips-linux<br><br>workspace/|

The important directories and files included in the eSDK are as follows:

n  **buildtools:** Tools to configure the build environment of Yocto Project for the Linux_YP4.0_IVI

n  **conf:** Directory that contains user configuration files such as “local.conf” and “bblayers.conf”

n  **downloads:** Directory that contains the downloaded files

n  **environment-setup-cortexa76-cortexa55-telechips-linux:** Script file to set eSDK environment

n  **layers:** Directory that contains recipes, patches, configuration files, and so on that are required for building the eSDK

n  **sstate-cache:** Directory that contains prebuilt cache

n  **workspace:** Directory that contains recipes and source code in working

#### 4.8.2.3    Build Application

Yocto project supports **_devtool_** that provides the several features for developer. Refer to Chapter 4.7.3 to modify source code.

### 4.8.3   Copy Application File to Board via USB

**{Storage_Path}** depends on the build option (UFS mode or not) and the number of connected storages.

Check and use the path set when connecting storage. (**Example**: /run/media/sda1)

#### 4.8.3.1    Connect to Main Core

1.       Connect USB storage to USB3.0 Host or USB2.0 DRD port.

2.       When copying the application file to root folder, run the following **copy** command:

n  **root@telechips-MACHINE:~# cp {Storage_Path}/user_file .**

3.       If the copied path has authority of read-only, you need to run the following **remount** and **copy** commands.

n  **root@telechips-MACHINE:~# mount -o remount,rw /**

n  **root@telechips-MACHINE:~# cp {Storage_Path}/user_file .**

 

#### 4.8.3.2    Connect to Sub-core

1.       Connect USB storage to USB2.0 Host port.  
  

2.       When copying the application file to root folder, run the following **copy** command.

n  **root@telechips-MACHINE:~# cp {Storage_Path}/user_file .**  
  

3.       If the copied path has authority of read-only, you need to run the following **remount** and **copy** commands.

n  **root@telechips-MACHINE:~# mount -o remount,rw /**

n  **root@telechips-MACHINE:~# cp {Storage_Path}/user_file .**[[조(C54]](#_msocom_54) [[김김55]](#_msocom_55) 

# 5         Firmware Downloader (FWDN) Guide

This chapter describes how to download the Linux_YP4.0_IVI to TCC805x Evaluation Board (EVB) and to log in the Linux console.

For more information on how to use the tools for **_Firmware Downloader_**, refer to the following documents.

n  **FWDN V8**: “_TCCxxxx Common-User Guide for Firmware Downloader V8_” [8]

n  **mktcimg**: “_TC Common-User Guide for mktcimg_” [10]

The **_FWDN V8_** is a PC tool for downloading firmware in Windows 10 64-bit and Linux environments.

This chapter describes the case of downloading in Windows environment. For Linux, refer to "_TCCxxxx Common-User Guide for Firmware Downloader V8_”. [8]

## 5.1    System Requirement

### 5.1.1   Software Requirement

Table 5.1 Software Requirement

|   |   |   |   |
|---|---|---|---|
|**Category**|**Description**|**Path**|**Note**|
|VTC Driver|Driver for Windows PC that is used to download Linux_YP4.0_IVI firmware.<br><br>VTC driver corresponding to the Windows version must be installed.<br><br>It is installed only once on your PC.|fwdn_v8/out/vtcdrv v5.0.0.14.zip|V5.0.0.14 or higher is strongly recommended.<br><br>Refer to VTC Driver information path:<br><br>n  "ReadMe.txt" in vtcdrv v5.0.0.14.zip|
|FWDN|Tools for downloading Linux_YP4.0_IVI firmware|fwdn_v8/out/fwdn<br><br>or<br><br>fwdn_v8/out/fwdn.exe|You must use **_FWDN V8_**.|

### 5.1.2   Hardware Requirement

Table 5.2 Hardware Requirement

|   |   |   |
|---|---|---|
|**Category**|**Description**|**Note**|
|Demo Board|Supported chipsets are TCC807x.|-|
|Power Adapter|12V power adapter is used to supply power to the board and LCD.|Recommend using the power adapter (12V) provided by Telechips.|
|USB Cable|It is used to connect a demo board to PC.|Refer to Chapter 2.2.1 for USB cable connection.|

  

## 5.2    Linux_YP4.0_IVI Firmware Construction

Note: If you have already built the SDK following Chapter 4.6.2.5 and have created “SD_Data.fai”, you can skip this chapter.[[김김56]](#_msocom_56) 

Table 5.3 Linux_YP4.0_IVI Firmware Construction

|**Image Type**|**Description**|
|---|---|
|U-Boot  <br>boot loader Image<br><br>(*.rom)|Image to initialize the system hardware and put the Linux kernel image into memory for execution<br><br>Refer to the following example for the U-Boot image names used in each core.<br><br>Main core: ap0_bl3.rom<br><br>Sub-core: ap1_bl3.rom|
|Kernel Image<br><br>(*.img)|Boot image file in which the Linux kernel is compressed<br><br>Refer to the following example for the Kernel image names used in each board.<br><br>**Example:**<br><br>tc-boot-[MACHINE].img<br><br>Main core: tc-boot-tcc8070-main.img<br><br>Sub-core: tc-boot-tcc8070-sub.img|
|Root File System Image<br><br>(*.ext4)|Image that is served as the root file system for Linux system<br><br>Refer to the following example for the root file system image names used in each machine.<br><br>By default, the generated Root File System Image is read-only.<br><br>**Example:**<br><br>Main core: automotive-linux-platform-image-[MACHINE].ext4<br><br>automotive-linux-platform-image-tcc8070-main.ext4<br><br>Sub-core: telechips-ivi-subcore-image-[MACHINE].ext4<br><br>telechips-ivi-subcore-image-tcc8070-sub.ext4|
|RW Partition Image<br><br>(Home directory)<br><br>(*.ext4)|It is used to store the RW data of the database and application used in Media Player as the RW area required by Linux_YP4.0_IVI.<br><br>**Example:** home-directory.ext4|
|Device Tree Binary (DTB) Image  <br>(*.dtb)|Image that contains driver information on the hardware devices of each board<br><br>Refer to the following example for the dtb image names used in each core.<br><br>**Example:**<br><br>Main core: [chip_name]-ivi-[board_name].dtb<br><br>tcc8070-ivi-lpd4x322.dtb<br><br>Sub-core: [chip_name]-ivi-subcore-[board_name].dtb<br><br>tcc8070-ivi-subcore-lpd4x322.dtb|
|SNOR Image<br><br>(*.rom)|This image contains SNOR firmware image.<br><br>SNOR image uses prebuilt image. Refer to the following example for the SNOR image.<br><br>**Example:** tcc807x_snor.rom|
|bconf.bin|This is an image of the configuration information for the chipboot code and the boot firmware such as BL1/2 and SC F/W|
|ap0_bl1.rom|This is an image of trusted-firmware BL1 for CA76|
|ap0_bl2.rom|This is an image of trusted-firmware BL2 for CA76|
|ap0_lib.rom|This is an image of DRAM initialization code used by trusted-firmware BL1 for CA76|
|ap1_bl1.rom|This is an image of trusted-firmware BL1 for CA55|
|ap1_bl2.rom|This is an image of trusted-firmware BL2 for CA55|
|ap1_lib.rom|This is an image of DRAM initialization code used by trusted-firmware BL1 for CA55|
|dram_params.bin|This is the DRAM parameter information data used during initialization of DRAM|
|fwdn.rom|This is an image of firmware that runs in Safety Island Controller (SIG) to use **_FWDN_**.|
|hsm.bin|This is an image of firmware that runs in Hardware Security Module (HSM).|
|mcert.bin|This is the image where the master key for Secure Boot is stored.|
|optee.rom|This is an image of Trusted Environment Execution (TEE) OS for CA76.|
|subcore_optee.rom|This is an image of Trusted Environment Execution (TEE) OS for CA55|
|tcc807x_snor.rom|This is an image to initialize the system hardware and execute the main firmware of SIC image.|
|scfw.rom|This is an image of storage core firmware.|

**Note 1:** Use Linux **dd** command to create RW file system for home directory image:

n  **$ dd if=/dev/zero of=home-directory.ext4 bs=1K count=512000**

n  **Case of eMMC:  
$ mkfs.ext4 home-directory.ext4  
Case of UFS:  
$ mkfs.ext4 -b 4096 home-directory.ext4**

**Note 2:**

n   chip_name = tcc8070

n   MACHINE = [chip_name]-main or sub

**Example**: tcc8070-main, tcc8070-sub

n   board_name = lpd4x322

### 5.2.1   Boot-firmware

Linux_YP4.0_IVI requires “fwdn.rom”, HSM, trusted firmware-A, and storage core firmware. These files are included in the boot-firmware. You can get the boot-firmware from SDK.

|   |
|---|
|$ ls -1 boot-firmware_tcc807x/prebuilt/<br><br>ap0_bl1.rom<br><br>ap0_bl2.rom<br><br>ap0_lib.rom<br><br>ap1_bl1.rom<br><br>ap1_bl2.rom<br><br>ap1_lib.rom<br><br>bconf.bin<br><br>dram_params.bin<br><br>fwdn.rom<br><br>hsm.bin<br><br>mcert.bin<br><br>mxic_mx25l25645g.bin<br><br>optee.rom<br><br>scfw.rom<br><br>sic-fw.rom<br><br>snor_read_3b.bin<br><br>subcore_optee.rom<br><br>tcc807x_snor.rom<br><br>ufs/|

#### 5.2.1.1    Make bconf.bin

**Note:** You should make “bconf.bin” according to **boot option**.

1.       Go to the boot-firmware that you downloaded.

|   |
|---|
|$ cd boot-firmware_tcc807x/|

2.       Edit “tcc807x_bconf.xml”.

n  **Example 1**: For single boot, change the **bootsel** to **single**.

|   |
|---|
|$ vi tools/bconf_maker/tcc807x_bconf.xml<br><br><!--<br><br>    ** boot option<br><br>    bootsel<br><br>        - dual: boot with main/sub cores<br><br>        - single: boot with main core only<br><br>    imgmaptype<br><br>        - 0: BL3 image in user, OPTEE image in boot part<br><br>        - 1: BL3 image/OPTEE image in boot part<br><br>        - 2: BL3 image in boot part, OPTEE image in user<br><br>    mainsys<br><br>        - main: main cluster is the main system, init dram<br><br>        - sub: sub-cluster is the main system, init dram<br><br>--><br><br><bootconfig bootsel="**single**" imgmaptype="0" mainsys="main"/|

n  **Example 2**: For STR feature, change the IPC configuration.

  
**Important:** This configuration value is essential for using the Telechips EVB/VCP module. You must configure it as follows according to your hardware configuration.

|   |
|---|
|$ vi tools/bconf_maker/tcc807x_bconf.xml<br><br><!--<br><br>    ** AP-MCU IPC configuration<br><br>    device<br><br>        - none<br><br>        - uart<br><br>        - gpsb<br><br>    port: port number for UART or GPSB<br><br>    *** device configuration for uart<br><br>        baudrate: UART baud rate (max: 115200)<br><br>    *** device configuration for gpsb<br><br>        reg: SPI start request pin gpio group register offset<br><br>        pin: SPI start request pin num<br><br>--><br><br><ipc device="gpsb" port="39" reg="0x740" pin="21"/>|

3.       Make “bconf.bin”.

|   |
|---|
|$ python tools/bconf_maker/bconf_maker_v01.py -c tools/bconf_maker/tcc807x_bconf.xml -o prebuilt/bconf.bin|

 

  

 

### 5.2.2   Make SD Data using make_fai[[김57]](#_msocom_57) 

#### 5.2.2.1    Check Device Information

Before creating the fai file, it must be created according to the customer's eMMC Capacity or UFS Capacity.

1.       Connect **_FWDN V8_** to the board.

2.       Check User capacity in eMMC Info or LUN2 (User) capacity in UFS Info.  
  

**Note:** To connect **_FWDN V8_** to the board, refer to Chapter 5.4.3.

|   |
|---|
|fwdn> [fwdn.exe](https://wiki.telechips.com:8443/display/A2/fwdn.exe) --fwdn ...\boot-firmware\fwdn.json<br><br>...<br><br>...<br><br>fwdn> fwdn.exe --device-info<br><br>[main:30] FWDN V8 v1.4.12 - 2023.6.22 11:23:58<br><br>[FWDN_V8::GetFWDNRomVersion:1588] fwdn.rom version : 23.5.22<br><br>[FWDN_V8::PrintDeviceInfo:1201] --------------Device info-------------<br><br>[FWDN_V8::PrintDeviceInfo:1202]<br><br>----- Detail of Storages -----<br><br>#### eMMC Info ####<br><br>Manufacture ID: 0x11<br><br>OEM: 0x100<br><br>Name: 008GB<br><br>User Capacity: 7.3 GiB (7818182656 Byte)<br><br>Boot Capacity: 8 MiB (8388608 Byte)<br><br>RPMB Capacity: 4 MiB (4194304 Byte)<br><br>Speed Mode: HS200<br><br>#### SNOR Info ####<br><br>Manufacture ID: 0xc2<br><br>Device ID: 0x2019<br><br>Name: MXIC-MX25L25645G<br><br>Sector Size: 4 KiB (4096 Byte)<br><br>Total Capacity: 32 MiB (33554432 Byte)<br><br>4Byte Address Mode: Supported<br><br>#### UFS Info ####<br><br>Vendor : TOSHIBA<br><br>Product : THGAFEG8T10100<br><br>Revision : 0100<br><br>bSecureRemovalType : 3<br><br>LUN0(Boot) Capcity: 8 MiB(8388608 Byte)<br><br>LUN0(Boot) bProvisioningType = 3<br><br>LUN1(Boot) Capcity: 8 MiB(8388608 Byte)<br><br>LUN1(Boot) bProvisioningType = 3<br><br>LUN2(User) Capcity: 29.8 GiB(31998345216 Byte)<br><br>LUN2(Boot) bProvisioningType = 3<br><br>Total Capacity: 29.8 GiB(32015122432 Byte)<br><br>----- Summary of Storages -----<br><br>eMMC : O<br><br>SNOR : O<br><br>UFS : O<br><br>- O : Init success<br><br>- X : Init failed or not exist<br><br>----- Summary of DRAM Init -----<br><br>DRAM Init : Success (Result 0x0 )<br><br>DRAM Size : 8192MB<br><br>[FWDN_V8::PrintDeviceInfo:1203] --------------------------------------<br><br>[main:156] Complete FWDN|

**Note:** The Byte capacity of User capacity is written as eMMC_storage_size (Byte), and the LUN2 (User) capacity is written as UFS_storage_size (Byte).

  

#### 5.2.2.2    Create SD Data with eMMC/UFS size

Add the confirmed eMMc or UFS capacity (Byte) to **STORAGE_SIZE** in local.conf.

|   |
|---|
|~/release/build-autolinux$ vi build/tcc8070-main/conf/[[강(K58]](#_msocom_58) [[H김59]](#_msocom_59) local.conf<br><br>In case of eMMC,<br><br># Storage Size<br><br># Set STORAGE_SIZE variable according to the storage size you are using<br><br>STORAGE_SIZE = "7818182656"<br><br>In case of UFS,<br><br># Storage Size<br><br># Set STORAGE_SIZE variable according to the storage size you are using<br><br>STORAGE_SIZE = "31998345216"|

|   |
|---|
|~/release/build-autolinux$ ./autolinux -c build|

After adding eMMC size, Makes SD Data and “partition.list[[강(K60]](#_msocom_60) [[김(K61]](#_msocom_61) ” based on the contents of “make_fai.bbclass”.

**Note:** Class files are used to abstract common functionality and share it amongst multiple recipe (.bb) files. To use a class file, the recipe should inherit the class.

|   |
|---|
|~/release/build-autolinux$ ./autolinux -c make_fai|

  

#### 5.2.2.3    Partition Information of SD Data

**Type 1**: With meta-update (default)

|**FWDN  <br>Partition**|**Size  <br>(KB)**|**Label Name**|**Block Device**<br><br>**(eMMC)**|**Description**|**File Name**|
|---|---|---|---|---|---|
|Partition 1|2048|bl3_ap0_a|mmcblk0p1|Main Core Boot Loader A|ap0_bl3.rom|
|Partition 2|2048|bl3_ap0_b|mmcblk0p2|Main Core Boot Loader B|ap0_bl3.rom|
|Partition 3|40960|boot_a|mmcblk0p3|Kernel image A|tc-boot-[MACHINE].img|
|Partition 4|40960|boot_b|mmcblk0p4|Kernel image B|tc-boot-[MACHINE].img|
|Partition 5|Customized|system_a|mmcblk0p5|Root file system A|automotive-linux-platform-image-[MACHINE].ext4|
|Partition 6|Customized|system_b|mmcblk0p6|Root file system B|automotive-linux-platform-image-[MACHINE].ext4|
|Partition 7|1024|dtb_a|mmcblk0p7|Device tree A|[chip_name]-ivi-[board_name].dtb|
|Partition 8|1024|dtb_b|mmcblk0p8|Device tree B|[chip_name]-ivi-[board_name].dtb|
|Partition 9|1024|env|mmcblk0p9|Environment|-|
|Partition 10|1024|misc|mmcblk0p10|Miscellaneous|-|
|Partition 11|40960|splash|mmcblk0p11|Splash|-|
|Partition 12|512000|home|mmcblk0p12|RW file system for home directory|home-directory.ext4|
|Partition 13|2048|bl3_ap1_a|mmcblk0p13|Sub-core Boot Loader A<br><br>(optional)|ap1_bl3.rom|
|Partition 14|2048|bl3_ap1_b|mmcblk0p14|Sub-core Boot Loader B<br><br>(optional)|ap1_bl3.rom|
|Partition 15|40960|subcore_boot_a|mmcblk0p15|Sub-core Kernel Image A<br><br>(optional)|tc-boot-[MACHINE].img|
|Partition 16|40960|subcore_boot_b|mmcblk0p16|Sub-core Kernel Image B<br><br>(optional)|tc-boot-[MACHINE].img|
|Partition 17|1024|subcore_dtb_a|mmcblk0p17|Sub-core Device tree A<br><br>(optional)|[chip_name]-ivi-subcore-[board_name].dtb|
|Partition 18|1024|subcore_dtb_b|mmcblk0p18|Sub-core Device tree B<br><br>(optional)|[chip_name]-ivi-subcore-[board_name].dtb|
|Partition 19|Customized|subcore_root_a|mmcblk0p19|Sub-core root file system A<br><br>(optional)|telechips-ivi-subcore-image-[MACHINE].ext4|
|Partition 20|Customized|subcore_root_b|mmcblk0p20|Sub-core root file system B<br><br>(optional)|telechips-ivi-subcore-image-[MACHINE].ext4|
|Partition 21|1024|subcore_env|mmcblk0p21|Sub-core Environment<br><br>(optional)|-|
|Partition 22|1024|subcore_misc|mmcblk0p22|Sub-core miscellaneous|-|
|Partition 23|Remainder|data|mmcblk0p23|User storage|user-data.ext4|

  

**Type 2**: Without meta-update

|**FWDN  <br>Partition**|**Size  <br>(KB)**|**Label Name**|**Block Device**<br><br>**(eMMC)**|**Description**|**File Name**|
|---|---|---|---|---|---|
|Partition 1|2048|bl3_ap0_a|mmcblk0p1|Main Core Boot Loader A|ap0_bl3.rom|
|Partition 2|2048|bl3_ap0_b|mmcblk0p2|Main Core Boot Loader B|ap0_bl3.rom|
|Partition 3|40960|boot_a|mmcblk0p3|Kernel image A|tc-boot-[MACHINE].img|
|Partition 4|Customized|system_a|mmcblk0p4|Root file system B|automotive-linux-platform-image-[MACHINE].ext4|
|Partition 5|1024|dtb_a|mmcblk0p5|Device tree A|[chip_name]-ivi-[board_name].dtb|
|Partition 6|1024|misc|mmcblk0p6|Miscellaneous|-|
|Partition 7|40960|splash|mmcblk0p7|Splash|-|
|Partition 8|512000|home|mmcblk0p8|RW file system  <br>for home directory|home-directory.ext4|
|Partition 9|2048|bl3_ap1_a|mmcblk0p9|Sub-core Boot Loader A<br><br>(optional)|ap1_bl3.rom|
|Partition 10|2048|bl3_ap1_a|mmcblk0p10|Sub-core Boot Loader B<br><br>(optional)|ap1_bl3.rom|
|Partition 11|40960|subcore_boot_a|mmcblk0p11|Sub-core Kernel Image A<br><br>(optional)|tc-boot-[MACHINE].img|
|Partition 12|1024|subcore_dtb_a|mmcblk0p12|Sub-core Device tree B<br><br>(optional)|[chip_name]-ivi-subcore-[board_name].dtb|
|Partition 13|Customized|subcore_root_a|mmcblk0p13|Sub-core root file system A<br><br>(optional)|telechips-ivi-subcore-image-[MACHINE].ext4|
|Partition 14|1024|subcore_misc|mmcblk0p14|Sub-core miscellaneous|-|
|Partition 15|512000|home_Sub|mmcblk0p15|Sub-core RW file system for home directory|home-directory.ext4|
|Partition 16|1024|subcore_env|mmcblk0p16|Sub-core Environment<br><br>(optional)|-|
|Partition 17|1024|env|mmcblk0p17|Environment|-|
|Partition 18|Remainder|data|mmcblk0p18|User storage|user-data.ext4|

  

If you want to add or redefine a partition, follow the steps below and re-make SD Data.

n  Add Partition

The following example shows how to add a partition.

|   |
|---|
|~/release/build-autolinux$ vi poky/meta-telechips/meta-core/classes/make_fai_customer.bbclass|

|   |
|---|
|inherit make_fai<br><br>make_plist_tcc807x:append() {<br><br>        **echo "example:100M@"                    >> ${DEPLOY_DIR}/fwdn/partition.list$1**<br><br>}|

|   |
|---|
|~/release/build-autolinux$ vi poky/meta-telechips/meta-core/classes/tcc-base-image.bbclass|

|   |
|---|
|#<br><br># Copyright (C) Telechips Inc.<br><br>#<br><br>inherit core-image extrausers make_fai chk_security **make_fai_customer**<br><br>IMAGE_FSTYPES = "squashfs ext4"<br><br>...|

n  Redefine Partition

This example renames an existing partition to **rom_a** and **rom_b**.

|   |
|---|
|~/release/build-autolinux$ vi poky/meta-telechips/meta-core/classes/make_fai_customer.bbclass|

|   |
|---|
|inherit make_fai<br><br>MAKE_PLIST = "make_plist_customer"<br><br>make_plist_customer() {<br><br>        **echo "rom_a:2M@${DEPLOY_DIR}/images/${MACHINE}/ap0_bl3.rom$1"                         >> ${DEPLOY_DIR}/fwdn/partition.list$1**<br><br>        **echo "rom_b:2M@${DEPLOY_DIR}/images/${MACHINE}/ap0_bl3.rom$1"                         >> ${DEPLOY_DIR}/fwdn/partition.list$1**<br><br>}|

|   |
|---|
|~/release/build-autolinux$ vi poky/meta-telechips/meta-core/classes/tcc-base-image.bbclass|

|   |
|---|
|#<br><br># Copyright (C) Telechips Inc.<br><br>#<br><br>inherit core-image extrausers make_fai chk_security **make_fai_customer**<br><br>IMAGE_FSTYPES = "squashfs ext4"<br><br>...|

  

### 5.2.3   Make SNOR ROM Image

Pre-built images are in the following path:

n  “tcc8070_snor.rom” in boot-firmware_tcc807x/prebuilt  

If you need to change the binary stored in the SNOR ROM, you must make a new SNOR ROM image.

To make SNOR ROM image of TCC807x, use the **_snor_image_maker_** in boot-firmware as follows:

|   |
|---|
|$ cd boot-firmware-tcc807x/tools/snor_image_maker/<br><br>$ python3 snor_image_maker.py -c tcc807x_snor.json -o ../../prebuilt/tcc807x_snor.rom|

The “tcc807x_snor.json” is a list of files with their offset address on SNOR flash

|   |
|---|
|{<br><br>    "area0": {<br><br>        ".\\prebuilt\\mxic_mx25um51245g_OPI_100_DTR.bin" : [{"storage" : "snor", "area" : "die1", "addr" : "0x00000000"}],<br><br>        ".\\prebuilt\\mcert.bin" : [{"storage" : "snor", "area" : "die1", "addr" : "0x00000008"}],<br><br>        ".\\prebuilt\\hsm.bin" : [{"storage" : "snor", "area" : "die1", "addr" : "0x00000010"}],<br><br>        ".\\prebuilt\\sic-fw.rom" : [{"storage" : "snor", "area" : "die1", "addr" : "0x00000050"}]<br><br>    },<br><br>    "area1": {<br><br>        ".\\prebuilt\\mxic_mx25um51245g_OPI_100_DTR.bin" : [{"storage" : "snor", "area" : "die1", "addr" : "0x00000450"}],<br><br>        ".\\prebuilt\\mcert.bin" : [{"storage" : "snor", "area" : "die1", "addr" : "0x00000458"}],<br><br>        ".\\prebuilt\\hsm.bin" : [{"storage" : "snor", "area" : "die1", "addr" : "0x000000460"}],<br><br>        ".\\prebuilt\\sic-fw.rom" : [{"storage" : "snor", "area" : "die1", "addr" : "0x000004A0"}]<br><br>    }<br><br>}|

#### 5.2.3.1    snor_conf_maker

SNOR ROM image contains configuration data that consists of SFMC register information and SFMC instructions.

The configuration data is initially written in XML format and converted to a binary file by the **snor_conf_maker** in boot-firmware as follows:

|   |
|---|
|$ cd boot-firmware/tools/snor_conf_maker<br><br>$ python3 snor_conf_maker.py -c mxic_mx25um51245g_OPI_100_DTR.xml -o mxic_mx25um51245g_OPI_100_DTR.bin|

**Important:** The distributed Linux_YP4.0_IVI_1.0.0 does not properly support SNOR boot mode. To use SNOR boot mode, you need to apply a fix patch, contact Telechips. [1]

## 5.3    Install VTC Driver

Install USB driver (VTC Driver V5.0.0.14) for **_FWDN_** on your Windows PC. You only need to install this driver once.

Figure 5.1 VTC Driver Installation Screen

Use the VTC driver V5.0.0.14 or higher. If you use previous version, install the latest version.

To check the version, confirm the device manager in Windows environment.

The VTC driver installation file (vtcdrv v5.0.0.14.zip) is included in **_fwdn_v8/out_** in the SDK.

  

## 5.4    Linux_YP4.0_IVI Firmware Download Sequence

The downloading sequence of **_FWDN_** is as follows:

1.       Set the boot mode switch to USB boot mode.

2.       Connect 12V power adapter to board.

3.       Open Windows prompt or Linux console and test **_FWDN V8_**.

4.       Connect **_FWDN V8_** to board.

5.       Execute **--low-format** command by using **_FWDN V8_**.

6.       Download pre-built boot F/W image.

7.       Download images to SNOR for SIC.

8.       Download “.fai” file.

9.       Download Image to GPT Partition. (Optional)

10.    Set the boot mode switch (eMMC, SNOR/eMMC, UFS, or SNOR/UFS) and reset.

**Note 1:** **_FWDN V8_** runs in Windows 10 or Linux environment.

**Note 2:** Use **_FWDN V8_** v1.4.12 or higher.

### 5.4.1   Set Board to USB Boot Mode

Refer to Chapter 2.2.1.

 

### 5.4.2   Open Windows Prompt or Linux Console and Test FWDN V8

|   |
|---|
|fwdn> [fwdn.exe](https://wiki.telechips.com:8443/display/A2/fwdn.exe) --help<br><br>[main:30] FWDN V8 v1.4.12 - 2023.6.22 11:23:58<br><br>Usage : fwdn <command> <options><br><br>Example:<br><br>  Start to fwdn(load FWDN F/W) :<br><br>    fwdn --fwdn tcc805x_fwdn.json<br><br>  Download files written to a config file :<br><br>    fwdn --write tcc805x_boot.json<br><br>  Download file :<br><br>    fwdn -w [file name] -m emmc --area boot0<br><br>    fwdn -w [file name] -m emmc --area boot1 -s 512<br><br>  Download file at GPT partition:<br><br>    fwdn -w [file name] -m emmc --area user --part boot<br><br>    fwdn -w [file name] -m ufs --area user --part boot --sector-size 4096<br><br>  Read dump :<br><br>    fwdn -r [file name] -m emmc --area boot1 --size 0x100 --addr 0x123456<br><br>    fwdn -r [file name] -m emmc --area boot1 --size 0x100<br><br>...|

### 5.4.3   Connect FWDN V8 to Board

|   |
|---|
|fwdn> [fwdn.exe](https://wiki.telechips.com:8443/display/A2/fwdn.exe) --fwdn ...\boot-firmware\fwdn.json|

 

### 5.4.4   Execute --low-format Command by Using FWDN V8 (Optional)

|   |
|---|
|fwdn> [fwdn.exe](https://wiki.telechips.com:8443/display/A2/fwdn.exe) --storage emmc --low-format|

**Note:** This task is optional. If this task is not required, you can skip this chapter.

### 5.4.5   Download Pre-built F/W Image

|   |
|---|
|fwdn> [fwdn.exe](https://wiki.telechips.com:8443/display/A2/fwdn.exe) -w ...\boot-firmware\boot.json|

  

### 5.4.6   Download Images to SNOR for SIC

|   |
|---|
|fwdn> fwdn.exe --write ...\prebuilt\tcc807x_snor.rom --area die1 --storage snor|

### 5.4.7   Download “.FAI” File

Depending on the storage, you should use different option as follows:

n  eMMC: **--storage emmc**

|   |
|---|
|fwdn> [fwdn.exe](https://wiki.telechips.com:8443/display/A2/fwdn.exe) -w ...\SD_Data.fai --storage emmc --area user|

n  UFS: **--storage ufs --sector-size 4096**

|   |
|---|
|fwdn> [fwdn.exe](https://wiki.telechips.com:8443/display/A2/fwdn.exe) -w ...\SD_Data.fai --storage ufs --area user --sector-size 4096|

### 5.4.8   Download Images to GPT Partition (Optional)

If you want to download only a specific partition, follow the example below: Download “boot.img” to eMMC’s boot partition.

Depending on the storage, you should use different option as follows:

n  eMMC: **--storage emmc**

|   |
|---|
|fwdn> [fwdn.exe](https://wiki.telechips.com:8443/display/A2/fwdn.exe) -w ...\boot.img --storage emmc --area user --part boot_a|

n  UFS: **--storage ufs --sector-size 4096**[[김62]](#_msocom_62) 

|   |
|---|
|fwdn> [fwdn.exe](https://wiki.telechips.com:8443/display/A2/fwdn.exe) -w ...\boot.img --storage ufs --sector-size 4096 --area user --part boot_a|

### 5.4.9   Complete FWDN and Reset Board

Set the boot mode switch to the desired boot mode and reset the board.

# 6         Booting Guide

This chapter describes booting guide for TCC807x EVB.

## 6.1    Booting Guide for Board

### 6.1.1   Booting Screen

After power is supplied to board for normal booting, U-Boot screen is shown as follows:

Figure 6.1 U-Boot Screen

### 6.1.2   Linux Console Login

After firmware writing is completed, you can see the log message on the Linux console as shown in Figure 6.3.

Figure 6.2 Connected USB to UART Bridge Interface

**Caution:** When resetting the EVB, you must remove USB cable from USB2.0 DRD port to protect board and host PC.

To use the USB Type-C cable, check the driver first. If the driver is not installed, install or re-install UART driver.

You can download the latest version at the official homepage:

n  [https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)

Connect UART serial cable to PC, to check console message.

n  UART configuration is as follows:

l  Baud rate         : 115200 bps

l  Data bits          : 8

l  Stop bits          : 1

l  Parity              : None

n  Login ID and Password are **root**.

Figure 6.3 Console Login

# 7         References

[1]    Contact Telechips for more details: [sales@telechips.com](mailto:sales@telechips.com)

[2]    Yocto Project Quick Build: [https://docs.yoctoproject.org/dev-manual/start.html](https://docs.yoctoproject.org/dev-manual/start.html)

[3]    Yocto Project Wiki: [https://wiki.yoctoproject.org/wiki/Main_Page](https://wiki.yoctoproject.org/wiki/Main_Page)

[4]    Yocto Project Development Tasks Manual: [https://docs.yoctoproject.org/kernel-dev/index.html](https://docs.yoctoproject.org/kernel-dev/index.html)

[5]    Yocto Project Reference Manual: [https://docs.yoctoproject.org/ref-manual/index.html](https://docs.yoctoproject.org/ref-manual/index.html)

[6]    Yocto Project Application Development and the Extensible Software Development Kit (eSDK): [https://docs.yoctoproject.org/sdk-manual/index.html](https://docs.yoctoproject.org/sdk-manual/index.html)

[7]    BitBake User Manual: [https://docs.yoctoproject.org/bitbake.html](https://docs.yoctoproject.org/bitbake.html)

[8]    TCC807x Common Hardware-Assembly Manual for EVB

[9]     TCCxxxx Common-User Guide for Firmware Downloader V8

[10]  TC Common-User Guide for mktcimg

[11]  TCCxxxx Common SDK-Application Note for Touch Screen Driver

[12]  TCC807x Common Hardware-User Guide for EVB

[13]  TCC70xx Common-User Guide for Firmware Downloader_VCP

[14]  TCCxxxx Common SDK-User Guide for AUO and BOE touch IC

**Note**: Reference documents can be provided whenever available, depending on the terms of a contract. If the reference documents are unavailable, the contents directly related to your development can be guided.

# 8         Revision History

## Rev. 1.20: 2024-10-22

n  Updated

l  Chapter 2.1: **Important**

l  Chapter 4.5.1: Website address of repo

l  Chapter 4.6.3.5.5: Added **Note**

l  Chapter 5.2.3: Description and Source code (execute command)

l  Chapter 7: Added [14]

n  Added

l  Chapter 5.2.3.1: snor_conf_maker

n  Deleted

l  Chapter 5.2.3.1: tcc807x.cfg

l  Chapter 4.7.7.1: Use Network with Static IP

## Rev. 1.10: 2024-05-31

n  Updated

l  Chapter [4.4.1](#_Linux_Distribution_Versions): Website address of Yocto Project

l  Chapter 4.4.2: Website address of Yocto Project

l  Chapter 4.6.2.1: Source code (deleted pre2 from SDK name)

l  Chapter 4.6.2.4:

   Added description for step 2 (**Choose the manifest to repo**)

   Source code

l  Chapter [4.6.2.7.2](#_Modify): Source code of **modify feature** and **modify sub-feature**

l  Chapter [4.6.3](#_Detailed_Configuration): Overall description of order of sub-chapters

l  Chapter [4.7.10](#_Q10._How_to): Website address of Yocto Project

l  Chapter 4.8.1.1: Source code (deleted PRE2 from SDK name)

l  Chapter 4.8.1.2: Source code (deleted PRE2 from SDK name)

l  Chapter [6.1.2](#_Linux_Console_Login): Figure 6.3

l  Chapter [7](#_Toc522636947): Website address of Yocto Project (from [2] to [7])

## Rev. 1.00: 2024-04-30

n  Official version release

 

  

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

**For customers who use licensed Codec ICs and/or licensed codec firmware of mp3:**

“Supply of this product does not convey a license nor imply any right to distribute content created with this product in revenue-generating broadcast systems (terrestrial. Satellite, cable and/or other distribution channels), streaming applications (via internet, intranets and/or other networks), other content distribution systems (pay-audio or audio-on-demand applications and the like) or on physical media (compact discs, digital versatile discs, semiconductor chips, hard drives, memory cards and the like). An independent license for such use is required. For details, please visit [http://mp3licensing.com](http://mp3licensing.com)”.

**For customers who use other firmware of mp3:**

“Supply of this product does not convey a license under the relevant intellectual property of Thomson and/or Fraunhofer Gesellschaft nor imply any right to use this product in any finished end user or ready-to-use final product. An independent license for such use is required. For details, please visit [http://mp3licensing.com](http://mp3licensing.com)”.

**For customers who use Digital Wave DRA solution:**

“Supply of this implementation of DRA technology does not convey a license nor imply any right to this implementation in any finished end-user or ready-to-use terminal product. An independent license for such use is required.”

**For customers who use DTS technology:**

 "This product made under license to certain U.S. patents and/or foreign counterparts."

 "© 1996 – 2011 DTS, Inc. All rights reserved."  

**For customers who use Dolby technology:**

"Supply of this Implementation of Dolby technology does not convey a license nor imply a right under any patent, or any other industrial or intellectual property right of Dolby Laboratories, to use this Implementation in any finished end-user or ready-to-use final product. It is hereby notified that a license for such use is required from Dolby Laboratories."

**For customers who use Google technology:**

 "Copyright © 2013 Google Inc. All rights reserved.”

**For customers who use MS technology:**

"This product is subject to certain intellectual property rights of Microsoft and cannot be used or distributed further without the appropriate license(s) from Microsoft."

---

 [[H김1]](#_msoanchor_1)Board version update 필요

 [[김(K2]](#_msoanchor_2)어떤 의미인가요?

 [[백(B3]](#_msoanchor_3)SOC 에서 정한 D5 의 pin name 입니다.

 [[김(K4]](#_msoanchor_4)Corebsp 적용 이후 이부분 수정되었는지 확인 필요

 [[신(HS5]](#_msoanchor_5)변경 사항없음

 [[김(K6]](#_msoanchor_6)Corebsp 적용 이후 이 부분 수정되었음. 반영 필요.

 [[신(HS7]](#_msoanchor_7)변경사항은 있지만 하위 디렉토리여서 수정 필요하지 않음

 [[김(K8]](#_msoanchor_8)Builtools 와 ADT 내용 재확인 필요함

 [[신(HS9]](#_msoanchor_9)buildtools은 변경사항 없음

ADT 수정 완료

 [[강(K10]](#_msoanchor_10)Pre_유지인지 확인 부탁 드립니다.

 [[H김11]](#_msoanchor_11)네. 유지합니다.

 [[J김12]](#_msoanchor_12)1.0.0 버전을 말하는건가요?

 [[H김13]](#_msoanchor_13)네. 1.0.0 의미합니다.

 [[W김14]](#_msoanchor_14)bootchart Feature 내용 추가.

 [[강(K15]](#_msoanchor_15)10인지 확인 부탁 드립니다.

 [[H김16]](#_msoanchor_16)10 으로 수정

 [[H김17]](#_msoanchor_17)릴리즈시마다 업데이트 하기

 [[김김18]](#_msoanchor_18)최신코드로 업데이트 필요

 [[김김19]](#_msoanchor_19)수정완료

 [[H김20]](#_msoanchor_20)Need update

 [[W김21]](#_msoanchor_21)bootchart Feature 내용 추가.

 [[강(K22]](#_msoanchor_22)

 [[H김23]](#_msoanchor_23)10 으로 수정

 [[W김24]](#_msoanchor_24)bootchart Feature 내용 추가.

 [[강(K25]](#_msoanchor_25)

 [[H김26]](#_msoanchor_26)10 으로 수정

 [[신(HS27]](#_msoanchor_27)최신 정보로 변경 필요

early-camera 삭제 필요

 [[김김28]](#_msoanchor_28)수정완료

 [[J김29]](#_msoanchor_29)한번만 구성해도 된다는 의미인가요? Only once

 [[H김30]](#_msoanchor_30)main core 또는 sub-core 중 한쪽에서만 설정해야 한다는 의미입니다.

main core에서 booting-animation을 사용하겠다고 설정하면 sub-core에서는 설정하면 안된다는 뜻.

 [[김31]](#_msoanchor_31)불필요한 셋팅이라

INVITE_PLATFORM += "gpu-vz"

삭제했습니다.

 [[김32]](#_msoanchor_32)Sub-core Cluster 에 대한 Main-core 연관된 내용에 대해 추가 하였습니다.

검토 부탁 드립니다.

 [[W김33]](#_msoanchor_33)Altia-cluster 관련 내용 추가하였습니다.

검토 부탁 드립니다.

 [[J김34]](#_msoanchor_34)?  tcc70XX를 명시한 이유가 무엇인가요 반드시 여기서만 해당된다는건가요?

 [[H김35]](#_msoanchor_35)네, STR 기능을 사용하려면 VCP도 연결되어야 하기 때문에 추가 작성했습니다.

 [[김(K36]](#_msoanchor_36)공란 유지

 [[W김37]](#_msoanchor_37)SDK 에서 AUO -> BOE panel 변경 설정 내용 추가.

 [[강(K38]](#_msoanchor_38)#LCD_PANEL_TYPE=”AUO”에서 "BOE”로 변경하라는 의미일까요?

 [[H김39]](#_msoanchor_39)이렇게 변경하라는 의미로,

#LCD_PANEL_TYPE = "BOE" -> LCD_PANEL_TYPE = "BOE"

주석표시를 지우라는 뜻입니다.

 [[H김40]](#_msoanchor_40)확인했습니다.

 [[강(K41]](#_msoanchor_41)**각** **코어에서** **각각** 변경하라는 의미인지 확인 부탁 드립니다.

 [[H김42]](#_msoanchor_42)네, 각 코어에서 각각 수정해야한다는 뜻입니다.

 [[W김43]](#_msoanchor_43)Subcore 64 bit memory size 변경 설정 내용 추가.

 [[Y강44]](#_msoanchor_44)It = 메모리 사이즈를 의미하는 것인지 확인 부탁 드립니다.

 [[H김45]](#_msoanchor_45)메모리 사이즈로 설정하는 숫자 (0x20000000)를 의미합니다.

 [[H김46]](#_msoanchor_46)확인했습니다.

 [[강(K47]](#_msoanchor_47)삭제인지 확인 부탁 드립니다.

 [[H김48]](#_msoanchor_48)이 chapter에서는 conf 유지합니다.

 [[강(K49]](#_msoanchor_49)

 [[H김50]](#_msoanchor_50)이 chapter에서는 conf 유지합니다.

 [[강(K51]](#_msoanchor_51)

 [[H김52]](#_msoanchor_52)이 chapter에서는 conf 유지합니다.

 [[김김53]](#_msoanchor_53)Makefile 기반의 프로젝트인 경우 Makefile에서 AR, CC, CXX, LD 변수를 정의하지 마십시오. ADT 빌드 환경에 설정된 값이 Makefile에서 재정의되면 안됩니다.

 [[조(C54]](#_msoanchor_54)문서 전반적으로 emmc와 ufs 모드 설명이 있으므로, USB 인식 부분돠 다르게 설명이 되었으면 합니다.

eMMC의 경우는, "/run/media/sda1/" 이나, UFS의 경우는, "/run/media/sdd1/" 이므로,

SDK에서의 default 설정인 eMMC로 해서 기술을 하고, UFS의 경우에 대해서 추가 명기 필요

 [[김김55]](#_msoanchor_55)Usb 가 연결되었을때 인식되는 경로를 예측하기 어려우므로 (emmc라고 항상 sda1인것도 아니고) 구체적 경로를 삭제하고, 챕터 상단에 경로가 달라진다는 내용을 추가했습니다.

 [[김김56]](#_msoanchor_56)Note 추가한 내용 cross-check 필요.

SDK 가이드대로 빌드하고 있는거면 본 챕터는 안봐도 된다는 얘기를 하고 싶었습니다.

(항상 파일을 수정해서 빌드해야하는것처럼 적혀 있어서)

 [[김57]](#_msoanchor_57) eMMC / UFS 용량 확인 방법 추가

 [[강(K58]](#_msoanchor_58)

 [[H김59]](#_msoanchor_59)conf 유지합니다.

 [[강(K60]](#_msoanchor_60)gpt_partition.list인가요? 확인 부탁 드립니다.

 [[김(K61]](#_msoanchor_61)gpt_partition.list와 다른 partition.list 입니다.

 [[김62]](#_msoanchor_62)Fwdn --sector-size

Mktcimg --sector_size