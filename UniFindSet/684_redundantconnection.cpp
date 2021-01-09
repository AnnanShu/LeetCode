#include<vector>
#include<iostream>
#include"unionFindSet.h"
using namespace std;

class Solution{
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges){
        UnionFindSet s(edges.size());
        for(const auto& edge: edges)
            if (!s.Union(edge[0], edge[1])){
                return edge;
            }
        
        return {};
    }
};

// class UnionFindSet{
// public:
//     UnionFindSet(int n){
//         rank_ = vector<int>(n + 1, 0);
//         parents_ = vector<int>(n+1, 0);

//         for(int i = 0; i < parents_.size();i++)
//             parents_[i] = i;
                    
//     }
//     // Merge sets that contains u and v
//     // Return true if merged, flase if u and v are already in one set
//     bool Union(int u, int v){
//         int pu = Find(u);
//         int pv = Find(v);
//         if (pu == pv) return false;

//         // Merge low rank tree into high high ranl tree
//         if (rank_[pv] > rank_[pu])
//             parents_[pu] = pv;
//         else if (rank_[pu] > rank_[pv])
//             parents_[pv] = pu;
//         else{
//             parents_[pu] = pv;
//             rank_[pv] ++;
//         }
//         return true;
//     }

//     // get the root of u 
//     int Find(int u){
//         // Compress the path during traversal
//         if (u != parents_[u])
//             parents_[u] = Find(parents_[u]);
//         return parents_[u];
//     }
// private:
//     vector<int> rank_;
//     vector<int> parents_;

// };