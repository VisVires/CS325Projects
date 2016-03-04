#ifndef CRISTOF_H
#define CRISTOF_H
#include <climits>
#include <cmath>


class cristof
{
    private:
        int n;

    public:
        vector<int>odds;
        vector<int> *mst;
        int **graph;
        int **tsp;
        cristof();
        ~cristof();
        void primMST(int graph[][]);
        int minKey(int key[], bool setMst[]);
        void findOddDegree();
        void printMST();

};

#endif // CRISTOF_H
