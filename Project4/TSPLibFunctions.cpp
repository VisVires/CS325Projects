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

TSPtour SimulatedAnnealing(TSPtour tour, TSPadjMatrix adjM)
{
	double maxTemp = 150;
	double temperature = maxTemp;
	double coolingRate = 0.999999;
	double minTemp = 1;
	int iteration = 0;
	int cycles = 10000000;
	int curDist = calcTourLen(tour, adjM);
	int lastDist = curDist;
	int bestDist = curDist;
	srand(time(NULL));
	TSPtour tempTour;
	tempTour.length = tour.length;
	tempTour.tour = new int[tour.length];
	for (int j = 0; j < tour.length; j++)
	{
		tempTour.tour[j] = tour.tour[j];
	}
	closeCities closeBy = genCloseByCities(adjM);
	int improvements = 0;
	for (int i = 0; i < cycles; i++)
	{
		//pick cities to swap
		int city = rand() % adjM.length;
		int near;
		do{
			near = closeBy.closeByCities[city][rand() % closeBy.numCloseBy];
		} while (city == near);
		//std::cout << "City = " << city << " Near = " << near << std::endl;
		int cityIndex, nearIndex;
		//Find indexes
		//std::cout << "Loop";
		for (int j = 0; j < tempTour.length; j++)
		{
			if (tempTour.tour[j] == city){
				cityIndex = j;
				//std::cout << "City: " << j;
			}
			else if (tempTour.tour[j] == near){
				nearIndex = j;
				//std::cout << "Near: " << j;
			}
		}
		//std::cout << std::endl;
		//swap
		tempTour.tour[cityIndex] = near;
		tempTour.tour[nearIndex] = city;
		curDist = calcTourLen(tempTour, adjM);
		//Move is better accept it
		if (curDist < lastDist)
		{
			
			improvements++;
			lastDist = curDist;
			if (curDist < bestDist)
			{
				
				bestDist = curDist;
				for (int j = 0; j < tour.length; j++)
				{
					tour.tour[j] = tempTour.tour[j];
				}
			}
		}
		//Move is worse accept maybe
		else if (exp(-(curDist - lastDist) / temperature) > (((double)rand()) / RAND_MAX))
		{
			lastDist = curDist;
		}
		//Move not accepted reverse it
		else
		{
			tempTour.tour[cityIndex] = city;
			tempTour.tour[nearIndex] = near;
		}

		//Cycle housekeeping
		iteration++;
		if (temperature > minTemp)
			temperature *= coolingRate;
		else
			temperature = minTemp;
	}
	std::cout << temperature << std::endl;
	return tour;
}

closeCities genCloseByCities(TSPadjMatrix adjM)
{
	int cityDepth = 0;
	if (adjM.length < 100)
		cityDepth = adjM.length;
	else if (adjM.length < 500)
		cityDepth = 100;
	else
		cityDepth = 100;

	int **closeCityList = new int*[adjM.length];
	for (int i = 0; i < adjM.length; i++)
	{
		closeCityList[i] = new int[cityDepth];
	}

	for (int i = 0; i < adjM.length; i++)
	{
		int added = 0;
		int largestSize = 0;
		int largestIndex;
		for (int j = 0; j < adjM.length; j++){
			if (added < cityDepth)
			{
				closeCityList[i][j] = j;
				added++;
				if (closeCityList[i][j] > largestSize)
				{
					largestSize = closeCityList[i][j];
					largestIndex = j;
				}
			}
			else
			{
				if (adjM.adjMatrix[i][j] < largestSize)
				{
					closeCityList[i][largestIndex] = j;
					largestSize = adjM.adjMatrix[i][closeCityList[i][0]];
					largestIndex = 0;
					for (int k = 0; k < cityDepth; k++)
					{
						if (adjM.adjMatrix[i][closeCityList[i][k]] > largestSize)
						{
							largestIndex = k;
							largestSize = adjM.adjMatrix[i][closeCityList[i][k]];
						}
					}
				}
			}
		}
	}
	closeCities closeBy;
	closeBy.closeByCities = closeCityList;
	closeBy.numberOfCities = adjM.length;
	closeBy.numCloseBy = cityDepth;
	return closeBy;
}

TSPtour twoOPT(TSPtour tour, TSPadjMatrix adjM)
{
	//Create a temp to hold the tour
	TSPtour tourTemp;
	tourTemp.length = tour.length + 1;
	tourTemp.tour = new int[tourTemp.length];
	//Copy the tour
	for (int i = 0; i < tour.length; i++)
	{
		tourTemp.tour[i] = tour.tour[i];
	}
	//Append the first city to the position after the last city to make it easier to consider the edge between the last and first city.
	tourTemp.tour[tourTemp.length - 1] = tour.tour[0];
	int iteration = 0;
	int minChange = 0;
	
	do{
		int mini = 0;
		int minj = 0;
		minChange = 1;
		iteration += 1;
		
		for (int i = 0; i < tourTemp.length - 4; i++)
		{
			for (int j = i + 2; j < tourTemp.length - 2; j++)
			{
				int change = adjM.adjMatrix[tourTemp.tour[i]][tourTemp.tour[j]] + adjM.adjMatrix[tourTemp.tour[i + 1]][tourTemp.tour[j + 1]] - adjM.adjMatrix[tourTemp.tour[i]][tourTemp.tour[i + 1]] - adjM.adjMatrix[tourTemp.tour[j]][tourTemp.tour[j + 1]];
				if (minChange > change)
				{
					minChange = change;
					mini = i + 1;
					minj = j;
				}
			}
		}
		std::cout << calcTourLen(tourTemp, adjM) << ": " << iteration << " i:" << mini << " j: " << minj << " change: " << minChange << std::endl;
		for (int k = 0; k < floor((minj - mini + 1) / 2); k++)
		{
			int temp = tourTemp.tour[k + mini];
			tourTemp.tour[k + mini] = tourTemp.tour[minj - k];
			tourTemp.tour[minj - k] = temp;
		}
		if (!(minChange < 0))
			break;
	} while (minChange < 0);
	
	//copy improved tour back
	for (int i = 0; i < tour.length; i++)
	{
		tour.tour[i] = tourTemp.tour[i];
	}
	return tour;
}