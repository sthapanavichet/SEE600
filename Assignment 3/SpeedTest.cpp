#include <iostream>
#include <iomanip>
#include <map>
#include "AVLTree.h"
#include "timer.h"

using namespace std;

void testSpeedSearchMap()
{
    cout << "\nLinux std::map Worst-case Search Speed Test:" << endl;
    map<int, EmployeeInfo> empMap;
    const int iterations = 100000;

    // Insert sorted keys
    for (int i = 0; i < iterations; ++i)
    {
        EmployeeInfo emp = {50000, 30, i, 100000000 + i};
        empMap[emp.sin] = emp;
    }

    Timer timer;
    timer.start();

    auto it = empMap.find(100000000);

    timer.stop();
    double elapsed = timer.currtime();

    cout << fixed << setprecision(9);
    if (it == empMap.end())
        cout << "Key not found in std::map." << endl;
    else
        cout << "std::map search completed in " << elapsed << " seconds." << endl;
}

void testSpeedSearchAVL()
{
    cout << "\nLinux AVL Tree Worst-case Search Speed Test:" << endl;
    AVL tree;
    const int iterations = 100000;

    // Insert nodes into the AVL tree
    for (int i = 0; i < iterations; ++i)
    {
        EmployeeInfo emp = {50000, 30, i, 100000000 + i};
        tree.insert(emp);
    }

    Timer timer;
    timer.start();

    node *foundNode = tree.Find(tree.GetRoot(), 100000000);

    timer.stop();
    double elapsed = timer.currtime();

    cout << fixed << setprecision(9);
    if (!foundNode)
        cout << "Key not found in AVL tree." << endl;
    else
        cout << "AVL tree search completed in " << elapsed << " seconds." << endl;
}

int main()
{
    cout << "Starting Speed Search Tests...\n";
    testSpeedSearchMap();
    testSpeedSearchAVL();
    return 0;
}
