## 1 Introduction

This document describes Automotive Android SDK (AAS) usage as follows:

- Board Description
- Set up environment (Toolchain)
- Build Guide
- FWDN Guide
- Partition Update
- Fast Cold Boot
- Android Application Guide
- Telechips Application Guide
- Debugging Guides

&nbsp;&nbsp;&nbsp;

## 2 Board Description

### 2.1 EVB Version

**Table 2.1 EVB Version**

| **Board** | **Board Name/Version** |
|:--:|----|
| CPU Board | TCC8030_CPU_LPD4321_V1.2.2 |
| Main Board | TCC803X_MAIN_V1.1.1 |
| Audio, Broadcasting, and Radio Tuner Board (ABRB) | TCC8XXX_AK4601_SILAB_ISDBT_DAB_SV1.0 |
| 12.3" 1920x720 LCD | TCC80XX_BOE_WLCD_12.3_SV1.1.1 |
| Jog Navigation Sub-board | TCC80XX_KEY_SV0.1 |

&nbsp; 

&nbsp; 

#### 2.1.1 CPU Board

**Figure 2.1 TCC8030_CPU_LPD4321_V1.2.2**

![](https://ye-eun-kang.github.io/documentimage/images/TCC803x/SW/Android/12/TCC803x%20Android%2012%20SDK-Getting%20Started/image-20250527134448818.png)

&nbsp; 

&nbsp; 

##### 2.1.2 Main Board

**Figure 2.2 TCC803X_MAIN_V1.1.1**

![](https://ye-eun-kang.github.io/documentimage/images/TCC803x/SW/Android/12/TCC803x%20Android%2012%20SDK-Getting%20Started/image-20250527134601944.png)

&nbsp; 

&nbsp; 

#####  2.1.3 Audio, Broadcasting, and Radio Tuner Board (ABRB)

**Figure 2.3 TCC8XXX_AK4601_SILAB_ISDBT_DAB_SV1.0**

![](https://ye-eun-kang.github.io/documentimage/images/TCC803x/SW/Android/12/TCC803x%20Android%2012%20SDK-Getting%20Started/image-20250527134721516.png)

&nbsp;

**Note:** For this SDK, the AK4601 codec is supported by default. Refer to Table 2.2.

&nbsp;

**Table 2.2 Codec Selection**

| **Category** |                     **Function Switch**                      | **Description** |
| :----------: | :----------------------------------------------------------: | :-------------: |
|  CODEC_SEL   | ![](https://ye-eun-kang.github.io/documentimage/images/TCC803x/SW/Android/12/TCC803x%20Android%2012%20SDK-Getting%20Started/image-20250527134813798.png) |     AK4601      |
|              | ![](https://ye-eun-kang.github.io/documentimage/images/TCC803x/SW/Android/12/TCC803x%20Android%2012%20SDK-Getting%20Started/image-20250527134823042.png) |     TCC7604     |

&nbsp;

&nbsp;

##### 2.1.4 12.3" 1920x720 LCD

**Figure 2.4 TCC80XX_BOE_WLCD_12.3_SV1.1.1**

![](https://ye-eun-kang.github.io/documentimage/images/TCC803x/SW/Android/12/TCC803x%20Android%2012%20SDK-Getting%20Started/image-20250527134914704.png)

&nbsp;

&nbsp;

##### 2.1.5 Jog Navigation Sub-board

**Figure 2.5 TCC80XX_KEY_SV0.1 (Top View)**

![](https://ye-eun-kang.github.io/documentimage/images/TCC803x/SW/Android/12/TCC803x%20Android%2012%20SDK-Getting%20Started/image-20250527134942851.png)

&nbsp;



**Figure 2.6 TCC80XX_KEY_SV0.1 (Bottom View)**

![](https://ye-eun-kang.github.io/documentimage/images/TCC803x/SW/Android/12/TCC803x%20Android%2012%20SDK-Getting%20Started/image-20250527134955525.png)

&nbsp;

&nbsp;

#### 2.2 Boot Mode

##### 2.2.1 USB Boot Mode

**Table 2.3 Set to USB Boot Mode (USB 2.0)**

| **Category** |                   **USB Boot Mode Switch**                   |                        **FWDN Port**                         |
| ------------ | :----------------------------------------------------------: | :----------------------------------------------------------: |
| TCC803x      | ![](https://ye-eun-kang.github.io/documentimage/images/TCC803x/SW/Android/12/TCC803x%20Android%2012%20SDK-Getting%20Started/image-20250527135144435.png) | ![](https://ye-eun-kang.github.io/documentimage/images/TCC803x/SW/Android/12/TCC803x%20Android%2012%20SDK-Getting%20Started/image-20250527135133425.png) |

&nbsp;

&nbsp;

##### 2.2.2 eMMC Boot Mode

Table 2.4 Set to eMMC Boot Mode

| Category |                    eMMC Boot Mode Switch                     |                         Reset Switch                         |                            Note                             |
| :------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :---------------------------------------------------------: |
| TCC803x  | ![](https://ye-eun-kang.github.io/documentimage/images/TCC803x/SW/Android/12/TCC803x%20Android%2012%20SDK-Getting%20Started/image-20250527135256948.png) | ![](https://ye-eun-kang.github.io/documentimage/images/TCC803x/SW/Android/12/TCC803x%20Android%2012%20SDK-Getting%20Started/image-20250527135254175.png) | The reset button is on the bottom left corner of the board. |

&nbsp;

&nbsp;

##### 2.2.3 SNOR/eMMC Boot Mode

**Table 2.5 Set to SNOR/eMMC Boot Mode**

| **Category** | **SNOR/eMMC Boot Mode Switch**                               | **Reset Switch**                                             | **Note**                                                     |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| TCC803x      | ![](https://ye-eun-kang.github.io/documentimage/images/TCC803x/SW/Android/12/TCC803x%20Android%2012%20SDK-Getting%20Started/image-20250527135356911.png) | ![](https://ye-eun-kang.github.io/documentimage/images/TCC803x/SW/Android/12/TCC803x%20Android%2012%20SDK-Getting%20Started/image-20250527135400032.png) | The  reset button is on the bottom left corner of the board. |

&nbsp;

&nbsp;

## 3 Set Up Environment

This chapter describes how to set up the environment to build the Android source files.

> [!IMPORTANT]
>
> You must use Linux because building on Windows is currently not supported.
>

&nbsp;

### 3.1 Set Up Linux Host Machine

#### 3.1.1 Hardware Requirements

Your development host machine should meet the following hardware requirements:

- 64-bit environment

- At least 250 GB of free disk space to check out the code and an extra 150 GB to build the code  
  (If you conduct multiple builds, you will need even more space.)

- At least 16 GB of RAM (only if you run Linux in a virtual machine)

&nbsp;

&nbsp;

#### 3.1.2 Software Requirements

##### 3.1.2.1 Install Required Packages

To set up the build environment recommended by google, refer to [https://source.android.com/docs/setup/start/initializing](https://source.android.com/docs/setup/start/initializing).

If you want to set up a build environment tested by Telechips, see the followings:

- **Ubuntu 20.04**
  - Required packages


```
apt install -y net-tools make build-essential cmake gcc g++ perl openjdk-11-jdk ncftp chrony diffstat ctags

apt install -y git gnupg flex bison zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev libc6-dev-i386 lib32ncurses-dev x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig sqlite libffi-dev libbz2-dev libreadline-dev libsqlite3-dev libssl-dev lzop dos2unix python2 python-dev python3-dev libncurses5 xz-utils tk-dev manpages-dev bzip2 device-tree-compiler libspiro-dev p7zip
apt install -y gawk wget texinfo chrpath socat cpio python3 python3-pip python3-pexpect debianutils iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint3 xterm python3-subunit mesa-common-dev
apt install -y libncurses* subversion automake
apt install -y zstd
apt install -y git
```

&nbsp;

- **Fedora 20**
  - Required packages


```
yum -y install glibc*
yum -y install glibc-devel*
yum -y install libstdc++*
yum -y install libstdc++-devel*
yum -y install python-devel
yum -y install perl-XML-Xerces.x86_64*
yum -y install aalib-libs*
yum -y install antlr-javadoc*
yum -y install baekmuk-bdf-fonts*
yum -y install baekmuk-ttf-fonts-batang*
yum -y install baekmuk-ttf-fonts-dotum*
yum -y install baekmuk-ttf-fonts-gulim*
yum -y install baekmuk-ttf-fonts-hline*
yum -y install createrepo*
yum -y install deltarpm*
yum -y install docbook-utils-pdf*
yum -y install fonts-ISO8859*
yum -y install gitk*
yum -y install global*
yum -y install graphviz*
yum -y install gtksourceview2*
yum -y install gupnp-devel*
yum -y install gypsy-devel*
yum -y install jakarta-commons-beanutils-javadoc*
yum -y install libdiscid*
yum -y install libogg-devel*
yum -y install libspiro*
yum -y install libssh2-devel*
yum -y install libuser-devel*
yum -y install libX11*
yum -y install libXrandr*
yum -y install man-pages-ko*
yum -y install meld*
yum -y install monodoc*
yum -y install ncurses-devel*
yum -y install perl-devel*
yum -y install perl-ExtUtils-MakeMaker*
yum -y install rapidsvn*
yum -y install SDL-devel*
yum -y install sos*
yum -y install system-config-date*
yum -y install system-config-httpd*
yum -y install vim-X11*
yum -y install w3m*
yum -y install wxBase*
yum -y install wxGTK*
yum -y install dx*
yum -y install xfsprogs*
yum -y install xorg-x11-fonts-ISO8859*
yum -y install xorg-x11-fonts-misc*
yum -y install xz-lzma-compat*
yum -y install readline*
yum -y install libX11-devel*
yum -y install glibc-devel*
yum -y install readline-devel*
yum -y install acpi*
yum -y install libx86*
yum -y install libssl*
yum -y install hdparm*
yum -y install gucharmap*
yum -y install libX11*
yum -y install libX11-devel*
yum -y install x11-ssh-askpass*
yum -y install libX11-devel*
yum -y install libX11.x86_64*
yum -y install python
yum -y install bleachbit.noarch*
yum -y install libstdc++.i686*
yum -y install zlib.i686*
yum -y install zlib-devel.i686*
yum -y install python-devel.i686*
yum -y install xerces-c-devel.i686*
yum -y install readline.i686*
yum -y install libX11-devel.i686*
yum -y install glibc-devel.i686*
yum -y install readline-devel.i686*
yum -y install libx86.i686*
yum -y install libX11.i686*
yum -y install libX11-devel.i686*
yum -y install libX11.i686*
yum -y install libX11-devel.i686*
yum -y install libXrender.i686*
yum -y install vim-X11.x86_64*
yum -y install gperf
yum -y install perl-Switch.noarch
yum -y install libmp*
yum -y install tmux
yum -y install java-1.8.0-openjdk*
yum -y install vim
yum -y install sysstat
yum -y install zlib-devel
yum -y install openldap-clients nss-pam-ldapd
yum -y install java-1.8.0-openjdk*
yum -y install bison
yum -y install flex

```

&nbsp;

- **Fedora 20**
  - GCC upgrade (v5.3.1)


```
yum install gcc-c++ --nogpgcheck --releasever=23
yum install libgcc-5.3.1-6.fc23.i686 --nogpgcheck --releasever=23
```

&nbsp;

**Note 1:** For the details on the required packages for Linux Host Machine to build sub-core, refer to Chapter 4.4.3 List of Packages Required for Host Development System to Use Yocto Project in *“TCC805x Linux SDK-Getting Started”*. \[6\]

**Note 2:** Required packages to be installed may be different depending on the version of Ubuntu and Fedora. If the build does not work, the required package may not be installed.

&nbsp;

&nbsp;

##### 3.1.2.2 Toolchain Path

**<u>Bootloader</u>**

This Android SDK uses U-Boot as the bootloader. Refer to Chapter 4.1.2.2.1 Set Configuration of Toolchain for U-Boot.

&nbsp;

**<u>Kernel</u>**

Refer to Chapter 4.1.2.4.2 Kernel Configuration for Toolchain of Kernel.

&nbsp;

&nbsp;

#### 3.1.3 Telechips Test Environment 

- Tested on Fedora

  - Fedora 20 (Linux-3.19.8-100.fc20.x86_64-x86_64++debug)


  - GNU Make 3.82 or higher


  - Python 2.7.5


  - Git 2.25.1 or higher


  - OpenJDK 9 or higher


&nbsp;

- Tested on Ubuntu

  - Ubuntu 20.04.5-LTS


  - GNU Make 3.82 or higher


  - Python 2.7.18


  - Git 2.25.1 or higher


  - OpenJDK 9 or higher

  &nbsp;

  &nbsp;

  

## 4 Build Guide

### 4.1 TCC803x EVB (64-bit SDK)

#### 4.1.1 Download SDK

Download SDK **TCC803x_Android12_IVI_1.0.0** from the Telechips Android Git server.

```
$ mkdir mydroid
$ cd mydroid


$ repo init -u ssh://android.telechips.com/android_avn/android/platform/manifest.git -b TCC803x_Android12_IVI_1.0.0
$ repo sync

```

&nbsp;

**Note:** It is recommended to use the **c** option for repo sync to reduce the time for downloading SDK.

The **c** option means that only the source of the revision branch specified in the manifest file is synchronized. (Usage: **`repo sync -c -j8`**)

To reduce the downloading time and SDK size, **`clone-depth = "1"`** for a specific AOSP git in the manifest file is specified as follows. The manifest file, “default.xml”, is in the “.repo/manifests” path.

![](https://ye-eun-kang.github.io/documentimage/images/TCC803x/SW/Android/12/TCC803x%20Android%2012%20SDK-Getting%20Started/image-20250527142018329.png)

The **`clone-depth`** option means that a shallow clone is created with a history truncated to the number of commits specified by **`depth`** option.

However, the shallow clone cannot be pushed to the server. If you need to push all the sources to the server or push the commit, you should use the following command. You can get all commit history for the shallow clone by using the following command.

&nbsp;

**Note:** You can check the remote-name of the specific git by using the **`git remote -v`** command.

```
$ git fetch --unshallow [remote-name]
```

To apply the **`git fetch`** command above to all gits with clone-depth in the SDK, you should use the following command.

```
$ repo forall -c "git fetch --unshallow [remote-name]"
```

&nbsp;

&nbsp;

#### 4.1.2 Compile and Build Android Framework

##### 4.1.2.1 Set Up Compiling Environment

**`TARGET_PRODUCT`** must be set correctly for board configuration before compiling.

Execute the following commands.

&nbsp;

**Note:** **`.`** **`build/envsetup.sh`** is used to execute the shell scripter. There should be a space between dot (`.`) and **`build/envsetup.sh`**.

```
$ cd ~/mydroid/maincore
$ . build/envsetup.sh

$ lunch

You're building on Linux

Lunch menu... pick a combo:
     1. aosp_arm-eng
     2. aosp_arm64-eng
     3. aosp_barbet-userdebug
     4. aosp_blueline-userdebug
     5. aosp_blueline_car-userdebug
     6. aosp_bonito-userdebug
     7. aosp_bonito_car-userdebug
     8. aosp_bramble-userdebug
     9. aosp_bramble_car-userdebug
     10. aosp_car_arm-userdebug
     11. aosp_car_arm64-userdebug
     12. aosp_car_x86-userdebug
     13. aosp_car_x86_64-userdebug
     14. aosp_cf_arm64_auto-userdebug
     15. aosp_cf_arm64_phone-userdebug
     16. aosp_cf_x86_64_foldable-userdebug
     17. aosp_cf_x86_64_pc-userdebug
     18. aosp_cf_x86_64_phone-userdebug
     19. aosp_cf_x86_64_tv-userdebug
     20. aosp_cf_x86_auto-userdebug
     21. aosp_cf_x86_phone-userdebug
     22. aosp_cf_x86_tv-userdebug
     23. aosp_coral-userdebug
     24. aosp_coral_car-userdebug
     25. aosp_crosshatch-userdebug
     26. aosp_crosshatch_car-userdebug
     27. aosp_crosshatch_vf-userdebug
     28. aosp_flame-userdebug
     29. aosp_flame_car-userdebug
     30. aosp_redfin-userdebug
     31. aosp_redfin_car-userdebug
     32. aosp_redfin_vf-userdebug
     33. aosp_sargo-userdebug
     34. aosp_sargo_car-userdebug
     35. aosp_sunfish-userdebug
     36. aosp_sunfish_car-userdebug
     37. aosp_trout_arm64-userdebug
     38. aosp_trout_x86-userdebug
     39. aosp_x86-eng
     40. aosp_x86_64-eng
     41. arm_krait-eng
     42. arm_v7_v8-eng
     43. armv8-eng
     44. armv8_cortex_a55-eng
     45. armv8_kryo385-eng
     46. beagle_x15-userdebug
     47. beagle_x15_auto-userdebug
     48. car_tcc803x_arm64-eng
     49. car_x86_64-userdebug
     50. db845c-userdebug
     51. fuchsia_arm64-eng
     52. fuchsia_x86_64-eng
     53. gsi_car_arm64-userdebug
     54. gsi_car_x86_64-userdebug
     55. hikey-userdebug
     56. hikey64_only-userdebug
     57. hikey960-userdebug
     58. hikey960_tv-userdebug
     59. hikey_tv-userdebug
     60. pixel3_mainline-userdebug
     61. poplar-eng
     62. poplar-user
     63. poplar-userdebug
     64. qemu_trusty_arm64-userdebug
     65. sdk_car_arm-userdebug
     66. sdk_car_arm64-userdebug
     67. sdk_car_x86-userdebug
     68. sdk_car_x86_64-userdebug
     69. silvermont-eng
     70. uml-userdebug
     71. yukawa-userdebug
     72. yukawa_sei510-userdebug

Which would you like? [aosp_arm-eng] 48
[W][2024-07-09T15:58:10+0900][1] bool caps::initNs(nsjconf_t *)():215 prctl(PR_CAP_AMBIENT, PR_CAP_AMBIENT_CLEAR_ALL): Invalid argument
[W][2024-07-09T15:58:12+0900][1] bool caps::initNs(nsjconf_t *)():215 prctl(PR_CAP_AMBIENT, PR_CAP_AMBIENT_CLEAR_ALL): Invalid argument
device/telechips/car_tcc803x_arm64/device.mk:711: warning: BOARD_PLAT_PRIVATE_SEPOLICY_DIR has been deprecated. Use SYSTEM_EXT_PRIVATE_SEPOLICY_DIRS instead.
Updated 131 paths from the index

============================================
PLATFORM_VERSION_CODENAME=REL
PLATFORM_VERSION=12
TARGET_PRODUCT=car_tcc803x_arm64
TARGET_BUILD_VARIANT=eng
TARGET_BUILD_TYPE=release
TARGET_ARCH=arm64
TARGET_ARCH_VARIANT=armv8-a
TARGET_CPU_VARIANT=cortex-a72
TARGET_2ND_ARCH=arm
TARGET_2ND_ARCH_VARIANT=armv8-a
TARGET_2ND_CPU_VARIANT=cortex-a53
HOST_ARCH=x86_64
HOST_2ND_ARCH=x86
HOST_OS=linux
HOST_OS_EXTRA=Linux-3.19.8-100.fc20.x86_64-x86_64-Fedora-20-(Heisenbug)
HOST_CROSS_OS=windows
HOST_CROSS_ARCH=x86
HOST_CROSS_2ND_ARCH=x86_64
HOST_BUILD_TYPE=release
BUILD_ID=RT12.230114.001.A1
OUT_DIR=out
============================================

```

&nbsp;

**Note:** If you want to set **user** mode, use the **choosevariant** command.

&nbsp;

&nbsp;

##### 4.1.2.2 Compile Bootloader

You must compile bootloader and kernel first and then frameworks respectively.

- Bootloader path: ~/mydroid/maincore/bootable/bootloader/u-boot

&nbsp;

##### 4.1.2.2.1 Set Configuration of Toolchain for U-Boot

Before building the bootloader, you should download toolchain from the following website:

- [https://developer.arm.com/downloads/-/gnu-a](https://developer.arm.com/downloads/-/gnu-a)

&nbsp;

**Note**: The link is subject to change without notice.

The information of the toolchain to compile U-Boot is **`gcc-arm-9.2-2019.12-x86_64-aarch64-none-linux-gnu.tar.xz`** and **`gcc-arm-9.2-2019.12-x86_64-arm-none-linux-gnueabihf.tar.xz`**.

You can build the bootloader after setting all prerequisites. If you select a configuration according to the CPU board, it will be set accordingly.

Set toolchain path and configuration of U-Boot as follows.

```
$ cd gcc-arm-9.2-2019.12-x86_64-arm-none-linux-gnueabihf/bin
$ export PATH=$PWD:$PATH
$ cd gcc-arm-9.2-2019.12-x86_64-aarch64-none-linux-gnu/bin
$ export PATH=$PWD:$PATH
$ echo $PATH  // you can check toolchain path is applied in $PATH$ cd ~/mydroid/maincorebootable/bootloader/u-boot
$ cd ~/mydroid/maincore/bootable/bootloader/u-boot 
$ source scripts/envsetup.sh

[1] Telechips Android Platform
[2] Telechips Android Platform (64bit)
[3] Telechips Linux Platform
[4] Telechips Linux Platform (64bit)
Select platform (default 4): 2

[1] TCC805x
[2] TCC803x
Select SoC family (default 1): 2

[1] TCC803XP EVB 1.0
[2] TCC8030 EVB 0.1
Select board (default 1): 2

[1] Maincore
Select core (default 1): 1

### U-Boot Environment Setup Complete ###

- ARCH=arm64
- CROSS_COMPILE=aarch64-none-linux-gnu-
- DEVICE_TREE=tcc8030-evb_sv0.1

```

&nbsp;

&nbsp;

##### 4.1.2.2.2 Build U-Boot and Make ROM File

To build the bootloader (U-Boot) for EVB of 64-bit SDK, use the following default configuration files and execute the **make** command depending on the chipset.

```
$  make tcc803x_android_12_defconfig       
```

&nbsp; 

**Note:** If you want to configure the boot mode to **single** mode, remove the build option as follows:

 &nbsp;

1. Run **make menuconfig** command and remove the configuration as follows.

```
 $ make menuconfig  ARM  architecture --->  Telechips  architecture specifics --->  [  ] Boot subcore kernel by maincore       
```

&nbsp;

2. Compile the code, and you will find the “u-boot.rom” file in ~mydroid/maincore/bootable/bootloader/u-boot.

```
 $ make -j8     
```

 &nbsp;

 &nbsp;

##### 4.1.2.3 Generic Kernel Image (GKI)

Information about the Generic Kernel Image (GKI) project by Google can be found at the following website:

- [https://source.android.com/docs/core/architecture/kernel/generic-kernel-image](https://source.android.com/docs/core/architecture/kernel/generic-kernel-image)

&nbsp;

&nbsp;

#### Compile Linux Kernel

The top layer of the SDK tree consists of the following components:

- Kernel

- Maincore

- Subcore

If you modify the kernel code, you must compile the GKI image, “boot.img” and “vendor_boot.img”, because the output file (“.ko”) of the kernel device is included in the “vendor_boot.img”.

Information about the vendor_boot partition can be found at the following website:

- [https://source.android.com/docs/core/architecture/partitions/vendor-boot-partitions](https://source.android.com/docs/core/architecture/partitions/vendor-boot-partitions)

&nbsp;

##### 4.1.2.4.1 Kernel Configuration – Device Tree

The board configuration files are all in “kernel/common/arch/arm64/boot/dts” path**.** The “.dts” file includes a specific configuration depending on the LCD panel.

Also, detailed configuration files are listed in the “kernel/common/arch/arm64/boot/dts/tcc” path**.**

- For TCC803x, “tcc803x-android-lpd4321_sv1.0.dts” and “tcc803x-android-ivi.dtsi” are used for kernel device configuration. After compiling the kernel, these dt-files produce binaries named “tcc803x-android-lpd4321_sv1.0.dtb” in the following two paths:

  - kernel/out_abi/android12-5.4/common/arch/arm64/boot/dts/tcc


  - maincore/out/target/product/car_tcc803x_arm64


&nbsp;

##### 4.1.2.4.2 Kernel Configuration

Before building the kernel, you should download the toolchain from the following:

- [https://releases.linaro.org/components/toolchain/binaries/7.2-2017.11/aarch64-linux-gnu/](https://releases.linaro.org/components/toolchain/binaries/7.2-2017.11/aarch64-linux-gnu/)

The information of toolchain for compiling kernel is **gcc-linaro-7.2.1-2017.11-x86_64_aarch64-linux-gnu.tar.xz**. And you should set up your environment as follows.

The path where the toolchain is installed should be set in **PATH**. The following is an example.

```
Example)
$ export  PATH=/opt/gcc-linaro-7.2.1-2017.11-x86_64_aarch64-linux-gnu/bin:$PATH     
```

To set the GKI kernel configuration, use the following default configuration file located in **“**kernel/common/arch/arm64/configs/” path.

- gki_defconfig

&nbsp;

> [!IMPORTANT]
>
> “gki_defconfig” is a config defined by Google and must not be modified or deleted.
>

&nbsp;

To set the telechips kernel configuration, use the following fragment files located in “kernel/common/arch/arm64/configs/” path.

- TCC803x: “telechips_gki_tcc803x.fragment”

By compiling “gki_defconfig” and “telechips_gki_tcc803xpe.fragment", “.config" is created and this file will be located in the “kernel/out_abi/android12-5.10/common/” path. Refer to Chapter 4.1.2.4.3.

To build the GKI kernel and enable automatic copying of the output after building the GKI kernel, you must set the path to “maincore/device/telechips/car_tcc803x-kernel”. If the output is not copied, you will be unable to build the Android 12 SDK.

```
$ cd ~/mydroid/maincore
$ cd device/telechips/car_tcc803x-kernel

$ sdk_dir=$PWD
$ croot
$ cd ../kernel
$ export ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- LLVM=1
```

&nbsp;

&nbsp;

##### 4.1.2.4.3 Compile Kernel

Execute **build_abi.sh** in the kernel directory. (file path: kernel/build/build_abi.sh)

&nbsp;

&nbsp;

# References

1.  Contact Telechips for more details: [sales@telechips.com](mailto:sales@telechips.com)

2.  For more information about ADB: [https://developer.android.com/studio/releases/platform-tools](https://developer.android.com/studio/releases/platform-tools)

3.  For ADB Command: [https://developer.android.com/studio/command-line/adb](https://developer.android.com/studio/command-line/adb)

4.  For more information about Toolchain: [https://developer.android.com/ndk/guides/build](https://developer.android.com/ndk/guides/build)

5.  TC Common-User Guide for mktcimg

TCCxxxx Common-User Guide for Firmware Downloader V8

6.  TCC805x Linux SDK-Getting Started

7.  TCCxxxx Android 12 SDK-Reference Manual for Supported Media Format

8.  TCCxxxx Android SDK-User Guide for Dynamic Partitions

**Note**: Reference documents can be provided whenever available, depending on the terms of a contract. If the reference documents are unavailable, the contents directly related to your development can be guided.

&nbsp;

&nbsp;

## Revision History

### Rev. 1.00: 2024-07-30

- Official version release

&nbsp;

&nbsp;



##### DISCLAIMER

This material is being made available solely for your internal use with its products and service offerings of Telechips, Inc (“Telechips”). and/or licensors and shall not be used for any other purposes. This material may not be altered, edited, or modified in any way without Telechips’ prior written approval. Unauthorized use or disclosure of this material or the information contained herein is strictly prohibited, and you agree to indemnify Telechips and licensors for any damages or losses suffered by Telechips and/or licensors for any unauthorized uses or disclosures of this material, in whole or part. Further, Telechips, Inc. reserves the right to revise this material and to make changes to its content, at any time, without obligation to notify any person or entity of such revisions or changes.

THIS MATERIAL IS BEING PROVIDED “AS IS” WITHOUT WARRANTY OF ANY KIND, WHETHER EXPRESSED, IMPLIED, STATUTORY OR OTHERWISE. TO THE MAXIMUM EXTENT PERMITTED BY LAW, TELECHIPS AND/OR LICENSORS SPECIFICALLY DISCLAIM ALL WARRANTIES OF TITLE, MERCHANTABILITY, NON-INFRINGEMENT, FITNESS FOR A PARTICULAR PURPOSE, SATISFACTORY QUALITY, COMPLETENESS OR ACCURACY, AND ALL WARRANTIES ARISING OUT OF TRADE USAGE OR OUT OF A COURSE OF DEALING OR COURSE OF PERFORMANCE. MOREOVER, NEITHER TELECHIPS, INC. NOR LICENSORS, SHALL BE LIABLE TO YOU OR ANY THIRD PARTY FOR ANY EXPENSES, LOSSES, USE, OR ACTIONS HOWSOEVER INCURRED OR UNDERTAKEN BY YOU IN RELIANCE ON THIS MATERIAL.

THIS MATERIAL IS DESIGNED FOR GENERAL PURPOSE, AND ACCORDINGLY YOU ARE RESPONSIBLE FOR ALL OR ANY OF INTELLECTUAL PROPERTY LICENSES REQUIRED FOR ACTUAL APPLICATION. TELECHIPS, INC. DOES NOT PROVIDE ANY INDEMNIFICATION FOR ANY INTELLECTUAL PROPERTIES OWNED BY THIRD PARTY.

Copyright Statement

Copyright in this material provided by Telechips, Inc. is owned by Telechips unless otherwise noted. For reproduction or use of Telechips’ copyright material, prior written consent should be obtained from Telechips. That prior written consent, if given, will be subject to conditions that Telechips’ name should be included and interest in the material should be acknowledged when the material is reproduced or quoted, either in whole or in part. You must not copy, adapt, publish, distribute, or commercialize any contents contained in the material in any manner without the written permission of Telechips. Trademarks used in Telechips’ copyright material are the property of Telechips.

***For customers who use Google technology:***

 "Copyright © 2013 Google Inc. All rights reserved.”