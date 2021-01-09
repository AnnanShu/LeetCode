from typing import List 
from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(None)
        def backtrack(index: int) -> List[List[str]]:
            if index == len(s):
                return [[]]
            ans = list()
            for i in range(index + 1, len(s) + 1):
                word = s[index:i]
                if word in wordSet:
                    nextWordBreaks = backtrack(i)
                    for nextWordBreak in nextWordBreaks:
                        ans.append(nextWordBreak.copy() + [word])
            return ans
        
        wordSet = set(wordDict)
        breakList = backtrack(0)
        return breakList

        # lens = list(set(len(word) for word in wordDict))
        # n = len(s)
        # wordDict = set(wordDict)

        # @lru_cache(None)
        # def backtrack(i):
        #     if i >= len(s):  return [[]]

        #     ans = []
        #     for word_len in lens:
        #         cur_word = s[i: min(i + word_len, n)]
        #         print(cur_word)
        #         if cur_word in wordDict:
        #             nxtwordbreaks = backtrack(i + word_len)
        #             print(nxtwordbreaks)
        #             for nxtwordbreak in nxtwordbreaks:
        #                 ans.append([cur_word] + nxtwordbreak[:])
        #     return ans 
        
        # res = backtrack(0)
        # return res

Solution().wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])
