from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int):
        the_windows = deque()
        deque.append(nums[0])
        for i in range(1,k):
