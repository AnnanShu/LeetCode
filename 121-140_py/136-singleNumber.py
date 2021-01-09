from functools import reduce

class Solution:
    def singleNumber(self, nums) -> int:
        return reduce(lambda x,y: x^y, nums)

print(Solution().singleNumber([2,2,3,3,4]) )


reduce(lambda x,y: x + y,['a','p','p','l','e'])


''.join(['a','p','p','l','e'])