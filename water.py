#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  water.py
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



# water output
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

f = open("MD_npt.data","r")
outf = "water.data"
lines = f.readlines()
i=2
ic = 1
nchains = 0
chargedensity = 0
nions = nchains*64*chargedensity

atoms = []
natomts = []
bonds = []
nbondts = []
angles = []
nanglets = []
dihedrals = []
impropers = []
ndihedralts = []
box = []


natom = 0
i+=1
natomt = 0
i+=1
nbond = 0
i+=1
nbondt = 0
i+=1
nangle = 0
i+=1
nanglet = 0
i+=1
ndihedral = 0
i+=1
ndihedralt = 0
i+=1
nimproper = 0
i+=1
nimpropert = 0
i+=2


for m in range(3):
    #print lines[i]
    box.append(float(lines[i].split()[0]))
    box.append(float(lines[i].split()[1]))
    i+=1
p = open("insertedwater.txt","r")
water = p.readlines()
natomn = (len(water)-2)
natomtn =2
nbondn = (len(water)-2)*2/3
nbondtn = 1
nanglen = (len(water)-2)/3
nangletn =  1
ndihedraln = 0
nimpropern = 0
ndihedraltn = 0
nimpropertn = 0

atomsn = []
bondsn = []
anglesn = []
index = natom+1
for i in range(2,len(water)):
    pos = np.asarray([water[i].split()[0],water[i].split()[1],water[i].split()[2]],dtype=float)
    if((i-2)%3==0):
        atomsn.append([ic,natomt+1,-0.820,pos])
        bondsn.append([nbondt+1,index, index+1])
        bondsn.append([nbondt+1,index, index+2])
        anglesn.append([nanglet+1, index+1,index,index+2])
        index += 3
    else:
        atomsn.append([ic,natomt+2,0.410,pos])
    

out_file = open(outf,"w")

out_file.write('PS with ' + str(0) +' chains and ' + str(64) + ' internal PS monomers per chain and ' + str(64) +' int PMMA monomers per chain'+ 'and ' + str(nions) + ' ions' + ' '+str(len(water)-2)+' waters' +'\n'
+ '\n' +
str(natomn) + ' ' + 'atoms' + '\n'
+ str(nbondn) + ' ' + 'bonds' + '\n'
+ str(nanglen) + ' ' + 'angles' + '\n'
+ str(ndihedraln) + ' ' + 'dihedrals' + '\n'
+ str(nimpropern) + ' ' + 'impropers' + '\n'
+ '\n'
+ str(natomtn)+' atom types'+'\n'+
str(nbondtn)+' bond types'+'\n'+
str(nangletn)+' angle types'+'\n'+
str(ndihedraltn)+' dihedral types'+'\n'+
#str(2)+' improper types'+'\n'+
'\n'+

str(box[0])+' '+str(box[1])+' xlo xhi'+'\n'+
str(box[2])+' '+str(box[3])+' ylo yhi'+'\n'+
str(box[4])+' '+str(box[5])+' zlo zhi'+'\n'+'\n'+'Masses'+'\n'+'\n')

for i in range(len(natomts)):
    out_file.write(natomts[i])
out_file.write(str(len(natomts)+1)+' '+str(15.9994)+'\n')
out_file.write(str(len(natomts)+2)+' '+str(1.008)+'\n'+'\n')
out_file.write("Bond Coeffs"+'\n'+'\n')
for i in range(len(nbondts)):
    out_file.write(nbondts[i])
out_file.write(str(nbondt+1)+' '+str(1000.0)+' '+str(1.0)+'\n'+'\n')
out_file.write("Angle Coeffs"+'\n'+'\n')
for i in range(len(nanglets)):
    out_file.write(nanglets[i])
out_file.write(str(nanglet+1)+' '+str(100.0)+' '+str(109.47)+'\n'+'\n')


    
out_file.write('\n'+'Atoms'+'\n'+'\n')
for i in range(len(atoms)):
	#out_file.write(atoms[i])
    out_file.write(str(atoms[i].split()[0])+' '+str(atoms[i].split()[1])\
    +' '+str(atoms[i].split()[2])+' '+str("{0:.6f}".format(float(atoms[i].split()[3])))+' '+\
    str("{0:.3f}".format(float(atoms[i].split()[4])))+' '+str("{0:.3f}".format(float(atoms[i].split()[5])))+' '+\
    str("{0:.3f}".format(float(atoms[i].split()[6])))+' '+str(atoms[i].split()[7])\
    +' '+str(atoms[i].split()[8])+' '+str(atoms[i].split()[9])+'\n')
  
  
for i in range(len(atomsn)):
    index_chain = atomsn[i][0]
    type_atom = atomsn[i][1]
    charge = atomsn[i][2]
    x_coord = atomsn[i][3][0]
    y_coord = atomsn[i][3][1]
    z_coord = atomsn[i][3][2]
    out_file.write(str(len(atoms)+1+i)+ ' ' + str(index_chain)+ ' ' + str(type_atom) + ' ' + str(charge) + ' ' + 
    str("{0:.3f}".format(x_coord)).strip('[]') + ' ' + str("{0:.3f}".format(y_coord)).strip('[]') + ' ' +
    str("{0:.3f}".format(z_coord)).strip('[]') + ' 0 0 0'+'\n')
    #out_file.write(str(i+len(atoms)+1)+' '+str(atomsn[i][0])+' '+str(atomsn[i][1])+' '+str(atomsn[i][2])+' '+str(atomsn[i][3])+' '+str(atomsn[i][4])+'\n')
   
    

out_file.write('\n'+'Bonds'+'\n'+'\n')
bonding =bondsn
for i in range(len(bonding)):
	out_file.write(str(i+1)+' '+str(bonding[i][0])+' '+str(bonding[i][1])+' '+str(bonding[i][2])+'\n')
    

out_file.write('\n'+'Angles'+'\n'+'\n')
angle=anglesn
for i in range(len(angle)):
    out_file.write(str(i+1)+' '+str(angle[i][0])+' '+str(angle[i][1])+' '+str(angle[i][2])+' '+str(angle[i][3])+'\n')


