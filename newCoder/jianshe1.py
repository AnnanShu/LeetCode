import sys 
# A, B, C, D = list(map(int, sys.stdin.readline().split()))
A, B, C, D = 4, 4, 4, 4
ans = 0 
# if A < 1 or B < 1 or C < 1 or D < 1: return 0
def comon(a, b):
    if a == 1 or b == 1: return True 
    for divisor in range(2, a + 1):
        if a % divisor == 0 and b % divisor == 0: 
            return False 
    return True

for i in range(1, A + 1):
    for j in range(1, B + 1):
        for k in range(1, C + 1):
            for l in range(1, D + 1):
                a = (i - j) % 3 == 0
                b = (i * k) % 4 == 0 
                c = (j + k) % 5 == 0
                d = comon(i, l)
                
                
                if a and b and c and d: 
                    print(i, j, k, l)
                    ans += 1

                    
print(ans)