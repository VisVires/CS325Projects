#include "cristof.h"
#include <string>
#include <iostream>
#include <fstream>
using std::string;
using std::cout;
using std::cin;
using std::endl;
using std::ifstream;

int** create2dMatrix(int length);

int main(){
    int n = 5;
    ifstream myfile;
    int** graph2 = create2dMatrix(n);
    myfile.open("test.txt");
    if(!myfile)
    {
        cout << "File does not exist" << endl;
        return 1;
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            myfile >> graph2[i][j];
        }
    }
    myfile.close();
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cout << graph2[i][j] << " ";
        }
        cout << endl;
    }
    Cristof *cris = new Cristof(n);
    cris->primMST(graph2, n);

return 0;

}

int** create2dMatrix(int length) {
    int** array = new int*[length];
    for (int row=0; row < length; row++) {
        array[row] = new int[length];
    }
    return array;
}


