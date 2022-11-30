EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 2 2
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Device:R R3
U 1 1 617CFAA7
P 2750 1400
F 0 "R3" H 2820 1446 50  0000 L CNN
F 1 "100" H 2820 1355 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 2680 1400 50  0001 C CNN
F 3 "~" H 2750 1400 50  0001 C CNN
	1    2750 1400
	1    0    0    -1  
$EndComp
$Comp
L Device:R R2
U 1 1 617CFE39
P 2750 1800
F 0 "R2" H 2820 1846 50  0000 L CNN
F 1 "4.7k" H 2820 1755 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 2680 1800 50  0001 C CNN
F 3 "~" H 2750 1800 50  0001 C CNN
	1    2750 1800
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 617D03A7
P 2450 2050
F 0 "R1" V 2243 2050 50  0000 C CNN
F 1 "470k" V 2334 2050 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 2380 2050 50  0001 C CNN
F 3 "~" H 2450 2050 50  0001 C CNN
	1    2450 2050
	0    1    1    0   
$EndComp
$Comp
L Device:R R4
U 1 1 617D09C7
P 3500 2350
F 0 "R4" H 3570 2396 50  0000 L CNN
F 1 "100k" H 3570 2305 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 3430 2350 50  0001 C CNN
F 3 "~" H 3500 2350 50  0001 C CNN
	1    3500 2350
	1    0    0    -1  
$EndComp
$Comp
L Device:Q_NPN_EBC Q1
U 1 1 617D2176
P 2650 2350
F 0 "Q1" H 2840 2396 50  0000 L CNN
F 1 "KT3102E" H 2840 2305 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92L_Wide" H 2850 2450 50  0001 C CNN
F 3 "~" H 2650 2350 50  0001 C CNN
	1    2650 2350
	1    0    0    -1  
$EndComp
$Comp
L Device:CP1_Small C1
U 1 1 617D29CB
P 2000 2350
F 0 "C1" V 1772 2350 50  0000 C CNN
F 1 "10u" V 1863 2350 50  0000 C CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.80mm" H 2000 2350 50  0001 C CNN
F 3 "~" H 2000 2350 50  0001 C CNN
	1    2000 2350
	0    1    1    0   
$EndComp
$Comp
L Device:CP1_Small C3
U 1 1 617D3312
P 3150 2050
F 0 "C3" V 3378 2050 50  0000 C CNN
F 1 "10u" V 3287 2050 50  0000 C CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.80mm" H 3150 2050 50  0001 C CNN
F 3 "~" H 3150 2050 50  0001 C CNN
	1    3150 2050
	0    -1   -1   0   
$EndComp
$Comp
L Device:CP1_Small C2
U 1 1 617D429A
P 3150 1600
F 0 "C2" V 3378 1600 50  0000 C CNN
F 1 "100u" V 3287 1600 50  0000 C CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.80mm" H 3150 1600 50  0001 C CNN
F 3 "~" H 3150 1600 50  0001 C CNN
	1    3150 1600
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0112
U 1 1 617D4994
P 2750 2800
F 0 "#PWR0112" H 2750 2550 50  0001 C CNN
F 1 "GND" H 2755 2627 50  0000 C CNN
F 2 "" H 2750 2800 50  0001 C CNN
F 3 "" H 2750 2800 50  0001 C CNN
	1    2750 2800
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0113
U 1 1 617D4E96
P 3600 1600
F 0 "#PWR0113" H 3600 1350 50  0001 C CNN
F 1 "GND" H 3605 1427 50  0000 C CNN
F 2 "" H 3600 1600 50  0001 C CNN
F 3 "" H 3600 1600 50  0001 C CNN
	1    3600 1600
	1    0    0    -1  
$EndComp
$Comp
L power:+9V #PWR0114
U 1 1 617D5551
P 2750 1150
F 0 "#PWR0114" H 2750 1000 50  0001 C CNN
F 1 "+9V" H 2765 1323 50  0000 C CNN
F 2 "" H 2750 1150 50  0001 C CNN
F 3 "" H 2750 1150 50  0001 C CNN
	1    2750 1150
	1    0    0    -1  
$EndComp
Wire Wire Line
	2750 2150 2750 2050
