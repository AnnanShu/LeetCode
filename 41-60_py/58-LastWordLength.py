from typing import List
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cur1 = -1
        n = len(s)
        mark = False
        if n < 1:
            return 0
        for idx, char in enumerate(s):
            if char == ' ':
                mark = True
            elif mark and char != ' ':
                cur1 = idx - 1
                mark = False
            if not mark:  
                cur2 = idx
        return cur2 - cur1

Solution().lengthOfLastWord('aa')

a = 1