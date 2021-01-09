class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int):
        if N < 0:
            return 0
        elif i >= m or i < 0 or j >= n or j < 0:
            return 1
        else:  
            return \
            self.findPaths(m, n, N-1, i + 1, j) + \
                self.findPaths(m, n, N-1, i - 1, j) + \
                    self.findPaths(m, n, N-1, i, j + 1) + \
                        self.findPaths(m, n, N-1, i, j -1)


Solution().findPaths(1,3,3,0,1)