# Introduction

This document provides the DC and AC specifications of the Power Delivery Network (PDN) for the target board.
The DC PDN specification is defined by the DC resistance, which is the PDN impedance at zero frequency.
The AC PDN specification is defined by the target impedance, which is the maximum allowable PDN impedance in the specific frequency range. the PDN of the board does not affect the PDN impedance above 100 MHz so the relevant frequency range is 1–100 MHz.
Figure 1.1 shows a graph of the typical PDN specification and the board’s impedance profile.

![image.png](attachment:703eeee7-ab33-46a8-b3e7-d77d430e6b7b:image.png)

| Power Supply Rails         | Power Domains of TCC807x            |
|:----------------------------|:------------------------------------|
| CORE_0P75                   | VDD075D_CORE <br/> VDD075D_DDI       |
| CPUMC_0P95_1CPU Power 1     | VDD095D_CPUMC_76_CORE0-1            |
| CPUMC_0P95_2CPU Power 2     | VDD095D_CPUMC_76_CORE2-3            |
| CPUMC_0P95_3CPU Power 3     | VDD095D_CPUMC_55_CORE0-3            |
| CPUSC_0P95CPU Power 4       | VDD095D_CPUMC_WRAP <br/> VDD095D_CPUSC_55_CORE0-1 <br/> VDD095D_CPUSC_WRAP |
| NPU_0P85NPU Power           | VDD085D_NPU                        |
| IP_0P85DDR Controller Power | VDD085D_DDR0-1                     |
| GB_0P75Video Power 1        | VDD075D_GPU                        |
| TC_VB_0P95Video Power 2     | VDD095D_VPU                        |
