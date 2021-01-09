import time
class Solution:
    def threeSum(self, nums):
        solution = list()
        n = len(nums)
        s_nums = sorted(nums)
        for i in range(n-2):
            if i > 0 and s_nums[i] == s_nums[i-1]:
                continue
            # If first element >=0, break 
            if s_nums[i] > 0:
                break
            m, j = i+1, n-1
            while m < j:
                sum_3 = s_nums[i] + s_nums[m] + s_nums[j]
                if sum_3 == 0:
                    solution.append([s_nums[i], s_nums[m], s_nums[j]])
                    # First pointer shouldn't same with previous one.
                    while m+1 < j and s_nums[m] == s_nums[m+1]:
                        m += 1
                    m += 1
                    j -= 1
                elif sum_3 > 0:
                    j -= 1
                else:
                    m += 1

        return solution

solution = Solution()
l1 = [-1, 0, 1, 2, -1, -4]
print(solution.threeSum(l1))
print(Solution().threeSum(l1))
                
