class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not t:
            return 1
        if not s:
            return 0
        m = len(t)
        n = len(s)
        dp = [[1] * (n + 1)] + [[0] * (n + 1) for _ in range(m)]

        for i in range(1, m+1):
            for j in range(1, n + 1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        
        return dp[-1][-1]