# board = []
# for _ in range(m):
#     board.append(input().strip().split())
m, n = list(map(int, input().strip().split()))
if m == 0:
    print(0)
else:
    
    board = []
    for _ in range(m):
        board.append(input().strip())
    dp = [[0] * n for _ in range(m)]
    dp[0] = [1 if board[0][i]=='M' else 0 for  i in range(n)]
    for i in range(m):
        if board[i][0] == 'M':
            dp[i][0] = 1
    for j in range(1, m):
        for i in range(1, n):
            if board[j][i] == 'M':
                dp[j][i] = min(dp[j-1][i-1], dp[j][i-1], dp[j-1][i]) + 1

    max_edges = max(max(line) for line in dp)
    print(max_edges * max_edges)