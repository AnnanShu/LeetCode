#include<string>
#include<iostream>
using namespace std;
class Solution {
public:
    bool judgeCircle(string moves) {
        if (moves.size() == 0)return true;
        int x = 0, y = 0;
        for(char c : moves){
            if (c == 'U') x ++;
            if (c == 'D') x --;
            if (c == 'R') y ++;
            if (c == 'L') y --;
        }
        return x == 0 & y == 0;
    }
};
