class Solution:
    def countAndSay(self, n: int) -> str:
        current = '1'
        cnt = 1
        while cnt < n:
            next_cur = ""
            print(current)
            inner_cnt = 0
            inner_char = ''
            for i in range(len(current)):
                if i == 0 or inner_cnt == 0:
                    inner_char = current[i]
                    inner_cnt += 1
                elif current[i] == current[i-1]:
                    inner_cnt += 1
                else:
                    next_cur += str(inner_cnt) + inner_char
                    inner_cnt = 0
            else:
                next_cur += inner_char + str(inner_cnt)
            
            current = next_cur
            
            cnt += 1
        
        return current