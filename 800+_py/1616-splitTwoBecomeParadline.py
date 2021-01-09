class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        """Use KMP algorithm to solve this problem
        """
        if a == a[::-1] or b == b[::-1]: return True 
        def build(p):
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

        def match(p, q):
            q = q
            n = len(p)
            nxt = build(p)
            bld = []
            j = 0
            for i in range(n):
                while j > 0 and p[j] != q[i]:
                    j = nxt[j]
                if p[j] == q[i]:
                    j += 1
                bld.append(j)
            return bld 
        
        return match(a, b)

a = "ulacfd"
b = "jizalu"

Solution().checkPalindromeFormation(a, b[::-1])
Solution().checkPalindromeFormation(a, a)