from typing import List
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        EPSLION = 1e-6
        ADD, MUL, SUB, DIV = 1, 2, 3, 4 
        TARGET = 24

        def dfs(nums:List[float]):
            if len(nums) == 0:
                return False
            if len(nums) == 1:
                return abs(nums[0] - TARGET) < EPSLION
            
            for i, n1 in enumerate(nums):
                for j, n2 in enumerate(nums):
                    if i != j:
                        new_num = []
                        for k, n3 in enumerate(nums):
                            if k != i and k != j:
                                new_num.append(n3)
                        for ope in [1,2,3,4]:
                            if ope == ADD:
                                new_num.append(n1 + n2)
                            if ope == MUL:
                                new_num.append(n1 * n2)
                            if ope == SUB:
                                new_num.append(n1 - n2)
                            if ope == DIV:
                                if abs(n2) < EPSLION:
                                    continue
                                new_num.append(n1 / n2)
                        
                            if dfs(new_num):
                                return True
                            else:
                                new_num.pop()
            return False
        return dfs(nums)
Solution().judgePoint24([4, 1, 8, 7])
                                