from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        func_cnt = 0
        
        @lru_cache(None)
        def dp(i, j):
            nonlocal func_cnt 
            func_cnt += 1
            if i < 0 or j < 0: return 0
            if text1[i] == text2[j]: return 1 + dp(i-1, j-1) 
            if text1[i] != text2[j]: return max(dp(i-1, j), dp(i, j-1))

        ans = dp(n1-1, n2-1)   
        print(f'function_exec count: {func_cnt}')
Solution().longestCommonSubsequence('abcedfdfd', 'abcdffd')