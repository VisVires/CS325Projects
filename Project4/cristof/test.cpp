#include "cristof.h"
#include <string>
#include <iostream>
using std::string;
using std::cout;
using std::cin;
using std::endl;

int main(){
    int n = 5;
    int graph[][5] = {{0, 2, 0, 6, 0},
                      {2, 0, 3, 8, 5},
                      {0, 3, 0, 0, 7},
                      {6, 8, 0, 0, 9},
                      {0, 5, 7, 9, 0},
                     };
    Cristof *cris = new Cristof(5);
    // make graph
    cris->primMST((int**)graph, n);
return 0;

}
