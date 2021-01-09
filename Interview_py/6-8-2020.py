'A'.iscapital()
'A'.isdigit()
ord('Z')
class Solution:
    def detectCapitalUse(self, word: str):
        n = len(word)
        if n <= 1:
            return True
        first = word[0]
        if ord(first) >= 65 and ord(first) <= 90:
            if n <= 2:
                return True
            second = word[1]
            if ord(second) >= 65 and ord(second) <= 90:
                print('first condition')
                for char in word[2:]:
                    if ord(char) > 90:
                        print('False')
                        return False
                
            if ord(second) > 90:
                print('second condition')
                for char in word[2:]:
                    if ord(char) <= 90:
                        print('False')
                        return False
        
        else:
            print('third condition')
            for char in word[1:]:
                print(ord(char))
                if ord(char) <= 90:
                    print('False')
                    return False

        return True
Solution().detectCapitalUse('uZfa')

min({'2':3,2:3}.values())

not None