//
//  InsertWater.h
//  Solvation
//
//  Created by Weiwei Chu on 5/17/16.
//  Copyright (c) 2016 Weiwei Chu. All rights reserved.
//

#ifndef __Solvation__InsertWater__
#define __Solvation__InsertWater__

#include <stdio.h>
#include <vector>
#include "Vector.h"
#include "GridM.h"

using namespace std;

typedef vector<Vector> atom;

class InsertWater{
public:
    InsertWater(atom polymer, atom water, double radius,VectorInt ngrid, vector<double> box):
    grid_(polymer, ngrid, box),
    polymer_(polymer),
    water_(water),
    radius_(radius),
    ngrid_(ngrid),
    box_(box)
    {
				cout<<"insetwater"<<endl;
		};
    
    void insert(atom *inserted);
private:
    GridM grid_;
    atom polymer_;
    atom water_;
    double radius_;
    VectorInt ngrid_;
    vector<double> box_;
    
};

#endif /* defined(__Solvation__InsertWater__) */
