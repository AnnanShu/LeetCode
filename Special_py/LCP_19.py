class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        dp = [[0, 0, 0] for _ in range(n)]
        # 0: left_r, 1: y, 2: right_r 
        isRed = lambda x: int(leaves[x] == 'r')
        isYellow = lambda x: int(leaves[x] == 'y')
        dp[0][0] = isYellow(0)
        dp[0][1], dp[0][2] = float('inf'), float('inf')
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + isYellow(i)
            dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + isRed(i)
            if i >= 2:
                dp[i][2] = min(dp[i-1][1], dp[i-1][2]) + isYellow(i)
            else:
                dp[i][2] = float('inf')
        return dp[-1][-1]

Solution().minimumOperations('yry')