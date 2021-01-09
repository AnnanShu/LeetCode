class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] * n
        if s[0] == '0': return 0
        for i in range(1, n):
            if s[i] == '0':
                if s[i-1] > '2':
                    return 0
                else:
                    dp[i] = dp[i-1]        
            elif s[i-1] == '1':
                dp[i] = dp[i-1] + dp[i-2]
            elif s[i-1] == '2':
                if i > 1 and  '0' < s[i] <= '6':
                    dp[i] = dp[i-1] + dp[i]
                else:
                    dp[i] = dp[i-1]
            
            else:
                dp[i] = dp[i-1]
        print(dp)
        
        return dp[-1]

Solution().numDecodings('226')