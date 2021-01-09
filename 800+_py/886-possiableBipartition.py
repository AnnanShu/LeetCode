from collections import defaultdict
from typing import List
class Solution:
    def canBipartition(self, N:int, dislike: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in dislike:
            graph[u].append(v)
            graph[v].append(u)

        color = {}
        def dfs(node, c = 0):
            if node in color:
                return c == color[node]
            color[node] = c  
            return all(dfs(nei, c ^ 1) for nei in graph[node])

        return all(dfs(node) for node in range(1, N+1) if node not in color)