//
//  ReadWater.h
//  Solvation
//
//  Created by Weiwei Chu on 5/17/16.
//  Copyright (c) 2016 Weiwei Chu. All rights reserved.
//

#ifndef __Solvation__ReadWater__
#define __Solvation__ReadWater__

#include <stdio.h>
#include <vector>
#include <fstream>
#include <iostream>
#include <math.h>
#include "Vector.h"
#include <stdlib.h>

#endif /* defined(__Solvation__ReadWater__) */

using namespace std;

typedef vector<Vector> atom;
class ReadWater{
public:
    ReadWater(char* fname,vector<double> box,double density,vector<double> wbox):
    fname_(fname),
    box_(box),
    density_(density),
    wbox_(wbox)
    {};
    void OutWater(atom *water);
private:
    char* fname_;
    vector<double> box_,wbox_;
    double density_;
};
