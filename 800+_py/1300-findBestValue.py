from typing import List
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr = sorted(arr)
        n = len(arr)
        for i, num in enumerate(arr):
            if target / (n - i) <= num:
                return target // (n - i) if abs(target - (n-i)*(target // (n - i) + 1)) >= abs(target - (n-i)*(target // (n - i))) else target // (n - i) + 1
            target -= num
        else: 
            return arr[-1]

Solution().findBestValue([60864,25176,27249,21296,20204] ,56803)