from typing import List
import math
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        """use bucket sort to solve this problem in O(n) time complexity"""
        n = len(nums)
        if n < 2: return 0 
        l, r = min(nums), max(nums)
        if r - l == 0: return 0 
        gap_instance = max(1, (r - l) // n)
        gapcnts = math.ceil((r - l + 1) / gap_instance)
        buckets = [[-1, -1] for _ in range(gapcnts)] 
        calpos = lambda num: (num - l) // gap_instance

        for num in nums:
            pos = calpos(num)
            if num < buckets[pos][0] or buckets[pos][0] == -1:
                buckets[pos][0] = num 
            if num > buckets[pos][1] or buckets[pos][1] == -1:
                buckets[pos][1] = num 

        ans, pre = 0, l
        for small, large in buckets:
            if small == -1:
                continue 
            else:
                ans = max(small - pre, ans)
                pre = large
        return ans 

Solution().maximumGap([3, 6, 9, 1])
Solution().maximumGap([1, 39, 44, 32, 11,22])