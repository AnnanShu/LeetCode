from typing import List
import math
class Solution:
    def divisorGame(self, N: int):
        dp = [False] * (N+1)
        dp[2] = True
        for num in range(3,N + 1):
            divisor = math.floor(math.sqrt(num))
            for may_divisor in range(1, divisor + 1):
                if not num % may_divisor and not dp[num-may_divisor]:
                    dp[num] = True
                    break
        print(dp)
        return dp[N]

Solution().divisorGame(10)





