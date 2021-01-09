class Solution:
    def combinationSum2(self, candidates, target:int) -> list:
        sortedcan = sorted(candidates)

        for i in range(len(sortedcan) - 2):
            if i >= 1:
                if sortedcan[i] == sortedcan[i-1]:
                    continue
            

