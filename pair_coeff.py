#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pair_coeff.py
#  
#  Copyright 2016 weiwei <weiwei@xps8700>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



#Generate pairwise parameter for lammps
import os
import numpy as np
import re 
import fnmatch 
import itertools 
from operator import itemgetter
import sys
import contextlib
import collections
import random
import math

def arith(a,b):
    c1 = math.sqrt(a[0]*b[0])
    c2 = (a[1]+b[1])/2
    c = [c1,c2]
    return c
    
def geomatric(a,b):
    c1 = math.sqrt(a[0]*b[0])
    c2 = math.sqrt(a[1]*b[1])
    c = [c1,c2]
    return c
    
#epsilon, sigma with arithmatic mixing rule
#1
p1 = [0.084, 3.207]
p2 = [0.076, 2.318]
p3 = [0.070, 3.550]
p4 = [0.070, 3.550]
p5 = [0.030, 2.420]
p6 = [0.084, 3.207]
p7 = [0.076, 2.318]
p8 = [0.070, 3.550]
p9 = [0.030, 2.420]
p10 = [0.170, 3.250]
p11 = [0.084, 3.207]
p12 = [0.076, 2.318]
p13 = [0.070, 3.550]
p14 = [0.030, 2.420]
p15 = [0.170, 3.250]
p16 = [0.066, 3.500]
p17 = [0.030, 2.500]
p18 = [0.043, 5.201]
p19 = [0.155, 3.166]
p20 = [0.000, 0.000]

#all
p = []
p.append(p1)
p.append(p2)
p.append(p3)
p.append(p4)
p.append(p5)
p.append(p6)
p.append(p7)
p.append(p8)
p.append(p9)
p.append(p10)
p.append(p11)
p.append(p12)
p.append(p13)
p.append(p14)
p.append(p15)
p.append(p16)
p.append(p17)
p.append(p18)
p.append(p19)
p.append(p20)

#pairstyle modify
#ps =[[1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0]
ps = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3],#1
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3],#2
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3],#3
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3],#4
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3],#5
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3],#6
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3],#7
      [1,1,1,1,1,1,1,2,2,2,1,1,2,2,2,2,2,2,3,3],#8
      [1,1,1,1,1,1,1,2,2,2,1,1,2,2,2,2,2,2,3,3],#9
      [1,1,1,1,1,1,1,2,2,2,1,1,2,2,2,2,2,2,3,3],#0
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3],#1
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3],#2
      [1,1,1,1,1,1,1,2,2,2,1,1,2,2,2,2,2,2,3,3],#3
      [1,1,1,1,1,1,1,2,2,2,1,1,2,2,2,2,2,2,3,3],#4
      [1,1,1,1,1,1,1,2,2,2,1,1,2,2,2,2,2,2,3,3],#5
      [1,1,1,1,1,1,1,2,2,2,1,1,2,2,2,2,2,2,3,3],#6
      [1,1,1,1,1,1,1,2,2,2,1,1,2,2,2,2,2,2,3,3],#7
      [1,1,1,1,1,1,1,2,2,2,1,1,2,2,2,2,2,2,3,3],#8
      [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],#9
      [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]]#0
      
      
#pairstyle
psh = 'lj/cut/coul/long'

#geometric for P2VP+
geo = [8,9,10,13,14,15,16,17]
o = open("pair_coeff.txt",'w')
for i in range(len(p)):
    for j in range(i,len(p)):
        if (i+1) in geo and (j+1) in geo:
            c = geomatric(p[i],p[j])
        elif (i+1)== 20 or (j+1) == 20:
            c = [0, 0]
        else:
            c=arith(p[i],p[j])
        o.write("pair_coeff "+str(i+1)+'  '+str(j+1)+' '+psh+' '+str(ps[i][j])+' '+'{0:4.3f}{1:6.3f}\n'.format(c[0],c[1]))
o.close()
        

