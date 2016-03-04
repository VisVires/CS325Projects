#ifndef CRISTOF_H
#define CRISTOF_H
#include <limits>
#include <cmath>
#include <vector>
#include <iostream>
#include <iterator>

using std::cin;
using std::cout;
using std::endl;
using std::vector;


class Cristof
{
    private:
        int n;

    public:
        vector<int>odds;
        vector<int> *mst;
        int **graph;
        int **tsp;
        Cristof(int n);
        ~Cristof();
        void primMST(int **graph);
        int minKey(int key[], bool setMst[]);
        void findOddDegree();
        void printMST();
        void printOdds();

};

#endif // CRISTOF_H
