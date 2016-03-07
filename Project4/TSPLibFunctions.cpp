#include "TSPLibFunctions.h"
#include <math.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>
#include <time.h>
#include <limits>
#include <algorithm>

TSPadjMatrix adjMatrixGenerator(TSPmap tspMap)
{
	int **matrix = new int*[tspMap.length];
	for (int i = 0; i < tspMap.length; i++)
		matrix[i] = new int[tspMap.length];
	
	for (int i = 0; i < tspMap.length; i++){
		for (int j = 0; j < tspMap.length; j++){
			
			double dist = sqrt(pow((tspMap.map[i][1] - tspMap.map[j][1]), 2) + pow(double(tspMap.map[i][2] - tspMap.map[j][2]), 2));
			matrix[i][j] = (int)round(dist);
		}
	}
	TSPadjMatrix adjM;
	adjM.adjMatrix = matrix;
	adjM.length = tspMap.length;

	return adjM;
}

void printAdjMatrix(TSPadjMatrix matrix)
{
	for (int i = 0; i < matrix.length; i++){
		for (int j = 0; j < matrix.length; j++){
			std::cout << matrix.adjMatrix[i][j] << ", ";
		}
		std::cout << std::endl;
	}
}

TSPmap readFile(std::string fileName)
{
	
	int city, x, y;
	TSPmap tspMap;
	std::ifstream input;
	
	//Count the number of lines in the file
	input.open(fileName);
	int length = 0;
	while (input >> city >> x >> y)
	{
		length++;
	}
	input.close();
	//Initilize the array for the map
	int **matrix = new int*[length];
	for (int i = 0; i < length; i++)
		matrix[i] = new int[3];
	//Read file to map
	input.open(fileName);
	length = 0;
	while (input >> city >> x >> y)
	{
		
		matrix[length][0] = city;
		matrix[length][1] = x;
		matrix[length][2] = y;
		length++;
	}
	input.close();

	tspMap.map = matrix;
	tspMap.length = length;
	
	return tspMap;
}

int calcTourLen(TSPtour tspTour, TSPadjMatrix adjM)
{
	int tourLen = 0;
	int **matrix = adjM.adjMatrix;
	//add the distance between the last and first city to complete the loop
	tourLen += matrix[tspTour.tour[0]][tspTour.tour[tspTour.length - 1]];
	for (int i = 0; i < tspTour.length - 1; i++)
	{
		tourLen += matrix[tspTour.tour[i]][tspTour.tour[i + 1]];
	}
	return tourLen;
}

void printMap(TSPmap tspMap)
{
	for (int i = 0; i < tspMap.length; i++){
		std::cout << tspMap.map[i][0] << ", " << tspMap.map[i][1] << ", " << tspMap.map[i][2] << std::endl;
	}
}


void outputTourToFile(std::string fileName, TSPtour tour, TSPadjMatrix adjM)
{
	std::ofstream output;
	output.open(fileName + ".tour");
	output << calcTourLen(tour, adjM) << "\n";
	for (int i = 0; i < tour.length; i++)
	{
		output << tour.tour[i] << "\n";
	}
	output.close();
}

TSPtour greedyInsertion(TSPadjMatrix adjM)
{
	std::vector<int> unVisited;
	for (int i = 0; i < adjM.length; i++)
	{
		unVisited.emplace_back(i);
	}
	int* tour = new int[adjM.length];
	int tourLength = 1;
	srand(time(NULL));
	int startCity = rand() % adjM.length;
	tour[0] = startCity;
	tour[1] = startCity;
	unVisited.erase(unVisited.begin() + startCity);
	int size = unVisited.size();
	for (int i = 0; i < size; i++)
	{
		int cityToVisitIndex = rand() % unVisited.size();
		int cityToVisit = unVisited[cityToVisitIndex];
		int minIndex = 0;
		int minLength = std::numeric_limits<int>::max();
		for (int j = 0; j < tourLength; j++)
		{
			int dist = adjM.adjMatrix[cityToVisit][tour[j]] + adjM.adjMatrix[cityToVisit][tour[j + 1]] - adjM.adjMatrix[tour[j+1]][tour[j]];
			if (dist < minLength)
			{
				minLength = dist;
				minIndex = j + 1;
				int cityIndex = cityToVisitIndex;
			}
		}
		//shift the tour
		for (int i = std::min(tourLength + 1, adjM.length); i > minIndex; i--)
		{
			tour[i] = tour[i - 1];
		}
		//insert into the tour
		tour[minIndex] = unVisited[cityToVisitIndex];
		unVisited.erase(unVisited.begin() + cityToVisitIndex);
		tourLength++;
	}
	TSPtour output;
	output.tour = tour;
	output.length = tourLength;
	return output;
}

TSPtour opt2(TSPtour existing_tour, TSPadjMatrix adjM){
    TSPtour new_tour;
    int iteration = 0;
    int best_distance = 0;
    int new_distance = 0;

    start_again:
        best_distance = calcTourLen(existing_tour, adjM);
        for (int i = 0; i < existing_tour.length - 1; i++) {
            for (int k = i + 1; k < existing_tour.length; k++) {
                new_tour = opt2Swap(existing_tour, i, k);
                new_distance = calcTourLen(new_tour, adjM);
                if (new_distance < best_distance) {
                   existing_tour = new_tour;
                   goto start_again;
               }
            }
        }

    std::cout << "Opt2 end of function";
}

TSPtour opt2Swap(TSPtour route, int i, int k) {
  TSPtour new_route = route;
  int tempK = k;
  //1. take route[1] to route[i-1] and add them in order to new_route
  for (int j = 1; j < route[i-1]; j++){
    new_route[j] = route[j];
  }

  //2. take route[i] to route[k] and add them in reverse order to new_route
  for(int j=i; j<k; j++){
    new_route[j] = route[tempK-1];
    tempK--; 
  }

  //3. take route[k+1] to end and add them in order to new_route
  for (int j = k+1; j < route.length; j++){
    new_route[j] = route[j];
  }

  return new_route;
}