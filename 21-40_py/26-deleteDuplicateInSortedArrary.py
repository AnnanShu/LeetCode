class Solution:
    def removeDuplicates(self, nums:list):
        cursor = 1
        for i, num in enumerate(nums[1:], start=1):
            if num == num[cursor-1]:
                continue
            else:
                nums[cursor] = num
                cursor += 1

        return nums[:cursor]
