#ifndef CRISTOF_H
#define CRISTOF_H
#include <limits>
#include <cmath>
#include <vector>
#include <iostream>
#include <iterator>
#include <stack>

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
        void minPerfect();
        void setBest(int best);
        void eulerPath(vector<int> &);
        void printMST();
        void printOdds();

};

#endif // CRISTOF_H
