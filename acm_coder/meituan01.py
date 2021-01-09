# class Solution:
#     def fdfd(self, memo):

the_num = 10000
if __name__ == "__main__":
    the_num = int(input())
    cnt = 0
    res = []
    i = 10
    while i < the_num:
        strify = str(i)
        if i == 4 * int(strify[::-1]):
            cnt += 1
            res.append((int(strify[::-1]), i))
        
        i += 1

    print(cnt)
    for each in res:
        print(each[0], each[1])

int('0011')
        