Wire Wire Line
	2600 2050 2750 2050
Connection ~ 2750 2050
Wire Wire Line
	2750 2050 2750 1950
Wire Wire Line
	3050 2050 2750 2050
Wire Wire Line
	3050 1600 2750 1600
Wire Wire Line
	2750 1600 2750 1650
Wire Wire Line
	2750 1550 2750 1600
Connection ~ 2750 1600
Wire Wire Line
	2750 1250 2750 1150
Wire Wire Line
	3250 1600 3600 1600
Wire Wire Line
	2300 2050 2300 2350
Wire Wire Line
	2100 2350 2300 2350
Connection ~ 2300 2350
Wire Wire Line
	2300 2350 2450 2350
$Comp
L Device:R R13
U 1 1 617D9E8C
P 5600 1750
F 0 "R13" H 5670 1796 50  0000 L CNN
F 1 "5.1k" H 5670 1705 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 5530 1750 50  0001 C CNN
F 3 "~" H 5600 1750 50  0001 C CNN
	1    5600 1750
	1    0    0    -1  
$EndComp
$Comp
L Device:CP1_Small C6
U 1 1 617DA796
P 5600 2000
F 0 "C6" H 5691 2046 50  0000 L CNN
F 1 "100u" H 5691 1955 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.80mm" H 5600 2000 50  0001 C CNN
F 3 "~" H 5600 2000 50  0001 C CNN
	1    5600 2000
	1    0    0    -1  
$EndComp
$Comp
L Device:R R9
U 1 1 617DB2E3
P 5300 1550
F 0 "R9" H 5370 1596 50  0000 L CNN
F 1 "10k" H 5370 1505 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 5230 1550 50  0001 C CNN
F 3 "~" H 5300 1550 50  0001 C CNN
	1    5300 1550
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0115
U 1 1 617DB6D7
P 5300 1750
F 0 "#PWR0115" H 5300 1500 50  0001 C CNN
F 1 "GND" H 5305 1577 50  0000 C CNN
F 2 "" H 5300 1750 50  0001 C CNN
F 3 "" H 5300 1750 50  0001 C CNN
	1    5300 1750
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0116
U 1 1 617DBB28
P 5600 2100
F 0 "#PWR0116" H 5600 1850 50  0001 C CNN
F 1 "GND" H 5605 1927 50  0001 C CNN
F 2 "" H 5600 2100 50  0001 C CNN
F 3 "" H 5600 2100 50  0001 C CNN
	1    5600 2100
	1    0    0    -1  
$EndComp
$Comp
L Device:R_POT_Dual_Separate RV5
U 1 1 617DC534
P 4950 1400
F 0 "RV5" H 4881 1446 50  0000 R CNN
F 1 "47k" H 4881 1355 50  0000 R CNN
F 2 "" H 4950 1400 50  0001 C CNN
F 3 "~" H 4950 1400 50  0001 C CNN
	1    4950 1400
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0117
U 1 1 617DD8A6
P 4950 1600
F 0 "#PWR0117" H 4950 1350 50  0001 C CNN
F 1 "GND" H 4955 1427 50  0000 C CNN
F 2 "" H 4950 1600 50  0001 C CNN
F 3 "" H 4950 1600 50  0001 C CNN
	1    4950 1600
	1    0    0    -1  
$EndComp
$Comp
L Device:CP1_Small C11
U 1 1 617DDCE3
P 6700 1500
F 0 "C11" V 6928 1500 50  0000 C CNN
F 1 "100u" V 6837 1500 50  0000 C CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.80mm" H 6700 1500 50  0001 C CNN
F 3 "~" H 6700 1500 50  0001 C CNN
	1    6700 1500
	0    -1   -1   0   
$EndComp
$Comp
L Device:C_Small C12
U 1 1 617DEE03
P 7050 1700
F 0 "C12" H 7142 1746 50  0000 L CNN
F 1 "0.1u" H 7142 1655 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric" H 7050 1700 50  0001 C CNN
F 3 "~" H 7050 1700 50  0001 C CNN
	1    7050 1700
	1    0    0    -1  
