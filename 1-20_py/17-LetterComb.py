## Letter combination of a Phone Number

class Solution:
    def letterCombinations(self, digits):
        map_dict = {
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'
        }
        for digit in digits:
            assert int(digit) in map_dict.keys(), "Please enter a valid string of number"
        output = list()
        list_contained = [map_dict[int(digit)] for digit in digits]
        n = len(digits)
        states = [0] * n
        lengths = [len(list_contained[i]) for i in range(n)]
        while True:
            if states[n-1]<lengths[n-1]:
                output.append(''.join([list_contained[fir][sed] for fir,sed in enumerate(states)]))
                states[n-1] += 1
            elif states[n-1] == lengths[n-1]:
                output.append(''.join([list_contained[fir][sed] for fir,sed in enumerate(states)]))
                modify = n-2
                while modify >= 0:
                    if states[modify]+1 <= lengths[modify]:
                        states[modify] += 1
                        states[modify+1:] = 0*[n-modify-1]
                        break
                    else:
                         modify-=1
                if modify < 0:
                    break  
            
Solution().letterCombinations('23')