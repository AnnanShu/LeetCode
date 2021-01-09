from typing import List
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze: return False 
        R, C = len(maze), len(maze[0])
        visited = [[False] * C for _ in range(R)]
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        def dfs(j, i):
            visited[j][i] = True 
            ans = False 
            for dy, dx in directions:
                cj, ci = j, i
                while 0 <= cj + dy < R and 0 <= ci + dx < C and maze[cj + dy][ci + dx] != 1:
                    cj += dy 
                    ci += dx 
                if cj == destination[0] and ci == destination[1]: return True 
                if not visited[cj][ci]:
                    ans |= dfs(cj, ci)
            return ans 
        
        return dfs(*start)