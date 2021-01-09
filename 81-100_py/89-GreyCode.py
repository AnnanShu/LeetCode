int('10101010',2)


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        the_list = [['0'],['1']]
        next_list = []
        if n < 2:
            return [int(''.join(i),2) for i in the_list[:n]]

        for _ in range(2, n):
            next_list = [['0'] + each for each in the_list] + [['1'] + each for each in the_list[::-1]]
            the_list = next_list 

        return [int(''.join(i),2) for i in the_list]

Solution().grayCode(3)
[int(''.join(i),2) for i in [['0'],['1']]]


