from typing import List
class Solution:
    def __init__(self):
        super().__init__()
    def eraseOverlapIntervals(self, intervals: List[List[int]]):
        if not intervals:
            return 0
        intervals = sorted(intervals, key = lambda x: x[0])
        # print(intervals)
        end = intervals[0][1]
        removes = 0
        for cura, curb in intervals[1:]:
            if cura >= end:
                print(f"end:{end}, cura:{cura}")
                end = curb
                continue
            else:
                print(f"end:{end}, curb:{curb}")
                removes += 1
                end = min(end, curb)
            
        
        return removes

Solution().eraseOverlapIntervals([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]])

set(['a', 2])|(set([3, 4]))

[null,"x","x","x",true,"x","x","x","","","","",false,"","","","","",false,"","","","","",false,"","","","",false,"","","","","","","","","","","","","","","","","","","",false,"",false,"","","","","","",false,"","","","","","","","","","","","","","",false,"","","",false,"","",false,"","","","",""]
[null,"x","x","x",true,"x","x","x"," "," "," "," ",false," "," "," "," "," ",false," "," "," "," "," ",false," "," "," "," ",false," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",false," ",false," "," "," "," "," "," ",false," "," "," "," "," "," "," "," "," "," "," "," "," "," ",false," "," "," ",false," "," ",false," "," "," "," "," "]