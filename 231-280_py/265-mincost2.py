class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0: return 0
        k = len(costs[0])
        dp = [[0] * k for _ in range(n)]
        dp[0] = costs[0]
        for i in range(1, n):
            for j in range(k):
                dp[i][j] = costs[i][j] + min(dp[i-1][alpha] for alpha in range(k) if alpha != j)
        
        return min(dp[-1])