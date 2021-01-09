# Given a string, find the length of the longest substring without repeating 
# characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s) -> int:
        """
        :type s: str
        :rtype: int
        """

        longest = 1
        len_s = len(s)
        current = 1
        if len_s == 0:
            return 0

        i = 1 
        while i < len_s:
            if current == 1:  
                if s[i] == s[i-1]:
                    i += 1
                else:
                    current += 1
                    i += 1
            # current  > 1 and without duplication
            elif s[i] not in s[i-current:i]:
                # counter increase 1
                current += 1
                i += 1  
            
            else:
                i = i - current + 2 
                current = 1
                
            
            if longest < current:
                longest = current
        
        return longest

Solution().lengthOfLongestSubstring("anviaj")

