class Solution:
    def subsets(self, nums):
        output = []
        n = len(nums)

        for i in range(2**n, 2**(n+1)):
            bin_mask = bin(i)[3:]

            output.append([nums[j] for j in range(n) if bin_mask[j] == '1'])


        return output

print(Solution().subsets([1,2,3]))