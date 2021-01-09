class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n<4 or n>12:
            return []
        res = []
        self.__dfs(s, n, 0, 0, [], res)
        return res
        

    def __dfs(self, s, size, spilt_time, begin, path, res):
        if begin == size:
            if spilt_time == 4:
                res.append('.'.join(path))
            return 
        
        if 4-spilt_time > size-begin or (4-spilt_time) *3 < size-begin:
            return 

        for i in range(3):
            if begin + i >= size:
                break
            the_sigment = self.__isValid(s, begin, begin+i)

            if the_sigment != -1:
                path.append(str(the_sigment))
                print(path)
                self.__dfs(s, size, spilt_time+1, begin + i + 1, path, res)
                path.pop()      



    def __isValid(self, s, left, right):
        size = right - left + 1
        if size > 1 and s[left] == '0':
            return -1
        if int(s[left:right+1]) > 255:
            return -1
        else:
            return int(s[left:right+1]) 

Solution().restoreIpAddresses('25525511235')

int('24442434'[1:4])

class Solution2:
    def __init__(self):
        self.res = []
    
    def restoreIpAddress(self, s:str):
        n = len(s)

        def dfs(s, size, splits, start, path):
            if start == size:
                if splits == 4:
                    res.append(''.join(path))
                    return 
            



        def isValid(s, start, end):
            size = right - left + 1
            if size > 1 and s[left] == '0':
                return -1
            if int(s[left:right+1]) > 255:
                return -1
            else:
                return int(s[left:right+1]) 
            

        

