class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        s = s.lower()
        s.replace(' ','')
        l, r = 0, n-1
        def is_valid(char):
            # return (ord(char) >= 48 and ord(char) <= 57) | (ord(char) >= 97 and ord(char) <= 122)
            return char.isdigit() | char.islower()

        while l < r:
            if not is_valid(s[l]):
                l += 1
            elif not is_valid(s[r]):
                r -= 1
            elif s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
            
        return True

Solution().isPalindrome('0P')

's'.isalnum()