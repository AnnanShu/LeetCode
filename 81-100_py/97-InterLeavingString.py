class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        print(l1, l2, l3)
        if l3 != l1 + l2:
            return False
        
        dp = [[False] * (l1+1) for _ in range(l2+1)]
        dp[0][0] = True
        cur_point = 0
        cor_fit = [(0, 0),]
        
        while cur_point < l3:
            next_fit = list()
            for x, y in cor_fit:
                if x < l2:
                    if s2[x] == s3[cur_point]:
                        dp[x+1][y] = True
                        next_fit.append((x+1, y))

                if y < l2:
                    if s1[y] == s3[cur_point]:
                        dp[x][y+1] = True
                        next_fit.append((x, y+1))
            
            if next_fit:
                cor_fit = next_fit
            else:
                return False
            
            cur_point += 1
        
        for line in dp:
            print(line)

        return dp[-1][-1]

s1 = "aabcc" 
s2 = "dbbca" 
s3 = "aadbbbaccc"
Solution().isInterleave(s1, s2, s3)



class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if not s1 and not s2 and not s3:
            return True
        elif not s1:
            return s2 == s3
        elif not s2:
            return s1 == s3
        if l3 != l1 + l2:
            return False
        
        dp = [[False] * (l1+1) for _ in range(l2+1)]
        dp[0][0] = True
        for i in range(l1):
            if s1[i] == s3[i]:
                dp[0][i+1] = True
            else:
                break

        for i in range(l2):
            if s2[i] == s3[i]:
                dp[i+1][0] = True
            else:
                break

        for i in range(l2):
            for j in range(l1):
                cursor = i + j + 1
                if cursor > l3:
                    break
                if s1[j] == s3[cursor] and s2[i] == s3[cursor]:
                    dp[i+1][j+1] = dp[i+1][j] | dp[i][j+1]
                else:
                    if s1[j] == s3[cursor]:
                        dp[i+1][j+1] = dp[i+1][j]
                    if s2[i] == s3[cursor]:
                        dp[i+1][j+1] = dp[i][j+1]
        
        for line in dp:
            print(line)
        return dp[-1][-1]


s1 = "aabcc" 
s2 = "dbbca" 
s3 = "aabdbbccca"
Solution().isInterleave(s1, s2, s3)

s1 = "aa"
s2 = "ab"
s3 = "abaa"
Solution().isInterleave(s1, s2, s3)
Solution().isInterleave("ab","bc","babc")



