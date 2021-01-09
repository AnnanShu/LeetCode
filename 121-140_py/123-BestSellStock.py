from typing import List
from pprint import pprint
class Solution:
    def maxProfit(self, prices: List[int]):
        K = 2
        n = len(prices)
        dp = [[[0]*2 for _ in range(n)] for __ in range(K)]
        # dp[k][i][j] -> j, selling day
        for k in range(K):
            for i in range(n):
                


from pprint import pprint
n = 8
k = 2
pprint([[[0]*2 for _ in range(n)] for __ in range(k)])