$EndComp
$Comp
L Device:R R17
U 1 1 617DF4AB
P 7050 1950
F 0 "R17" H 7120 1996 50  0000 L CNN
F 1 "4.7" H 7120 1905 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric" V 6980 1950 50  0001 C CNN
F 3 "~" H 7050 1950 50  0001 C CNN
	1    7050 1950
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0118
U 1 1 617DFA77
P 7050 2100
F 0 "#PWR0118" H 7050 1850 50  0001 C CNN
F 1 "GND" H 7055 1927 50  0000 C CNN
F 2 "" H 7050 2100 50  0001 C CNN
F 3 "" H 7050 2100 50  0001 C CNN
	1    7050 2100
	1    0    0    -1  
$EndComp
Wire Wire Line
	4950 1550 4950 1600
Wire Wire Line
	5100 1400 5300 1400
Wire Wire Line
	5800 1400 5300 1400
Connection ~ 5300 1400
Wire Wire Line
	5300 1700 5300 1750
Wire Wire Line
	6400 1500 6600 1500
Wire Wire Line
	6800 1500 7050 1500
Wire Wire Line
	7050 1500 7050 1600
$Comp
L tda:TDA2822 U1
U 1 1 617E6652
P 6100 1500
F 0 "U1" H 6100 1867 50  0000 C CNN
F 1 "TDA2822" H 6100 1776 50  0000 C CNN
F 2 "Package_SO:SO-8_3.9x4.9mm_P1.27mm" H 6100 1500 50  0001 C CIN
F 3 "https://www.nxp.com/docs/en/data-sheet/TDA1308.pdf" H 6100 1500 50  0001 C CNN
	1    6100 1500
	1    0    0    -1  
$EndComp
$Comp
L Device:R R14
U 1 1 617E8190
P 5600 2750
F 0 "R14" H 5670 2796 50  0000 L CNN
F 1 "5.1k" H 5670 2705 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 5530 2750 50  0001 C CNN
F 3 "~" H 5600 2750 50  0001 C CNN
	1    5600 2750
	1    0    0    -1  
$EndComp
$Comp
L Device:CP1_Small C7
U 1 1 617E81A6
P 5600 3000
F 0 "C7" H 5691 3046 50  0000 L CNN
F 1 "100u" H 5691 2955 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.80mm" H 5600 3000 50  0001 C CNN
F 3 "~" H 5600 3000 50  0001 C CNN
	1    5600 3000
	1    0    0    -1  
$EndComp
$Comp
L Device:R R10
U 1 1 617E81C4
P 5300 2550
F 0 "R10" H 5370 2596 50  0000 L CNN
F 1 "10k" H 5370 2505 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 5230 2550 50  0001 C CNN
F 3 "~" H 5300 2550 50  0001 C CNN
	1    5300 2550
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0119
U 1 1 617E81DA
P 5300 2750
F 0 "#PWR0119" H 5300 2500 50  0001 C CNN
F 1 "GND" H 5305 2577 50  0000 C CNN
F 2 "" H 5300 2750 50  0001 C CNN
F 3 "" H 5300 2750 50  0001 C CNN
	1    5300 2750
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0120
U 1 1 617E81EC
P 5600 3100
F 0 "#PWR0120" H 5600 2850 50  0001 C CNN
F 1 "GND" H 5605 2927 50  0001 C CNN
F 2 "" H 5600 3100 50  0001 C CNN
F 3 "" H 5600 3100 50  0001 C CNN
	1    5600 3100
	1    0    0    -1  
$EndComp
$Comp
L Device:R_POT_Dual_Separate RV5
U 2 1 617E81FE
P 4950 2400
F 0 "RV5" H 4880 2446 50  0000 R CNN
F 1 "47k" H 4880 2355 50  0000 R CNN
F 2 "" H 4950 2400 50  0001 C CNN
F 3 "~" H 4950 2400 50  0001 C CNN
	2    4950 2400
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0121
U 1 1 617E8220
P 4950 2600
F 0 "#PWR0121" H 4950 2350 50  0001 C CNN
F 1 "GND" H 4955 2427 50  0000 C CNN
F 2 "" H 4950 2600 50  0001 C CNN
F 3 "" H 4950 2600 50  0001 C CNN
	1    4950 2600
	1    0    0    -1  
