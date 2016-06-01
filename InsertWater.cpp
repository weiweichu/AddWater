//
//  InsertWater.cpp
//  Solvation
//
//  Created by Weiwei Chu on 5/17/16.
//  Copyright (c) 2016 Weiwei Chu. All rights reserved.
//

#include "InsertWater.h"

void InsertWater::insert(atom *inserted){
   // atomlist all;
    atomlist po = grid_.AtomList();
    int insertedwater=0;
    //cout << water_.size()<<endl;
    for (int i=0;i<water_.size();i++) {
		cout << water_.size()<< "   "<< i<<endl;
        int flag=1;
        
        //for(int k =0; k<3;k++){
        if (i%3 == 0){
			cout << "insert  "<<water_[i][0]<<"  "<<water_[i][1]<< "  "<<water_[i][2]<<endl;
	        atom p = grid_.neighborlist(water_[i],po);
	        
	        cout <<p.size()<<"  neighborlistsize per water"<<endl;
	       
	        for(int j=0;j<p.size();j++){
	                if (water_[i*3].dist(p[j])>radius_) {
	                    flag *= 1;
	                }
	                else{
	                    flag *= 0;
	                   // break;
	                }
	                if (flag == 0) {
	                    break;
	                }
	        }
		//}
	        if (flag == 1){
				insertedwater++;
				cout << "inserted   "<<insertedwater<<endl;
	            inserted->push_back(water_[i+0]);
	            cout << water_[i+0][0]<<" "<< water_[i+1][1]<<" "<<water_[i+2][2]<<" "<<endl;
	            inserted->push_back(water_[i+1]);
	            cout << water_[i+1][0]<<" "<< water_[i+1][1]<<" "<<water_[i+1][2]<<" "<<endl;
	            inserted->push_back(water_[i+2]);
	            cout << water_[i+2][0]<<" "<< water_[i+2][1]<<" "<<water_[i+2][2]<<" "<<endl;
            }        
        }
    }
    
}
