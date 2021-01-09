class Solution:
    def maximalRectangle(self, matrix) -> int:
        flag = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    flag = True  
        # return 0 if there isn't any 1 in the matrix 
        if not flag:
            return 0

        max_rect = 1

        def rect(list1):
            return list1[0] * list1[1]

        dp = [[[0,0] for _ in matrix[0]] for __ in matrix]
        if matrix[0][0] == '1':
            dp[0][0] = [1,1] 

        for c_idx, elem in enumerate(matrix[0][1:], start=1):
            if elem == '1' and matrix[0][c_idx-1] == '1':
                dp[0][c_idx] = [dp[0][c_idx-1][0] + 1, 1]
                max_rect = max(rect(dp[0][c_idx]), max_rect)
            elif elem == '1':
                dp[0][c_idx] = [1, 1]

        for r_idx, row in enumerate(matrix[1:], start=1):
            if row[0] == '1' and matrix[r_idx-1][0] == '1':
                dp[r_idx][0] = [1, dp[r_idx-1][0][1] + 1]
                max_rect = max(rect(dp[r_idx][0]), max_rect)
            elif row[0] == '1':
                dp[r_idx][0] = [1, 1]

        # def rect(list1):
        #     return list1[0] * list1[1]

        for r_idx, row in enumerate(matrix[1:], start = 1):
            for c_idx, elem in enumerate(row[1:], start = 1):
                if elem== '1':
                    if matrix[r_idx-1][c_idx-1] == '1' and matrix[r_idx-1][c_idx] == '1' and \
                        matrix[r_idx][c_idx-1] == '1':
                        dp[r_idx][c_idx] = [dp[r_idx-1][c_idx-1][0] + 1, dp[r_idx-1][c_idx-1][1] + 1]
                        if rect(dp[r_idx][c_idx]) > max_rect:
                            max_rect = rect(dp[r_idx][c_idx])  

                    elif matrix[r_idx][c_idx - 1] == '1':
                        dp[r_idx][c_idx] = [dp[r_idx][c_idx-1][0] + 1,1]
                        if rect(dp[r_idx][c_idx]) > max_rect:
                            max_rect = rect(dp[r_idx][c_idx])

                    elif matrix[r_idx-1][c_idx] == '1':
                        dp[r_idx][c_idx] = [1, dp[r_idx-1][c_idx][1] + 1]
                        if rect(dp[r_idx][c_idx]) > max_rect:
                            max_rect = rect(dp[r_idx][c_idx]) 

        return dp
                



l1 = [["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]
dp = Solution().maximalRectangle(l1)
dp
for line in dp:
    print(dp)