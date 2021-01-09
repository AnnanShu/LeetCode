from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        pending, pds, end = False, 0, False 
        ans = []
        ns, ne = newInterval
        if ne < intervals[0][0]:
            ans.append([ns, ne])
            end = True 
        for ins, ine in intervals:
            if end:
                ans.append([ins, ine])
                continue 

            elif pending:
                if ins > ne:
                    ans.append([pds, ne])
                    ans.append([ins, ine])
                    end = True
                    continue
                if ine < ne:
                    continue 

                if ine >= ne:
                    ans.append([pds, ine])
                    end = True 
                    continue 
                
            else:
                if ine < ns:
                    ans.append([ins, ine])
                if ins <= ns < ne <= ine:
                    ans.append([ins, ine])
                    end = True
                if ins <= ns <= ine <= ne:
                    pds = ins 
                    pending = True 
                    continue
                if ns <= ins:
                    if ne <= ine:
                        ans.append([ns, ine])
                        end = True 
                    else:                    
                        pds = ns 
                        pending = True

        if not end:
            if pending:
                ans.append([pds, ne])
            if not pending:
                ans.append([ns, ne])

        return ans

Solution().insert([[1, 5]], [5, 7])
Solution().insert([[1, 5]], [0, 3])
Solution().insert([[1, 5]], [1, 5])
