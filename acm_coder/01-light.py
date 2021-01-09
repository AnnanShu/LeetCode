if __name__ == "__main__":
    # lights, streetlen, *ot = list(map(int, input().split()))
    lights, streetlen = 7, 15
    # posit = list(map(int, input().split()))
    posit = [15,5,3,7,9,14,0]
    print(posit)
    posit = [0] + sorted(posit) + [streetlen]
    max_dis = posit[1] - posit[0]
    for i in range(2, len(posit)):
        print(posit)
        max_dis = max(max_dis, posit[i] - posit[i-1])
    
    print(max_dis/2)

'%.2f' %(max_dis/2)
50 10
1280930

bin(-2)
bin(2)
2 ^ -2