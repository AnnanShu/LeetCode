from typing import List
from pprint import pprint
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l, r, t, b = 0, n-1, 0, n-1
        num = 1
        res = [[0]*n for __ in range(n)]
        while num <= n*n:
            for i in range(l, r+1):
                res[t][i] = num
                num += 1
            t += 1
            for j in range(t, b+1):
                res[j][r] = num
                num += 1
            r -= 1
            for k in range(r, l-1, -1):
                res[b][k] = num
                num += 1
            b -= 1
            for m in range(b, t-1, -1):
                res[m][l] = num
                num += 1
            l += 1
        
        return res

for line in Solution().generateMatrix(4):
    print(line)