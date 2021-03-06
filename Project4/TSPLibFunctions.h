#pragma once

#include <string>
#include <stdlib.h>
#include <time.h>

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
TSPtour greedyInsertionVerTwo(TSPadjMatrix);

//Optimization Functions
TSPtour SimulatedAnnealing(TSPtour, TSPadjMatrix);
TSPtour twoOPT(TSPtour, TSPadjMatrix, clock_t, clock_t, int);
TSPtour SimulatedAnnealingVTwo(TSPtour, TSPadjMatrix, clock_t, clock_t, int);