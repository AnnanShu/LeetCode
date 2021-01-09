"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        dp = [[0]*col for _ in range(row)]

        col_mark = True
        if col > 1:
            for i, elem in enumerate(obstacleGrid[0]):
                if elem == 1:
                    col_mark = False
                elif col_mark:
                    dp[0][i] = 1

        row_mark = True
        if row > 1:
            for i, elems in enumerate(obstacleGrid):
                if elems[0] == 1:
                    row_mark = False
                elif row_mark:
                    dp[i][0] = 1

        if row > 1 and col > 1:
            for i in range(1, row):
                for j in range(1, col):
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] =  dp[i-1][j] + dp[i][j-1] 

        print(dp)

        return dp[-1][-1]  


Solution().uniquePathsWithObstacles([[1],[0],[0]])