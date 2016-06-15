//
//  main.cpp
//  Solvation
//
//  Created by Weiwei Chu on 5/17/16.
//  Copyright (c) 2016 Weiwei Chu. All rights reserved.
//

#include <iostream>
#include "ReadPolymer.h"
#include "ReadWater.h"
#include "InsertWater.h"
//#include "ReadPotential.h"
//#include "GridM.h"

using namespace std;
typedef vector<Vector> atom;
typedef vector<atom> atomlist;

int main(int argc, const char * argv[]) {
    char waterfile[] = "300k.xyz";
    char polymerfile[] = "MD_npt.data";
    double radius = 3.0;
    VectorInt ngrid(100,50,50);
    vector<double> polymerbox;
    atom polymer;
    atom allwater;
    atom insertedwater;
    double density = 1;
    vector<double> waterbox (3,200);
    ReadDataFile readpolymer(polymerfile);
    readpolymer.OutPolymer(&polymer,&polymerbox);
    ReadWater readwater(waterfile, polymerbox, density, waterbox);
    readwater.OutWater(&allwater);
   // GridM(polymer, ngrid, polymerbox); 
   cout << " main " << allwater.size() << endl;
    InsertWater insert(polymer, allwater, radius, ngrid, polymerbox);
    insert.insert(&insertedwater);
    ofstream out;
    out.open("insertedwater.txt");
    out << insertedwater.size() <<endl;
    out << endl;
    for(int i = 0; i< insertedwater.size();i++){
		out << insertedwater[i][0] << "    " <<insertedwater[i][1] << "    "<<insertedwater[i][2]<<endl;
	}
    //cout << insertedwater.size()<<endl;
    return 0;
}
