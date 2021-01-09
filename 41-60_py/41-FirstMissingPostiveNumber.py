class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        if 1 not in nums:
            return 1
        
        if len(nums) == 1:
            return 2

        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1
        

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        the_idx = 0
        while the_idx < len(nums):
            if nums[the_idx] > 0:
                return the_idx + 1
            else:
                the_idx += 1

        return the_idx + 1


Solution().firstMissingPositive([2, 1, 3,-1])