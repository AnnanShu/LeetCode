#include"unionFindSet.h"
#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

class Solution {
public:
    bool areSentencesSimilarTwo(vector<string>& words1, vector<string>& words2, vector<vector<string>>& pairs) {
        if(words1.size() != words2.size()) return false;
        
        UnionFindSet s(pairs.size() * 2);

        unordered_map<string, int> indices; // word to index

        for(const auto& pair: pairs){
            int u = getIndex(pair[0], indices, true);
            int v = getIndex(pair[1], indices, true);
            s.Union(u, v);
        }
        
        for (int i = 0; i < words1.size(); ++i){
            if (words1[i] == words2[i]) continue;
            int u = getIndex(words1[i], indices);
            int v = getIndex(words2[i], indices);
            if (u < 0 || v < 0) return false;
            if (s.Find(u) != s.Find(v)) return false;
        }
    }
private:
    int getIndex(const string& word, unordered_map<string, int> indices, bool create = false){
        auto it = indices.find(word);
        
    }
};