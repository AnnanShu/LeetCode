from typing import List
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        if n <= 2: return False 
        if A[1] < A[0]: return False 
        direction = 0
        for i in range(2, n):
            if A[i] > A[i-1]:
                if direction != 0: return False     
            elif A[i] < A[i-1]:
                direction = 1
            else:
                return False
                
        return direction == 1

Solution().validMountainArray([0, 3, 2, 1])
