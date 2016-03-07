#include "tsp.h"

TSP::TSP(int length){
    this->cris = new Cristof(length);
    this->length = length;
}

TSP::~TSP(){
    delete cris;
}

void TSP::runTSP(int **graph){
    cout << "Finding MST Tree" << endl;
    cris->primMST(graph, length);
    cout << endl;
    cout << "Creating Min Perfect Tree" << endl;
    cris->minPerfect();
    cout << endl;
    cout << "Running Euler Path:" << endl;
    cris->eulerPath(path);
    cout << endl;
    cout << "Running Hamilton Path" << endl;
    cris->hamiltonPath(path);
    cout << endl;

}
