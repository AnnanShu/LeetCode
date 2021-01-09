from typing import List
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        if num < 0 or num >= 10: return []
        all_times = [2**i for i in range(4)] + [2**i for i in range(6)]
        visited = [False] * 10 
        ans = []
        def is_valid(visited):
            actual_time = [visited[i] * all_times[i] for i in range(10)]
            if sum(actual_time[:4]) < 12 and sum(actual_time[4:]) < 60:
                return str(sum(actual_time[:4]))+ ':' + str(sum(actual_time[4:])).zfill(2)
            else:
                return False
        def dfs(cnt, start):
            if cnt == num:
                valid = is_valid(visited)
                if valid:
                    ans.append(valid)
            if cnt < num:
                for idx in range(start, 10):
                    if not visited[idx]:
                        visited[idx] = True 
                        dfs(cnt + 1, idx+1)
                        visited[idx] = False 
        
        dfs(0, 0)
        return ans

Solution().readBinaryWatch(3)

                        
