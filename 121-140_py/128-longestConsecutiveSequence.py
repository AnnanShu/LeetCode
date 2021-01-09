'''
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

## easiest way to solve this question
# Time complexity: O(n^3)
# class Solution:
#     def longestConsecutive(self, nums: list) -> int:
#         longest = 1
#
#         for num in nums:
#             current_num = num
#             num_length = 1
#             while current_num+1 in nums:
#                 num_length += 1
#                 current_num += 1
#
#             longest = max(longest, num_length)
#
#         return longest
#

class Solution:
    def longestConsecutive(self, nums: list) -> int:
        num_set = set(nums)
        longest = 1
        for num in nums:
            if num-1 in num_set:
                continue
            current_length = 1
            while num + 1 in num_set:
                num += 1
                current_length += 1
            longest = max(longest, current_length)

        return longest


print(Solution().longestConsecutive([100, 4, 200, 1, 2, 3]))



