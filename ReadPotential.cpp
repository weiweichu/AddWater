//
//  ReadPotential.cpp
//  Solvation
//
//  Created by Weiwei Chu on 6/13/16.
//  Copyright (c) 2016 Weiwei Chu. All rights reserved.
//

#include "ReadPotential.h"

void ReadPotential::potential(vector <double> *potential){
	ifstream in(fname_);
    if (in.is_open()){
		cout << "potential file is open" << endl;
	}
    string line;
    getline(in,line);
    int nt;
    double t;
    sscanf(line.c_str(),"%d",&nt);
    for (int i=0; i<nt; i++){
		getline(in,line);
		sscanf(line.c_str(),"%lf",&t);
		potential->push_back(t);
	}
}	
	