$EndComp
$Comp
L Device:CP1_Small C13
U 1 1 617E8232
P 6700 2500
F 0 "C13" V 6928 2500 50  0000 C CNN
F 1 "100u" V 6837 2500 50  0000 C CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.80mm" H 6700 2500 50  0001 C CNN
F 3 "~" H 6700 2500 50  0001 C CNN
	1    6700 2500
	0    -1   -1   0   
$EndComp
$Comp
L Device:C_Small C14
U 1 1 617E8250
P 7050 2700
F 0 "C14" H 7142 2746 50  0000 L CNN
F 1 "0.1u" H 7142 2655 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric" H 7050 2700 50  0001 C CNN
F 3 "~" H 7050 2700 50  0001 C CNN
	1    7050 2700
	1    0    0    -1  
$EndComp
$Comp
L Device:R R18
U 1 1 617E8268
P 7050 2950
F 0 "R18" H 7120 2996 50  0000 L CNN
F 1 "4.7" H 7120 2905 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric" V 6980 2950 50  0001 C CNN
F 3 "~" H 7050 2950 50  0001 C CNN
	1    7050 2950
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0122
U 1 1 617E827E
P 7050 3100
F 0 "#PWR0122" H 7050 2850 50  0001 C CNN
F 1 "GND" H 7055 2927 50  0000 C CNN
F 2 "" H 7050 3100 50  0001 C CNN
F 3 "" H 7050 3100 50  0001 C CNN
	1    7050 3100
	1    0    0    -1  
$EndComp
Wire Wire Line
	4950 2550 4950 2600
Wire Wire Line
	5100 2400 5300 2400
Wire Wire Line
	5800 2400 5300 2400
Connection ~ 5300 2400
Wire Wire Line
	5300 2700 5300 2750
Wire Wire Line
	6400 2500 6600 2500
Wire Wire Line
	6800 2500 7050 2500
Wire Wire Line
	7050 2500 7050 2600
$Comp
L tda:TDA2822 U1
U 2 1 617E829E
P 6100 2500
F 0 "U1" H 6100 2867 50  0000 C CNN
F 1 "TDA2822" H 6100 2776 50  0000 C CNN
F 2 "Package_SO:SO-8_3.9x4.9mm_P1.27mm" H 6100 2500 50  0001 C CIN
F 3 "https://www.nxp.com/docs/en/data-sheet/TDA1308.pdf" H 6100 2500 50  0001 C CNN
	2    6100 2500
	1    0    0    -1  
$EndComp
$Comp
L tda:TDA2822 U1
U 3 1 617FA4D5
P 10050 4050
F 0 "U1" H 10008 4096 50  0000 L CNN
F 1 "TDA2822" H 10008 4005 50  0000 L CNN
F 2 "Package_SO:SO-8_3.9x4.9mm_P1.27mm" H 10050 4050 50  0001 C CIN
F 3 "https://www.nxp.com/docs/en/data-sheet/TDA1308.pdf" H 10050 4050 50  0001 C CNN
	3    10050 4050
	1    0    0    -1  
$EndComp
Wire Wire Line
	5600 1600 5800 1600
Wire Wire Line
	5600 2600 5800 2600
$Comp
L power:GND #PWR0123
U 1 1 6180B79B
P 9950 4350
F 0 "#PWR0123" H 9950 4100 50  0001 C CNN
F 1 "GND" H 9955 4177 50  0000 C CNN
F 2 "" H 9950 4350 50  0001 C CNN
F 3 "" H 9950 4350 50  0001 C CNN
	1    9950 4350
	1    0    0    -1  
$EndComp
$Comp
L power:+9V #PWR0124
U 1 1 6180BBE3
P 9950 3600
F 0 "#PWR0124" H 9950 3450 50  0001 C CNN
F 1 "+9V" H 9965 3773 50  0000 C CNN
F 2 "" H 9950 3600 50  0001 C CNN
F 3 "" H 9950 3600 50  0001 C CNN
	1    9950 3600
	1    0    0    -1  
