class Solution:
    def letterCombinations(self, digits: str) -> list:
        map_dict = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        # letters = [map_dict[digit] for digit in digits]
        output = []
        def auxiliary_func(current, remaining):
            if remaining:
                for i in map_dict[remaining[0]]:
                    auxiliary_func(current+i, remaining[1:])

            else:
                output.append(current)

        auxiliary_func('', digits)
        return output

[i for i in range(60)]
print(Solution().letterCombinations('234'))

