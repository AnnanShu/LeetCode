from typing import List
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        temp = []
        res = []

        def dfs(cur, last):
            pass