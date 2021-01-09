from typing import List
def build(p: str) -> List:
    nxt = [0, 0]
    m = len(p)
    j = 0
    for i in range(1, m):
        if j > 0 and p[i] != p[j]:
            j = nxt[j]
        
        if p[j] == p[i]:
            j += 1
        
        nxt.append(j)
    return nxt

def match(s: str, p: str) -> int:
    nxt = build(p)
    m = len(p)
    n = len(s)
    j = 0
    ans = 0
    for i in range(n):
        if j > 0 and p[j] != s[i]:
            j = nxt[j]

        if p[j] == s[i]:
            j += 1

        if j == m:
            ans += 1
            j = nxt[j]
        
    return ans 
     
match('ababab','ab')