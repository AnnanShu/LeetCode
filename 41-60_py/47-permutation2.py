class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    

        n = len(nums)
        res = []

        def dfs(path, depth, visited):
            if depth == n:
                res.append(path[:])
            for i in range(n):
                if not visited[i]:
                    if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                        continue
                    else:
                        visited[i] = True
                        path.append(nums[i])
                        dfs(path, depth + 1, visited)
                        visited[i] = False
                        path.pop()
        
        nums = sorted(nums)
        if not nums:
            return 
        visited = [False] * n 
        dfs([], 0, visited)
        return res
    


        