$EndComp
$Comp
L Device:CP1_Small C5
U 1 1 6180C778
P 9750 3700
F 0 "C5" V 9522 3700 50  0000 C CNN
F 1 "1000u" V 9613 3700 50  0000 C CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.80mm" H 9750 3700 50  0001 C CNN
F 3 "~" H 9750 3700 50  0001 C CNN
	1    9750 3700
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR0125
U 1 1 6180D663
P 9550 3750
F 0 "#PWR0125" H 9550 3500 50  0001 C CNN
F 1 "GND" H 9555 3577 50  0000 C CNN
F 2 "" H 9550 3750 50  0001 C CNN
F 3 "" H 9550 3750 50  0001 C CNN
	1    9550 3750
	1    0    0    -1  
$EndComp
Wire Wire Line
	9950 3600 9950 3700
Wire Wire Line
	9850 3700 9950 3700
Connection ~ 9950 3700
Wire Wire Line
	9950 3700 9950 3750
Wire Wire Line
	9650 3700 9550 3700
Wire Wire Line
	9550 3700 9550 3750
$Comp
L Device:R R15
U 1 1 6180F178
P 5600 4950
F 0 "R15" H 5670 4996 50  0000 L CNN
F 1 "5.1k" H 5670 4905 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 5530 4950 50  0001 C CNN
F 3 "~" H 5600 4950 50  0001 C CNN
	1    5600 4950
	1    0    0    -1  
$EndComp
$Comp
L Device:CP1_Small C9
U 1 1 6180F18E
P 5600 5200
F 0 "C9" H 5691 5246 50  0000 L CNN
F 1 "100u" H 5691 5155 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.80mm" H 5600 5200 50  0001 C CNN
F 3 "~" H 5600 5200 50  0001 C CNN
	1    5600 5200
	1    0    0    -1  
$EndComp
$Comp
L Device:R R11
U 1 1 6180F1AC
P 5300 4750
F 0 "R11" H 5370 4796 50  0000 L CNN
F 1 "10k" H 5370 4705 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 5230 4750 50  0001 C CNN
F 3 "~" H 5300 4750 50  0001 C CNN
	1    5300 4750
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0126
U 1 1 6180F1C2
P 5300 4950
F 0 "#PWR0126" H 5300 4700 50  0001 C CNN
F 1 "GND" H 5305 4777 50  0000 C CNN
F 2 "" H 5300 4950 50  0001 C CNN
F 3 "" H 5300 4950 50  0001 C CNN
	1    5300 4950
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0127
U 1 1 6180F1D4
P 5600 5300
F 0 "#PWR0127" H 5600 5050 50  0001 C CNN
F 1 "GND" H 5605 5127 50  0001 C CNN
F 2 "" H 5600 5300 50  0001 C CNN
F 3 "" H 5600 5300 50  0001 C CNN
	1    5600 5300
	1    0    0    -1  
$EndComp
$Comp
L Device:R_POT_Dual_Separate RV7
U 1 1 6180F1E6
P 4950 4600
F 0 "RV7" H 4881 4646 50  0000 R CNN
F 1 "47k" H 4881 4555 50  0000 R CNN
F 2 "" H 4950 4600 50  0001 C CNN
F 3 "~" H 4950 4600 50  0001 C CNN
	1    4950 4600
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0128
U 1 1 6180F208
P 4950 4800
F 0 "#PWR0128" H 4950 4550 50  0001 C CNN
F 1 "GND" H 4955 4627 50  0000 C CNN
F 2 "" H 4950 4800 50  0001 C CNN
F 3 "" H 4950 4800 50  0001 C CNN
	1    4950 4800
	1    0    0    -1  
$EndComp
$Comp
L Device:CP1_Small C15
U 1 1 6180F21A
P 6700 4700
F 0 "C15" V 6928 4700 50  0000 C CNN
F 1 "100u" V 6837 4700 50  0000 C CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.80mm" H 6700 4700 50  0001 C CNN
F 3 "~" H 6700 4700 50  0001 C CNN
	1    6700 4700
	0    -1   -1   0   
$EndComp
$Comp
L Device:C_Small C16
U 1 1 6180F238
P 7050 4900
F 0 "C16" H 7142 4946 50  0000 L CNN
F 1 "0.1u" H 7142 4855 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric" H 7050 4900 50  0001 C CNN
F 3 "~" H 7050 4900 50  0001 C CNN
	1    7050 4900
	1    0    0    -1  
