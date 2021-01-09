from typing import List
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        if not A or not B: return ans
        n1, n2 = len(A), len(B)
        i, j = 0, 0 
        while i < n1 and j < n2:
            if A[i][1] < B[j][0]:
                i += 1
                continue

            if B[j][1] < A[i][0]:
                j += 1
                continue

            if A[i][1] <= B[j][1]:
                ans.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
                i += 1
                continue

            if A[i][1] > B[j][1]:
                ans.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
                j += 1
                continue
        return ans 