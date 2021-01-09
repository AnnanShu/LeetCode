from typing import List
class UFS:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.ranks = [0] * (n)

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        # return redundent edges number 
        if pu == pv: return 1
        if self.ranks[pv] > self.ranks[pu]:
           self.parents[pu] = pv 
        elif self.ranks[pv] < self.ranks[pu]:
            self.parents[pv] = pu 
        else:
            self.parents[pv] = pu 
            self.ranks[pu] += 1
        return 0

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        cns = len(connections)
        if cns + 1 < n:
            return -1
        ufs = UFS(n)
        red = 0
        for l, r in connections:
            red += ufs.union(l, r)       
        # actual useful connection = cns - red 
        # we need is n - 1
        return  (n - 1) - (cns - red)