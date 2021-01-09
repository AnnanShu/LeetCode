n = 4
import functools
import itertools
import operator
(lambda k: functools.reduce(int.__mul__, range(1, k + 1), 1))(n)
list(itertools.accumulate([i+1 for i in range(n)], operator.mul))
list(itertools.accumulate([i+1 for i in range(8)], operator.mul))[:-1][::-1]

import operator, itertools
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # first sort is actually the 0-th position
        k = k-1
        if n < 0:
            return 
        if n == 1:
            return "1"
        the_list = [0] * n
        n_fac = list(itertools.accumulate([i+1 for i in range(n)], operator.mul))[:-1][::-1]
        idx = 0
        while k > 0 and idx < n - 1:
            cur = k // n_fac[idx]
            the_list[idx] = cur
            k = k % n_fac[idx]
            idx += 1
        
        permus = [i+1 for i in range(n)]
        i = 0
        res = []
        while i < n:
            the_num = permus[the_list[i]]
            res.append(the_num)
            permus.remove(the_num)
            i += 1

        return ''.join([str(num) for num in res])