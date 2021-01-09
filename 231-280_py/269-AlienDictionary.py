from collections import deque
from functools import reduce
class Solution:
    def alienOrder(self, words: str):
        indegree = [0] * 26
        neibour = [[] for _ in range(26)]
        m = len(words)
        for row in range(m-1):
            if len(words[row]) > len(words[row+1]) and words[row][:len(words[row+1])] == words[row+1]:
                return ''
            min_col = min(len(words[row]), len(words[row+1]))
            i = 0
            while i < min_col:
                if words[row][i] != words[row+1][i]:
                    indegree[ord(words[row+1][i])-ord('a')] += 1
                    neibour[ord(words[row][i])-ord('a')].append(ord(words[row+1][i])-ord('a'))
                    break
                i += 1

        appears = [ord(char) -ord('a') for char in reduce(lambda x, y: set(x) | set(y), words)]
        zero_indegree = [i for i in range(26) if indegree[i] == 0 and i in appears]
        ans = []
        Q = deque(zero_indegree)
        while Q:
            pre = Q.popleft()
            ans.append(pre)
            for cur in neibour[pre]:
                indegree[cur] -= 1
                if indegree[cur] == 0:
                    Q.append(cur)
        
        return '' if len(ans) != len(appears) else  ''.join(chr(i + ord('a')) for i in ans)


dict_ = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
Solution().alienOrder(dict_)

Solution().alienOrder(["za","zb","ca","cb"])



