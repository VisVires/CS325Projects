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
         struct Tour{
            int length;
            int **tour;
        };
    public:

        int **graph;
        vector<int>odds;
        vector<int> *mst;
        int **tsp;
        Cristof(int);
        ~Cristof();
        void primMST(int **tour);
        int minKey(int key[], bool setMst[]);
        void findOddDegree();
        void minPerfect();
        void setBest(int best);
        void eulerPath(vector<int> &);
        void hamiltonPath(vector<int> &, int &);
        void printMST();
        void printOdds();
};

#endif // CRISTOF_H
