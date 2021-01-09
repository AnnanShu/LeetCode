from typing import List
import itertools
from functools import lru_cache
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        stoneValue = [0] + stoneValue
        
        sums = list(itertools.accumulate(stoneValue))
        
        @lru_cache(None)
        def dp(l, r):
            if l == r: return 0
            ans = 0
            for k in range(l, r):
                sum_l = sums[k + 1] - sums[l]
                sum_r = sums[r + 1] - sums[k + 1]
                if sum_l < sum_r:
                    ans = max(ans, sum_l + dp(l, k))
                elif sum_l > sum_r:
                    ans = max(ans, sum_r + dp(k + 1, r))
                else:
                    ans = max(sum_l + dp(l, k), sum_l + dp(k + 1, r))
            return ans 
    
        return dp(0, n-1)

