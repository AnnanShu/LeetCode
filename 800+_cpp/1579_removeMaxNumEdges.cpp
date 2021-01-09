#include<iostream>
#include<vector>
#include<stdlib.h>
using namespace std;

class DSU{
public:
    DSU(int n): p_(n + 1), e_(0){
        itoa(begin(p_), end(p_), 0);
    }



private:
    vector<int> p_;
    int e_;
};