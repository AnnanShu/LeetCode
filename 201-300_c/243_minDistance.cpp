/*
Given a list of words and two words word1 and word2, return the shortest distance
between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
*/
#include<string>
#include<vector>
#include<cmath>
using namespace std;

class Solution {
public:
    int shortestDistance(vector<string>& words, string word1, string word2) {
        int loc_1 = -1, loc_2 = -1;
        int pre_1 = -1, pre_2 = -1;
        for(int i = 0; i < words.size(); i ++){
            if (words[i] == word1){
                if (loc_1 == -1 | loc_2 == -1) loc_1 = i;
                if (i - loc_2 < abs(loc_1 - loc_2)) loc_1 = i;
            }

            if (words[i] == word2){
                if (loc_1 == -1 | loc_2 == -1) loc_2 = i;
                if (i - loc_1 < abs(loc_2 - loc_1)) loc_2 = i;
            }

        }
        return abs(loc_2 - loc_1);
    }
};