from math import log2, ceil
class Solution:
    def racecar(self, target: int):
        m = [0] * (target + 1)

        def dp(t: int):
            """
            count dp            
            """
            if m[t] > 0: return m[t]

            n = ceil(log2(t + 1))
            # AAA...AAA(nA) best case
            if 1 << n == t + 1: return n

            m[t] = n + 1 + dp((1 << n) - t -1)

            for i in range(n-1):
                cur = (1 << (n-1)) - (1 << i)
                m[t] = min(m[t], n + i + 1 + dp(t - cur))

            return m[t]
        
        return dp(target)




