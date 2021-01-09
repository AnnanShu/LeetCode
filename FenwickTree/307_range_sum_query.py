from typing import List
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = [0] + nums  
        n = len(self.nums)
        self.ori = [0] * (n)
        self.sums = [0] * (n)
        for i in range(1, n):
            self.update(i-1, self.nums[i])

    def lowbit(self, i:int) -> int:
        return i & (-i)

    def update(self, i: int, val: int) -> None:  
        i = i + 1
        delta = val - self.ori[i]
        self.ori[i] = val
        while i < len(self.sums):
            self.sums[i] += delta 
            i += self.lowbit(i)

    def sumRange(self, i: int, j: int) -> int:
        i = i
        j = j + 1
        sumi, sumj = 0, 0
        while i > 0:
            sumi += self.sums[i]
            i -= self.lowbit(i)
        while j > 0:
            sumj += self.sums[j]
            j -= self.lowbit(j)
        
        return sumj - sumi