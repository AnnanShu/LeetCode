from typing import List
class Solution:
    def spiralPrder(self, matrix:List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        l, r, t, b = 0, cols -1, 0, rows -1
        max_num = rows * cols
        res = []
        count = 1
        while count < max_num:
            for i in range(l, r+1):
                res.append(matrix[t][i])
                count += 1
            t += 1
            for i in range(t, b+1):
                res.append(matrix[i][r])
                count += 1
            r -= 1
            for i in range(r, l-1, -1):
                res.append(matrix[b][i])
                count += 1
            b -= 1
            for i in range(b, t-1, -1):
                res.append(matrix[i][l])
                count += 1
            l += 1
        return res

the_list = [[i+x+1 for x in range(c_size)] for i in range(0, r_size * c_size, c_size)]
for line in the_list:
    print(line)
Solution().spiralPrder(the_list)