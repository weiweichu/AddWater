//
//  ReadPolymer.h
//  Solvation
//
//  Created by Weiwei Chu on 5/17/16.
//  Copyright (c) 2016 Weiwei Chu. All rights reserved.
//

#ifndef __Solvation__ReadPolymer__
#define __Solvation__ReadPolymer__

#include <stdio.h>
#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include "Vector.h"



#endif /* defined(__Solvation__ReadPolymer__) */
using namespace std;

typedef vector<string> sentence;
typedef string::size_type s_type;
typedef vector<Vector> atom;

class ReadDataFile{
public:
    ReadDataFile(char* fname):
    fname_(fname)
    {
		cout<<"readpolymer"<<endl;
		};
    //virtual ~ReadDataFile();
    void OutPolymer(atom *polymer,vector<double> *polymerbox);
    sentence split(const string& s);
private:
    char* fname_;
    //vector<double> polymerbox_;
    //atom polymer_;
    
};
