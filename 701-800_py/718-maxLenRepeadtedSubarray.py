"""
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].

"""

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        len_a = len(A)
        len_b = len(B)
        # (a+1) * (b+1)
        dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]
        for i, a_elem in enumerate(A,start=1):
            for j, b_elem in enumerate(B, start=1):
                if a_elem == b_elem:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
        
        return max([max(i) for i in dp])


A = [1,2,3,2,1]
B = [3,2,1,4,7]

Solution().findLength(A, B)