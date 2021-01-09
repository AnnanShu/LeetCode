from typing import List
class Solution:
    # use memo recursive to solve this problems
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        # memo recursive 
        m = [[[0] * n for _ in range(n)] for _ in range(n)]
        
        def dfs(boxes, l, r, k):
            if l > r: return 0
            if m[l][r][k] > 0: return m[l][r][k]
            m[l][r][k] = dfs(boxes, l, r-1, 0) + (k + 1) * (k + 1)
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    m[l][r][k] = max(m[l][r][k], dfs(boxes, l, i, k + 1) + \
                        dfs(boxes, i + 1, r-1, 0))
            
            return m[l][r][k]

        return dfs(boxes, 0, n-1, 0)

# from typing import List
# class Solution:
#     # use memo recursive to solve this problems
#     def removeBoxes(self, boxes: List[int]) -> int:

any(1 for i in range(5) if i in [6,7])

[1,2,3][:10]