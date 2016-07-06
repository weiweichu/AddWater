#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  in_gen_water.py
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

f = open("after_min.data","r")
outf = "polymerwater.data"
lines = f.readlines()
i=2
ic = 300
nchains = 204
chargedensity = 0.5
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


natom = int(lines[i].split()[0])
i+=1
natomt = int(lines[i].split()[0])
i+=1
nbond = int(lines[i].split()[0])
i+=1
nbondt = int(lines[i].split()[0])
i+=1
nangle = int(lines[i].split()[0])
i+=1
nanglet = int(lines[i].split()[0])
i+=1
ndihedral = int(lines[i].split()[0])
i+=1
ndihedralt = int(lines[i].split()[0])
i+=1
nimproper = int(lines[i].split()[0])
i+=1
nimpropert = int(lines[i].split()[0])
i+=2


for m in range(3):
    #print lines[i]
    box.append(float(lines[i].split()[0]))
    box.append(float(lines[i].split()[1]))
    i+=1

i += 3
for m in range(natomt):
    natomts.append(lines[i])
    i += 1

i+=3
for m in range(nbondt):
    nbondts.append(lines[i])
    i += 1
    
i+=3
for m in range(nanglet):
    nanglets.append(lines[i])
    i+=1
    
i+=3
for m in range(ndihedralt):
    ndihedralts.append(lines[i])
    i += 1


i+=3
for m in range(natom):
    atoms.append(lines[i])
    i += 1


print atoms[0]

i+=(3+natom+3)
for m in range(nbond):
    bonds.append(lines[i])
    i+=1

print bonds[0]  

i+=3
for m in range(nangle):
    angles.append(lines[i])
    i+=1

print angles[0] 
i+=3
for m in range(ndihedral):
    dihedrals.append(lines[i])
    i+=1

print dihedrals[0]  
i+=3
for m in range(nimproper):
    impropers.append(lines[i])
    i+=1
    
#print impropers[0]

p = open("insertedwater.txt","r")
water = p.readlines()
natomn = natom + (len(water)-2)
natomtn = natomt 
nbondn = nbond + (len(water)-2)*2/3
nbondtn = nbondt 
nanglen = nangle + (len(water)-2)/3
nangletn = nanglet 
ndihedraln = ndihedral
nimpropern = nimproper
ndihedraltn = ndihedralt
nimpropertn = nimpropert

atomsn = []
bondsn = []
anglesn = []
index = natom+1
for i in range(2,len(water)):
    pos = np.asarray([water[i].split()[0],water[i].split()[1],water[i].split()[2]],dtype=float)
    if((i-2)%3==0):
        atomsn.append([ic,19,-0.820,pos])
        bondsn.append([20,index, index+1])
        bondsn.append([20,index, index+2])
        anglesn.append([24, index+1,index,index+2])
        index += 3
    else:
        atomsn.append([ic,20,0.410,pos])
    

out_file = open(outf,"w")

out_file.write('PS with ' + str(nchains) +' chains and ' + str(64) + ' internal PS monomers per chain and ' + str(64) +' int PMMA monomers per chain'+ 'and ' + str(nions) + ' ions' + ' '+str((len(water)-2)/3)+' waters' +'\n'
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
str(2)+' improper types'+'\n'+'\n'+

str(box[0])+' '+str(box[1])+' xlo xhi'+'\n'+
str(box[2])+' '+str(box[3])+' ylo yhi'+'\n'+
str(box[4])+' '+str(box[5])+' zlo zhi'+'\n'+'\n'+'Masses'+'\n'+'\n')

for i in range(len(natomts)):
    out_file.write(natomts[i])

out_file.write('\n'+"Bond Coeffs"+'\n'+'\n')
for i in range(len(nbondts)):
    out_file.write(nbondts[i])

out_file.write('\n'+"Angle Coeffs"+'\n'+'\n')
for i in range(len(nanglets)):
    out_file.write(nanglets[i])
out_file.write('\n'+"Dihedral Coeffs"+'\n'+'\n')
for i in range(len(ndihedralts)):
    out_file.write(ndihedralts[i])


    
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
for i in range(len(bonds)):
    out_file.write(bonds[i])

bonding =bondsn
for i in range(len(bonding)):
	out_file.write(str(i+1+len(bonds))+' '+str(bonding[i][0])+' '+str(bonding[i][1])+' '+str(bonding[i][2])+'\n')
    

out_file.write('\n'+'Angles'+'\n'+'\n')
angle=anglesn
for i in range(len(angles)):
    out_file.write(angles[i])
for i in range(len(angle)):
    out_file.write(str(i+1+len(angles))+' '+str(angle[i][0])+' '+str(angle[i][1])+' '+str(angle[i][2])+' '+str(angle[i][3])+'\n')

out_file.write('\n'+'Dihedrals'+'\n'+'\n')
for i in range(len(dihedrals)):
    out_file.write(dihedrals[i])

out_file.write('\n'+'Impropers'+'\n'+'\n')
for i in range(len(impropers)):
	out_file.write(impropers[i])

