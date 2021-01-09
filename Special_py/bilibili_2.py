inputs = ["2 misakamikoto^aisuki",
"3 !bakabaka~ bakabaka~ 1~2~9!",
"3 3.1415926535897932384626433832795028841971693993751o582097494459211451488946419191919l91919hmmhmmahhhhhhhhhh",
"7 www.bilibili.com/av170001",
"1 111"]

import sys 
from collections import Counter
for line in inputs:
    start = 0
    while line[start].isdigit():
        start += 1
    n = int(line[:start])
    s = line[1:].replace(" ", "")
    cnt = 0
    the_c = ''
    cntr = Counter(s)
    for c in s:
        if cntr[c] == 1:
            cnt += 1
            if cnt == n:
                the_c = c
                break 
    
    if cnt == n:
        print('['+ the_c + ']')
    else:
        print('Myon~')