$EndComp
$Comp
L Device:R R19
U 1 1 6180F250
P 7050 5150
F 0 "R19" H 7120 5196 50  0000 L CNN
F 1 "4.7" H 7120 5105 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric" V 6980 5150 50  0001 C CNN
F 3 "~" H 7050 5150 50  0001 C CNN
	1    7050 5150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0129
U 1 1 6180F266
P 7050 5300
F 0 "#PWR0129" H 7050 5050 50  0001 C CNN
F 1 "GND" H 7055 5127 50  0000 C CNN
F 2 "" H 7050 5300 50  0001 C CNN
F 3 "" H 7050 5300 50  0001 C CNN
	1    7050 5300
	1    0    0    -1  
$EndComp
Wire Wire Line
	4950 4750 4950 4800
Wire Wire Line
	5100 4600 5300 4600
Wire Wire Line
	5800 4600 5300 4600
Connection ~ 5300 4600
Wire Wire Line
	5300 4900 5300 4950
Wire Wire Line
	6400 4700 6600 4700
Wire Wire Line
	6800 4700 7050 4700
Wire Wire Line
	7050 4700 7050 4800
$Comp
L tda:TDA2822 U2
U 1 1 6180F280
P 6100 4700
F 0 "U2" H 6100 5067 50  0000 C CNN
F 1 "TDA2822" H 6100 4976 50  0000 C CNN
F 2 "Package_SO:SO-8_3.9x4.9mm_P1.27mm" H 6100 4700 50  0001 C CIN
F 3 "https://www.nxp.com/docs/en/data-sheet/TDA1308.pdf" H 6100 4700 50  0001 C CNN
	1    6100 4700
	1    0    0    -1  
$EndComp
$Comp
L Device:R R16
U 1 1 6180F2A4
P 5600 5950
F 0 "R16" H 5670 5996 50  0000 L CNN
F 1 "5.1k" H 5670 5905 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 5530 5950 50  0001 C CNN
F 3 "~" H 5600 5950 50  0001 C CNN
	1    5600 5950
	1    0    0    -1  
$EndComp
$Comp
L Device:CP1_Small C10
U 1 1 6180F2BA
P 5600 6200
F 0 "C10" H 5691 6246 50  0000 L CNN
F 1 "100u" H 5691 6155 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.80mm" H 5600 6200 50  0001 C CNN
F 3 "~" H 5600 6200 50  0001 C CNN
	1    5600 6200
	1    0    0    -1  
$EndComp
$Comp
L Device:R R12
U 1 1 6180F2D8
P 5300 5750
F 0 "R12" H 5370 5796 50  0000 L CNN
F 1 "10k" H 5370 5705 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 5230 5750 50  0001 C CNN
F 3 "~" H 5300 5750 50  0001 C CNN
	1    5300 5750
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0130
U 1 1 6180F2EE
P 5300 5950
F 0 "#PWR0130" H 5300 5700 50  0001 C CNN
F 1 "GND" H 5305 5777 50  0000 C CNN
F 2 "" H 5300 5950 50  0001 C CNN
F 3 "" H 5300 5950 50  0001 C CNN
	1    5300 5950
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0131
U 1 1 6180F300
P 5600 6300
F 0 "#PWR0131" H 5600 6050 50  0001 C CNN
F 1 "GND" H 5605 6127 50  0001 C CNN
F 2 "" H 5600 6300 50  0001 C CNN
F 3 "" H 5600 6300 50  0001 C CNN
	1    5600 6300
	1    0    0    -1  
$EndComp
$Comp
L Device:R_POT_Dual_Separate RV7
U 2 1 6180F312
P 4950 5600
F 0 "RV7" H 4880 5646 50  0000 R CNN
F 1 "47k" H 4880 5555 50  0000 R CNN
F 2 "" H 4950 5600 50  0001 C CNN
F 3 "~" H 4950 5600 50  0001 C CNN
	2    4950 5600
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0132
U 1 1 6180F334
P 4950 5800
F 0 "#PWR0132" H 4950 5550 50  0001 C CNN
F 1 "GND" H 4955 5627 50  0000 C CNN
F 2 "" H 4950 5800 50  0001 C CNN
F 3 "" H 4950 5800 50  0001 C CNN
	1    4950 5800
	1    0    0    -1  
