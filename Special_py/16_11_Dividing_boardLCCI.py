"""
You are building a diving board by placing a bunch of planks of wood 
end-to-end. There are two types of planks, one of length shorter and one 
of length longer. You must use exactly K planks of wood. Write a method to 
generate all possible lengths for the diving board.

return all lengths in non-decreasing order.

"""



class Solution(object):
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        difference = longer - shorter
        res = list()
        start = shorter * k
        res.append(start)
        for i in range(1,k+1):
            res.append(start + difference*i)

        return res

shorter = 1
longer = 2
k = 3z
Solution().divingBoard(shorter, longer, k)

