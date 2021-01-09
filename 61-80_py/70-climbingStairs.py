'''
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(3)]
        dp[1] = 1
        dp[2] = 2
        if n >= 3:
            for num in range(3,n+1):
                dp[1],dp[2] = dp[2],dp[1]+dp[2]

        else:
            dp[2] = dp[n]

        return dp[2]

print(Solution().climbStairs(8))