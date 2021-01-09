#include<vector>
#include<iostream>
#include<unordered_set>
#include"unionFindSet.h"
using namespace std;
class Solution {
public:
    int findCircleNum(vector<vector<int>>& M) {
        int n = M.size();
        UnionFindSet s(n);
        for(int i=0;i < n; i++)
            for(int j=i+1;j < n; j++)
                if (M[i][j] == 1) s.Union(i, j);
        
        unordered_set<int> circles;
        for(int i = 0; i < n; ++i)
            circles.insert(s.Find(i));
        
        return circles.size();

    }
};