class Solution:
    def convert(self, s: str, numRows: int) -> str:
        the_list = []
        for i in range(numRows):
            the_list.append([s[i],])

        current_col = 1
        denominator = numRows-1
        current_char = numRows


        while current_char < len(s):
            remaining = current_col%denominator

            if remaining == 0:
                for i in range(numRows):
                    the_list[i].append(s[current_char])
                    current_char += 1
                current_col += 1
            else:
                for i in range(numRows):
                    if denominator - remaining - i == 0:
                        the_list[i].append(s[current_char])
                        current_char += 1

                    else:
                        the_list[i].append('.')
                current_col += 1

        return the_list


s = "LEETCODEISHIRING"
numRows = 4
(Solution().convert(s, numRows))

'SdfdfD'.lower()
ord('A')
'4'.isdigit()
'5'.islower()