import heapq
from typing import List
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        i, n = 0, len(heights)
        height_differs = [0] + [heights[i + 1] - heights[i] if heights[i] < heights[i+1] else 0 for i in range(n - 1)]
        # print(height_differs)
        q = [0] * ladders
        brick_sum = 0
        while i < n:
            cur = heapq.heappushpop(q, height_differs[i])
            # print(cur)
            brick_sum += cur
            if brick_sum > bricks: break
            i += 1
        return i - 1