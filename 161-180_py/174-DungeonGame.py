"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. 
The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially 
positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health 
point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering 
these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health 
(positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or 
downward in each step.
。
"""

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        M = len(dungeon)
        N = len(dungeon[0])
        BIG = 10**5
        dp = [[BIG]*(N+1) for _ in range(M+1)]
        dp[M][N-1] = dp[M-1][N] = 1
        for 
        