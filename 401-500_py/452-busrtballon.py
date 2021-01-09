from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x:x[0])
        ans = 0
        pre_min = -float('inf') 
        for left, right in points:
            if left > pre_min:
                ans += 1
                pre_min = right
            elif right < pre_min:
                pre_min = right
        return ans 