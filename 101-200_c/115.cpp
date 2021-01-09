#include<iostream>
#include<vector>
#include<string>
using namespace std;

class Solution{
public:
    int numDistinct(string s, string t){
        int ls = s.length();
        int lt = t.length();

        vector<vector<long>> dp(lt + 1, vector<long>(ls + 1));
        fill(begin(dp[0]), end(dp[0]), 1);
        for(int i = 1; i <= lt; i ++)
            for (int j=1; j <= ls;j++)
                if (s[j-1] == t[i-1]) 
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1];
                else
                    dp[i][j] = dp[i][j-1];

        return dp[lt][ls];
    }
};