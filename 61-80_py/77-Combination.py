from typing import List
# class Solution2(object):
#     def combine(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         candidates = [i for i in range(n)]
#         res = list()
#         def auxiliary_func(current, len_remaining, k):
#             if k == 0:
#                 res.append(current)
#             else:
#                 possibilities = len_remaining - k + 1
#                 if possibilities < 1:
#                     return None
            
#                 for num in range(n-len_remaining-1, n-len_remaining + possibilities-1):
#                     the_current = current.copy()
#                     the_current.append(num)
#                     return auxiliary_func(the_current, n-num-1, k-1)
#         auxiliary_func([], n, k)
#         return res

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        the_number = [i+1 for i in range(n)]
        res = list()
        def auxiliary_func(current, len_remaining, k):
            if k == 0:
                return current
            elif len_remaining - k >= 0:
                candidates = len_remaining - k + 1
                for num in range(n+1 -len_remaining,n+1 -len_remaining + candidates):
                    the_current = current.copy()
                    the_current.append(num)
                    res.append(auxiliary_func(the_current, n-num, k-1))
        new_res = list()
        auxiliary_func([], n, k)
        for lis in res:
            # if hasattr(lis,'append'):
            if lis:
                new_res.append(lis)
        return new_res

# current Version
class Solution3:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(path, remaining):
            if len(path) == k:
                res.append(path[:])
                return 
            if len(remaining) >= k - len(path):
                for i in range(len(remaining)):
                    path.append(remaining[i])
                    dfs(path, remaining[i+1:])
                    path.pop()
                     
        dfs([], list(range(1, n+1)))
        return res

Solution3().combine(5,3)
