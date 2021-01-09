class UnionFindSet:
    def __init__(self, n:int):
        self.rank_ = [0] * (n + 1)
        self.parents_ = [0] * (n + 1)
        for i in range(n + 1):
            self.parents_[i] = i
    
    def Find(self, u):
        if u != self.parents_[u]:
            self.parents_[u] = self.Find(self.parents_[u])
        return self.parents_[u]
    
    def Union(self, u:int, v:int) -> bool:
        pu = self.Find(u)
        pv = self.Find(v)
        if pu == pv: return False 
        
        # Merge low rank tree into high rank tree
        if self.rank_[pu] > self.rank_[pu]:
            self.parents_[pv] = pu
        elif self.rank_[pu] < self.rank_[pv]:
            self.parents_[pv] = pu
        else:
            self.parents_[pv] = pu 
            self.rank_[pu] += 1
    