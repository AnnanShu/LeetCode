'''
Rotate the image in-place
Given input matrix
 1, 2, 3
 4, 5, 6
 7, 8, 9
 After rotate:
 7, 4, 1
 8, 5, 2
 9, 6, 3
'''
class Solution:
    def rotate(self, matrix:list):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()

        return matrix

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(Solution().rotate(matrix))