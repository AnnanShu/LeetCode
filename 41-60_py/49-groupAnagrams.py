'''
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

'''
import collections
class Solution:
    def groupAnagrams(self, strs):
        ans = dict()
        for s in strs:
            if ans.get(tuple(sorted(s))):
                ans[tuple(sorted(s))].append(s)
            else:
                ans[tuple(sorted(s))] = [s,]
        return list(ans.values())

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

