from typing import List
from typing import Iterable
"""
I should use DFS here to get all nodes appears in the list
current time periods.
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]):
        N = len(graph)

        color = {}
        def dfs(node, c = 0):
            if node in color:
                return color[node] == c 
            color[node] = c 
            return all(dfs(nei, c ^ 1) for nei in graph[node])

        return (dfs(node) for node in range(N) if node not in color)

        # init, blue, red = 0, 1, 2
        # n = len(graph)
        # visited = [False]*n
        # color_panel = [init]*n
        # color_panel[0] = blue
        # node_list = graph[0]
        # visited[0] = True
        # while node_list:
        #     current_node = node_list[0]
        #     if visited[current_node]:
        #         node_list.remove(current_node)
        #         continue
        #     else:
        #         node_list.remove(current_node)
        #         neibour_color = blue if color_panel[current_node] == red else red
        #         for node in graph[current_node]:
        #             node_list.append(node)
        #             if color_panel[node] == init:
        #                 color_panel[node] = neibour_color
        #             else:
        #                 if color_panel[node] != neibour_color:
        #                     return False
        #         visited[current_node] = True

        # return True

Solution().isBipartite([[1,3], [0,2], [1,3], [0,2]])

Solution().isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]])

Solution().isBipartite([[1],[0,3],[3],[1,2]])


str(1110101001).count('1')

str(11111111111111111111111111111101).count('1')