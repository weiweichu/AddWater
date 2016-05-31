/*
 * test.cxx
 * 
 * Copyright 2016 weiwei <weiwei@xps8700>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <map>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <sstream>
#include "Vector.h"

using namespace std;
typedef vector<double> ma;


class test{
	public:
	test(){};
	void out(ma *p){
		p->push_back(1.0);
		p->push_back(2.0);
	}
};

int main(int argc, char **argv)
{
	vector<Vector> a;
	vector<vector<Vector> > b;
	b.resize(9,a);
	for (int i=0;i<9;i++){
		b[i].push_back(Vector(i,i,i));
		b[i].push_back(Vector(i+1,i+1,i+1));
	}
	cout<<b[1][0][0]<<"  "<<b[1][1][1]<<endl;
	
}

