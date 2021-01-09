class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset = set(words)
        dp = [[True] + [False] * len(word) for word in words]
        for row, word in enumerate(words):
            n = len(word)
            for i in range(1, n+1):
                for j in range(i):
                    if dp[row][j] and (word[j:i] in wordset):
                        dp[row][i] = True
                        break
            
        
        return [words[i] for i in range(len(words)) if (dp[i][-1] and dp[i].count(True) > 3)]