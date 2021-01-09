class Solution:
    def codeSwitch(self, s:str):
        if len(s) < 4:
            the_type = 1
        else:
            if s[0] == 'R' and s[1].isdigit() and 'C' in s[2:]:
                the_type = 0
            else:
                the_type = 1
        
        if the_type == 0:
            row_end = s.index('C')
            row = s[1:row_end]
            col = int(s[row_end + 1:])
            # print(col)
            row_rep = []
            while col > 0:
                if col % 26:
                    row_rep.append(col % 26)
                    col = col // 26
                else:
                    row_rep.append(26)
                    col = (col // 26) -1
            # print(row_rep)
            return ''.join([chr(ord('A')  + i - 1 )for i in row_rep[::-1]]) + row
    
        if the_type == 1:
            str_end = 0
            while s[str_end].isalpha():
                str_end += 1
            col = s[:str_end]
            row = s[str_end:]
            col_num = 0
            for char in col:
                col_num = col_num * 26 + (ord(char) - ord('A') + 1)
            return 'R' + row + 'C' + str(col_num)

if __name__ == "__main__":
    n = int(input())

    for i in range(n):
        line = input().strip()
        print(Solution().codeSwitch(line))

            

Solution().codeSwitch('R23C55')
Solution().codeSwitch('BC23')

        
