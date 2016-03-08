#include "TSPLibFunctions.h"
#include <iostream>
#include <string>
#include <time.h>

int main(int argc, char* argv[])
{
	clock_t t1, t2;
	t1 = clock();
	if (argc < 2)
		std::cout << "TSPSolver [file name of problem] \n Program call must be made with the location of the problem" << std::endl;
	else
	{
		
		char* fileName = argv[1];
		std::cout << "Reading in file." << std::endl;
		TSPmap myMap = readFile(fileName);
		t2 = clock();
		std::cout << "File was read in. Taking: " << ((double)t2 - (double)t1) / CLOCKS_PER_SEC << " seconds" << std::endl;
		//printMap(myMap);
		std::cout << "Creating adjacency matrix" << std::endl;
		TSPadjMatrix myAdjMatrix = adjMatrixGenerator(myMap);
		t2 = clock();
		std::cout << "Adjacency matrix has been made. " << ((double)t2 - (double)t1) / CLOCKS_PER_SEC << " seconds" << std::endl;
		//printAdjMatrix(myAdjMatrix);
		std::cout << "Generating a greedy solution" << std::endl;
		TSPtour myTour = greedyInsertion(myAdjMatrix);
		t2 = clock();
		std::cout << "Run time so far: " << ((double)t2 - (double)t1) / CLOCKS_PER_SEC << " seconds" << std::endl;
		std::cout << "The tour lenght is: " << calcTourLen(myTour, myAdjMatrix) << std::endl;
		std::cout << "Running optimization" << std::endl;
		myTour = twoOPT(myTour, myAdjMatrix);
		myTour = SimulatedAnnealing(myTour, myAdjMatrix);
		t2 = clock();
		std::cout << "Run time so far: " << ((double)t2 - (double)t1) / CLOCKS_PER_SEC << " seconds" << std::endl;
		std::cout << "The tour lenght is: " << calcTourLen(myTour, myAdjMatrix) << std::endl;
		outputTourToFile(fileName, myTour, myAdjMatrix);
		t2 = clock();
		std::cout << "Solution was output to file.\nTotal run time was: " << ((double)t2 - (double)t1) / CLOCKS_PER_SEC << " seconds" << std::endl;
	}
	return 0;
}