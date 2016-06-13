#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  density.py
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


#Periodic density profile
import sys
import math
import pylab
import matplotlib.pyplot as plt
import numpy as np

#filename = "MD_npt.data"
#natom = 0
#nmove = 35
#pxl = 10
#pxh = 352
#bxl = pxl
#bxh = pxh
#bl = pxh-pxl
#setp = 1
#m=100
#bxll=13

filename = "polymerwater.data"
natom = 0
nmove = 38
pxl = 21
pxh = 343
bxl = pxl
bxh = pxh
bl = pxh-pxl
setp = 1
m=101
bxll=14
nbin = 1

atom = []

f = open(filename, 'r')
lines = f.readlines()
for i in range(len(lines)):
    if i==2:
        natom = int(lines[i].split()[0])
    elif i==bxll:
        bxl = float(lines[i].split()[0])
        bxh = float(lines[i].split()[1])
        break
    
print bxl, bxh
bl = pxh-pxl
nl = int((bl+1))
n0 = [0]*nl
n1 = [0]*nl 
n2 = [0]*nl
n3 = [0]*nl    
for i in range(m,m+natom):
    atom.append(np.asarray([lines[i].split()[2],lines[i].split()[4]],dtype=float))

#periodic boundary condition
for i in range(natom):
    if atom[i][1]<pxl:
        atom[i][1] += bl
    elif atom[i][1] > pxh:
        atom[i][1] -= bl
    else:
        continue

#move
for i in range(natom):
    if atom[i][1]>nmove:
        atom[i][1]-=nmove
    else:
        atom[i][1]+=(bl-nmove)
        
for i in range(natom):
    if int(atom[i][0])==1:
        k = int(math.floor(atom[i][1]))
        #print k, nl
        n0[k] += 1
    elif int(atom[i][0])==6 or int(atom[i][0])==11:
        k = int(math.floor(atom[i][1])*nbin)
        n1[k] += 1
        
    elif int(atom[i][0])==18:
        k = int(math.floor(atom[i][1]))
        n2[k] += 1
        
    elif int(atom[i][0])==19:
        k = int(math.floor(atom[i][1]))
        n3[k] += 1
        
#print len(n1)
print np.amax(n1)
w = open("density.txt",'w')
w.write(str(len(n1)))
w.write('\n')
for i in range(len(n1)):
	w.write('{0:8f}\n'.format(float(n1[i])/np.amax(n1)))
w.close()      
#x = np.arange(0,nl*0.1,0.1)
#plt.plot(x,n0,label="PS")
#plt.plot(x,n1,label="P2VP")
#plt.plot(x,n2,label="Ion")
##plt.plot(x,n3,label="Water")
#plt.axis([0,40,0,180])
#plt.xlabel("L/nm")
##plt.yticks([])
#plt.legend()
#plt.show()
        
        
    
        
    


