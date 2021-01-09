class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        if not strs:
            return ""
        idx_len = min([len(s) for s in strs])
        res = 0
        while res < idx_len:
            if len(set([s[res] for s in strs])) == 1:
                res += 1
            else:
                break
        
        return strs[0][:res]

{1,2,3} | {2,3,4,5}