#include "cristof.h"

cristof::cristof()
{

}

cristof::~cristof()
{
    //dtor
}

//http://www.geeksforgeeks.org/greedy-algorithms-set-5-prims-minimum-spanning-tree-mst-2/
void cristof::primMST(int graph[V][V]){

    int currMst[V];     //holds MST
    int key[V];         //
    bool setMst[V];     //set of vertices not in MST yet

    //initialize all keys to infinity and bool in set to false
    for(int v = 0; v < V; v++){
        key[v] = INT_MAX;
        setMst[v] = false;
    }

    key[0] = 0;         //first vertex
    currMst[0] = -1;    //root of MST is first node

    for (int num = 0; num < V - 1; num++){
        //pick lowest key vertex not yet in the MST
        int low = minKey(key, setMst);
        //add to chosen in set
        setMst[low] = true;
        //check adjacent vertices that have not been picked
        //and add to key
        for (v = 0; v < V; v++){
            if (graph[low][v] && setMst[v] == false && graph[low][v] < key[v])
                currMst[v] = low;
                key[v] = graph[low][v];
        }

    }
}

//find vertex from those not yet in MST with min value
int cristof::minKey(int key[], bool setMst[]){
    //initialize min as infinity
    int min = INT_MAX, min_index;
    for (int v = 0; v < V; v++)
        if(setMst[v] == false && key[v] < min)
            min = key[v];
            min_index = v;
    return min_index;
}

void cristof::printMST(){

}
