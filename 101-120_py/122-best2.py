class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        dp = [[-prices[0],0]] + [[0]*2 for _ in range(n-1)]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][0] + prices[i], dp[i-1][1])

        return dp[-1][1]

prices = [7,1,5,3,6,4]
Solution().maxProfit(prices)