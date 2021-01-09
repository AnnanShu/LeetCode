from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        if n < 4:
            return []
        res = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k, m = j + 1, n -1
                while k < m:
                    sum4 = nums[i] + nums[j] + nums[k] + nums[m]
                    if sum4 == target:
                        res.append([nums[i], nums[j], nums[k], nums[m]])
                        while k < m -1 and nums[k] == nums[k+1]:
                            k += 1
                        k += 1
                        m -= 1
                    elif sum4 < target:
                        k += 1
                    else:
                        m -= 1
        
        return res