class Solution:
    def intToRoman(self, num: int) -> str:
        data = 'IVXLCDM'
        level = 0
        result = list()
        while num:
            mod = num % 10
            if mod >= 1 and mod <= 3:
                for _ in range(mod):
                    current_sign = data[level*2]
                    result.append(current_sign)
            if mod == 4:
                result.append(data[level*2 + 1])
                result.append(data[level*2])
            if mod >= 5 and mod <=8:
                for _ in range(mod-5):
                    result.append(data[level*2])
                result.append(data[level*2 + 1])
                
            if mod == 9:
                result.append(data[(level + 1)*2])
                result.append(data[level*2])
                
            num = num // 10
            level += 1

        return "".join(result[::-1])

Solution().intToRoman(3999)

'a' - 'Z'
