#ifndef TSP_H_INCLUDED
#define TSP_H_INCLUDED

#include "cristof.h"

class TSP{

    private:
        Cristof *cris;
        int length;
        vector<int> path;
    public:
        TSP(int length);
        ~TSP();
        vector<int>& runTSP(int **graph);
};


#endif // TSP_H_INCLUDED
