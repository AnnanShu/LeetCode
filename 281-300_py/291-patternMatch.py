import collections
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        key_set = set()
        value_set = set()
        hash_map = {k:k for k in pattern}

        def dfs(p, s):
            if not p and not s: return True
            if not p or not s: return False
            if len(s) < len(p): return False 
            if p[0] in key_set:
                the_len = len(hash_map[p[0]])
                if s[:the_len] != hash_map[p[0]]: return False
                return dfs(p[1:], s[the_len:])
            lp, ls = len(p), len(s)
            for len_ in range(1, ls - lp + 2):
                if s[:len_] in value_set: continue
                hash_map[p[0]] = s[:len_]
                key_set.add(p[0])
                value_set.add(s[:len_])
                if dfs(p[1:], s[len_:]): return True 
                key_set.remove(p[0])
                value_set.remove(s[:len_])
            return False 
        ans = dfs(pattern, s)
        return ans, hash_map if ans else ans

Solution().wordPatternMatch('aba', 'aaaa')
Solution().wordPatternMatch(pattern = "abab", s = "redblueredblue")
Solution().wordPatternMatch(pattern = "aaaa", s = "asdasdasdasd")

