class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if n <= k-1:
            return max(arr)
        
        local_max = max(arr[0], arr[1])
        max_cnt = 1
        if k == 1: return local_max
        for num in arr[2:]:
            if num < local_max:
                max_cnt += 1
                if max_cnt == k: return local_max
            else:
                local_max = num
                max_cnt = 1

        return local_max