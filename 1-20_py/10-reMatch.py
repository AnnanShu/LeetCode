"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' 
and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regular-expression-matching
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l_p = len(p)
        l_s = len(s)
        dp = [[False] * (l_p + 1) for _ in range(l_s + 1)]
        dp[0][0] = True
        def match(j, i):
            if j == 0: return False 
            elif p[i-1] == '.': return True 
            else: return s[j-1] == p[i-1]

        for j in range(l_s + 1):
            for i in range(1, l_p+1):
                if p[i-1] == '*':
                    dp[j][i] |= dp[j][i-2]
                    if match(j, i-1):
                        dp[j][i] |= dp[j-1][i]
                else:
                    if match(j, i):
                        dp[j][i] |= dp[j-1][i-1]
        for line in dp:
            print(line)

        return dp[-1][-1]
       
s = "aab"
p = "c*a*b"
Solution().isMatch(s, p)
