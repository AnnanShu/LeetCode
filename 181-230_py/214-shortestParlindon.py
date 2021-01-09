class Solution:

    ## KMP create the nxt table
    def build(self, p: str):
        nxt = [0, 0]
        m = len(p)
        j = 0
        for i in range(1, m):
            while j > 0 and p[i] != p[j]:
                j = nxt[j]
            if p[i] == p[j]:
                j += 1
            nxt.append(j)
        return nxt
        
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        s_rev = s[::-1]
        # print(s_rev)
        nxt = self.build(s)
        j = 0
        for i in range(n):
            # print(j)
            while j > 0 and s_rev[i] != s[j]:
                j = nxt[j]
            if s_rev[i] == s[j]:
                j += 1
        
        return s_rev[:n-j] + s