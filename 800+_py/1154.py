import itertools
class Solution:
    def dayOfYear(self, date: str):
        year = int(date[:4])
        mons = int(date[5:7])
        days = int(date[8:])
        moon = False
        if year % 100 == 0:
            moon = year % 400 == 0
        else:
            moon = year % 4 == 0
        
        monday = [31, 28+moon, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        print(f"year:{year}, month:{mons}, day:{days}, moon:{moon}")
        if mons > 1:
            return list(itertools.accumulate(monday[:mons-1]))[-1] + days
        else:
            return days

Solution().dayOfYear("2003-03-01")