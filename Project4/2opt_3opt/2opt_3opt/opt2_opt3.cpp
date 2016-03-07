#include "opt2_opt3.h"
#include <math.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>
#include <time.h>
#include <limits>
#include <algorithm>


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

    //std::cout << "Opt2 end of function";
}

TSPtour opt2Swap(TSPtour route, int i, int k) {
  TSPtour new_route = route;
  int tempK = k;
  //1. take route[1] to route[i-1] and add them in order to new_route
  for (int j = 1; j < route[i-1]; j++){
    //new_route[j] = route[j];
  }

  //2. take route[i] to route[k] and add them in reverse order to new_route
  for(int j=i; j<k; j++){
    //new_route[j] = route[tempK-1];
    tempK--; 
  }

  //3. take route[k+1] to end and add them in order to new_route
  for (int j = k+1; j < route.length; j++){
    //new_route[j] = route[j];
  }

  return new_route;
}


/*
def twoOpt(tour, adjMatrix):
    tour.append(tour[0])
    iteration = 0
    while True:
        print(str(iteration) + ": " + str(calcTourLen(tour,adjMatrix)))
        iteration += 1
        minChange = 0
        for i in range(len(tour) - 3):
            for j in range(i + 2, len(tour) - 2):
                change = adjMatrix[tour[i]][tour[j]] + adjMatrix[tour[i+1]][tour[j+1]] - adjMatrix[tour[i]][tour[i+1]] - adjMatrix[tour[j]][tour[j+1]]
                if minChange > change:
                    minChange = change
                    mini = i+1
                    minj = j
         #swap edges
        for k in range(int(math.floor( (minj - mini + 1) / 2 ))):
            temp = tour[k + mini]
            tour[k + mini] = tour[minj - k]
            tour[minj - k]  = temp

        if not(minChange < 0):
            tour.remove(tour[0])
            return tour

TSPtour opt2(TSPtour existing_tour, TSPadjMatrix adjM){
  int iteration = 0;

  while
}
*/
/*
   repeat until no improvement is made {
       start_again:
       best_distance = calculateTotalDistance(existing_route)
       for (i = 0; i < number of nodes eligible to be swapped - 1; i++) {
           for (k = i + 1; k < number of nodes eligible to be swapped; k++) {
               new_route = 2optSwap(existing_route, i, k)
               new_distance = calculateTotalDistance(new_route)
               if (new_distance < best_distance) {
                   existing_route = new_route
                   goto start_again
               }
           }
       }
   }
*/
/*
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
  TSPtour new_route;
  int tempK = k;
  //1. take route[1] to route[i-1] and add them in order to new_route
  for (int j = 1; j < route.length[i-1]; j++){
    new_route[j] = route.[j];
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
*/


/*
TSPtour opt3(TSPadjMatrix adjM){


    cout << "Opt3 end of function";
}
*/

/* Functions from other code */
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

/*******Reference******/
//https://en.wikipedia.org/wiki/2-opt
/**********************/