$EndComp
$Comp
L Device:CP1_Small C17
U 1 1 6180F346
P 6700 5700
F 0 "C17" V 6928 5700 50  0000 C CNN
F 1 "100u" V 6837 5700 50  0000 C CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.80mm" H 6700 5700 50  0001 C CNN
F 3 "~" H 6700 5700 50  0001 C CNN
	1    6700 5700
	0    -1   -1   0   
$EndComp
$Comp
L Device:C_Small C18
U 1 1 6180F364
P 7050 5900
F 0 "C18" H 7142 5946 50  0000 L CNN
F 1 "0.1u" H 7142 5855 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric" H 7050 5900 50  0001 C CNN
F 3 "~" H 7050 5900 50  0001 C CNN
	1    7050 5900
	1    0    0    -1  
$EndComp
$Comp
L Device:R R20
U 1 1 6180F37C
P 7050 6150
F 0 "R20" H 7120 6196 50  0000 L CNN
F 1 "4.7" H 7120 6105 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric" V 6980 6150 50  0001 C CNN
F 3 "~" H 7050 6150 50  0001 C CNN
	1    7050 6150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0133
U 1 1 6180F392
P 7050 6300
F 0 "#PWR0133" H 7050 6050 50  0001 C CNN
F 1 "GND" H 7055 6127 50  0000 C CNN
F 2 "" H 7050 6300 50  0001 C CNN
F 3 "" H 7050 6300 50  0001 C CNN
	1    7050 6300
	1    0    0    -1  
$EndComp
Wire Wire Line
	4950 5750 4950 5800
Wire Wire Line
	5100 5600 5300 5600
Wire Wire Line
	5800 5600 5300 5600
Connection ~ 5300 5600
Wire Wire Line
	5300 5900 5300 5950
Wire Wire Line
	6400 5700 6600 5700
Wire Wire Line
	6800 5700 7050 5700
Wire Wire Line
	7050 5700 7050 5800
$Comp
L tda:TDA2822 U2
U 2 1 6180F3AC
P 6100 5700
F 0 "U2" H 6100 6067 50  0000 C CNN
F 1 "TDA2822" H 6100 5976 50  0000 C CNN
F 2 "Package_SO:SO-8_3.9x4.9mm_P1.27mm" H 6100 5700 50  0001 C CIN
F 3 "https://www.nxp.com/docs/en/data-sheet/TDA1308.pdf" H 6100 5700 50  0001 C CNN
	2    6100 5700
	1    0    0    -1  
$EndComp
Wire Wire Line
	5600 4800 5800 4800
Wire Wire Line
	5600 5800 5800 5800
$Comp
L tda:TDA2822 U2
U 3 1 61858CCC
P 10050 5350
F 0 "U2" H 10008 5396 50  0000 L CNN
F 1 "TDA2822" H 10008 5305 50  0000 L CNN
F 2 "Package_SO:SO-8_3.9x4.9mm_P1.27mm" H 10050 5350 50  0001 C CIN
F 3 "https://www.nxp.com/docs/en/data-sheet/TDA1308.pdf" H 10050 5350 50  0001 C CNN
	3    10050 5350
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0134
U 1 1 61858CF0
P 9950 5650
F 0 "#PWR0134" H 9950 5400 50  0001 C CNN
F 1 "GND" H 9955 5477 50  0000 C CNN
F 2 "" H 9950 5650 50  0001 C CNN
F 3 "" H 9950 5650 50  0001 C CNN
	1    9950 5650
	1    0    0    -1  
$EndComp
$Comp
L power:+9V #PWR0135
U 1 1 61858D02
P 9950 4900
F 0 "#PWR0135" H 9950 4750 50  0001 C CNN
F 1 "+9V" H 9965 5073 50  0000 C CNN
F 2 "" H 9950 4900 50  0001 C CNN
F 3 "" H 9950 4900 50  0001 C CNN
	1    9950 4900
	1    0    0    -1  
