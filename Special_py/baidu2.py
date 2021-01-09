from collections import defalutdict, deque
n, m = list(map(int, input().strip().split()))
if n - m > 1: print(-1, -1)
else:
    indegrees = [0] * (n+1)
    graph_set = set()
    for _ in range(m):
        in_, out_ = list(map(int, input().split()))
        indegrees[out_] += 1
        graph_set.add(in_)
        graph_set.add(out_)
    if len(graph_set) < n - 1:
        print(-1, -1)
    
    else:
        non_indegrees = [i for i in range(1, n+1) if indegrees[i] == 0]
        if len(non_indegrees) > 1:
            smallest = -1
        else:
            smallest = non_indegrees[0]
        removed = list()
        while non_indegrees:
            u = non_indegrees.popleft()
            removed.append(u)
            indegrees[u].remove()
            if indegrees[u] == 0:
                non_indegrees.append(u)

        print(smallest, removed[-1])      


