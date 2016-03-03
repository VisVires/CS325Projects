#ifndef CRISTOF_H
#define CRISTOF_H
#include <climits>
#include <cmath>


class cristof
{
    private:

    public:
        cristof();
        ~cristof();
        void primMST(int graph[][]);
        int minKey(int key[], bool setMst[]);
        void printMST();

};

#endif // CRISTOF_H
