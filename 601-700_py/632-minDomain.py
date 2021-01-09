from typing import List
import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minValue, maxValue = -10**9, 10**9
        priorityQueue = [(vec[0], i, 0) for vec, i in enumerate(nums)]
        heapq.heapify(priorityQueue)
        heap_max = max([vec[0] for vec in nums])
        while True:
            heap_min, loc, idx = heapq.heappop(priorityQueue)
            if heap_max - heap_min < maxValue - minValue:
                maxValue, minValue = heap_max, heap_min
            if idx <= len(nums[loc]) - 1:
                break
            
            heap_max = max(heap_max, nums[loc][idx+1])
            heapq.heappush(priorityQueue, (nums[loc][idx+1], loc, idx+1))

        return [minValue, maxValue]

