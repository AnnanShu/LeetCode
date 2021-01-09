from typing import List
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = []
        heapq.heappush(q, (grid[0][0], 0, 0))
        visited = [[False] * n for _ in range(n)]
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while q:
            t, x, y = heapq.heappop(q)
            if x == y == n - 1: return t 
            for dx, dy in directions:
                tx = x + dx 
                ty = y + dy 
                if 0 <= tx < n and 0 <= ty < n and not visited[tx][ty]:
                    visited[tx][ty] = True
                    heapq.heappush(q, (max(t, grid[tx][ty]), tx, ty))  


