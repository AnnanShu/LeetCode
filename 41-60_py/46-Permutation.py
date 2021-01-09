class Solution:
    def permute(self, nums):
        permutation = []
        current_nums = []
        

        def auxiliary_func(remain_nums: list, current_nums:list,permutation):
            if len(remain_nums) < 1:
                return current_nums
            elif len(remain_nums) == 1:
                current_nums.append(remain_nums[0])
                # print(current_nums)
                permutation.append(current_nums)
            else:    
                for num in remain_nums:
                    current_nums_ = current_nums.copy()
                    remain_nums_ = remain_nums.copy()
                    remain_nums_.remove(num)
                    current_nums_.append(num)
                    auxiliary_func(remain_nums_, current_nums_,permutation)

        auxiliary_func(nums, current_nums,permutation)
        return permutation

https://stc-spadesdns.com/link/lcDfJnyaOysQuVm4?sub=1

print(Solution().permute([1,2,3]))