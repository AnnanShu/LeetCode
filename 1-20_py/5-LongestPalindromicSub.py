class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''If Palindrome: aa (even number of characters) or aba (odd number of characters)
            Using DP to solve this question'''
        if not s:
            return ""
        res = ""
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        max_len = float('-inf')
        for i in range(n):
            for j in range(i, -1, -1):
                if s[i]==s[j] and (i-j <= 2 or dp[i-1][j+1]):
                    dp[i][j] = 1
                if dp[i][j] and max_len <= i - j + 1:
                    res = s[j:i+1]
                    max_len = i - j + 1

        return res

class Solution2:
    @staticmethod
    def longestPalindrome(s):
        '''If Palindrome: aa (even number of characters) or aba (odd number of characters)
            Using DP to solve this question'''
        if not s:
            return ""
        n = len(s)
        # each element in dp list store the longest palindrome length for each is the end elemnt
        dp = [1]*n
        max_i = 1
        max_len = 1
        for i in range(1,n):
            # i is the end of any palindrome
            if dp[i-1] == 1 and s[i-1] == s[i]:
                dp[i] = 2
                if dp[i] > max_len:
                    max_i = i
                    max_len = dp[i]
            elif dp[i-1]%2==0 and s[i-dp[i-1]-1] ==s[i]:
                dp[i] = dp[i-1]+2
                if dp[i] > max_len:
                    max_i = i
                    max_len = dp[i]
            elif dp[i-1]%2==1 and s[i-dp[i-1]-1] == s[i]:
                dp[i] = dp[i-1] + 2
                if dp[i] > max_len:
                    max_i = i
                    max_len = dp[i]
            else:
                dp[i]=1


        return s[max_i-max_len:max_i+1]


str = "abcdcbabcddd"
print(Solution2.longestPalindrome("abcdcbabcddd"))


