//
//  Grid.h
//  Solvation
//
//  Created by Weiwei Chu on 5/18/16.
//  Copyright (c) 2016 Weiwei Chu. All rights reserved.
//

//Grid is used to
//1. return the grid index for all atoms
//2. determine the atom list for each grid point
//3. get neighbor list for a certain atom

#ifndef Solvation_Grid_h
#define Solvation_Grid_h
#include <vector>
#include "Vector.h"


using namespace std;

typedef vector<Vector> atom;
typedef vector<vector<Vector> > atomlist;
class Grid {
public:
    Grid(VectorInt ngrid, vector<double> box):
    ngrid_(ngrid),
    box_(box)
    {
		cout<<"grid"<<endl;
		};
    
    VectorInt Grid_index(Vector position){
        Vector boxl_(box_[1]-box_[0],box_[3]-box_[2],box_[5]-box_[4]);
        
        for(int i=0;i<3;i++){
			position[i] -= box_[i*2];
			while(position[i]<0){
				position[i]+=boxl_[i];}
			while(position[i]>boxl_[i]){
				position[i]-=boxl_[i];}
		}
        int a,b,c;
        a = ceil(position[0]*ngrid_[0]/boxl_[0]);
        b = ceil(position[1]*ngrid_[1]/boxl_[1]);
        c = ceil(position[2]*ngrid_[2]/boxl_[2]);
       
        return VectorInt(a,b,c);
    }
    
    int wrap(int a,int b, int c){
		if (a>ngrid_[0]){
			a-=ngrid_[0];
			//cout<< "grid wrap x yes" << endl;
			}
		if (a<=0){
			a+=ngrid_[0];
			//cout<< "grid wrap x yes" << endl;
			}
			
		if (b>ngrid_[1]){
			b-=ngrid_[1];
			//cout<< "grid wrap y yes" << endl;
			}
		if (b<=0){
			b+=ngrid_[1];
			//cout<< "grid wrap y yes" << endl;
			}
			
		if (c>ngrid_[2]){
			c-=ngrid_[2];
			//cout<< "grid wrap z yes" << endl;
			}
		if (c<=0){
			c+=ngrid_[2];
			//cout<< "grid wrap z yes" << endl;
			}
		//cout<<"gridindex  "<<a<<"  "<<b<<"   "<<c<<endl;				
		int p;
		p = a-1+ngrid_[0]*(b-1+ngrid_[1]*(c-1));
		return p;
	}
    
    //return the atom list for each grid point
        
private:
    VectorInt ngrid_;
    vector<double> box_;
    
    
};

#endif