$EndComp
$Comp
L Device:CP1_Small C8
U 1 1 61858D18
P 9750 5000
F 0 "C8" V 9522 5000 50  0000 C CNN
F 1 "1000u" V 9613 5000 50  0000 C CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.80mm" H 9750 5000 50  0001 C CNN
F 3 "~" H 9750 5000 50  0001 C CNN
	1    9750 5000
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR0136
U 1 1 61858D36
P 9550 5050
F 0 "#PWR0136" H 9550 4800 50  0001 C CNN
F 1 "GND" H 9555 4877 50  0000 C CNN
F 2 "" H 9550 5050 50  0001 C CNN
F 3 "" H 9550 5050 50  0001 C CNN
	1    9550 5050
	1    0    0    -1  
$EndComp
Wire Wire Line
	9950 4900 9950 5000
Wire Wire Line
	9850 5000 9950 5000
Connection ~ 9950 5000
Wire Wire Line
	9950 5000 9950 5050
Wire Wire Line
	9650 5000 9550 5000
Wire Wire Line
	9550 5000 9550 5050
$Comp
L Device:CP1_Small C4
U 1 1 6186FA6A
P 3850 2050
F 0 "C4" V 4078 2050 50  0000 C CNN
F 1 "10u" V 3987 2050 50  0000 C CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.80mm" H 3850 2050 50  0001 C CNN
F 3 "~" H 3850 2050 50  0001 C CNN
	1    3850 2050
	0    -1   -1   0   
$EndComp
Wire Wire Line
	2750 2550 2750 2650
Wire Wire Line
	3250 2050 3500 2050
Wire Wire Line
	3500 2050 3500 2200
Wire Wire Line
	3500 2500 3500 2650
Wire Wire Line
	3500 2650 2750 2650
Connection ~ 2750 2650
Wire Wire Line
	2750 2650 2750 2800
Wire Wire Line
	3500 2050 3750 2050
Connection ~ 3500 2050
Wire Wire Line
	4950 1250 4950 1100
Wire Wire Line
	4950 1100 4150 1100
Wire Wire Line
	4150 1100 4150 2050
Wire Wire Line
	4150 2050 3950 2050
Wire Wire Line
	4150 2050 4950 2050
Wire Wire Line
	4950 2050 4950 2250
Connection ~ 4150 2050
Text GLabel 1700 2350 0    50   Input ~ 0
MIC_IN
Wire Wire Line
	1700 2350 1900 2350
Text GLabel 4350 4300 0    50   Input ~ 0
AUX_IN1
Wire Wire Line
	4350 4300 4950 4300
Wire Wire Line
	4950 4300 4950 4450
Text GLabel 4350 5300 0    50   Input ~ 0
AUX_IN2
Wire Wire Line
	4950 5300 4950 5450
Wire Wire Line
	4950 5300 4350 5300
Text GLabel 9100 1500 2    50   Output ~ 0
OUT1
Text GLabel 9100 2500 2    50   Output ~ 0
OUT2
Wire Wire Line
	9100 1500 8200 1500
Connection ~ 7050 1500
Wire Wire Line
	9100 2500 8550 2500
Connection ~ 7050 2500
$Comp
L Device:R R21
U 1 1 6188ACA4
P 7750 4700
F 0 "R21" V 7957 4700 50  0000 C CNN
F 1 "10k" V 7866 4700 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric" V 7680 4700 50  0001 C CNN
F 3 "~" H 7750 4700 50  0001 C CNN
	1    7750 4700
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R22
U 1 1 6188B27E
P 7700 5700
F 0 "R22" V 7907 5700 50  0000 C CNN
F 1 "10k" V 7816 5700 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric" V 7630 5700 50  0001 C CNN
F 3 "~" H 7700 5700 50  0001 C CNN
	1    7700 5700
	0    -1   -1   0   
$EndComp
Wire Wire Line
	7050 4700 7600 4700
Connection ~ 7050 4700
Wire Wire Line
	7900 4700 8200 4700
Wire Wire Line
	8200 4700 8200 1500
Connection ~ 8200 1500
Wire Wire Line
	8200 1500 7050 1500
Wire Wire Line
	7050 5700 7550 5700
Connection ~ 7050 5700
Wire Wire Line
	7850 5700 8550 5700
Wire Wire Line
	8550 5700 8550 2500
Connection ~ 8550 2500
Wire Wire Line
	8550 2500 7050 2500
$EndSCHEMATC
