import heapq
from typing import List
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        # In order to use min heap we need to take the negative of all the elements in the list (priority queue).
        A = [[-i for i in line] for line in A]
        R, C = len(A), len(A[0])
        q = []
        heapq.heappush(q, (A[0][0], 0, 0))
        visited = [[False] * C for _ in range(R)]
        dires = [(-1, 0), (1, 0), (0, 1), (0,-1)]
        visited[0][0] = True 
        while q:
            t, y, x = heapq.heappop(q)
            if y == R - 1 and x == C - 1: return -t 
            for dy, dx in dires:
                j = y + dy 
                i = x + dx 
                if 0 <= i < C and 0 <= j < R and not visited[j][i]:
                    visited[j][i] = True  
                    heapq.heappush(q, (max(A[j][i], t), j, i))