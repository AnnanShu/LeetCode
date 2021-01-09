from typing import List
from functools import reduce
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        def dfs(path):
            if len(path) == n:
                ans.append(reduce(lambda x, y: 10* x + y, path[:]))
                return 
            if not path:
                if k <= 4:
                    candis = [i for i in range(1, 10)]
                else:
                    candis = [i+1 for i in range(9-k)] + [9-i for i in range(10-k)]  
            else:
                if k == 0: candis = [path[-1],]
                else:
                    candis = []
                    if path[-1] + k <= 9:
                        candis.append(path[-1] + k)
                    if path[-1] - k >= 0:
                        candis.append(path[-1] - k)
            
            for candi in candis:
                path.append(candi)
                dfs(path)
                path.pop()
        
        dfs([])
        return ans