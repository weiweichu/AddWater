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

filename = "MD_npt.data"
natom = 0
nmove = 38
pxl = 0
pxh = 340
bxl = pxl
bxh = pxh
bl = pxh-pxl
setp = 1
m=96
bxll=13
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
pxh = int(bxh)
pxl = int(bxl)
bl = pxh-pxl
nl = int((bl))
n0 = [0]*nl
n1 = [0]*nl 
n2 = [0]*nl
n3 = [0]*nl    
for i in range(m,m+natom):
    atom.append(np.asarray([lines[i].split()[2],lines[i].split()[4]],dtype=float))

for i in range(natom):
    if atom[i][1]<pxl:
        atom[i][1] += bl
    elif atom[i][1] > pxh:
        atom[i][1] -= bl
    else:
        continue
       
for i in range(natom):
    if int(atom[i][0])==1:
        k = int(math.floor(atom[i][1]))-pxl
        #print k, nl
        n0[k] += 1
    elif int(atom[i][0])==6 or int(atom[i][0])==11:
        k = int(math.floor(atom[i][1]))-pxl
        n1[k] += 1
        
    elif int(atom[i][0])==18:
        k = int(math.floor(atom[i][1]))-pxl
        n2[k] += 1
        
    elif int(atom[i][0])==19:
        k = int(math.floor(atom[i][1]))-pxl
        n3[k] += 1
        

w = open("density.txt",'w')
w.write(str(len(n2)))
w.write('\n')
for i in range(len(n2)):
	w.write('{0:8f}\n'.format(float(n2[i])/np.amax(n2)))
w.close()  

    
x = np.arange(0,nl*0.1,0.1)
#plt.plot(x,n0,label="PS")
#plt.plot(x,n1,label="P2VP")
plt.plot(x,n2,label="Ion")
#plt.plot(x,n3,label="Water")
plt.axis([0,40,0,180])
plt.xlabel("L/nm")
#plt.yticks([])
plt.legend()
plt.show()
        
        
    
        
    


