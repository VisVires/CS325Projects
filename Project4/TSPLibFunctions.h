#pragma once

#include <string>

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

struct closeCities{
	int** closeByCities;
	int numberOfCities;
	int numCloseBy;
};

//AdjMatrix Functions
TSPadjMatrix adjMatrixGenerator(TSPmap);
void deleteAdjMatrix(TSPadjMatrix);
void printAdjMatrix(TSPadjMatrix);

//Map Functions
TSPmap readFile(std::string);
void deleteMap(TSPmap tspMap);
void printMap(TSPmap);

//Utility functions
int calcTourLen(TSPtour, TSPadjMatrix);
void outputTourToFile(std::string, TSPtour, TSPadjMatrix);
closeCities genCloseByCities(TSPadjMatrix);

//Heruristic functions
TSPtour greedyInsertion(TSPadjMatrix);

//Optimization Functions
TSPtour SimulatedAnnealing(TSPtour, TSPadjMatrix);
TSPtour twoOPT(TSPtour, TSPadjMatrix);