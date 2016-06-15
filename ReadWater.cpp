//
//  ReadWater.cpp
//  Solvation
//
//  Created by Weiwei Chu on 5/17/16.
//  Copyright (c) 2016 Weiwei Chu. All rights reserved.
//

#include "ReadWater.h"
void ReadWater::OutWater(atom * water){
    ifstream in(fname_);
    string line;
    atom allwater;
    char t;
    double ran;
    double tx,ty,tz;
    int nw = 0;
    getline(in,line);
    sscanf(line.c_str(),"%d",&nw);
    getline(in,line);
    int ip = -1;
    //int tw = int((int(density_*nw)-int(density_*nw)%3)/3);
    for(int i = 0; i< nw/3; i++){
		ran = double(rand())/RAND_MAX;
		if (ran < density_){
		getline(in,line);
		sscanf(line.c_str(),"%s %lf %lf %lf",&t,&tx,&ty,&tz);
		//cout << t << "  "<<tx<<"  "<<ty<<"  "<<tz<<endl;
		allwater.push_back(Vector(tx,ty,tz));
		getline(in,line);
		sscanf(line.c_str(),"%s %lf %lf %lf",&t,&tx,&ty,&tz);
		//cout << t << "  "<<tx<<"  "<<ty<<"  "<<tz<<endl;
		allwater.push_back(Vector(tx,ty,tz));
		getline(in,line);
		sscanf(line.c_str(),"%s %lf %lf %lf",&t,&tx,&ty,&tz);
		//cout << t << "  "<<tx<<"  "<<ty<<"  "<<tz<<endl;
		allwater.push_back(Vector(tx,ty,tz));}
		else{
			getline(in,line);
			getline(in,line);
			getline(in,line);}
	}
    
    //put water molecule into simulation box periodically

    int fxl,fxh,fyl,fyh,fzl,fzh;
    if(box_[0]>0)
        fxl = ceil(box_[0]/wbox_[0]);
    else
        fxl = floor(box_[0]/wbox_[0]);
    if(box_[1]>0)
        fxh = ceil(box_[1]/wbox_[0]);
    else
        fxh = floor(box_[1]/wbox_[0]);
    if(box_[2]>0)
        fyl = ceil(box_[2]/wbox_[1]);
    else
        fyl = floor(box_[2]/wbox_[1]);
    if(box_[3]>0)
        fyh = ceil(box_[3]/wbox_[1]);
    else
        fyh = floor(box_[3]/wbox_[1]);
    if(box_[4]>0)
        fzl = ceil(box_[4]/wbox_[2]);
    else
        fzl = floor(box_[4]/wbox_[2]);
    if(box_[5]>0)
        fzh = ceil(box_[5]/wbox_[2]);
    else
        fzh = floor(box_[5]/wbox_[2]);
    
    cout << fxl <<"  " << fxh <<"  "<< fyl <<"  " << fyh <<"  "<< fzl <<"  " << fzh <<"  "<<endl;
    for (int i=fxl; i<=fxh; i++) {
        for (int j=fyl; j<=fyh; j++) {
            for (int k = fzl; k<=fzh; k++) {
                for (int n=0; n<allwater.size()/3; n++) {
                    int m = n*3;
                    if (allwater[m][0]+wbox_[0]*(i-1)>box_[0] && allwater[m][0]+wbox_[0]*(i-1)<box_[1] && allwater[m][1]+wbox_[1]*(j-1)>box_[2] && allwater[m][1]+wbox_[1]*(j-1)<box_[3] && allwater[m][2]+wbox_[2]*(k-1)>box_[4] && allwater[m][2]+wbox_[2]*(k-1)<box_[5]) {
                        double d1 = allwater[m].dist(allwater[m+1]);
                        double d2 = allwater[m].dist(allwater[m+2]);
                        //cout << "before wrap" << endl;
                        //cout << allwater[m][0] << "  "<<allwater[m][1]<< "  "<<allwater[m][2]<<endl;
                        //cout << allwater[m+1][0] << "  "<<allwater[m+1][1]<< "  "<<allwater[m+1][2]<<endl;
                        //cout << allwater[m+2][0] << "  "<<allwater[m+2][1]<< "  "<<allwater[m+2][2]<<endl;
                        //cout << allwater[m][0]<<endl;
                        if ((d1 < 1.5) && (d2 < 1.5)){
                        water->push_back(Vector(allwater[m][0]+wbox_[0]*(i-1),allwater[m][1]+wbox_[1]*(j-1),allwater[m][2]+wbox_[2]*(k-1)));
                        water->push_back(Vector(allwater[m+1][0]+wbox_[0]*(i-1),allwater[m+1][1]+wbox_[1]*(j-1),allwater[m+1][2]+wbox_[2]*(k-1)));
                        water->push_back(Vector(allwater[m+2][0]+wbox_[0]*(i-1),allwater[m+2][1]+wbox_[1]*(j-1),allwater[m+2][2]+wbox_[2]*(k-1)));
                       // cout << "after wrap" << endl;
                        //cout << allwater[m][0]+wbox_[0]*(i-1) << "  "<<allwater[m][1]+wbox_[1]*(j-1)<< "  "<<allwater[m][2]+wbox_[2]*(k-1)<<endl;
                       // cout << allwater[m+1][0]+wbox_[0]*(i-1) << "  "<<allwater[m+1][1]+wbox_[1]*(j-1)<< "  "<<allwater[m+1][2]+wbox_[2]*(k-1)<<endl;
                       // cout << allwater[m+2][0]+wbox_[0]*(i-1) << "  "<<allwater[m+2][1]+wbox_[1]*(j-1)<< "  "<<allwater[m+2][2]+wbox_[2]*(k-1)<<endl;
                      
                      }//  cout<<"i   "<<i<<"   j   "<<j<<"   k  "<<k<<"   n   "<<endl;                  
                    }
                }
            }
        }
    } 
    cout << "size of waterlist  " << water->size()<< endl;   
}
