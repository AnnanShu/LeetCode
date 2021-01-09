"""Question Description
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which
together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
Example:
    Input: [1,8,6,2,5,4,8,3,7]
    Output: 49
source：力扣（LeetCode）
link：https://dev.lingkou.xyz/problems/container-with-most-water
"""
import time
import numpy as np 

class Solution:
    @staticmethod
    def maxArea(height) -> int:
        maximum = 0
        n = len(height)
        for i in range(n):
            for j in range(n-1, i, -1):
                contains = (j-i) * min(height[i], height[j])
                if contains > maximum:
                    maximum = contains

        return maximum

    

start = time.clock()
height = [1,8,6,2,5,4,8,3,7]
Solution.maxArea(height)
end = time.clock()
print("Total time is :%s"%(end-start))
