#include "cristof.h"
#include <string>
#include <iostream>
using std::string;
using std::cout;
using std::cin;
using std::endl;

#define V 5

int main(){

    int graph[5][5] = {{0, 2, 0, 6, 0},
                      {2, 0, 3, 8, 5},
                      {0, 3, 0, 0, 7},
                      {6, 8, 0, 0, 9},
                      {0, 5, 7, 9, 0},
                     };
    Cristof cris = new Cristof(5)
    // make graph
    cris.primMST(graph);
return 0;

}
