#ifndef AVLTREE_H
#define AVLTREE_H

#include <iostream>
#include <fstream>
#include <sys/resource.h> // For memory limit

struct EmployeeInfo
{
    int salary;
    int age;
    int emplNumber;
    int sin; // Social Insurance Number (Search Key)
};

struct node
{
    EmployeeInfo empl;
    node *left;
    node *right;
    int height;
};

class AVL
{
private:
    node *root;

    void makeEmpty(node *t);
    int max(int a, int b);
    int min(int a, int b);
    node *insert(EmployeeInfo empl, node *t);
    node *singleRightRotate(node *&t);
    node *singleLeftRotate(node *&t);
    node *doubleLeftRotate(node *&t);
    node *doubleRightRotate(node *&t);
    node *findMin(node *t);
    node *findMax(node *t);
    node *remove(int sin, node *t);
    int height(node *t);
    int getBalance(node *t);
    void inorder(node *t);
    std::ofstream outfile;

public:
    AVL();
    void insert(EmployeeInfo empl);
    void remove(int sin);
    void display();
    node *GetRoot();
    node *Find(node *node, int sin);
};

void limitMemory(size_t maxMemoryMB);

#endif // AVLTREE_H
