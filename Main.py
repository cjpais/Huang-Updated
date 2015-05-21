# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:46:22 2015

@author: Samuel
@author: Christopher
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import math

import PolyModelFunctionsHuang as poly
import Huangparameters as Huang
import HuangData
import RunLammps


def main():

    if os.name != 'posix':
        print "cannot get location of lammps, due to unsupported os"
        quit()

    for x in range(0,5):
        Huang.ChainLength *= 2
        Huang.NumChains = int(math.sqrt(Huang.ChainLength)*70.6+1)
        print "Chain Length: %s" % Huang.ChainLength
        print "Number of Chains: %s" % Huang.NumChains 
        
        PDF, CDF = poly.Gen_PDF_CDF_Multi(Huang.P1P1P1P1, Huang.Beta)
        
        Position_M, Position_S1, Position_S2, Bases  =  poly.Gen_Many_Polymers( Huang.ChainLength, Huang.NumChains, Huang.BondLengths, Huang.Angles, CDF, Huang.SigmaM_M, Huang.Box_Length)
        In_Filename = 'in.P3HTHuangE%d_%d' % ( Huang.ChainLength, Huang.NumChains)
        Data_Filename = 'data.P3HTHuang%d_%d' % ( Huang.ChainLength, Huang.NumChains)
        Restart_Filename = 'restart.P3HTHuang%d_%d' % (Huang.ChainLength, Huang.NumChains)
        Dump_Filename = 'P3HTHuangCheck.lammpstrj'
        Pair_Table = 'HuangPair.table'
         
        os.mkdir('P3HTHuang%d_%d' %(Huang.ChainLength, Huang.NumChains))
        os.system('cp HuangPair2.table P3HTHuang%d_%d' % (Huang.ChainLength, Huang.NumChains)); os.system('cp HuangBond.table P3HTHuang%d_%d' % (Huang.ChainLength, Huang.NumChains)); os.system('cp HuangAngle.table P3HTHuang%d_%d' % (Huang.ChainLength, Huang.NumChains))
    	
        os.chdir('P3HTHuang%d_%d' %(Huang.ChainLength, Huang.NumChains))
        
        HuangData.P3HTHuangDataLammps(Position_M, Position_S1, Position_S2, Data_Filename)
        
        HuangData.Run_Huang_Equil(In_Filename, Data_Filename, Pair_Table, Restart_Filename, Dump = Dump_Filename, Num_Steps= 100000, Time_Step = 2)
        
        infileNPT = 'in.P3HTHuang%d_%d_NPT' % (Huang.ChainLength, Huang.NumChains)
        Restart_Out = 'restart.P3HTHuang%d_%d_E' %(Huang.ChainLength, Huang.NumChains)
        Dump_Filename2 = 'P3HTHuang%d_%d_compress.lammpstrj' %(Huang.ChainLength, Huang.NumChains)
        HuangData.EquilibrateNPT(infileNPT, Restart_Filename, Restart_Out, Dump=Dump_Filename2, Time_Step = 2, Num_Steps = 1000000);

    
if __name__=='__main__': main()