from collections import deque

class Solution:
    def largestRectangleArea(self, heights: list):

        heights = [0] + heights + [0]
        n = len(heights)
        if n == 3:
            return heights[1]
        area = 0
        stack = []
        stack.append(heights[0])
        for i in range(1,n):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                idx = stack[-1]
                area = max((i-idx-1)*height, area)
            stack.append(i) 
        return area
        

heights = [0,1,0,1]
print(Solution().largestRectangleArea(heights))

bin(14)[2:]

label = 15
height = len(bin(label)[2:])
l_to_r = True if height % 2 == 0 else False
l_to_r




