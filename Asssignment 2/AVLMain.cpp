#include <iostream>
#include <fstream>
#include <map>
#include <stdexcept>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include "timer.h" // Provided Timer
#include "AVLTree.h"

using namespace std;

const int NUM = 2000000;
ofstream outfile;
int treeHeight = 0;

int main()
{
    AVL t;
    int sinArray[NUM];
    for (int i = 0; i < NUM; ++i)
        sinArray[i] = 100000000 + i;
    random_shuffle(&sinArray[0], &sinArray[NUM]);
    //	random_shuffle(begin(sinArray), end(sinArray));
    //	for (int i = 0; i < NUM; ++i) cout << "i:" << i << " sin:" << sinArray[i] << endl;
    for (int i = 0; i < NUM; ++i)
    {
        EmployeeInfo empl;
        empl.age = 25 + (i * 2) % 45;
        empl.salary = 50000 + (i * 10) % 100000;
        empl.emplNumber = i;
        empl.sin = sinArray[i];
        t.insert(empl);
    }
    outfile.open("inorder.txt");
    cout << "INORDER (NUM=" << NUM << ", height=" << t.GetRoot()->height << "): root node has sin:" << t.GetRoot()->empl.sin << endl
         << endl;
    outfile << "INORDER (NUM=" << NUM << ", height=" << t.GetRoot()->height << "): root node has sin:" << t.GetRoot()->empl.sin << endl
            << endl;
    t.display();
    outfile.close();
    cout << endl
         << "DONE" << endl
         << endl;

    srand(time(NULL));
    return 0;
}