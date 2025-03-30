#include <iostream>
#include "AVLTree.h"

using namespace std;

// Task 12: Maximum Size Test for std::map on Linux
// This test continuously inserts entries until a std::bad_alloc exception is thrown.
void testMaximumSizeMap()
{
    cout << "Linux std::map Maximum Size Test:" << endl;
    map<int, EmployeeInfo> empMap;
    try
    {
        for (int i = 0;; ++i)
        {
            EmployeeInfo emp = {50000, 30, i, 100000000 + i};
            empMap[emp.sin] = emp;
            if (i % 100000 == 0)
            {
                cout << "Inserted " << i << " items..." << endl;
            }
        }
    }
    catch (const bad_alloc &)
    {
        cout << "Maximum size reached (std::bad_alloc caught) for std::map." << endl;
    }
}

int main()
{
    cout << "Starting Map Maximum Size Test...\n";
    size_t memoryLimitMB = 512; // Set a memory limit in MB
    limitMemory(memoryLimitMB);
    testMaximumSizeMap();
    return 0;
}