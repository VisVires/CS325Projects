#include "cristof.h"

Cristof::Cristof(int n)
{
    //create graph size of number of nodes
    graph = new int*[n];
    for (auto i = 0; i < n; i++) {
        //create multidimensional graph
        graph[i] = new int[n];
        //initialize graph
        for (int j = 0; j < n; j++)
            graph[i][j] = 0;
	}

	//adjacency list for mst T
    mst = new vector<int> [n];
}

Cristof::~Cristof()
{
    delete[] graph;
    delete[] mst;
}

//http://www.geeksforgeeks.org/greedy-algorithms-set-5-prims-minimum-spanning-tree-mst-2/
void Cristof::primMST(int **graph){

    int currMst[n];     //holds MST
    int key[n];         //holds current key
    bool setMst[n];     //set of vertices not in MST yet

    //initialize all keys to infinity and bool in set to false
    for(auto v = 0; v < n; v++){
        key[v] = std::numeric_limits<int>::max();
        setMst[v] = false;
    }

    key[0] = 0;         //first vertex
    currMst[0] = -1;    //root of MST is first node

    for (auto num = 0; num < n - 1; num++){
        //pick lowest key vertex not yet in the MST
        int low = minKey(key, setMst);
        //add to chosen in set
        setMst[low] = true;
        //check adjacent vertices that have not been picked
        //and add to key
        for (auto v = 0; v < n; v++){
            if (graph[low][v] && setMst[v] == false && graph[low][v] < key[v])
                currMst[v] = low;
                key[v] = graph[low][v];
        }

    }

    //move mst to mst matrix and build adjacency list
    for (auto start = 0; start < n; start++){
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
int Cristof::minKey(int key[], bool setMst[]){
    //initialize min as infinity
    int min = std::numeric_limits<int>::max(), min_index;
    for (auto v = 0; v < n; v++){
        if(setMst[v] == false && key[v] < min){
            min = key[v];
            min_index = v;
        }
    }
    return min_index;
}

//find all the nodes with odd degrees
void Cristof::findOddDegree(){
    for (unsigned int i = 0; i < odds.size(); i++){
        //if vertex touches an odd number of edges add to odds
        if((mst[i].size()%2) != 0){
            odds.push_back(i);
        }
    }
}

//construct minimum weight perfect matching subtree from Odds
void Cristof::minPerfect{

    //minimum weight variables
    int minimum, weight;

    //iterator for first node and tmp
    vector<int>::iterator tmp, first;

    //create odds vector
    findOddDegree();

    //for each node in odds
    while(!odds.empty()){
        //set first to first remaining node
        first = odds.begin()
        //set curr to next item after first
        vector<int>::iterator curr = odds.begin() + 1
        //set end to last item in odds
        vector<int>::iterator end = odds.end()
        //set weight to largest int possible
        weight = std::numeric_limits<int>::max();
        //until we go from current first to last
        while(curr != end){
            //if current node is of lower weight than current minimum, update current minimum
            if (graph[*first][*curr] < weight){
                weight = graph[*first][*curr];
                minimum = *curr
                tmp = *curr
            }
        }
        //complete matching tree
        mst[*first].push_back(minimum);
        mst[minimum].push_back(*first);
        //destroy iterators
        odds.erase(tmp);
        odds.erase(first);
    }
}



void Cristof::printMST(){
    for (auto i = 0; i < n; i++){
            for (auto j = 0; j < n; j++){
                cout << mst[i][j];
            }
            cout << endl;
    }
}

void Cristof::printOdds(){
    for (auto i = 0; i < n; i++){
            cout << odds[i] < endl;
    }
}
