#include<iostream>
#include<unordered_map>
#include<deque>
using namespace std;

class Solution {
deque<unordered_map<string, int>> scopes_;
public:
    int evaluate(string expression) {
        scopes_.clear();
        int pos = 0;
        return eval(expression, pos);
    }

private:
    int eval(const string& s, int& pos){
        scopes_.push_front(unordered_map<string, int>());
        int value = 0; // The return value of current expr
        if (s[pos] == '(') ++ pos;

        // com
    }
};