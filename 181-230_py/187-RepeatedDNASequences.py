from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str):
        # Using Rabin Karp to caculate the hash value
        n, L = 10, len(s)
        base = 4
        current_hash = 0
        map_dict = dict(zip('ACGT',range(1,5)))
        hash_set = set()
        res_set = set()
        res = list()
        def f(char):
            return map_dict[char]
        ori_s = s
        s = list(map(f, s))
        # for i in range(10):
        #     current_hash += base*current_hash + s[i]
        current_hash = int(''.join([str(each) for each in s[:10]]),base)
        hash_set.add(current_hash)
        for start in range(n, L-n):
            next_hash = base*(current_hash - (base**(n-1)) * s[start-n]) + s[start]
            if next_hash in hash_set and next_hash not in res_set:
                res.append(ori_s[start:start+10])
                res_set.add(next_hash)
            else:
                hash_set.add(next_hash)
            current_hash = next_hash
        
        return res

Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")


str([1,2,3])

