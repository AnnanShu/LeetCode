g = [400, 500, 200, 300, 350]
p = [5, 5, 3, 4, 3]
n = 10
w = 5
dp = [[0] * n for _ in range(w)]

for i in range(w):
    for j in range(n):
        if j+1 < p[i]:
            if j == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i][j-1]
        
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-p[i]] + g[i])

for line in dp:
    print(line)
