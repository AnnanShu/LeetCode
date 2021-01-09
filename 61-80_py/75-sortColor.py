class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        start = 0
        idx = 0
        while idx <= n:
            if nums[idx] == 2 and idx < n:
                temp = nums[idx]
                nums[idx] = nums[n]
                nums[n] = temp
                n -= 1

            elif nums[idx] == 0 and idx > start:
                temp = nums[idx]
                nums[idx] = nums[start]
                nums[start] = temp
                start += 1

            else:
                idx += 1




nums = [1,2,0]
Solution().sortColors(nums)
print(nums)
