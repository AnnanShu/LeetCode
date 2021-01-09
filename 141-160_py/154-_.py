from typing import List
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        n = len(numbers)
        
        def auxiliary_func(start, end, numbers):
            if end - start > 1:
                mid = (start + end) // 2
                if numbers[start] >= numbers[mid]:
                    return auxiliary_func(start, mid, numbers)
                elif numbers[mid] >= numbers[end]:
                    return auxiliary_func(mid, end, numbers)
                elif numbers[mid] >= numbers[start] and numbers[mid] <= numbers[end]:
                    return auxiliary_func(start, mid, numbers)
            elif end - start == 1:
                return numbers[start] if numbers[start] <= numbers[end] else numbers[end]
            elif end == start:
                return numbers[start]
        
        return auxiliary_func(0, n-1, numbers)

Solution().minArray([3,4,5,1,2])


Solution().minArray([1,3,5])

[3,9,20,15,7][0:0]