#-*- encoding utf-8 -*-
# Author:Anan

class Solution:
    def isValid(self, s: str) -> bool:
        open = '([{'
        close = ')]}'
        plist = []
        curser = 0
        for char in s:
            if char in open:
                if len(plist) == curser:
                    plist.append(char)
                    curser += 1
                else:
                    plist[curser] = char
                    curser += 1
            elif char in close:
                if curser != 0 and plist[curser-1] == open[close.index(char)]:
                    curser -= 1
                else:
                    return False

        if curser == 0:
            return True
        else:
            return False


print(Solution().isValid(']'))

