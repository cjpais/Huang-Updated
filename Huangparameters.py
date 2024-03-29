# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:08:05 2015
Huang Parameter File
@author: Samuel
"""

import numpy as np
import glob
import multiprocessing
from sys import platform as _platform

Avogadro = 6.0221413e23 # Particles per mole
Kb = 0.0019872041 # Kcal/mol/K
T = 300.0 # Kelvin
Beta = 1.0/(T*Kb)

ChainLength = 5

NumChains = 0

NumPCBM = 0
NumTotal = NumChains*ChainLength + NumPCBM

Density = .0001 # g/mol

Total_Moles = NumTotal/ Avogadro

Monomer_MW = 166.3

Molar_Volume = Monomer_MW/ Density

Volume = Molar_Volume*Total_Moles

Box_Length_CM = Volume**(1./3.)
Box_Length = Box_Length_CM*100000000

BondLengths = { 'P1P1': 3.8283, 'P1P2': 4.0717, 'P2P3': 3.5379}

Angles = { 'P1P1P1': 180.0, 'P1P2P3': 180.0, 'P1P1P2': 122.3208, 'P2P1P1': 82.966}

Dihedral = { 'P1P1P1P1': [0.5351,-0.3752, -0.1948, .0043, .0307]}

SigmaM_M = 10.0 

MP1 = 81.14
MP2 = 42.0
MP3 = 43.0 

P1P1 = [3.82, 69.2079, 99.9792, 56.1341]
P1P2 = [4.0717, 52.654, 204.587, -16.5917, -1274.19, -1508.92, 1974.5, 5398.08, 4062.79, 1047.06]
P2P3 = [3.5379, 42.7122, -35.9374, -765.2834, -57.7580, 5987.6943, 4521.3293, -18075.7468, -23031.1720, 14569.7691, 34470.5839, 14124.3235]

P1P1P1 = [ 180.0, .1510, -4.007, 0.0, 33.5046, 0.0, -72.5621, 95.3526, -78.47, 39.4813, -11.1020, 1,3361]
P1P2P3 = [180.0, 0.8308, -15.9323, 0.0, 112.8127, 0.0, -385.7309, 783.1507, -1009.4080, 860.7848, -496.3477, 194.3546, -50.8883, 8.5235, -0.8252, 0.0351]
P1P1P2 = [ 122.3208, 0.0, 9.1015, -1.6127, -9.4041, 9.3766, 17.0502]
P2P1P1 = [ 82.9660, 0.0, 18.8156, 10.6338, -31.3568, -72.7769, 152.89]

P1P1P1P1 = [ 0.5351, -0.3752, -0.1948, 0.0043, 0.0307]
P2P1P1P2 = [ 0.5445, 0.0884, 0.7051, 1.6496, -1.1050, -2.258, 0.1608, 0.9272, .1018]
P1P1P2P3 = [ 0.2849, -.4701, -.0475, 0.1486, 0.1121]
P3P2P1P1 = [ .0227, .2109, .4953, .0094, -.0727]
P2P1P1P2OPT = [ 0.55509257, 0.38837346,  0.52557038,  0.04405308, -0.68564385]

cores = multiprocessing.cpu_count()

if _platform == "darwin":
   lammps = "lammps"

elif _platform == "linux" or _platform == "linux2":
   lmp = glob.glob('/usr/local/bin/lmp*')
   lmp1 = [x for y in lmp for x in y.split("/")]
   lammps = lmp1[len(lmp1) - 1]