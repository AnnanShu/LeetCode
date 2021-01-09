# Naive algorithm brute forch
# KMP Knuth-Morris-Pratt Fast Pattern Matching in Strings
from typing import List

def build(p: str) -> List[int]:
    m = len(p)
    nxt = [0, 0]
    j = 0
    for i in range(1, m):
        while j > 0 and p[i] != p[j]: 
            j = nxt[j]
        if p[i] == p[j]: 
            j += 1
        nxt.append(j)
    return nxt


# KMP match algorithm
def match(s: str, p: str) -> List[int]:
    n, m = len(s), len(p)
    nxt = build(p)
    res = []
    j =  0
    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = nxt[j]
        if s[i] == p[j]:
            j += 1
      
        if j == m:
            res.append(i - j + 1)
            j = nxt[j]
    
    return res