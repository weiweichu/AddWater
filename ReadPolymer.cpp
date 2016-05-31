//
//  ReadPolymer.cpp
//  Solvation
//
//  Created by Weiwei Chu on 5/17/16.
//  Copyright (c) 2016 Weiwei Chu. All rights reserved.
//

#include "ReadPolymer.h"
sentence ReadDataFile::split(const string &s){
    sentence a;
    s_type i=0;
    while(i!=s.size()) {
        while (i!=s.size() && isspace(s[i])) {
            ++i;
        }
        
        s_type j=i;
        while (j!=s.size() && !isspace(s[j])) {
            ++j;
        }
        
        if(i!=j) {
            a.push_back(s.substr(i,j-i));
            i = j;
        }
    }
    return a;
}

void ReadDataFile::OutPolymer(atom *polymer,vector<double> *polymerbox){
    ifstream in(fname_);
    if (in.is_open()){
		cout << "file is open" << endl;
	}
    string line;
    int natom = 0;
    double xt,yt,zt;
    Vector pt;
    const string aa("Atoms");
    const string aas("atoms");
    const string imp("improper");
    sentence a;
    while (getline(in,line)) {
        a = split(line);
        if (a.size()!= 0){
            if ((a.size()==2) && (!a[1].compare(aas)) ){
				istringstream(a[0])>>natom;
            }
            if ((a.size()==3) && (!a[1].compare(imp))) {
                getline(in,line);
                getline(in,line);
                double b;
                a = split(line);
                istringstream(a[0])>>b;
                polymerbox->push_back(b);
                istringstream(a[1])>>b;
                polymerbox->push_back(b);
                getline(in,line);
                a = split(line);
                istringstream(a[0])>>b;
                polymerbox->push_back(b);
                istringstream(a[1])>>b;
                polymerbox->push_back(b);
                getline(in,line);
                a = split(line);
                istringstream(a[0])>>b;
                polymerbox->push_back(b);
                istringstream(a[1])>>b;
                polymerbox->push_back(b);
                
            }
            if (!a[0].compare(aa)) {
                break;
            }
        }
    }
    
    getline(in,line);
    for(int i=0;i<natom;i++){
        getline(in, line);
        a = split(line);
        istringstream(a[4])>>xt;
        istringstream(a[5])>>yt;
        istringstream(a[6])>>zt;
        //xt = atoi(a[4].c_str());
        //yt = atoi(a[5].c_str());
        //zt = atoi(a[6].c_str());
        polymer->push_back(Vector(xt,yt,zt));
        
    }
    
    
}

