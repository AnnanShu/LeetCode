from typing import List
class Solution:
    def subsets(self, nums):
        output = [[]]
        for num in nums:
            output += [[num] + i for i in output]

        return output




class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(path, candis):
            ans.append(path[:])
            for i, candi in enumerate(candis):
                path.append(candi)
                dfs(path, candis[i+1:])
                path.pop()
    
        dfs([], nums)
        return ans


print(Solution().subsets([1,2,3]))