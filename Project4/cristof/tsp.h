#ifndef TSP_H_INCLUDED
#define TSP_H_INCLUDED

#include "cristof.h"

class TSP{

    private:
        Cristof *cris;
        int length;
    public:
        TSP(int length);
        ~TSP();
        void runTSP(int **graph);
};


#endif // TSP_H_INCLUDED
