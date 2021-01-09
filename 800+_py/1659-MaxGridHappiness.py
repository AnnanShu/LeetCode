from functools import lru_cache
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, I: int, E: int) -> int:
        init, gain = [None, 120, 40], [None, -30, 20]

        def get(val, i): return (val // (3 ** i)) % 3
        def update(val, s): return (val * 3 + s) % (3 ** n)

        @lru_cache(None)
        def dp(x: int, y: int, i: int, e: int, mask: int) -> int:
            if x == n: x, y = 0, y + 1 # new line 
            if i + e == 0 or y == m: return 0 # if no i or e remians or till last line 

            ans = dp(x + 1, y, i, e, update(mask, 0)) 
            left, up = get(mask, 0), get(mask, n-1)

            for cur, count in [(1, i), (2, e)]:
                if count == 0: continue
                s = init[cur] 
                if x - 1 >= 0 and left: s += gain[cur] + gain[left]
                if y - 1 >= 0 and up: s += gain[cur] + gain[up]

                ans = max(ans, s + dp(x + 1, y, i - (cur == 1), e - (cur == 2), update(mask, cur)))

            return ans 
        
        return dp(0, 0, I, E, 0)