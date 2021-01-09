
class Solution:
    def partitionLabels(self, S: str):
        last_appear = {c:i for i, c in enumerate(S)}
        prev = -1
        ans = []
        max_appear = 0
        for idx, c in enumerate(S):
            max_appear = max(last_appear[c], max_appear)
            if max_appear == idx:
                ans.append(idx - prev)
                prev = idx 
        return ans 


Solution().partitionLabels("ababcbacadefegdehijhklij")

print(enumerate("ababcbacadefegdehijhklij"))


































class Solution2:
    def partitionLabels(self, S: str):
        last = {c:i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c]) 
            if i==j:
                ans.append( j- anchor + 1)
                anchor = j + 1
            
        return ans