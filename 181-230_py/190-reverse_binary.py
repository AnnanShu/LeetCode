# class Solution:
#     def reverseBits(self, n: int) -> int:
#         res = 0
#         i = 0
#         while i < 32:
#             res <<= 1
#             res += (n >> i) & 1
#             i += 1
#         return res

n = input("please input the number")
all_list = []
for i in range(int(n)):
    all_list.append(input(f"the {i}-th string is: "))
while True:
    cur = input("please enter current data (use space to split):")
    cur = cur.split(' ')
    print(all_list[int(cur[0])])
    print(all_list[int(cur[1])])

dp = [[1]*8] + [[1] + [0]*7 for _ in range(7) ]
dp
for i in range(1, 8):
    for j in range(1, 8):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

ord('1')

words = ["w","wo","wor","worl", "world", 'wa']
def key(word):
    return len(word)
words = sorted(words, key = key)
words

"1(234)567-890".split("@")

a, b, c, *d = [1,2,3,4,5,6,7]
list(map(str, [1,2,3,4,5]))
from functools import reduce
import operator
reduce(operator.mul, [1,2,3,4,5])
