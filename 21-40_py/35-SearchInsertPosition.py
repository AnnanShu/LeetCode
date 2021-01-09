from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int):
        n = len(nums)
        def auxiliary_func(nums, start, end, target):
            if end-start <= 1:
                if nums[start] >= target :
                    return start 
                else:
                    return start + 1
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return auxiliary_func(nums, start, mid, target)
            else:
                return auxiliary_func(nums, mid + 1, end, target)

        
        return auxiliary_func(nums, 0, n, target)

Solution().searchInsert([1,3,5,6], 2)

Solution().searchInsert([1,3,5,6], 0)


