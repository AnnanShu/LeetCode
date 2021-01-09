from typing import List
class UFS:
    def __init__(self, n):
        self.p = [i for i in range(n+1)]
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, u, v, c):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            self.p[pu] = pv 
            return 1, c
        return 0, 0


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        connections = sorted(connections, key = lambda x: x[2])
        ufs = UFS(N)
        connected = 0
        res = 0 
        for connection in connections:
            dc, dr = ufs.union(*connection)
            connected += dc 
            res += dr 
            
        return res if connected == N - 1 else -1