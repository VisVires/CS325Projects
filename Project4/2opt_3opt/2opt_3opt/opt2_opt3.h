#ifndef OPT2_OPT3_H
#define OPT2_OPT3_H
#include <limits>
#include <cmath>
#include <vector>
#include <iostream>
#include <iterator>
#include <stack>

#pragma once
#include <string>

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::stack;

//TSPtour opt2(TSPadjMatrix);
//TSPtour opt3(TSPadjMatrix);

struct TSPadjMatrix{
	int** adjMatrix;
	int length;
};

struct TSPmap{
	int** map;
	int length;
};

struct TSPtour{
	int* tour;
	int length;
};


int calcTourLen(TSPtour, TSPadjMatrix);
TSPtour opt2Swap(TSPtour, int, int);

#endif // OPT2_OPT3_H
