"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in
 nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of
  C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the 
ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of
 friend circles among all the students.

"""
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
        return True

from typing import List
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        s = UnionFindSet(n)
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j] == 1: s.Union(i, j)
        
        circles = set()
        for i in range(n):
            circles.add(s.Find(i))
        
        return len(circles)