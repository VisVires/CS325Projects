#include "cristof.h"

cristof::cristof(int n)
{
    //create graph size of number of nodes
    graph = new int*[n];
    for (int i = 0; i < n; i++) {
        //create multidimensional graph
        graph[i] = new int[n];
        //initialize graph
        for (int j = 0; j < n; j++)
            graph[i][j] = 0;
	}

	//adjacency list for mst T
    mst = new vector<int> [n];
}

cristof::~cristof()
{
    delete[] graph;
    delete[] mst;
}

//http://www.geeksforgeeks.org/greedy-algorithms-set-5-prims-minimum-spanning-tree-mst-2/
void cristof::primMST(int graph[V][V]){

    int currMst[V];     //holds MST
    int key[V];         //holds current key
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

    //move mst to mst matrix and build adjacency list
    for (int start = 0; start < n; start++){
        int last = currMst[start];
        //if not root
        if(last != -1){
            //key each value to it's adjacent edge
            mst[start].push_back(last);
            mst[last].push_back(start);
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

void cristof::findOddDegree(){
    for (int i = 0; i < nodes; i++){
        if(())
    }

}

void cristof::printMST(){

}
