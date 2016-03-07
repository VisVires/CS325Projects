#include "tsp.h"

TSP::TSP(int length){
    this->cris = new Cristof(length);
    this->length = length;
}

TSP::~TSP(){

}

void TSP::runTSP(int **graph){
    cris->primMST(graph, length);
}
