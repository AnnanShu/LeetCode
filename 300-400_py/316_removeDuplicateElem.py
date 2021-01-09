from collections import Counter 
class Solution:
    def removeDuplicateChar(self, s):
        n = len(s)
        if s <= 1: return s
        cnt = dict(Counter(s))
        orderedKey = sorted(cnt.keys())
        s_rev = s[::-1]
        marker = [True] * n

        for i in range(n):
            if cnt[s_rev] > 1:
                marker[i] = False 
                cnt[s_rev] -= 1
        
        
        