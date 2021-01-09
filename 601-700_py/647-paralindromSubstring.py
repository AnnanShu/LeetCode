class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        cnt = 0
        #dp[i][j] stands for whether from i to j is an palindromic string
        for j in range(n):
            dp[j][j] = True
            cnt += 1
            for i in range(0, j):
                if (j - i) == 1:
                    dp[i][j] = (s[i] == s[j])
                    cnt += dp[i][j]
                else:
                    dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
                    cnt += dp[i][j]
        print(dp)
        return cnt

Solution().countSubstrings('aaa')