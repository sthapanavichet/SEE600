#include <iostream>
#include "AVLTree.h"

// Task 14: Maximum Size Test for AVL Tree on Linux
// Continuously inserts nodes until a std::bad_alloc exception is thrown.
void testMaximumSizeAVL()
{
    cout << "\nLinux AVL Tree Maximum Size Test:" << endl;
    AVL tree; // Use your AVL tree class
    try
    {
        for (int i = 0;; ++i)
        {
            EmployeeInfo emp = {50000, 30, i, 100000000 + i};
            tree.insert(emp);
            if (i % 100000 == 0)
            {
                cout << "Inserted " << i << " nodes..." << endl;
            }
        }
    }
    catch (const bad_alloc &)
    {
        cout << "Maximum size reached (std::bad_alloc caught) for AVL tree." << endl;
    }
}

int main()
{
    cout << "Starting AVL Tree Maximum Size Test...\n";
    size_t memoryLimitMB = 512; // Set a memory limit in MB
    limitMemory(memoryLimitMB);
    testMaximumSizeAVL();
    return 0;
}
