"""
Given an integer array nums, find the contiguous subarray (containing at least 
one number) which has the largest sum and return its sum.

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        # dp[i][0] contains current node
        # dp[i][1] do not contains current node
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i]= max(dp[i-1] + nums[i], nums[i])

        return max(dp)

Solution().maxSubArray([-2,1])

