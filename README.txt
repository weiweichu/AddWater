This file add water into P2VP domain according to the density of ions along x asis.
1. density.py give a density.txt file. This include ion density along x axis
2. main.cpp is to insert water
3. in_gen.py is to generate LAMMPS data file for the solvated system

To run:
1. Run density.py
2. Run main.cpp: g++ main.cpp ReadPolymer.cpp ReadWater.cpp InsertWater.cpp ReadPotential.cpp -o m.out 
3. Run ./m.out
4. Run in_gen.py

Things to notify;
1. In density.py, m is the number of lines before Atoms, m need to be set manually.
