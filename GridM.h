//
//  GridM.h
//  Solvation
//
//  Created by Weiwei Chu on 5/18/16.
//  Copyright (c) 2016 Weiwei Chu. All rights reserved.
//

#ifndef Solvation_GridM_h
#define Solvation_GridM_h
#include "Grid.h"

class GridM : public Grid{
public:
    
    GridM(atom atoms,VectorInt ngrid, vector<double> box):
    Grid(ngrid, box),
    ngrid_(ngrid),
    atoms_(atoms),
    ngrids_(ngrid.prod())
    {
		cout<<"gridm"<<endl;
		//cout<< ngrid_.prod()<<endl;
		};
    
    atomlist AtomList()
    {   
		atomlist p;
		p.resize(ngrids_,ve_);
		//cout <<"atomilst"<<endl;		
        for (int i=0;i<atoms_.size();i++) {
            VectorInt gridi=Grid_index(atoms_[i]);
            int in=wrap(gridi[0],gridi[1],gridi[2]);
            //cout << gridi[0] <<"   "<<gridi[1]<<"  "<<gridi[2]<<endl;
            //cout << in << endl;
            //cout<<p.size()<<endl;
           
            p[in].push_back(atoms_[i]);
            
        }
       // cout<< p[0].size()<<"   atomlist size"<<endl;
        return p;
    }
    atom neighborlist(Vector a, atomlist po){
        atom p;
        VectorInt vi=Grid_index(a);
        for (int i=-1; i<=1; i++) {
            for(int j=-1;j<=1;j++){
                for (int k=-1; k<=1; k++) {
					int in = wrap(vi[0]+i,vi[1]+k,vi[2]+j);
					for(int mk=0;mk<po[in].size();mk++){
                    p.push_back(po[in][mk]);
				}
                }
            }
        }
        //cout<<"gridm neighborlist"<< p.size()<<endl;
        return p;
    }
private:
    atom atoms_;
    VectorInt ngrid_;
    vector<Vector> ve_;
    int ngrids_;
    

};

#endif
