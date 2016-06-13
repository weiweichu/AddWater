//
//  ReadPotential.h
//  Solvation
//
//  Created by Weiwei Chu on 6/13/16.
//  Copyright (c) 2016 Weiwei Chu. All rights reserved.
//

#ifndef __Solvation__ReadPotential__
#define __Solvation__ReadPotential__

#include <stdio.h>
#include <vector>
#include <fstream>
#include <iostream>
#include <math.h>
#include "Vector.h"
#include <stdlib.h>


using namespace std;
class ReadPotential{
public:
    ReadPotential(char *fname):
    fname_(fname)
    {}
    void potential(vector <double> *potential);
private:
    char *fname_;
    
};
#endif /* defined(__Solvation__ReadPotential__) */
