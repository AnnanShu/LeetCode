from typing import List 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx, cur = 0, 0 
        n = len(nums)
        while idx < n:
            if nums[idx] == 0:
                idx += 1
                continue 
            if idx != cur:
                nums[cur] = nums[idx]
            cur += 1
            idx += 1 
        while cur < n:
            nums[cur] = 0
            cur += 1