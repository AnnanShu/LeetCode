#-*- encoding utf-8 -*-
# Author:Anan
class Solution:
    def combinationSum(self, candidates: list, target: int):
        candidates = sorted(candidates)
        combinations = []
        def auxiliary_func(candidates, target, queue):
            current_sum = sum(queue)
            for idx, number in enumerate(candidates):
                if number > target - current_sum:

                    break
                if number == target - current_sum:
                    queue.append(number)
                    combinations.append(queue)
                    continue
                else:
                    new_queue = queue.copy()
                    new_queue.append(number)
                    auxiliary_func(candidates[idx:], target, new_queue)

            return combinations
        combinations = auxiliary_func(candidates, target, [])

        print(combinations)

Solution().combinationSum([2,3,6,7],7)



