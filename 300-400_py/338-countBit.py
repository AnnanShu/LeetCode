class Solution:
    def countBits(self, num: int) -> list:
        if num == 0:
            return [0,]
        dp = [0] * (num + 1)
        dp[0], dp[1] = 0, 1
        for i in range(2, num + 1):
            dp[i] = dp[i>>1] + (i % 2)
        return dp


            
Solution().countBits(63)
