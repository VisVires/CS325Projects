#include "cristof.h"

Cristof::Cristof(int length)
{
    //create graph size of number of nodes
    n = length;
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

Cristof::~Cristof()
{
    for(int i = 0; i < n; i++){
        delete[] graph[i];
    }
    delete [] graph;
    delete [] mst;
}

//http://www.geeksforgeeks.org/greedy-algorithms-set-5-prims-minimum-spanning-tree-mst-2/
void Cristof::primMST(int *tour[], int n){

    graph = tour;

    int currMst[n];     //holds MST
    int key[n];         //holds current key
    bool mstSet[n];     //set of vertices not in MST yet

    //initialize all keys to infinity and bool in set to false
    for(int v = 0; v < n; v++){
        key[v] = std::numeric_limits<int>::max();
        mstSet[v] = false;
    }

    key[0] = 0;         //first vertex
    currMst[0] = -1;    //root of MST is first node

    for (int num = 0; num < n - 1; num++){
        //pick lowest key vertex not yet in the MST
        int u = minKey(key, mstSet);
        //add to chosen in set
        mstSet[u] = true;
        //check adjacent vertices that have not been picked
        //and add to key
        for (int v = 0; v < n; v++){
            if (graph[u][v] && mstSet[v] == false && graph[u][v] < key[v]){
                currMst[v] = u;
                key[v] = graph[u][v];
            }
        }
    }
    for (int v1 = 0; v1 < n; v1++){
        int v2 = currMst[v1];
        //if not root
        if(v2 != -1){
            //key each value to it's adjacent edge
            mst[v1].push_back(v2);
            mst[v2].push_back(v1);
        }
    }
    cout << endl;
    printMST(currMst, n, graph);
    cout << endl;
    //move mst to mst matrix and build adjacency list
}


//find vertex from those not yet in MST with min value
int Cristof::minKey(int key[], bool setMst[]){
    //initialize min as infinity
    int min = std::numeric_limits<int>::max(), min_index;
    for (int v = 0; v < n; v++){
        if(setMst[v] == false && key[v] < min){
            min = key[v];
            min_index = v;
        }
    }
    return min_index;
}

//find all the nodes with odd degrees
void Cristof::oddDegree(){
    cout << "Printing Odd Degrees" << endl;
    for (unsigned int i = 0; i < n; i++){
        cout << i << " " << mst[i].size() << endl;
        //if vertex touches an odd number of edges add to odds
        if((mst[i].size()%2) != 0){
            odds.push_back(i);
        }
    }
}

//construct minimum weight perfect matching subtree from Odds
void Cristof::minPerfect(){
    //create odds vector
    odds.clear();
    oddDegree();
    //minimum weight variables
    int minimum, weight;
    //iterator for first node and tmp
    vector<int>::iterator tmp, first;
    //for each node in odds
    while(!odds.empty()){
        //set first to first remaining node
        first = odds.begin();
        //set curr to next item after first
        vector<int>::iterator curr = odds.begin() + 1;
        //set end to last item in odds
        vector<int>::iterator last = odds.end();
        //set weight to largest int possible
        weight = std::numeric_limits<int>::max();
        //until we go from current first to last
        while(curr != last){
            //if current node is of lower weight than current minimum, update current minimum
            if (graph[*first][*curr] < weight){
                weight = graph[*first][*curr];
                minimum = *curr;
                tmp = curr;
            }
            ++curr;
        }
        //complete matching tree
        mst[*first].push_back(minimum);
        mst[minimum].push_back(*first);
        //destroy iterators
        odds.erase(tmp);
        odds.erase(first);
    }
    printMST2();
}

void Cristof::setBest(int b){
    best = b;
}


//http://www.graph-magics.com/articles/euler.php
void Cristof::eulerPath(vector<int> &ePath){

    //copy mst to temp vector
    vector<int> *temp = new vector<int> [n];
    for (int i = 0; i < n; i++){
        temp[i].resize(mst[i].size());
        temp[i] = mst[i];
    }
    best = 2;
    //start with empty stack and empty path
    ePath.clear();
    stack<int> stk;
    //choose any start because there are no odd vertices
    int curr = best;
    //while curr vertex has no more neighbors
    while(!stk.empty() || temp[curr].size() > 0){
        //If curr has no out-going edges, add to path
        if(temp[curr].size() == 0) {
            ePath.push_back(curr);
            //remove last vertex from stack and set as curr
            int last = stk.top();
            stk.pop();
            curr = last;
        }
        //else add vertex to stack with a neighbor
        else{
            //add vertex to stack
            stk.push(curr);
            //take an adjacent neighbor
            int neighbor = temp[curr].back();
            //remove edge b/w neighbor and vertex
            temp[curr].pop_back();
            //go through neighbors neighbors
            for (unsigned int i = 0; i < temp[neighbor].size(); i++){
                //remove curr from neighbor list
                if (temp[neighbor][i] == curr){
                    temp[neighbor].erase(temp[neighbor].begin() + i);
                    break;
                }
            }
            //set curr as neighbor
            curr = neighbor;
        }
        //add final vertex to path
        ePath.push_back(curr);
    }
    printPath(ePath);
}

//http://www.csd.uoc.gr/~hy583/papers/ch14.pdf
void Cristof::hamiltonPath(vector<int> &ePath){
    //remove duplicate nodes from Euler
    bool seen[n];
    //set all values as false
    for(int i = 0; i > n; i++){
        seen[i] = false;
    }

    vector<int>::iterator start,curr = ePath.begin();
    vector<int>::iterator next = ePath.begin() + 1;
    //set first node as visited
    seen[0] = true;

    //until we reach the end of the list
    while(next != ePath.end()){
        //if node not yet reached
        if(!seen[*next]){
            //add edge to total distance
            dist += graph[*curr][*next];
            //move curr to next node
            curr = next;
            //set curr to true
            seen[*curr] = true;
            //move next node
            next = curr + 1;
        }
        //else remove duplicate from path
        else {
            next = ePath.erase(next);
        }
    }
    //add total distance back to root
    dist += graph[*curr][*next];
    printPath(ePath);
}

int Cristof::getDist(){
    return dist;
}

void Cristof::printPath(vector<int> &ePath){
    for (int i = 0; i < ePath.size(); i++){
        cout << ePath[i] << endl;
    }
}


void Cristof::printMST(int *currMst, int n, int **graph)
{
    printf("Edge   Weight\n");
    for (int i = 1; i < n; i++)
        printf("%d - %d    %d \n", currMst[i], i, graph[i][currMst[i]]);
    cout << endl;
    printMST2();
}

void Cristof::printMST2(){
    for (int i = 0; i < n; i++){
        cout << "Vertex: " << i;
        cout << " Adjacent Vertices: ";
        for (unsigned int j = 0; j < mst[i].size(); ++j){
                cout << mst[i][j] << " ";
        }
        cout << endl;
    }
}


void Cristof::printOdds(){
    cout << endl;
    for (unsigned int i = 0; i < odds.size(); i++){
            cout << odds[i] << endl;
    }
}
