class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m = len(nums1)
        n = len(nums2)
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i = j = 0
        res = list()
        while i < m and j < n:
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1


        return res

n1 = [1,2,2,1]
n2 = [2,2]

Solution().intersect(n1,n2)