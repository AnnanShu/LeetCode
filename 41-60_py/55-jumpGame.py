'''
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''

## Greedy approach
class Solution:
    def canJump(self, nums: list) -> bool:
        max_step = 0
        for idx, num in enumerate(nums):
            if num + max_step <= idx and idx < len(nums) - 1:
                return False
            else:
                max_step = max(idx + num, max_step)

        return True

print(Solution().canJump([3,2,1,0,4]))


