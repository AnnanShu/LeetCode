import collections
from typing import List
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        n = len(values)
        labeled = collections.defaultdict(list)
        for i in range(n):
            labeled[labels[i]].append(values[i])
        new_list = [sorted(label, reverse=True)[:use_limit] for label in labeled.values()]
        print(new_list)
        planed = [each for the_list in new_list for each in the_list]
        planed = sorted(planed, reverse=True)
        print(planed)
        return sum(planed[:num_wanted])

# [5,4,3,2,1]
# [1,3,3,3,2]
# 3
# 2
Solution().largestValsFromLabels([5,4,3,2,1], [1,3,3,3,2],3, 2)
Solution().largestValsFromLabels([2,6,1,2,6], [2,2,2,1,1],1,1)
        