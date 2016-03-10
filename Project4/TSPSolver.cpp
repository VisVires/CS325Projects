#include "TSPLibFunctions.h"
#include <iostream>
#include <string>
#include <time.h>
#include <stdlib.h>


int main(int argc, char* argv[])
{
	clock_t t1, t2;
	srand(time(NULL));
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
		TSPtour myTour;
		myTour.length = myAdjMatrix.length;
		myTour.tour = new int[myTour.length];


		//Initilize variables for generating multiple greedy solutions
		int greedyTime = 100;
		int timeOPT1 = greedyTime + 60;
		int timeOPT2 = 180 - timeOPT1;
		if (myTour.length > 1000){
			greedyTime = 60;
			timeOPT1 = greedyTime + 60;
			timeOPT2 = 180 - timeOPT1;
		}
		TSPtour newTour;
		int cycles = 0;
		int best = 999999999;
		std::cout << "Generating a greedy solution" << std::endl;
		do{
			cycles++;
			//newTour = greedyInsertionVerTwo(myAdjMatrix);
			newTour = greedyInsertion(myAdjMatrix);
			int dist = calcTourLen(newTour, myAdjMatrix);
			if (dist < best)
			{
				best = dist;
				for (int i = 0; i < myTour.length; i++)
				{
					myTour.tour[i] = newTour.tour[i];
				}
			}
			t2 = clock();
		} while ((((double)t2 - (double)t1) / CLOCKS_PER_SEC) < greedyTime);
		std::cout << "Number of cycles: " << cycles << std::endl;
		std::cout << "Run time so far: " << ((double)t2 - (double)t1) / CLOCKS_PER_SEC << " seconds" << std::endl;
		std::cout << "The tour lenght is: " << calcTourLen(myTour, myAdjMatrix) << std::endl;
		std::cout << "Running optimization" << std::endl;
		
		myTour = SimulatedAnnealingVTwo(myTour, myAdjMatrix, t1, t2, timeOPT1);
		std::cout << "The tour lenght is: " << calcTourLen(myTour, myAdjMatrix) << std::endl;
		
		myTour = twoOPT(myTour, myAdjMatrix, t1, t2, timeOPT2);
		std::cout << "The tour lenght is: " << calcTourLen(myTour, myAdjMatrix) << std::endl;
		outputTourToFile(fileName, myTour, myAdjMatrix);
		t2 = clock();
		std::cout << "Solution was output to file.\nTotal run time was: " << ((double)t2 - (double)t1) / CLOCKS_PER_SEC << " seconds" << std::endl;
	}
	return 0;
}