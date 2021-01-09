from typing import List
def maxSum(nums:List[int]) -> int:
    n = len(nums)
    dp = [0] * n 
    for i in range(n):
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])
    
    return dp[-1]

maxSum([4,1,1,9,1])
maxSum([1,2,4,1,7,8,3])

10 ** 9 + 7