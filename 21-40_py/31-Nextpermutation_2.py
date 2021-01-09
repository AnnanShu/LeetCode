class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse_list(nums):
            length = len(nums)
            for i in range(length//2):
                nums[i], nums[length-i] = nums[length-i], nums[i]

        length = len(nums)
        for idx in range(length-1, 0, -1):
            if idx - 1 == 0:
                reverse_list(nums)
            if nums[idx] > nums[idx-1]:
                reverse_list(nums[idx-1:])
                break

        return nums



Solution().nextPermutation([1,2,3])