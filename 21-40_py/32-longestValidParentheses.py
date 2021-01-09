from collections import deque
class Solution:
    def longestValidParentheses(self, s: str): 
        s = ")" + s
        n = len(s)
        dp = [0] * (n)
        for i in range(1, n):
            if s[i] == ')' and s[i-1] == '(':
                dp[i] = dp[i-2] + 2
            if s[i] == ')' and s[i-1] == ')':
                if s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
        print(dp)
        
        return max(dp)

Solution().longestValidParentheses("(()")
Solution().longestValidParentheses("(()(((()")
Solution().longestValidParentheses("(")


False + False


        
