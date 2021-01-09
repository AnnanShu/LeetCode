# Topological sort is an algorithm which handle with 
from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]):
        indegrees = [0] * numCourses
        adjancent = [[] for _ in range(numCourses)]

        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjancent[pre].append(cur)
        
        Q = deque(i for i in range(numCourses) if indegrees[i] == 0)
        can_finished = set(Q)
        while Q:
            pre = Q.popleft()
            for cur in adjancent[pre]:
                indegrees[cur] -= 1
                if indegrees[cur] == 0:
                    Q.append(cur)
                    can_finished.add(cur)
        
        return len(can_finished == numCourses)
        



# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]):
#         indegrees = [0 for _ in range(numCourses)]
#         adjacency = [[] for _ in range(numCourses)]
#         queue = deque()
#         # Get the indegree and adjacency of every course.
#         for cur, pre in prerequisites:
#             indegrees[cur] += 1
#             adjacency[pre].append(cur)
#         # Get all the courses with the indegree of 0.
#         for i in range(len(indegrees)):
#             if not indegrees[i]: queue.append(i)
#         # BFS TopSort.
#         while queue:
#             pre = queue.popleft()
#             numCourses -= 1
#             for cur in adjacency[pre]:
#                 indegrees[cur] -= 1
#                 if not indegrees[cur]: queue.append(cur)
#         return not numCourses
