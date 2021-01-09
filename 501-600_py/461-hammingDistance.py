"""
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # return sum([((x>>i)&1) ^ ((y>>i)&1) for i in range(32)])
        return bin(x^y).count('1')

Solution().hammingDistance(1,4)

