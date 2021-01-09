"""
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.
"""
from typing import List
import collections

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """Use BFS to solve this problem"""
        if not grid or grid[0][0] == 1: return -1
        q = collections.deque()
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dires = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, 0), (-1, -1), (-1, 1)]
        ans = 1 
        q.append((0, 0))
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                if row == m - 1 and col == n - 1: return ans 
                for dy, dx in dires:
                    r, c = row + dy, col + dx
                    if 0 <= r < m and 0 <= c < n and not visited[r][c] and grid[r][c] == 0:
                        visited[r][c] = True 
                        q.append((r, c))
            ans += 1
            
        return -1 

Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])