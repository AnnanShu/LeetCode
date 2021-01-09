all_pairs = [[4,2],[3, 3],[5, 4],[5, 3],[1, 5]]

n = 5
res = []
visited = [False] * n
def dfs(profit, i, j, visited):
    cur_pairs = [all_pairs[i] for i in range(n) if not visited[i] else [0,0]]
    i = 
    if not i and not j:
        res.append(profit)
    elif not i:
        
        for idx in range(n):
            if visited[idx] == False:
                visited[idx] = True
                dfs(profit + all_pairs[idx][1], i, j-1, visited)
                visited[idx] = False
    elif not j:
        for idx in range(n):
            if visited[idx] == False:
                visited[idx] = True
                dfs(profit + all_pairs[idx][0], i-1, j, visited)
                visited[idx] = False
    else:
        for idx in range(n):
            if visited[idx] == False:
                visited[idx] = True
                dfs(profit + all_pairs[idx][1], i, j-1, visited)
                dfs(profit + all_pairs[idx][0], i-1, j, visited)
                visited[idx] = False

dfs(0, 2, 2, visited)
print(max(res))

n, max_i, max_j = list(map(int, input().strip().split()))
all_pairs = []
for i in range(n):
	all_pairs.append(list(map(int, input().strip().split())))
res = []
visited = [False] * n
def dfs(profit, i, j, visited):
    if not i and not j:
        res.append(profit)
    elif not i:
        for idx in range(n):
            if visited[idx] == False:
                visited[idx] = True
                dfs(profit + all_pairs[idx][1], i, j-1, visited)
                visited[idx] = False
    elif not j:
        for idx in range(n):
            if visited[idx] == False:
                visited[idx] = True
                dfs(profit + all_pairs[idx][0], i-1, j, visited)
                visited[idx] = False
    else:
        for idx in range(n):
            if visited[idx] == False:
                visited[idx] = True
                dfs(profit + all_pairs[idx][1], i, j-1, visited)
                dfs(profit + all_pairs[idx][0], i-1, j, visited)
                visited[idx] = False

dfs(0, max_i, max_j, visited)
print(max(res))