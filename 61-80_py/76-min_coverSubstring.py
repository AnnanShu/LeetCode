import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""
        n = len(s)
        t_cnt = collections.Counter(t)
        t_set = set(t)
        t_remaining_set = set(t)
        s_cnt = collections.defaultdict(int)
        i, j = 0, 0
        for idx, c in enumerate(s):
            j = idx
            if c in t_cnt:
                if c in t_remaining_set: 
                    s_cnt[c] += 1
                    if s_cnt[c] >= t_cnt[c]:
                        t_remaining_set.remove(c)
                        if not t_remaining_set: break 
                else:
                    s_cnt[c] += 1
        if t_remaining_set: return ''
        min_dist = j - i
        min_i = i 
        min_j = j
        while True:
            if s[i] in t_set:
                if s_cnt[s[i]] > t_cnt[s[i]]:
                    s_cnt[s[i]] -= 1
                    i += 1
                    if j - i < min_dist:
                        min_dist = j - i
                        min_i = i 
                        min_j = j 
                    continue
            else:
                i += 1
                if j - i < min_dist:
                    min_dist = j - i
                    min_i = i 
                    min_j = j 
                continue
            j += 1
            if j < n and s[j] in t_set:
                s_cnt[s[j]] += 1
            if j >= n: break
                
        return s[min_i:min_j+1]