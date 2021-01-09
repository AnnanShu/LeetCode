from typing import List
class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        max_n = (N-1)//2 + 1
        if N*N == len(mines):
            return 0
        grid = [[1]*N for _ in range(N)]

        for i, j in mines:
            grid[i][j] = 0
        dp = grid.copy()
        for line in dp:
            print(line)
        for rad in range(1, max_n + 1):
            for core_i in range(rad, N - rad):
                for core_j in range(rad, N - rad):
                    if dp[core_i][core_j] == rad and (grid[core_i-rad][core_j] and\
                        grid[core_i+rad][core_j]  and grid[core_i][core_j-rad]  and\
                            grid[core_i][core_j+rad] ):
                        print(f"i:{core_i}, j:{core_j}, rad:{rad}")
                        dp[core_i][core_j] += 1
        
        for line in dp:
            print(line)
        return max([max(line) for line in dp])


Solution().orderOfLargestPlusSign(5,[[0,0],[0,3],[1,1],[1,4],[2,3],[3,0],[4,2]])
10
the_sn = [[0,0],[0,1],[0,2],[0,7],[1,2],[1,3],[1,9],[2,3],[2,5],[2,7],[2,8],[3,2],[3,5],[3,7],[4,2],[4,3],[4,5],[4,7],[5,1],[5,4],[5,8],[5,9],[7,2],[7,5],[7,7],[7,8],[8,5],[8,8],[9,0],[9,1],[9,2],[9,8]]
Solution().orderOfLargestPlusSign(10,the_sn)
True & True & True & True and True and False

nums = [i for i in range(10)]
for i in nums[:5:-1]:
    print(i)