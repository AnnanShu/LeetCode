from typing import List
class Solution:
    # this is like dp, O(n) space complexity
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        if n < 3: return 0
        left, right = [0] * n, [0] * n 
        for i in range(1, n):
            left[i] = left[i-1] + 1 if A[i] > A[i-1] else 0
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] + 1 if A[i] > A[i+1] else 0
        ans = 0
        for i in range(1, n-1):
            cur_mnt = left[i] + right[i] + 1 if left[i] and right[i] else 0
            ans = max(cur_mnt, ans)
        
        return ans 