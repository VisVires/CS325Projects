#ifndef CRISTOF_H
#define CRISTOF_H
#include <limits>
#include <cmath>
#include <vector>
#include <iostream>
#include <iterator>
#include <stack>
#include <stdio.h>

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::stack;


class Cristof
{
    private:
        int n;
        int best;
        int dist = 0;
    public:
        int **graph;
        vector<int>odds;
        vector<int> *mst;
        int **tsp;
        Cristof(int);
        ~Cristof();
        void primMST(int *tour[], int);
        int minKey(int key[], bool setMst[]);
        void oddDegree();
        void minPerfect();
        void setBest(int best);
        void eulerPath(vector<int> &);
        void hamiltonPath(vector<int> &);
        void printMST(int *parent, int n, int **graph);
        void printMST2();
        void printOdds();
        void printPath(vector<int> &);
};

#endif // CRISTOF_H
