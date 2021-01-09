class Solution:
    def numTrees(self, n: int):
        if n>=2:
            # ranges = [i+1 for i in range(n)]
            dp = [0]*(n+1)
            dp[0], dp[1] = 1, 1 
            for i in range(2, n+1):
                total = 0
                for j in range(i):
                    left = j
                    right = i - j - 1
                    total += dp[left]*dp[right]
                dp[i] = total

            return dp[n]

        else:
            return 1

print(Solution().numTrees(3))


                
        