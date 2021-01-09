class Solution:
    def __init__(self):
        self.memo = {}

    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        if N == 0 or not (0<=i<m and 0<=j<n): return 0
        if (i,j,N) in self.memo:  return self.memo[(i,j,N)]

        ans = (i == 0) + (j == 0) + (i == m-1) + (j == n-1)

        for n_i,n_j in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
             ans += self.findPaths(m, n, N-1, n_i, n_j)

        self.memo[(i,j,N)] = ans %(10**9 + 7)
        return ans%(10**9 + 7)

class Solution2:
    def __init__(self):
        self.memo = {}

    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        if N == 0 or not (0 <= i < m and 0 <= j< n): return 0
        if (i, j, N) in self.memo: return self.memo[(i, j, N)]

        mod = 10 ** 9 + 7
        ans = (i == 0) + (j == 0) + (i == m-1) + (j == n - 1)
        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            ans += self.findPaths(m, n, N-1, ni, nj)
        
        self.memo[(i, j, N)] = ans % mod
        
        return ans % mod