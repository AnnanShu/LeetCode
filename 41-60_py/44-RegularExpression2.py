"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching 
with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

Wildcard Match
"""
class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        l_s = len(s)
        l_p = len(p)
        dp = [[False] * (l_p + 1) for _ in range(l_s + 1)]
        dp[0][0] = True 
        def matchs(j, i):
            if j == 0: return False 
            if p[i-1] == '?': return True 
            else: return s[j-1] == p[i-1]
        
        for j in range(l_s + 1):
            for i in range(1, l_p + 1):
                if p[i-1] == '*':
                    dp[j][i] |= dp[j][i-1] or dp[j-1][i]  
                else:
                    if matchs(j, i):
                        dp[j][i] = dp[j-1][i-1]
        
        for line in dp:
            print(line)
        
        return dp[-1][-1]

Solution().isMatch("adceb","*a*b")
Solution().isMatch('a',"a*")



        

