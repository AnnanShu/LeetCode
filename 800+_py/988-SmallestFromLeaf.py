"""
Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 
'z': a value of 0 represents 'a', a value of 1 represents 'b', and so on.

Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

(As a reminder, any shorter prefix of a string is lexicographically smaller: for example, "ab" is
 lexicographically smaller than "aba".  A leaf of a node is a node that has no children.)

"""

dict(zip(range(26), [chr(i) for i in range(ord('a'), ord('z') + 1)]))


class Solution:
    def convertToBase7(self, num: int) -> str:
        sign = 1 if num > 0 else -1
        ans = []
        while num > 0:
            print(num)
            ans.append(num % 7)
            num //= 7
        if sign == -1:
            ans.append('-')

        return ''.join(str(each) for each in ans[::-1])
Solution().convertToBase7(-7)